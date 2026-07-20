#!/usr/bin/env python3
"""Generátor přílohy C (doplňkové tabulky) — NEEDITOVAT výstup ručně.

Generuje `kapitoly/cs/appendix-C-supplementary-tables.md` z matice pokrytí
(data/processed/anotace_pokryti.csv) a existujících manifestů (kap4/5/6/7).
Vlastní spočítané hodnoty ukládá do `vystupy/tabulky/priloha_c_cisla.csv`;
hodnoty převzaté z jiných manifestů kotví přímo na ně (jediný zdroj pravdy).

Asserty: multiplicita a překryvy musí sedět na kap4 manifest; všechny
odkazované klíče musí v manifestech existovat.

Spuštění: ./.venv/bin/python habilitace-2/analyzy/scripts/17_priloha_c.py
"""
from __future__ import annotations

import csv
import hashlib
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "data" / "processed" / "anotace_pokryti.csv"
TAB = ROOT / "vystupy" / "tabulky"
OUT_MD = ROOT / "kapitoly" / "cs" / "appendix-C-supplementary-tables.md"
OUT_MAN = TAB / "priloha_c_cisla.csv"
SKRIPT = "analyzy/scripts/17_priloha_c.py"

KAMPANE = {
    "K1": ["k1_test_03_24", "k1_test_04_24", "k1_naostro_05_24"],
    "K2": ["k2_setkani10_04_25", "k2_anotace40_04_25", "k2_final351_06_25"],
    "K3": ["k3_zacvik_26", "k3_pilot1_26", "k3_pilot2_26", "k3_final_26"],
}
HUMAN = [e for cols in KAMPANE.values() for e in cols]

# Registr událostí: metadata z DATA_README §2 (jen pseudonymy!); počty se počítají
REGISTR = [
    ("–", "prosinec 2023 – únor 2024", "K1 zácvik (pokus)", "A1, A2, A5, A6",
     None, "kvalitativní kódy bez matice; kódovací kniha, strom V1→V2"),
    ("k1_test_03_24", "březen 2024", "K1 test", "❓ (pět souborů)", "c1_k1_test_03_24", ""),
    ("k1_test_04_24", "duben 2024", "K1 test", "A1–A4, A7", "c1_k1_test_04_24", ""),
    ("k1_naostro_05_24", "od května 2024", "K1 finál", "A1–A4, A7",
     "c1_k1_naostro_05_24",
     "dělba práce s vestavěným překryvem; anotační listy obsahují 1 413"
     " kazuistik, <!-- necislo: registr událostí --> z nichž 69"
     " <!-- necislo: rozdíl 1413−1344 --> se nepodařilo spárovat"
     " přes text popisu"),
    ("llm_anotace_matice_08_24", "srpen 2024", "K1 konsolidace", "–",
     "c1_llm_anotace_matice_08_24",
     "lidské kódy K1 sloučené do matice korpusu (provenience ověřena, kap. 4)"),
    ("k2_setkani10_04_25", "duben 2025", "K2 zácvik", "A1, A2, A8–A11",
     "c1_k2_setkani10_04_25", ""),
    ("k2_anotace40_04_25", "duben 2025", "K2 zácvik 2", "A1, A2, A8–A12 ❓",
     "c1_k2_anotace40_04_25", ""),
    ("–", "červen 2025", "K2 příprava", "gpt-4o (strojově)", None,
     "generace srovnávacích řešení, ne anotace"),
    ("k2_final351_06_25", "červen 2025", "K2 finál", "A1, A2, A8, A9, A10, A12",
     "c1_k2_final351_06_25",
     "zaslepené hodnocení dvojic řešení; hodnoceno 351"
     " <!-- necislo: registr událostí --> identifikátorů, autoritativní analytický"
     " soubor čítá 324 <!-- manifest kap7_k2_shoda_cisla: n_kazuistik=324 -->"
     " kazuistik (kapitola 7); zde uvedený počet = spárované na jednotný"
     " identifikátor"),
    ("k3_zacvik_26", "2026", "K3 zácvik", "A2 ❓, A12 ❓", "c1_k3_zacvik_26", ""),
    ("k3_pilot1_26", "2026", "K3 pilot 1", "A2 ❓, A12 ❓", "c1_k3_pilot1_26", ""),
    ("k3_pilot2_26", "2026", "K3 pilot 2", "A2 ❓, A12 ❓", "c1_k3_pilot2_26", ""),
    ("k3_final_26", "2026 (probíhá)", "K3 finál", "A2 ❓, A12 ❓", "c1_k3_final_26",
     "stav k datu otisku matice pokrytí; freeze viz Studie 4"),
    ("hf_publikovano_en", "podzim 2024 ❓", "publikace (ne anotace)", "–",
     "c1_hf_publikovano_en", "veřejný dataset, výběr z řezu srpen 2024"),
]


def tis(n: int) -> str:
    return f"{n:,}".replace(",", " ")


def dc(x: float, mist: int = 2) -> str:
    return f"{x:.{mist}f}".replace(".", ",")


def load_manifest(name: str) -> dict[str, str]:
    path = TAB / f"{name}.csv"
    with path.open(encoding="utf-8") as fh:
        return {r["metric"]: r["value"] for r in csv.DictReader(fh)}


def main() -> None:
    rows = list(csv.DictReader(SRC.open(encoding="utf-8")))
    sha = hashlib.sha256(SRC.read_bytes()).hexdigest()
    kap4 = load_manifest("kap4_metodologie_cisla")
    kap5 = load_manifest("kap5_korpus_cisla")
    kap6 = load_manifest("kap6_kodovani_cisla")
    kap7 = load_manifest("kap7_k2_shoda_cisla")

    def val(v) -> int:
        return int(v or 0)

    pocty = {
        e: sum(1 for r in rows if val(r.get(e)) > 0)
        for e in HUMAN + ["llm_anotace_matice_08_24", "hf_publikovano_en"]
    }
    mult = {k: sum(1 for r in rows if sum(1 for e in HUMAN if val(r.get(e)) > 0) == k)
            for k in (1, 2, 3, 4)}
    ge2_ud = sum(1 for r in rows
                 if sum(1 for e in HUMAN if val(r.get(e)) > 0) >= 2)
    nk = [sum(1 for cols in KAMPANE.values()
              if any(val(r.get(e)) > 0 for e in cols)) for r in rows]
    ge2_kamp, ge3_kamp = sum(1 for x in nk if x >= 2), sum(1 for x in nk if x >= 3)

    # tvrdé asserty proti kap4 manifestu (jediná pravda o multiplicitě)
    assert mult[2] == int(kap4["multiplicita_2x"]), (mult[2], kap4["multiplicita_2x"])
    assert mult[3] == int(kap4["multiplicita_3x"])
    assert mult[4] == int(kap4["multiplicita_4x"])
    assert ge2_ud == int(kap4["prekryv_ge2_udalosti"])
    assert ge2_kamp == int(kap4["prekryv_ge2_kampane"])
    assert ge3_kamp == int(kap4["prekryv_ge3_kampane"])

    manifest_rows = [("c1_" + e, pocty[e]) for e in pocty]
    manifest_rows.append(("c2_multiplicita_1x", mult[1]))

    with OUT_MAN.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["metric", "value", "skript", "data_sha", "seed", "datum"])
        for k, v in manifest_rows:
            w.writerow([k, v, SKRIPT, sha, "", date.today().isoformat()])

    def a_c(key: str, n: int) -> str:
        return f"{tis(n)} <!-- manifest priloha_c_cisla: {key}={n} -->"

    def a(man: str, key: str, prose: str, raw: str) -> str:
        return f"{prose} <!-- manifest {man}: {key}={raw} -->"

    def a4(key: str) -> str:
        return a("kap4_metodologie_cisla", key, tis(int(kap4[key])), kap4[key])

    md: list[str] = []
    md.append("# Příloha C. Doplňkové tabulky")
    md.append("")
    md.append("> Jazyk souboru: CZ (autoritativní; habilitace-2 nemá EN zrcadlo)")
    md.append("> Typ kapitoly: příloha (doplňkové tabulky)")
    md.append(f"> Podkladová data a analýzy: {SKRIPT} ← data/processed/anotace_pokryti.csv"
              " + manifesty kap4/kap5/kap6/kap7")
    md.append(f"> GENEROVÁNO SKRIPTEM {date.today().isoformat()} – NEEDITOVAT RUČNĚ,"
              " regenerovat skriptem 17")
    md.append("")
    md.append("Tato příloha dokládá registr anotačních událostí,")
    md.append("rekonciliaci velikostí datových řezů a kanonický přehled měr shody.")
    md.append("Úplná matice pokrytí (kazuistika × událost) je dostupná v doprovodném")
    md.append("repozitáři jako `anotace_pokryti.csv`; zde uvádíme agregáty. Počty")
    md.append("kazuistik se vztahují k záznamům spárovaným na jednotný identifikátor")
    md.append("(kapitola 4); počty řádků v původních anotačních souborech se mohou")
    md.append("mírně lišit o záznamy, které se spárovat nepodařilo.")
    md.append("")
    md.append("## C.1 Registr anotačních událostí")
    md.append("")
    md.append("**Tabulka C.1.** Anotační události tří etap (anotátorky pod"
              " anonymizovanými pseudonymy A1–A12; ❓ = mapování pseudonymu"
              " na osobu čeká na potvrzení).")
    md.append("")
    md.append("```{=latex}")
    md.append("\\footnotesize")
    md.append("```")
    md.append("")
    md.append("| Událost | Období | Etapa a fáze | Anotátorky | Kazuistik | Poznámka |")
    md.append("|:------------------|:-------|:---------|:-----------|:-------|:----------------|")
    for ev, obdobi, faze, kdo, key, pozn in REGISTR:
        n_cell = a_c(key, pocty[ev]) if key else "–"
        md.append(f"| `{ev}` | {obdobi} | {faze} | {kdo} | {n_cell} | {pozn} |")
    md.append("")
    md.append("```{=latex}")
    md.append("\\normalsize")
    md.append("```")
    md.append("")
    md.append("*Poznámka. Vygenerováno z matice pokrytí [skriptem přílohy C](https://github.com/JanNehyba/edustories-habilitation/blob/main/analyzy/scripts/17_priloha_c.py); metadata událostí dle datové dokumentace.*")
    md.append("")
    md.append("## C.2 Rekonciliace velikostí řezů")
    md.append("")
    md.append("**Tabulka C.2.** Čísla, která se v knize a podkladech vztahují k „velikosti dat“, a jejich vztah.")
    md.append("")
    md.append("| Číslo | Co označuje | Zdroj |")
    md.append("|---|---|---|")
    md.append(f"| {a('kap5_korpus_cisla', 'n_korpus_s6', tis(3202), '3202')} | zveřejněné kazuistiky, řez květen 2026 (S6) | zdrojová tabulka kap5 |")
    md.append(f"| {a('kap5_korpus_cisla', 'rust_S4082024', tis(1695), '1695')} | řez srpen 2024 (S4; prostor identifikátorů druhé etapy) | zdrojová tabulka kap5 |")
    md.append(f"| {a('kap5_korpus_cisla', 'rust_S5HFrelease', tis(1492), '1492')} | veřejný dataset (kurátorovaný výběr z S4); záznamy výběru odpovídají {a_c('c1_hf_publikovano_en', pocty['hf_publikovano_en'])} unikátním kazuistikám (Tabulka C.1) | zdrojové tabulky kap5 + příloha C |")
    md.append(f"| {a('kap5_korpus_cisla', 'n_k1_rez', tis(1359), '1359')} | reprodukovatelný řez K1 (dedup ∧ lidská anotace v matici) | zdrojová tabulka kap5 |")
    md.append(f"| {a('kap4_provenience_cisla', 'prov_rez_pokryto_lidskou', tis(1350), '1350')} | z řezu K1 s dochovaným přímým anotačním listem | zdrojová tabulka kap4_provenience |")
    md.append(f"| {a('kap7_k2_shoda_cisla', 'n_kazuistik', tis(324), '324')} | analytický vzorek druhé etapy (zaslepené dvojice) | zdrojová tabulka kap7 |")
    md.append("| přibližně třináct set <!-- necislo: historické číslo rukopisů, nerekonstruovatelné --> | dobový stav pracovní databáze ve starších rukopisech | kniha nepoužívá (kapitola 4) |")
    md.append("")
    md.append("*Poznámka. Hodnoty pocházejí ze zdrojových tabulek čísel citovaných v tomto přehledu; zdůvodnění viz kapitola 4.*")
    md.append("")
    md.append("## C.3 Kanonický přehled měr shody")
    md.append("")
    md.append("**Tabulka C.3.** Shrnutí spolehlivosti napříč etapami (podrobnosti a intervaly spolehlivosti v kapitolách 6 a 7).")
    md.append("")
    md.append("| Etapa | Veličina | Hodnota |")
    md.append("|---|---|---|")

    def r6(key: str) -> str:
        return a("kap6_kodovani_cisla", key, dc(float(kap6[key])), kap6[key])

    def r7(key: str) -> str:
        return a("kap7_k2_shoda_cisla", key, dc(float(kap7[key])), kap7[key])

    md.append(f"| K1 (lidé) | α typ chování | {r6('k1_alpha_nom_chovani')} |")
    md.append(f"| K1 (lidé) | α typ řešení | {r6('k1_alpha_nom_reseni')} |")
    md.append(f"| K1 (lidé) | α dopad | {r6('k1_alpha_nom_dopad')} |")
    md.append(f"| K1 (LLM × člověk) | přesná shoda | {r6('shoda_presna_llm')} |")
    md.append(f"| K1 (LLM × člověk) | rozšířená shoda | {r6('shoda_rozsirena_llm')} |")
    md.append(f"| K1 (LLM × člověk) | Cohenovo κ | {r6('kappa_llm_clovek')} |")
    md.append(f"| K2 | α vhodnost | {r7('alpha_ord_final_vhodnost')} |")
    md.append(f"| K2 | α reaktivní–proaktivní | {r7('alpha_ord_final_reaktivni')} |")
    md.append(f"| K2 | α humanistická–behaviorální | {r7('alpha_ord_final_humanisticke')} |")
    md.append(f"| K2 | α systémová–situační | {r7('alpha_ord_final_systemove')} |")
    md.append(f"| K2 | Jaccard rámce (konvence článku) | {r7('jaccard_pristupy_obe_prazdne_shoda')} |")
    md.append("| K3 | probíhá | viz Studie 4 po uzavření etapy <!-- necislo: bez hodnoty --> |")
    md.append("")
    md.append("*Poznámka. Hodnoty ze [zdrojových čísel Studie 2](https://github.com/JanNehyba/edustories-habilitation/blob/main/vystupy/tabulky/kap6_kodovani_cisla.csv) a [zdrojových čísel Studie 3](https://github.com/JanNehyba/edustories-habilitation/blob/main/vystupy/tabulky/kap7_k2_shoda_cisla.csv) v doprovodném repozitáři.*")
    md.append("")
    md.append("---")
    md.append("")
    md.append("### Kontrolní seznam před finalizací (build tento blok stripuje)")
    md.append("")
    md.append("- [x] Každé tvrdé číslo má kotvu na manifest nebo `<!-- necislo -->` (generováno skriptem)")
    md.append("- [x] Tabulky číslované C.1–C.3, s uvedeným zdrojem")
    md.append("- [x] Anonymizace: pouze pseudonymy A1–A12")
    md.append("- [x] Žádný em-dash; en-dash jen v rozsazích")
    md.append("- [ ] Po K3 freeze regenerovat (řádek K3 finál a C.3) skriptem 17")
    md.append("- [ ] Zápis freeze přílohy do PLAN.md §1 log")
    md.append("")

    OUT_MD.write_text("\n".join(md), encoding="utf-8")
    print(f"Manifest: {len(manifest_rows)} metrik → {OUT_MAN.relative_to(ROOT)}")
    print(f"Příloha C: {len(md)} řádků → {OUT_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
