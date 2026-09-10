# 10. Závěr


Kniha vyšla z jednoduché otázky: co vypovídají kazuistiky náročného chování
o tom, jak čeští učitelé takové chování zvládají, a nakolik lze jejich
výzkum ve velkém rozsahu svěřit jazykovému modelu. Odpověď hledala ve
čtyřech studiích nad jedním korpusem projektu Edustories. Tato kapitola
shrnuje odpovědi na čtyři výzkumné otázky, pojmenovává přínos knihy
a naznačuje, kam práce směřuje.

## 10.1 Odpovědi na výzkumné otázky

Na první otázku, jak vybudovat a popsat rozsáhlý korpus autentických
kazuistik a co zachycuje, odpovídá Studie 1. Korpus vznikl na platformě
projektu zrcadlovou šablonou, která od pisatelů žádá úspěšně i neúspěšně
řešenou situaci, prošel strukturací, anonymizací a redakční kontrolou
a jeho zveřejněný řez z května 2026 čítá 3 202
<!-- manifest kap5_korpus_cisla: n_korpus_s6=3202 --> kazuistik. Kazuistiky
zachycují celé spektrum náročného chování od narušování výuky po šikanu
a sebedestruktivní chování a repertoár řešení, v němž dominuje rozhovor
a další reaktivní kroky; vztahová a kolektivní řešení se v nich pojí
s příznivějším vnímaným výsledkem než řešení represivní. Korpus je
zároveň časovou řadou řezů, a každé číslo knihy proto platí pro svůj
datovaný řez.

Na druhou otázku, nakolik se jazykový model shodne s vyškolenými lidmi
při deduktivní klasifikaci obsahu, odpovídá Studie 2. Na úplných dvojicích
dosáhla shoda s lidským kódem typu řešení κ = 0,64
<!-- manifest kap6_kodovani_cisla: kappa_llm_clovek=0.6445 -->.
Po dodatečném vyloučení zjištěných překryvů s příklady činí κ = 0,61
<!-- manifest kap6_kodovani_cisla: bez_prekryvu_kappa=0.6143 -->.
Jde o retrospektivní kontrolu, ne o nový nezávislý test. Rozdíl oproti
lidskému α na jiném vzorku nedokládá dosažení lidského stropu.
Modelové kategorie proto vyžadují průběžnou kontrolu a nenahrazují
lidský úsudek nad jednotlivým případem.

Na třetí otázku, jak se liší řešení generovaná modelem od autentických
řešení učitelů, odpovídá Studie 3 zaslepeným hodnocením 324
<!-- manifest kap7_k2_shoda_cisla: n_kazuistik=324 --> dvojic řešení. Učitelská
řešení byla hodnocena jako méně vhodná (rozdíl −0,85
<!-- manifest kap7_k2_shoda_cisla: lmm_b1_ucitel_vhodnost=-0.8547 --> bodu
škály), jako reaktivnější a behaviorálnější, a měla zhruba třetinovou šanci,
že v nich anotátorky rozpoznají některý z přístupů opřených o důkazy.
Výsledek platí pro textovou podobu řešení, pro jediný model a jedinou
instrukci; nedokládá, že „AI radí lépe než učitel“, ale že generované řešení
může nabídnout kontrast k zaznamenanému postupu. Úplný repertoár ani
znalosti jednotlivých učitelů studie neměřila.

Na čtvrtou otázku odpovídá Studie 4. Na dvojitě posouzeném překryvu 693
<!-- manifest kap8_kvalita_cisla: n_prekryv=693 --> kazuistik rozlišuje
použitelnost textu, popsaný dopad a vhodnost řešení. Po vyloučení
projednaných případů vykazuje použitelnost vysokou vzájemnou shodu;
bez vnějšího kritéria však nelze určit správnost posouzení. U dopadu
činí κ = 0,69 <!-- manifest kap8_kvalita_cisla: shoda_dopad_kappa=0.6875 -->,
u vhodnosti je shoda nižší. Porovnání dřívějších hodnocení s jednou
pozdější anotátorkou dosahuje κ = 0,59
<!-- manifest kap8_kvalita_cisla: k1k3_dopad_kappa=0.588 -->;
nejde o externí replikaci dvěma týmy. Rozdíly mezi částmi etapy časově
souvisejí s rekalibrací, ale její samostatný účinek nelze oddělit od
zácviku a změny posuzovaných případů.

Při předpovědi dopadu bez jeho popisu dosahuje model Kimi vyvážené
přesnosti 60 %
<!-- manifest kap8_predikce_cisla: predikce_kimi_k3_zero_shot_konsenzus_bal_acc=0.6002 -->.
Párové intervaly rozdílů modelů i variant s příklady zahrnují nulový
rozdíl. Výsledek nedokládá jejich ekvivalenci ani informační strop úlohy.
Lidská shoda při čtení popisu výsledku je kontextová reference, nikoli
srovnatelná predikční úloha.

## 10.2 Přínos knihy

Přínos knihy je trojí. Empirický: kniha popisuje učitelské postupy
zaznamenané v rozsáhlém souboru autentických českých situací. Převahu
snadno dostupných reakcí označuje interpretačním pojmem repertoár
nejmenšího odporu. Neměří však znalosti učitelů ani příčiny volby postupů.
Souvislosti s kódovaným úspěchem se týkají historických anotačních
kategorií, které částečně zahrnují i normativní posouzení přijatelnosti.
Nejsou nezávislým důkazem účinnosti strategií.

Metodologický: kniha prověřila jazykový model ve třech rolích na jednom
reálném korpusu v jazyce mimo angličtinu a v každé roli jej poměřila
lidským měřítkem s měřenou reliabilitou. Z toho odvodila rozdělení rolí,
které lze převzít: klasifikace obsahu na úrovni kategorií po validaci na
vlastních datech, generování kontrastních řešení pro reflexi, žádné
posuzování vhodnosti bez lidské reference. A doložila, že spolehlivost
lidského posouzení je proměnná, kterou je třeba měřit, vykazovat
z finálních dat, chránit před paradoxem shody a doprovázet přiznáním
každého zásahu do protokolu.

Infrastrukturní: kniha zanechává korpus s datovanými řezy, tři anotační
etapy s dokumentovanými schématy a maticí pokrytí, a doprovodný
repozitář, v němž jsou analýzy, tabulky výsledných hodnot, skripty obrázků
a odvozená data bez textů kazuistik a bez osobních údajů. Hlavní statistické výsledky lze přepočítat z odvozených dat a uložených
predikcí bez nového volání modelu. Historické souhrny a dokumentační
údaje jsou označené vstupy; bez neveřejných textů nelze nezávisle zopakovat
původní anotaci, tvorbu příkladů ani kontrolu anonymizace. Pro český pedagogický výzkum je to
zároveň první doklad, že jazykový model může být kriticky prověřeným
nástrojem analýzy velkého korpusu autentického českého textu.

## 10.3 Směřování

Práce pokračuje třemi směry, které kniha připravila. Intervenční studie
prověří, zda generované kontrastní řešení nad vlastní situací repertoár
učitelů skutečně rozšiřuje; platforma Edustories pro ni poskytuje
materiál, měřicí nástroj i očekávanou velikost mezery. Příští anotační
etapa dostane časový záznam hodnocení, kontrolní body a označené přepisy,
aby bylo možné vývoj spolehlivosti sledovat přesně. A opakování Studie 2
a predikčního experimentu s dalšími modely i poskytovateli, spolu
s anglickou datovou sadou Edustories-en, ukáže, nakolik jsou výsledky
vlastností úlohy a nakolik vlastností jednoho modelu a jednoho jazyka.

Kniha tak nekončí tvrzením, že jazykové modely pedagogický výzkum promění.
Ukazuje možnosti jejich kontrolovaného použití i hranice dosavadních
ověření. Praktická doporučení rozlišují shodu, správnost, predikci a
pedagogickou účinnost. Pro další použití je podstatné tuto odlišnost
zachovat, nikoli hledat jediný koeficient vyjadřující univerzální hranici.

---
