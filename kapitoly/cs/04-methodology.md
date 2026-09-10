# 4. Metodologie


Kapitola popisuje metodologii knihy jako celku, aby jednotlivé studie mohly
odkazovat na společný rámec: jak chápeme korpus v čase, jak proběhly tři
anotační etapy, jak vznikala data od textu k analyzovatelné podobě, jaká
kódovací schémata se použila, jak nakládáme s opakovanými anotacemi téže
kazuistiky, jaké platí etické náležitosti a jak je zajištěna
reprodukovatelnost.

## 4.1 Korpus jako časová řada řezů

Data nepocházejí z jednorázového sběru, ale z databáze, která v čase roste
(kapitola 3). Každá analýza se proto váže na pojmenovaný časový řez korpusu,
nikoli na „korpus“ obecně. Kniha pracuje s doloženými řezy od roku 2023 po
export z května 2026 (přehled uvádí Tabulka 5.1 ve Studii 1). Z tohoto pojetí
plynou dva důsledky, které platí napříč studiemi. Čísla z různých řezů nelze
bez rozmyslu srovnávat ani slučovat; rozdíly ve velikosti korpusu odrážejí
jeho růst a publikační pohyb, nikoli chybu. A publikační status kazuistiky
(zveřejněná, či interní) je samostatná proměnná: řez z května 2026 obsahuje
pouze zveřejněné kazuistiky, přičemž část dříve zveřejněných byla mezitím
stažena. Analýzy proto s publikačním statusem pracují explicitně a nesměšují
zveřejněné a nezveřejněné kazuistiky bez uvedení.

## 4.2 Tři anotační etapy a jejich zaučování

Nad korpusem proběhly tři anotační etapy (kapitola 3). Každá měla stejnou
vnitřní logiku: zaučování anotátorek na malém vzorku, jedno či více
kalibračních kol se společným rozborem sporných případů, změření shody
a teprve poté finální anotování. Tato posloupnost je pro interpretaci
spolehlivosti zásadní, protože shodu vykazujeme z finálních kol, nikoli
ze zácviku, a případný vývoj shody mezi kalibrací a finálem pojmenováváme
jako samostatné zjištění (kapitola 9). Úplný registr etap, jejich kroků
a zúčastněných anotátorek (pod pseudonymy) uvádí příloha C; zdrojové datové
soubory jednotlivých událostí dokumentuje doprovodný repozitář.

Finální kolo první etapy (kvalitativní obsahové kódování) provádělo pět
anotátorek formou dělby práce: každá kódovala jiné kazuistiky, aby se pokryl
co největší rozsah korpusu, s vestavěným překryvem pro kontrolu shody. Druhá
etapa (hodnocení kvality řešení) zapojila šest anotátorek, které v zaslepeném
uspořádání hodnotily každou dvojici řešení nezávisle; materiál etapy tvořilo 324
<!-- manifest kap7_k2_shoda_cisla: n_kazuistik=324 --> kazuistik
z kategorií agresivního chování (fyzická a verbální agrese), k nimž bylo jazykovým modelem
vygenerováno alternativní řešení s vynucenou paritou délky a stylu (podrobně
Studie 3 a příloha B).

### Třetí etapa

Třetí etapa (kvalita kazuistik, dopad a vhodnost řešení) proběhla se dvěma
anotátorkami, v knize pod pseudonymy A2 a A12, nad celým zveřejněným řezem
z května 2026. Řez byl rozdělen na dvě poloviny s vestavěným překryvem:
anotátorka A12 ohodnotila 1 947
<!-- manifest kap8_kvalita_cisla: n_radku_A12=1947 --> kazuistik, anotátorka A2
dalších 1 938; <!-- manifest kap8_kvalita_cisla: n_radku_A2=1938 --> obě
společně hodnotily překryv 693
<!-- manifest kap8_kvalita_cisla: n_prekryv=693 --> kazuistik, z něhož se
počítá shoda. Etapa měla stejnou posloupnost jako předchozí: zácvik na šesti
kazuistikách, první pilot na 19 kazuistikách a druhý pilot na 49
<!-- manifest priloha_c_cisla: c1_k3_pilot2_26=49 --> kazuistikách se
společným rozborem neshod, poté finální anotování od března do září 2026.
Uprostřed finálního kola, v červenci 2026, se anotátorkám rozešla škála
vhodnosti; etapa proto zařadila rekalibraci, tedy společný podklad
s kotvícími kazuistikami pro jednotlivé stupně škály a schůzku nad 40
<!-- manifest kap8_kvalita_cisla: adj_vybrano_vhodnost=40 --> spornými
kazuistikami. Rekalibrace uprostřed sběru je změna protokolu; kniha ji
vykazuje jako takovou a projednané kazuistiky vylučuje z primárního výpočtu
shody (kapitola 8). Etapa byla uzavřena stop-rozhodnutím 8. září 2026, kdy
vznikl řez `K3_freeze_2026-09-08` z finálních tabulek obou anotátorek;
dohodnuté známky u sporných případů, které anotátorky dodaly později, do
řezu nevstupují a slouží jen jako referenční štítky. Průběh, shodu i její
vývoj během etapy popisuje Studie 4 (kapitola 8).

## 4.3 Od textu k datům

Odevzdané texty procházejí postupem zpracování, jehož tři kroky (extrakce
a strukturace, vícestupňová anonymizace, publikace) shrnuje kapitola 3.
Z metodologického hlediska jsou podstatné tři body. Extrakce dělí odevzdaný
soubor na jednotlivé kazuistiky a jejich čtyři části, přičemž u části dat
asistuje jazykový model; strukturace se proto může u některých kazuistik
lišit kvalitou a některé starší kazuistiky nesou stopy nedokonalé extrakce
(viz oddíl 4.6). Anonymizace je trojstupňová s ruční kontrolou; její protokol
uvádí příloha D a etické náležitosti shrnuje oddíl 4.7 (data analyzovaná
v knize prošla první generací tohoto postupu; současný stav platformy,
s anonymizací na národní e-infrastruktuře, popisuje příloha D.2). Publikace je
selektivní, což zakládá proměnnou publikačního statusu (oddíl 4.1).

Pro analýzy je klíčové, že tytéž kazuistiky se objevují v různých řezech
a souborech pod odlišnými identifikátory. Napříč knihou proto pracujeme
s jednotným identifikátorem kazuistiky, který propojuje záznamy z různých
řezů; tam, kde chybí sdílený identifikátor, se kazuistiky párují přes otisk
textu, a nejednoznačné případy se neslučují. Tento krok je předpokladem
jakéhokoli srovnání napříč etapami.

## 4.4 Kódovací schémata a řezy dat

Každá etapa má vlastní kódovací schéma; schémata se nesměšují. První etapa
kódovala tři dimenze (typ chování, typ řešení, dopad) do kategorií, jejichž
plné znění uvádí příloha A. Druhá etapa hodnotila řešení na čtyřech
ordinálních škálách a přidělovala rámcové štítky. Třetí etapa posuzovala
kvalitu kazuistiky, dopad a vhodnost řešení na vlastních škálách. Škály
nesoucí podobný název v různých etapách (například vhodnost v druhé a třetí
etapě) mají odlišný rozsah i význam a nesmějí se slučovat. Jedinou
výjimkou, kterou kniha používá, je dopad řešení: první etapa jej kódovala
do čtyř kategorií a třetí do tří, a pro srovnání obou etap (kapitola 8)
se částečný a krátkodobý úspěch první etapy slučují do jedné kategorie
explicitním pravidlem, ne posuzovatelským úsudkem.

Toto sloučení kategorií však neodstraňuje rozdíl mezi popsaným výsledkem
a hodnotovým posouzením. Historický manuál první etapy řadí mezi neúspěchy
i eticky nepřijatelné prostředky; třetí etapa může takový případ označit
za plochý. Z konečných štítků nelze spolehlivě rekonstruovat důvod tohoto
rozhodnutí. Historická data nepřekódujeme odhadem: asociace proto
interpretujeme jako vztahy mezi takto definovanými kategoriemi, nikoli
jako nezávislé měření pedagogické účinnosti.

Deskriptivní výsledky první etapy (Studie 1) uvádíme na reprodukovatelném
řezu 1 359
<!-- manifest kap5_korpus_cisla: n_k1_rez=1359 --> ručně kódovaných kazuistik.
Tento řez je definován jednoznačným pravidlem (deduplikované kazuistiky
z matice ze srpna 2024, jimž byla přiřazena lidská anotace) a je reprodukovatelný
skriptem. Že anotační sloupce matice skutečně nesou lidské kódování, dokládá
nezávislé srovnání s dochovanými anotačními listy etapy: množiny přiřazených
kategorií se shodují u 97 %
<!-- manifest kap4_provenience_cisla: prov_chovani_shoda_mnozin=0.9677 -->
kazuistik u typu chování, u 95 %
<!-- manifest kap4_provenience_cisla: prov_reseni_shoda_mnozin=0.9548 -->
u typu řešení a u 98 %
<!-- manifest kap4_provenience_cisla: prov_dopad_shoda_mnozin=0.9783 -->
u dopadu; přímý lidský záznam se dochoval pro 1 350
<!-- manifest kap4_provenience_cisla: prov_rez_pokryto_lidskou=1350 -->
kazuistik řezu. Dřívější dílčí výstupy projektu uváděly o něco nižší počet
kódovaných kazuistik, odpovídající tehdejšímu stavu pracovní databáze; kniha
pracuje výhradně s výše vymezeným řezem. Obdobně je vymezen řez třetí etapy
`K3_freeze_2026-09-08`: finální tabulky obou anotátorek k 8. září 2026,
spárované s kazuistikami zveřejněného řezu přes jednotný identifikátor
(oddíl 4.3), s otisky souborů uloženými v doprovodném repozitáři.

## 4.5 Multiplicita anotací

Protože kazuistiky prošly etapami nerovnoměrně, je počítání s opakovanými
anotacemi samostatným metodologickým problémem. Na úrovni jednotlivých etap
je typické, že jedné kazuistice bylo přiřazeno více kategorií zároveň (kódování
je víceznačné); frekvence proto vždy odlišujeme jako počet kazuistik s danou
kategorií od počtu přiřazení. Na úrovni celku prošlo 973
<!-- manifest kap4_metodologie_cisla: prekryv_ge2_kampane=973 --> kazuistik
alespoň dvěma různými etapami a 236
<!-- manifest kap4_metodologie_cisla: prekryv_ge3_kampane=236 --> všemi
třemi; třetí etapa totiž pokryla téměř celý zveřejněný řez z května 2026,
takže se překrývá s oběma předchozími. Počítáme-li jemněji jednotlivé
anotační události (táž etapa mohla kazuistiku zasáhnout opakovaně,
například v pilotním a finálním kole), bylo ve dvou událostech anotováno 790
<!-- manifest kap4_metodologie_cisla: multiplicita_2x=790 --> kazuistik,
ve třech 241, <!-- manifest kap4_metodologie_cisla: multiplicita_3x=241 -->
ve čtyřech 20 <!-- manifest kap4_metodologie_cisla: multiplicita_4x=20 -->
a v jednom případě v pěti;
<!-- necislo: jedna kazuistika v 5 událostech --> celkem tak více než
jednou událostí prošlo 1 052
<!-- manifest kap4_metodologie_cisla: prekryv_ge2_udalosti=1052 --> kazuistik.
Přehled anotačních událostí dokládá příloha C; úplná matice
pokrytí (kazuistika × událost) je součástí doprovodného repozitáře.

Z toho plyne závazné pravidlo: opakované anotace téže kazuistiky nejsou
nezávislá pozorování. Všude, kde je to relevantní, proto modelujeme kazuistiku
jako náhodný efekt (smíšené modely ve Studii 3), nikoli jako nezávislé
jednotky, a nikde neslučujeme hodnocení téže kazuistiky napříč nekompatibilními
škálami.

## 4.6 Známá omezení dat

Kniha pojmenovává tři známá omezení už v metodologii. Za prvé, 52
<!-- manifest kap5_korpus_cisla: n_vyrazeno_delky_trunc=52 --> kazuistik
bylo v minulosti dotčeno zkrácením textu při automatické extrakci; u menší
části z nich je v aktuálním řezu doložena oprava, u většiny nikoli, a proto
z analýz závislých na délce textu konzervativně vylučujeme všechny dotčené.
Za druhé, kódovací schémata se mezi verzemi mírně vyvíjela (například počet
kategorií řešení); verzi schématu proto u každé analýzy výslovně uvádíme
a kategorie napříč verzemi nemapujeme mlčky. Za třetí, nízký koeficient
shody mezi anotátory může mít dvě odlišné příčiny, které důsledně
rozlišujeme: skutečnou nejednoznačnost úsudku danou jemností a překryvností
kategorií, a silně nevyvážené rozdělení odpovědí, které srazí koeficient
i při vysoké hrubé shodě (paradox shody). Koeficienty proto všude uvádíme
spolu s hrubou shodou a u silně nevyvážených škál třetí etapy doplňujeme
i koeficient odolný vůči nevyváženosti (kapitola 8).

## 4.7 Etika

Sběr probíhal s informovaným souhlasem přispěvatelů a bez sběru přímých
osobních údajů; výzkumný projekt schválila Etická komise pro výzkum Masarykovy
univerzity pod jednacím číslem EKV-2022-118, s finálním schválením dne
27. 9. 2023. <!-- necislo: jednací číslo a datum stanoviska EKV --> Autoři
kazuistik přitom nejsou předmětem výzkumu; jejich postavení a informované
prohlášení rozvádí příloha D. Kazuistiky jsou anonymizované a v datech ani
v textu knihy nevystupují přímé identifikátory žáků, škol ani pisatelů;
anotátorky uvádíme pouze pod projektovými pseudonymy A1 až A12.
Ve veřejné tabulce K2 je samostatná lokální řada A1 až A6; shodné číslo
neznamená totožnou osobu napříč těmito dvěma řadami. Nezveřejněné kazuistiky
se nedostávají do žádných veřejných výstupů knihy. Znění informovaného
souhlasu a anonymizační protokol uvádí příloha D.

## 4.8 Reprodukovatelnost

Příprava dat probíhá v jazyce Python, inferenční statistika v jazyce R
s uzamčeným prostředím. Každá analýza je zapsána jako spustitelný dokument,
který od zdrojových dat vytvoří výsledný report a tabulku výsledných hodnot
(název míry a její hodnota, spolu s údajem o skriptu, verzi vstupních dat
a nastavení náhodného výběru). Text knihy uvádí čísla jen z těchto tabulek
a před každým sestavením knihy automatická kontrola ověřuje, že čísla
v textu odpovídají výsledkům analýz a že každá citace má záznam v seznamu
literatury. Analýzy přitom předcházejí próze: každá se nejprve uzavře nad
verzovaným řezem dat a teprve poté se píše text s výsledky. Všechna čísla
v knize jsou tak dohledatelná až ke skriptu a verzi dat.

Ověřitelnost nekončí u autora. Doprovodný repozitář zpřístupňuje analýzy
v R, tabulky výsledných hodnot, HTML reporty, skripty obrázků i veřejnou
datovou podmnožinu bez textů kazuistik a bez osobních údajů; jeho součástí
je český návod, jak si čísla knihy ověřit bez programátorských znalostí,
a konfigurace prostředí pro opakování analýz.
Studie 1 a 2 jsou přepočitatelné z veřejných odvozených dat, která nenesou
texty kazuistik ani jména: Studie 1 z tabulky počtů slov, věku
a publikačního statusu na úrovni kazuistiky a z anotačních štítků, Studie 2
z tabulky kategorií přiřazených člověkem a modelem. Studie 3 se přepočítá
z tabulky hodnocení dvojic řešení, v níž jsou anotátorky pod pseudonymy
a která neobsahuje texty kazuistik; její úplná podoba (včetně textů) je
uložena v balíčku na platformě OSF (odkaz bude zveřejněn s publikací
souvisejícího článku, do té doby na vyžádání). Studie 4 se přepočítá
z tabulky hodnocení třetí etapy, opět bez textů a pod pseudonymy. Doprovodný repozitář nezpřístupňuje úplné textové vstupy těchto analýz.
Odvozené tabulky umožňují přepočet statistik, nikoli opakování samotného
kódování, generování odpovědí nebo prověření anonymizace. Součástí
reprodukce jsou i uložené predikce; nové volání modelu je jiný experiment.
Historické monitorovací a provenienční souhrny se přebírají jako označené
vstupy. Toto vymezení doprovodného balíčku nepředjímá budoucí vydání
nejnovější databáze.

---
