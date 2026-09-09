#!/usr/bin/env python3
"""Predikční experiment Studie 4 (oddíl 8.6): předpoví jazykový model dopad řešení?

Úloha: model dostane Popis situace + Anamnézu + Řešení a má určit dopad řešení
(Neúspěch / Krátkodobý nebo částečný úspěch / Dlouhodobý úspěch) podle definic třetí
etapy (příloha A.3). **Popis výstupu do promptu NIKDY nevstupuje** (kontroluje assert
i test úniku informace, jehož výsledek se ukládá do manifestu).

Poskytovatel: e-INFRA CZ (https://llm.ai.e-infra.cz/v1, OpenAI-kompatibilní API).
Důvod volby: české pedagogické texty zůstávají v národní akademické infrastruktuře
a modely jsou s otevřenými vahami, takže běh je opakovatelný i mimo tento projekt.
e-INFRA negarantuje, že nasazená verze modelu zůstane stejná, proto skript ukládá
otisk nasazení (odpověď na pevnou kontrolní otázku při teplotě 0) a datum běhu.

Uspořádání (pre-spec, PLAN §5):
  * vývojová množina  = kazuistiky mimo překryv (výběr modelu, ladění promptu)
  * hodnoticí množina = dvojitě kódovaný překryv BEZ kazuistik projednaných na
    rekalibrační schůzce; predikce se srovnává zvlášť s A12, s A2 a s podmnožinou,
    na níž se anotátorky shodly (konsenzuální štítek)
  * primární metriky: vyvážená přesnost a makro-F1; prostá přesnost pro srovnatelnost;
    referenční rámec: většinová třída a shoda anotátorek mezi sebou
  * varianty promptu: zero-shot (primární) a few-shot se šesti příklady z vývojové
    množiny (sekundární)

Použití:
  export EINFRA_API_TOKEN=...            # klíč z https://chat.ai.e-infra.cz → API keys
  python 26_k3_predikce_llm.py --models glm-5.3,kimi-k3,qwen3.5-int4 --set dev --n 120
  python 26_k3_predikce_llm.py --models glm-5.3 --set eval            # finální běh
  python 26_k3_predikce_llm.py --models glm-5.3 --set eval --shots 6  # few-shot varianta

Výstupy:
  data/processed/k3_predikce_raw.csv        predikce (case_uid, model, varianta, predikce;
                                            BEZ textů kazuistik)
  vystupy/tabulky/kap8_predikce_cisla.csv   manifest čísel pro kapitolu 8
  analyzy/vystupy/predikce/cache.jsonl      keš odpovědí (klíč = sha256 promptu, bez textu)
"""
from __future__ import annotations

import argparse
import hashlib
import importlib
import json
import os
import random
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path

import pandas as pd
import requests

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
m27 = importlib.import_module("27_k3_freeze")

ROOT = Path(__file__).resolve().parents[2]
PROC = ROOT / "data" / "processed"
TAB = ROOT / "vystupy" / "tabulky"
OUT = ROOT / "analyzy" / "vystupy" / "predikce"
K3_DIR = ROOT / "data" / "raw" / "k3-kvalita-kazuistik-2026" / "05-final-freeze-2026-09-08"
BASE_URL = os.environ.get("EINFRA_BASE_URL", "https://llm.ai.e-infra.cz/v1")
TOKEN_ENV = "EINFRA_API_TOKEN"
SEED = 20260714
FREEZE = "K3_freeze_2026-09-08"

TRIDY = {"NEU": "Neúspěch", "KU": "Krátkodobý úspěch", "DU": "Dlouhodobý úspěch"}
# operacionalizace třetí etapy (příloha A.3), zkráceně a doslovně v klíčových formulacích
INSTRUKCE = """Jsi zkušená posuzovatelka pedagogických kazuistik. Dostaneš popis situace
ve škole, anamnézu žáka a popis toho, jak učitel situaci řešil. Popis výsledku k dispozici
nemáš; tvým úkolem je odhadnout, jak řešení podle všeho dopadlo.

Vyber právě jednu z těchto tří možností:
NEU = neúspěch: problém trvá dál nebo se zhoršil, řešení nepomohlo.
KU = krátkodobý nebo částečný úspěch: situace se zklidnila jen na čas nebo jen zčásti.
DU = dlouhodobý úspěch: problém se podařilo vyřešit a změna vydržela.

Odpověz jediným slovem: NEU, KU, nebo DU."""


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def token() -> str:
    t = os.environ.get(TOKEN_ENV, "").strip()
    if not t:
        sys.exit(f"CHYBA: chybí {TOKEN_ENV} (klíč z https://chat.ai.e-infra.cz → API keys)")
    return t


# ---------------------------------------------------------------- data
def nacti_kazuistiky() -> pd.DataFrame:
    """Texty částí kazuistik z tabulek řezu (drží se jen v paměti, nikam se neukládají)."""
    from openpyxl import load_workbook
    f2u = m27.fp2uid_map()
    rows = []
    for name, pseudo in m27.PSEUDO.items():   # mapování drží neveřejný modul 27
        ws = load_workbook(K3_DIR / f"Tabulka anotování celá_ {name} v2.xlsx",
                           read_only=True, data_only=True)["List 1"]
        for r in ws.iter_rows(values_only=True):
            r = list(r)[:8] + [None] * 8
            popis = r[1]
            if not popis or str(popis).strip() == "Popis" or len(str(popis).strip()) < 40:
                continue
            uid = f2u.get(m27.fp(popis))
            if not uid:
                continue
            rows.append({"case_uid": uid, "anotator": pseudo,
                         "popis": str(popis), "anamneza": str(r[2] or ""),
                         "reseni": str(r[3] or ""), "vystup": str(r[4] or ""),
                         "dopad": (str(r[6]).strip() if r[6] else None)})
    df = pd.DataFrame(rows).drop_duplicates(subset=["case_uid", "anotator"], keep="first")
    return df


def mnoziny(texty: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """(vývojová, hodnoticí) — hodnoticí = překryv bez projednaných kazuistik."""
    W = pd.read_csv(PROC / "k3_wide.csv")
    W = W[W["case_uid"].notna()]
    dop = W[W["dopad"].notna()]
    poc = dop.groupby("case_uid")["anotator"].nunique()
    adj = W.groupby("case_uid")["adjudikovano"].max()
    prekryv = set(poc[poc == 2].index)
    projednane = set(adj[adj == 1].index)
    eval_uids = prekryv - projednane
    dev_uids = set(poc[poc == 1].index) - projednane

    base = texty.drop_duplicates("case_uid")[["case_uid", "popis", "anamneza", "reseni", "vystup"]]
    wide = dop.pivot_table(index="case_uid", columns="anotator", values="dopad",
                           aggfunc="first")
    wide.columns = [f"dopad_{c}" for c in wide.columns]
    ev = base[base.case_uid.isin(eval_uids)].merge(wide, on="case_uid", how="inner")
    dv = base[base.case_uid.isin(dev_uids)].merge(wide, on="case_uid", how="inner")
    dv["dopad"] = dv[["dopad_A12", "dopad_A2"]].bfill(axis=1).iloc[:, 0]
    return dv, ev


def prompt(row: pd.Series, priklady: list[tuple[str, str]]) -> list[dict]:
    zprava = [{"role": "system", "content": INSTRUKCE}]
    for text, stitek in priklady:
        zprava += [{"role": "user", "content": text},
                   {"role": "assistant", "content": stitek}]
    telo = (f"POPIS SITUACE:\n{row['popis']}\n\nANAMNÉZA:\n{row['anamneza']}\n\n"
            f"ŘEŠENÍ:\n{row['reseni']}")
    zprava.append({"role": "user", "content": telo})
    return zprava


def test_uniku(zpravy: list[dict], vystup: str) -> bool:
    """True = v promptu není nic z popisu výstupu (kontrola na 60 znacích)."""
    v = re.sub(r"\s+", " ", str(vystup or "")).strip()
    if len(v) < 60:
        return True
    text = " ".join(re.sub(r"\s+", " ", m["content"]) for m in zpravy)
    return v[:60] not in text


# ---------------------------------------------------------------- API
class Klient:
    def __init__(self, model: str, cache: Path):
        self.model = model
        self.cache_path = cache
        self.cache: dict[str, str] = {}
        if cache.exists():
            for line in cache.open(encoding="utf-8"):
                try:                       # souběžný zápis z více vláken může řádek porušit
                    r = json.loads(line)
                except json.JSONDecodeError:
                    continue
                self.cache[r["k"]] = r["v"]
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Bearer {token()}"})

    def zeptej(self, zpravy: list[dict], max_tokens: int = 256) -> str:
        klic = sha(self.model + json.dumps(zpravy, ensure_ascii=False) + str(max_tokens))
        if klic in self.cache:
            return self.cache[klic]
        payload = {"model": self.model, "messages": zpravy, "temperature": 0,
                   "max_tokens": max_tokens}
        odpoved = ""
        for pokus in range(4):
            try:
                r = self.session.post(f"{BASE_URL}/chat/completions", json=payload, timeout=180)
                if r.status_code == 429:
                    time.sleep(6 * (pokus + 1))
                    continue
                r.raise_for_status()
                odpoved = (r.json()["choices"][0]["message"].get("content") or "").strip()
                if odpoved:
                    break
                payload["max_tokens"] = min(4096, payload["max_tokens"] * 8)  # modely, které přemýšlejí
            except requests.RequestException:
                time.sleep(4 * (pokus + 1))
        with self.cache_path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps({"k": klic, "v": odpoved}, ensure_ascii=False) + "\n")
        self.cache[klic] = odpoved
        return odpoved

    def otisk(self) -> str:
        """Otisk nasazení: hash odpovědi na pevnou otázku při teplotě 0.

        e-INFRA nasazení neverzuje, takže „glm-5.3" dnes a za měsíc nemusí být totéž.
        Otázka musí být dost otevřená, aby se odpovědi modelů lišily; faktický dotaz
        („hlavní město Norska") vrací u všech totéž a nic nerozliší.
        """
        z = [{"role": "user", "content":
              "Napiš přesně tři věty o tom, proč je obloha modrá. Bez úvodu a bez odrážek."}]
        return sha(self.zeptej(z, max_tokens=256))[:16]


def parsuj(text: str) -> str | None:
    """Kód z odpovědi: nejprve zkratka, pak české slovo, nakonec zkrácené „NE"."""
    t = (text or "").strip().upper()
    for k in ("NEU", "KU", "DU"):
        if re.search(rf"\b{k}\b", t):
            return k
    if "DLOUHODOB" in t:
        return "DU"
    if "KRÁTKODOB" in t or "KRATKODOB" in t or "ČÁSTEČ" in t or "CASTEC" in t:
        return "KU"
    if "NEÚSPĚCH" in t or "NEUSPECH" in t or t.startswith("NE"):
        return "NEU"
    return None


# ---------------------------------------------------------------- metriky
def metriky(y_true: list[str], y_pred: list[str]) -> dict[str, float]:
    from sklearn.metrics import (balanced_accuracy_score, cohen_kappa_score, f1_score,
                                 recall_score)
    par = [(t, p) for t, p in zip(y_true, y_pred) if p is not None]
    t = [a for a, _ in par]
    p = [b for _, b in par]
    if not par:
        return {}
    tridy = ["NEU", "KU", "DU"]
    out = {
        "n": len(par),
        "acc": sum(a == b for a, b in par) / len(par),
        "bal_acc": balanced_accuracy_score(t, p),
        "macro_f1": f1_score(t, p, average="macro", labels=tridy, zero_division=0),
        "kappa": cohen_kappa_score(t, p, labels=tridy),
    }
    rec = recall_score(t, p, average=None, labels=tridy, zero_division=0)
    for k, v in zip(tridy, rec):
        out[f"recall_{k}"] = float(v)
    return out


KOD = {"Neúspěch": "NEU", "Krátkodobý úspěch": "KU", "Dlouhodobý úspěch": "DU"}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", required=True, help="čárkou oddělené id modelů na e-INFRA")
    ap.add_argument("--set", choices=["dev", "eval"], default="dev")
    ap.add_argument("--n", type=int, default=0, help="omezit počet kazuistik (0 = vše)")
    ap.add_argument("--shots", type=int, default=0, help="počet příkladů v promptu")
    ap.add_argument("--concurrency", type=int, default=3)
    args = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)

    texty = nacti_kazuistiky()
    dev, ev = mnoziny(texty)
    print(f"vývojová množina {len(dev)} kazuistik; hodnoticí množina {len(ev)} kazuistik "
          f"(překryv bez projednaných)")
    data = dev if args.set == "dev" else ev
    rnd = random.Random(SEED)
    idx = list(range(len(data)))
    rnd.shuffle(idx)
    priklady_idx = idx[:args.shots] if args.set == "dev" else []
    if args.shots and args.set == "eval":  # příklady VŽDY mimo hodnoticí množinu
        dev_idx = list(range(len(dev)))
        rnd.shuffle(dev_idx)
        priklady = [( f"POPIS SITUACE:\n{dev.iloc[i]['popis']}\n\nANAMNÉZA:\n"
                      f"{dev.iloc[i]['anamneza']}\n\nŘEŠENÍ:\n{dev.iloc[i]['reseni']}",
                      KOD.get(dev.iloc[i]["dopad"], "KU"))
                     for i in dev_idx[:args.shots]]
    else:
        priklady = [(f"POPIS SITUACE:\n{data.iloc[i]['popis']}\n\nANAMNÉZA:\n"
                     f"{data.iloc[i]['anamneza']}\n\nŘEŠENÍ:\n{data.iloc[i]['reseni']}",
                     KOD.get(data.iloc[i].get("dopad", ""), "KU")) for i in priklady_idx]
        idx = idx[args.shots:]
    if args.n:
        idx = idx[:args.n]
    vyber = data.iloc[sorted(idx)].reset_index(drop=True)
    varianta = "few_shot" if args.shots else "zero_shot"

    # Test úniku informace: kazuistiky, jejichž popis výstupu se objevuje v zadání
    # (posunuté sloupce ve zdrojové tabulce), se z hodnocení vyřazují.
    ciste = [i for i in range(len(vyber))
             if test_uniku(prompt(vyber.iloc[i], priklady), vyber.iloc[i]["vystup"])]
    n_unik = len(vyber) - len(ciste)
    if n_unik:
        print(f"test úniku: vyřazeno {n_unik} kazuistik (výstup se objevuje v zadání)")
    vyber = vyber.iloc[ciste].reset_index(drop=True)
    print(f"běh: {args.set}, {len(vyber)} kazuistik, varianta {varianta}")

    zaznamy = []
    for model in args.models.split(","):
        model = model.strip()
        kl = Klient(model, OUT / f"cache_{re.sub(r'[^a-z0-9.-]', '_', model.lower())}.jsonl")
        otisk = kl.otisk()
        zpravy = [prompt(vyber.iloc[i], priklady) for i in range(len(vyber))]
        assert all(test_uniku(z, vyber.iloc[i]["vystup"]) for i, z in enumerate(zpravy)), \
            "ÚNIK: prompt obsahuje popis výstupu"
        t0 = time.time()
        with ThreadPoolExecutor(max_workers=args.concurrency) as ex:
            odpovedi = list(ex.map(kl.zeptej, zpravy))
        pred = [parsuj(o) for o in odpovedi]
        print(f"{model}: {len(vyber)} dotazů za {time.time() - t0:.0f} s; "
              f"nerozparsováno {sum(p is None for p in pred)}; otisk {otisk}")
        for i in range(len(vyber)):
            r = vyber.iloc[i]
            zaznamy.append({"case_uid": r["case_uid"], "model": model, "varianta": varianta,
                            "mnozina": args.set, "predikce": pred[i], "otisk_nasazeni": otisk,
                            "dopad_A12": KOD.get(r.get("dopad_A12"), None),
                            "dopad_A2": KOD.get(r.get("dopad_A2"), None),
                            "datum": date.today().isoformat()})
    Z = pd.DataFrame(zaznamy)
    raw = PROC / "k3_predikce_raw.csv"
    if raw.exists():
        stare = pd.read_csv(raw)
        Z = pd.concat([stare[~stare.set_index(["case_uid", "model", "varianta", "mnozina"]).index
                             .isin(Z.set_index(["case_uid", "model", "varianta", "mnozina"]).index)],
                       Z], ignore_index=True)
    Z.to_csv(raw, index=False)

    # ---- vyhodnocení
    radky = []
    for (model, var), g in Z[Z["mnozina"] == args.set].groupby(["model", "varianta"]):
        for ref in ("A12", "A2"):
            sl = g[g[f"dopad_{ref}"].notna()]
            m = metriky(list(sl[f"dopad_{ref}"]), list(sl["predikce"]))
            for k, v in m.items():
                radky.append({"model": model, "varianta": var, "reference": ref,
                              "metrika": k, "hodnota": round(float(v), 4)})
        if args.set == "eval":
            sh = g[(g["dopad_A12"].notna()) & (g["dopad_A12"] == g["dopad_A2"])]
            m = metriky(list(sh["dopad_A12"]), list(sh["predikce"]))
            for k, v in m.items():
                radky.append({"model": model, "varianta": var, "reference": "konsenzus",
                              "metrika": k, "hodnota": round(float(v), 4)})
    V = pd.DataFrame(radky)
    vysl = OUT / f"vysledky_{args.set}_{varianta}.csv"
    V.to_csv(vysl, index=False)
    print("\n" + V.pivot_table(index=["model", "varianta"], columns=["reference", "metrika"],
                               values="hodnota").to_string())
    print(f"\nvýstupy: {raw}, {vysl}")
    print("manifest kap8_predikce_cisla.csv se zapisuje až finálním během (--set eval).")

    if args.set == "eval":
        man = []
        ref_dop = Z[(Z["mnozina"] == "eval")]
        vetsina = ref_dop["dopad_A12"].value_counts(normalize=True)
        man.append({"metric": "predikce_majorita_podil", "value": round(float(vetsina.iloc[0]), 4)})
        man.append({"metric": "predikce_n_eval", "value": int(ref_dop["case_uid"].nunique())})
        man.append({"metric": "predikce_leakage_test_ok", "value": 1})
        man.append({"metric": "predikce_vyrazeno_unik", "value": n_unik})
        man.append({"metric": "predikce_majorita_bal_acc", "value": round(1 / 3, 4)})
        # lidský strop v týchž metrikách: A2 jako „predikce" proti A12 jako referenci
        par = ref_dop.drop_duplicates("case_uid")
        par = par[par["dopad_A12"].notna() & par["dopad_A2"].notna()]
        for k, v in metriky(list(par["dopad_A12"]), list(par["dopad_A2"])).items():
            man.append({"metric": f"predikce_clovek_clovek_{k}", "value": round(float(v), 4)})
        man.append({"metric": "predikce_seed", "value": SEED})
        for _, r in V.iterrows():
            slug = re.sub(r"[^a-z0-9]+", "_", f"{r.model}_{r.varianta}_{r.reference}_{r.metrika}".lower())
            man.append({"metric": f"predikce_{slug}", "value": r.hodnota})

        # rozdělení predikcí vs. lidské rozdělení + chování na sporných kazuistikách
        for (mm, vv), g in ref_dop.groupby(["model", "varianta"]):
            g = g.dropna(subset=["dopad_A12", "dopad_A2"])
            ms = re.sub(r"[^a-z0-9]+", "_", f"{mm}_{vv}".lower())
            for tr in ("NEU", "KU", "DU"):
                man.append({"metric": f"predikce_{ms}_podil_pred_{tr.lower()}",
                            "value": round(float((g["predikce"] == tr).mean()), 4)})
            shoda = g[g["dopad_A12"] == g["dopad_A2"]]
            nesh = g[g["dopad_A12"] != g["dopad_A2"]]
            man.append({"metric": f"predikce_{ms}_konsenzus_trefa",
                        "value": round(float((shoda["predikce"] == shoda["dopad_A12"]).mean()), 4)})
            man.append({"metric": f"predikce_{ms}_sporne_n", "value": int(len(nesh))})
            trefa = (nesh["predikce"] == nesh["dopad_A12"]) | (nesh["predikce"] == nesh["dopad_A2"])
            man.append({"metric": f"predikce_{ms}_sporne_jedna_ze_dvou",
                        "value": round(float(trefa.mean()), 4)})
        # lidské rozdělení pro srovnání (tytéž kazuistiky)
        par2 = ref_dop.drop_duplicates("case_uid").dropna(subset=["dopad_A12", "dopad_A2"])
        for ref in ("A12", "A2"):
            for tr in ("NEU", "KU", "DU"):
                man.append({"metric": f"predikce_podil_{ref.lower()}_{tr.lower()}",
                            "value": round(float((par2[f"dopad_{ref}"] == tr).mean()), 4)})
        pd.DataFrame(man).to_csv(TAB / "kap8_predikce_cisla.csv", index=False)
        print(f"manifest: {TAB / 'kap8_predikce_cisla.csv'} ({len(man)} metrik)")


if __name__ == "__main__":
    main()
