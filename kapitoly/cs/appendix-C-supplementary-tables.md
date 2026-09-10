# Příloha C. Doplňkové tabulky

> GENEROVÁNO SKRIPTEM 2026-09-10 – NEEDITOVAT RUČNĚ, regenerovat skriptem 17

Tato příloha dokládá registr anotačních událostí,
přehled velikostí datových řezů a přehled měr shody.
Úplná matice pokrytí (kazuistika × událost) je dostupná v doprovodném
repozitáři jako tabulka pokrytí; zde uvádíme agregáty. Počty
kazuistik se vztahují k záznamům spárovaným na jednotný identifikátor
(kapitola 4); počty řádků v původních anotačních souborech se mohou
mírně lišit o záznamy, které se spárovat nepodařilo.

## C.1 Registr anotačních událostí

**Tabulka C.1.** Anotační události tří etap (anotátorky pod anonymizovanými pseudonymy A1–A12).

Číslo pseudonymu odpovídá pořadí, v němž se anotátorka zapojila do projektu jako celku, nikoli pořadí uvnitř jednotlivé etapy. Táž osoba proto vystupuje pod týmž projektovým pseudonymem ve všech kapitolách; ve třetí etapě tak vedle sebe stojí A2 a A12. Veřejná tabulka K2 používá samostatné lokální pseudonymy A1–A6. Jejich čísla nejsou převodníkem na projektové pseudonymy ani prostředkem propojování osob.

```{=latex}
\footnotesize
```

| Událost | Období | Etapa a fáze | Anotátorky | Kazuistik | Poznámka |
|:------------------|:-------|:---------|:-----------|:-------|:----------------|
| `–` | prosinec 2023 – únor 2024 | K1 zácvik (pokus) | A1, A2, A5, A6 | – | kvalitativní kódy bez matice; kódovací kniha, strom V1→V2 |
| `k1_test_03_24` | březen 2024 | K1 test | pět anotátorek | 10 <!-- manifest priloha_c_cisla: c1_k1_test_03_24=10 --> |  |
| `k1_test_04_24` | duben 2024 | K1 test | A1–A4, A7 | 10 <!-- manifest priloha_c_cisla: c1_k1_test_04_24=10 --> |  |
| `k1_naostro_05_24` | od května 2024 | K1 finál | A1–A4, A7 | 1 344 <!-- manifest priloha_c_cisla: c1_k1_naostro_05_24=1344 --> | dělba práce s vestavěným překryvem; anotační listy obsahují 1 413 kazuistik, <!-- necislo: registr událostí --> z nichž 69 <!-- necislo: rozdíl 1413−1344 --> se nepodařilo spárovat přes text popisu |
| `llm_anotace_matice_08_24` | srpen 2024 | K1 konsolidace | – | 1 377 <!-- manifest priloha_c_cisla: c1_llm_anotace_matice_08_24=1377 --> | lidské kódy K1 sloučené do matice korpusu (provenience ověřena, kap. 4) |
| `k2_setkani10_04_25` | duben 2025 | K2 zácvik | A1, A2, A8–A11 | 10 <!-- manifest priloha_c_cisla: c1_k2_setkani10_04_25=10 --> |  |
| `k2_anotace40_04_25` | duben 2025 | K2 zácvik 2 | A1, A2, A8–A12 | 38 <!-- manifest priloha_c_cisla: c1_k2_anotace40_04_25=38 --> |  |
| `–` | červen 2025 | K2 příprava | gpt-4o (strojově) | – | generace srovnávacích řešení, ne anotace |
| `k2_final351_06_25` | červen 2025 | K2 finál | A1, A2, A8, A9, A10, A12 | 309 <!-- manifest priloha_c_cisla: c1_k2_final351_06_25=309 --> | zaslepené hodnocení dvojic řešení; hodnoceno 351 <!-- necislo: registr událostí --> identifikátorů, autoritativní analytický soubor čítá 324 <!-- manifest kap7_k2_shoda_cisla: n_kazuistik=324 --> kazuistik (kapitola 7); zde uvedený počet = spárované na jednotný identifikátor |
| `k3_zacvik_26` | jaro 2026 | K3 zácvik | A2, A12 | 6 <!-- manifest priloha_c_cisla: c1_k3_zacvik_26=6 --> |  |
| `k3_pilot1_26` | jaro 2026 | K3 pilot 1 | A2, A12 | 19 <!-- manifest priloha_c_cisla: c1_k3_pilot1_26=19 --> |  |
| `k3_pilot2_26` | jaro 2026 | K3 pilot 2 | A2, A12 | 49 <!-- manifest priloha_c_cisla: c1_k3_pilot2_26=49 --> |  |
| `k3_final_26` | březen až září 2026 | K3 finál | A2, A12 | 3 185 <!-- manifest priloha_c_cisla: c1_k3_final_26=3185 --> | dělba práce s vestavěným překryvem; uzavřeno řezem K3_freeze_2026-09-08 (kapitola 8) |
| `hf_publikovano_en` | září 2024 | publikace (ne anotace) | – | 1 246 <!-- manifest priloha_c_cisla: c1_hf_publikovano_en=1246 --> | veřejná datová sada, výběr z řezu srpen 2024 |

```{=latex}
\normalsize
```

*Poznámka.* Vygenerováno z matice pokrytí [skriptem přílohy C](https://github.com/JanNehyba/edustories-habilitation/blob/main/analyzy/scripts/17_priloha_c.py); metadata událostí dle datové dokumentace.

## C.2 Přehled velikostí datových řezů

**Tabulka C.2.** Čísla, která se v knize a podkladech vztahují k „velikosti dat“, a jejich vztah.

| Číslo | Co označuje | Zdroj |
|---|---|---|
| 3 202 <!-- manifest kap5_korpus_cisla: n_korpus_s6=3202 --> | zveřejněné kazuistiky, řez květen 2026 (S6) | kapitola 5 |
| 1 695 <!-- manifest kap5_korpus_cisla: rust_S4082024=1695 --> | řez srpen 2024 (S4; prostor identifikátorů druhé etapy) | kapitola 5 |
| 1 492 <!-- manifest kap5_korpus_cisla: rust_S5HFrelease=1492 --> | veřejná datová sada (kurátorovaný výběr z S4); záznamy výběru odpovídají 1 246 <!-- manifest priloha_c_cisla: c1_hf_publikovano_en=1246 --> unikátním kazuistikám (Tabulka C.1) | kapitola 5, příloha C |
| 1 359 <!-- manifest kap5_korpus_cisla: n_k1_rez=1359 --> | reprodukovatelný řez K1 (deduplikované kazuistiky s lidskou anotací v matici) | kapitoly 4 a 5 |
| 1 350 <!-- manifest kap4_provenience_cisla: prov_rez_pokryto_lidskou=1350 --> | z řezu K1 s dochovaným přímým anotačním listem | kapitola 4 |
| 324 <!-- manifest kap7_k2_shoda_cisla: n_kazuistik=324 --> | vzorek druhé etapy (zaslepené dvojice) | kapitola 7 |
| přibližně třináct set <!-- necislo: historické číslo rukopisů, nerekonstruovatelné --> | stav pracovní databáze v dřívějších výstupech projektu | kapitola 4 |

*Poznámka.* Hodnoty pocházejí z tabulek výsledných hodnot analýz citovaných v uvedených kapitolách; zdůvodnění viz kapitola 4.

## C.3 Přehled měr shody

**Tabulka C.3.** Shrnutí spolehlivosti napříč etapami (podrobnosti a intervaly spolehlivosti v kapitolách 6, 7 a 8).

| Etapa | Veličina | Hodnota |
|---|---|---|
| K1 (lidé) | α typ chování | 0,50 <!-- manifest kap6_kodovani_cisla: k1_alpha_nom_chovani=0.4952 --> |
| K1 (lidé) | α typ řešení | 0,29 <!-- manifest kap6_kodovani_cisla: k1_alpha_nom_reseni=0.2868 --> |
| K1 (lidé) | α dopad | 0,72 <!-- manifest kap6_kodovani_cisla: k1_alpha_nom_dopad=0.7245 --> |
| K1 (LLM × člověk) | přesná shoda | 0,72 <!-- manifest kap6_kodovani_cisla: shoda_presna_llm=0.7237 --> |
| K1 (LLM × člověk) | rozšířená shoda | 0,93 <!-- manifest kap6_kodovani_cisla: shoda_rozsirena_llm=0.9339 --> |
| K1 (LLM × člověk) | Cohenovo κ | 0,64 <!-- manifest kap6_kodovani_cisla: kappa_llm_clovek=0.6445 --> |
| K1 (LLM × člověk), bez zjištěných překryvů | retrospektivní κ | 0,61 <!-- manifest kap6_kodovani_cisla: bez_prekryvu_kappa=0.6143 --> |
| K2 | α vhodnost | 0,53 <!-- manifest kap7_k2_shoda_cisla: alpha_ord_final_vhodnost=0.5274 --> |
| K2 | α reaktivní–proaktivní | 0,65 <!-- manifest kap7_k2_shoda_cisla: alpha_ord_final_reaktivni=0.6454 --> |
| K2 | α humanistická–behaviorální | 0,53 <!-- manifest kap7_k2_shoda_cisla: alpha_ord_final_humanisticke=0.5289 --> |
| K2 | α systémová–situační | 0,56 <!-- manifest kap7_k2_shoda_cisla: alpha_ord_final_systemove=0.5558 --> |
| K2 | Jaccard rámce (konvence článku) | 0,73 <!-- manifest kap7_k2_shoda_cisla: jaccard_pristupy_obe_prazdne_shoda=0.7254 --> |
| K3 | κ kvalita | 0,77 <!-- manifest kap8_kvalita_cisla: shoda_kvalita_kappa=0.7689 --> |
| K3 | AC1 kvalita | 0,98 <!-- manifest kap8_kvalita_cisla: shoda_kvalita_ac1=0.9773 --> |
| K3 | κ dopad | 0,69 <!-- manifest kap8_kvalita_cisla: shoda_dopad_kappa=0.6875 --> |
| K3 | vážená κ vhodnost | 0,52 <!-- manifest kap8_kvalita_cisla: shoda_vhodnost_wkappa=0.5188 --> |
| K1 × K3 | κ dopad mezi etapami | 0,59 <!-- manifest kap8_kvalita_cisla: k1k3_dopad_kappa=0.588 --> |
| K3 predikce | vyvážená přesnost modelu glm-5-3 vůči shodě anotátorek | 0,60 <!-- manifest kap8_predikce_cisla: predikce_glm_5_3_zero_shot_konsenzus_bal_acc=0.6039 --> |
| K3 predikce | vyvážená přesnost modelu kimi-k3 vůči shodě anotátorek | 0,60 <!-- manifest kap8_predikce_cisla: predikce_kimi_k3_zero_shot_konsenzus_bal_acc=0.6002 --> |
| K3 čtení výstupu | vyvážená shoda A2 vůči A12 (jiná úloha než predikce) | 0,80 <!-- manifest kap8_predikce_cisla: predikce_clovek_clovek_bal_acc=0.802 --> |
| K3 predikce | vyvážená přesnost hádání většinové třídy | 0,33 <!-- manifest kap8_predikce_cisla: predikce_majorita_bal_acc=0.3333 --> |

*Poznámka.* Hodnoty ze [zdrojových čísel Studie 2](https://github.com/JanNehyba/edustories-habilitation/blob/main/vystupy/tabulky/kap6_kodovani_cisla.csv) a [zdrojových čísel Studie 3](https://github.com/JanNehyba/edustories-habilitation/blob/main/vystupy/tabulky/kap7_k2_shoda_cisla.csv) v doprovodném repozitáři.

---
