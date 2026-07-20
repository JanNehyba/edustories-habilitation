# Edustories: companion repozitář habilitační práce

Doprovodný repozitář monografie *Náročné chování žáků v době AI: kazuistiky
z praxe a jazykové modely v pedagogickém výzkumu* (Jan Nehyba, Masarykova
univerzita, 2026). Slouží k tomu, aby si kdokoli mohl ověřit každé číslo v knize.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/JanNehyba/edustories-habilitation/HEAD?urlpath=rstudio)

## Jak si ověřit čísla knihy

Každé číslo v knize je dohledatelné ke skriptu a datům. Vyberte si podle toho,
kolik techniky chcete (podrobný návod: [JAK-OVERIT-CISLA.md](JAK-OVERIT-CISLA.md)):

**1. Bez instalace (2 minuty).** Otevřete v prohlížeči HTML report příslušné
analýzy ve složce [`vystupy/reporty/`](vystupy/reporty): `10_korpus.html`
(kap. 5), `20_kodovani_llm.html` (kap. 6), `30_ai_vs_ucitel.html` (kap. 7).
Najdete v nich tytéž tabulky a hodnoty jako v knize. Konkrétní číslo dohledáte
ve zdrojové tabulce čísel ve složce [`vystupy/tabulky/`](vystupy/tabulky) (tabulka „název
metriky, hodnota“; klíč je v knize v komentáři u každého čísla).

**2. Přepočítat v prohlížeči (Binder, ~15 min první spuštění).** Klikněte na
odznak „launch binder“ nahoře. Otevře se RStudio v prohlížeči (nic se
neinstaluje k vám). Otevřete notebook v `analyzy/notebooks/` a dejte
**Render**. Všechny tři empirické studie jsou reprodukovatelné rovnou
z veřejných dat tohoto repozitáře, bez textů kazuistik a bez jmen:
- **Studie 1** (`10_korpus.qmd`): z odvozené tabulky `kap5_perkazuistika.csv`
  (počty slov, věk, publikační status; bez textů kazuistik);
- **Studie 2** (`20_kodovani_llm.qmd`): ze `srovnani_k1_llm.csv` (kategorie
  člověka a modelu, bez textů a jmen);
- **Studie 3** (`30_ai_vs_ucitel.qmd`): z `kap7_hodnoceni_pseudo.csv`
  (hodnocení dvojic řešení; anotátorky pod pseudonymy A1–A6, bez textů).

**Pozn. k pseudonymům:** veřejný dataset Studie 3 přečíslovává svých šest
anotátorek nezávisle jako A1–A6. V knize (příloha C.1) tytéž anotátorky
vystupují v celoknižním schématu A1–A12 (Studie 3 = A1, A2, A8, A9, A10, A12).
Obě sady jsou pseudonymy a nemají mezi sebou vztah 1:1.

**3. Lokálně** (technicky): `./reproduce.sh` ověří prostředí, přepočítá figury
a spustí kontrolní brány.

## Co repozitář obsahuje a co ne

Obsahuje: analýzy v R a skripty, zdrojové tabulky čísel (jediný zdroj čísel
prózy), HTML reporty, figury, veřejnou datovou podmnožinu **bez textů kazuistik
a bez osobních údajů** (anotátorky pod pseudonymy) a build knihy.

Neobsahuje **plné texty kazuistik**: korpus zahrnuje i nezveřejněné případy
a jde o citlivá data o reálných dětech od identifikovatelných pisatelů, takže
celý řez korpusu veřejný být nemůže. Analýzy proto běží z odvozených tabulek
(počty, kategorie), které texty nepotřebují; texty jsou nutné jen pro doslovné
citace, které jsou vytištěné přímo v knize. Veřejný anotovaný výběr korpusu je
na Hugging Face: `MU-NLPC/Edustories-en`.

## Licence

- **Kód** (skripty a notebooky, build knihy): MIT (viz `LICENSE`).
- **Odvozená data** (tabulky a reporty bez textů kazuistik): CC BY-NC 4.0
  (ověření a nekomerční výzkum s uvedením zdroje; viz `DATA-LICENSE.md`).
- **Text a PDF knihy**: © Jan Nehyba, všechna práva vyhrazena (pracovní verze
  ke kontrole; kvůli chystanému knižnímu vydání bez otevřené licence).
- **Plný korpus kazuistik** není součástí repozitáře (dostupný přes platformu
  projektu). Výběr v angličtině na Hugging Face `MU-NLPC/Edustories-en` má
  vlastní licenci.

Chyby a neshody čísel hlaste v Issues tohoto repozitáře.

Průběžná pracovní verze; release s DOI vznikne až po finálním PDF knihy.
