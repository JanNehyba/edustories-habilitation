# Veřejná datová podmnožina

Odvozené tabulky **bez textů kazuistik a bez osobních údajů** (anotátorky pod
pseudonymy). Slouží k ověření čísel v knize, ne jako náhrada korpusu.

## Co tu je
- `kap5_perkazuistika.csv` — na úroveň kazuistiky: publikační status, věk,
  počty slov čtyř částí (žádný text). Studie 1.
- `srovnani_k1_llm.csv` — kategorie řešení přiřazené člověkem a modelem
  (id + štítky, žádný text). Studie 2.
- `kap7_hodnoceni_pseudo.csv` — hodnocení dvojic řešení (id, dimenze,
  hodnocení, zdroj, štítky přístupů; anotátorky A1–A6, žádný text). Studie 3.
- `anotace_long_k*.csv`, `k1_rez_ids.csv`, `*_ids.csv`, `truncated_uids.csv` —
  odvozené anotační a pomocné tabulky.

## Co tu NENÍ a proč
**Plný korpus kazuistik (texty ~3 200 případů) není součástí companionu.**
Obsahuje i nezveřejněné případy a je to hodnotné dílo dostupné přes platformu
projektu, nikoli k volnému stažení. Analýzy proto běží z odvozených metadat
výše, která text nepotřebují; doslovné citace jsou vytištěné přímo v knize.
Kurátorovaný anotovaný **výběr** korpusu v angličtině je na Hugging Face
(`MU-NLPC/Edustories-en`) pod tam uvedenou licencí.

## Podmínky užití
Odvozené tabulky v této složce lze užít k ověření a nekomerčnímu výzkumu
s uvedením zdroje (kniha + companion). Plný korpus tomuto režimu NEpodléhá.
❓ Autor doplní explicitní licenční soubor (LICENSE) před veřejným releasem.
Významy sloupců dokumentuje kniha (kap. 4, příloha C).
