# 9. Diskuse


Čtyři studie této knihy položily čtyři otázky nad jedním korpusem. Tato
kapitola je čte dohromady. Nejprve shrne, co která studie zjistila a s jakou
jistotou (9.1). Poté rozvine tři motivy, které studie spojují: repertoár
nejmenšího odporu jako empirický obraz učitelské praxe (9.2), otázku, co
lze jazykovému modelu v pedagogickém výzkumu svěřit (9.3), a spolehlivost
posouzení jako proměnnou, kterou je třeba měřit, ne předpokládat (9.4).
Následují omezení (9.5), důsledky pro přípravu učitelů, pro platformu
Edustories a pro výzkum s jazykovými modely (9.6) a směry dalšího výzkumu
(9.7).

## 9.1 Oblouk čtyř studií

Kniha začala materiálem a skončila u hranic jeho použitelnosti. Studie 1
vybudovala a popsala korpus, Studie 2 prověřila jazykový model jako
anotátora tohoto korpusu, Studie 3 nechala lidi zaslepeně hodnotit řešení,
která model generuje, a Studie 4 se ptala, jak spolehlivě lze posoudit
kvalitu kazuistik a úspěšnost řešení a nakolik to dokáže model předvídat.
Tabulka 9.1 shrnuje odpovědi a míru jistoty, s níž je kniha předkládá.

\needspace{18\baselineskip}

\footnotesize

**Tabulka 9.1.** Výzkumné otázky, hlavní zjištění a míra jistoty.

| Otázka | Hlavní zjištění | Míra jistoty |
|---|---|---|
| VO1: korpus a jeho obsah (Studie 1) | Zveřejněný řez čítá 3 202 <!-- manifest kap5_korpus_cisla: n_korpus_s6=3202 --> kazuistik se čtyřdílnou strukturou. V repertoáru dominuje rozhovor (v 922 <!-- manifest kap5_korpus_cisla: k1_reseni_pripadu:Rozhovor=922 --> z 1 359 <!-- manifest kap5_korpus_cisla: n_k1_rez=1359 --> kódovaných kazuistik) a další reaktivní kroky; vztahová a kolektivní řešení se pojí s příznivějším vnímaným výsledkem. | Vysoká pro četnosti a strukturu; souběhy řešení a dopadu jsou popis, ne příčina. |
| VO2: model jako anotátor (Studie 2) | κ = 0,64 <!-- manifest kap6_kodovani_cisla: kappa_llm_clovek=0.6445 --> na úplných dvojicích, po dodatečném vyloučení překryvů s příklady κ = 0,61. <!-- manifest kap6_kodovani_cisla: bez_prekryvu_kappa=0.6143 --> | Omezená validace; retrospektivní citlivost není nový nezávislý test a nesrovnává výkon modelu s lidským stropem. |
| VO3: generovaná versus učitelská řešení (Studie 3) | Učitelská řešení hodnocena jako méně vhodná (rozdíl −0,85 <!-- manifest kap7_k2_shoda_cisla: lmm_b1_ucitel_vhodnost=-0.8547 --> bodu), reaktivnější a behaviorálnější; šance na rozpoznání rámce třetinová (OR 0,31). <!-- manifest kap7_k2_shoda_cisla: glmm_or_ucitel_ramce=0.3127 --> | Vysoká pro směr a robustnost efektů v textové podobě řešení; nevypovídá o proveditelnosti. |
| VO4: kvalita, spolehlivost, predikce (Studie 4) | Posouzení použitelnosti kazuistiky s vysokou vzájemnou shodou (κ = 0,77, <!-- manifest kap8_kvalita_cisla: shoda_kvalita_kappa=0.7689 --> AC1 = 0,98), <!-- manifest kap8_kvalita_cisla: shoda_kvalita_ac1=0.9773 --> dopadu spolehlivé (κ = 0,69), <!-- manifest kap8_kvalita_cisla: shoda_dopad_kappa=0.6875 --> vhodnosti střední (vážená κ = 0,52); <!-- manifest kap8_kvalita_cisla: shoda_vhodnost_wkappa=0.5188 --> dopad se při opakovaném čtení týchž textů jinou anotátorkou shoduje κ = 0,59. <!-- manifest kap8_kvalita_cisla: k1k3_dopad_kappa=0.588 --> Předpověď dopadu jazykovým modelem dosáhla vyvážené přesnosti 60 % <!-- manifest kap8_predikce_cisla: predikce_kimi_k3_zero_shot_konsenzus_bal_acc=0.6002 --> proti 33 % <!-- manifest kap8_predikce_cisla: predikce_majorita_bal_acc=0.3333 --> u hádání a 80 % <!-- manifest kap8_predikce_cisla: predikce_clovek_clovek_bal_acc=0.802 --> u shody dvou lidí. | Vzájemná shoda není správnost vůči externímu kritériu; predikce omezená a s výhradou, že lidé výstup četli. |

*Poznámka.* Hodnoty ze zdrojových čísel studií 1 až 4 (kapitoly 5 až 8); intervaly spolehlivosti a podmínky výpočtu uvádějí příslušné kapitoly.

\normalsize

Čtyři odpovědi drží pohromadě dvěma způsoby. Zaprvé věcně: obraz
repertoáru ze Studie 1 se vrací ve Studii 3 jako pozadí, na němž vynikají
generovaná řešení, a ve Studii 4 jako souvislost kategorií při opakovaném čtení týchž kazuistik. Zadruhé metodologicky: každý výsledek o modelu je
vztažen k lidskému měřítku, jehož spolehlivost kniha měří místo toho, aby
ji předpokládala. Právě tento druhý způsob dává knize tvar validačního
žebříku popsaného v kapitole 3. Model byl nejprve poměřen lidmi v úloze,
kterou lidé umějí (klasifikace), poté lidé zaslepeně hodnotili to, co model
dokáže vytvořit (alternativní řešení), a nakonec kniha změřila,
kde končí spolehlivost lidí samotných. Odpovědi tak nejsou čtyři izolovaná
čísla, ale stupně jedné otázky: co lze o učitelských repertoárech zjistit
z textu a komu, člověku nebo stroji, lze které čtení textu svěřit.

## 9.2 Repertoár nejmenšího odporu

Kapitola 2 zavedla repertoár nejmenšího odporu jako interpretační pojem
pro převahu snadno dostupných reakcí v zaznamenaných situacích. Studie
mapují frekvence a vlastnosti textů; neměří však úplný repertoár
jednotlivce, jeho znalosti, časový tlak ani vznik konkrétního rozhodnutí.
Mechanismy učňovství pozorováním a situační dostupnosti proto zůstávají
hypotézami pro další výzkum.

Studie 1 dala pojmu obsah. Rozhovor je přítomen ve dvou třetinách
kódovaných kazuistik a za ním následují spolupráce s odborníky, podpora,
důsledky a upozornění; samostatnou proaktivní kategorii finální schéma
ani neobsahovalo: příslušné podkategorie byly při vývoji schématu přesunuty.
Absence samostatné kategorie proto není dokladem absence proaktivního jednání. Studie 3
přidala měřítko zvenčí. Když šest anotátorek zaslepeně hodnotilo
učitelské řešení vedle řešení generovaného pro tutéž situaci, bylo
učitelské reaktivnější (rozdíl −1,01
<!-- manifest kap7_k2_shoda_cisla: lmm_b1_ucitel_reaktivni=-1.01 --> bodu)
a behaviorálnější (o 0,77
<!-- manifest kap7_k2_shoda_cisla: lmm_b1_ucitel_humanisticke=0.7719 --> bodu)
a mělo jen třetinovou šanci na to, že v něm anotátorky rozpoznají některý
z pojmenovaných přístupů. Studie 4 pak ukázala, že
vzorec ze Studie 1, podle něhož se vztahová a kolektivní řešení pojí
s příznivějším výsledkem než řešení represivní, přečte z týchž kazuistik
i pozdější anotátorka. Na týchž kazuistikách hodnotil první tým podíl dlouhodobého
úspěchu u práce s kolektivem na 70 %
<!-- manifest kap8_kvalita_cisla: reseni_prace_s_kolektivem_du_podil_k1=0.7027 --> a třetí
etapa na 51 %,
<!-- manifest kap8_kvalita_cisla: reseni_prace_s_kolektivem_du_podil=0.5135 -->
u rozhovoru na 50 %
<!-- manifest kap8_kvalita_cisla: reseni_rozhovor_du_podil_k1=0.4989 --> a 42 %,
<!-- manifest kap8_kvalita_cisla: reseni_rozhovor_du_podil=0.4209 --> u upozornění na 38 %
<!-- manifest kap8_kvalita_cisla: reseni_upozorneni_du_podil_k1=0.3846 --> a 30 %.
<!-- manifest kap8_kvalita_cisla: reseni_upozorneni_du_podil=0.2967 --> U těchto příkladů jsou podíly třetí etapy nižší; neplatí to pro všechny
kategorie a ani jejich pořadí není totožné (Tabulka 8.3).

Proč repertoár vypadá právě takto, vysvětluje kapitola 2 dvěma mechanismy,
které data knihy nemohou přímo testovat, ale s nimiž jsou v souladu.
Učňovství pozorováním (Lortie, 1975) dodává učitelům zásobu postupů,
které viděli z lavice: napomenutí, domluvu, trest, poslání za dveře.
Proaktivní práce může být z lavice méně viditelná a časový tlak může
zvýhodnit dostupné postupy. Tato vysvětlení však předložená data přímo
neověřují. Repertoár nejmenšího odporu tedy není označení
pro pohodlnost učitelů. Je to hypotetický výklad vztahu mezi profesním učením a podmínkami jednání; v pojetí, které nabízí
Swidler (1986), jde o zásobu, z níž se strategie skládají, ne o volbu mezi
známými alternativami. S tímto čtením se shoduje i domácí výzkum, který
reaktivní strategie zachytil přímým pozorováním praxe (Vlčková et al.,
2020) a v situacích začínajících učitelů (Karasová a Nehyba, 2025),
a evidence oboru, která proaktivním a strukturovaným strategiím přiznává
větší přínos (Korpershoek et al., 2016; Simonsen et al., 2008).

Jedno upřesnění je podstatné. Reaktivnost repertoáru neznamená, že by
učitelé zůstávali na řešení sami: spolupráce s odborníky patří
k nejčastějším krokům. Znamená, že i tento krok je spouštěn incidentem.
A vzorec dopadů zůstává popisem souběhů, jak opakují kapitoly 5 a 8:
učitelé si typ řešení nevybírají náhodně, k trestu sahají v situacích
s horšími vyhlídkami a dopad posuzuje čtenář sebevýpovědi. Opakované čtení jinou anotátorkou kauzální interpretaci nezakládá.
Historické kódy navíc částečně spojují výsledek s přijatelností prostředku;
bez jejich oddělení nelze vztah kategorií pokládat za nezávislou validaci
účinnosti.

## 9.3 Co lze jazykovému modelu svěřit

Kniha prověřuje tři odlišné role: anotátora, generátora a prediktora.
Ve Studii 2 dosahuje κ vůči lidskému kódu typu řešení 0,64
<!-- manifest kap6_kodovani_cisla: kappa_llm_clovek=0.6445 -->,
po dodatečném vyloučení zjištěného překryvu příkladů 0,61
<!-- manifest kap6_kodovani_cisla: bez_prekryvu_kappa=0.6143 -->.
Přenos poznatků z krátkých anglických textů (Gilardi et al., 2023;
Törnberg, 2025) na tento korpus je tedy podpořen jen omezeně: chybí nový
test nezávislý na vývoji promptu. Lidské α z jiného uspořádání není
výkonovým stropem modelu. Část neshod může souviset se schématem, ale
podíl takových neshod zde nelze určit.

V roli generátora model obstál v zaslepeném lidském hodnocení. Jeho řešení
byla hodnocena jako vhodnější a proaktivnější a nesla rozpoznatelné rysy
přístupů opřených o důkazy, aniž k tomu byl model instruován. Kniha z toho
nevyvozuje, že „AI radí lépe než učitel“. Hodnocen byl text, ne jednání ve
třídě; model odpovídal bez časového tlaku a bez odpovědnosti za následky;
a výsledky se vážou k jedinému modelu a jediné instrukci. Co lze z výsledku
vyvodit, je skromnější a užitečnější: generované řešení nabízí učiteli nad
konkrétní situací kontrast k zaznamenanému postupu. Zda učitel tento
postup již zná, studie nezjišťovala. Zda takový kontrast repertoár rozšiřuje, je otázka pro
intervenční studii.

Modelové posuzování vhodnosti kniha přímo netestovala. Z lidské shody
proto nelze dovozovat úspěch ani selhání modelu v této roli. Studie 4 ukázala proč. Vhodnost řešení
posuzují i dvě vyškolené anotátorky jen se střední shodou (vážená κ = 0,52)
<!-- manifest kap8_kvalita_cisla: shoda_vhodnost_wkappa=0.5188 --> a ve druhé
etapě šest anotátorek s α = 0,53.
<!-- manifest kap7_k2_shoda_cisla: alpha_ord_final_vhodnost=0.5274 --> Model
posuzující vhodnost by tedy byl validován proti měkkému měřítku a jeho
„shoda s lidmi“ by vypovídala hlavně o tom, se kterým člověkem se shoduje.
Naopak dopad řešení, jak jej pisatel popsal, posuzují lidé spolehlivě
(κ = 0,69 <!-- manifest kap8_kvalita_cisla: shoda_dopad_kappa=0.6875 --> uvnitř
etapy, κ = 0,59
<!-- manifest kap8_kvalita_cisla: k1k3_dopad_kappa=0.588 --> mezi etapami),
a právě proto je dopad tou dimenzí, na níž kniha model prověřuje v roli
prediktora (oddíl 8.6). Predikce má však jinou logiku než posouzení:
anotátorky výstup četly, model jej nevidí. Srovnání proto neříká, zda model
předvídá lépe než člověk, ale zda se s lidským čtením výsledku shoduje tak
jako druhý člověk.
Predikční experiment dosáhl vyvážené přesnosti 60 %
<!-- manifest kap8_predikce_cisla: predikce_kimi_k3_zero_shot_konsenzus_bal_acc=0.6002 -->.
Intervaly párových rozdílů mezi modely a variantami zahrnují nulu
(oddíl 8.6). Výsledek nedokládá ekvivalenci ani informační strop úlohy.
Chybí lidská predikce při stejné informaci a externí měření skutečného
dopadu ve třídě; pro individuální doporučování proto tato validace nestačí.


Z toho plyne rozdělení rolí, které kniha doporučuje. Modelu lze svěřit
klasifikaci obsahu velkého korpusu na úrovni kategorií, vždy po validaci
na vlastních datech proti lidskému kódování s doloženou reliabilitou
(Reiss, 2023; Ziems et al., 2024). Lze mu svěřit generování kontrastních
řešení pro reflexi, ne pro rozhodnutí. Nelze mu svěřit posouzení
vhodnosti bez lidské reference ani rozhodování o jednotlivém žákovi.
A protože poskytovatelé modely průběžně mění (Ollion et al., 2024), platí
každý takový výsledek pro doložený běh a instrukci. Alias služby a otisk
odpovědi však nezaručují totožnost vah; omezení popisuje příloha B.

## 9.4 Spolehlivost jako proměnná, ne konstanta

Nejméně nápadným, ale pro metodologii nejdůležitějším výsledkem knihy je,
jak se chovala spolehlivost lidského posouzení. Nebyla vlastností
anotátorek ani konstantou etapy. Měnila se s konstruktem, se schématem,
s fází etapy a s časem, a kniha tyto změny měřila.

S konstruktem: Obrázek 8.3 řadí koeficienty všech tří etap podle
náročnosti úsudku. Binární kvalita kazuistiky a dopad se třemi kategoriemi
leží nad konvenčním prahem, úsudkové škály vhodnosti a orientací řešení
pod ním a jedenáctikategoriální schéma typů řešení nejníže. Se schématem:
u typu řešení srazila shodu jemnost a překryvnost kategorií, což ukázal
Jaccardův index 0,56
<!-- manifest kap6_kodovani_cisla: k1_jaccard_reseni=0.5571 --> přiznávající
částečný překryv, zatímco α trestá každou neshodu stejně. S fází etapy: ve
třetí etapě dosáhl druhý pilot na padesáti kazuistikách κ nad 0,8
<!-- necislo: pilotní hodnoty z podkladu etapy, doslovně příloha A.3 --> u dopadu
i vhodnosti, finální kolo na stovkách kazuistik však κ = 0,69
<!-- manifest kap8_kvalita_cisla: shoda_dopad_kappa=0.6875 --> a vážené κ = 0,52.
<!-- manifest kap8_kvalita_cisla: shoda_vhodnost_wkappa=0.5188 --> Pilotní
shoda je měřena krátce po společném rozboru, na malém vzorku a s čerstvou
instrukcí; finální shoda po měsících samostatné práce. Kniha proto
spolehlivost vykazuje z finálních kol, a kde má obě hodnoty, uvádí obě.
Totéž platí pro druhou etapu, jejíž dvě kalibrační kola byla malá a
společně rozebíraná; srovnatelný pilotní koeficient pro ni kniha nemá,
a proto se i tam opírá jen o finální kolo. A s časem: uprostřed třetí
etapy se škála vhodnosti oběma anotátorkám rozešla o půl stupně.
V pozdějším segmentu byl průměrný rozdíl menší bez obdobného růstu vážené
shody; samostatný účinek rekalibrace však tento design neidentifikuje
(oddíl 8.4). <!-- necislo: hodnoty kotveny v kapitole 8 -->

Z těchto pozorování kniha odvozuje čtyři pravidla, která považuje za svůj
metodologický příspěvek pro výzkum s posuzovateli, lidskými i strojovými.
Koeficient se uvádí vždy s hrubou shodou a u nevyvážených kategorií
s mírou odolnou vůči nevyváženosti, protože paradox shody (Feinstein
a Cicchetti, 1990; Gwet, 2008) vede při vysoké hrubé shodě kvality k nižšímu κ se širokým intervalem. Spolehlivost se vykazuje z finálních
dat, ne z pilotu. Zásah do protokolu uprostřed sběru, jako byla
rekalibrace, se přizná, kvantifikuje a projednané případy se z primárního
výpočtu vyloučí, protože po projednání už nejde o nezávislá měření.
A zpětné přepisy hodnocení se v datech označují; kde se to nestalo, jako
ve třetí etapě, pomůže archivovaná starší verze týchž tabulek. Řádkový rozdíl
mezi ní a finálem segmenty rekonstruuje a zpětné přepisy pojmenuje, takže
i dodatečně lze vykázat shodu zvlášť pro dobu před zásahem a po něm. Právě
to ve třetí etapě rozlišilo změnu průměrného rozdílu od vážené shody.
Časová souvislost s rekalibrací přitom není jejím kauzálním účinkem. Zálohovaná verze dat je tedy metodologický nástroj,
ne jen pojistka proti ztrátě. Tato pravidla nejsou nová v teorii reliability
(Krippendorff, 2018; Hallgren, 2012); nová je jejich uplatnění na dlouhé,
vícefázové anotační etapy nad pedagogickým textem, kde se shoda v čase
prokazatelně mění.

## 9.5 Omezení

Omezení knihy plynou z povahy materiálu, z uspořádání studií a z nástroje.

Materiál je korpus dobrovolně psaných sebevýpovědí. Kazuistiky
nadreprezentují dramatické situace, dopad posuzuje čtenář toho, co pisatel
o výsledku napsal, a zrcadlová šablona vede pisatele k jednoznačně
vydařeným a jednoznačně nevydařeným situacím, takže částečné úspěchy jsou
v korpusu vzácnější než v praxi (kapitoly 3 a 5). Korpus roste a kniha
pracuje s datovanými řezy; každé číslo platí pro svůj řez. Část kazuistik
je psána slovensky nebo nese anglické zástupné označení žáka a část byla
v minulosti dotčena zkrácením textu při extrakci; kniha tyto případy
z analýz závislých na délce vylučuje, jazykovou vrstvu však popisuje jen
z komentářů anotátorek (kapitoly 4 a 8). Kódovací schémata se mezi
etapami liší a kniha je nesměšuje; jedinou převodní operací je sloučení
částečného a krátkodobého úspěchu pro srovnání dopadu mezi etapami.

Uspořádání studií je popisné a srovnávací, ne intervenční. Souběhy typů
řešení s dopadem nezakládají kauzální tvrzení a kniha jich žádné nečiní.
Zaslepené hodnocení ve Studii 3 chránilo před zkreslením očekáváním, ale
hodnotilo text, ne jednání ve třídě. Třetí etapu nesly jen dvě anotátorky,
její adjudikace zůstala nedokončená a rekalibrace uprostřed sběru je
změnou protokolu; její účinek lze doložit jen proto, že se dochovala starší
verze tabulek, a i pak jde o srovnání dvou různých souborů kazuistik. Kazuistiky
prošly etapami nerovnoměrně a část jich prošla několika, což kniha eviduje
v matici pokrytí (kapitola 4), ale co omezuje čtení překryvů jako
nezávislých vzorků.

Studie 2 a 3 pracovaly každá s konkrétním modelem a instrukcí.
Predikční experiment naproti tomu zahrnul více kandidátů ve vývoji
a dva modely při hodnocení, včetně varianty s příklady. Výsledky nelze
zobecnit na jiné instrukce, jazyky, poskytovatele ani budoucí verze.
Otevřené váhy a akademické nasazení nejsou zárukou totožnosti backendu;
otisk kontrolní odpovědi je jen doplňkovým údajem. Příloha B rozlišuje
doloženou identifikaci historického běhu od podmínek nového experimentu.
Lidé v predikčním srovnání výstup četli, model nikoli; lidská predikční
báze za shodných podmínek není k dispozici.

## 9.6 Důsledky

### Pro přípravu učitelů a školní praxi

Obraz repertoáru nejmenšího odporu nabízí podnět pro přípravu učitelů:
pracovat s konkrétními situacemi a vedle zaznamenaného postupu zvažovat
alternativy. Data však nerozhodují, zda rozdíly souvisejí s neznalostí,
časovým tlakem, dostupnými prostředky nebo vlastnostmi situace.
Kazuistiky a generované kontrasty mohou sloužit jako materiál k reflexi;
jejich účinek na jednání musí prověřit intervenční studie. Pozorované
asociace historických kategorií neopravňují k doporučení strategie jako
účinnější bez dalšího ověření.

### Pro platformu Edustories

Platforma nabízí řešení v šesti přístupech (kapitola 3).
Studie 3 však použila jednu instrukci bez předepsaného rámce, a není tedy
validací všech platformových generátorů. Studie 4 měřila lidské posouzení
použitelnosti; automatický filtr kvality netestovala. Pro platformu z toho
plynou návrhy k ověření: kontrola úplnosti před generováním, označení
výstupu jako materiálu k reflexi a sběr zpětné vazby o jeho využití.
Spolehlivost případného automatického filtru musí být vyhodnocena zvlášť.

### Pro jazykové modely v pedagogickém výzkumu

Pro výzkum kniha nabízí postup, který lze převzít: validovat model na
vlastních datech proti lidskému kódování s měřenou reliabilitou, vykazovat
shodu modelu s lidmi vždy vedle shody lidí mezi sebou, používat zaslepené
lidské hodnocení tam, kde model generuje, a dokumentovat verze modelů
i instrukcí. Doprovodný repozitář tento postup zpřístupňuje včetně
odvozených dat bez textů kazuistik, takže hlavní statistiky lze přepočítat bez nového volání modelu.
Původní anotace, textové kontroly a historické souhrny mají odlišný rozsah
ověřitelnosti popsaný v kapitole 4. Pro český pedagogický výzkum
je to první doklad, že jazykový model může být kriticky prověřeným
nástrojem analýzy velkého korpusu autentického českého textu.

## 9.7 Další výzkum

Tři směry plynou z výsledků přímo. První je intervenční studie kontrastu:
zda učitelé, kteří nad vlastní situací dostanou generované řešení v jiném
rámci, volí v dalších situacích proaktivnější kroky. Korpus a platforma
pro ni poskytují materiál i měřicí nástroj, velikost intervenčního účinku však tato kniha neodhaduje.

Druhým směrem je spolehlivost v čase. Třetí etapa ukázala, že se shoda
během měsíců samostatné práce mění. Rozdíly segmentů samostatný účinek
rekalibrace neidentifikují; příští etapa by měla mít časový
záznam každého hodnocení, průběžné kontrolní body a označené přepisy, aby
segmenty nebylo nutné rekonstruovat ze zálohy. Totéž uspořádání dovolí ověřit, zda pilotní shoda
předpovídá finální.

Třetím směrem je rozšíření modelů a jazyků. Výběr modelů zůstal omezený;
opakování Studie 2 a predikčního experimentu s dalšími modely, včetně
otevřených a lokálně provozovaných, by ukázalo, nakolik jsou výsledky
vlastností úlohy a nakolik vlastností jednoho poskytovatele. Anglická
datová sada Edustories-en (kapitola 3) navíc umožňuje ptát se, zda model
kóduje tentýž obsah v obou jazycích shodně, a tedy měřit jazykovou mezeru
přenosu přímo.

## 9.8 Shrnutí

Kniha propojuje popis korpusu, modelové kódování, zaslepené hodnocení
alternativních řešení a opakované lidské posouzení s predikcí dopadu.
Rozlišuje přitom frekvence od příčin volby strategií, shodu od správnosti
a hodnocení textu od účinku jednání. Modelové kódování má omezenou
retrospektivní validaci, generované alternativy byly hodnoceny příznivěji
a predikce dopadu zůstává nejistá. Žádný z těchto výsledků nestanovuje
univerzální lidský ani informační strop. Změny protokolu, překryvy příkladů,
neúplné odpovědi a normativní složka kategorií patří k výsledku, nikoli
jen k technickým poznámkám.

---
