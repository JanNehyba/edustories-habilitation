#!/usr/bin/env bash
# Reprodukce analýz knihy od dat po manifesty a reporty (živá habilitace, PLAN §8).
# Předpoklady: Python 3.11 (+ requirements.txt), R + renv, Quarto.
# Datové vstupy: veřejná podmnožina v data/processed/ (plné surové datové řezy
# nejsou součástí companionu — obsahují nezveřejněné kazuistiky).
set -euo pipefail
cd "$(dirname "$0")"

echo "── R prostředí (renv)"
Rscript -e 'if (!requireNamespace("renv", quietly=TRUE)) install.packages("renv"); renv::restore(prompt=FALSE)' || true

echo "── notebooky (render → HTML reporty + manifesty čísel)"
for nb in analyzy/notebooks/10_korpus.qmd analyzy/notebooks/20_kodovani_llm.qmd \
          analyzy/notebooks/30_ai_vs_ucitel.qmd; do
  [ -f "$nb" ] && quarto render "$nb" --output-dir ../vystupy/reporty || \
    echo "   (přeskočeno: $nb vyžaduje surová data mimo companion)"
done

echo "── figury knihy (z manifestů)"
[ -x analyzy/scripts/render_figures.sh ] && analyzy/scripts/render_figures.sh

echo "── kontrolní brány (čísla ↔ manifesty, reference)"
python3 analyzy/scripts/95_check_cisla.py || true
python3 analyzy/scripts/96_check_references.py || true

echo "HOTOVO. Manifesty: vystupy/tabulky/ | reporty: vystupy/reporty/ | figury: vystupy/obrazky/"
