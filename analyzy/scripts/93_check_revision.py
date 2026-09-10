from __future__ import annotations

import argparse
import importlib
from pathlib import Path
import tempfile
from types import SimpleNamespace
from unittest import mock

import numpy as np
import pandas as pd

from revision_metrics import prediction_metrics


def check(root: Path) -> None:
    processed = root / "data/processed"
    tables = root / "vystupy/tabulky"
    comparison = pd.read_csv(processed / "srovnani_k1_llm.csv", keep_default_na=False)
    flags = pd.read_csv(processed / "kap6_overlap_flags.csv")
    assert len(comparison) == 334 and flags.id.is_unique
    assert len(flags) == 334 and flags.exact_overlap.sum() == 36
    assert set(flags.id.astype(str)) == set(comparison.id.astype(str))
    slice_ids = pd.read_csv(processed / "k1_rez_ids.csv", keep_default_na=False)
    assert slice_ids.case_uid.eq("").sum() == 13
    assert slice_ids.mat_id.is_unique
    assert slice_ids.loc[slice_ids.case_uid.ne(""), "case_uid"].is_unique
    quality = pd.read_csv(processed / "k3_wide.csv", keep_default_na=False)
    identified = quality.loc[quality.case_uid.ne("")]
    assert identified.case_uid.nunique() == 3185
    assert quality.case_uid.eq("").sum() == 7
    assert not identified.duplicated(["case_uid", "anotator"]).any()
    assert set(quality.kvalita) <= {"Plná", "Plochá", ""}
    scores = prediction_metrics(["NEU", "KU", "DU"], ["NEU", None, np.nan])
    assert scores["n"] == 3 and scores["n_invalid"] == 2
    assert np.isclose(scores["acc"], 1 / 3)
    assert np.isclose(scores["bal_acc"], 1 / 3)
    assert np.isfinite(scores["kappa"])
    failed = prediction_metrics(["NEU", "KU", "DU"], [None, "", "unparsed"])
    assert failed["coverage"] == 0 and failed["acc"] == 0
    assert failed["kappa"] == 0
    assert np.isclose(scores["kappa"], 0.25)
    module = importlib.import_module("26_k3_predikce_llm")
    assert module.parsuj(np.nan) is None
    assert module.parsuj(None) is None
    assert module.parsuj("KU") == "KU"
    assert not module.test_uniku([{"content": "VYSLEDEK: ZLE"}], "zle")
    assert not module.test_uniku([{"content": "anything"}], None)
    assert module.test_uniku([{"content": "description without outcome"}], "different outcome")
    response = SimpleNamespace(status_code=200, raise_for_status=lambda: None,
                               json=lambda: {"choices": [{"message": {"content": "KU"}}]})
    session = SimpleNamespace(headers={}, post=mock.Mock(return_value=response))
    with tempfile.TemporaryDirectory() as directory, mock.patch.object(module, "token", return_value="test-only"), \
            mock.patch.object(module.requests, "Session", return_value=session):
        client = module.Klient("test-model", Path(directory) / "cache.jsonl", "deployment-one")
        prompt = [{"role": "user", "content": "test-only"}]
        client.zeptej(prompt)
        client.zeptej(prompt)
        assert session.post.call_count == 1
        client.otisk()
        client.otisk()
        assert session.post.call_count == 3
        with mock.patch.object(module, "BASE_URL", "https://example.invalid"):
            client.zeptej(prompt)
        assert session.post.call_count == 4
        client.deployment_id = "deployment-two"
        client.zeptej(prompt)
        assert session.post.call_count == 5
    expected = {
        "kap6_kodovani_cisla": {"n_paru_llm_clovek": 333, "bez_prekryvu_n": 297},
        "kap7_k2_shoda_cisla": {"n_chybejicich_bunek_celkem": 1676, "n_chybejicich_radku": 76},
        "kap8_kvalita_cisla": {"k1k3_dopad_n": 885, "obe_plne_dopad_n": 593},
        "kap8_predikce_cisla": {"predikce_n_eval": 601,
                               "predikce_kimi_k3_zero_shot_a12_n_invalid": 13,
                               "predikce_glm_5_3_zero_shot_a12_n_invalid": 7},
    }
    for table, values in expected.items():
        manifest = pd.read_csv(tables / f"{table}.csv")
        assert manifest.metric.is_unique, table
        indexed = manifest.set_index("metric").value
        for metric, value in values.items():
            assert indexed[metric] == value, (table, metric)
    differences = pd.read_csv(tables / "kap8_predikce_rozdily.csv")
    assert differences.n.eq(487).all()
    assert differences.ci_lo.lt(0).all() and differences.ci_hi.gt(0).all()
    print("Revision checks: valid units, missingness, invalid predictions and paired comparisons OK.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    check(parser.parse_args().root)
