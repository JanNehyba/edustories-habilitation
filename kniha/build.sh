#!/usr/bin/env bash
# P8 build (habilitace-2): stage kapitoly/cs → strip redakčních bloků → TVRDÉ
# brány (95 čísla↔manifesty, 96 reference CZ-HARD, em-dash) → render → obálka.
# Kniha je POUZE ČESKÁ (jediný EN text = Abstract ve front matter).
#
# Použití:
#   ./build.sh            # PDF
#   ./build.sh docx       # DOCX
#   ./build.sh all        # PDF + DOCX
set -euo pipefail
cd "$(dirname "$0")"

PY="../../.venv/bin/python"
[ -x "$PY" ] || PY="python3"

format="${1:-pdf}"
case "$format" in pdf|docx|all) ;; *)
  echo "Neznámý formát '$format' (pdf, docx, all)." >&2; exit 2
esac

# ── TVRDÉ BRÁNY (build spadne při neshodě) ─────────────────────────────────
"$PY" ../analyzy/scripts/95_check_cisla.py || {
  echo "95_check_cisla FAILED — čísla prózy nesedí na manifesty." >&2; exit 1; }
"$PY" ../analyzy/scripts/96_check_references.py || {
  echo "96_check_references FAILED — citace bez záznamu v literatuře." >&2; exit 1; }
if grep -l "—" ../kapitoly/cs/*.md >/dev/null 2>&1; then
  echo "EM-DASH nalezen v kapitolách (pravidlo: 0 v celé knize):" >&2
  grep -c "—" ../kapitoly/cs/*.md | grep -v ":0" >&2
  exit 1
fi

# ── STAGING: kapitoly/cs → kniha/ (strip metadata blockquote + checklist) ──
"$PY" - <<'PYEOF'
import os, re, glob

src = os.path.join("..", "kapitoly", "cs")
files = (["00-front-matter.md"]
         + sorted(os.path.basename(p) for p in glob.glob(os.path.join(src, "0[1-9]-*.md")))
         + sorted(os.path.basename(p) for p in glob.glob(os.path.join(src, "1[0-9]-*.md")))
         + ["99-references.md"]
         + sorted(os.path.basename(p) for p in glob.glob(os.path.join(src, "appendix-*.md"))))

metadata_labels = (
    "Jazyk souboru", "Typ kapitoly", "Pokrytá výzkumná otázka",
    "Podkladová data", "Podkladová analýza", "Model draftu",
    "GENEROVÁNO SKRIPTEM",
)
metadata_re = re.compile(
    r"^>\s*(?:\*\*)?(?:" + "|".join(re.escape(x) for x in metadata_labels)
    + r")[^\n]*\n?", re.I | re.M)
visible_checklist_re = re.compile(
    r"\n---+\s*\n#{2,4}\s*Kontrolní seznam před finalizací[^\n]*\n.*\Z",
    re.I | re.S)

for filename in files:
    path = os.path.join(src, filename)
    if not os.path.exists(path):
        continue
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    text = visible_checklist_re.sub("\n", text)
    text = metadata_re.sub("", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    # cesty k figurám: autorsky ../../vystupy/… (z kapitoly/cs) → z kniha/ ../vystupy/…
    text = text.replace("](../../vystupy/", "](../vystupy/")
    out = "index.md" if filename == "00-front-matter.md" else filename
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(text.rstrip() + "\n")

print(f"Staged {len([f for f in files if os.path.exists(os.path.join(src, f))])} souborů.")
PYEOF

# ── RENDER ──────────────────────────────────────────────────────────────────
command -v quarto >/dev/null || { echo "Quarto není v PATH." >&2; exit 1; }
targets=("$format"); [ "$format" = "all" ] && targets=(pdf docx)
for t in "${targets[@]}"; do
  quarto render --to "$t" --no-clean
done

# ── OBÁLKA (až bude): cover/cover_final-cs.pdf se předřadí jako 1. strana ──
if printf '%s\n' "${targets[@]}" | grep -qx pdf && [ -f cover/cover_final-cs.pdf ]; then
  "$PY" - cover/cover_final-cs.pdf ../vystupy/export/habilitace2-CZ.pdf <<'PYEOF'
import sys
from pypdf import PdfWriter, PdfReader
cover, book = sys.argv[1], sys.argv[2]
w = PdfWriter()
w.append(PdfReader(cover))
w.append(PdfReader(book))
with open(book, "wb") as f:
    w.write(f)
print(f"cover prepended -> {book}")
PYEOF
fi

echo "OK: ../vystupy/export/habilitace2-CZ.*"
