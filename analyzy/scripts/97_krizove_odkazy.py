"""Brána a nástroj pro vnitřní odkazy v kapitoly/cs (převzato z revize habilitace 1, 12. 10. 2026).

1. Každý číslovaný nadpis dostane kotvu: `# 5. …` → {#sec-kap-5}, `## 5.4 …` → {#sec-5-4},
   `# Příloha B. …` → {#sec-priloha-b}, `## B.2 …` → {#sec-b-2}.
2. Textové odkazy v próze („v oddílu 5.4", „příloha B", „kapitola 8", „kap. 7.3", „příloha A.3")
   se převedou na vnitřní hypertextové odkazy `[v oddílu 5.4](#sec-5-4)`; v PDF jsou klikací.
3. Existující kotva u nadpisu zůstává i po přečíslování; čísla v textu odkazů se odvozují
   z cílového nadpisu, takže po přečíslování stačí skript spustit znovu (`--apply`).
4. Bez `--apply` jen kontroluje. Návratový kód 1, když odkaz míří na neexistující kotvu,
   nebo (s `--prisne`, tak ho volá build.sh) když v próze zůstal textový odkaz bez hypertextu.

Nemění nadpisy (kromě doplnění kotvy), HTML komentáře, metadata (řádky začínající „>"),
bloky kódu, kontrolní seznamy, seznam literatury ani text uvnitř existujících odkazů.
Přeskakuje odkazy na kapitoly cizích prací v citacích („(Autor, 2020, kap. 3)").
Zachovává konce řádků souboru (CRLF/LF).

Úpravy proti habilitaci 1: přílohy mají v nadpisu tečku („Příloha A. …"), bloky kódu
a kontrolní seznamy se přeskakují, přísný režim pro textové odkazy bez hypertextu.

Užití: python habilitace-2/analyzy/scripts/97_krizove_odkazy.py [--apply] [--prisne] [--chapters kapitoly/cs]
"""
import argparse
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
ap = argparse.ArgumentParser()
ap.add_argument("--chapters", default=str(pathlib.Path(__file__).resolve().parents[2] / "kapitoly" / "cs"))
ap.add_argument("--apply", action="store_true")
ap.add_argument("--prisne", action="store_true", help="textový odkaz bez hypertextu je chyba")
args = ap.parse_args()
root = pathlib.Path(args.chapters)
files = [p for p in sorted(root.glob("*.md")) if p.name not in ("99-references.md",)]

H_CHAP = re.compile(r"^(# )(\d+)\. (.+?)(\s*\{#[^}]+\})?\s*$")
H_SEC = re.compile(r"^(#{2,4} )(\d+(?:\.\d+)+) (.+?)(\s*\{#[^}]+\})?\s*$")
H_APP = re.compile(r"^(# )Příloha ([A-E])([.:]) (.+?)(\s*\{#[^}]+\})?\s*$")
H_APPSEC = re.compile(r"^(#{2,4} )([A-E](?:\.\d+)+) (.+?)(\s*\{#[^}]+\})?\s*$")
H_SKIP = re.compile(r"^#{1,4} .*(?:Kontrolní seznam|Literatura)")


def sec_id(num):
    if re.fullmatch(r"[A-E](\.\d+)+", num):
        return "sec-" + num.lower().replace(".", "-")
    return "sec-" + num.replace(".", "-")


def keep(group):
    """Existující kotva zůstává (stabilní id i po přečíslování oddílu)."""
    return group.strip()[2:-1] if group else None


# --- 1. kotvy nadpisů + mapa id -> číslo (id se přidělí jen nadpisům bez kotvy)
targets = {}
texts = {}
noanchor = []
for p in files:
    raw = p.read_bytes().decode("utf-8")
    nl = "\r\n" if "\r\n" in raw else "\n"
    out = []
    in_code = False
    for line in raw.split(nl):
        if line.lstrip().startswith("```"):
            in_code = not in_code
        if in_code or H_SKIP.match(line):
            out.append(line)
            continue
        m = H_CHAP.match(line)
        if m:
            i = keep(m.group(4)) or f"sec-kap-{m.group(2)}"
            targets[i] = m.group(2)
            line = f"{m.group(1)}{m.group(2)}. {m.group(3)} {{#{i}}}"
        elif (m := H_APP.match(line)):
            i = keep(m.group(5)) or f"sec-priloha-{m.group(2).lower()}"
            targets[i] = m.group(2)
            line = f"{m.group(1)}Příloha {m.group(2)}{m.group(3)} {m.group(4)} {{#{i}}}"
        else:
            for rx in (H_SEC, H_APPSEC):
                m = rx.match(line)
                if m:
                    i = keep(m.group(4)) or sec_id(m.group(2))
                    targets[i] = m.group(2)
                    line = f"{m.group(1)}{m.group(2)} {m.group(3)} {{#{i}}}"
                    break
        out.append(line)
    texts[p] = (raw, nl, out)
    noanchor += [f"{p.name}: {a}" for a, b in zip(raw.split(nl), out) if a != b]

# --- 2. textové odkazy -> hypertext
WORD_APP = r"(?:[Pp]říloh(?:a|y|e|u|ou|ách|ám))"
WORD_SEC = r"(?:[Oo]ddíl(?:u|e|ech|ům|y|ů|em)?|[Pp]ododdíl(?:u|e|em)?)"
WORD_KAP = r"(?:[Kk]apitol(?:a|y|e|u|ou|ách|ám)|kap\.)"
NUM = r"\d+(?:\.\d+)*"
RX_APP = re.compile(rf"\b({WORD_APP}) ([A-E])\b(?![.\d])")
RX_APP_SEC = re.compile(rf"\b({WORD_APP}|{WORD_SEC}) ([A-E](?:\.\d+)+)\b")
RX_SEC = re.compile(rf"\b({WORD_SEC}|{WORD_KAP}) ({NUM})(?:–(\d+(?:\.\d+)*))?\b")
LINK = re.compile(r"\[[^\]]*\]\([^)]*\)")
CITE = re.compile(r"\([^()]*\b(?:19|20)\d{2}[a-z]?,[^()]*\)")  # (Autor, 2020, kap. 3)
missing, plain = [], []


def protect(line):
    """Úseky, na které se nesahá: existující odkazy, inline kód, citace cizích prací."""
    return ([m.span() for m in LINK.finditer(line)]
            + [m.span() for m in re.finditer(r"`[^`]*`", line)]
            + [m.span() for m in CITE.finditer(line)]
            + [m.span() for m in re.finditer(r"<!--.*?-->", line)])


def inside(pos, spans):
    return any(a <= pos < b for a, b in spans)


def target_of(word, num, kind):
    if kind == "app":
        return f"sec-priloha-{num.lower()}"
    if kind == "appsec":
        return sec_id(num)
    if "." not in num and word.lower().startswith("kap"):
        return f"sec-kap-{num}"
    return sec_id(num)


def link_line(line, fname, lineno):
    for rx, kind in ((RX_APP_SEC, "appsec"), (RX_APP, "app"), (RX_SEC, "sec")):
        spans = protect(line)
        res, last = [], 0
        for m in rx.finditer(line):
            if inside(m.start(), spans):
                continue
            tid = target_of(m.group(1), m.group(2), kind)
            if tid not in targets:
                missing.append(f"{fname}:{lineno}: „{m.group(0)}“ → {tid} neexistuje")
                continue
            res.append(line[last:m.start()] + f"[{m.group(0)}](#{tid})")
            last = m.end()
        if res:
            line = "".join(res) + line[last:]
    return line


def prose_lines(lines):
    """(číslo řádku, řádek, je_próza) – próza = mimo kód, komentáře, metadata, nadpisy,
    kontrolní seznamy a seznam literatury."""
    in_code = in_comment = in_skip = False
    for n, line in enumerate(lines, 1):
        s = line.lstrip()
        if s.startswith("```"):
            in_code = not in_code
            yield n, line, False
            continue
        if in_code:
            yield n, line, False
            continue
        if in_comment or (s.startswith("<!--") and "-->" not in s):
            in_comment = "-->" not in s if not in_comment else "-->" not in line
            yield n, line, False
            continue
        if re.match(r"^#{1,4} ", line):
            in_skip = bool(H_SKIP.match(line))
            yield n, line, False
            continue
        yield n, line, not (in_skip or s.startswith(">"))


for p, (raw, nl, out) in texts.items():
    new = [link_line(line, p.name, n) if prose else line for n, line, prose in prose_lines(out)]
    # 3. srovnat čísla v textech existujících odkazů s cílem
    fixed = []
    for line in new:
        def relabel(m):
            label, tid = m.group(1), m.group(2)
            if tid not in targets:
                missing.append(f"{p.name}: odkaz na neexistující #{tid} („{label}“)")
                return m.group(0)
            num = targets[tid]
            label2 = re.sub(r"(\s)([A-E](?:\.\d+)*|\d+(?:\.\d+)*)(–\d+(?:\.\d+)*)?$",
                            lambda k: k.group(1) + num + (k.group(3) or ""), label)
            return f"[{label2}](#{tid})"
        fixed.append(re.sub(r"\[([^\]]+)\]\(#(sec-[\w-]+)\)", relabel, line))
    new_raw = nl.join(fixed)
    # bez --apply se hlásí odkazy bez hypertextu v souboru tak, jak je; s --apply jen ty,
    # které nešlo převést (cíl neexistuje)
    for n, line, prose in prose_lines(fixed if args.apply else out):
        if not prose:
            continue
        spans = protect(line)
        for rx in (RX_APP_SEC, RX_APP, RX_SEC):
            for m in rx.finditer(line):
                if not inside(m.start(), spans):
                    plain.append(f"{p.name}:{n}: {m.group(0)}")
    if args.apply and new_raw != raw:
        p.write_bytes(new_raw.encode("utf-8"))
        print(f"zapsáno: {p.name}")

if args.apply:
    noanchor = []
print(f"kotev: {len(targets)}; nadpisů bez kotvy: {len(noanchor)}; visících odkazů: {len(missing)}; "
      f"textových odkazů bez hypertextu: {len(plain)}")
for x in noanchor[:20]:
    print("  bez kotvy:", x)
for x in missing:
    print("  VISÍ:", x)
for x in plain[:60]:
    print("  bez odkazu:", x)
fail = bool(missing) or (args.prisne and bool(plain or noanchor))
sys.exit(1 if fail else 0)
