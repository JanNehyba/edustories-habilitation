# Příloha A. Kódovací manuály


Tato příloha dokládá kódovací nástroje všech tří anotačních etap
v podobě, v jaké je anotátorky používaly. Definice kategorií a škálových
bodů jsou převzaty doslovně ze zdrojových souborů (včetně případných
stylistických nedokonalostí předlohy); komentář knihy je od citací
typograficky oddělen. Vývoj nástrojů mezi verzemi je popsán explicitně,
protože kniha verze schémat zásadně nesměšuje (kapitola 4).

## A.1 První etapa: kódovací kniha obsahového kódování

Kódovací kniha vznikala induktivně: v zácvičné fázi
(zima 2023/2024) anotátorky otevřeně kódovaly menší vzorky kazuistik do
vlastních listů a z těchto kódů byl postupně sestaven kódovací strom
(verze V1), který byl po kalibračních kolech zpřesněn do finální verze V2.
Verze V2 přidala anotační kódy (zkratky kategorií) a upřesnila definice;
kategorie chování „Neuposlechnutí pokynu“ z V1 byla ve V2 zrušena.
Finální anotování (kapitola 4) probíhalo podle V2 se závazným kódovacím
postupem, který zdrojový soubor uvádí takto:

```text
1. Při kódování kódujeme pouze to, co je explicitně napsáno, snažíme se
   vystihnout jen to, co přímo souvisí s problémem/řešením. […]
2. U kódů k řešení situací je to stejné - kóduji pouze to, co učitel
   explicitně zmiňuje, že použil jako konkrétní řešení (ne, co by si
   myslel, že by fungovalo; ne co se stalo o pár měsíců později).
3. Pozor na to, aby byly v kategoriích napsány přesné názvy kódů.
4. Pozor na to, jak zní definice kategorie, kterou ke kódu dáváte. Vždy
   si jí dobře pročtěte a zvažte, jestli i ta definice sedí s tím, co je
   v textu.

[z navazujícího seznamu téhož listu, bod 1:]
1. Flat/deep - budeme kódovat jako flat, pokud v kazuistice chybí nějaká
   část, pokud kazuistika z nějakého jiného důvodu nejde použít (je příliš
   stručná, není ze školního kontextu, nejedná se o popis problémové
   situace atd.). […]
```

*Poznámka.* Přepsáno z interního kódovacího stromu první etapy (list Kódovací postup). Výpustky vyznačeny […]; vynechány zbylé body navazujícího seznamu (kontrola správnosti výstupu šablony) a technická poznámka o zaškrtávací liště; plné znění ve zdrojovém souboru.

**Tabulka A.1.** Analyticky použité kategorie typů náročného chování
(finální verze V2; definice doslovně).

| Kategorie | Kód | Definice |
|---|---|---|
| Fyzická agrese | FAG | Žák/žákyně fyzicky napadá/poškozuje/ubližuje nebo hrozí ublížením spolužákům, učiteli, nebo ničí majetek školy nebo věci spolužáků/učitele (hází věcmi, rozbíjí věci, vyhrožuje nožem, kope do věcí, pere se, bije,...) |
| Verbální agrese | VAG | Žák záměrně používá verbální výraz/y, které jsou vulgární nebo mají za cíl ublížit (ponížit,...) učiteli/spolužákům. |
| Šikana | SIK | Dlouhodobé záměrné verbální nebo neverbální ubližování spolužákovi/spolužačce/učiteli. |
| Emoční výbuchy | EV | Afektivní - Vyafektované chování, krátkodobá silná a prudká emoční reakce na podnět při sníženém sebeovládání. Žák nezvládne nápor emocí. Může se to projevit tak, že je vybíjí agresivním chováním ven (udeří spolužáka, hází předměty, ničení nábytku školy,...) |
| Lhaní a podvody | LH | Žák/žákyně záměrně poskytuje nepravdivé informace učiteli/rodičům. |
| Nevěnování se výuce/Nepozornost při výuce | NEV | Žák/žákyně se nevěnuje výuce - nedává pozor, není aktivní, běhá po třídě, ignoruje pokyny učitele, spí, dívá se z okna, atd. |
| Neplnění školních povinností/nepřipravenost na výuku | NEP | Žák/žákyně neplní své školní povinnosti (učení se, nošení pomůcek,...) |
| Nezvládání výuky | NEZ | Dítěti brání absence dovednosti zvládat výuku. |
| Verbální narušování výuky | VER | Žák/žákyně narušuje hodinu verbálními projevy. |
| Porušování třídních/školních pravidel | PRA | Žák porušuje třídní nebo školní pravidla |
| Neverbální narušování výuky | NEVER | Žák/žákyně narušuje vyučování neverbálním chováním (interakcí s věcmi, hlučnými pohyby,...) |
| Sebedestruktivní chování | SEB | Žák/žákyně si záměrně ubližuje/hrozí ublížením. |
| Problémy s docházkou | DOC | Dívka chodila za školu. |

*Poznámka.* Přepsáno z interního kódovacího stromu první etapy (list
Problémové chování). Definice kategorie Problémy s docházkou je ve zdroji
formulována příkladem; ponecháno doslovně. Zdrojový strom obsahoval ještě
položku DIA, jejíž definice popisovala přítomnost diagnózy žáka, nikoli jeho
chování. V deskriptivě i výpočtu shody je proto vyřazena a údaj o diagnóze se
čte z kurátorovaného kontextového pole korpusu (oddíly 5.3, 5.4 a 6.3). Tím
zůstává zachován doklad původního nástroje, aniž by byla kontextová vlastnost
prezentována jako čtrnáctý typ chování.

**Tabulka A.2.** Kategorie typů řešení (finální verze V2; definice doslovně).

| Kategorie | Kód | Definice |
|---|---|---|
| Rozhovor | ROZ | Řešení problému rozhovorem (s rodiči, se žákem, s třídou,...). Cíleně vedený rozhovor za učelem zjištění více informací a řešení dané situace. |
| Dohoda | DOH | Dohoda učitele s žákem/třídou na společně přijatelném řešení. |
| Práce s kolektivem | KOL | Učitel řeší situaci skrze podporu vztahů ve třídě, čímž se snaží situaci vyřešit a zároveň předcházet dalším |
| Spolupráce s odborníky | SPO | Učitel vyhledává pomoc jinde - mezi odborníky v rámci školy i mimo školu. |
| Upozornění | UPO | Učitel popisuje žákovo chování, které je pro něj rušivé. Žák je verbálně upozorněn na rušivé chování. |
| Přemístění žáka | PRE | Učitel řeší situaci tak, že žák/žákyně opouští danou situaci a je přemístěn(a) v rámci třídy, školy nebo systému. |
| Nerespektující komunikace | NER | Učitel volí formu reakce skrze verbální komunikační bloky, např. vyhrožování, křik, oplácení chování, rozkaz... |
| (Kázeňské) Tresty | TRE | Učitel řeší situaci formou trestu, který není přímým důsledkem žákova chování. Příčina-následek není - trest nesouvisí přímo s chováním žáka. Učitel pojmenovává zásah jako trestající. |
| Důsledky | DUS | Žák/žákyně plní přirozené důsledky, které vyplývají z jeho chování. Učitel poskytl informaci, která seznamuje žáka s tím, že toto je důsledek, který se stane, když bude v nekázni pokračovat. (sociálně vyjednané) |
| Fyzické zakročení | FYZ | Učitel fyzicky reaguje na chování žáka. |
| Podpora | POD | Žák/žákyně dostává speciální formu individuální podpory, např. skrze asitenta nebo IVP. |

*Poznámka.* Přepsáno z interního kódovacího stromu první etapy (list Řešení situací).

**Poznámka ke kategorii Proaktivní řešení.** Ve verzi V1 byla „Proaktivní
řešení“ samostatnou kategorií s definicí (doslovně): „Učitel volí strategie,
kterými předchází dalšímu potenciálnímu náročnému chování žáků a které vrací
pozornost žáků směrem k výuce.“; ve verzi V2 byla přesunuta mezi podřazené
kódy a číselná řada kategorií po ní nese mezeru. Do klasifikačního promptu
jazykového modelu (příloha B) přesto vstoupila jako samostatná položka s vlastní
definicí, a proto ji model v korpusu přiřazuje (kapitola 6). V lidském kódování
první etapy ji jako samostatnou kategorii zaznamenala jediná anotátorka, u níž
se do výběrového seznamu řešení omylem dostala namísto kategorie „Fyzické
zakročení“; v korpusové deskriptivě (kapitola 5) ji proto mezi lidské kategorie
řešení nezařazujeme (kmenová sada řešení má 11
<!-- necislo: 11 kategorií V2; Proaktivní řešení jen jako kód predikovaný modelem, viz kap. 6 --> položek),
zatímco v porovnání s modelem (kapitola 6) ji ponecháváme jako kategorii predikovanou modelem.
V datech se ojediněle vyskytují i štítky mimo strom (například „humor“)
a překlepové varianty; deskriptivní analýzy je normalizují na kanonické
znění (kapitola 5).

```{=latex}
\needspace{12\baselineskip}
```

**Tabulka A.3.** Kategorie dopadu řešení (finální verze V2; definice doslovně).

| Kategorie | Kód | Definice |
|---|---|---|
| Neúspěch | NEU | Chování žáka nebo daná situace se nijak nezměnila. Nebo učitel použil k vyřešení situace neakceptovatelné a nevhodné způsoby (fyzické násilí, psychické násilí, nerespektující strategie) - ne v souladu s hodnotami chováním učitele. |
| Částečný úspěch | CU | Chování žáka nebo daná situace se změnila jen částečně. |
| Krátkodobý úspěch | KU | Situace se změnila pouze na krátkou dobu a poté se chování začalo opět opakovat. |
| Dlouhodobý úspěch | DU | Situaci se podařilo vyřešit v danou chvíli a chování/situace se již neopakovala. |

*Poznámka.* Přepsáno z interního kódovacího stromu první etapy (list Dopad řešení). Zdroj u kategorie Částečný úspěch nese překlep „Částěčný“; analýzy jej normalizují (kapitola 5).

Historické definice jsou zachovány doslovně. NEU však spojuje popsané
nezměněné chování s hodnotovým odmítnutím prostředku. Konečný štítek
neumožňuje určit, který z těchto důvodů rozhodl. Ani ve třetí etapě není
plochost pouze technickou neúplností: zahrnuje také eticky nepřijatelné
jednání. Tato konstrukční omezení zohledňují kapitoly 4, 5 a 8; chybějící
důvod kódu se nedoplňuje odhadem.

## A.2 Druhá etapa: manuál hodnocení kvality řešení

Manuál druhé etapy definuje pojmy tří bipolárních dimenzí, čtyři
rámce opřené o důkazy a škálové body. Anotátorky hodnotily každé řešení
(učitelské i generované, zaslepeně; kapitola 7) na čtyřech škálách
a označovaly rozpoznané rámce.

**Tabulka A.4.** Vymezení pólů bipolárních dimenzí (definice doslovně).

| Pojem | Definice |
|---|---|
| Reaktivní řešení | Okamžitá reakce na aktuální problém či konflikt ve třídě. Cílem je rychle obnovit řád a minimalizovat negativní dopady na průběh výuky. |
| Proaktivní řešení | Preventivní opatření a postupy, které předcházejí vzniku problémového chování či náročných situací. Učitel je plánuje a zavádí dopředu, aby žáky učil principy prosociálního chování a aby ve třídě vytvořil pozitivní prostředí a jasná pravidla. |
| Systémové řešení | Komplexní rámec, který platí pro celou třídu nebo školu. Přináší jasně definované zásady, postupy a jednotné přístupy ke zvládání chování, na nichž se podílí vedení, učitelé i žáci (využívá další aktéry jako školní psycholog, metodik prevence, školní programy, rodiče...) |
| Situační řešení | Okamžitá a flexibilní reakce v rámci konkrétní situace. Učitel volí postup podle aktuálních podmínek a potřeb žáků s cílem minimalizovat narušení výuky a vyřešit konflikt nebo nežádoucí chování na místě. |
| Humanisticky orientované | V centru pozornosti je žák (jeho potřeby, motivace, emoční stav). Učitel buduje vztah založený na empatii, respektu a sebereflexi. Učitel vědomě pěstuje respektující a empatický přístup, dává žákovi prostor vyjádřit se, vede ho k uvědomění si dopadu svého chování a společně s ním hledá možná řešení. |
| Behaviorálně orientované | Vychází z behaviorálních teorií učení, kde se posiluje žádoucí chování nebo potlačuje nežádoucí chování pomocí odměn (pochval, výhod) či trestů (sankcí). Řešení je jasně nastavené (učitel se rozhodnul a řešení nastavil), nebere ohledy na pocity/potřeby žáků, je direktivní směrem od učitele. |

*Poznámka.* Přepsáno z interního kódovacího manuálu druhé etapy (list Popis definic).

**Škály.** Celková vhodnost byla ve formuláři zadávána jako pětibodová
(1 – Zcela nevhodné, 2 – Spíše nevhodné, 3 – Vyvážené, 4 – Spíše vhodné,
5 – Zcela vhodné); v analyzovaném souboru je lineárně
překódována na −2 až +2 jako ostatní dimenze (kapitola 7). Tři bipolární
dimenze užívají pětibodovou škálu −2 až +2, jejíž krajní a střední body
zdroj definuje takto (výběr; plné znění všech bodů ve zdrojovém souboru):

```text
Reaktivní vs. Proaktivní
  -2 – Čistě reaktivní: „Řešení se zaměřuje výhradně na okamžitou reakci
       na vzniklý problém či konflikt, aniž by zahrnovalo preventivní
       opatření či dlouhodobou vizi."
   0 – Vyvážené: „Řešení kombinuje okamžitou reakci s preventivními kroky…"
  +2 – Čistě proaktivní: „Řešení je plně orientované na prevenci – učitel
       plánuje a zavádí opatření před vznikem problému…"

Systémové vs. Situační (konverzační)
  -2 – Plně systémové: „Řešení vychází z jednotného, jasně definovaného
       rámce a pravidel, platných pro celou třídu nebo školu…"
  +2 – Plně situační (konverzační): „Řešení je zcela situační a flexibilní,
       přizpůsobuje se okamžitým potřebám a podmínkám, aniž by se opíralo
       o přísně daný systém."

Humanisticky vs. Behaviorálně orientované
  -2 – Plně humanisticky orientované: „Řešení se zcela soustředí na
       individuální potřeby, motivaci a emoční stav žáků…"
  +2 – Plně behaviorálně orientované: „Řešení je zcela orientované na
       behaviorální techniky, využívá jasně definovaných odměn a sankcí…"
```

*Poznámka.* Přepsáno z interního kódovacího manuálu druhé etapy (list se škálami, aktuální znění). Orientace pólů (záporný pól = reaktivní/systémové/humanistické) odpovídá znaménkům výsledků v kapitole 7.

**Rámce.** Manuál definuje čtyři přístupy opřené o důkazy, které
anotátorky rozpoznávaly ve znění řešení: PBIS (pozitivní behaviorální
intervence a podpora; systémový přístup s jasnými pravidly, konzistentní
pozitivní zpětnou vazbou a předem určenými kroky při porušení pravidel),
SEL (sociálně-emoční učení; dlouhodobý rozvoj emočních a vztahových
dovedností, seberegulace a odpovědného rozhodování), NVC (nenásilná
komunikace; respektující dialog ve čtyřech krocích pozorování, pocity,
potřeby, prosba) a restorativní praxe (náprava škody a obnovení
vztahů namísto trestu). Plné znění definic s příklady z praxe uvádí list
„Popis definic“ zdrojového souboru; teoretické ukotvení rámců podává
kapitola 2.

## A.3 Třetí etapa: operacionalizace kvality kazuistik

Třetí etapa posuzovala kvalitu kazuistiky, dopad řešení a vhodnost řešení.
Nástroje byly definovány takto (definice doslovně):

**Tabulka A.5.** Kvalita kazuistiky (binární posouzení).

| Kategorie | Definice |
|---|---|
| Plochá (nepoužitelná) | Kazuistika neposkytuje dostatek informací pro pochopení situace ani pro interpretaci řešení. Nebo učitel použil k vyřešení situace neakceptovatelné a nevhodné způsoby (fyzické násilí, psychické násilí, vysoce nerespektující strategie) - ne v souladu s hodnotami chováním učitele a právy dítěte. |
| Použitelná (dostatečná - skvělá) | Kazuistika poskytuje dostatek informací pro základní pochopení situace a pro interpretaci řešení. |

*Poznámka.* Přepsáno z interního kódovacího manuálu třetí etapy; z definice kategorie Plochá byla vypuštěna editorská instrukce předlohy („+ PŘIDAT KOMENTÁŘ K PLOCHOSTI“). V anotačních datech je kladná kategorie zapisována štítkem „Plná“; kniha obě označení ztotožňuje a v próze i analýzách používá znění z dat (plná, plochá).

**Dopad řešení** je ve třetí etapě tříkategoriální: Neúspěch (NEU),
Krátkodobý/částečný úspěch (KU) a Dlouhodobý úspěch (DU). Oproti první
etapě jsou tedy kategorie Částečný a Krátkodobý úspěch sloučeny; dopady
z obou etap proto nelze přímo slučovat bez explicitního převodu
(kapitola 4). **Vhodnost řešení** je čtyřbodová bez středního bodu
(1 – Zcela nevhodné, 2 – Spíše nevhodné, 3 – Spíše vhodné, 4 – Zcela
vhodné); s pětibodovou vhodností druhé etapy se nesměšuje (kapitola 4).
Vedle kategorií anotátorky vyplňovaly tři textové komentáře (jazykový
komentář, komentář k plochosti s povinným zdůvodněním, další komentář).

**Postup etapy a pilotní shoda.** Zdrojový soubor dokumentuje zamýšlený
postup etapy a shodu z pilotáže na padesáti kazuistikách doslovně takto:

```text
Budeme kódovat takto:
- děláme zaškolení na 5-10 kazuistikách (jen vysvětlení pojmů, nácvik kódování)
- poté budou anotátorky kódovat 20 kazuistik. Projdeme společně každou z nich
  a nesrovnalosti vyjasníme a dle toho upravíme kódovací manuál (viz
  operacionalizace pojmů výše)
- poté budou anotátorky kódovat 50 kazuistik - spočte se shoda […]. Shoda
  vyšla ve všech případech nad 80%, někde i nad 90% […]
- kóduje se 1950 kazuistik, z toho 695 je překryv pro výpočet shody
- poté se opět spočte shoda […]
```

Shoda z pilotáže je ve zdroji zapsána slovensky, doslovně takto:

```text
1. Sloupec: Kvalita kazuistiky:
Zhoda: 97.96%
Cohen's kappa: nedefinovana: jedna z anotatoriek neoznacila ani jednu
kazuistiku za "plochu".
2. Sloupec: Dopad řešení:
Zhoda: 93.88%
Cohen's kappa: 0.8960
3. Sloupec: Vhodnost:
Zhoda: 89.80%
Cohen's kappa: 0.8131
```

*Poznámka.* Přepsáno z interního kódovacího manuálu třetí etapy. Výpustky vyznačeny […]; vypuštěny pouze zmínky o členech týmu (anonymizace). Jde o pilotní hodnoty z podkladu etapy; shodu na finálních datech uvádí Studie 4 (kapitola 8).

---
