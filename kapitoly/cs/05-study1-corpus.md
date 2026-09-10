# 5. Studie 1: Korpus a jeho obsah


První studie odpovídá na otázku, jak vypadá vybudovaný korpus kazuistik
a co obsahuje (VO1). Popisuje rozsah a růst korpusu (5.1), základní
charakteristiky kazuistik (5.2), typy chování, řešení a dopadů, které
kazuistiky zachycují (5.3), souběhy řešení s typy chování (5.4) a vztah
řešení k vnímanému výsledku (5.5). Všechny analýzy kapitoly jsou
deskriptivní; kapitola nedělá kauzální závěry.

## 5.1 Rozsah a růst korpusu

Korpus je průběžně rostoucí databáze (kapitola 3).
Analýzy se proto vždy vážou na pojmenovaný časový řez. Tabulka 5.1 shrnuje
velikost korpusu v doložených řezech od nejstaršího sběru po aktuální stav.

**Tabulka 5.1.** Růst korpusu v pojmenovaných časových řezech.

| Řez | Počet kazuistik |
|---|---|
| 2023 | 757 <!-- manifest kap5_korpus_cisla: rust_S12023=757 --> |
| duben 2024 | 1 507 <!-- manifest kap5_korpus_cisla: rust_S3042024=1507 --> |
| srpen 2024 | 1 695 <!-- manifest kap5_korpus_cisla: rust_S4082024=1695 --> |
| veřejná datová sada* | 1 492 <!-- manifest kap5_korpus_cisla: rust_S5HFrelease=1492 --> |
| květen 2026 | 3 202 <!-- manifest kap5_korpus_cisla: rust_S6052026=3202 --> |

*Poznámka.* Podklady v doprovodném repozitáři: [zdrojová čísla](https://github.com/JanNehyba/edustories-habilitation/blob/main/vystupy/tabulky/kap5_korpus_cisla.csv), [analýza v R](https://github.com/JanNehyba/edustories-habilitation/blob/main/analyzy/notebooks/10_korpus.qmd); definice řezů viz metodologie,
kap. 4. \*Veřejná datová sada není chronologickým bodem růstu: jde o kurátorovaný výběr
z řezu srpen 2024, zveřejněný jako samostatný datový produkt; uvedený počet jsou záznamy výběru, nikoli unikátní kazuistiky (příloha C.2).

![*Obrázek 5.1.* Růst korpusu v chronologických řezech (hodnoty viz Tabulka 5.1; veřejná datová sada jako kurátorovaný výběr není bodem růstu, proto ve figuře chybí). *Poznámka.* Podklady v doprovodném repozitáři: [zdrojová čísla](https://github.com/JanNehyba/edustories-habilitation/blob/main/vystupy/tabulky/kap5_korpus_cisla.csv), [kód obrázku](https://github.com/JanNehyba/edustories-habilitation/blob/main/analyzy/scripts/fig_05_korpus.R).](../../vystupy/obrazky/kap5_rust_korpusu.png)

Nejnovější řez z května 2026 obsahuje 3 202
<!-- manifest kap5_korpus_cisla: n_korpus_s6=3202 --> zveřejněných kazuistik.
Růst není prostou akumulací: srovnání se starším exportem téhož období ukazuje,
že 395
<!-- manifest kap5_korpus_cisla: n_odpublikovano_s6b_vs_s6=395 --> kazuistik,
přítomných v dřívějším exportu, se v aktuálním řezu již nevyskytuje, protože
byly mezitím staženy z publikace. Stažení patří k redakčnímu životu
databáze; konkrétní důvody jednotlivých stažení data
nezaznamenávají a kniha je proto nerekonstruuje. Pro výzkum z toho plyne
zásadní důsledek: „korpus“ bez data není
definovaný objekt a jakákoli replikace se musí vztáhnout k datovanému
řezu, nikoli k živé databázi. Publikační status je proto samostatnou
proměnnou, s níž analýzy pracují explicitně (kapitola 4). Veřejně dostupná
datová sada (kapitola 3) je kurátorovaný výběr z řezu srpen 2024 čítající 1 492
<!-- manifest kap5_korpus_cisla: rust_S5HFrelease=1492 --> záznamů, jež odpovídají 1 246
<!-- manifest priloha_c_cisla: c1_hf_publikovano_en=1246 --> unikátním kazuistikám (příloha C.2);
rozdíl mezi ním a plným řezem není jen početní, ale i kvalitativní,
protože do výběru vstupovaly kazuistiky s dokončeným lidským kódováním.

## 5.2 Základní charakteristiky kazuistik

Kazuistiky mají čtyřdílnou strukturu (kapitola 3) a jsou
to souvislé texty střední délky. V aktuálním řezu má popis situace medián
102 <!-- manifest kap5_korpus_cisla: description_slov_median=102 --> slov
(mezikvartilové rozpětí 76
<!-- manifest kap5_korpus_cisla: description_slov_q1=76 --> až 148),
<!-- manifest kap5_korpus_cisla: description_slov_q3=148 --> popis řešení
medián 102 <!-- manifest kap5_korpus_cisla: solution_slov_median=102 --> slov
(74 <!-- manifest kap5_korpus_cisla: solution_slov_q1=74 --> až 154),
<!-- manifest kap5_korpus_cisla: solution_slov_q3=153.75 --> anamnéza
medián 79 <!-- manifest kap5_korpus_cisla: anamnesis_slov_median=79 --> slov
(66 <!-- manifest kap5_korpus_cisla: anamnesis_slov_q1=66 --> až 109)
<!-- manifest kap5_korpus_cisla: anamnesis_slov_q3=109 --> a popis výsledku
medián 68 <!-- manifest kap5_korpus_cisla: outcome_slov_median=68 --> slov
(43 <!-- manifest kap5_korpus_cisla: outcome_slov_q1=43 --> až 102).
<!-- manifest kap5_korpus_cisla: outcome_slov_q3=102 --> Rozdělení délek
jsou pravostranně zešikmená s dlouhým chvostem podrobných textů; desetina
popisů situace přesahuje 221
<!-- manifest kap5_korpus_cisla: delka_p90_description=221 --> slov
(Obrázek 5.2). Statistiky délky konzervativně vylučují všech 52
<!-- manifest kap5_korpus_cisla: n_vyrazeno_delky_trunc=52 --> kazuistik
dotčených dřívějším zkrácením textu při automatické extrakci (kapitola 4).

![*Obrázek 5.2.* Rozdělení délek čtyř částí kazuistiky (počet slov; houslový graf s vyznačeným mezikvartilovým rozpětím a mediánem; pro čitelnost oříznuto na 99. percentil). *Poznámka.* Podklady v doprovodném repozitáři: [data obrázku](https://github.com/JanNehyba/edustories-habilitation/blob/main/vystupy/tabulky/kap5_delky_rozdeleni.csv), [analýza v R](https://github.com/JanNehyba/edustories-habilitation/blob/main/analyzy/notebooks/10_korpus.qmd), [kód obrázku](https://github.com/JanNehyba/edustories-habilitation/blob/main/analyzy/scripts/fig_05_hloubka.R).](../../vystupy/obrazky/kap5_delky.png)

Pisatelé věnují nejvíce slov
popisu situace a řešení, zatímco výsledek bývá odbyt několika větami:
je systematicky nejkratší částí kazuistiky. Pro pedagogické čtení to
znamená, že korpus je bohatší na to, co učitelé dělali, než na to, jak to
dopadlo; pro strojové zpracování to předznamenává, že právě predikce
úspěšnosti řešení (Studie 4) bude pracovat s nejtenčí textovou oporou.

Medián věku žáka, jehož se kazuistika týká, je 13
<!-- manifest kap5_korpus_cisla: vek_median=13 --> let (mezikvartilové
rozpětí 10 až 15 let; údaj o věku je uveden u 3 142
<!-- manifest kap5_korpus_cisla: vek_n=3142 --> kazuistik; patnáct
záznamů s nulovým věkem, kódem nevyplněného pole, bylo vyřazeno jako
chybějící). Rozložení věku
(Obrázek 5.3) pokrývá celou školní docházku s těžištěm na druhém stupni
základní školy; zastoupeny jsou ale i situace z mateřských a středních
škol. Korpus tedy zachycuje náročné chování především tam, kde je
literatura lokalizuje nejčastěji, v pubertálním období, aniž by na ně byl
omezen. Šíře věkového rozpětí má praktický význam pro obě linie knihy.
Pedagogicky umožňuje číst tytéž kategorie chování napříč stupni;
nepozornost prvňáka a nepozornost deváťáka jsou různé jevy pod jedním
štítkem, což je třeba mít na paměti při interpretaci frekvencí.
Metodologicky znamená, že jazykový model je v dalších studiích prověřován
na textech o dětech od předškolního věku po adolescenty, tedy v plné šíři
situací, s nimiž by se podpůrný nástroj v praxi potkal.

![*Obrázek 5.3.* Rozložení věku žáků v kazuistikách (počet kazuistik podle uvedeného věku). *Poznámka.* Podklady v doprovodném repozitáři: [data obrázku](https://github.com/JanNehyba/edustories-habilitation/blob/main/vystupy/tabulky/kap5_vek_rozdeleni.csv), [analýza v R](https://github.com/JanNehyba/edustories-habilitation/blob/main/analyzy/notebooks/10_korpus.qmd), [kód obrázku](https://github.com/JanNehyba/edustories-habilitation/blob/main/analyzy/scripts/fig_05_hloubka.R).](../../vystupy/obrazky/kap5_vek.png)

## 5.3 Co kazuistiky zachycují: chování, řešení, dopady

Deskriptivní obraz obsahu čerpáme z první anotační etapy na reprodukovatelném
řezu 1 359
<!-- manifest kap5_korpus_cisla: n_k1_rez=1359 --> ručně kódovaných kazuistik
(vymezení řezu i doklad lidské provenience kódů uvádí kapitola 4). Kódování je
víceznačné: jedné kazuistice mohla anotátorka přiřadit více kategorií.
Frekvence proto uvádíme jako počet kazuistik, v nichž se kategorie objevila;
celkový počet přiřazení je vyšší než počet kazuistik. U typů chování připadá
na jednu kazuistiku v průměru 1,84
<!-- manifest kap5_korpus_cisla: k1_chovani_pomer_prirazeni_na_pripad=1.841 -->
kategorie, u typů řešení 2,29,
<!-- manifest kap5_korpus_cisla: k1_reseni_pomer_prirazeni_na_pripad=2.2857 -->
zatímco dopad je téměř vždy jediný (poměr 1,01).
<!-- manifest kap5_korpus_cisla: k1_dopad_pomer_prirazeni_na_pripad=1.0146 -->
Náročné situace zřídka sestávají z jediného
projevu a učitelé na ně zřídka odpovídají jediným krokem; řešení jsou
v reálné praxi kombinacemi. Typická kazuistika tak nese dvojici projevů
(například verbální agresi spolu s narušováním výuky) a dvojici až trojici
kroků řešení (například rozhovor se žákem, informování rodičů a zapojení
poradenského pracoviště). Tento rys má metodologické důsledky, k nimž se
kniha opakovaně vrací: frekvence kategorií nelze sčítat do sta procent,
míry shody musí víceznačnost zohledňovat (Studie 2) a jednotkou
ko-výskytových analýz v oddílu 5.4 je pár kazuistika × kategorie.

Nejčastěji zachycenými projevy jsou verbální
agrese (v 330
<!-- manifest kap5_korpus_cisla: k1_chovani_pripadu:Verbální agrese=330 -->
kazuistikách), verbální narušování výuky (328),
<!-- manifest kap5_korpus_cisla: k1_chovani_pripadu:Verbální narušování výuky=328 -->
fyzická agrese (299),
<!-- manifest kap5_korpus_cisla: k1_chovani_pripadu:Fyzická agrese=299 -->
nepozornost a nevěnování se výuce (293)
<!-- manifest kap5_korpus_cisla: k1_chovani_pripadu:Nevěnování se výuce/Nepozornost při vý=293 -->
a porušování třídních či školních pravidel (255).
<!-- manifest kap5_korpus_cisla: k1_chovani_pripadu:Porušování třídních/školních pravidel=255 -->
Úplné rozdělení všech třinácti kategorií ukazuje Obrázek 5.4. Rozdělení
klesá pozvolna a bez dominance jednoho projevu; nezanedbatelné zastoupení
mají i závažné a organizačně náročné kategorie jako šikana, emoční výbuchy
nebo problémy s docházkou.
Korpus tedy nepokrývá jen běžnou nekázeň, ale celé spektrum situací, se
kterými se učitelé setkávají.

Kódovací strom první etapy nabízel kategorií čtrnáct. Čtrnáctou byla
„Diagnóza“, definovaná jako „žák/žákyně má diagnostikovanou některou z diagnóz
speciálních vzdělávacích potřeb“. Tato definice ovšem nepopisuje chování, ale
stav žáka, takže do dimenze problémového chování nepatří; z deskriptivy je
proto vyřazena a diagnóza vstupuje do analýzy jako kontextová proměnná
(oddíl 5.4). Nešlo o chybu sběru dat; kategorie byla shodně v nabídce
u všech pěti anotátorek. Šlo o vadu konstrukce kódovacího stromu, kterou
data potvrzují ze tří stran. Kategorie se v naprosté většině výskytů
objevovala jako přívěsek k jinému, skutečně behaviorálnímu kódu;
anotátorky ji používaly nesouměřitelně často; a shoda na ní byla nejnižší
v celé dimenzi, takže její vyřazení míru shody typů chování zvyšuje
(kapitola 6). Podrobný doklad uvádí příloha A.

Neplnění školních
povinností (201
<!-- manifest kap5_korpus_cisla: k1_chovani_pripadu:Neplnění školních povinností/nepřiprav=201 -->
kazuistik) ukazuje, že za náročné učitelé nepovažují jen jednání
namířené proti nim nebo proti spolužákům, ale i pasivní vzdor vůči školní
práci. Na samém konci rozdělení stojí sebedestruktivní chování; jeho
výskyt je řádově desítkový, ale právě u něj je cena chybného řešení
nejvyšší, což z něj činí důležitý testovací případ pro jakoukoli budoucí
podpůrnou technologii. Pro čtení všech frekvencí zároveň platí opatrnost
formulovaná v kapitole 4: kategorie odrážejí to, co pisatelé považovali za
hodné zaznamenání, nikoli epidemiologii náročného chování v českých
školách; nadreprezentace dramatických situací je u dobrovolně psaných
kazuistik očekávatelná.

![*Obrázek 5.4.* Typy náročného chování v první anotační etapě (počet kazuistik s kategorií; kódování je víceznačné). *Poznámka.* Podklady v doprovodném repozitáři: [data obrázku](https://github.com/JanNehyba/edustories-habilitation/blob/main/vystupy/tabulky/kap5_k1_kategorie.csv), [analýza v R](https://github.com/JanNehyba/edustories-habilitation/blob/main/analyzy/notebooks/10_korpus.qmd), [kód obrázku](https://github.com/JanNehyba/edustories-habilitation/blob/main/analyzy/scripts/fig_05_hloubka.R).](../../vystupy/obrazky/kap5_k1_chovani.png)

V repertoáru učitelů výrazně dominuje rozhovor, přítomný
v 922 <!-- manifest kap5_korpus_cisla: k1_reseni_pripadu:Rozhovor=922 -->
kazuistikách, následovaný spoluprací s odborníky (461),
<!-- manifest kap5_korpus_cisla: k1_reseni_pripadu:Spolupráce s odborníky=461 -->
podporou žáka (342),
<!-- manifest kap5_korpus_cisla: k1_reseni_pripadu:Podpora=342 -->
prací s důsledky (245)
<!-- manifest kap5_korpus_cisla: k1_reseni_pripadu:Důsledky=245 --> a
upozorněním (229).
<!-- manifest kap5_korpus_cisla: k1_reseni_pripadu:Upozornění=229 -->

![*Obrázek 5.5.* Nejčastější typy řešení v první etapě (počet kazuistik s kategorií; kódování je víceznačné, hodnoty viz text). *Poznámka.* Podklady v doprovodném repozitáři: [zdrojová čísla](https://github.com/JanNehyba/edustories-habilitation/blob/main/vystupy/tabulky/kap5_korpus_cisla.csv), [kód obrázku](https://github.com/JanNehyba/edustories-habilitation/blob/main/analyzy/scripts/fig_05_korpus.R).](../../vystupy/obrazky/kap5_k1_reseni.png)

Skladba repertoáru je pro tuto knihu podstatná: převažují snadno dostupné
postupy reagující na již vzniklý incident. Samostatnou proaktivní kategorii
finální kódovací schéma (V2) neobsahuje, proto proaktivitu v první etapě přímo
nekvantifikujeme; reaktivní charakter repertoáru potvrzuje bipolární dimenze
reaktivní–proaktivní ve Studii 3 (kapitola 7). Jednu výjimku je třeba uvést: vysoko v žebříčku stojí
spolupráce s odborníky, tedy krok, který překračuje hranici třídy
a zapojuje poradenský systém školy. Reaktivnost repertoáru tedy neznamená,
že by učitelé zůstávali na řešení sami; znamená, že i kroky za hranici
třídy jsou typicky spouštěny až incidentem, nikoli prací s podmínkami,
které mu předcházejí. Toto čtení, které ve Studii 3 poslouží jako
srovnávací pozadí pro řešení generovaná umělou inteligencí, komentuje
jako „repertoár nejmenšího odporu“ diskuse v kapitole 9.

Vnímaný výsledek řešení je nejčastěji dlouhodobý úspěch (598
<!-- manifest kap5_korpus_cisla: k1_dopad_pripadu:Dlouhodobý úspěch=598 -->
kazuistik) nebo naopak neúspěch (483),
<!-- manifest kap5_korpus_cisla: k1_dopad_pripadu:Neúspěch=483 --> méně často
částečný (158)
<!-- manifest kap5_korpus_cisla: k1_dopad_pripadu:Částečný úspěch=158 --> či
krátkodobý úspěch (84).
<!-- manifest kap5_korpus_cisla: k1_dopad_pripadu:Krátkodobý úspěch=84 -->
Bimodální tvar rozdělení (Obrázek 5.6) je přímým důsledkem sběru zrcadlovou
šablonou (kapitola 3): pisatelé odevzdávají úspěšně a neúspěšně řešenou
situaci v páru, a korpus se tak vyhýbá zkreslení přežití, jímž trpí typické
sbírky dobré praxe. Mezi krajními póly leží jen málo případů: částečný a krátkodobý úspěch dohromady tvoří menšinu dopadů.
I to je pravděpodobně důsledek šablony, která pisatele vede k volbě
jednoznačně vydařené a jednoznačně nevydařené situace; reálná praxe bude
na částečné úspěchy bohatší, než korpus ukazuje, a Studie 4 s touto
výhradou u posuzování dopadů dále pracuje.

![*Obrázek 5.6.* Dopady řešení v první anotační etapě (počet kazuistik s kategorií). *Poznámka.* Podklady v doprovodném repozitáři: [data obrázku](https://github.com/JanNehyba/edustories-habilitation/blob/main/vystupy/tabulky/kap5_k1_kategorie.csv), [analýza v R](https://github.com/JanNehyba/edustories-habilitation/blob/main/analyzy/notebooks/10_korpus.qmd), [kód obrázku](https://github.com/JanNehyba/edustories-habilitation/blob/main/analyzy/scripts/fig_05_hloubka.R).](../../vystupy/obrazky/kap5_k1_dopady.png)

## 5.4 Jak se řešení pojí s chováním

Frekvence kategorií říkají, co učitelé dělají; neříkají, kdy to dělají.
Obrázek 5.7 proto ukazuje podmíněné podíly: pro každý typ chování podíl
kazuistik s tímto chováním, v nichž se objevilo dané řešení. Jednotkou je
pár kazuistika × kategorie (kódování je víceznačné, kapitola 4), do analýzy
vstupují typy chování s dostatečným počtem kazuistik a podíly se čtou po
řádcích; jde o popis souběhů v kazuistikách, nikoli o doporučení či
kauzální vztah.

![*Obrázek 5.7.* Podmíněné podíly řešení podle typu chování, P(řešení | chování): podíl kazuistik s daným chováním, v nichž se objevilo dané řešení. Řádky = typy chování (seřazeny podle četnosti), sloupce = typy řešení; kódování je víceznačné, řádkové podíly se proto nesčítají do 1. *Poznámka.* Podklady v doprovodném repozitáři: [data obrázku](https://github.com/JanNehyba/edustories-habilitation/blob/main/vystupy/tabulky/kap5_kovyskyt.csv), [analýza v R](https://github.com/JanNehyba/edustories-habilitation/blob/main/analyzy/notebooks/10_korpus.qmd), [kód obrázku](https://github.com/JanNehyba/edustories-habilitation/blob/main/analyzy/scripts/fig_05_hloubka.R).](../../vystupy/obrazky/kap5_kovyskyt.png)

Obrázek ukazuje především univerzalitu rozhovoru: je nejčastějším řešením u všech typů chování a jeho podíl kulminuje
u šikany, kde se objevuje v 81 %
<!-- manifest kap5_korpus_cisla: kov_podil:Šikana|Rozhovor=0.8067 -->
kazuistik. Jde o četnost zmínek, nikoli o pořadí jednání učitele.
Zastoupení dalších postupů se mezi typy situací liší; analýza však
neurčuje, který krok byl první, druhý nebo třetí. U šikany je nadprůměrně častá práce
s kolektivem (37 %
<!-- manifest kap5_korpus_cisla: kov_podil:Šikana|Práce s kolektivem=0.3697 -->
kazuistik se šikanou oproti výrazně nižším podílům, nejvýše kolem jedné
pětiny, u ostatních typů chování), což odpovídá skupinové povaze jevu.
U porušování pravidel je nadprůměrně časté sahání k důsledkům (35 %)
<!-- manifest kap5_korpus_cisla: kov_podil:Porušování třídních/škol|Důsledky=0.349 -->
a tam, kde pisatel popisuje nezvládání výuky, se vedle rozhovoru rovným
dílem objevuje podpora (64 %).
<!-- manifest kap5_korpus_cisla: kov_podil:Nezvládání výuky|Podpora=0.6379 -->

Totéž ukazuje srovnání dvou zdánlivě podobných řádků. U verbálního
narušování výuky, typického drobného incidentu, se vedle rozhovoru (59 %)
<!-- manifest kap5_korpus_cisla: kov_podil:Verbální narušování výuk|Rozhovor=0.5884 -->
objevují se srovnatelnou četností podpora žáka (31 %)
<!-- manifest kap5_korpus_cisla: kov_podil:Verbální narušování výuk|Podpora=0.311 -->
a upozornění (31 %),
<!-- manifest kap5_korpus_cisla: kov_podil:Verbální narušování výuk|Upozornění=0.3079 -->
tedy vedle práce s příčinami i okamžitá, nízkonákladová korekce v běhu
hodiny. U neplnění školních povinností, které je v korpusu rovněž časté, ale má
pomalejší dynamiku, okamžitá korekce ustupuje: upozornění klesá na 14 %,
<!-- manifest kap5_korpus_cisla: kov_podil:Neplnění školních povinn|Upozornění=0.1443 -->
zatímco vedle rozhovoru (66 %)
<!-- manifest kap5_korpus_cisla: kov_podil:Neplnění školních povinn|Rozhovor=0.6567 -->
stojí spolupráce s odborníky (40 %)
<!-- manifest kap5_korpus_cisla: kov_podil:Neplnění školních povinn|Spolupráce s odborníky=0.398 -->
a podpora žáka (39 %).
<!-- manifest kap5_korpus_cisla: kov_podil:Neplnění školních povinn|Podpora=0.393 -->
Tam, kde incident nevyžaduje zásah v běhu hodiny, tedy z repertoáru mizí
především okamžitá korekce; práce s příčinami zůstává. Repertoár se tedy
podle situace liší, ale až za univerzální první volbou a v mezích převážně
reaktivních kategorií.

Samostatnou otázkou je, zda se repertoár mění tam, kde má žák zaznamenanou
diagnózu. Protože diagnóza není typem chování, čteme ji z kurátorovaného pole
korpusu, nikoli z anotace: vyplněné je u 530
<!-- manifest kap5_korpus_cisla: dia_pripadu=530 -->
kazuistik řezu, tedy u 39 %.
<!-- manifest kap5_korpus_cisla: dia_podil=0.39 -->
Zřetelný posun se týká jediné kategorie. Podpora žáka se v těchto
kazuistikách objevuje ve 37 %
<!-- manifest kap5_korpus_cisla: dia_podil_reseni:Podpora=0.3717 -->
oproti 25 % v celém řezu;
<!-- manifest kap5_korpus_cisla: dia_podil_reseni_ref:Podpora=0.2517 -->
opačným směrem se posouvají důsledky (13 %
<!-- manifest kap5_korpus_cisla: dia_podil_reseni:Důsledky=0.1302 -->
oproti 18 %)
<!-- manifest kap5_korpus_cisla: dia_podil_reseni_ref:Důsledky=0.1803 -->
a nerespektující komunikace (9 %
<!-- manifest kap5_korpus_cisla: dia_podil_reseni:Nerespektující komunikac=0.0943 -->
oproti 11 %).
<!-- manifest kap5_korpus_cisla: dia_podil_reseni_ref:Nerespektující komunikac=0.1133 -->
Spolupráce s odborníky přitom zůstává prakticky beze změny (36 %
<!-- manifest kap5_korpus_cisla: dia_podil_reseni:Spolupráce s odborníky=0.3623 -->
oproti 34 %):
<!-- manifest kap5_korpus_cisla: dia_podil_reseni_ref:Spolupráce s odborníky=0.3392 -->
zaznamenaná diagnóza sama nevede k častějšímu
zapojení poradenského pracoviště. Tam, kde je diagnóza známa, tedy učitelé
sahají spíše k podpoře než k sankci, ale mezioborový krok tím nepřibývá.
I zde jde o popis souběhů: kazuistiky s diagnózou se liší i skladbou situací,
takže rozdíl v podílech nelze číst jako účinek diagnózy samotné.

## 5.5 Dopad podle typu řešení

Historický kód neúspěchu zahrnuje nejen nezměněné chování, ale také
normativní odmítnutí nevhodného prostředku (příloha A.1). Z konečných
štítků tyto důvody nelze oddělit. Následující asociace proto popisují
vztah anotačních kategorií, nikoli nezávisle zjištěnou účinnost strategií.

Poslední deskriptivní pohled spojuje řešení s vnímaným výsledkem.
Obrázek 5.8 ukazuje pro každý typ řešení podíl kazuistik s tímto řešením,
které skončily dlouhodobým úspěchem. I zde platí, že jde o popis souběhů:
typ řešení si učitelé nevybírají náhodně, ale podle situace, takže rozdíly
mezi řešeními odrážejí i rozdílnou skladbu situací, v nichž se používají.
Z podílů proto nelze vyvozovat, že by některé řešení úspěch způsobovalo.

![*Obrázek 5.8.* Podíl kazuistik s dlouhodobým úspěchem podle typu řešení (deskriptivně; n = počet kazuistik s daným řešením a uvedeným dopadem). *Poznámka.* Podklady v doprovodném repozitáři: [data obrázku](https://github.com/JanNehyba/edustories-habilitation/blob/main/vystupy/tabulky/kap5_dopad_podle_reseni.csv), [analýza v R](https://github.com/JanNehyba/edustories-habilitation/blob/main/analyzy/notebooks/10_korpus.qmd), [kód obrázku](https://github.com/JanNehyba/edustories-habilitation/blob/main/analyzy/scripts/fig_05_hloubka.R).](../../vystupy/obrazky/kap5_dopad_reseni.png)

Rozdíly jsou přesto zřetelné. Nejvyšší podíl dlouhodobého úspěchu vykazují
kazuistiky s prací s kolektivem (67 %
<!-- manifest kap5_korpus_cisla: dopadDU:Práce s kolektivem=0.6685 -->
z 178 <!-- manifest kap5_korpus_cisla: dopadN:Práce s kolektivem=178 -->
kazuistik), s dohodou (63 %)
<!-- manifest kap5_korpus_cisla: dopadDU:Dohoda=0.6279 --> a s podporou
žáka (50 %); <!-- manifest kap5_korpus_cisla: dopadDU:Podpora=0.503 -->
rozhovor, univerzální první volba, leží uprostřed (49 %).
<!-- manifest kap5_korpus_cisla: dopadDU:Rozhovor=0.4933 --> Na opačném
konci stojí kategorie mocenského vynucení: kázeňské tresty (39 %),
<!-- manifest kap5_korpus_cisla: dopadDU:(Kázeňské) Tresty=0.3922 -->
přemístění žáka (37 %),
<!-- manifest kap5_korpus_cisla: dopadDU:Přemístění žáka=0.3682 -->
fyzické zakročení (27 %)
<!-- manifest kap5_korpus_cisla: dopadDU:Fyzické zakročení=0.2683 -->
a nerespektující komunikace, u níž pisatelé referují dlouhodobý úspěch
nejméně často (22 %).
<!-- manifest kap5_korpus_cisla: dopadDU:Nerespektující komunikace=0.2153 -->
Deskriptivně tedy platí, že vztahová a systémová řešení se v korpusu
vyskytují spolu s příznivějšími vnímanými výsledky než řešení represivní.
To je v souladu s poznatky shrnutými v kapitole 2; kauzální čtení by však
vyžadovalo jiné uspořádání studie a kniha se ho zdržuje.

Dva mechanismy, které mohou vzorec spoluutvářet, je třeba uvést, protože
ukazují, co by kauzální čtení muselo vyloučit. Prvním je selekce
situací: k práci s kolektivem nebo k dohodě učitel sahá typicky tam, kde
situace ještě dohodu připouští, zatímco fyzické zakročení je z povahy
věci vyhrazeno situacím eskalovaným, jejichž vyhlídky jsou horší bez
ohledu na zvolený zásah. Druhým je pohled pisatele: dopad hodnotí
tentýž člověk, který řešení volil a popsal, takže vnímaná úspěšnost
může být přikrášlena u řešení, s nimiž se pisatel identifikuje.
Zrcadlová šablona (kapitola 3) druhý mechanismus částečně krotí, protože
neúspěchy do korpusu aktivně přivádí; selekci situací však žádný sběr
tohoto typu neodstraní. Právě proto kniha vzorec předkládá jako popis
souběhů a jeho silnější čtení ponechává studiím s uspořádáním, které by umělo
situace srovnávat.

## 5.6 Shrnutí

Studie 1 popsala korpus jako rostoucí databázi, jejíž aktuální zveřejněný řez
z května 2026 čítá 3 202
<!-- manifest kap5_korpus_cisla: n_korpus_s6=3202 --> kazuistik, s doloženým
publikačním pohybem v čase.
Kazuistiky jsou souvislé texty střední délky se čtyřdílnou strukturou, v níž
je popis výsledku systematicky nejkratší; těžištěm korpusu je druhý stupeň
základní školy. Obsahově dominují verbálně a fyzicky agresivní projevy
a projevy narušující výuku; v řešeních převažuje rozhovor a další dostupná,
převážně reaktivní řešení. Podmíněné podíly ukázaly, že repertoár se
diferencuje podle situace až za univerzální první volbou rozhovoru,
a deskriptivní spojení řešení s dopady ukázalo, že vztahová a systémová
řešení se v kazuistikách pojí s příznivějšími vnímanými výsledky než řešení
represivní. Tento základ otevírá otázky dalších studií: nakolik spolehlivě
lze takový obsah kódovat jazykovým modelem (Studie 2) a jak si učitelská
řešení stojí ve srovnání s generovanými (Studie 3).

---
