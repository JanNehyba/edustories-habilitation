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
- `k3_wide.csv` — hodnocení třetí etapy (řez K3_freeze_2026-09-08): id,
  anotátorka A2/A12, kvalita, dopad, vhodnost, příznaky komentářů, délky
  částí; žádný text. Studie 4.
- `k1_k3_pary.csv` — kazuistiky s kódováním první i třetí etapy (id, štítky
  K1 pod pseudonymy, hodnocení K3; žádný text). Studie 4.
- `k3_predikce_raw.csv` — predikce dopadu jazykovým modelem (id, model, varianta,
  předpověď, hodnocení obou anotátorek; žádný text). Oddíl 8.6.
- `k1_rez_ids.csv` — řez K1 (1 359 kazuistik): identifikátory, kategorie
  chování, řešení a dopadu a příznak diagnózy; bez textu i bez otisku textu.
- `anotace_long_k*.csv`, `*_ids.csv`, `truncated_uids.csv` —
  odvozené anotační a pomocné tabulky.

## Co tu NENÍ a proč
**Plný korpus kazuistik (texty ~3 200 případů) není součástí companionu.**
Obsahuje i nezveřejněné případy a je to hodnotné dílo dostupné přes platformu
projektu, nikoli k volnému stažení. Analýzy proto běží z odvozených metadat
výše, která text nepotřebují; doslovné citace jsou vytištěné přímo v knize.
Kurátorovaný anotovaný **výběr** korpusu v angličtině je na Hugging Face
(`MU-NLPC/Edustories-en`) pod tam uvedenou licencí.

## Podmínky užití
Celý repozitář je pod licencí **CC BY-NC 4.0** (ověření a nekomerční výzkum
s uvedením zdroje; viz `LICENSE` v kořeni repozitáře).
Plný korpus tomuto režimu NEpodléhá a není součástí repozitáře.
Významy sloupců dokumentuje kniha (kap. 4, příloha C).
