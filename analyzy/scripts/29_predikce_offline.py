"""Přepočítá metriky predikcí Studie 4 z veřejných uložených štítků.

Vstupy: k3_predikce_raw.csv a historický protokol v data/processed.
Výstupy: manifest, metriky podle reference a párové rozdíly ve vystupy/tabulky.
Nevytváří nové modelové odpovědi, nevolá API a nepotřebuje soukromé texty.
"""

import argparse
from datetime import date
import hashlib
import json
from pathlib import Path
import re

import pandas as pd

from revision_metrics import LABELS, SEED, bootstrap_intervals, paired_balanced_difference, prediction_metrics


def slug(value):
    return re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--bootstrap", type=int, default=1000)
    args = parser.parse_args()
    root = args.root.resolve()
    processed = root / "data/processed"
    output = root / "vystupy/tabulky"
    output.mkdir(parents=True, exist_ok=True)
    input_path = processed / "k3_predikce_raw.csv"
    predictions = pd.read_csv(input_path, dtype=str, keep_default_na=False)
    keys = ["case_uid", "model", "varianta", "mnozina"]
    if predictions.duplicated(keys).any():
        raise ValueError("Klíče predikcí nejsou jedinečné.")
    development_ids = set(predictions.loc[predictions.mnozina.eq("dev"), "case_uid"])
    evaluation = predictions.loc[predictions.mnozina.eq("eval")].copy()
    if development_ids & set(evaluation.case_uid):
        raise ValueError("Vývojové a hodnoticí případy se překrývají.")
    for reference_name in ("dopad_A12", "dopad_A2"):
        if evaluation.groupby("case_uid")[reference_name].nunique().gt(1).any():
            raise ValueError("Lidské reference se mezi modelovými běhy liší.")
    unique_cases = evaluation.drop_duplicates("case_uid")
    manifest = {}
    rows = []

    def put(key, value):
        if key in manifest:
            raise ValueError(f"Opakovaný klíč metriky: {key}")
        manifest[key] = round(float(value), 4)

    majority = unique_cases.dopad_A12.value_counts().index[0]
    put("predikce_majorita_podil", unique_cases.dopad_A12.eq(majority).mean())
    put("predikce_n_eval", len(unique_cases))
    put("predikce_majorita_bal_acc", prediction_metrics(unique_cases.dopad_A12, [majority] * len(unique_cases))["bal_acc"])
    put("predikce_seed", SEED)
    put("predikce_bootstrap_n", args.bootstrap)
    protocol = json.loads((processed / "k3_predikce_protocol.json").read_text(encoding="utf-8"))
    put("predikce_leakage_test_ok", protocol["historical_check_passed"])
    put("predikce_vyrazeno_unik", protocol["historical_excluded_cases"])
    for metric, value in prediction_metrics(unique_cases.dopad_A12, unique_cases.dopad_A2).items():
        put(f"predikce_clovek_clovek_{metric}", value)
    consensus_runs = {}
    for (model, variant), group in evaluation.groupby(["model", "varianta"]):
        if set(group.case_uid) != set(unique_cases.case_uid):
            raise ValueError("Modelové běhy nepokrývají stejné hodnoticí případy.")
        for reference in ("A12", "A2", "konsenzus"):
            if reference == "konsenzus":
                selected = group.loc[group.dopad_A12.eq(group.dopad_A2) & group.dopad_A12.isin(LABELS)].copy()
                target = "dopad_A12"
                consensus_runs[(model, variant)] = selected.set_index("case_uid")
            else:
                target = f"dopad_{reference}"
                selected = group.loc[group[target].isin(LABELS)]
            scores = prediction_metrics(selected[target], selected.predikce)
            prefix = f"predikce_{slug(f'{model}_{variant}_{reference}')}"
            for metric, value in scores.items():
                put(f"{prefix}_{metric.lower()}", value)
            intervals = bootstrap_intervals(selected[target], selected.predikce, args.bootstrap)
            for metric, interval in intervals.items():
                put(f"{prefix}_{metric}_ci_lo", interval[0])
                put(f"{prefix}_{metric}_ci_hi", interval[1])
            rows.append({"model": model, "varianta": variant, "reference": reference, **scores,
                         **{f"{metric}_ci_{bound}": float(interval[index])
                            for metric, interval in intervals.items() for index, bound in enumerate(("lo", "hi"))}})
        for label in LABELS:
            put(f"predikce_{slug(model)}_{variant}_podil_pred_{label.lower()}", group.predikce.eq(label).mean())
        consensus = group.loc[group.dopad_A12.eq(group.dopad_A2)]
        disputed = group.loc[group.dopad_A12.ne(group.dopad_A2)]
        put(f"predikce_{slug(model)}_{variant}_konsenzus_trefa", consensus.predikce.eq(consensus.dopad_A12).mean())
        put(f"predikce_{slug(model)}_{variant}_sporne_n", len(disputed))
        put(f"predikce_{slug(model)}_{variant}_sporne_jedna_ze_dvou",
            (disputed.predikce.eq(disputed.dopad_A12) | disputed.predikce.eq(disputed.dopad_A2)).mean())
    comparisons = [
        ("glm_vs_kimi", ("kimi-k3", "zero_shot"), ("glm-5.3", "zero_shot")),
        ("few_vs_zero", ("glm-5.3", "zero_shot"), ("glm-5.3", "few_shot")),
    ]
    differences = []
    for name, baseline_key, alternative_key in comparisons:
        baseline = consensus_runs[baseline_key].sort_index()
        alternative = consensus_runs[alternative_key].reindex(baseline.index)
        if alternative.predikce.isna().any():
            raise ValueError("Párové porovnání obsahuje nespárované případy.")
        difference = paired_balanced_difference(baseline.dopad_A12, baseline.predikce,
                                               alternative.predikce, args.bootstrap)
        for metric, value in difference.items():
            put(f"predikce_rozdil_{name}_{metric}", value)
        differences.append({"comparison": name, **difference})
    for reference in ("A12", "A2"):
        for label in LABELS:
            put(f"predikce_podil_{reference.lower()}_{label.lower()}", unique_cases[f"dopad_{reference}"].eq(label).mean())
    input_sha = hashlib.sha256(input_path.read_bytes()).hexdigest()
    pd.DataFrame([{"metric": metric, "value": value, "skript": "analyzy/scripts/29_predikce_offline.py",
                   "data_sha": input_sha, "seed": SEED, "datum": date.today().isoformat()}
                  for metric, value in manifest.items()]).to_csv(output / "kap8_predikce_cisla.csv", index=False)
    pd.DataFrame(rows).to_csv(output / "kap8_predikce_vysledky.csv", index=False)
    pd.DataFrame(differences).to_csv(output / "kap8_predikce_rozdily.csv", index=False)
    print(f"Přepočteno {len(unique_cases)} hodnoticích případů a {len(rows)} řádků podle reference; otisk vstupu {input_sha}")
    print(pd.DataFrame(differences).to_string(index=False))


if __name__ == "__main__":
    main()
