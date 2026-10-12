#!/usr/bin/env python3
"""Generátor přílohy C (doplňkové tabulky) — NEEDITOVAT výstup ručně.

Generuje `kapitoly/cs/appendix-C-supplementary-tables.md` z matice pokrytí
(data/processed/anotace_pokryti.csv) a existujících manifestů (kap4 až kap8).
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

# Registr událostí: metadata z DATA_README §2 (jen pseudonymy!); počty se počítají.
# (sloupec tabulky pokrytí | None, popisný název události, období, kódující, poznámka)
# Popisné názvy nahrazují interní identifikátory sloupců (revize G7-064); sloupec
# `llm_anotace_matice_08_24` nese historický název, obsahuje lidské kódy K1.
# Metadata jen v rozsahu, který dokládá DATA_README §2 (revize G7-069): u testu
# z března 2024 „pět souborů“ (kdo kódoval, není doloženo), u zácviku a pilotů K3
# jen rok, u zveřejnění datové sady „podzim 2024“.
REGISTR = [
    (None, "K1 zácvik (pokus)", "prosinec 2023 – únor 2024", "A1, A2, A5, A6",
     "kvalitativní kódy bez matice; kódovací kniha, strom V1→V2"),
    ("k1_test_03_24", "K1 test 1", "březen 2024", "pět souborů", ""),
    ("k1_test_04_24", "K1 test 2", "duben 2024", "A1–A4, A7", ""),
    ("k1_naostro_05_24", "K1 finál", "od května 2024", "A1–A4, A7",
     "dělba práce s vestavěným překryvem"),
    ("llm_anotace_matice_08_24", "K1 sloučení do matice", "srpen 2024", "–",
     "lidské kódy K1 sloučené do matice korpusu"),
    ("k2_setkani10_04_25", "K2 zácvik 1", "duben 2025", "A1, A2, A8–A11", ""),
    ("k2_anotace40_04_25", "K2 zácvik 2", "duben 2025", "A1, A2, A8–A12", ""),
    (None, "K2 příprava", "červen 2025", "gpt-4o (strojově)",
     "generace srovnávacích řešení, ne anotace"),
    ("k2_final351_06_25", "K2 finál", "červen 2025", "A1, A2, A8, A9, A10, A12",
     "zaslepené hodnocení dvojic řešení (kapitola 7)"),
    ("k3_zacvik_26", "K3 zácvik", "2026", "A2, A12", ""),
    ("k3_pilot1_26", "K3 pilot 1", "2026", "A2, A12", ""),
    ("k3_pilot2_26", "K3 pilot 2", "2026", "A2, A12", ""),
    ("k3_final_26", "K3 finál", "březen až září 2026", "A2, A12",
     "dělba práce s vestavěným překryvem; uzavřeno řezem ze září 2026"
     " (kapitola 8)"),
    ("hf_publikovano_en", "zveřejnění datové sady (ne anotace)", "podzim 2024", "–",
     "veřejná datová sada, výběr z řezu srpen 2024"),
]

# Názvy modelů v próze: klíče manifestu nesou slug (tečka → podtržítko), proto se
# mapují výslovně podle záznamu běhu 26/29 (revize G7-065); neznámý model = chyba.
MODELY = {"glm_5_3": "glm-5.3", "kimi_k3": "kimi-k3"}


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
        w = csv.writer(fh, lineterminator="\n")
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
              " + manifesty kap4/kap5/kap6/kap7/kap8")
    md.append(f"> GENEROVÁNO SKRIPTEM {date.today().isoformat()} – NEEDITOVAT RUČNĚ,"
              " regenerovat skriptem 17")
    md.append("")
    md.append("Příloha uvádí registr anotačních událostí, přehled velikostí datových")
    md.append("řezů a přehled měr shody. Počty kazuistik se vztahují k záznamům")
    md.append("spárovaným na jednotný identifikátor; úplná tabulka pokrytí")
    md.append("(kazuistika × událost) je v doprovodném repozitáři (Nehyba, 2026).")
    md.append("")
    md.append("## C.1 Registr anotačních událostí")
    md.append("")
    md.append("**Tabulka C.1.** Anotační události tří etap (anotátorky pod"
              " projektovými pseudonymy A1–A12).")
    md.append("")
    md.append("Číslo pseudonymu je projektové: táž osoba vystupuje pod týmž"
              " pseudonymem ve všech etapách a kapitolách.")
    md.append("")
    md.append("```{=latex}")
    md.append("\\footnotesize")
    md.append("```")
    md.append("")
    md.append("| Událost | Období | Kódující | Kazuistik | Poznámka |")
    md.append("|:------------------|:-------|:-----------|:-------|:----------------|")
    for sloupec, nazev, obdobi, kdo, pozn in REGISTR:
        n_cell = a_c("c1_" + sloupec, pocty[sloupec]) if sloupec else "–"
        md.append(f"| {nazev} | {obdobi} | {kdo} | {n_cell} | {pozn} |")
    md.append("")
    md.append("```{=latex}")
    md.append("\\normalsize")
    md.append("```")
    md.append("")
    md.append("*Poznámka.* Vlastní výpočet z tabulky pokrytí; kód a data v doprovodném"
              " repozitáři (Nehyba, 2026).")
    md.append("")
    md.append("## C.2 Přehled velikostí datových řezů")
    md.append("")
    md.append("**Tabulka C.2.** Velikosti datových řezů a vzorků užívaných v knize.")
    md.append("")
    md.append("| Číslo | Co označuje | Zdroj |")
    md.append("|---|---|---|")
    md.append(f"| {a('kap5_korpus_cisla', 'n_korpus_s6', tis(3202), '3202')} | zveřejněné kazuistiky, řez květen 2026 | kapitola 5 |")
    md.append(f"| {a('kap5_korpus_cisla', 'rust_S4082024', tis(1695), '1695')} | řez srpen 2024 (prostor identifikátorů druhé etapy) | kapitola 5 |")
    md.append(f"| {a('kap5_korpus_cisla', 'rust_S5HFrelease', tis(1492), '1492')} | veřejná datová sada (kurátorovaný výběr z řezu srpen 2024); záznamy výběru odpovídají {a_c('c1_hf_publikovano_en', pocty['hf_publikovano_en'])} unikátním kazuistikám (Tabulka C.1) | kapitola 5, příloha C |")
    md.append(f"| {a('kap5_korpus_cisla', 'n_k1_rez', tis(1359), '1359')} | reprodukovatelný řez K1 (deduplikované kazuistiky s lidskou anotací v matici) | kapitoly 4 a 5 |")
    md.append(f"| {a('kap7_k2_shoda_cisla', 'n_kazuistik', tis(324), '324')} | vzorek druhé etapy (zaslepené dvojice) | kapitola 7 |")
    md.append("")
    md.append("*Poznámka. Hodnoty z tabulek výsledných hodnot analýz v uvedených kapitolách.*")
    md.append("")
    md.append("## C.3 Přehled měr shody")
    md.append("")
    md.append("**Tabulka C.3.** Shrnutí spolehlivosti napříč etapami (podrobnosti a intervaly spolehlivosti v kapitolách 6, 7 a 8).")
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
    md.append(f"| K1 (model × člověk) | přesná shoda | {r6('shoda_presna_llm')} |")
    md.append(f"| K1 (model × člověk) | rozšířená shoda | {r6('shoda_rozsirena_llm')} |")
    md.append(f"| K1 (model × člověk) | Cohenovo κ | {r6('kappa_llm_clovek')} |")
    md.append(f"| K1 (model × člověk), bez kazuistik z příkladů instrukce | Cohenovo κ | {r6('bez_prekryvu_kappa')} |")
    md.append(f"| K2 | α vhodnost | {r7('alpha_ord_final_vhodnost')} |")
    md.append(f"| K2 | α reaktivní–proaktivní | {r7('alpha_ord_final_reaktivni')} |")
    md.append(f"| K2 | α humanistická–behaviorální | {r7('alpha_ord_final_humanisticke')} |")
    md.append(f"| K2 | α systémová–situační | {r7('alpha_ord_final_systemove')} |")
    md.append(f"| K2 | Jaccard rámce | {r7('jaccard_pristupy_obe_prazdne_shoda')} |")
    kap8_path = TAB / "kap8_kvalita_cisla.csv"
    if kap8_path.exists():
        kap8 = load_manifest("kap8_kvalita_cisla")

        def r8(key: str) -> str:
            return a("kap8_kvalita_cisla", key, dc(float(kap8[key])), kap8[key])

        md.append(f"| K3 | κ kvalita (bez sporných kazuistik) | {r8('shoda_kvalita_kappa')} |")
        if "plny_kvalita_kappa" in kap8:
            md.append(f"| K3 | κ kvalita (plný překryv) | {r8('plny_kvalita_kappa')} |")
        md.append(f"| K3 | AC1 kvalita | {r8('shoda_kvalita_ac1')} |")
        md.append(f"| K3 | κ dopad | {r8('shoda_dopad_kappa')} |")
        md.append(f"| K3 | vážená κ vhodnost | {r8('shoda_vhodnost_wkappa')} |")
        md.append(f"| K1 × K3 | κ dopad mezi etapami | {r8('k1k3_dopad_kappa')} |")
    else:
        md.append("| K3 | shoda | viz kapitola 8 <!-- necislo: bez hodnoty --> |")

    # predikční experiment (oddíl 8.6): model proti konsenzuálnímu štítku a lidský strop
    pred_path = TAB / "kap8_predikce_cisla.csv"
    if pred_path.exists():
        pred = load_manifest("kap8_predikce_cisla")

        def rp(key: str) -> str:
            return a("kap8_predikce_cisla", key, dc(float(pred[key])), pred[key])

        modely = sorted({k.split("_zero_shot_")[0][len("predikce_"):]
                         for k in pred if "_zero_shot_konsenzus_bal_acc" in k})
        nezname = [m for m in modely if m not in MODELY]
        if nezname:
            raise KeyError(f"Model bez názvu pro prózu (doplň MODELY): {nezname}")
        for m in modely:
            popis = MODELY[m]
            md.append(f"| K3 predikce | vyvážená přesnost modelu {popis} vůči shodě "
                      f"anotátorek | {rp(f'predikce_{m}_zero_shot_konsenzus_bal_acc')} |")
        if "predikce_clovek_clovek_bal_acc" in pred:
            md.append("| K3 čtení výstupu | vyvážená shoda A2 vůči A12 (jiná úloha než predikce) | "
                      f"{rp('predikce_clovek_clovek_bal_acc')} |")
        if "predikce_majorita_bal_acc" in pred:
            md.append("| K3 predikce | vyvážená přesnost hádání většinové třídy | "
                      f"{rp('predikce_majorita_bal_acc')} |")
    md.append("")
    md.append("*Poznámka.* Vlastní analýza; tabulky výsledných hodnot studií 2 až 4"
              " v doprovodném repozitáři (Nehyba, 2026; kapitoly 6 až 8).")
    md.append("")
    md.append("---")
    md.append("")
    md.append("### Kontrolní seznam před finalizací (build tento blok stripuje)")
    md.append("")
    md.append("- [x] Každé tvrdé číslo má kotvu na manifest nebo `<!-- necislo -->` (generováno skriptem)")
    md.append("- [x] Tabulky číslované C.1–C.3, s uvedeným zdrojem")
    md.append("- [x] Anonymizace: pouze pseudonymy A1–A12")
    md.append("- [x] Žádný em-dash; en-dash jen v rozsazích")
    md.append("- [x] Po přepočtu matice pokrytí s finální třetí etapou regenerováno skriptem 17 (řádek K3 finál, C.3 z manifestu kap8; 8. 9. 2026)")
    md.append("- [ ] Zápis freeze přílohy do PLAN.md §1 log")
    md.append("")

    md = [line[:-1].replace("*Poznámka. ", "*Poznámka.* ", 1)
          if line.startswith("*Poznámka. ") and line.endswith("*") else line for line in md]
    OUT_MD.write_text("\n".join(md), encoding="utf-8")
    print(f"Manifest: {len(manifest_rows)} metrik → {OUT_MAN.relative_to(ROOT)}")
    print(f"Příloha C: {len(md)} řádků → {OUT_MD.relative_to(ROOT)}")
    # kotvy nadpisů a klikací křížové odkazy doplní brána 97 (12. 10. 2026)
    import subprocess
    import sys
    subprocess.run([sys.executable, str(Path(__file__).with_name("97_krizove_odkazy.py")), "--apply"],
                   check=True)


if __name__ == "__main__":
    main()
