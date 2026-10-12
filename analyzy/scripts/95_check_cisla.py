#!/usr/bin/env python3
"""Brána čísel: próza ↔ výstupy analýz (verze 12. 10. 2026).

Převzato z revize habilitace 1 (rozhodnutí D30: každé tvrdé číslo v próze se hledá
ve výstupech analýz) a sloučeno s dosavadní kontrolou kotev habilitace 2.

Kontroluje v `kapitoly/cs/*.md` (mimo 99-references.md):
1. KOTVY `<!-- manifest <soubor>: <klic>=<hodnota> -->`:
   - manifest `vystupy/tabulky/<soubor>.csv` existuje a klíč v něm je,
   - hodnota kotvy odpovídá manifestu (po zaokrouhlení na přesnost kotvy),
   - poslední tvrdé číslo před kotvou odpovídá manifestu (próza = kotva).
2. KAŽDÉ DALŠÍ TVRDÉ ČÍSLO v próze se automaticky hledá ve všech výstupech analýz
   (každá buňka všech `vystupy/tabulky/*.csv`, manifesty i datové tabulky). Shoda po
   zaokrouhlení výstupu na přesnost prózy; u procent i podíl ×100; celá čísla přesně;
   záporné hodnoty i v absolutní hodnotě. Nenalezené číslo = chyba.
3. Číslo bez vlastní kotvy, které se ve výstupech najde, je v přísném režimu (`--kotvy`,
   tak ho volá build.sh) také chyba: hlášení uvede, ve kterém výstupu se číslo našlo,
   aby šlo doplnit kotvu. Bez `--kotvy` se jen vypíše jako upozornění.
4. Výjimka `<!-- necislo: důvod -->` kryje jen JEDNO číslo bezprostředně před sebou
   (údaj z literatury, nastavení analýzy, identifikátor). Dříve krylo celý úsek od
   předchozí kotvy, takže pod ním mohla projít i analytická čísla.

Tvrdé číslo = desetinné (0,64), procento (72 %), N s mezerou (1 319), celé číslo ≥ 20.
Mimo záběr: roky 1900–2099, rozsahy škál (1–4, −2..+2), čísla u odkazů na tabulku,
obrázek, kapitolu, oddíl, přílohu, studii, etapu (K1–K3), řez (S1–S7), pseudonym (A1–A12),
HTML komentáře, inline kód, odkazy, nadpisy, blockquoty, kód a kontrolní seznamy.

Užití: python habilitace-2/analyzy/scripts/95_check_cisla.py [--kotvy] [--warn] [--verbose] [soubor.md …]
Exit 1 = neshoda kotvy, číslo nenalezené ve výstupech, nebo (s --kotvy) číslo bez kotvy.
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from bisect import bisect_left
from pathlib import Path

HERE = Path(__file__).resolve()
DEFAULT_CHAPTERS = HERE.parents[2] / "kapitoly" / "cs"
DEFAULT_TABULKY = HERE.parents[2] / "vystupy" / "tabulky"

# klíč smí obsahovat dvojtečku, lomítko, mezery i diakritiku (názvy kategorií);
# hodnota je token bez mezery před koncem kotvy.
ANCHOR = re.compile(r"<!--\s*manifest\s+([\w\-\.]+?)(?:\.csv)?\s*:\s*(.+?)\s*=\s*([^\s>]+)\s*-->")
# necislo smí nést zdůvodnění za dvojtečkou: <!-- necislo: proč -->
SUPPRESS = re.compile(r"<!--\s*necislo\b[^>]*-->")

SP = "[   ]"  # mezera, NBSP, úzká NBSP (oddělovač tisíců)
# tvrdá čísla (v pořadí priorit)
NUM_PATTERNS = [
    re.compile(r"[−\-]?\d+[.,]\d+\s?%"),                     # desetinné procento (4,7 %)
    re.compile(r"[−\-]?\d+[.,]\d+"),                         # desetinné (0,64 / -0.85)
    re.compile(r"\d{1,3}(?:" + SP + r"\d{3})+(?:[.,]\d+)?"),  # 1 319 (mezera v tisících)
    re.compile(r"\d+\s?%"),                                  # 72 % / 72%
    re.compile(r"\b\d{2,}\b"),                               # celá čísla (filtr níže: ≥ 20)
]
YEAR_RE = re.compile(r"\b(?:19|20)\d{2}[a-z]?\b")
# kontexty, kde číslo NENÍ tvrdý údaj
SOFT_CONTEXT = re.compile(
    r"(?:Tabulk[aáue]\w*|Obrázk?[uůey]?\w*|Obrázek|kapitol\w*|Kapitol\w*|RQ|přílo[hz]\w*|Přílo[hz]\w*|"
    r"§|Studi[eií]\w*|verz\w*|List|škál[aey]?\s*\d|krok\w*|oddíl\w*|www|http|doi|ISBN|"
    r"K[123]\b|S[1-7]\b|A\d{1,2}\b|F[0-9]\b|J[0-9]\b|P[0-9]\b|E[0-9]\b|D[0-9]\b)",
)
RANGE_RE = re.compile(r"[−\-]?\d+\s*[–\-\.]{1,2}\s*[−\-+]?\d+")  # 1–4, −2..+2
CI_BOILER = re.compile(r"95\s?%\s?(?:CI|interval)")  # „95% CI" = statistická vata, ne údaj


def to_float(tok: str) -> float | None:
    s = re.sub(SP, "", tok).replace(",", ".").replace("−", "-").rstrip("%").strip()
    try:
        return float(s)
    except ValueError:
        return None


def load_manifests(tabulky: Path) -> dict[str, dict[str, str]]:
    out: dict[str, dict[str, str]] = {}
    for f in tabulky.glob("*_cisla.csv"):
        d: dict[str, str] = {}
        with f.open(encoding="utf-8") as fh:
            rd = csv.DictReader(fh)
            cols = rd.fieldnames or []
            kcol = "nazev" if "nazev" in cols else ("metric" if "metric" in cols else cols[0])
            vcol = "hodnota" if "hodnota" in cols else ("value" if "value" in cols else cols[1])
            for r in rd:
                d[str(r[kcol]).strip()] = str(r[vcol]).strip()
        out[f.stem] = d
    return out


def build_index(tabulky: Path) -> tuple[list[float], dict[float, str], int]:
    """Všechna čísla ze všech buněk výstupních tabulek (seřazená) + první soubor výskytu."""
    where: dict[float, str] = {}
    nfiles = 0
    for f in sorted(tabulky.glob("*.csv")):
        nfiles += 1
        with f.open(encoding="utf-8", newline="") as fh:
            for row in csv.reader(fh):
                for cell in row:
                    v = to_float(cell)
                    vals = []
                    if v is not None:
                        vals.append(v)
                        if "e" in cell.lower():  # 6.69e-16 -> próza „6,7 × 10⁻¹⁶“
                            vals.append(float(cell.lower().split("e")[0]))
                    else:  # buňky typu „0.81 [0.78, 0.84]“ nebo „44.2%“
                        for m in re.finditer(r"[−\-]?\d+(?:[.,]\d+)?", cell):
                            w = to_float(m.group(0))
                            if w is not None:
                                vals.append(w)
                    for w in vals:
                        for x in {w, abs(w)}:
                            where.setdefault(x, f.name)
    return sorted(where), where, nfiles


def lookup(tok: str, index: list[float], where: dict[float, str]) -> str | None:
    """Vrátí název výstupu, kde se číslo z prózy našlo (po zaokrouhlení), jinak None."""
    x = to_float(tok)
    if x is None:
        return "—"
    norm = re.sub(SP, "", tok).replace(",", ".").replace("−", "-").rstrip("%").strip()
    dec = len(norm.split(".")[1]) if "." in norm else 0
    is_pct = tok.strip().endswith("%")
    half = 10 ** (-dec) / 2 + 1e-9
    targets = {abs(x)}
    probes = [(t, 1.0) for t in targets]
    if is_pct:
        probes += [(t / 100, 100.0) for t in targets]
    for t, scale in probes:
        if dec == 0 and not is_pct:
            if t in where:
                return where[t]
            continue
        lo, hi = t - half / scale, t + half / scale
        i = bisect_left(index, lo - 1e-12)
        while i < len(index) and index[i] <= hi + 1e-12:
            v = index[i]
            if abs(round(v * scale, dec) - t * scale) < half:
                return where[v]
            i += 1
    return None


def num_equal(anchor_val: str, manifest_val: str) -> bool:
    is_pct = anchor_val.strip().endswith("%")

    def norm(x: str) -> str:
        return re.sub(SP, "", x).replace(",", ".").replace("−", "-").rstrip("%")
    a, m = norm(anchor_val), norm(manifest_val)
    try:
        fa, fm = float(a), float(m)
    except ValueError:
        return anchor_val.strip() == manifest_val.strip()
    if is_pct and abs(fm) <= 1:  # „72 %“ v próze vs podíl v manifestu
        fm = fm * 100
    dec = len(a.split(".")[1]) if "." in a else 0  # zaokrouhlení manifestu na přesnost kotvy
    return abs(round(fm, dec) - fa) < 10 ** (-dec) / 2 + 1e-12


def hard_numbers(text: str) -> list[str]:
    """Tvrdá čísla v úseku textu v pořadí výskytu (po odstranění měkkých kontextů)."""
    s = re.sub(r"<!--.*?-->", " ", text)
    s = re.sub(r"`[^`]*`", " ", s)  # inline kód (`99-references.md` apod.)
    s = re.sub(r"!\[[^\]]*\]\([^)]*\)|\]\([^)]*\)", " ", s)  # cíle odkazů a obrázky
    s = re.sub(r"\{[#.][^}]*\}", " ", s)  # atributy {#sec-…}
    s = CI_BOILER.sub(" ", s)
    s = YEAR_RE.sub(" ", s)
    s = RANGE_RE.sub(" ", s)
    # odstranit čísla přilepená k měkkému kontextu (Tabulka 6.1, RQ2, kap. 5…)
    for m in list(SOFT_CONTEXT.finditer(s)):
        s = s[: m.start()] + " " * (m.end() - m.start()) + re.sub(
            r"^[\s\.\[]*[\d\.,]+", lambda x: " " * len(x.group(0)), s[m.end():], count=1)
    found: list[tuple[int, str]] = []
    taken: list[tuple[int, int]] = []
    for pat in NUM_PATTERNS:
        for m in pat.finditer(s):
            if any(a < m.end() and m.start() < b for a, b in taken):
                continue
            tok = m.group(0)
            if pat is NUM_PATTERNS[-1] and int(tok) < 20:  # celá čísla
                continue
            taken.append((m.start(), m.end()))
            found.append((m.start(), tok))
    return [t for _, t in sorted(found)]


def paragraphs(path: Path):
    """(číslo prvního řádku, spojený text odstavce); přeskočí kód, blockquoty, nadpisy
    a kontrolní seznam. Čeština láme věty přes řádky, číslo a kotva tak mohou být
    na různých řádcích."""
    in_code = in_checklist = False
    buf: list[str] = []
    start = None
    for ln, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        stripped = line.strip()
        if re.match(r"#{2,}\s*Kontrolní seznam", stripped):
            in_checklist = True
        elif line.startswith("#"):
            in_checklist = False
        if stripped.startswith("```"):
            in_code = not in_code
            continue
        skip = in_code or in_checklist or line.lstrip().startswith((">", "#"))
        if not stripped or skip:
            if buf:
                yield start, " ".join(buf)
                buf, start = [], None
            continue
        if start is None:
            start = ln
        buf.append(line)
    if buf:
        yield start, " ".join(buf)


def check_file(path, manifests, index, where):
    """Vrátí (chyby, čísla bez kotvy nalezená ve výstupech, počet kontrolovaných čísel)."""
    errors: list[str] = []
    unanchored: list[str] = []
    n = 0
    marker = re.compile(ANCHOR.pattern + "|" + SUPPRESS.pattern)
    for ln, text in paragraphs(path):
        pos = 0
        segments = []  # (úsek, typ značky za ním, shoda)
        for am in marker.finditer(text):
            segments.append((text[pos:am.start()], am))
            pos = am.end()
        segments.append((text[pos:], None))
        for seg, am in segments:
            nums = hard_numbers(seg)
            covered = None
            if am is not None and am.group(1) is None:      # necislo: kryje jen poslední číslo
                covered = nums.pop() if nums else None
            elif am is not None:                            # kotva
                mf, key, val = am.group(1), am.group(2), am.group(3)
                man = manifests.get(mf) or manifests.get(mf + "_cisla")
                if man is None:
                    errors.append(f"{path.name}:{ln}: kotva na neexistující manifest „{mf}“")
                elif key not in man:
                    errors.append(f"{path.name}:{ln}: klíč „{key}“ není v manifestu {mf}")
                elif not num_equal(val, man[key]):
                    errors.append(f"{path.name}:{ln}: NESHODA {mf}:{key}, kotva {val} vs manifest {man[key]}")
                elif nums and not num_equal(nums[-1], man[key]):
                    errors.append(f"{path.name}:{ln}: PRÓZA {nums[-1]} ≠ manifest {mf}:{key}={man[key]}")
                if nums:
                    covered = nums.pop()
                    n += 1
            for tok in nums:
                n += 1
                src = lookup(tok, index, where)
                i = seg.find(tok)
                ctx = re.sub(r"\s+", " ", re.sub(r"<!--.*?-->", "", seg[max(0, i - 50): i + len(tok) + 30])).strip()
                if src is None:
                    errors.append(f"{path.name}:{ln}: „{tok}“ není ve výstupech analýz | …{ctx}…")
                else:
                    unanchored.append(f"{path.name}:{ln}: „{tok}“ bez kotvy (nalezeno v {src}) | …{ctx}…")
            del covered
    return errors, unanchored, n


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*", type=Path)
    ap.add_argument("--chapters", type=Path, default=DEFAULT_CHAPTERS)
    ap.add_argument("--tabulky", type=Path, default=DEFAULT_TABULKY)
    ap.add_argument("--kotvy", action="store_true", help="číslo bez kotvy je chyba i když je ve výstupech")
    ap.add_argument("--warn", action="store_true", help="jen varovat, nevracet chybu")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

    manifests = load_manifests(args.tabulky)
    index, where, nfiles = build_index(args.tabulky)
    # 99-references.md je bibliografie (čísla svazků/stran/DOI), mimo záběr
    files = args.files or sorted(args.chapters.glob("*.md"))
    files = [f for f in files if f.name != "99-references.md"]
    errors: list[str] = []
    unanchored: list[str] = []
    n_checked = n_anchors = 0
    for f in files:
        n_anchors += len(ANCHOR.findall(f.read_text(encoding="utf-8")))
        e, u, n = check_file(f, manifests, index, where)
        errors += e
        unanchored += u
        n_checked += n
    if args.kotvy:
        errors += [x + " → doplň kotvu" for x in unanchored]

    print(f"95_check_cisla: {len(files)} souborů, {n_checked} tvrdých čísel, {n_anchors} kotev; "
          f"hledáno v {nfiles} výstupech ({len(index)} různých hodnot).")
    if unanchored and (args.verbose or not args.kotvy):
        print(f"\n⚠️  čísla bez kotvy nalezená ve výstupech ({len(unanchored)}):")
        for x in unanchored:
            print("   " + x)
    if errors:
        print(f"\n❌ PROBLÉMY ({len(errors)}):")
        for e in errors:
            print("   " + e)
    else:
        print("✅ každé tvrdé číslo v textu je kotvené a shodné s výstupy analýz."
              if args.kotvy or not unanchored else
              "✅ každé tvrdé číslo v textu se našlo ve výstupech analýz.")
    return 0 if (not errors or args.warn) else 1


if __name__ == "__main__":
    sys.exit(main())
