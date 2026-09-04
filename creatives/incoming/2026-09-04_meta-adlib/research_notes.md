# Joint/Arthrosis grey-nutra creative research — working notes

## Method
Tyver API: https://api.tyver.io/creatives/?countries=XX&page=1&search_query="kw"&size=180&sort_by=activity_days_amount
Harvested via authenticated fetch in the Tyver tab; aggregated by ad provider_id (= Meta ad archive ID).

## CANDIDATE 1 (DE/AT) — heilkompass-magazin.de -> ArthroCare+ (Vitaliskraft)
- Domain: get.heilkompass-magazin.de
- Ads found: 28 (11 active at scrape), max run 60d, first 2026-07-02
- FB pages: "Gelenk-Ratgeber Deutschland", "Ingrid Hoffmann" (+1)
- GEO: DE, AT
- LP: https://get.heilkompass-magazin.de/hamburger-radiologin-widerspricht-orthopden/adv11
- Alt path: https://get.heilkompass-magazin.de/adv-FL/fb-FL-1
- Hook: "Arthrose: Radiologin enthuellt die Wahrheit"
- Story: Dr. Anja Brenner, Hamburg radiologist, 14 yrs / 18,000 joint MRIs. Her own mother
  was to get a knee prosthesis at 73; at 76 her MRI shows MORE cartilage than 3 yrs before.
- "New cause": the 40-year misreading of "hyaline cartilage does not regenerate" — it does
  NOT regenerate ON ITS OWN, but it CAN under 3 conditions.
- Mechanism: (1) circulation OPC+piperine, (2) inflammation Boswellia 65% AKBA,
  (3) building blocks UC-II collagen type II immune tolerance + cofactors
- Product: ArthroCare+ Gelenk-Komplex, brand Vitaliskraft
- Proof: 3 named patients (Gisela 63, Mariechen 71, Renate 58), MRI before/after,
  12,843 reviews / 98% satisfaction, 100-day money-back
- Fear: knee replacement surgery
- CTA: "JETZT VERFUEGBARKEIT & ANGEBOT PRUEFEN"

## CANDIDATE 2 (DE/AT/CH) — dailyrituals.news -> Glow25 Kollagen
- 34 ads, up to 28d, 2 FB pages, DE/AT/CH
- Article grid (advertorial disguised as health magazine):
  /artikel/so-repariert-sich-der-knorpel-von-allein/
  /artikel/knorpelverschleiss-ruckgangig-machen-kint/
  /artikel/du-brauchst-keine-operation/
  /artikel/sie-wanderte-mit-68-jahren-allein-auf-die-zugspitze-.../
- Angle A (unisex): "Arthrose ist eine Entzuendungserkrankung" not wear. Collagen peptides +
  vit C activate M2 macrophages + bone marrow stem cells. Expert: Dr. Wolfgang Feil.
- Angle B (women 55+): menopause = -30% collagen in 5 yrs then -2%/yr; cartilage is 75% collagen.
  Protagonist Margot 68 (Austrian architect), NSAIDs -> cortisone -> knee replacement advised ->
  naturopath Hanna Bergmann -> hydrolysed collagen -> hiked Zugspitze.
- Ad hook seen in Tyver: "Was Gelenkschmerzen mit hartnaeckigem Bauchfett zu tun haben"
- Product: Glow25 Kollagen (1200 Dalton peptides, TUEV 99.3%). 25% off, 90-day guarantee.
- Checkout: news.dailyrituals.de/joints-glow-kollagen-angebot/ (+ Amazon link)

## CANDIDATE 3 (DE/AT + multi-GEO brand rotation) — hebratis.com -> Hyaflexa / Kniexa
- LPs: /Hyaflexa-DE/adv , /Hyaflexa-2/adv ; 22 ads DE/AT
- Hook: "Wie ich mit 66 eine Knie-OP dank dieser natuerlichen Loesung vermeiden konnte"
- Story: Margareta 66, told she needs knee replacement in 6 months, refuses, retired ortho nurse
  friend recommends cream, cancels the operation.
- Mechanism: patella misalignment / cartilage rebuild; turmeric + bee venom + green tea + D3/E
- SCALING PROOF: same funnel under different brand names per GEO:
  Hyaflexa (DE), Kniexa / Jointsyn (SE), Ortheva (UK), Ledig (NO)
- Fake authority: "Karolinska Institute", physios James Thompson / Erik Nilsson / Anders Bergstroem
- Backend domains named in fine print: eternicals.com, sernalique.com

## CANDIDATE 4 (DE) — rubelena.com -> ArthroFix (GOUT variant)
- LP: /ArthroFix/DE/Gesundheitsreport/gicht ; 15 ads, up to 73d, AT/DE/CH
- Hook: "5 Gruende, warum Ihre Gichtanfaelle immer schlimmer werden"; ad hook "Kristalle raus. Leben zurueck."
- New cause: 80% of uric acid comes from the LIVER, not diet; glucose-fructose syrup blocks kidney excretion
- Mechanism: hydrangea "Seven Barks" dissolves crystals + Chanca Piedra + 3nB celery seed (allopurinol-like)
- Scarcity: "only 500 packages produced monthly", 90-day guarantee

## CANDIDATE 5 (PL) — noom.pl -> NoomKneePro (SYNOVIAL FLUID mechanism)
- 103 ads (!), 6 FB pages, PL. LPs: /pages/kp-adv-1 , /pages/kp-adv-2 -> /products/masazer-kolan-noomkneepro
- Persona pages: "Twoje Zdrowie 24", "Maria Poznanska"
- Hooks: "Dlaczego Twoje kolano boli BARDZIEJ w nocy niz w dzien" (Andrzej 58, wakes at 1:50am);
  "Mam termin operacji drugiego [kolana]"
- LP headline: "Ortopeda powiedzial 'operacja'. Ale zanim sie zgodzilam - odkrylam dlaczego moje
  kolano naprawde 'rdzewieje' od srodka."
- New cause: SYNOVIAL FLUID DEPLETION. Rusty door-hinge metaphor.
- Mechanism: heat 42-55C -> more synovial fluid + pneumatic compression + vibration
- Money anchor: endoproteza costs 35,000 zl vs device 299 zl. 90-day guarantee.
- Doctor persona: Dr. Tomasz Kowalski, 22 yrs. Patient Bozena 57, grade III OA.

## META AD LIBRARY CONFIRMATION — ArthroCare+ / heilkompass (TIER A #1)
FB page: "Gelenk-Ratgeber Deutschland", page_id 1071691136025619
Meta Ad Library: ~830 results in DE. Status ACTIVE.
Library URL: facebook.com/ads/library/?active_status=all&ad_type=all&country=DE&view_all_page_id=1071691136025619&search_type=page&media_type=all

Sample ad IDs (EU transparency reach/spend shown):
- 1293987872716598 | ACTIVE | 86 days | reach 2k | ~$26 | started 10 Jun 2026 | creative used in 3 ads | -> adv11
- 1291430559732432 | ACTIVE | 63 days | reach 104k | ~$1k | started 3 Jul 2026 | used in 5 ads | -> /pages/top-5-2026-a1
- 3691298077718797 | ACTIVE | 86 days | started 10 Jun 2026 | "Top 5 Mittel gegen Arthrose" test advertorial
- 2186416618787905 | off | 18 days | reach 1k | 22 May - 8 Jun 2026 | used in 10 ads
- 1445783930680967 | off | 19 days | 15 May - 2 Jun 2026 | used in 11 ads
- 962087266873893 | off | 27 days | reach 3k | ~$35 | 3 Jul - 29 Jul 2026 | used in 4 ads
- 1807430953960099 | off | 29 days | reach 752 | 21 Jul - 18 Aug 2026 | ROMAN LEGIONARIES angle
- 1708340256954379 | off | 19 days | reach 523 | 31 Jul - 18 Aug 2026 | ROMAN LEGIONARIES -> adv-FL/fb-FL-1
- 1453287529936566 | ACTIVE | started 3 Jul 2026

### FOUR DISTINCT ANGLES ON THE SAME PRODUCT (ArthroCare+)
A) "Radiologin Dr. Anja Brenner" — 18,000 joint MRIs, two MRIs 13 months apart show MORE
   cartilage; orthopedist on the phone says "Knorpel regeneriert sich nicht, das ist
   Grundwissen seit 40 Jahren"; her own mother, grade-3 bilateral arthrosis 2019, told
   "in 5 years you get a knee prosthesis", now 76 with no prosthesis and a better MRI.
   Mechanism: 3 conditions must be met at once - capillary perfusion, stop silent
   inflammation, type-II collagen building blocks. -> Boswellia 65% AKBA, UC-II, OPC,
   piperine, eggshell membrane hydrolysate.
   LP: get.heilkompass-magazin.de/hamburger-radiologin-widerspricht-orthopden/adv11
B) "ROMAN LEGIONARIES" (the most unusual mechanism found in the whole research)
   Roman legionaries marched 40 km/day in 30 kg armour for 30 days straight; Oxford team
   2009 excavates their skeletons expecting destroyed joints, finds pristine cartilage -
   BETTER than sedentary wealthy Romans of the same age. Dr. Helena Marsh (lead
   archaeologist), Markus Weber (nutrition archaeologist) finds the answer in the camp
   BONE PITS: marrow, cartilage, tendons boiled for hours in the field kettle.
   NEW CAUSE: "Gelenk-Dürre" (joint drought). Cartilage has no blood supply, it is fed
   100% by synovial fluid; production drops from age ~40, by 60 the joint runs on half
   lubrication. Plus zero dietary collagen/hyaluron intake today.
   Reframe: "Verschleiss ist nicht die Krankheit. Verschleiss ist das Symptom."
   "Dein Gelenk ist kein Reifen" (your joint is not a car tyre).
   Proof-by-contradiction: your orthopedist INJECTS hyaluronic acid - so medicine already
   knows the missing fluid is the core problem; the injection just refills from outside
   for EUR 300 every 8 weeks and never restarts your own production ("a dry engine you
   pour a sip of oil into every eight weeks").
   Solution mechanism: Spanish research team working since 1975 finds the most concentrated
   natural hyaluron source in the ROOSTER COMB (Hahnenkamm); patented gentle process keeps
   the hyaluron-collagen matrix intact; placebo-controlled study claims joint cells make
   "up to 10x more synovial fluid", results in 90 days at 60 mg/day.
   German team combines it with UC-II + Boswellia 65% AKBA = ArthroCare+, 18 actives.
   Testimonials: Herbert 64 (2 orthopedists had discussed a prosthesis; op postponed after
   6 months), Renate 59, Christa 63 (deliberately includes a SLOW responder - 7 weeks of
   nothing - which raises believability).
   Offer: summer discount on bulk packs, 100-day money-back, small-batch scarcity.
   LP: get.heilkompass-magazin.de/adv-FL/fb-FL-1
C) "Wir haben die 5 meistverkauften Arthrose-Mittel getestet" — fake comparison test,
   5 required actives (UC-II, Boswellia >=60%, MSM, curcumin 95%, piperine), only ONE of
   5 products has them all. Money-loss framing (EUR 150 wasted / 3 months lost).
   LP: heilkompass-magazin.de/pages/top-5-2026-a1
D) Short radiologist version: "An alle, die mit Gelenkschmerzen oder Arthrose zu kaempfen
   haben" — pain does not correlate with visible wear on MRI; 3 conditions; patient who
   cancelled a hip operation.

## FAMILY 6 — "EMOTIONAL STORY / BURN-AND-ROTATE" NETWORK (CEE + Balkans + IT)
Scale in this dataset: 1,527 ads across 381 disposable domains (.top .xyz .sbs .online
.shop .ink .fit .click), 10+ GEOs. Each ad runs 2-7 days; Meta shows total active time of
8-13 HOURS for some. Pages are fake personas, often with Anglo names on Slavic-language ads
(Gael Hunter / RS, Maddie Shields Parramore / CZ, Ritmo Estable / HR).
Page example: Gael Hunter, page_id 114373201593357, ~21 ads, all inactive, 2-3 day runs.

Same script translated GEO to GEO (proof of one operator):
- "Imam 73 godine. Pre cetiri meseca smo se zena i ja uselili u dom za starije. Sami.
  Svojom voljom. A da deci nismo rekli ni rec." (RS)
  = "Je mi 72 let. Pred pul rokem jsme se s manzelkou prestehovali do domova pro seniory" (CZ)
- "Am 68 de ani. Si imi urasc propria fiica." (RO) = "Stara sem 68 let. In sovrazim
  lastnega sina!" (SI)
- "Brat mi pochina na devetiya den sled operatsiya na kolyanoto. Beshe na 61 godini." (BG)
  -> direct surgery-death fear
- "Drzim v ruce fotku Terezky. Zitra prijde pani z OSPODu a vezme mi ji. Protoze ja, deda,
  uz na nohy nestacim." (CZ) - grandfather loses custody of granddaughter
- "Jesam li ja losa majka?" (HR)
- "Dolaze mi ljudi iz cijele Bosne i Hercegovine. Red cekanja je osam mjeseci." (BA) - healer
- "L'ho portata in braccio per 36 anni. Poi i medici me l'hanno portata via." (IT)
Mechanism variant: BAKING SODA. "Samo jedna porcija sode bikarbone i bol u zglobovima je
nestala za pet dana" (HR) / "Soda, fratilor. Bicarbonat de sodiu obisnuit" (RO)
Domain wellthspring.online/n1ZKFb8C - 50 ads, up to 52 days, 17 pages, HR/RS/BA/ME.
Pages "Kucna Apoteka" (RS) and "Recepti za vas" (HR) point to the SAME link.
LP is CLOAKED: from a clean browser it serves a neutral "ZdravjeInfo" health-magazine
whitepage ("Bolovi u zglobovima: sta ih uzrokuje...", byline "Zdravjeinfo redakcija",
"Medicinski pregledano") with no product at all.

## CANDIDATE — tryneurobalm.com / NeuroBalm (ES-language, US-Hispanic + ES + LatAm)
99 creatives, up to 173 days, single page "Vivo Con Artritis", still active.
LP: tryneurobalm.com/pages/neurobalm
Promise: "Camina sin dolor en 60 dias o te devolvemos tu dinero."
Mechanism: MSM (the "missing crucial ingredient" your supplements lack), mineral remedies
instead of painkillers. Fear: RTC / knee replacement.

## CANDIDATE — typedeal.com (multi-GEO, 55 pages)
Long-running (63d), still active, dozens of persona pages, DE/IT/ES/EN variants:
"Entzuendungshemmende Medikamente bei Gelenkschmerzen verstehen" /
"Scopri come i farmaci antinfiammatori per il dolore articolare sono prescritti..."
Angle: educational/"understand your anti-inflammatory meds" -> quiz/offer.

## RO — dozadesanatate.net -> ArtroCollagen / ArtroMobil
221 days, page "Doza De Sanatate", RO(+BG). Offers: /oferta-artrocollagen ,
/oferta-artrocollagen-concurs-secret , /oferta-artromobil . "2+1 Gratis. Doar 99 Lei"

## META AD LIBRARY PAGE COUNTS (verified)
- Gelenk-Ratgeber Deutschland (DE) page 1071691136025619 -> ~830 ads, ACTIVE
- Twoje Zdrowie 24 (PL) page 815822988277742 -> ~1000 ads, ACTIVE
  (49 days / reach 77k / ~$840 spend; 98 days / 11k / ~$123; creative reused in 4 ads)
- Freya Walsh (vasozi, ALL) page 809279735604337 -> ~520 ads, ACTIVE, 148 days,
  "this ad has several versions"
- Daily Rituals (DE) page 107503954861538 -> ~2400 ads; ads running 465 days and 309 days
- Gael Hunter (RS, burn-and-rotate net) page 114373201593357 -> ~21 ads, all off,
  total active time 8-13 HOURS per ad

## PAGE MAP (same domain, many FB pages = account rotation)
heilkompass: Ingrid Hoffmann (1111289788728964), Gelenk-Ratgeber Deutschland
  (1071691136025619), "Leben mit Arthrose - Selbsthilfegruppe" (1177292532133776)
noom.pl: Twoje Zdrowie 24 (815822988277742), Danuta Dobrowolska (924535254068388),
  Codziennie Lepiej (1117813288082097), Noom.pl (753902501131672), Maria Poznanska
vasozi.com: Freya Walsh (809279735604337), Chad Thompson (708739865656146),
  Naturally Good Nutrition (476335342235353), Joint Health Community (478139438709765)
dozadesanatate.net: Doza De Sanatate (100997305069976)
hebratis.com: Lebensharmonie (567786923086714)
rubelena.com: Eibenhof Natur (167430896446409)

## CANDIDATE — vasozi.com / Vasozi NAD+ (EN, multi-GEO, LONGEST RUN)
39 ads in sample, 9 active, up to 215 days, 4+ persona pages, GEO spread
SI/LT/CH/MK/CZ/FI/NO/LU/GB/ES + US
LP: vasozi.com/products/nad2 (older: /products/nad)
Hooks: "3 signs your hip pain might not be arthritis - even if that's what they told you";
"The pain pills they handed you are doing something they never explained."
NEW CAUSE: not arthritis - "cellular power failure", NAD+ down 50% by age 40, zombie cells.
Mechanism: NR 500mg + quercetin 250mg + resveratrol 150mg, liposomal.
Proof: 4.7/5 from 1,010 reviews; 83% less stiffness in 23 days; "Dr. James Whitfield, MD".
Offer: $39.99 (from $59.99), buy 2 get 1 free. CTA "GET YOURS NOW".

## CANDIDATE — wearebloomy.com / Happy-Meno Articulations (FR/CH/BE)
22 ads, up to 213 days, page "Bloomy"
LP: wearebloomy.com/products/happy-meno-articulations
Hooks: "Vous sentez cette douleur profonde dans la hanche? Voici le veritable responsable.";
"Arretez d'ignorer ma douleur!" ("Are you seriously telling women over 45 they have to live
with hip pain for the rest of their lives?"); "Je connais enfin le veritable coupable"
NEW CAUSE: menopause hormones, not age. Gynecologist "Dr. Anne Martin".
Mechanism: hormonal regulation + inflammation + collagen. Liposomal magnesium, black cohosh, B6.
EUR 35, 2+1 free, "92% de nos clientes ont perdu leurs douleurs en moins de 3 semaines".

## CANDIDATE — Koprez (knee sleeve, competitor-attack angle)
offers.koprez.com/10-reasons-sc , 72 days, 34 pages, US/FR/SI/HR/BE/LT
Hook: "Your Rehband Doesn't Address the Problem in Your Cartilage. Here's Why."

## WAVE 3 — расширенные ключи (артрит, спина, бедро, подагра, ревматизм, скованность)

### NEW: berlyheal.com -> "Her Again" (DE/AT/CH + NL) — ЛУЧШИЙ alt-cause угол
Hook: "WARNUNG: Die am haeufigsten fehldiagnostizierte Erkrankung bei Frauen im Alter von
40-75 Jahren zerstoert langsam Ihre Hueftsehnen - und die meisten Aerzte nennen es
,Arthrose' 😱  Es ist keine Arthrose. Es ist eine Tendinopathie der Glutaeussehnen."
Title: "Die am haeufigsten fehldiagnostizierte Erkrankung bei Frauen ueber 40 zerstoert
Ihre Hueftsehnen - und Ihr Arzt nennt es ,Arthrose'"  DESC: ⭐⭐⭐⭐⭐ (4,8/5)
LP: berlyheal.com/cvh981/564983 ; 14 дн; много персона-страниц
PAGES (19+): Dr. Andrea Hoffmann, Kerstin Schneider, Martina Schneider, Dr. Anna Mueller,
Sabine Mueller, Brigitte Schneider, Sophie Fischer, Tahlia Rowan, Laura Schmidt,
Sabine Fischer, Jessica Smith, Wellness Picks, + NL-страницы: Elke Dag Gezond Leven,
Wellness Connection, Dagelijkse Gezondheidsnotities, Gezonde Basis, Gezondheid in Balans,
Gezond Leven Vandaag, Focus op Welzijn
NEW CAUSE: не артроз, а тендинопатия ягодичных сухожилий (gluteal tendinopathy).
"Wenn Ihr Schmerz ausstrahlt - bauen Ihre Sehnen ab. Nicht Ihre Gelenke."
Механизм: сухожилиям нужен эстроген, чтобы оставаться эластичными и чинить себя. В
менопаузу эстроген обваливается -> сухожилия высыхают, твердеют, рвутся; каждый шаг даёт
микроповреждения, которые тело не чинит.
ATTACK LIST (бьёт по конкурентам в нише!):
  ❌ Schmerzmittel - маскируют симптом, сухожилия изнашиваются дальше
  ❌ Cortisonspritzen - временно, ничего не восстанавливают
  ❌ Dehnen/Chiro/Massage - помогает мышцам, не сухожилиям
  ❌ Turmeric / Collagen / Provitalize - не восстанавливают эстроген
Решение: "Her Again" - Curcumin-Phytoestrogen-Mischung. Шаг 1: экстракт листьев моринги
350 мг 7:1, фитоэстрогены "заполняют пробел, созданный менопаузой".
ЗАМЕЧАНИЕ: этот оффер прямо атакует механизм ArthroCare+/Glow25 (коллаген+куркума).

### NEW: intagetemseums.com -> "Lanuvi - Magazin" (page 782988494906837) DE/AT/CH
54 объявления, 4 дня, фейк-журнал. Углы:
- "Warum eine Koelner Apothekerin jetzt einen 7-fach-Komplex empfiehlt" - аптекарь
  Nadine Forster, 14 лет не могла ничего рекомендовать, пока не наткнулась на
  "Cochrane-Review aus Skandinavien - den Goldstandard der Wissenschaft"
- "Warum Apotheker jetzt ueber eine Kapsel fuer steife Knie sprechen" - Lukas B. (28!)
  из Саарбрюккена: думал, что колени болят только после 60; на прогулке с собакой каждый
  шаг под гору хрустел, через 800 м пришлось остановиться. МОЛОДОЙ ГЕРОЙ - редкая вариация.

### NEW (DE, из ключа Gicht/Rheuma/steife Gelenke):
- www.glinterra.de - 51 объявл., 13 АКТИВНЫХ, 5 страниц, DE/AT/CH/LU
  "Die 15-Minuten-Loesung fuer das tiefe Gewebe"
- www.nimm-medivita.de - 38 объявл., 12 страниц, "Beseitigt Schmerzen in 3 Tagen und
  reduziert Entzuendungen in 7"
- shoporthevia.com - 31 объявл., 72 дня, 6 страниц, "Mach den ersten Schritt raus aus dem Schmerz"
- hiporashop.com - 24 объявл., 68 дней, "37,000+ zufriedene Nutzer"
- surfinbalance.net - 176 дней, CH/DE/AT
- www.fixbv.com - 125 объявл., 8 страниц, "📕Read More Chapter Now" (инфопродукт)

### CROSS-VERTICAL: паразиты как "настоящая причина" боли в суставах
berlyheal.com также крутит: "Ich bin seit 31 Jahren Bestatter. Ich habe ueber 4.000 Koerper
geoeffnet. Und es gibt etwas, das ich in fast jedem einzelnen sehe, worueber niemand
spricht. Wuermer. Ganze Kolonien davon. Eingegraben in die Darmwaende wie Baumwurzeln in
Beton." (гробовщик 31 год, 4000 вскрытых тел, черви) - боль в суставах подаётся как
симптом паразитов. LP: berlyheal.com/ve911/579316 , 63 дня.

### NEW: thebbco.com / Provitalize (BB Company) — ОРИГИНАЛ угла "не артрит, а сухожилия"
175 / 156 дней открутки, US/CH/BR/JP/SI/ES
LP: thebbco.com/pages/pp-provitalize-j-sns
Hook A: "Achy Hips? It's Not Arthritis...  WARNING: Cortisol might be eating your hip
tendons like termites RIGHT now 😱 After menopause, this rogue hormone starts dismantling
your body piece by piece. You see... Cortisol isn't just a 'stress' hormone. It's the
menopause..."
Hook B (UGC-письмо себе): "Dear Past Me, Stop Pill-Hopping. I used to think the next
supplement would be the one. Until I realized I never gave any of them a real shot.
2 weeks here. 3 weeks there. A cabinet full of half-empty bottles... and no results."
  -> снимает возражение "я уже всё пробовала" ЧЕРЕЗ признание собственной вины.

>>> ВОЙНА ОФФЕРОВ: berlyheal "Her Again" в своём списке зачёркнутого прямо пишет
"❌ Turmeric / Collagen / PROVITALIZE - stellen das Oestrogen nicht wieder her".
То есть Her Again атакует Provitalize по имени. Два конкурирующих механизма на одну
аудиторию (женщины 40-75, боль в бедре):
  Provitalize: виноват КОРТИЗОЛ, он ест сухожилия как термиты
  Her Again:   виноват дефицит ЭСТРОГЕНА, сухожилия высыхают без него
Оба отрицают артроз как причину. Это готовая рамка для третьего игрока.

### NEW: orthoakt.com — 11 из 12 объявлений АКТИВНЫ, запуск 23.08.2026
"Knieschmerzen oder Arthrose? Machen Knieschmerzen oder instabile Gelenke jeden Schritt
zur Qual?" -> /products/orthoakt-kniebandage. В тексте упоминается "Orthotal Kniebandage"
= тот же товар, что у orthotal.com -> реселлер/клон. PACK-SHOT, не наш формат, но полезно
как индикатор: сегмент наколенников в DACH пересобирают под новыми доменами.

### NEW: senzio.store — 195 дней, 5 активных
"Soothe Joint Pain in Minutes with This All-Natural Balm", SI/LT/CH/ES/FI/GE

### NEW (PL, из ключей биодро/скованность):
- akademiazdrowia.org — 125 дней, "1 Prosty mechanizm ustawienia biodra"
  (один простой механизм установки бедра) — механический угол, не БАД
- www.zdrowa-aura.pl — 39 объявл., "Po 14 latach spędzonych w towarzystwie małży jestem
  winien prz..." (после 14 лет в компании мидий я должен...) — зеленогубая мидия
- ebook.gabinetkasprzak.pl — 52 дня, "15 lat doświadczenia chiropraktyka zamknięte
  w jednym eBooku" — инфопродукт от хиропрактика

### NEW (HU, после добора):
- getmybodycare.com — 66 объявл., 42 дня, 4 страницы:
  "A csípőfájdalom éveken át tönkretette az alvásomat" (боль в бедре годами разрушала мой сон)
- www.nuvoor.com — 64 объявл., HU, UGC-формат
- tiwnr.com работает и в HU: "A térdinjekciók felfedezése" (открытие уколов в колено)
