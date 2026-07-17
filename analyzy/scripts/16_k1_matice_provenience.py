#!/usr/bin/env python3
"""Provenience anotačních sloupců matice S4 (K1_rez): člověk, nebo stroj?

Adversariální nález (15. 7. 2026): DATA_README událost 5 vedla sloupce
`*_annotated` v S4 jako strojové (gpt-4o). Tento skript to empiricky testuje
srovnáním obsahu sloupců v k1_rez_ids.csv s lidskými anotačními listy
K1-naostro (data/processed/anotace_long_k1.csv, event k1_naostro_05_24).

Výsledek (viz manifest): množiny kategorií se shodují u 96–98 % kazuistik
(Jaccard ~0,99) → sloupce matice NESOU LIDSKÉ K1 kódy. Strojová shoda
člověk×gpt-4o se přitom pohybuje kolem 71 % na primární kategorii (notebook
20), takže záměna je vyloučena.

Výstup: vystupy/tabulky/kap4_provenience_cisla.csv (manifest pro kap. 4).
"""
from __future__ import annotations

import hashlib
from datetime import date
from pathlib import Path

import pandas as pd

H2 = Path(__file__).resolve().parents[2]
REZ = H2 / "data/processed/k1_rez_ids.csv"
LONG = H2 / "data/processed/anotace_long_k1.csv"
OUT = H2 / "vystupy/tabulky/kap4_provenience_cisla.csv"
SKRIPT = "analyzy/scripts/16_k1_matice_provenience.py"

COLMAP = {
    "chovani": "problems_annotated",
    "reseni": "solutions_annotated",
    "dopad": "implications_annotated",
}
JUNK = {"-", "?", "(zvolit)", ""}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canon(label: str) -> str:
    s = str(label).strip()
    s = s.replace("Částěčný", "Částečný").replace("odbonríky", "odborníky")
    return s[:1].upper() + s[1:] if s else s


def split_matrix(value) -> frozenset:
    if pd.isna(value):
        return frozenset()
    parts = [canon(p.strip()) for p in str(value).replace(";", ",").split(",")]
    return frozenset(p for p in parts if p not in JUNK)


def main() -> None:
    rez = pd.read_csv(REZ)
    lk = pd.read_csv(LONG)
    lk = lk[lk["event"].str.contains("naostro")]

    data_sha = hashlib.sha256(
        (sha256(REZ) + sha256(LONG)).encode()
    ).hexdigest()
    rows: list[dict] = []

    def put(metric: str, value: float) -> None:
        rows.append(
            {
                "metric": metric,
                "value": round(float(value), 4),
                "skript": SKRIPT,
                "data_sha": data_sha,
                "seed": "",
                "datum": date.today().isoformat(),
            }
        )

    for dim, col in COLMAP.items():
        hum = (
            lk[lk["dimenze"] == dim]
            .groupby("case_uid")["hodnota"]
            .apply(lambda v: frozenset(canon(x) for x in v))
        )
        mat = rez.set_index("case_uid")[col].map(split_matrix)
        common = hum.index.intersection(mat.index)
        h, m = hum.loc[common], mat.loc[common]
        exact = (h == m).mean()
        jac = [
            (len(a & b) / len(a | b)) if (a | b) else 1.0
            for a, b in zip(h, m)
        ]
        put(f"prov_{dim}_n_spolecnych", len(common))
        put(f"prov_{dim}_shoda_mnozin", exact)
        put(f"prov_{dim}_jaccard", sum(jac) / len(jac))
        print(
            f"{dim:8s} n={len(common):5d}  shoda množin={exact:.4f}"
            f"  Jaccard={sum(jac) / len(jac):.4f}"
        )

    covered = rez["case_uid"].isin(set(lk["case_uid"])).sum()
    put("prov_rez_n", len(rez))
    put("prov_rez_pokryto_lidskou", covered)
    put("prov_rez_podil_pokryto", covered / len(rez))
    print(f"K1_rez: {len(rez)} | pokryto lidskou K1-naostro: {covered}")

    for dim in COLMAP:
        exact = next(
            r["value"] for r in rows if r["metric"] == f"prov_{dim}_shoda_mnozin"
        )
        assert exact > 0.9, (
            f"Sloupce matice se u dimenze {dim} neshodují s lidskými listy "
            f"({exact}) — provenience NENÍ lidská, zastavit a prošetřit!"
        )

    pd.DataFrame(rows).to_csv(OUT, index=False)
    print(f"Manifest: {len(rows)} metrik → {OUT.relative_to(H2)}")


if __name__ == "__main__":
    main()
