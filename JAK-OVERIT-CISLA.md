# Jak ověřit výsledky knihy

## Bez instalace

Otevřete report podle kapitoly: Studie 1 (`10_korpus.html`), Studie 2
(`20_kodovani_llm.html`), Studie 3 (`30_ai_vs_ucitel.html`) nebo Studie 4
(`40_kvalita.html`) ve složce `vystupy/reporty/`.
Výsledkové tabulky leží ve `vystupy/tabulky/`; název metriky, její hodnota,
zdrojový skript a otisk vstupu spojují číslo s výpočtem. Při přepočtu se
porovnávají hodnoty; otisk vstupního souboru se může lišit i u obsahově
shodného souboru (například podle konců řádků).

## Vlastní přepočet

Postup a závislosti uvádí [README.md](README.md). Spusťte `python reproduce.py`.
Verze balíčků R jsou v `analyzy/renv.lock`, verze balíčků Pythonu pro přípravu
dat v `analyzy/requirements-lock.txt`. Dvě veřejné vstupní tabulky Studií 2 a 3
vytváří ze syrových dat skript `analyzy/scripts/31_verejne_vstupy.R`.
Skript nevyžaduje původní texty ani API klíč, kontroluje všechny čtyři studie
a skončí chybou, pokud výsledky neodpovídají přibaleným manifestům.

## Co srovnávat

- Studie 2: archivní řádky, úplné dvojice a retrospektivní soubor bez překryvů jsou odlišné analýzy.
- Studie 3: rozlišujte prázdná hodnocení od chybějících řádků exportu; doplňkový model pracuje s úplnými dvojicemi.
- Studie 4: rozlišujte plný překryv, primární soubor bez projednaných případů a případy oběma označené jako plné.
- Predikce: neplatná odpověď je selhání, nikoli důvod vyřadit případ. Lidské čtení popsaného výstupu není totožná úloha.
- Párové intervaly rozdílů modelů zahrnují nulu; to samo nedokazuje ekvivalenci.

Přepočet statistik neověřuje pravdivost vyprávění ani správnost původní
anotace. Historické kontrolní souhrny jsou dokumentační vstupy. Původní texty,
interní kontrolní seznamy a klíče k identitám nejsou součástí tohoto balíčku.
