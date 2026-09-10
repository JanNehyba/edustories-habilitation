"""Offline agreement and prediction metrics with explicit failed-response handling."""

from collections import Counter

import numpy as np


LABELS = ("NEU", "KU", "DU")
INVALID = "__INVALID__"
SEED = 20260714


def normalize_prediction(value):
    if not isinstance(value, str):
        return INVALID
    value = value.strip().upper()
    return value if value in LABELS else INVALID


def nominal_kappa(reference, prediction):
    reference = list(reference)
    prediction = list(prediction)
    if len(reference) != len(prediction):
        raise ValueError("Reference and prediction lengths differ.")
    if not reference:
        return float("nan")
    count = len(reference)
    observed = sum(actual == predicted for actual, predicted in zip(reference, prediction)) / count
    reference_counts = Counter(reference)
    prediction_counts = Counter(prediction)
    chance = sum(frequency * prediction_counts[label] for label, frequency in reference_counts.items()) / count**2
    return (observed - chance) / (1 - chance) if chance < 1 else float("nan")


def prediction_metrics(reference, prediction):
    reference = np.asarray(list(reference), dtype=object)
    prediction = np.asarray([normalize_prediction(value) for value in prediction], dtype=object)
    if len(reference) != len(prediction):
        raise ValueError("Reference and prediction lengths differ.")
    if not len(reference):
        return {}
    if not np.isin(reference, LABELS).all():
        raise ValueError("Reference contains missing or unknown labels.")
    valid = prediction != INVALID
    recalls = {}
    f_scores = []
    for label in LABELS:
        actual = reference == label
        predicted = prediction == label
        true_positive = int((actual & predicted).sum())
        recalls[label] = true_positive / int(actual.sum()) if actual.any() else float("nan")
        denominator = int(actual.sum() + predicted.sum())
        f_scores.append(2 * true_positive / denominator if denominator else 0.0)
    result = {
        "n": len(reference), "n_valid": int(valid.sum()), "n_invalid": int((~valid).sum()),
        "coverage": float(valid.mean()), "acc": float((reference == prediction).mean()),
        "bal_acc": float(np.nanmean(list(recalls.values()))), "macro_f1": float(np.mean(f_scores)),
        "kappa": nominal_kappa(reference, prediction),
        "kappa_valid": nominal_kappa(reference[valid], prediction[valid]),
    }
    result.update({f"recall_{label}": value for label, value in recalls.items()})
    return result


def bootstrap_intervals(reference, prediction, repetitions=1000):
    reference = np.asarray(reference, dtype=object)
    prediction = np.asarray(prediction, dtype=object)
    random = np.random.default_rng(SEED)
    metrics = ("acc", "bal_acc", "macro_f1", "kappa")
    estimates = {metric: [] for metric in metrics}
    for _ in range(repetitions):
        selected = random.integers(0, len(reference), size=len(reference))
        result = prediction_metrics(reference[selected], prediction[selected])
        for metric in metrics:
            estimates[metric].append(result[metric])
    return {metric: np.nanquantile(values, [.025, .975]) for metric, values in estimates.items()}


def paired_balanced_difference(reference, baseline, alternative, repetitions=1000):
    reference = np.asarray(reference, dtype=object)
    baseline = np.asarray(baseline, dtype=object)
    alternative = np.asarray(alternative, dtype=object)
    if not (len(reference) == len(baseline) == len(alternative)):
        raise ValueError("Paired comparison requires the same cases.")
    random = np.random.default_rng(SEED)
    differences = []
    for _ in range(repetitions):
        selected = random.integers(0, len(reference), size=len(reference))
        differences.append(prediction_metrics(reference[selected], alternative[selected])["bal_acc"]
                           - prediction_metrics(reference[selected], baseline[selected])["bal_acc"])
    estimate = prediction_metrics(reference, alternative)["bal_acc"] - prediction_metrics(reference, baseline)["bal_acc"]
    interval = np.quantile(differences, [.025, .975])
    return {"n": len(reference), "difference": estimate, "ci_lo": interval[0], "ci_hi": interval[1]}
