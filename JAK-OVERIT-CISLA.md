# Jak si ověřit čísla knihy (návod pro netechnické čtenáře)

Každé analytické číslo v knize pochází z tzv. manifestu: tabulky, kterou
vygeneroval analytický notebook nad verzovaným řezem dat. Tento repozitář
obsahuje vše, co potřebujete k ověření, že čísla v knize odpovídají
výstupům analýz. Nabízíme tři cesty podle toho, kolik techniky chcete.

## Cesta 1: bez instalace čehokoli (2 minuty)

1. Otevřete složku `vystupy/reporty/` a v ní HTML report analýzy, která vás
   zajímá (`10_korpus.html` pro kapitolu 5, `20_kodovani_llm.html` pro
   kapitolu 6, `30_ai_vs_ucitel.html` pro kapitolu 7). Stačí prohlížeč.
2. V reportu najdete tytéž tabulky a hodnoty, které cituje kniha.
3. Chcete-li konkrétní číslo, otevřete manifest ve složce
   `vystupy/tabulky/` (např. `kap7_k2_shoda_cisla.csv`), což je obyčejná
   tabulka „název metriky, hodnota“. Název klíče najdete v knize
   v komentáři u každého čísla (ve zdrojovém textu kapitoly).

## Cesta 2: spustit analýzu v prohlížeči (Binder, ~15 minut poprvé)

1. Klikněte na odznak „launch binder“ v README tohoto repozitáře. Poprvé se
   prostředí sestaví (~15 minut), pak se otevře RStudio ve vašem prohlížeči;
   nic se neinstaluje k vám do počítače.
2. **Všechny tři studie běží rovnou** z veřejných dat repozitáře. Otevřete
   notebook a klikněte na **Render**, pak porovnejte hodnoty s knihou:
   - `10_korpus.qmd` (Studie 1, kap. 5): z odvozené tabulky počtů slov a věku,
     bez textů kazuistik;
   - `20_kodovani_llm.qmd` (Studie 2, kap. 6): z kategorií přiřazených člověkem
     a modelem, bez textů a jmen;
   - `30_ai_vs_ucitel.qmd` (Studie 3, kap. 7): z tabulky hodnocení dvojic řešení
     (anotátorky pod pseudonymy A1–A6, bez textů).

Poznámka: v logu RStudia se mohou objevit hlášky „checkSpelling / iconv“ nad
českými slovy. Jsou neškodné (jen kontrola pravopisu neumí diakritiku) a na
výpočty ani render nemají vliv.

## Cesta 3: lokálně (pro technické čtenáře)

```bash
./reproduce.sh          # ověří prostředí, přepočítá figury a brány
```

Skript `analyzy/scripts/95_check_cisla.py` zkontroluje, že každé tvrdé
číslo v próze knihy má kotvu na klíč manifestu a že se hodnoty shodují;
`96_check_references.py` zkontroluje citace proti seznamu literatury.

## Co znamená, když se čísla neshodují

Neshoda mezi prózou a manifestem je chyba a budeme rádi, když ji nahlásíte
(kontakt v README). Brány 95/96 běží před každým sestavením knihy, takže
publikovaná verze by měla být vždy konzistentní.
