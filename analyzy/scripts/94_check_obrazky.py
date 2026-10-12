#!/usr/bin/env python3
"""Brána obrázků: žádný obrázek v knize nesmí být starší než kód a data, ze kterých vzniká.

Revize G8-032 (12. 10. 2026). Build knihy obrázky nepřekresluje (nemá vyžadovat R);
tato brána jen ověří, že každý obrázek z `vystupy/obrazky/`, na který odkazuje některá
kapitola v `kapitoly/cs/`, je novější (čas poslední změny souboru) než:
  - skript `analyzy/scripts/fig_*.R`, který ho kreslí (ten, kdo ho ukládá přes
    `save_book_fig(...)` nebo `ggsave(...)`; skripty spouští `render_figures.sh`),
  - pomocné skripty, které fig skript načítá přes `source(...)` (theme_book.R),
  - všechny tabulky, které fig skript čte (`read.csv(...)` / `read_manifest(...)`
    z `vystupy/tabulky/` nebo `data/processed/`).
Mapování obrázek → skript → vstupy se odvozuje z kódu skriptů (bez komentářů), ne ručně.

Obrázek, který žádný fig skript nekreslí (např. sken stanoviska v příloze D), se jen
vypíše jako „bez skriptu“. Chybějící obrázek nebo chybějící vstup skriptu je chyba.
Tolerance 2 s pokrývá zápis souborů během jednoho běhu render_figures.sh.

Omezení: čas změny po čerstvém `git clone` nebo `git checkout` odráží okamžik zápisu
souboru, ne vznik obrázku; při falešném poplachu stačí obrázky překreslit.

Užití: python habilitace-2/analyzy/scripts/94_check_obrazky.py [--verbose] [--koren DIR]
Exit 1 = zastaralý nebo chybějící obrázek, chybějící vstup skriptu.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

TOLERANCE_S = 2.0
FIG_REF = re.compile(r"\]\(\s*(?:\.\./)*vystupy/obrazky/([^)\s#?]+)")
STRING = re.compile(r'"([^"\\]*(?:\\.[^"\\]*)*)"|\'([^\'\\]*(?:\\.[^\'\\]*)*)\'')
OUTPUT_CALL = re.compile(r"\b(?:save_book_fig|ggsave)\s*\(")
SOURCE_CALL = re.compile(r"\bsource\s*\(")
READ_MANIFEST = re.compile(r"\bread_manifest\s*\(\s*[\"']([\w\-.]+)[\"']")


def strip_r_comments(code: str) -> str:
    """Odstraní komentáře R (# mimo řetězce), aby se nepočítaly soubory zmíněné v komentáři."""
    out_lines = []
    for line in code.splitlines():
        quote = None
        escaped = False
        cut = len(line)
        for i, ch in enumerate(line):
            if escaped:
                escaped = False
                continue
            if ch == "\\" and quote:
                escaped = True
                continue
            if quote:
                if ch == quote:
                    quote = None
            elif ch in "\"'":
                quote = ch
            elif ch == "#":
                cut = i
                break
        out_lines.append(line[:cut])
    return "\n".join(out_lines)


def statements(code: str) -> list[str]:
    """Rozdělí kód na volání podle závorek (stačí pro hledání argumentů save/read/source)."""
    out, depth, start = [], 0, 0
    for i, ch in enumerate(code):
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth = max(depth - 1, 0)
        elif ch == "\n" and depth == 0:
            out.append(code[start:i])
            start = i + 1
    out.append(code[start:])
    return [s for s in out if s.strip()]


def literals(text: str) -> list[str]:
    return [a or b for a, b in STRING.findall(text)]


def analyze_script(path: Path, root: Path) -> tuple[set[str], set[Path], list[str]]:
    """Vrátí (výstupní obrázky, závislosti, chyby) jednoho fig skriptu."""
    code = strip_r_comments(path.read_text(encoding="utf-8"))
    outputs: set[str] = set()
    deps: set[Path] = {path}
    errors: list[str] = []
    tabulky = root / "vystupy" / "tabulky"
    processed = root / "data" / "processed"
    for stmt in statements(code):
        lits = literals(stmt)
        if OUTPUT_CALL.search(stmt):
            for lit in lits:
                if lit.lower().endswith(".png"):
                    outputs.add(lit)
                    outputs.add(lit[:-4] + ".pdf")   # save_book_fig ukládá PNG i PDF
                elif lit.lower().endswith(".pdf"):
                    outputs.add(lit)
        if SOURCE_CALL.search(stmt):
            for lit in lits:
                if lit.lower().endswith(".r"):
                    deps.add(path.parent / lit)
        for name in READ_MANIFEST.findall(stmt):
            deps.add(tabulky / f"{name}.csv")
        for lit in lits:
            if not lit.lower().endswith((".csv", ".rds", ".parquet", ".json")):
                continue
            if "processed" in stmt or "PROC" in stmt:
                candidates = [processed / lit]
            elif "tabulky" in stmt or "TAB" in stmt:
                candidates = [tabulky / lit]
            else:
                candidates = [tabulky / lit, processed / lit]
            found = next((c for c in candidates if c.exists()), None)
            if found is None:
                errors.append(f"{path.name}: vstup {lit} nenalezen ({', '.join(c.relative_to(root).as_posix() for c in candidates)})")
            else:
                deps.add(found)
    for dep in list(deps):
        if not dep.exists():
            errors.append(f"{path.name}: závislost {dep.relative_to(root).as_posix()} neexistuje")
            deps.discard(dep)
    return outputs, deps, errors


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--koren", default=str(Path(__file__).resolve().parents[2]),
                    help="kořen habilitace-2 (pro testy na kopii)")
    ap.add_argument("--verbose", action="store_true", help="vypsat mapování obrázek → skript → vstupy")
    args = ap.parse_args()
    root = Path(args.koren).resolve()
    chapters = root / "kapitoly" / "cs"
    figs_dir = root / "vystupy" / "obrazky"
    scripts_dir = root / "analyzy" / "scripts"

    referenced: dict[str, list[str]] = {}
    for md in sorted(chapters.glob("*.md")):
        for name in FIG_REF.findall(md.read_text(encoding="utf-8")):
            referenced.setdefault(name, []).append(md.name)

    producer: dict[str, Path] = {}
    script_deps: dict[Path, set[Path]] = {}
    errors: list[str] = []
    for script in sorted(scripts_dir.glob("fig_*.R")):
        outputs, deps, errs = analyze_script(script, root)
        script_deps[script] = deps
        errors.extend(errs)
        for out in outputs:
            if out in producer and producer[out] != script:
                errors.append(f"{out}: kreslí ho dva skripty ({producer[out].name}, {script.name})")
            producer[out] = script

    stale: list[str] = []
    bez_skriptu: list[str] = []
    checked = 0
    for name, used_in in sorted(referenced.items()):
        fig = figs_dir / name
        if not fig.exists():
            errors.append(f"{name}: obrázek chybí (odkaz v {', '.join(used_in)})")
            continue
        script = producer.get(name)
        if script is None:
            bez_skriptu.append(name)
            continue
        checked += 1
        fig_time = fig.stat().st_mtime
        newer = sorted((d for d in script_deps[script] if d.stat().st_mtime > fig_time + TOLERANCE_S),
                       key=lambda d: d.stat().st_mtime, reverse=True)
        if args.verbose:
            vstupy = ", ".join(sorted(d.name for d in script_deps[script] if d != script))
            print(f"  {name} ← {script.name} ← {vstupy}")
        if newer:
            stale.append(f"{name} (kreslí {script.name}; novější: "
                         + ", ".join(d.relative_to(root).as_posix() for d in newer) + ")")

    if bez_skriptu:
        print("Obrázky bez fig skriptu (mimo kontrolu): " + ", ".join(bez_skriptu))
    if errors or stale:
        for line in errors:
            print(f"CHYBA: {line}")
        for line in stale:
            print(f"ZASTARALÝ: {line}")
        print("Obrázky překresli: bash habilitace-2/analyzy/scripts/render_figures.sh"
              " (vyžaduje R, knihovna renv v analyzy/renv) a build spusť znovu.")
        return 1
    print(f"94_check_obrazky: {checked} obrázků z kapitol je novějších než jejich skripty a vstupy.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
