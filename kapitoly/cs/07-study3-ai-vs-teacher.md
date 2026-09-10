# 7. Studie 3: Řešení generovaná umělou inteligencí versus řešení učitelů


Třetí studie odpovídá na otázku, jak se řešení náročných situací generovaná
velkým jazykovým modelem liší od autentických řešení, která zvolili učitelé
(VO3). Využívá druhou anotační etapu: zaslepené hodnocení dvojic řešení
šesti vyškolenými anotátorkami na čtyřech pedagogických dimenzích a v úloze
rozpoznávání rámců opřených o důkazy. Kapitola popisuje materiál
a uspořádání studie (7.2), dokládá spolehlivost hodnocení (7.3) a předkládá
výsledky smíšených modelů (7.4).

## 7.1 Východiska

Kapitola 2 vymezila generování řešení jako jednu ze tří rolí, v nichž kniha
jazykový model prověřuje; otevřenou otázkou zůstává,
zda generované návrhy obstojí před měřítky pedagogické kvality: vhodností pro danou
situaci, poměrem prevence a reakce, hodnotovou orientací a systémovostí
zásahu. Přímé srovnání na autentických případech přitom naráží na zjevný
metodologický problém: kdyby hodnotitelé věděli, které řešení pochází od
stroje, jejich očekávání by hodnocení kontaminovala. Druhá etapa proto
byla navržena jako zaslepená: anotátorky hodnotily obě řešení téže kazuistiky,
aniž věděly, že jedno z nich je generované.

## 7.2 Metoda

### Materiál

Z korpusu (kapitola 5) bylo vybráno 324
<!-- manifest kap7_k2_shoda_cisla: n_kazuistik=324 --> kazuistik z kategorií
agresivního chování (fyzická a verbální agrese), tedy ze závažného a silně
zastoupeného segmentu korpusu, s úplným popisem
situace i učitelského řešení. Ke každé kazuistice bylo modelem gpt-4o
vygenerováno alternativní řešení se stejným zadáním, jaké implicitně řešil
učitel; prompt vynucoval paritu délky, gramatického rodu a minulého času,
aby povrchové rysy textu neprozrazovaly jeho původ. Šlo o jediné srovnávací
řešení generované jednotným promptem; se šesticí rámcovaných řešení, která
nabízí platforma (kapitola 3), se nezaměňuje. Postup výběru a generování
shrnuje kapitola 4, prompt je uveden v příloze B.

### Hodnocení

U každé dvojice řešení bylo plánováno hodnocení všech 6
<!-- manifest kap7_k2_shoda_cisla: n_anotatorek=6 --> anotátorek, a to
nezávisle a v zaslepeném, znáhodněném pořadí (krycí instrukce bez zmínky o AI).
Každé řešení bylo posuzováno na čtyřech ordinálních pětibodových dimenzích:
celková vhodnost pro danou situaci, orientace reaktivní versus proaktivní,
orientace humanistická versus behaviorální a zaměření systémové versus
situační. V analyzovaném souboru jsou všechny čtyři uloženy
na škále od −2 do +2 (vhodnost byla v kódovacím formuláři zadávána jako
pětibodová a pro analýzu lineárně překódována). Vedle škál anotátorky označovaly, zda řešení rozpoznatelně
odráží některý z rámců opřených o důkazy (sociálně-emoční učení, pozitivní
behaviorální podpora, nenásilná komunikace, restorativní praxe). Zácvik
proběhl ve dvou kalibračních kolech s rozborem neshod; jeho průběh dokládá
registr anotačních etap v příloze C. Soubor hodnocení obsahuje
15 476
<!-- manifest kap7_k2_shoda_cisla: n_odpovedi_dimenze=15476 --> hodnoticích
polí (kombinace kazuistiky, řešení, dimenze a anotátorky), z nichž 1 600
<!-- manifest kap7_k2_shoda_cisla: n_missing_dimenze=1600 --> (přibližně
desetina) zůstalo nevyplněno; chybění nebylo rozloženo rovnoměrně mezi
anotátorky a analýzy pracují se všemi vyplněnými odpověďmi. V dochovaných
řádcích činí podíl prázdných hodnocení 11 %
<!-- manifest kap7_k2_shoda_cisla: missing_podil_AI=0.1106 --> u řešení
generovaných, 10 %
<!-- manifest kap7_k2_shoda_cisla: missing_podil_ucitel=0.0961 -->
u učitelských. Úplný plán obsahuje 15 552
<!-- manifest kap7_k2_shoda_cisla: n_ocekavanych_bunek=15552 --> buněk,
ale 76 <!-- manifest kap7_k2_shoda_cisla: n_chybejicich_radku=76 -->
řádků v exportu zcela chybí, všechny u učitelského zdroje. Celkem tedy
chybí 1 676 <!-- manifest kap7_k2_shoda_cisla: n_chybejicich_bunek_celkem=1676 -->
hodnocení. Zaslepení samo nezaručuje náhodné chybění: vynechání mohlo
souviset s vlastnostmi textu nebo s nejistotou anotátorky. Rozpis podle
zdroje, dimenze a anotátorky obsahuje veřejný report.

Ve veřejné tabulce K2 mají anotátorky lokální označení A1 až A6.
Tato řada není totožná s projektovými pseudonymy v knize a neslouží
k propojování osob napříč etapami; veřejný převodník osob nezveřejňujeme.

### Analýza

Primárním modelem je lineární smíšený model (LMM) s pevným
efektem zdroje řešení (referenční kategorie AI) a náhodnými průsečíky pro
kazuistiku a anotátorku; tím model zohledňuje opakovaná hodnocení týchž
případů i systematické rozdíly v přísnosti hodnotitelek. Jeho koeficient má
přímočarou interpretaci v bodech škály, zachází však s pětibodovou škálou,
jako by vzdálenosti mezi sousedními stupni byly stejné.

Předem stanovenou citlivostní analýzou je proto kumulativní logitový
smíšený model (CLMM), který tento předpoklad nepotřebuje. Hodnocení v něm
vystupuje jako uspořádaná kategoriální proměnná a model popisuje kumulativní
pravděpodobnosti, tedy šanci, že hodnocení nepřekročí daný stupeň škály,
přes čtyři prahy mezi pěti stupni. Logit každé kumulativní pravděpodobnosti
je lineární funkcí týchž členů jako v primárním modelu: pevného efektu
zdroje řešení a náhodných průsečíků pro kazuistiku a anotátorku. Model
předpokládá proporcionalitu šancí: jediný efekt zdroje posouvá všechny
prahy stejně. Exponenciála koeficientu je pak poměr šancí (odds ratio, OR).
OR menší než jedna znamená, že učitelské řešení má oproti
řešení generovanému nižší šanci dosáhnout vyššího stupně škály, a to u kterékoli
hranice mezi stupni, při hodnocení téže kazuistiky touž anotátorkou;
OR větší než jedna znamená šanci vyšší. Model odhadujeme metodou maximální
věrohodnosti (balík ordinal, funkce clmm) a k odhadům uvádíme Waldovy
95% intervaly spolehlivosti. Závěry se opírají o LMM; CLMM slouží k ověření,
že směr a věrohodnost efektů nestojí na předpokladu stejných vzdáleností
mezi stupni škály. Protože uspořádání je párové uvnitř kazuistiky, doplňujeme
ještě druhou citlivostní analýzu: LMM s náhodným sklonem zdroje po
kazuistikách, který připouští, že se rozdíl mezi zdroji případ od případu
liší (oddíl 7.4). Spolehlivost hodnocení vyjadřujeme
Krippendorffovým α (ordinálním) s 95% intervaly spolehlivosti získanými
bootstrapem přes kazuistiky a u rámců průměrným párovým Jaccardovým indexem.

## 7.3 Spolehlivost hodnocení

Shoda šesti anotátorek na jednotkách kazuistika × řešení dosahovala hodnot
α = 0,53 <!-- manifest kap7_k2_shoda_cisla: alpha_ord_final_vhodnost=0.5274 -->
(95% CI 0,49 <!-- manifest kap7_k2_shoda_cisla: alpha_ci_lo_vhodnost=0.4854 -->
až 0,57) <!-- manifest kap7_k2_shoda_cisla: alpha_ci_hi_vhodnost=0.5664 -->
pro vhodnost, α = 0,65
<!-- manifest kap7_k2_shoda_cisla: alpha_ord_final_reaktivni=0.6454 -->
(0,61 <!-- manifest kap7_k2_shoda_cisla: alpha_ci_lo_reaktivni=0.6098 -->
až 0,68) <!-- manifest kap7_k2_shoda_cisla: alpha_ci_hi_reaktivni=0.6767 -->
pro dimenzi reaktivní–proaktivní, α = 0,53
<!-- manifest kap7_k2_shoda_cisla: alpha_ord_final_humanisticke=0.5289 -->
(0,49 <!-- manifest kap7_k2_shoda_cisla: alpha_ci_lo_humanisticke=0.4908 -->
až 0,57) <!-- manifest kap7_k2_shoda_cisla: alpha_ci_hi_humanisticke=0.5652 -->
pro dimenzi humanistickou–behaviorální a α = 0,56
<!-- manifest kap7_k2_shoda_cisla: alpha_ord_final_systemove=0.5558 -->
(0,52 <!-- manifest kap7_k2_shoda_cisla: alpha_ci_lo_systemove=0.5196 -->
až 0,59) <!-- manifest kap7_k2_shoda_cisla: alpha_ci_hi_systemove=0.5916 -->
pro dimenzi systémovou–situační. Obrázek 7.1 hodnoty shrnuje. Jde o střední
míru položkové shody, očekávatelnou u úsudkových škál tohoto typu; nejvyšší
shody dosahovala dimenze reaktivní–proaktivní, jejíž póly jsou v textu
řešení nejsnáze rozpoznatelné (zásah po incidentu versus práce
s podmínkami). Podstatné je, že smíšené modely
v oddíle 7.4 s meziposuzovatelskou variabilitou přímo počítají, takže závěry
o rozdílu mezi zdroji řešení na položkové shodě nestojí. Vývoj shody mezi
kalibračními koly a finálním anotováním, včetně jeho možných příčin,
komentujeme v kapitole 9.

![*Obrázek 7.1.* Reliabilita hodnocení: Krippendorffovo ordinální α podle dimenzí (95% intervaly spolehlivosti z bootstrapu přes kazuistiky; svislice vyznačují konvenční prahy 0,667 a 0,80). *Poznámka.* Podklady v doprovodném repozitáři: [zdrojová čísla](https://github.com/JanNehyba/edustories-habilitation/blob/main/vystupy/tabulky/kap7_k2_shoda_cisla.csv), [analýza v R](https://github.com/JanNehyba/edustories-habilitation/blob/main/analyzy/notebooks/30_ai_vs_ucitel.qmd), [kód obrázku](https://github.com/JanNehyba/edustories-habilitation/blob/main/analyzy/scripts/fig_07_hloubka.R).](../../vystupy/obrazky/kap7_alpha.png)

Hodnocené konstrukty jsou úsudkové: co je pro danou situaci „vhodné“, závisí na
pedagogickém přesvědčení hodnotitelky a čtyři osy vyžadují vážení
protichůdných signálů v jednom textu. Škály tohoto typu zpravidla
nedosahují reliability jednoduchých klasifikací ani po pečlivém zácviku;
podstatné je, že zbylá neshoda je v analýze modelována, ne zamlčena.
Zároveň hodnoty připomínají, proč kniha důsledně mluví o „hodnocené
vhodnosti“, a ne o vhodnosti samé: měříme úsudek vyškolených posuzovatelek,
konsenzuální konstrukt, jehož nejistotu známe a přenášíme ji do intervalů
spolehlivosti výsledků.

U rozpoznávání rámců dosahoval průměrný párový Jaccardův index hodnoty
0,73 <!-- manifest kap7_k2_shoda_cisla: jaccard_pristupy_obe_prazdne_shoda=0.7254 -->
v konvenci, která shodu dvou prázdných množin počítá jako souhlas (tj. obě
anotátorky se shodly, že řešení žádný rámec nenese). Protože většina řešení
žádný rámec nenesla, uvádíme pro úplnost i přísnou konvenci bez prázdných
průniků, kde index klesá na 0,12;
<!-- manifest kap7_k2_shoda_cisla: jaccard_pristupy_bez_prazdnych=0.123 -->
rozdíl obou konvencí je dalším projevem paradoxu shody při šikmých
rozděleních, který podrobně rozebírá kapitola 4.

## 7.4 Výsledky

### Deskriptivní obraz

Tabulka 7.1 shrnuje průměrná hodnocení podle zdroje
řešení. Slovník kvality přitom náleží jen dimenzím, které ji nesou
(oddíl 2.3): jednoznačně příznivěji pro generovaná řešení vyznívá vhodnost
a orientace reaktivní–proaktivní. Obě zbývající osy jsou popisné. Na ose
humanistická–behaviorální se generovaná řešení klonila k humanistickému
pólu a učitelská k behaviorálnímu; na ose systémová–situační se oba zdroje
klonily k situačnímu pólu, generovaná řešení o něco výrazněji, byla tedy
nepatrně vzdálenější systémovému pólu než řešení učitelů.

**Tabulka 7.1.** Průměrná hodnocení řešení podle zdroje (škály −2 až +2).

| Dimenze | AI | Učitel |
|---|---|---|
| Vhodnost | 1,56 <!-- manifest kap7_k2_shoda_cisla: mean_AI_vhodnost=1.561 --> | 0,71 <!-- manifest kap7_k2_shoda_cisla: mean_teacher_vhodnost=0.7059 --> |
| Reaktivní–proaktivní | 0,69 <!-- manifest kap7_k2_shoda_cisla: mean_AI_reaktivni=0.6931 --> | −0,32 <!-- manifest kap7_k2_shoda_cisla: mean_teacher_reaktivni=-0.3205 --> |
| Humanistická–behaviorální | −0,44 <!-- manifest kap7_k2_shoda_cisla: mean_AI_humanisticke=-0.4418 --> | 0,34 <!-- manifest kap7_k2_shoda_cisla: mean_teacher_humanisticke=0.3402 --> |
| Systémová–situační | 0,35 <!-- manifest kap7_k2_shoda_cisla: mean_AI_systemove=0.348 --> | 0,17 <!-- manifest kap7_k2_shoda_cisla: mean_teacher_systemove=0.1689 --> |

*Poznámka.* Podklady v doprovodném repozitáři: [zdrojová čísla](https://github.com/JanNehyba/edustories-habilitation/blob/main/vystupy/tabulky/kap7_k2_shoda_cisla.csv), [analýza v R](https://github.com/JanNehyba/edustories-habilitation/blob/main/analyzy/notebooks/30_ai_vs_ucitel.qmd).

Vedle rozdílů jsou podstatné i absolutní polohy průměrů. Průměrné
hodnocení vhodnosti generovaných řešení 1,56
<!-- manifest kap7_k2_shoda_cisla: mean_AI_vhodnost=1.561 --> leží blízko
stropu pětibodové škály, což znamená, že anotátorky generovaná řešení
nejen preferovaly, ale hodnotily je téměř jednohlasně jako vhodná; zároveň
to ohlašuje stropový efekt, kvůli němuž může být skutečný rozdíl na horním
konci škály podhodnocen. Učitelská řešení přitom s průměrem 0,71
<!-- manifest kap7_k2_shoda_cisla: mean_teacher_vhodnost=0.7059 --> nejsou
hodnocena záporně: leží nad středem škály, na straně spíše vhodných řešení.
Učitelská řešení tedy nebyla hodnocena jako špatná; generovaná vedle nich
působila ještě vhodněji.

![*Obrázek 7.2.* Průměrná hodnocení řešení podle zdroje (hodnoty viz Tabulka 7.1; oranžově řešení generovaná umělou inteligencí, modře řešení učitelů; u bipolárních dimenzí odpovídá záporný pól reaktivnímu, humanistickému a systémovému řešení). *Poznámka.* Podklady v doprovodném repozitáři: [zdrojová čísla](https://github.com/JanNehyba/edustories-habilitation/blob/main/vystupy/tabulky/kap7_k2_shoda_cisla.csv), [kód obrázku](https://github.com/JanNehyba/edustories-habilitation/blob/main/analyzy/scripts/fig_07_k2.R).](../../vystupy/obrazky/kap7_prumery.png)

### Primární modely

Lineární smíšené modely potvrzují, že rozdíly nejsou
důsledkem opakovaných měření ani rozdílné přísnosti anotátorek. Učitelská
řešení byla oproti generovaným hodnocena jako méně vhodná, s rozdílem −0,85
<!-- manifest kap7_k2_shoda_cisla: lmm_b1_ucitel_vhodnost=-0.8547 --> bodu
škály (95% CI −0,90
<!-- manifest kap7_k2_shoda_cisla: lmm_b1_ci_lo_vhodnost=-0.8979 --> až
−0,81) <!-- manifest kap7_k2_shoda_cisla: lmm_b1_ci_hi_vhodnost=-0.8114 -->
a jako výrazně reaktivnější, s rozdílem −1,01
<!-- manifest kap7_k2_shoda_cisla: lmm_b1_ucitel_reaktivni=-1.01 --> bodu
(−1,07 <!-- manifest kap7_k2_shoda_cisla: lmm_b1_ci_lo_reaktivni=-1.0664 -->
až −0,95). <!-- manifest kap7_k2_shoda_cisla: lmm_b1_ci_hi_reaktivni=-0.9536 -->
Na hodnotové dimenzi se učitelská řešení posouvala k behaviorálnímu pólu
o 0,77 <!-- manifest kap7_k2_shoda_cisla: lmm_b1_ucitel_humanisticke=0.7719 -->
bodu (0,71
<!-- manifest kap7_k2_shoda_cisla: lmm_b1_ci_lo_humanisticke=0.7142 --> až
0,83), <!-- manifest kap7_k2_shoda_cisla: lmm_b1_ci_hi_humanisticke=0.8296 -->
zatímco na dimenzi systémové–situační byl rozdíl nejmenší: −0,17
<!-- manifest kap7_k2_shoda_cisla: lmm_b1_ucitel_systemove=-0.1716 --> bodu
(−0,23 <!-- manifest kap7_k2_shoda_cisla: lmm_b1_ci_lo_systemove=-0.2333 -->
až −0,11), <!-- manifest kap7_k2_shoda_cisla: lmm_b1_ci_hi_systemove=-0.1098 -->
oba zdroje se klonily k situačním zásahům.

![*Obrázek 7.3.* Efekty zdroje řešení ze smíšených modelů: rozdíl učitel − AI v bodech škály s 95% intervalem spolehlivosti (hodnoty viz text; nula = žádný rozdíl mezi zdroji). *Poznámka.* Podklady v doprovodném repozitáři: [zdrojová čísla](https://github.com/JanNehyba/edustories-habilitation/blob/main/vystupy/tabulky/kap7_k2_shoda_cisla.csv), [kód obrázku](https://github.com/JanNehyba/edustories-habilitation/blob/main/analyzy/scripts/fig_07_k2.R).](../../vystupy/obrazky/kap7_lmm_efekty.png)

### Rozpoznávání rámců

Anotátorky přiřadily celkem 874
<!-- manifest kap7_k2_shoda_cisla: ramce_n_labelu_celkem=874 --> rámcových
štítků; z nich 72 %
<!-- manifest kap7_k2_shoda_cisla: ramce_podil_labelu_AI=0.7174 --> připadlo
na řešení generovaná umělou inteligencí. Logistický smíšený model s náhodnými
průsečíky pro kazuistiku a anotátorku ukazuje, že učitelské řešení mělo
výrazně nižší šanci být rozpoznáno jako nesoucí některý z pojmenovaných
rámců: poměr šancí 0,31
<!-- manifest kap7_k2_shoda_cisla: glmm_or_ucitel_ramce=0.3127 --> (95% CI
0,26 <!-- manifest kap7_k2_shoda_cisla: glmm_or_ci_lo_ramce=0.2594 --> až
0,38); <!-- manifest kap7_k2_shoda_cisla: glmm_or_ci_hi_ramce=0.3771 -->
šance učitelského řešení na rozpoznání rámce byla tedy zhruba třetinová.
Vztaženo k prostým četnostem to odpovídá přibližně dvaapůlnásobku:
generovaná řešení nesla necelé tři čtvrtiny všech rámcových štítků,
učitelská zbytek.

Podstatné je, že srovnávací řešení nebyla generována
s instrukcí držet se některého z přístupů: vznikala jednotným promptem bez
rámcového zadání (oddíl 7.2). Rámcové rysy, které v nich anotátorky
rozpoznávaly, tedy nejsou splněním explicitního zadání, ale vlastností
textu, který model o řešení náročné situace typicky produkuje. Zjištění
má dvě výhrady. Rozpoznání rámce je úsudek s nízkou
shodou mezi anotátorkami (oddíl 7.3), takže vypovídá spíše o celkové
tendenci než o spolehlivé klasifikaci jednotlivých řešení; a rozpoznaný
rámec není totéž co věrné uplatnění přístupu, k němuž by texty musely
posoudit expertky na příslušné rámce.

### Citlivostní analýza

Kumulativní logitové smíšené modely (specifikace
v oddíle 7.2) potvrzují směr všech čtyř efektů; Tabulka 7.2 uvádí poměry
šancí s intervaly spolehlivosti a Obrázek 7.4 je vynáší na logaritmické ose.

**Tabulka 7.2.** Citlivostní CLMM: poměr šancí pro zdroj = učitel
(referenční kategorie AI; Waldovy 95% intervaly spolehlivosti).

| Dimenze | OR | 95% CI |
|---|---|---|
| Vhodnost | 0,06 <!-- manifest kap7_k2_shoda_cisla: clmm_or_ucitel_vhodnost=0.0614 --> | 0,05 <!-- manifest kap7_k2_shoda_cisla: clmm_or_ci_lo_vhodnost=0.0516 --> až 0,07 <!-- manifest kap7_k2_shoda_cisla: clmm_or_ci_hi_vhodnost=0.0732 --> |
| Reaktivní–proaktivní | 0,11 <!-- manifest kap7_k2_shoda_cisla: clmm_or_ucitel_reaktivni=0.1052 --> | 0,09 <!-- manifest kap7_k2_shoda_cisla: clmm_or_ci_lo_reaktivni=0.0905 --> až 0,12 <!-- manifest kap7_k2_shoda_cisla: clmm_or_ci_hi_reaktivni=0.1223 --> |
| Humanistická–behaviorální | 5,38 <!-- manifest kap7_k2_shoda_cisla: clmm_or_ucitel_humanisticke=5.3833 --> | 4,68 <!-- manifest kap7_k2_shoda_cisla: clmm_or_ci_lo_humanisticke=4.6839 --> až 6,19 <!-- manifest kap7_k2_shoda_cisla: clmm_or_ci_hi_humanisticke=6.1872 --> |
| Systémová–situační | 0,77 <!-- manifest kap7_k2_shoda_cisla: clmm_or_ucitel_systemove=0.7745 --> | 0,68 <!-- manifest kap7_k2_shoda_cisla: clmm_or_ci_lo_systemove=0.682 --> až 0,88 <!-- manifest kap7_k2_shoda_cisla: clmm_or_ci_hi_systemove=0.8796 --> |

*Poznámka.* Podklady v doprovodném repozitáři: [zdrojová čísla](https://github.com/JanNehyba/edustories-habilitation/blob/main/vystupy/tabulky/kap7_k2_shoda_cisla.csv), [analýza v R](https://github.com/JanNehyba/edustories-habilitation/blob/main/analyzy/notebooks/30_ai_vs_ucitel.qmd).

![*Obrázek 7.4.* Citlivostní CLMM: poměry šancí pro zdroj = učitel na logaritmické ose (95% Waldovy intervaly spolehlivosti; svislice OR = 1 značí žádný rozdíl mezi zdroji; hodnoty viz Tabulka 7.2). *Poznámka.* Podklady v doprovodném repozitáři: [zdrojová čísla](https://github.com/JanNehyba/edustories-habilitation/blob/main/vystupy/tabulky/kap7_k2_shoda_cisla.csv), [kód obrázku](https://github.com/JanNehyba/edustories-habilitation/blob/main/analyzy/scripts/fig_07_hloubka.R).](../../vystupy/obrazky/kap7_clmm.png)

Čtení tabulky ilustrujme na vhodnosti: OR 0,06
<!-- manifest kap7_k2_shoda_cisla: clmm_or_ucitel_vhodnost=0.0614 -->
znamená, že šance učitelského řešení na překročení kterékoli hranice mezi
stupni škály (například na hodnocení „spíše vhodné a lepší“ místo
„neutrální a horší“) je při hodnocení téže kazuistiky touž anotátorkou
zhruba šestnáctkrát nižší než u řešení generovaného. Interval
spolehlivosti je úzký a hluboko pod jedničkou, efekt tedy nestojí na
předpokladu stejných vzdáleností mezi stupni škály. Obdobně silný je
efekt u orientace reaktivní–proaktivní; u hodnotové dimenze míří opačným
směrem (učitelská řešení mají vyšší šanci na behaviorálnější hodnocení)
a u dimenze systémové–situační je nejslabší, byť i jeho interval leží
celý pod jedničkou. Shoda směru mezi primárním a citlivostním modelem na
všech čtyřech dimenzích splňuje předem stanovené kritérium robustnosti.

Druhá citlivostní analýza uvolňuje předpoklad stejného rozdílu mezi zdroji
napříč kazuistikami: LMM s náhodným sklonem zdroje po kazuistikách
konvergoval u všech čtyř dimenzí bez singularit a odhady efektů se od
primárního modelu prakticky neliší (u vhodnosti −0,86
<!-- manifest kap7_k2_shoda_cisla: lmm_slope_b1_ucitel_vhodnost=-0.8566 -->
bodu s 95% CI −0,93
<!-- manifest kap7_k2_shoda_cisla: lmm_slope_ci_lo_vhodnost=-0.932 --> až
−0,78; <!-- manifest kap7_k2_shoda_cisla: lmm_slope_ci_hi_vhodnost=-0.7813 -->
u dimenze systémové–situační, kde je efekt nejslabší, −0,16
<!-- manifest kap7_k2_shoda_cisla: lmm_slope_b1_ucitel_systemove=-0.164 -->
bodu s intervalem −0,27
<!-- manifest kap7_k2_shoda_cisla: lmm_slope_ci_lo_systemove=-0.2748 --> až
−0,05, <!-- manifest kap7_k2_shoda_cisla: lmm_slope_ci_hi_systemove=-0.0531 -->
stále celým pod nulou). Závěry tedy nestojí ani na předpokladu konstantního
rozdílu mezi zdroji.

Dodatečná analýza pouze úplných dvojic uvnitř kombinace kazuistiky,
anotátorky a dimenze zachovává směr všech čtyř rozdílů. U vhodnosti
vychází rozdíl učitel minus AI −0,86
<!-- manifest kap7_k2_shoda_cisla: paired_b1_vhodnost=-0.8588 -->
bodu, s intervalem od −0,90
<!-- manifest kap7_k2_shoda_cisla: paired_ci_lo_vhodnost=-0.9024 -->
do −0,82 <!-- manifest kap7_k2_shoda_cisla: paired_ci_hi_vhodnost=-0.8152 -->.
Výsledek omezuje obavu, že hlavní směr závisí pouze na neúplných dvojicích,
ale nedokazuje náhodnost chybění.

## 7.5 Shrnutí

Studie 3 v zaslepeném uspořádání porovnala 324
<!-- manifest kap7_k2_shoda_cisla: n_kazuistik=324 --> dvojic řešení hodnocených
šesti anotátorkami na čtyřech dimenzích. Primární smíšené modely ukázaly,
že řešení generovaná umělou inteligencí byla hodnocena jako vhodnější
a proaktivnější, učitelská jako behaviorálnější. Citlivostní ordinální
modely (Tabulka 7.2) směr všech efektů potvrdily s intervaly spolehlivosti
ležícími celými mimo hodnotu žádného rozdílu, stejně jako druhá citlivostní
analýza s náhodným sklonem zdroje po kazuistikách. Spolehlivost hodnocení
byla střední; náhodné efekty zohledňují závislost hodnocení, neodstraňují
však veškerou chybu měření. Dodatečný přepočet na úplných dvojicích
ověřuje citlivost na zacházení s chyběním. Ani tento přepočet nedokazuje,
že jsou chybějící odpovědi náhodné. Přibližně dvaapůlkrát častěji podle prostých četností
rozpoznávaly anotátorky v generovaných řešeních rámce opřené o důkazy
(oddíl 7.4). Učitelská řešení byla reaktivnější a behaviorálnější, což
odpovídá obrazu „repertoáru nejmenšího odporu“ ze Studie 1.

Interpretace však vyžaduje zdrženlivost, kterou rozvíjí kapitola 9.
Hodnocena byla textová podoba řešení, ne jeho proveditelnost v reálné
třídě. Učitelé řešili situaci v čase a pod tlakem, zatímco model
formuloval odpověď bez těchto omezení. Přes vynucenou paritu délky a stylu
nelze zcela vyloučit, že jazykové rysy generovaného textu hodnocení
ovlivnily. A výsledky se vážou k jedinému modelu (gpt-4o) a jediné
instrukci, takže je nelze bez dalšího zobecňovat na jazykové modely obecně
ani na jiné způsoby generování. Studie proto nedokládá, že „AI radí lépe
než učitel“. Dokládá, že generovaná řešení mají textové vlastnosti, které
vyškolení hodnotitelé spojují s kvalitním, proaktivním a rámcově
ukotveným postupem; pro zamýšlenou podpůrnou roli takových systémů je to
zjištění podstatné.

Právě podpůrné čtení výsledky spojuje se zbytkem knihy. Studie 1 ukázala
repertoár vychýlený k reaktivním, situačním zásahům; Studie 3 ukazuje, že
generovaná řešení nabízejí právě ten typ řešení, který v repertoáru
chybí: proaktivnější a rámcově ukotvený. Generované řešení tak může
učiteli nad konkrétní situací zviditelnit alternativy, jež jeho repertoár
nenabízí, aniž by nahrazovalo jeho úsudek o proveditelnosti. Zda takový
kontrast skutečně rozšiřuje repertoár, je otázka pro intervenční studii,
kterou tato kniha nedělá; její výsledky pro ni ale vymezují realistické
očekávání i rizika, včetně toho, že textová přesvědčivost není totéž co
pedagogická proveditelnost. Následující kapitola (Studie 4) obrací
pozornost od řešení k samotným kazuistikám a ptá se, jak spolehlivě lze
posoudit jejich kvalitu.

---
