# Příloha B. Prompty jazykových modelů


Tato příloha dokládá doslovné znění promptů, jimiž jazykové modely
vstupovaly do vzniku a analýzy dat knihy. Prompty jsou citovány přesně
tak, jak běžely (včetně stylistických nedokonalostí originálu), protože
doslovnost je podmínkou reprodukovatelnosti. U každého promptu je uveden
model, parametry a zdrojový soubor v archivu projektu. Příloha obsahuje
pouze prompty, jejichž znění je v archivu doloženo; co doloženo není, je
označeno výslovně.

**Tabulka B.1.** Přehled dokladovaných promptů.

| Krok zpracování | Model | Zdroj znění | Oddíl |
|---|---|---|---|
| Extrakce a strukturace kazuistik | gpt-4o (Batch API; dříve gpt-4-1106-preview) | interní extrakční notebook projektu | B.1 |
| Anonymizace (třetí stupeň) | součást promptu extrakce | tamtéž | B.2 |
| Klasifikace řešení (model v roli anotátora) | gpt-4o, finální běh | interní klasifikační notebook projektu | B.3 |
| Generace srovnávacího řešení (druhá etapa) | gpt-4o | rukopis článku o srovnání řešení a návrh studie | B.4 |
| Rámcovaná řešení platformy | (produkční kód platformy) | v archivu nedoloženo | B.5 |

## B.1 Extrakce a strukturace kazuistik

Odevzdané texty dělí do čtyř sekcí strukturační prompt, který zároveň
provádí třetí stupeň anonymizace (oddíl B.2). Finální běh: gpt-4o přes
Batch API, teplota nula; totéž znění běželo dříve na modelu
gpt-4-1106-preview s pojistkou opakování (tři pokusy, práh délky výstupu,
mírné zvýšení teploty). Vstupem je text po strojové anonymizaci
(sloupec anonymized_content).

```text
System:
- Jsi expert na univerzitě, který má za úkol detailně přepsat slovo od
  slova a následně upravit texty (kazuistiky) popisující problémové
  chování žáků na škole.
- Uživatel (User) ti poskytne celý text kazuistiky.

User:
- Doslovně transkribuj tento vstupní text “““{text}””” kazuistiky tak,
  aby odpovídal původnímu obsahu co nejpřesněji, a poté tento text rozděl
  do čtyř specifických sekcí podle následujících kritérií:
  - V sekci 'description' umísti text od začátku 'Podrobného popisu
    (vzniku) situace' až do 'Anamnéza'.
  - V sekci 'anamnesis' umísti text od 'Anamnéza' až do 'popis řešení'.
  - V sekci 'solution' umísti text popisující řešení situace, začínající
    od 'popis řešení' až do 'Výsledek'.
  - V sekci 'outcome' umísti text popisující dlouhodobý výsledek od
    'Výsledek' až do konce narativního popisu situace.
- Pokud vstupní text kazuistiky neobsahuje rozdělení na Podrobný popis
  (vzniku) situace, Anamnéza a podobně, pak veškerý vstupní text pouze
  rozděl podle svého nejlepšího uvážení do jednotlivých sekcí.
- V sekcích odstraň úvodní zadání jako: "Podrobný popis (vzniku) situace
  na úrovni chování", "Anamnéza žáka/žáků nebo třídy (max. 2 normostrany,
  chronologicky)", "Podrobný popis řešení problematického chování",
  "Výsledek řešení (krátkodobě-jak to probíhalo hned po incidentu
  a dlouhodobě-zda se to nějak odrazilo v dalších hodinách,
  chronologicky, max. 2 normostrany)".
- Každou sekci začni smysluplným slovem, kterým obvykle začínají věty
  v českém jazyce, například jako "Žák", "Učitel", "Žáci", "Situace"
  a podobně.
- Ve výstupu v sekcích použij maximum doslovných citací ze vstupního
  textu kazuistiky.
- Zkontroluj, že jsi transkriboval (transcribe) veškerý vstupní text
  kazuistiky, pokud ne, tak jej doplň o chybějící části textu.
- Celkově by měly mít všechny sekce dohromady stejný počet tokenů jako
  vstupní text kazuistiky.
- Svůj výstup poskytni v tomto formátu: (“description”:“”, “anamnesis”:
  “”, “solution”: “”, “outcome”: “”), každá sekce je na novém řádku.
- Z výstupu a citací odstraň pouze všechna jména, příjmení.
- Z výstupu a citací odstraň pouze zkratky jmen a příjmení (například
  jako: H., J., K., P., M., M.B., a podobně), tak aby text byl stále
  smysluplný popis situace.
- [ANONYMIZED] často označuje nějaké jméno nebo příjmení nebo město,
  ulici, nahraď tuto frázi obecným slovem jako například osobní zájmeno
  nebo žák, žačka a podobně.
- Ve výstupu nesmí být nikde fráze [ANONYMIZED] a fráze "Do jaké míry".
- Při řešení úkolu postupuj krok za krokem.
- Když se budeš držet těchto instrukcí, tak budeš pochválený a dostaneš
  nepředstavitelnou odměnu.
```

*Poznámka.* Přepsáno z interního extrakčního notebooku projektu (finální aktivní buňka; starší, obsahově shodné znění pro gpt-4-1106-preview tamtéž, liší se pouze typografií uvozovek a jedním nadbytečným uvozovacím znakem). Prototypy strukturace z podzimu 2023 (GPT-4) dokládá starší interní notebook; kniha jej necituje jako produkční nástroj.

## B.2 Anonymizace v promptu

Úplný třístupňový anonymizační protokol i schválení etickou komisí uvádí
příloha D.2; zde dokládáme jen jeho část, která se týká promptů. Druhý
stupeň není prompt, nýbrž kód: rozpoznávání pojmenovaných entit službou
NameTag (REST API ÚFAL, model Czech Named Entity Corpus 2.0) nahrazuje
entity typů osobních jmen, příjmení, měst, ulic a dalších (typy „pf“, „pp“,
„pc“, „gc“, „pm“, „ps“, „gs“, „gu“) řetězcem [ANONYMIZED]. Třetí stupeň je
vestavěn přímo do strukturačního promptu (B.1): jazykový model odstraní
jména a jejich zkratky a nahradí zbylé značky [ANONYMIZED] obecnými výrazy.

## B.3 Klasifikace řešení jazykovým modelem (model v roli anotátora)

Deduktivní klasifikaci typů řešení (Studie 2) provedl model gpt-4o
(teplota nula, průběžné ukládání; finální kompletní běh je archivován). Vstupem bylo pouze znění řešení; prompt obsahuje
definice kategorií kódovací knihy (příloha A) a několik doslovných
příkladů ke každé kategorii (few-shot). Srovnávací soubor s lidským
kódováním čítá 334
<!-- manifest kap6_kodovani_cisla: n_archivnich_radku=334 --> párů
a pracuje s 12
<!-- manifest kap6_kodovani_cisla: n_kategorii_reseni_srovnani=12 -->
kategoriemi (kapitola 6).

```text
System:
- Jsi expert na klasifikaci textu.
- Uživatel (User) ti poskytne popis navrženého řešení kazuistiky
  o náročném chování žáků.
- Tvým úkolem je přesně klasifikovat řešení kazuistiky podle
  předdefinovaných kategorií, které poskytne uživatel.

User:
- Analyzuj situaci krok za krokem (Let's Think Step by Step).
- Analyzuj podrobně řešení nevhodného chování žáka, žáků: ###{solution}###
  a přiřaď nejlepší možnou následující kategorii k řešení z kazuistiky.
- K přiřazování použij pouze tyto kategorie:
  • Rozhovor: Řešení chování pouze pomocí rozhovoru s různými účastníky
    (žák, rodiče, třída, učitelé, vedení školy).
  • Dohoda: Dohoda nebo kompromis mezi učitelem a žákem/třídou na
    společně přijatelném řešení.
  • Proaktivní řešení: Strategie učitele zaměřené na předcházení
    náročnému chování a zaměření pozornosti žáků na výuku.
  • Práce s kolektivem: Podpora vztahů ve třídě jako prostředek k řešení
    situace a prevenci dalších problémů.
  • Spolupráce s odborníky: Učitel vyhledává pomoc mezi odborníky
    (ve škole i mimo školu) při řešení situací (např. speciální pedagog,
    psycholog, policie).
  • Upozornění: Učitel verbálně upozorňuje žáka na jeho rušivé chování.
  • Přemístění žáka: Řešení problému přemístěním žáka v rámci třídy,
    školy nebo systému (např. diagnostický ústav, psychiatrická léčebna).
  • Nerespektující komunikace: Učitel reaguje pouze skrze komunikační
    bloky jako je křik, vyhrožování nebo oplácení chování.
  • (Kázeňské) Tresty: Učitel uvaluje tresty, které nejsou přímým
    důsledkem chování žáka (např. práce navíc, domácí úkoly).
  • Důsledky: Přirozené důsledky vyplývající z chování žáka, o kterých
    je informován (např. opakování ročníku, poznámka, snížená známka
    z chování).
  • Fyzické zakročení: Učitel fyzicky reaguje na chování žáka
    (např. facka, znehybnění).
  • Podpora: Individuální podpora žáka zaměřená na jeho motivaci,
    klidnění nebo zlepšení výkonu (např. odměny, pochvaly, doučování,
    IVP, asistent).
- Klasifikuj řešení pouze podle uvedených kategorií, jiné kategorie
  nejsou povoleny.
- Zkontroluj, zda jsi identifikoval hlavní kategorii řešení správně,
  pokud ne, tak ji oprav.
- Zkontroluj, zda má řešení kazuistiky ###{solution}### odpovídat více
  kategoriím, a pokud ano, tak zdůvodni proč a dopiš další návrhy
  kategorií.
- ### Zde jsou Few-Shot Examples pro zlepšení identifikace jednotlivých
  kategorií: [doslovné příklady řešení ke každé kategorii; plné znění
  v archivu projektu]
- Dodržuj tento formát výstupu:
  • Hlavní kategorie řešení: (uveď pouze label kategorie)
  • Zdůvodnění:
  • Zhodnocení, zda k řešení patří další kategorie:
  • Případně navrhni další kategorie a odděl je čárkou:
  • Zdůvodnění ostatních kategorií:
  • Ověření:
```

*Poznámka.* Přepsáno z interního klasifikačního notebooku první etapy (sekce „Automatická klasifikace řešení“, few-shot varianta). Výstupní formát je doslovně doložen v archivovaném výstupu finálního běhu; z něj se přebírá hlavní kategorie pro srovnání s lidmi (kapitola 6). Notebook obsahuje i pilotované varianty téhož úkolu (bez few-shot příkladů; s kontextem popisu situace; „LLM as Judge“) a obdobný prompt pro klasifikaci dopadů; ty nejsou zdrojem výsledků knihy.

Dodatečná kontrola odhalila překryv celých řešení mezi příklady
archivovaného klasifikačního promptu a srovnávacím souborem Studie 2.
Přesné požadavky jednotlivých historických volání nejsou dochovány.
Kapitola 6 proto odděluje původní srovnání od retrospektivní analýzy bez
zjištěných překryvů; veřejné příznaky překryvu neobsahují texty případů.

## B.4 Generace srovnávacího řešení pro druhou etapu

Ke každé kazuistice druhé etapy bylo modelem gpt-4o vygenerováno
alternativní řešení s vynucenou paritou délky, gramatického rodu
a minulého času (kapitola 7). Publikované znění promptu (v rukopise AIED
anglicky) je toto:

```text
System:
- You are an expert on inappropriate and challenging student behavior
  and an expert in classroom behavior management.
- The user will provide a detailed description of a problem involving
  a student's (or students') challenging behavior; based on the case
  study and the student's developmental/educational history, you will
  propose the best possible behavior-management techniques.

User:
- Task: Based on the following problem description, produce a detailed
  account of the resolution of the problematic behavior.
- Write in the first person, chronologically, and you may include some
  key lines of dialogue with the student and concrete activities that
  took place during the resolution.
- Write the output as a single continuous paragraph and preserve as much
  of the original stylistic tone of the problem description as possible.
  The solution must address the specific situation.
- Begin directly with the description of the solution; do not begin with
  a phrase such as "In this situation, I...".
- Avoid using technical terms from the "Task:" section.
- Write the entire text in the past tense and maintain the grammatical
  gender implied by the problem description.
- Child's age: {row["year"]} years.
- Length: approximately {row["length"]} sentences, {row["length_char"]}
  characters.
###
Here is the problem description: {row['description_cs']}
###
Output:
```

*Poznámka.* Přepsáno z rukopisu souvisejícího článku o srovnání učitelských a generovaných řešení (příloha B, Generation Prompt).

Starší česká pracovní verze téhož zadání (s ukázkovými zástupnými
hodnotami) je doložena v návrhu designu studie:

```text
Zadání: Na základě následujícího popisu problému s náročným chováním
žáka zformuluj velmi praktické, co nejvíce pedagogicky a didakticky
vhodné řešení z pohledu efektivního classroom managementu. Řešení napiš
v jednom uceleném odstavci a zachovej co nejvíce původní styl
(stylistiku) z popisu problému. Jen pokud je to opravdu vhodné, tak
použij pro řešení přímou řeč. Uveď konkrétní rady a postupy, které budou
ihned použitelné v každodenní praxi. Tyto nejlepší možné rady a postupy
vychází z kontextu popisu problému. ###
- Začínej vygenerované řešení rovnou popisovaným řešením.
- Nepoužívej ve vygenerovaném řešení žádná odborná slova ze "Zadání:"
- Napiš řešení v minulém gramatickém čase celé řešení.
- A zohledni gender, který vyplývá z popisu problému.
- Věk dítěte: 9 let.
- Navržené řešení bude mít ideálně kolem 168 slov.
###
Zde je popis problému: {text}

Výstup:
```

*Poznámka.* Přepsáno z interního designového dokumentu druhé anotační etapy (pracovní verze; hodnoty věku a délky jsou ukázkové zástupné údaje). Přípravnou generaci deseti a poté patnácti řešení v červnu 2025 dokládají archivované výstupy přípravných běhů. <!-- necislo: registr událostí, příloha C a DATA_README -->

## B.5 Rámcovaná řešení platformy Edustories

Platforma nabízí u kazuistik šest generovaných řešení v pojmenovaných
rámcích (kapitola 3): proaktivní přístup, reaktivní přístup,
sociálně-emoční učení, pozitivní behaviorální podpora, restorativní
praxe a nenásilná komunikace. Existenci šesti rámců dokládají exportní
sloupce datového modelu platformy (ai_solution_proactive,
ai_solution_reactive, ai_solution_social_emotional_learning,
ai_solution_pbis, ai_solution_restorative_justice,
ai_solution_nonviolent_communication). Produkční prompty těchto generací
jsou součástí kódu platformy a v archivu knihy doloženy nejsou;
rané prototypy rámcované generace z podzimu 2023
dokumentuje interní prototypový notebook a kniha je za produkční znění
nevydává. Srovnávací řešení Studie 3 (oddíl B.4) s těmito šesti
rámcovanými řešeními nesouvisí (kapitola 7).

## B.6 Predikce dopadu řešení (model v roli prediktora)

Predikční experiment Studie 4 (oddíl 8.6) dával modelu popis situace,
anamnézu a řešení a žádal odhad dopadu podle definic třetí etapy (příloha A.3).
Pole výstupu se záměrně nevkládalo. Historický test hledal doslovných
prvních šedesát znaků výstupu, rozlišoval velikost písmen a kratší výstupy
automaticky propouštěl. Dvě kazuistiky s posunutými sloupci byly vyřazeny.
Test nevylučoval parafráze, jiné části výstupu ani významové nápovědy;
jeho tehdejší výsledek se přebírá jako historický údaj, nikoli jako nově
provedená úplná kontrola úniku. Běh
probíhal na jazykových modelech nasazených v národní akademické
infrastruktuře e-INFRA CZ (rozhraní kompatibilní s OpenAI, teplota nula).
Systémová instrukce zněla doslova takto:

```text
Jsi zkušená posuzovatelka pedagogických kazuistik. Dostaneš popis situace
ve škole, anamnézu žáka a popis toho, jak učitel situaci řešil.
Popis výsledku k dispozici nemáš; tvým úkolem je odhadnout,
jak řešení podle všeho dopadlo.

Vyber právě jednu z těchto tří možností:
NEU = neúspěch: problém trvá dál nebo se zhoršil, řešení nepomohlo.
KU = krátkodobý nebo částečný úspěch: situace se zklidnila
jen na čas nebo jen zčásti.
DU = dlouhodobý úspěch: problém se podařilo vyřešit a změna vydržela.

Odpověz jediným slovem: NEU, KU, nebo DU.
```

Uživatelská zpráva měla vždy týž tvar: `POPIS SITUACE:`, `ANAMNÉZA:`
a `ŘEŠENÍ:`, každý oddíl s doslovným zněním příslušné části kazuistiky.
V doplňkové variantě předcházelo šest příkladů z kazuistik mimo hodnocenou
množinu, uvedených jako dvojice zpráva uživatele a odpověď modelu.

*Poznámka.* Prompt v této podobě je součástí skriptu predikčního experimentu
v doprovodném repozitáři; zalomení dlouhého řádku je pouze typografické.
Otisk kontrolní odpovědi není důkazem totožnosti nasazení. Historická
cache mohla znovu použít stejnou odpověď; nynější skript kontrolní dotaz
necachuje a odděluje běhy. Tato úprava nedokládá zpětně verzi vah.

---
