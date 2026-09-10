# 6. Studie 2: Jazykový model jako anotátor


Druhá studie se ptá, zda velký jazykový model dokáže kódovat obsah
kazuistik tak, aby se shodl s vyškolenými lidskými anotátorkami (VO2).
Shodu dokládá pro dimenzi typu řešení, tedy nejjemnější a nejbohatší část
schématu; kódování chování a dopadu modelem neověřuje. Postupuje od
kódovacího schématu a shody mezi lidmi (6.2, 6.3) ke shodě modelu s lidmi,
souhrnně, po kategoriích i na úrovni jednotlivých záměn (6.4),
a ke kvalitativnímu pohledu na neshody (6.5).

## 6.1 Východiska

Kapitola 5 ukázala, co kazuistiky obsahují, na řezu, který bylo možné ručně
okódovat. Ruční kódování je však úzké hrdlo: rostoucí korpus (kapitola 3)
brzy přeroste kapacitu, kterou lidští anotátoři unesou. Přirozenou úvahou je
proto použít jazykový model jako anotátor, který týmž kódovacím schématem
zpracuje libovolně velký objem textu. Taková úvaha ovšem stojí a padá
s doložením, že se model s lidmi shoduje. Studie 2 proto srovnává lidské
kódování s modelovým na sdíleném vzorku kazuistik. Že se srovnání opírá
právě o dimenzi typu řešení, není náhoda: je to dimenze s nejjemnějšími
a nejvíce se překrývajícími hranicemi mezi kategoriemi a, jak ukáže oddíl 6.3,
také s nejnižší shodou mezi lidmi. Pokud model obstojí zde, obstojí
pravděpodobně i na hrubších dimenzích; opačný závěr z hrubší dimenze by
neplatil. Zároveň jde o dimenzi, na níž stojí ústřední pedagogické čtení
knihy, repertoáry řešení, takže právě u ní je doložená spolehlivost
nejcennější.

## 6.2 Metoda

### Kódovací schéma a lidské kódování

Ve finálním kole první anotační
etapy (kapitola 3) kódovalo pět vyškolených anotátorek kazuistiky do tří
dimenzí: typ náročného chování, typ řešení a dopad řešení. Schéma vzniklo induktivně otevřeným
kódováním na části korpusu a bylo zpřesněno do kódovacího stromu (příloha A).
Finální anotování probíhalo jako dělba práce: každá anotátorka kódovala jiné
kazuistiky, aby se pokryl co největší rozsah korpusu, s vestavěným překryvem
sloužícím ke kontrole shody. Údaje o spolehlivosti proto počítáme na tomto
překryvu, deskriptivní frekvence uvádí Studie 1.
U typu chování vstupuje do výpočtu třináct behaviorálních kategorií;
kontextová položka původního stromu, která pouze zaznamenávala přítomnost
diagnózy žáka, je stejně jako v deskriptivě Studie 1 vyřazena (oddíl 5.3
a příloha A).

### Modelové kódování a srovnávací vzorek

Nad týmž korpusem provedl jazykový model deduktivní klasifikaci řešení
podle stejného schématu. Pro srovnání lidského a modelového kódování
slouží archivní soubor 334
<!-- manifest kap6_kodovani_cisla: n_archivnich_radku=334 --> řádků.
Jeden neobsahuje lidský štítek; hlavní přepočet proto zahrnuje 333
<!-- manifest kap6_kodovani_cisla: n_paru_llm_clovek=333 --> úplných dvojic.
Prázdný štítek nepovažujeme za další kategorii řešení. Že oba sloupce nesou to, co mají, bylo
ověřeno proti anotační matici korpusu: lidský sloupec se s ní shoduje v 99 %
<!-- manifest kap6_kodovani_cisla: overeni_solutions_je_clovek=0.994 -->
případů, zatímco modelový jen v 72 %;
<!-- manifest kap6_kodovani_cisla: overeni_main_vs_matice=0.7216 -->
modelový sloupec je zároveň totožný s hlavní kategorií finálního
klasifikačního běhu (shoda 100 %).
<!-- manifest kap6_kodovani_cisla: overeni_main_je_class7=1 -->
Srovnání pracuje s 12
<!-- manifest kap6_kodovani_cisla: n_kategorii_reseni_srovnani=12 -->
kategoriemi řešení: jedenácti kategoriemi kódovací knihy první etapy
a kategorií proaktivního řešení, kterou model dostal v klasifikačním promptu
(příloha A); pozdější veřejná datová sada používá
odlišnou variantu schématu s jinou sadou štítků, kterou v souladu s pravidly
této knihy nesměšujeme s verzí použitou zde.

### Míry shody

Shodu mezi lidmi kvantifikujeme Krippendorffovým α
(nominálním) na jednotkách kazuistika × anotátorka a doplňkově průměrným
párovým Jaccardovým indexem přes všechny přiřazené kategorie (schéma je
víceznačné). Shodu lidí a modelu vyjadřujeme přesnou shodou na primární
kategorii, rozšířenou shodou (lidská kategorie se objeví mezi kategoriemi
modelu) a Cohenovým κ. Všechny míry doplňujeme 95% intervaly spolehlivosti
z bootstrapu přes kazuistiky (tisíc opakování).
<!-- necislo: parametry bootstrapu jsou popsané slovy -->

## 6.3 Shoda mezi lidskými anotátorkami

Na překryvové podmnožině dosahovala shoda pěti anotátorek různých hodnot
podle dimenze. U dimenze dopadu byla vysoká, α = 0,72
<!-- manifest kap6_kodovani_cisla: k1_alpha_nom_dopad=0.7245 --> (95% CI 0,63
<!-- manifest kap6_kodovani_cisla: k1_alpha_ci_lo_dopad=0.6261 --> až 0,81,
<!-- manifest kap6_kodovani_cisla: k1_alpha_ci_hi_dopad=0.811 --> na 85
<!-- manifest kap6_kodovani_cisla: k1_n_prekryv_dopad=85 --> společně
kódovaných kazuistikách), což odpovídá tomu, že dimenze dopadu má jen několik
zřetelně odlišných kategorií. U typu chování byla shoda střední, α = 0,50
<!-- manifest kap6_kodovani_cisla: k1_alpha_nom_chovani=0.4952 --> (0,41
<!-- manifest kap6_kodovani_cisla: k1_alpha_ci_lo_chovani=0.4141 --> až 0,58),
<!-- manifest kap6_kodovani_cisla: k1_alpha_ci_hi_chovani=0.5782 --> zatímco
u typu řešení nejnižší, α = 0,29
<!-- manifest kap6_kodovani_cisla: k1_alpha_nom_reseni=0.2868 --> (0,19
<!-- manifest kap6_kodovani_cisla: k1_alpha_ci_lo_reseni=0.1914 --> až 0,38).
<!-- manifest kap6_kodovani_cisla: k1_alpha_ci_hi_reseni=0.3756 -->
Obrázek 6.1 tyto hodnoty shrnuje spolu s klíčovou mírou následujícího
oddílu; shoda modelu s lidmi se čte na pozadí toho, jak se shodují lidé
mezi sebou.

![*Obrázek 6.1.* Reliabilita kódování: Krippendorffovo α shody mezi anotátorkami po dimenzích a Cohenovo κ shody člověk × model u typu řešení (95% intervaly spolehlivosti z bootstrapu; svislice vyznačují konvenční prahy 0,667 a 0,80). Obě míry pocházejí z odlišného uspořádání (pět anotátorek na překryvu vs. konsolidovaný lidský kód × model na srovnávacím vzorku) a figura je řadí vedle sebe pro orientaci, ne jako přímo srovnatelné hodnoty (oddíl 6.4). *Poznámka.* Podklady v doprovodném repozitáři: [zdrojová čísla](https://github.com/JanNehyba/edustories-habilitation/blob/main/vystupy/tabulky/kap6_kodovani_cisla.csv), [analýza v R](https://github.com/JanNehyba/edustories-habilitation/blob/main/analyzy/notebooks/20_kodovani_llm.qmd), [kód obrázku](https://github.com/JanNehyba/edustories-habilitation/blob/main/analyzy/scripts/fig_06_shoda.R).](../../vystupy/obrazky/kap6_forest.png)

Nižší shodu u typu řešení vysvětluje především jemnost a překryvnost jeho
kategorií: totéž řešení lze legitimně zařadit pod více blízkých kategorií,
což α (které trestá každou neshodu stejně) tlačí dolů. Přispívá k tomu
i silně nerovnoměrné rozdělení kategorií v čele s rozhovorem (paradox shody,
kapitola 4). Ukazuje to i pohled zohledňující víceznačnost kódování:
průměrný párový Jaccardův index, který částečný překryv přiznává, dosahuje
u řešení 0,56,
<!-- manifest kap6_kodovani_cisla: k1_jaccard_reseni=0.5571 --> u chování 0,61
<!-- manifest kap6_kodovani_cisla: k1_jaccard_chovani=0.6103 --> a u dopadu 0,86.
<!-- manifest kap6_kodovani_cisla: k1_jaccard_dopad=0.8595 --> Tato zjištění
mají přímý důsledek pro následující srovnání s modelem i pro celou knihu.
Frekvenční výsledky Studie 1 uvádíme na úrovni kategorií, ne jako přesné
jednotlivé klasifikace, a hlubší psychometrické čtení jednotlivých kódů typu
řešení by přesahovalo spolehlivost, kterou data unesou.

## 6.4 Shoda jazykového modelu s lidmi

Na srovnávacím vzorku se model shodl s lidskou primární kategorií řešení
v 72 % <!-- manifest kap6_kodovani_cisla: shoda_presna_llm=0.7237 --> případů
(95% CI 68 %
<!-- manifest kap6_kodovani_cisla: shoda_presna_ci_lo=0.6757 --> až 77 %).
<!-- manifest kap6_kodovani_cisla: shoda_presna_ci_hi=0.7718 --> Připustíme-li
rozšířenou shodu, tedy případy, kdy se lidská kategorie objeví mezi kategoriemi
přiřazenými modelem, stoupá shoda na 93 %.
<!-- manifest kap6_kodovani_cisla: shoda_rozsirena_llm=0.9339 --> Cohenovo κ,
které koriguje shodu očekávanou náhodou, dosahuje hodnoty 0,64
<!-- manifest kap6_kodovani_cisla: kappa_llm_clovek=0.6445 --> (95% CI 0,58
<!-- manifest kap6_kodovani_cisla: kappa_ci_lo=0.5825 --> až 0,70),
<!-- manifest kap6_kodovani_cisla: kappa_ci_hi=0.7031 --> což se konvenčně
řadí k dobré shodě.

Tyto výsledky nejsou důkazem dosažení ani překročení lidské úrovně.
Vícehodnotitelské nominální α pěti anotátorek na malém překryvu a κ
konsolidovaného lidského kódu vůči modelu na jiném vzorku neodhadují tutéž
veličinu. Z jejich rozdílu nelze stanovit lidský strop. Neshody mohou
souviset s nejednoznačností schématu i s chybami modelu; tento design jejich
podíly neodděluje. U vzácných kategorií navíc zůstává odhad nejistý.
Výsledek podporuje kontrolované použití modelových kategorií, nikoli
nahrazení lidského úsudku ani nezávisle ověřenou generalizaci.

### Dodatečná kontrola překryvu příkladů

Při revizi byly v příkladech archivovaného promptu nalezeny celé texty
řešení 36 <!-- manifest kap6_kodovani_cisla: n_vstupnich_prekryvu=36 -->
případů ze srovnávacího souboru. Kontrola sjednotila Unicode, velikost
písmen a mezery a hledala úplné řešení v příkladové části archivní buňky.
Nejde o detekci parafrází ani o doklad, že je dochován přesný prompt každého
požadavku; úplné záznamy požadavků nejsou k dispozici. Srovnávací soubor
proto nelze označit za nezávislý test bez překryvu s příklady.

Retrospektivní citlivostní analýza vylučuje tyto shody i neúplný lidský
štítek. Na 297 <!-- manifest kap6_kodovani_cisla: bez_prekryvu_n=297 -->
případech činí přesná shoda 71 %
<!-- manifest kap6_kodovani_cisla: bez_prekryvu_shoda=0.7138 -->
a κ = 0,61 <!-- manifest kap6_kodovani_cisla: bez_prekryvu_kappa=0.6143 -->.
Interval spolehlivosti κ sahá od 0,55
<!-- manifest kap6_kodovani_cisla: bez_prekryvu_kappa_ci_lo=0.5492 -->
do 0,68 <!-- manifest kap6_kodovani_cisla: bez_prekryvu_kappa_ci_hi=0.6821 -->.
Příznaky překryvu bez textů a úplné výsledky obsahuje veřejný analytický report. Tato kontrola neodstraňuje jiné možné vazby
mezi vývojem promptu a testem. Silnější tvrzení vyžaduje nový oddělený
soubor, který nebyl použit při tvorbě instrukcí.

### Shoda po kategoriích

Souhrnné κ zakrývá, že spolehlivost modelu není
napříč kategoriemi stejná. Obrázek 6.2 proto rozkládá přesnou shodu podle
lidské kategorie řešení. U zdaleka nejčastější kategorie, rozhovoru, se
model shodl s lidmi v 77 %
<!-- manifest kap6_kodovani_cisla: shoda_kat:Rozhovor=0.7742 --> případů
(n = 155); <!-- manifest kap6_kodovani_cisla: n_kat:Rozhovor=155 -->
vysokou shodu má i upozornění (76 %,
<!-- manifest kap6_kodovani_cisla: shoda_kat:Upozornění=0.7647 -->
n = 17) <!-- manifest kap6_kodovani_cisla: n_kat:Upozornění=17 -->
a důsledky (75 %,
<!-- manifest kap6_kodovani_cisla: shoda_kat:Důsledky=0.75 -->
n = 16). <!-- manifest kap6_kodovani_cisla: n_kat:Důsledky=16 -->
Nejníže mezi kategoriemi s více než hrstkou případů leží podpora žáka,
u níž se model shodl s lidmi v 56 %
<!-- manifest kap6_kodovani_cisla: shoda_kat:Podpora=0.5581 --> případů
(n = 43), <!-- manifest kap6_kodovani_cisla: n_kat:Podpora=43 --> tedy
právě u kategorie, která je významově nejširší. Prakticky stejně nízko
je i dohoda, tu však nese jen devět případů. U kategorií s jednotkami
případů čísla uvádíme jen pro úplnost; nelze z nich usuzovat.

![*Obrázek 6.2.* Přesná shoda modelu s lidským kódem po kategoriích řešení (n = počet kazuistik s danou lidskou kategorií). *Poznámka.* Podklady v doprovodném repozitáři: [data obrázku](https://github.com/JanNehyba/edustories-habilitation/blob/main/vystupy/tabulky/kap6_shoda_kategorie.csv), [zdrojová čísla](https://github.com/JanNehyba/edustories-habilitation/blob/main/vystupy/tabulky/kap6_kodovani_cisla.csv), [analýza v R](https://github.com/JanNehyba/edustories-habilitation/blob/main/analyzy/notebooks/20_kodovani_llm.qmd), [kód obrázku](https://github.com/JanNehyba/edustories-habilitation/blob/main/analyzy/scripts/fig_06_shoda.R).](../../vystupy/obrazky/kap6_shoda_kategorie.png)

### Anatomie záměn

Konfuzní matice (Obrázek 6.3) ukazuje, kam neshody
směřují, a dokládá, že záměny nejsou nahodilé. Více než čtvrtina případů,
které lidé kódovali jako podporu žáka, dostala od modelu štítek
proaktivního řešení. Obě kategorie popisují vstřícné jednání ve prospěch
žáka a liší se především časováním (podpora reaguje, proaktivní řešení
předchází), tedy rozlišením, které je v retrospektivním textu často
nejednoznačné. Kategorie proaktivního řešení přitom v lidském kódování první
etapy pochází od jediné anotátorky (chybně sestavený výběrový seznam, viz
příloha A). Zde proto vystupuje prakticky jen jako štítek predikovaný
modelem, jemuž byla kategorie nabídnuta v promptu, ne jako plnohodnotná
lidská kategorie. Pětina případů nerespektující komunikace skončila
u modelu jako rozhovor, což odráží skutečnost, že toto jednání má
v kazuistikách typicky podobu slovní výměny s žákem a model se přiklonil
k jejímu doslovnému, hodnotově neutrálnímu čtení.
Záměny tedy kopírují významové hranice mezi kategoriemi; totéž ukázala
analýza lidské shody (oddíl 6.3), kde tytéž hranice snižovaly α.

![*Obrázek 6.3.* Konfuzní matice lidského a modelového kódu řešení (řádkově normalizované podíly; řádky = lidský kód, sloupce = kód modelu; prázdné buňky = podíl menší než 0,005). *Poznámka.* Podklady v doprovodném repozitáři: [data obrázku](https://github.com/JanNehyba/edustories-habilitation/blob/main/vystupy/tabulky/kap6_konfuzni_matice.csv), [analýza v R](https://github.com/JanNehyba/edustories-habilitation/blob/main/analyzy/notebooks/20_kodovani_llm.qmd), [kód obrázku](https://github.com/JanNehyba/edustories-habilitation/blob/main/analyzy/scripts/fig_06_shoda.R).](../../vystupy/obrazky/kap6_konfuzni.png)

## 6.5 Kvalitativní pohled: tři neshody zblízka

Z neshodných
případů, jejichž text řešení je zveřejněn na platformě (kniha zásadně
necituje nezveřejněné texty), jsme náhodně vylosovali
vzorek kandidátů a vybrali z něj tři případy ilustrující navzájem odlišné
mechanismy neshody. Citace jsou doslovné, včetně pravopisu.

> „Nemělo cenu s ním na tu chvíli chodit do kabinetu, když za chvíli byla
> přestávka. Nechala jsem ho tedy být a po chvilce jsem se snažila s ním
> příklady dopočítat, neúspěšně. Zazvonilo na přestávku a před začátkem
> další hodiny jsem se ještě jednou pokusila s ním příklady vypočítat, ale
> marně, tak bohužel musel dostat příklady za úkol na doma, protože ty
> příklady dodělat musí.“
> (člověk: rozhovor; model: přemístění žáka)

První případ ukazuje citlivost na zmíněné, ale neuskutečněné jednání.
Text přemístění žáka výslovně zavrhuje („nemělo cenu s ním chodit do
kabinetu“), přesto model tuto kategorii zvolil; nabízí se čtení, že
reagoval na přítomnost tématu přemístění bez ohledu na negaci, byť z
jediného případu nelze mechanismus doložit. Pro praxi strojového kódování
je to připomínka, že klasifikace podle povrchových vodítek může selhat
právě tam, kde pisatel zvažuje a odmítá alternativy.

> „Vyučování pokračovalo a nic se neřešilo. Ten den se mi ozvala matka
> žáka, že takovéto jednání se jí nelíbí. Já jsem samozřejmě o té situaci
> neměla žádné bližší informace, tak jsem jako třídní napsala, že o tom
> bohužel nic nevím a ať se obrátí na tu konkrétní paní učitelku.“
> (člověk: nerespektující komunikace; model: rozhovor)

Druhý případ odlišuje hodnotící a doslovné čtení. Anotátorka jednání
vyhodnotila jako nerespektující komunikaci, tedy kategorii, která nese
normativní úsudek o kvalitě jednání; model kódoval doslovný komunikační
akt, výměnu zpráv, jako rozhovor. Neshoda tu není omylem v pravém slova
smyslu: je rozdílem mezi popisem toho, co se stalo, a soudem o tom, jak
se to stalo. Právě hodnotící kategorie se ukazují jako nejtěžší disciplína
strojového kódování, což odpovídá obrazu z konfuzní matice.

> „Domlouvání studentovi nezabíralo. A tak se pan ředitel domluvil
> s maminkou žáka a kamarády u policie, že studenta přijdou ‚vytáhnout
> z postele’. A tak jej přišli vzpudit a policie v tomto případě
> zapůsobila. Platilo na něj jen takové vystrašení. Hned se posbíral
> a utíkal do školy. Asi si konečně uvědomil možné následky svého chování.“
> (člověk: rozhovor; model: práce s kolektivem)

Třetí případ ukazuje vícečetné jednání, na které je jednoznačný primární
kód krátký: v řešení vystupuje ředitel, matka i policie a obhajitelných
kategorií je několik. Neshoda modelu s primárním kódem anotátorky tu
z velké části odráží víceznačnost samotné situace; při rozšířené shodě,
která připouští více kategorií modelu (oddíl 6.4), může být hodnocen
jinak. Vybrané případy ilustrují možná vysvětlení neshody, nikoli
systematické rozdělení příčin všech chyb.
Pro praxi strojového kódování z toho plyne konkrétní doporučení: nasazení
modelu na velký korpus by mělo být doprovázeno lidskou kontrolou právě
u hodnotících a významově širokých kategorií, zatímco u kategorií
zřetelně ohraničených lze modelu důvěřovat více. Paušální míra shody
takové rozlišení neumožňuje, rozklad po kategoriích ano.

## 6.6 Shrnutí

Studie 2 doložila, že jazykový model kóduje typy řešení náročného chování
ve shodě s lidskými anotátorkami na úrovni Cohenova κ = 0,64,
<!-- manifest kap6_kodovani_cisla: kappa_llm_clovek=0.6445 --> tedy dobré
shody, s přesnou shodou 72 %
<!-- manifest kap6_kodovani_cisla: shoda_presna_llm=0.7237 --> a rozšířenou
shodou 93 %; <!-- manifest kap6_kodovani_cisla: shoda_rozsirena_llm=0.9339 -->
platí to pro dimenzi typu řešení, na niž se srovnání omezovalo.
Po vyloučení zjištěných překryvů s příklady zbývá κ = 0,61
<!-- manifest kap6_kodovani_cisla: bez_prekryvu_kappa=0.6143 -->;
tato dodatečná analýza není novým nezávislým testem. Lidské α z jiného
uspořádání nelze použít jako výkonový strop modelu. Rozklad po kategoriích ukázal, že spolehlivost modelu
je nejvyšší u frekventovaných a zřetelně ohraničených kategorií a nejnižší
u kategorií významově širokých. Konfuzní matice a kvalitativní analýza
neshod doložily, že záměny kopírují významové hranice schématu (podpora
versus proaktivní řešení, hodnotící versus doslovné čtení jednání)
a ilustrují významovou nejednoznačnost některých kódovacích rozhodnutí.
Vybrané příklady však neurčují podíl všech chyb způsobených schématem.
Model proto v této knize slouží jako nástroj pro
rozšíření obsahové analýzy, ne jako autorita nahrazující lidské kódování.
Následující kapitola obrací pozornost od klasifikace řešení k jejich kvalitě
a srovnává řešení generovaná modelem s řešeními učitelů.

---
