#!/usr/bin/env python3
"""Manifest čísel pro metodologickou kapitolu 4 (multiplicita, překryvy kampaní).

Zdroj: data/processed/anotace_pokryti.csv (matice pokrytí, skript 05).
Výstup: vystupy/tabulky/kap4_metodologie_cisla.csv
Spuštění: cd /Users/jannehyba/habilitace && ./.venv/bin/python habilitace-2/analyzy/scripts/15_kap4_cisla.py
"""
from __future__ import annotations

import csv
import hashlib
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "data" / "processed" / "anotace_pokryti.csv"
OUT = ROOT / "vystupy" / "tabulky" / "kap4_metodologie_cisla.csv"

HUMAN = ["k1_test_03_24", "k1_test_04_24", "k1_naostro_05_24",
         "k2_setkani10_04_25", "k2_anotace40_04_25", "k2_final351_06_25",
         "k3_zacvik_26", "k3_pilot1_26", "k3_pilot2_26", "k3_final_26"]

# Kampaň = množina přímých lidských anotačních událostí (bez odvozené
# konsolidace do matice; oprava 16. 7. 2026 — dřívější prekryv_ge2_kampane
# ve skutečnosti počítal UDÁLOSTI: 354+35+1=390, ne kampaně)
KAMPANE = {
    "K1": ["k1_test_03_24", "k1_test_04_24", "k1_naostro_05_24"],
    "K2": ["k2_setkani10_04_25", "k2_anotace40_04_25", "k2_final351_06_25"],
    "K3": ["k3_zacvik_26", "k3_pilot1_26", "k3_pilot2_26", "k3_final_26"],
}

sha = hashlib.sha256(SRC.read_bytes()).hexdigest()
rows = list(csv.DictReader(SRC.open(encoding="utf-8")))
mult = Counter()
kamp_mult = Counter()
for r in rows:
    n = sum(1 for e in HUMAN if int(r.get(e, 0) or 0) > 0)
    mult[n] += 1
    nk = sum(
        1 for cols in KAMPANE.values()
        if any(int(r.get(e, 0) or 0) > 0 for e in cols)
    )
    kamp_mult[nk] += 1

out = [
    ("multiplicita_2x", mult[2]),
    ("multiplicita_3x", mult[3]),
    ("multiplicita_4x", mult[4]),
    ("prekryv_ge2_udalosti", sum(v for k, v in mult.items() if k >= 2)),
    ("prekryv_ge1_udalost", sum(v for k, v in mult.items() if k >= 1)),
    ("prekryv_ge2_kampane", sum(v for k, v in kamp_mult.items() if k >= 2)),
    ("prekryv_ge3_kampane", sum(v for k, v in kamp_mult.items() if k >= 3)),
]
OUT.parent.mkdir(parents=True, exist_ok=True)
with OUT.open("w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow(["metric", "value", "skript", "data_sha", "seed", "datum"])
    for k, v in out:
        w.writerow([k, v, "analyzy/scripts/15_kap4_cisla.py", sha, "", date.today().isoformat()])
print(f"kap4 manifest: {len(out)} metrik →", OUT)
for k, v in out:
    print(f"  {k} = {v}")
