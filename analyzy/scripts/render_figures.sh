#!/usr/bin/env bash
# Obnoví všechny figury knihy z manifestů (GRAFICKY-MANUAL: figury vždy kódem).
set -euo pipefail
cd "$(dirname "$0")"
for f in fig_*.R; do
  echo "── $f"
  Rscript "$f"
done
