

::: {.content-visible unless-format="pdf"}

| **MASARYKOVA UNIVERZITA**
| Pedagogická fakulta

| **Náročné chování žáků v době AI**
| Kazuistiky z praxe a jazykové modely v pedagogickém výzkumu

| **Habilitační práce**

| Brno 2026, Jan Nehyba

{{< pagebreak >}}

:::

# Prohlášení {.unnumbered}

Prohlašuji, že jsem habilitační práci vypracoval samostatně s využitím pouze
citované literatury, informací a zdrojů a že tato práce nebyla předložena
k udělení žádného předchozího titulu.

V Brně dne ………………………………

\vspace{3em}

\hfill ……….…………………………...\hspace{1.5em}

\hfill \textit{vlastnoruční podpis autora}\hspace{2.5em}

{{< pagebreak >}}

# Prohlášení o využití umělé inteligence {.unnumbered}

Při přípravě této práce autor využíval nástroje umělé inteligence (Claude,
Anthropic) k organizaci pracovních podkladů, ke kontrole pravopisu, typografie
a formátování textu a příloh, k práci s verzovaným repozitářem (Git/GitHub),
k propojování a kontrole konzistence částí rukopisu s analytickými výstupy
a k jazykovým úpravám a zapracování oprav podle autorových pokynů.
Použití jazykových modelů jako předmětu i nástroje
výzkumu je popsáno v metodologii. Po použití těchto nástrojů autor veškerý obsah
zkontroloval a upravil a nese za něj plnou odpovědnost.

{{< pagebreak >}}

# Abstrakt {.unnumbered}

Zvládání náročného chování žáků patří k nejtěžším stránkám učitelské
profese a zároveň k oblastem, kde příprava učitelů naráží na mezeru mezi
obecnými principy a jednáním v konkrétní situaci. Tato monografie na tuto
mezeru odpovídá dvojím způsobem. Pedagogicky: na korpusu projektu
Edustories, který čítá přes tři tisíce
<!-- necislo: přesné číslo řezu uvádí kap. 5 --> autentických kazuistik
psaných studujícími učitelství a učiteli, popisuje, jaké typy náročného chování,
řešení a dopadů česká školní praxe zaznamenává; v repertoáru řešení
dominuje rozhovor a další snadno dostupné, na incident reagující postupy.
Metodologicky: kriticky prověřuje velké jazykové modely jako výzkumný
nástroj pro analýzu takového korpusu. Kniha dokládá, že model kóduje typy
řešení ve shodě s vyškolenými anotátorkami na úrovni Cohenova κ = 0,64,
<!-- manifest kap6_kodovani_cisla: kappa_llm_clovek=0.6445 -->.
Po dodatečném vyloučení překryvů s příklady činí κ = 0,61;
<!-- manifest kap6_kodovani_cisla: bez_prekryvu_kappa=0.6143 --> nejde o nový
nezávislý test. V
zaslepeném experimentu na 324
<!-- manifest kap7_k2_shoda_cisla: n_kazuistik=324 --> dvojicích řešení
ukazuje, že řešení generovaná modelem hodnotily anotátorky jako vhodnější
a proaktivnější než autentická řešení učitelů, jež byla reaktivnější
a behaviorálnější. Čtvrtá studie na dvojitě posouzeném překryvu 693
<!-- manifest kap8_kvalita_cisla: n_prekryv=693 --> kazuistik ukazuje, že
posouzení použitelnosti kazuistiky má vysokou vzájemnou shodu (κ = 0,77),
<!-- manifest kap8_kvalita_cisla: shoda_kvalita_kappa=0.7689 --> posouzení
dopadu řešení spolehlivé (κ = 0,69)
<!-- manifest kap8_kvalita_cisla: shoda_dopad_kappa=0.6875 --> a posouzení
vhodnosti shodné jen středně. Opakované posouzení dopadu týchž textů
jednou pozdější anotátorkou se shoduje s dřívějšími kódy (κ = 0,59)
<!-- manifest kap8_kvalita_cisla: k1k3_dopad_kappa=0.588 --> a vztahová
a kolektivní řešení se v korpusu pojí s vyšším podílem dlouhodobého úspěchu
než řešení represivní. Historické kategorie však částečně zahrnují
normativní úsudek, a nejsou nezávislým měřením účinnosti. Úspěšnost řešení dokáže jazykový model z textu kazuistiky
předvídat jen slabě (vyvážená přesnost 60 %
<!-- manifest kap8_predikce_cisla: predikce_kimi_k3_zero_shot_konsenzus_bal_acc=0.6002 -->
proti 80 %
<!-- manifest kap8_predikce_cisla: predikce_clovek_clovek_bal_acc=0.802 --> u shody
dvou posuzovatelek, které popis výsledku četly). Jde o jinou úlohu,
nikoli o lidský strop predikce. Hlavní statistické analýzy jsou
reprodukovatelné: kód, podkladové tabulky a hotové reporty zpřístupňuje
doprovodný repozitář. Kniha tak přináší trojí příspěvek: empirický obraz
repertoárů řešení náročného chování, metodologicky ukázněný postup pro
nasazení jazykových modelů v pedagogickém výzkumu a otevřeně dokumentovaný
postup, který obojí umožňuje ověřit.

*Klíčová slova:* náročné chování žáků, kazuistiky, řízení třídy,
velké jazykové modely, model v roli anotátora, spolehlivost anotací,
reprodukovatelnost, učitelské vzdělávání.

{{< pagebreak >}}

# Abstract {.unnumbered}

Managing challenging student behaviour is among the hardest parts of
teaching, and teacher education struggles to bridge the gap between
general principles and situated action. This monograph answers in two
registers. Pedagogically, drawing on the Edustories corpus of more than
three thousand <!-- necislo: přesné číslo řezu uvádí kap. 5 --> authentic
case studies written by pre-service and in-service teachers, it maps the types of
challenging behaviour, responses, and outcomes recorded in Czech school
practice; the response repertoire is dominated by conversation and other
readily available, incident-driven strategies. Methodologically, it puts
large language models under critical scrutiny as research instruments for
such a corpus. The book shows that a model codes response types in
agreement with trained human annotators at Cohen's κ = 0.64,
<!-- manifest kap6_kodovani_cisla: kappa_llm_clovek=0.6445 -->.
After retrospectively excluding detected overlaps with prompt examples,
κ is 0.61; <!-- manifest kap6_kodovani_cisla: bez_prekryvu_kappa=0.6143 -->
this is not a new independent test. In
a blinded experiment on 324
<!-- manifest kap7_k2_shoda_cisla: n_kazuistik=324 --> solution pairs it
demonstrates that model-generated solutions were rated as more appropriate
and more proactive than teachers' authentic solutions, which were more
reactive and behaviourally oriented. On a doubly rated overlap of 693
<!-- manifest kap8_kvalita_cisla: n_prekryv=693 --> case studies, the fourth
study shows high inter-rater agreement in judging case usability
(κ = 0.77), <!-- manifest kap8_kvalita_cisla: shoda_kvalita_kappa=0.7689 -->
judging the outcome of a solution is reliable (κ = 0.69)
<!-- manifest kap8_kvalita_cisla: shoda_dopad_kappa=0.6875 --> and judging its
appropriateness reaches only moderate agreement. Earlier outcome codes
agree with one later annotator reading the same texts (κ = 0.59),
<!-- manifest kap8_kvalita_cisla: k1k3_dopad_kappa=0.588 --> and relational
and class-level solutions are associated with a higher share of long-term
success than punitive ones. Historical categories partly incorporate
normative judgments and do not independently measure effectiveness.
A language model predicts the success of a solution from
the case text only weakly (balanced accuracy 60 %
<!-- manifest kap8_predikce_cisla: predikce_kimi_k3_zero_shot_konsenzus_bal_acc=0.6002 -->
against 80 %
<!-- manifest kap8_predikce_cisla: predikce_clovek_clovek_bal_acc=0.802 --> for the
agreement of two human raters who read the reported outcome). This is a
different task, not a human prediction ceiling. The main statistical
analyses are reproducible: the
companion repository provides the code, source tables and rendered analysis
reports. The contribution is threefold: an empirical picture of teachers'
response repertoires, a disciplined methodology for deploying language
models in educational research, and an openly documented procedure that
allows both to be verified.

*Keywords:* challenging student behaviour, case studies, classroom
management, large language models, LLM-as-annotator, annotation
reliability, reproducibility, teacher education.

{{< pagebreak >}}

# Poděkování {.unnumbered}

Kniha vznikla v rámci projektu TA ČR TQ01000030.
<!-- necislo: identifikátor projektu --> Děkuji anotátorkám výzkumného
týmu Edustories, jejichž pečlivá práce tvoří páteř všech tří anotačních
etap (v knize vystupují pod pseudonymy, protože anonymizaci uplatňujeme důsledně
i tam, kde by poděkování bylo zaslouženě jmenovité), Michalu Štefánikovi
za dlouholetou spolupráci na výpočetní straně projektu a všem studujícím
učitelství, kteří své zkušenosti proměnili v kazuistiky.


# Poznámka k publikacím {.unnumbered}

Tato monografie je původní vědeckou prací napsanou pro toto habilitační řízení:
uceleným a samostatným zpracováním nad daty projektu Edustories, nikoli souborem
převzatých článků. Není totožná s žádnou disertační ani jinou kvalifikační prací,
kterou autor dříve předložil k získání akademického titulu, a žádnou takovou
nereprodukuje. Přehled dřívějších publikovaných výstupů autora, s nimiž práce tematicky souvisí,
uvádí dokumentace habilitačního řízení.

---
