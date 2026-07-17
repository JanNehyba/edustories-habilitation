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
   tabulka „název metriky, hodnota". Název klíče najdete v knize
   v komentáři u každého čísla (ve zdrojovém textu kapitoly).

## Cesta 2: spustit analýzu v prohlížeči (Binder, ~10 minut)

1. Klikněte na odznak „launch binder" v README tohoto repozitáře.
   Otevře se RStudio ve vašem prohlížeči; nic se neinstaluje k vám do
   počítače.
2. V RStudiu otevřete `analyzy/notebooks/30_ai_vs_ucitel.qmd` (analýza
   Studie 3; její data jsou veřejná v balíčku OSF a jsou součástí
   prostředí).
3. Klikněte na tlačítko **Render** (případně spusťte buňky postupně).
4. Porovnejte vzniklé hodnoty s tabulkami 7.1 a 7.2 v knize.

Poznámka: notebooky 10 a 20 vyžadují neveřejné řezy korpusu (nezveřejněné
kazuistiky), proto je v Binderu spustit nelze; k nim slouží zmrazené
reporty z Cesty 1.

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
