#!/usr/bin/env python3
"""Segmenty před/po rekalibraci: řádkový rozdíl červencové a finální verze tabulek K3.

Proč: rekalibrace škály Vhodnost proběhla uprostřed finálního kódování (podklady
15. 7. 2026). Finální tabulky nenesou čas hodnocení ani příznak zpětného přepisu,
takže segmenty „před“ a „po“ nelze určit z nich samotných. Záloha dat z 22. 7. 2026
však obsahuje tehdejší verzi týchž tabulek (04-final-1905), a rozdíl řádek po řádku
segmenty rekonstruuje:

  beze_zmeny  — kazuistika byla ohodnocena už v červenci a hodnocení se nezměnilo
                → hodnoceno PŘED rekalibrací a rekalibrací nedotčeno
  zmeneno     — ohodnocena v červenci, ale hodnocení se ve finále liší
                → zpětný přepis (typicky po projednání)
  jen_finale  — v červenci ještě nebyla ohodnocena
                → hodnoceno PO rekalibraci

Vstupy:  data/raw/k3-kvalita-kazuistik-2026/{04-final-1905,05-final-freeze-2026-09-08}/
         tabulky obou anotátorek (parsování sdílené s 27_k3_freeze.py)
Výstup:  data/processed/k3_segmenty.csv — 1 řádek = kazuistika × anotátorka, bez textů:
         case_uid, anotator, segment, kvalita_cervenec, dopad_cervenec, vhodnost_cervenec,
         kvalita, dopad, vhodnost (finál), zmena_kvalita/dopad/vhodnost (0/1), adjudikovano

Kontrola: skript zároveň přepočítá červencový monitorovací bod (překryv, hrubá shoda
a vážená κ vhodnosti, průměry, směr neshod). Pokud se shoduje s hodnotami v podkladech
sladění (n = 239; 45,3 %; wκ = 0,415; 3,49 vs. 2,95; 120 ze 128), je červencová verze
skutečně stavem před rekalibrací a segmenty jsou platné.

Míry shody po segmentech počítá notebook 40_kvalita.qmd (bootstrapové intervaly);
tento skript čísla do knihy nedodává.

Spuštění: python habilitace-2/analyzy/scripts/28_k3_segmenty.py
"""
from __future__ import annotations

import importlib
import sys
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
m27 = importlib.import_module("27_k3_freeze")

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "data" / "raw" / "k3-kvalita-kazuistik-2026"
PROC = ROOT / "data" / "processed"
CERVENEC = RAW / "04-final-1905"          # stav v záloze z 22. 7. 2026
FINAL = RAW / "05-final-freeze-2026-09-08"  # řez K3_freeze_2026-09-08
DIMS = ("kvalita", "dopad", "vhodnost")


def nacti(dirpath: Path, f2u: dict[str, str], adj: dict[str, set[str]]) -> pd.DataFrame:
    """Načte obě tabulky z dané složky přesně tak jako 27_k3_freeze.py."""
    m27.K3_DIR = dirpath
    rows: list[dict] = []
    for name in m27.PSEUDO:                   # mapování drží neveřejný modul 27
        rows += m27.nacti_anotatorku(name, f2u, adj)
    df = pd.DataFrame(rows)
    return df.drop_duplicates(subset=["anotator", "_nt"], keep="first")


def kontrola_cervenec(J: pd.DataFrame) -> None:
    """Přepočet červencového monitorovacího bodu (musí sedět na podklady sladění)."""
    piv = J.pivot_table(index="_nt", columns="anotator", values="vhodnost", aggfunc="first")
    piv = piv.dropna(subset=[c for c in ("A12", "A2") if c in piv.columns])
    if not {"A12", "A2"}.issubset(piv.columns):
        print("KONTROLA: v červencové verzi chybí jedna z anotátorek")
        return
    a, b = piv["A12"].astype(int), piv["A2"].astype(int)
    n = len(piv)
    presna = float((a == b).mean())
    neshod = int((a != b).sum())
    a2_vyssi = int((b > a).sum())
    # kvadraticky vážená κ (shodně s 08_shoda_final.weighted_kappa)
    kappa = m27_weighted_kappa(list(zip(a, b)))
    print(f"KONTROLA červencového bodu: překryv {n} kazuistik; hrubá shoda {presna:.3f}; "
          f"vážená κ {kappa:.4f}; průměry A12 {a.mean():.2f} / A2 {b.mean():.2f}; "
          f"A2 výš u {a2_vyssi} z {neshod} neshod")
    print("  (podklady sladění 15. 7. 2026: 239; 0,453; 0,4154; 2,95 / 3,49; 120 ze 128)")

    dop = J.pivot_table(index="_nt", columns="anotator", values="dopad", aggfunc="first").dropna()
    if {"A12", "A2"}.issubset(dop.columns):
        print(f"  dopad: n {len(dop)}, hrubá shoda {(dop['A12'] == dop['A2']).mean():.3f}")


def m27_weighted_kappa(pairs: list[tuple[int, int]]) -> float:
    """Kvadraticky vážená Cohenova κ pro škálu 1–4."""
    kat = list(range(1, 5))
    k = len(kat)
    idx = {c: i for i, c in enumerate(kat)}
    n = len(pairs)
    obs = [[0.0] * k for _ in range(k)]
    for x, y in pairs:
        obs[idx[x]][idx[y]] += 1 / n
    px = [sum(obs[i]) for i in range(k)]
    py = [sum(obs[i][j] for i in range(k)) for j in range(k)]
    num = den = 0.0
    for i in range(k):
        for j in range(k):
            w = ((i - j) / (k - 1)) ** 2
            num += w * obs[i][j]
            den += w * px[i] * py[j]
    return 1 - num / den if den else float("nan")


def main() -> None:
    if not CERVENEC.exists():
        sys.exit(f"CHYBA: červencová verze tabulek chybí ({CERVENEC}); obnov ji ze zálohy")
    f2u = m27.fp2uid_map()
    adj = m27.adjudikovane()
    J = nacti(CERVENEC, f2u, adj)
    F = nacti(FINAL, f2u, adj)
    print(f"červenec (22. 7. 2026): {len(J)} ohodnocených řádků "
          f"(A12 {int((J.anotator == 'A12').sum())}, A2 {int((J.anotator == 'A2').sum())})")
    print(f"finál ({m27.FREEZE}): {len(F)} ohodnocených řádků "
          f"(A12 {int((F.anotator == 'A12').sum())}, A2 {int((F.anotator == 'A2').sum())})")
    kontrola_cervenec(J)

    jul = J.set_index(["anotator", "_nt"])[list(DIMS)]
    out_rows: list[dict] = []
    for _, r in F.iterrows():
        key = (r["anotator"], r["_nt"])
        rec = {"case_uid": r["case_uid"], "anotator": r["anotator"],
               "adjudikovano": int(r["adjudikovano"])}
        for d in DIMS:
            rec[d] = r[d]
        if key in jul.index:
            j = jul.loc[key]
            zmen = 0
            for d in DIMS:
                jv, fv = j[d], r[d]
                rec[f"{d}_cervenec"] = jv
                same = (pd.isna(jv) and pd.isna(fv)) or (jv == fv)
                rec[f"zmena_{d}"] = 0 if same else 1
                zmen += rec[f"zmena_{d}"]
            rec["segment"] = "beze_zmeny" if zmen == 0 else "zmeneno"
        else:
            for d in DIMS:
                rec[f"{d}_cervenec"] = None
                rec[f"zmena_{d}"] = None
            rec["segment"] = "jen_finale"
        out_rows.append(rec)

    S = pd.DataFrame(out_rows)
    cols = (["case_uid", "anotator", "segment", "adjudikovano"]
            + [c for d in DIMS for c in (d, f"{d}_cervenec", f"zmena_{d}")])
    S[cols].to_csv(PROC / "k3_segmenty.csv", index=False)

    print("\nsegmenty (řádky finálního řezu):")
    for seg, g in S.groupby("segment"):
        print(f"  {seg}: {len(g)} (A12 {int((g.anotator == 'A12').sum())}, "
              f"A2 {int((g.anotator == 'A2').sum())})")
    zm = S[S["segment"] == "zmeneno"]
    if len(zm):
        print("  z toho změněná dimenze: " + ", ".join(
            f"{d} {int(zm[f'zmena_{d}'].sum())}" for d in DIMS))
        print(f"  změněné a zároveň projednané v podkladech: {int(zm['adjudikovano'].sum())}")

    # kolik kazuistik má v překryvu obě anotátorky ve stejném segmentu
    piv = S.pivot_table(index="case_uid", columns="anotator", values="segment",
                        aggfunc="first").dropna()
    if {"A12", "A2"}.issubset(piv.columns):
        stejny = piv[piv["A12"] == piv["A2"]]
        print(f"\npřekryv s case_uid: {len(piv)} kazuistik; obě anotátorky ve stejném segmentu: "
              f"{len(stejny)}")
        print(stejny["A12"].value_counts().to_string())
    print(f"\nvýstup: {PROC / 'k3_segmenty.csv'}")


if __name__ == "__main__":
    main()
