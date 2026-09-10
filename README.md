# Edustories: doprovodný repozitář habilitační monografie

Pracovní verze monografie Jana Nehyby *Náročné chování žáků v době AI*.
Nejde o oficiální podání ani o stanovisko habilitační komise.

## Obsah

- Čtyři hotové HTML reporty v `vystupy/reporty/`.
- Odvozené tabulky bez úplných textů kazuistik v `data/processed/`.
- Analýzy v R, uložené predikce a jejich offline přepočet v Pythonu.
- Výsledkové tabulky a obrázky.
- Návod: [JAK-OVERIT-CISLA.md](JAK-OVERIT-CISLA.md).

## Opakování výpočtů

Vyžaduje Python 3.11 nebo novější, R 4.6.1 a Quarto na PATH.
Ověřená prostředí popisují `requirements.txt`, `analyzy/renv.lock`
a `vystupy/tabulky/R-session-info.txt`.

```sh
python -m pip install -r requirements.txt
python reproduce.py
```

Skript obnoví R balíčky, přepočítá uložené predikce i všechny čtyři studie,
vytvoří obrázky a zkontroluje výsledky proti přibaleným manifestům.
Při chybě skončí neúspěšně, žádnou studii tiše nepřeskočí.
Obnova balíčků může potřebovat internet; analýzy nevolají modelové API.
Přepínač `--skip-restore` použije již nainstalované R balíčky bez obnovy verzí.

## Rozsah ověřitelnosti

Reprodukce ověřuje výpočty z poskytnutých odvozených dat. Neopakuje původní
lidské kódování, generování odpovědí, anonymizaci ani textovou kontrolu úniku.
Historické monitorovací, adjudikační a provenienční souhrny jsou označené
vstupy; bez neveřejných textů je nelze znovu nezávisle vytvořit.
Skript `26_k3_predikce_llm.py` dokumentuje nový experiment, není součástí
offline reprodukce a vyžaduje další vstupy a oprávnění.
Kapitoly 4, 6 a 8 rozlišují tato omezení od statistické reprodukce.

Veřejná tabulka K2 používá vlastní lokální pseudonymy A1–A6.
Nejsou převodníkem na projektové pseudonymy knihy A1–A12.
Úplná textová databáze ani dokumenty habilitačního řízení nejsou součástí
tohoto balíčku. To nepředjímá rozhodnutí o budoucím vydání databáze.
[Veřejná platforma](https://edustories.cz/) a
[anglický výběr](https://huggingface.co/datasets/MU-NLPC/Edustories-en)
jsou samostatné výstupy.

## Licence

Dosavadní licence CC BY-NC 4.0 zůstává zachována; viz `LICENSE`.
Licence tohoto repozitáře se nevztahuje na jiné výstupy projektu.
