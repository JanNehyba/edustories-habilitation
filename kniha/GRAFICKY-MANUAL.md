# Grafický manuál knihy (habilitace-2)

Závazná pravidla vizuální podoby knihy a všech figur. Kostra převzata
z habilitace-1, role barev jsou vlastní (jiný obsah knihy). Figury vznikají
VÝHRADNĚ kódem (`analyzy/scripts/theme_book.R` + `fig_*.R`), nikdy ručně
ani generativně (jedinou plánovanou výjimkou je obálka).

## Barvy

| Role | Barva | HEX | Užití |
|---|---|---|---|
| ZÁKLAD knihy | MUNI modrá | `#0000DC` | nadpisy, externí odkazy, neutrální prvky |
| **UČITEL / lidské** | MUNI modrá | `#0000DC` | vše, co pochází od učitelů a lidských anotátorek |
| **AI / LLM / generované** | PdF oranžová | `#FF7300` | vše, co pochází z jazykového modelu |
| Kampaň K1 | tmavě modrá | `#003366` | odstín pro první kampaň (kde je třeba odlišit kampaně) |
| Kampaň K2 | střední modrá | `#3366CC` | odstín pro druhou kampaň |
| Kampaň K3 | světle modrá | `#99BBEE` | odstín pro třetí kampaň |
| Negativní/varování | šedá | `#666666` | chybění, vyřazené, limity (nikdy červená) |

**Klíčové pravidlo knihy: učitel = modrá, AI = oranžová, KONZISTENTNĚ v celé
knize** (tabulky, figury, zvýraznění). Duální rámování knihy (pedagogika ×
metodologie) se opírá právě o tento kontrast.

## Typografie

- Text knihy: STIX Two Text; matematika STIX Two Math; sans Arial (jen figury/popisky).
- Figury: písmo bez patek (Arial/Helvetica), velikost min. 9 pt při šířce strany.
- Čísla v popiscích: desetinná čárka, tisíce mezerou (jako v próze).
- Žádný em-dash (—) ani ve figurách; en-dash (–) jen v rozsazích.

## Figury

- Generuje `analyzy/scripts/fig_*.R` (ggplot2) přes `theme_book.R`;
  `render_figures.sh` obnoví vše. Výstup: `vystupy/obrazky/kapN_nazev.pdf`
  (vektor pro sazbu) + `.png` (300 dpi, náhledy/companion).
- Podklad VŽDY manifest/analytický výstup — žádná ručně vepsaná hodnota.
- Popisek v knize: *Obrázek N.M.* + věta; zdrojová věta „Zdroj: manifest …
  (skript fig_….R)" jako u tabulek.
- Jedna myšlenka na figuru; legenda jen, když barva nese význam nad rámec
  pravidla učitel/AI.

## Sazba

- scrbook, A4, řádkování 1,5 (SD PdF 2/2021 čl. 6/2), tectonic.
- Titulní strana dle Vzoru MU: `partials/muni-titlepage-cs.tex` (MUNI modrá).
- Obálka (síťová grafika) se předřazuje po renderu (pypdf) — vznikne ve F7,
  kandidáty schvaluje Jan (J6).

<!-- ❓ Jan (J2/J6): schválit role barev a celkový vzhled na zkušebním PDF -->
