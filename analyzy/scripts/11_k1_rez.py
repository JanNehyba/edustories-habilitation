#!/usr/bin/env python3
"""K1_rez — reprodukovatelný analytický řez pro Studie 1–2 (PLAN.md §5 D5).

Definice (freeze 15. 7. 2026): řádky snapshotu S4 (matrix-annotated-22-08-2024)
po deduplikaci textovým otiskem popisu (description_cs, NFC, lowercase,
jen alfanumerika, prvních 120 znaků) ∧ s lidskou anotací (problems_annotated
neprázdné). Očekávaný počet: 1 359.

Historické N=1 319 z rukopisů je NEREKONSTRUOVATELNÉ (DATA_README §5) —
kniha používá výhradně tento řez.

Výstup: data/processed/k1_rez_ids.csv (case_uid, mat_id, fp, problems_annotated…)
Spuštění: cd /Users/jannehyba/habilitace && ./.venv/bin/python habilitace-2/analyzy/scripts/11_k1_rez.py
"""

from __future__ import annotations

import csv
import hashlib
import re
import sys
import unicodedata
from datetime import date
from pathlib import Path

import pandas as pd

csv.field_size_limit(sys.maxsize)

ROOT = Path(__file__).resolve().parents[2]
S4 = ROOT / "data/raw/korpus/matice/Poslední záloha databáze 4.9.2024/matrix-annotated-22-08-2024 (2).csv"
XWALK = ROOT / "data/processed/id_crosswalk.csv"
OUT = ROOT / "data/processed/k1_rez_ids.csv"


def fp(x):
    if pd.isna(x):
        return None
    s = unicodedata.normalize("NFC", str(x)).lower()
    return re.sub(r"[^0-9a-zá-ž]", "", s)[:120] or None


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


mat = pd.read_csv(S4, encoding="utf-8-sig", dtype=str, engine="python")
mat["fp"] = mat["description_cs"].map(fp)
ann = mat["problems_annotated"].notna() & (mat["problems_annotated"].str.strip() != "")
dedup = ~mat.duplicated("fp")
rez = mat[ann & dedup].copy()

# case_uid z crosswalku (mat_id → case_uid)
xw = pd.read_csv(XWALK, dtype=str)
mat2uid = dict(zip(xw["mat_id"].dropna(), xw.loc[xw["mat_id"].notna(), "case_uid"]))
rez["case_uid"] = rez["id"].map(mat2uid)

n = len(rez)
print(f"K1_rez: {n} kazuistik (očekáváno 1 359) — {'OK' if n == 1359 else 'POZOR, NESEDÍ!'}")
print(f"  s case_uid z crosswalku: {rez['case_uid'].notna().sum()}")

cols = ["case_uid", "id", "fp", "problems_annotated", "solutions_annotated",
        "implications_annotated"]
rez = rez.rename(columns={"id": "mat_id"})
cols = ["case_uid", "mat_id", "fp", "problems_annotated", "solutions_annotated",
        "implications_annotated"]
rez[cols].to_csv(OUT, index=False)

meta = {
    "definice": "S4 dedup(fp description_cs 120) AND problems_annotated non-empty",
    "n": n,
    "s4_sha256": sha256_file(S4),
    "skript": "analyzy/scripts/11_k1_rez.py",
    "datum": date.today().isoformat(),
}
print("META:", meta)
if n != 1359:
    sys.exit(1)
