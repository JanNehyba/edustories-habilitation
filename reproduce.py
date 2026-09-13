"""Zopakuje čtyři studie z veřejných odvozených dat bez modelových služeb.

Vstupy: balíček companion, Python, R, Quarto a zamčené závislosti renv.
Výstupy: čtyři HTML reporty, tabulky a obrázky porovnané s přibalenými manifesty.
Obnova závislostí může využít síť; analýzy nepotřebují API klíč ani texty kazuistik.
"""

from __future__ import annotations

import argparse
import csv
import math
import os
from pathlib import Path
import shutil
import subprocess
import sys


def manifests(root: Path) -> dict:
    result = {}
    for path in (root / "vystupy/tabulky").glob("*_cisla.csv"):
        with path.open(encoding="utf-8-sig", newline="") as stream:
            reader = csv.DictReader(stream)
            if not {"metric", "value"}.issubset(reader.fieldnames or []):
                continue
            rows = list(reader)
        result[path.name] = {row["metric"]: float(row["value"]) for row in rows if row["value"] not in ("", "NA")}
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skip-restore", action="store_true", help="Použít již nainstalované R balíčky bez obnovy verzí.")
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    if not (root / "data/processed").is_dir():
        raise SystemExit("Spusťte kopii skriptu v sestaveném balíčku companion.")
    environment = os.environ.copy()
    environment["LC_ALL"] = "English_United States.utf8" if os.name == "nt" else "C.UTF-8"
    environment["LANG"] = environment["LC_ALL"]
    environment["RENV_CONFIG_AUTOLOADER_ENABLED"] = "false"
    environment["PYTHONIOENCODING"] = "utf-8"
    rscript = shutil.which("Rscript")
    quarto = shutil.which("quarto")
    if not rscript or not quarto:
        raise SystemExit("Rscript a Quarto musí být dostupné v PATH.")

    def run(command, directory=root):
        print("SPOUŠTÍM", " ".join(map(str, command)), flush=True)
        subprocess.run(command, cwd=directory, env=environment, check=True)

    if not args.skip_restore:
        library = root / "analyzy/.repro-library"
        library.mkdir(parents=True, exist_ok=True)
        run([rscript, "--vanilla", "-e", "if (!requireNamespace('renv', quietly=TRUE)) install.packages('renv', repos='https://cloud.r-project.org'); renv::restore(project='analyzy', library='analyzy/.repro-library', prompt=FALSE)"])
        environment["R_LIBS_USER"] = str(library)
        environment["R_LIBS"] = str(library)
    baseline = manifests(root)
    run([sys.executable, "analyzy/scripts/29_predikce_offline.py"])
    notebooks = root / "analyzy/notebooks"
    for notebook in ("10_korpus.qmd", "20_kodovani_llm.qmd", "30_ai_vs_ucitel.qmd", "40_kvalita.qmd"):
        run([quarto, "render", notebook, "--output-dir", "../vystupy/reporty"], notebooks)
    reports = root / "vystupy/reporty"
    reports.mkdir(parents=True, exist_ok=True)
    for report_name in ("10_korpus.html", "20_kodovani_llm.html", "30_ai_vs_ucitel.html", "40_kvalita.html"):
        report = root / "analyzy/vystupy/reporty" / report_name
        if not report.is_file():
            raise SystemExit(f"Chybí očekávaný vytvořený report: {report}")
        shutil.copy2(report, reports / report.name)
    scripts = root / "analyzy/scripts"
    for script in sorted(scripts.glob("fig_*.R")):
        run([rscript, "--encoding=UTF-8", script.name], scripts)
    run([sys.executable, "analyzy/scripts/93_check_revision.py"])
    current = manifests(root)
    differences = []
    for table, metrics in baseline.items():
        for metric, value in metrics.items():
            actual = current.get(table, {}).get(metric)
            if actual is None or not math.isclose(value, actual, abs_tol=0.0002, rel_tol=0):
                differences.append(f"{table}:{metric}: {value} -> {actual}")
    if differences:
        raise SystemExit("Přepočtená čísla se liší od přibalených manifestů:\n" + "\n".join(differences))
    if (root / "kapitoly/cs").is_dir():
        for gate in ("95_check_cisla.py", "96_check_references.py"):
            run([sys.executable, f"analyzy/scripts/{gate}"])
    else:
        print("Kontroly rukopisu nejsou součástí tohoto balíčku; zdrojové kapitoly nejsou přibaleny.")
    print("ÚSPĚCH: čtyři reporty, obrázky, kontroly a přibalené číselné výsledky byly reprodukovány.")


if __name__ == "__main__":
    main()
