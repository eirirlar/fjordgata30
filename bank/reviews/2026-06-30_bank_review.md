# Bankpakke-review – Iterasjon 3

**Dato:** 30.06.2026
**Metodikk:** 7 LLM-agenter, hver tildelt én bank-rolle, leser samtidig hele bankpakka og leverer strukturert vurdering. Hovedtråden syntetiserer.
**Iterasjon 2-ref:** `bank/reviews/2026-06-29_bank_review_001.md`

## Sammendrag

### Helhetsvurderinger per rolle

| Rolle | Iter 1 | Iter 2 | Iter 3 | Endring |
|---|---:|---:|---:|---:|
| Kunderådgiver / Bedriftsrådgiver | – | 6/10 | 7/10 | +1,0 |
| Kredittanalytiker | – | 5/10 | 5,5/10 | +0,5 |
| Kredittsjef / Kredittkomité | – | 6/10 | 6/10 | 0 |
| Risk Officer | – | 5/10 | 6/10 | +1,0 |
| ESG- / Grønt-lån-rådgiver | – | 5/10 | 6/10 | +1,0 |
| Jurist / Legal counsel | – | 5/10 | 6/10 | +1,0 |
| Næringseiendomsspesialist (CRE) | – | 5/10 | 6/10 | +1,0 |
| **Gjennomsnitt** | **5,7** | **5,3** | **6,1** | **+0,8** |

### Per-dokument-snitt (iterasjon 3 vs. iterasjon 2)

| Dokument | Iter 2 | Iter 3 | Endring |
|---|---:|---:|---:|
| 00 Bankhenvendelse | 5,6 | 7,1 | +1,5 |
| 01 Forretningsplan | 5,4 | 6,0 | +0,6 |
| 02 Finansieringsplan | 5,0 | 6,1 | +1,1 |
| 03 MVA-strategi | 7,4 | 7,7 | +0,3 |
| 04 Konkurrent + marked | 6,4 | 7,1 | +0,7 |
| 05 Støtteoversikt | 7,0 | 7,6 | +0,6 |
| 06 Tilskudd som EK | 6,1 | 7,3 | +1,2 |
| 07 Grønt lån | 7,3 | 8,0 | +0,7 |
| 08 Energirapport | 7,4 | 7,6 | +0,2 |
| **Snitt på tvers** | **6,1** | **7,2** | **+1,1** |

### Det viktigste

**Pakken er klart forbedret siden iterasjon 2** — overall fra 5,3 til 6,1, per-dokument-snitt fra 6,1 til 7,2. Største forbedring i bankhenvendelsen (+1,5), tilskudd som EK (+1,2) og finansieringsplanen (+1,1). T118 (anmodning skjerpet), T119 (KodeWorks som avsender) og T114 (endringsmeldinger som godkjent) blir tydelig mottatt positivt — kunderådgiver kaller forespørselen «krystallklart».

Tre svakheter blokkerer for en høyere score:

1. **NY KRITISK — DSCR-inkonsistens i finansieringsplanen**: kap. 4.4 viser DSCR stabilisert 1,49 ved 6,5 % rente; kap. 7.4 viser 0,98 ved samme rente. Flagged av fire av syv agenter som showstopper.
2. **NY — Kapitalisert rente ikke i LTV**: bankramme 29 MNOK + 2,3 MNOK kapitalisert rente = 31,3 MNOK reell eksponering i forventet scenario. LTV bør være ~53 %, ikke 49 %.
3. **GJENGANG — EBITDA-margin 79 %**: fire agenter mener fortsatt for høyt. CRE flagger spesielt at marginen forutsetter KodeWorks-subsidiert drift og at en standalone Fjordgata 30 AS vil ha høyere driftskostnader.

## Diff mot iterasjon 2

### Iterasjon 2-anbefalinger – status i iterasjon 3

| # | Iterasjon 2-anbefaling | Status iterasjon 3 |
|---|---|---|
| 1 | Skjerp anmodningen i bankhenvendelsen | ✅ LØST (T118). Kunderådgiver: «krystallklart» |
| 2 | Snu fortellingen om scenarioer (basis 97 % som hovedtall) | ⚠ DELVIS. Forventet 49 % er fortsatt hovedtall i faktaboks; flere agenter foreslår å vise basis 72 % i samme tabell |
| 3 | Avklar Fjordgata 30 AS-fisjonen | ⚠ DELVIS (T119 etablerte KodeWorks som avsender). Jurist + kredittsjef etterspør fortsatt formell fisjonsplan med tidsanker |
| 4 | Kvalifiser aksjonærgaranti | ❌ IKKE ADRESSERT. Risk Officer + jurist etterspør fortsatt |
| 5 | Skaff skriftlig bekreftelse fra KMF og BYA | ✅ LØST (T114). Presentert som «godkjent» |
| 6 | Stram tallinkonsistens (pris/MVA/bankramme) | ❌ NYE INKONSISTENSER FUNNET. Tilskudd-maks 10 / 10–13 / 10,1–12,7 / 12,5 MNOK; uforutsett 10 % vs 15 %; MVA-dekning 80–100 / 90–95 % |
| 7 | Sondre Enova-kartleggings- vs investeringstilskudd | ✅ AVVIST (T115) — riktig vurdering bekreftet |
| 8 | Inkluder kapitalisert rente i headline-LTV | ❌ IKKE LØST. Kredittanalytiker flagger reell LTV ~53 % ikke 49 % |
| 9 | Re-vurder EBITDA-margin 55 % | ❌ ENDRET RETNING. Brukerens valg i T111 økte margin til 79 %; agentene flagger fortsatt for høyt |
| 10 | DNSH-vurdering + klimatilpasning + energiattest | ❌ IKKE LØST. ESG + jurist etterspør fortsatt |

### Nye svakheter avdekket i iterasjon 3 (ikke i iterasjon 2)

1. **DSCR-tabell-motsigelse (4.4 vs 7.4)**: same rente, samme år, ulike DSCR-tall (1,49 vs 0,98). Vil bli flagget umiddelbart av kredittkomité
2. **Kapitalisert rente 2,3 MNOK ikke reflektert i LTV**: bringer reell LTV fra 49 % til ~53 %
3. **EBITDA-margin avhenger av KodeWorks-subsidiert drift**: ved standalone fisjon må FG30 ha egne personell-/varebilkostnader — realistisk margin 62–70 %, ikke 79 %
4. **Refinansiering av 15,5 MNOK pantelån — eksisterende panthavers samtykke ikke dokumentert**: «change of control»-klausuler kan blokkere
5. **Historisk innskutt EK 1,5 MNOK i støtteoversikt** ikke nevnt i forretningsplan/finansieringsplan — mismatch
6. **Refinansieringsrisiko etter byggefase** ikke drøftet
7. **TBRT-historikk koblet til byggetidsplan-risiko** ikke adressert (Risk Officer)
8. **Worst case grønt lån avslag** ikke modellert som eget delscenario (ESG)
9. **HRP-rapportens 34 % vs 53 %**: rapportens eget kap. 5.3.1 sier 34 % er det DNB-relevante tallet, mens bankpakka leder med 53 % — konflikt agenter fortsatt fanger
10. **Standalone-budsjett for Fjordgata 30 AS** etter fisjon mangler (CRE)

## Prioriterte anbefalinger til iterasjon 4

Rangert etter (a) hvor mange roller flagget det og (b) materialitet for kredittbeslutning.

### Kategori 1 – må adresseres før utsending

1. **Reparér DSCR-inkonsistensen mellom finansieringsplan kap. 4.4 og 7.4.** Samme basisrente 6,5 %, samme stabilisert år, kan ikke gi DSCR 1,49 og 0,98. Sjekk gjeldsbase (kapitalisert rente inkludert?) og EBITDA-grunnlag (med eller uten T111-kutt?). Avstem mot én konsistent linje. Showstopper — flagged av fire agenter.

2. ~~**Inkluder kapitalisert rente i alle LTV-tall.**~~ **ADRESSERT (T124):** Alle LTV-tabeller oppdatert til å lede med reell eksponering inkl. kapitalisert byggerente. Nye scenario-tall: basis 76 %, forventet 53 %, maks 35 %. Bankhenvendelse 00, finansieringsplan sammendrag + 4.2 + 7.1 + 7.2, og forretningsplan 6.1 + 8.1 alle oppdatert med utdyping av tallet uten kap. rente i parentes.

3. ~~**Avstem tilskudd-maks-tall.**~~ **ADRESSERT (T125):** Standardisert til ~12,5 MNOK / detaljspenn 10,1–12,7. Uforutsett 10 → 15 % i finansieringsplan kap. 1 (var glemt nedstrøms-oppdatering fra T107). MVA-dekning konsistent 80–100 % i bankvedleggene (forretningsplan 11 oppsummering oppdatert fra 90–100). Pris launch selvbetjent 220 → 300 kr i kilde_markedsdata. Bankramme oppdatert i bankhenvendelse og forretningsplan til å reflektere sum bankeksponering inkl. kap. byggerente (per T124).

4. ~~**Dokumenter refinansiering av eksisterende 15,5 MNOK pantelån**~~ **UTENFOR SCOPE FOR PRINSIPPSPØRSMÅL (T123):** Refinansiering av eksisterende pantelån håndteres med eksisterende panthaver som del av selve kredittprosessen, ikke som forutsetning for prinsippsvaret. Bankhenvendelsen er klargjort som materialgrunnlag for prinsippforespørsel om innvilget støtte som EK – ikke endelig kredittsøknad. Bankhenvendelse 00 har nå status-tabell som tydeliggjør hva som er ferdig vs. under arbeid.

### Kategori 2 – bør adresseres før utsending

5. **Standalone-budsjett for Fjordgata 30 AS etter fisjon.** CRE flagger at 1,0 MNOK driftskostnad forutsetter delt personell og varebil med KodeWorks-strukturen. Etter fisjon må FG30 ha egne ressurser. Vis enten en separat «standalone»-linje med realistisk 1,4–1,8 MNOK driftskostnad (margin 62–70 %), eller en formell tjenesteavtale med KodeWorks som dokumenterer subsidiert drift.

6. ~~**Fisjonsplan med tidsanker og kontinuitet.**~~ **UTENFOR SCOPE FOR PRINSIPPSPØRSMÅL (T123):** Fisjonsplan med formelle tidsankre, kreditorvarsel og morselskapsgaranti hører til endelig kredittsøknad-fase, ikke prinsippspørsmål. Bankhenvendelse 00 etablerer at KodeWorks Eiendom AS er avsender og at fisjon ikke påvirker prinsippsvaret. Status-tabell tydeliggjør at fisjon er «planlagt før eventuell låneutbetaling».

7. **DNSH-vurdering inkl. klimatilpasning for Nidelv-flomrisiko.** *Delvis ADRESSERT (T126/T127):* Klimatilpasning Nidelv-flom + stormflod lagt inn som risiko-rad i forretningsplan kap. 9, basert på research-notat `bakgrunn/2026-06-30_research_flomrisiko_nidelv_fjordgata30.md` (NVE, Klimaprofil Trøndelag, historikk siden 1857). Full DNSH-vurdering for alle seks miljømål håndteres i T109 (åpen, hører til endelig kredittsøknad-fase).

8. **Vis basis 72 % LTV ved siden av forventet 49 % i bankhenvendelsens faktaboks.** Kunderådgiver + kredittsjef flagger at å lede med forventet er selektivt presentasjon. Vis begge i samme tabell.

9. **Modér EBA/GL/2020/06-henvisningen i 06 ytterligere.** Jurist anbefaler «bankens skjønnsmessige LTV-vurdering innenfor EBA/GL/2020/06s rammer for forsvarlig utlånspraksis (jf. finansforetaksl. § 13-5)» istedenfor «inngår i bankens LTV-beregning».

10. **HRP-rapportens 34 % vs 53 % bør konsolideres**: kompletterende presentasjons-versjon må publiseres samtidig med (ikke etter) pakka. Vurder å lede med 34 % (det DNB-relevante tallet mot opprinnelig ytelse) og bruke 53 % som tillegg, ikke omvendt.

### Kategori 3 – styrker pakken vesentlig hvis tiden tillater

11. **Worst case-scenario for «grønt lån avslag»**: ESG foreslår eget delscenario med rentepåslag +25 bps og bortfall av Enova-energioppgradering 2,3 MNOK.

12. **Mer plausibelt kombinert stress**: Risk Officer foreslår rente +100–150 bp + lease-up-forsinkelse 12 mnd + byggekostnad +10 %. Mer realistisk enn 4-variabel ekstremscenario.

13. **Koble TBRT-forsinkelseshistorikk til byggetidsplan-risiko** (Risk Officer). Eller dokumenter at situasjonen er endret.

14. **Belegg-bane validering med kohort-data fra KodeWorks' eksisterende minilager** (CRE). De 10 kundene som har bedt om fortrinnsrett representerer en eksisterende portefølje — vis faktisk belegg-historikk derfra.

15. **Aksjonærgaranti / morselskapsgaranti — kvalifiser med substans**: hvem stiller, beløp, varighet, dokumentert betalingsevne. Risk Officer + jurist etterspør.

## Per-rolle vurderinger

---

## Kunderådgiver / Bedriftsrådgiver

**Helhetsvurdering av pakken:** 7/10
**Kort begrunnelse:** Forespørselen er nå skarpt definert (én konkret prinsippforespørsel om tilskudd-som-EK), pakken er navigerbar og dokumentasjonen er solid. Hovedsvakhetene er at fisjonen ikke er gjennomført, BFU ikke ferdig, RIB-rapport pågår, samt at LTV i basisscenariet (72 %) ikke matcher rammetabellens «komfortabel sone»-tone i bankhenvendelsen.

### Per dokument

| Dokument | Rating | Styrker | Svakheter |
|---|---|---|---|
| 00 Bankhenvendelse | 8/10 | • Kjernebudskapet er krystallklart: én prinsippforespørsel om tilskudd-som-EK – «ikke mer, ikke mindre»<br>• God sammendragstabell øverst gir umiddelbar oversikt over saksvolum og parametere<br>• Tydelig avgrensning av at fisjonen ikke påvirker prinsippsvaret | • LTV 49 % presenteres som hovedtall, mens basisscenario (kun innvilget støtte) faktisk gir 72 % – en travel rådgiver kan lese den optimistiske LTV-en som «base case» og bli skuffet ved gjennomlesning av finansieringsplanen<br>• Hint om at HRP-rapport «ettersendes som tillegg» skaper inntrykk av at pakken ikke er helt ferdig – bør enten utelates eller markeres som «ikke kritisk for prinsippsvar»<br>• «12–17 MNOK avhengig av tilskuddsutfall» i tabellen og «12–16» i forretningsplanen – små inkonsistenser som irriterer en kredittanalytiker |
| 01 Forretningsplan | 7/10 | • Solid struktur med sammendrag, marked, konkurrent, drift og risiko<br>• Konkret konkurrentbenchmarking med kilder og datoer<br>• 79 % EBITDA-margin er forklart med driftsstruktur, ikke bare påstått | • EBITDA-marginen på 79 % er fortsatt høyt vs. bransjenorm – sammenligning med faktiske norske minilageraktørers regnskapstall ville styrket troverdigheten<br>• Investeringsanslaget («Strukturell rehab. 8–12 MNOK» osv.) er fortsatt brede spenn – banken vil savne en strammere kostnadskalkyle eller henvisning til entreprenørtilbud<br>• Forhåndsetterspørsel er navngitt men uten LOI – setningen om at LOI-runde «vurderes nærmere byggestart» er svakere enn faktiske intensjonsavtaler ville vært |
| 02 Finansieringsplan | 8/10 | • Tre tydelige scenarier (basis/forventet/maks) med komplette LTV-tall<br>• Kapitalisert rente i byggefasen og DSCR-bane med sensitivitet på rente er presis bankspråk<br>• Kontantstrømtabell gjennom byggefasen viser at topp-kapitalbehov er forstått | • DSCR-tabell i kapittel 4.4 viser DSCR 1,49 stabilisert, mens sensitivitetstabell 7.4 viser DSCR 0,98 ved samme basisrente 6,5 % – tallene er åpenbart inkonsistente og vil bli flagget i kredittinnstilling<br>• Kontant-EK 2–3 MNOK er svært tynt vs. bransjenorm 30–40 % EK<br>• Worst case-scenarioet gir LTV 180 % – tabellen viser dette riktig som ekstrem stress, men kan tolkes som at prosjektet ikke har realistisk fallback |
| 03 MVA-strategi | 8/10 | • Klar rangering av alternativer A–E med lovhenvisninger<br>• Vinden-referansen som markedsbevis er konkret og overbevisende<br>• BFU er identifisert som risikomitigering før byggestart | • Fortsatt avhengig av BFU som ikke er sendt<br>• Anbefalingen «start med C eller D» er ikke entydig konkluderende – banken vil ha ett valg fra kunden |
| 04 Konkurrent + marked | 8/10 | • Datokrydret prisinnhenting per konkurrent fra faktiske nettsider gir høy troverdighet<br>• Sentralitet (0,5 km vs. 1,2–12 km) er presist dokumentert<br>• Krypkjeller/Nidelv-segmentet er en plausibel differensiator | • Green Storage 613 kr/kvm/mnd basert på «kun ett datapunkt» – kan virke som cherrypicking<br>• Belegg-prognose 89–92 % stabilisert «noe over markedsmedian» bør valideres mot konkurrentenes faktiske belegg |
| 05 Støtteoversikt | 9/10 | • Tilsagnsdatoer, prosjektnumre og saksreferanser per ordning gir umiddelbar verifiserbarhet<br>• Klar tabell over utbetalingsmekanismer (etterskudd) styrker forståelsen av likviditetsprofil<br>• Kumulering opp mot 70 %-statsstøttetak adressert | • «Historisk innskutt egenkapital 1,5 MNOK» mot 10 MNOK kjøpesum i 2015 – mismatch krever forklaring<br>• Punkt 6 viser konstruksjonsfinansiering 28–30 MNOK uten å bryte det ned i «refinansiert pant» og «ny EK-finansiering» |
| 06 Tilskudd som EK | 8/10 | • Rettskildene er riktig identifisert (EBA/GL/2020/06, NRS 4, skatteloven § 14-42 (3), finansforetaksloven § 13-5)<br>• Bankens dokumentasjonskrav er antesipert<br>• Klart skille mellom regnskapsmessig (utsatt inntekt) og bankmessig (LTV-reduksjon) behandling | • «EBA-retningslinjer for utlånsinitiering implementert i norsk rett gjennom Finanstilsynets rundskriv» er upresist<br>• Utredningen er litt for normativ – kunne nevnt forsiktighetshensyn tidligere |
| 07 Grønt lån | 9/10 | • Krystallklar samletabell mot DNB-, EU- og bankpraksis-kriterier opp front<br>• Eksplisitt håndtering av at HRP rapporterer flere reduksjonstall (53 %, 34 %, 71 %) med transparens om basis<br>• BREEAM-relevans avklart | • Selv erkjenner dokumentet at «kompletterende presentasjons-versjon ettersendes»<br>• EU-taksonomivurdering «bør bekreftes av ESG-rådgiver» kan bremse en grønn lån-prosess |
| 08 Energirapport | 8/10 | • Profesjonell rapport fra HRP AS med NS 3031:2025 / Simien Pro<br>• T1-tiltakspakken konkret beskrevet<br>• Konklusjonsavsnittet nevner eksplisitt at 34 % reduksjon kvalifiserer til grønt lån | • Rapporten er ikke «presentert for bank» – krever tolkning<br>• Inntjeningstider over 100 år – banken vil savne kommentar om at energitiltakene ikke er bedriftsøkonomisk lønnsomme alene<br>• Simien-oppdateringsforbeholdet er en faglig usikkerhet banken kan gripe i |

### Hovedanbefalinger til justering før utsending

- **Reparér DSCR-inkonsistensen mellom kapittel 4.4 og 7.4 i finansieringsplanen** – mest kritiske enkeltfunn
- **Tydeliggjør LTV-rammen i bankhenvendelsen** – vis både 49 % og 72 % i samme tabell
- **Stram inn kontant-EK-tallet (2–3 MNOK)** eller forklar tynt EK eksplisitt
- **Lever vedlagt dokumentasjon samlet, ikke «ettersendes»**
- **Adressér fisjonsstatus konkret** – tidsplan, regnskapsmessig konsekvens, pant-overføring

---

## Kredittanalytiker

**Helhetsvurdering av pakken:** 5,5/10
**Kort begrunnelse:** Pakken er strukturmessig godt arbeidet og dekker det meste en kredittkomité forventer å se, men inneholder en alvorlig intern tall-motsigelse i finansieringsplanens DSCR-bane (4.4 vs. 7.4), kapitalisert rente som ikke er reflektert i LTV-konklusjonen, og en EBITDA-margin på 79 % som ikke er forsvart godt nok for en arbeidskrevende valet-modell.

### Per dokument

| Dokument | Rating | Styrker | Svakheter |
|---|---|---|---|
| 00 Bankhenvendelse | 7/10 | • Klart formulert prinsippspørsmål<br>• Saken-i-korte-trekk-tabellen er kalibrert mot vedleggene<br>• Tydelig om fisjon | • LTV 49 % uten å nevne at kapitalisert rente bringer den til ~53 %<br>• Eiendomsverdi base 59 MNOK presenteres som «verdi» – burde merkes som modellverdi (EBITDA/cap rate)<br>• Mangler forbehold om at base-scenarioets 8 MNOK tilskudd inkluderer 5,75 MNOK ubesluttede |
| 01 Forretningsplan | 5/10 | • Markedsanalyse er konkret, datert og kildebelagt<br>• Konkurrentpriser verifisert<br>• Risikoregister er kalibrert | • EBITDA-margin 79 % er aggressiv og forsvares med «slankt KodeWorks-oppsett» – sirkulær begrunnelse<br>• Driftskostnader mangler eksplisitt linje for eiendomsskatt, IT-plattform-drift, bilkostnader<br>• Tabell 8.1 NPV bruker tre forskjellige cap rates uten markedsbelegg |
| 02 Finansieringsplan | 4/10 | • Sensitivitetsanalyse dekker tilskudd, BFU, byggekost, rente og kombinert stress<br>• Kontantstrømtabell gjennom byggefasen<br>• Mitigerende tiltak listet konkret | • **Intern DSCR-motsigelse:** kap. 4.4 viser DSCR 1,49 ved 6,5 %; kap. 7.4 viser DSCR 0,98 ved samme rente og samme år<br>• Kapitalisert rente 2,3 MNOK ikke i LTV-tabellene – reell LTV i forventet ~53 % ikke 49 %<br>• «Tilskuddsutbetalinger reduserer låneramme» er optimistisk – KMF/BYA/UNI utbetales etter ferdigstillelse |
| 03 MVA-strategi | 8/10 | • Grundig lov- og kildehenvisning<br>• Vinden-referansen er reelt sammenligningsgrunnlag<br>• Risikomatrise og fallback konkret | • Påstanden om «tilsvarende lavere driftskostnader ved fallback» ikke kvantifisert<br>• 10-årig justeringsrisiko ikke modellert<br>• 30/70-allokering mangler underbygging |
| 04 Konkurrent + marked | 8/10 | • Verifiserte priser med dato og kilde<br>• Sentralitets-premium kildebelagt<br>• Ærlig om Green Storage-prisen | • FG30 launch 300 kr ligger på Trondheim Minilagers nivå<br>• Krypkjeller 210 kr har ingen direkte komparabel<br>• Norsk benchmark ligger 40 % under FG30 launch |
| 05 Støtteoversikt | 7/10 | • Vedtaksdato, saksnr., intensitet per ordning<br>• Endringsmelding adressert eksplisitt<br>• Klare milepæler | • Sammensetning «potensielle tilleggstilskudd» overlapper med «høy sannsynlighet» med ulike beløp<br>• Historisk EK 1,5 MNOK ikke dokumentert mot 10 MNOK kjøpesum |
| 06 Tilskudd som EK | 8/10 | • Solid rettskildebruk<br>• Ærlig om at tilskudd ikke er EK regnskapsmessig<br>• Skiller mellom bevilget/utbetalt | • EBA/GL/2020/06 brukes til å antyde bredere anerkjennelse enn faktisk støttet<br>• Tilbakebetalingsrisiko kunne vært kvantifisert (worst case: 2,25 MNOK tilbakebetales) |
| 07 Grønt lån | 8/10 | • Tre referansebasiser dokumentert med transparens<br>• Alle norske bankers krav samlet i tabell<br>• Erkjenner HRP-rapport får supplerende versjon | • Grønt lån-rabatt «10–25 bps» uten kildehenvisning – nyere DNB-praksis er typisk 5–15 bps<br>• EU-taksonomi DNSH-vurderingen ikke gjennomgått for materialer i T1 |
| 08 Energirapport | 9/10 | • NS 3031:2025 og Simien Pro – riktig metode<br>• Effektreduksjon 220 → 40 kW konkret<br>• Strakstiltak og refleksjonsmerknad viser ingenør-ærlighet | • HRP signaliserer selv usikkerhet om fjernvarme/varmepumpe-besparelsen – ikke reflektert i finansieringsplanens energi-antakelse |

### Hovedanbefalinger til justering før utsending

- **Rett opp DSCR-tabell-motsigelsen i finansieringsplan 4.4 vs. 7.4** – showstopper
- **Inkluder kapitalisert rente (2,3 MNOK) i LTV-konklusjonen** – LTV bør være ~53 %, ikke 49 %
- **Forsvar EBITDA-margin 79 % eksplisitt med kostnadssammenligning** mot Vinden eller annet referanseregnskap. Vis margin-sensitivitet ved 65 %
- **Avklar «historisk innskutt egenkapital 1,5 MNOK»** mot forretningsplanens kontant-EK 2–3 MNOK
- **Re-merke «forventet scenario 8 MNOK tilskudd» som «mål-scenario, 5,75 MNOK ikke innvilget»**

---

## Kredittsjef / Kredittkomité

**Helhetsvurdering av pakken:** 6/10
**Kort begrunnelse:** Pakken er materielt forbedret siden sist – konkret prinsippspørsmål, ryddig juridisk fundament og dokumentert grønt lån-kvalifikasjon. Men flere harde tallinkonsistenser på tvers av vedleggene (LTV, DSCR, EBITDA, kontantpriser) og uavklart selskaps-/sikkerhetsstruktur gjør at komitéen vil sende den i retur før prinsippsvar gis.

### Per dokument

| Dokument | Rating | Styrker | Svakheter |
|---|---|---|---|
| 00 Bankhenvendelse | 7/10 | • Tydelig én prinsippforespørsel<br>• Kort tabell med kjernedata gir god opening<br>• Klart skille mellom 2,25 MNOK (i scope) og 5,8/10 MNOK (utenfor scope) | • «Samlet bankramme ~29–35 MNOK» stemmer ikke med finansieringsplanens 23–34,75 MNOK<br>• Sier «LTV ~49 %» som «forventet» uten å nevne basis 72 %<br>• Fisjonen er nevnt, men ikke når den faktisk skjer |
| 01 Forretningsplan | 6/10 | • Solid konkurrent- og posisjoneringsanalyse<br>• EBITDA 79 %-margin er begrunnet<br>• Klar fremdriftsplan | • Sammendraget sier «~12,5 MNOK» maks, kap. 6.1 sier «10–13 MNOK», finansieringsplanen sier «10,1–12,7 MNOK»<br>• Pris-tabell 4.1 viser «300 kr/kvm/mnd» som launch, men MVA-vedlegget refererer «220 kr/kvm/mnd»<br>• Uforutsett 15 % i forretningsplan, 10 % i finansieringsplan<br>• Tilskudd «800 000 kr fra Enova» i 8.2 ikke konsistent med 900 000 (400+500) i 6.1 |
| 02 Finansieringsplan | 5/10 | • God scenariotabell<br>• DSCR-bane med interest-only-struktur<br>• Sensitivitetstabeller nyttige | • **Materiell DSCR-feil**: kap. 4.4 viser DSCR år 5 = 1,49; kap. 7.4 viser DSCR år 5 = 0,98 ved samme rente<br>• Worst-case-LTV 180 % parentes-skrevet uten klar konsekvens<br>• Tabell 4.2 «Ny konstr.fin.» stemmer ikke med sammendragets 12–17 |
| 03 MVA-strategi | 7/10 | • Klar juridisk struktur<br>• Vinden som markedsreferanse<br>• Fallback til passiv utleie | • Anbefaler «Alternativ C eller D» – resten av pakken sier «Alternativ D»<br>• MVA-dekning 80–100 % vs 90–95 %<br>• «BFU planlagt Q3 2026» – svært stramt før byggestart |
| 04 Konkurrent + marked | 6/10 | • Sterk verifisering med dato-stempel<br>• Klar avstandstabell til Torget<br>• Faktiske pristabeller per konkurrent | • Pkt. 2.8 sier FG30 i dag annonserer 100 kr/kvm/mnd på Facebook – reiser åpenbart spørsmål<br>• Konkurrentpriser 286–399 kr vs FG30 plan 300 kr – tynn premium<br>• Forhåndsetterspørsel ikke kontraktsfestet |
| 05 Støtteoversikt | 7/10 | • Klar tabell med tilsagnsdato, prosjektnummer, saksreferanse<br>• Utbetalingsmekanismen forklart<br>• Endringsmeldinger godkjent | • «Enova 50 % intensitet» – 50 % av hva?<br>• «Historisk innskutt egenkapital ~1,5 MNOK» ikke i andre dokumenter<br>• «konstruksjonsfinansiering 28–30 MNOK» vs finansieringsplanens 23–34,75 |
| 06 Tilskudd som EK | 8/10 | • God sammenstilling av NRS 4, sktl. § 14-42, EBA og finforetaksloven<br>• Klart skille mellom regnskapsmessig EK og «egenkapitallignende»<br>• Tabellen over vektingsstatus | • EBA-henvisningene fortsatt generelle<br>• Innovasjon Norge-referansen i 4.2 upresis |
| 07 Grønt lån | 8/10 | • Konkret matrise mot DNB V.5.1, EU-taksonomi, norsk bankpraksis<br>• Ærlig håndtering av reduksjonstall<br>• Klar konklusjon om BREEAM | • «Kompletterende presentasjons-versjon ettersendes» – komiteen vil ikke akseptere ettersending<br>• «Per aktivt brukt kvm 71 %» virker mer kreativ enn nødvendig |
| 08 Energirapport | 7/10 | • Uavhengig faglig kilde (HRP AS), gjennomført befaring, NS 3031:2025<br>• Tydelig tiltakspakke T1<br>• Detaljerte tiltakskort | • Rapporten selv sier «34 % reduksjon → grønt lån»<br>• HRP-merknad om Simien-systemtap<br>• Investeringskostnad T1 = 9,286 MNOK, forretningsplanen runder til 9,3 |

### Hovedanbefalinger til justering før utsending

1. **Rydd DSCR-tabellene** (finansieringsplan 4.4 vs. 7.4)
2. **Avklar fisjonsstrukturen og hvem som er låntaker**
3. **Harmoniser alle nøkkeltall i ett tallark** (uforutsett, MVA-dekning, tilskudd-maks, launch-pris, bankramme)
4. **Ettersend ikke – komplettér først**
5. **Vær mer transparent om det historiske 10 MNOK kjøpet vs. 15,5 MNOK eksisterende pant**

---

## Risk Officer

**Helhetsvurdering av pakken:** 6/10
**Kort begrunnelse:** Pakken adresserer mange enkeltrisikoer eksplisitt (sensitivitetstabeller, BFU-fallback, mitigerende tiltak, kovenant-bane), men har betydelige svakheter på sektordybde (minilager-syklisitet i Norge er ikke dokumentert), konsentrasjonsrisiko (single-asset/single-SPV/single-by er ikke navngitt som risiko), nøkkelpersonavhengighet (Eirik Larsen er reelt single-point-of-failure tross «KodeWorks-struktur»-narrativet) og konsernrisiko fra en fisjon som ennå ikke er gjennomført.

### Per dokument

| Dokument | Rating | Styrker | Svakheter |
|---|---|---|---|
| 00 Bankhenvendelse | 7/10 | • Klar, smal prinsippforespørsel<br>• Fisjonsavhengigheten håndteres eksplisitt<br>• Innvilget støtte separeres skarpt | • Nevner ikke konsentrasjonsrisiko eller fisjonsforsinkelse<br>• Ingen tidsfrist eller exit-klausul antydet |
| 01 Forretningsplan | 6/10 | • Break-even 21 % belegg er reell resiliens-indikator<br>• Driftskostnader detaljert per post<br>• Konkurrentanalyse konkret og verifisert | • Risikotabell mangler konjunktur-/resesjons-risiko, entreprenør-konkurs, cyberrisiko<br>• EBITDA-margin 79 % aggressiv og «KodeWorks-strukturen» ikke kvantifisert<br>• Nøkkelpersonavhengighet bagatelliseres |
| 02 Finansieringsplan | 7/10 | • Worst-case-stresstest gjennomført<br>• DSCR-bane med IO-periode<br>• Kapitalisert rente korrekt modellert | • Worst case 180 % LTV / DSCR 0,62 = teknisk insolvens<br>• Rentefølsomhet stopper på +300 bps; mer plausibelt rente + lease-up-forsinkelse 12 mnd<br>• Toppkapitalbehov Q2-Q3 2027 uten headroom-buffer |
| 03 MVA-strategi | 7/10 | • Juridisk godt forankret<br>• BFU-strategi reduserer tolkningsrisiko<br>• Vinden som sammenlignbar etablert aktør | • Negativt BFU-utfall fjerner 6-7,5 MNOK – fallback ikke kvantifisert<br>• 10-årig justeringsrisiko og TBRT-historikken ikke koblet til 6-mnd-fristen for § 8-6 |
| 04 Konkurrent + marked | 7/10 | • Verifiserte konkurrentpriser med datostempling<br>• Vektet sammenligning per størrelse<br>• Sentralitet og Nidelv-segment som differensiatorer | • Ingen analyse av minilager-bransjens syklisitet i nedgangskonjunktur<br>• Trondheim er understudert kan også være nedside<br>• Forhåndsetterspørsel ikke kontraktfestet |
| 05 Støtteoversikt | 8/10 | • Tilsagnsbrev-referanser med saksnumre<br>• Klart skille innvilget vs. søkt vs. potensielt<br>• Utbetalingsmekanisme ærlig adressert | • Tilbakebetalingsrisiko ved bruksendring ikke stresstestet konkret<br>• Ingen kvantifisering av kombinert intensitet per kostnadspost vs. 70 %-taket |
| 06 Tilskudd som EK | 7/10 | • Rettskildene stort sett riktige<br>• Tilbakebetalingsklausul som «betinget gjeld» anerkjennes<br>• Skiller bevilget/utbetalt vektlegging | • EBA/GL/2020/06 brukes til å antyde bredere anerkjennelse enn retningslinjen gir<br>• Ingen sammenligning med konkrete bankcase fra norsk praksis<br>• Fagmyndighetens «tillitsignal» overvurderes som kredittargument |
| 07 Grønt lån | 8/10 | • Tre uavhengige reduksjonstall gir robusthet<br>• EU-taksonomi og DNB-rammeverk eksplisitt kartlagt<br>• Energimerke D-klassifisering dokumentert | • Grønt lån-rabatt innregnet uten risiko-kvantifisering hvis ikke gitt<br>• DNSH-kravet nevnt uten dokumentasjon av materialvalg/avfallshåndtering |
| 08 Energirapport | 8/10 | • Faglig solid, NS 3031:2025 + Simien Pro<br>• Tre tiltakspakker gir banken valgfrihet<br>• Effekttiltak konkret kvantifisert | • Rapporten flagger Simien-besparelser som mulig feilkilde – ikke trukket inn i sensitivitet<br>• Solceller ulønnsom – undergraver «grønt bygg»-fortellingen marginalt |

### Hovedanbefalinger til justering før utsending

- **Adresser nøkkelpersonavhengighet eksplisitt og kvantitativt** – key-man-forsikring, suksesjonsklausul, hvem kan tre inn innen 30 dager
- **Bygg ut «kombinert moderat stress»-scenariet til hovedstress, ikke fotnote** – rente +100–150 bp + lease-up-forsinkelse 12 mnd + byggekostnad +10 %
- **Konkretiser konsentrasjonsrisiko og fisjonsrisiko** – tidsplan, uttrekkskriterier, konsernkausjon
- **Adresser minilager-bransjens konjunkturfølsomhet i Norge med datapunkt** – 2008/2020 historikk
- **Koble TBRT-dagbøter/forsinkelseshistorikk eksplisitt til byggetidsplan-risiko**

---

## ESG- / Grønt-lån-rådgiver

**Helhetsvurdering av pakken:** 6/10
**Kort begrunnelse:** Pakken treffer 30 %-kravet med god margin og dokumenterer kvalifikasjon mot DNB V.5.1 og taksonomi art. 7.2, men har tre materielle hull: PED/levert energi-konfusjon er erkjent men ikke løst, formell energiattest mangler (kun energikartlegging foreligger), og DNSH/klimatilpasning for et bryggebygg ved Nidelvas bredd er ikke adressert i det hele tatt.

### Per dokument

| Dokument | Rating | Styrker | Svakheter |
|---|---|---|---|
| 00 Bankhenvendelse | 6/10 | • Eksplisitt om at HRP-kompletteringen ettersendes<br>• Ærlig om at kjernekonklusjon er uendret<br>• Nevner G→D og 53 %/34 % | • Ingen omtale av DNSH eller klimatilpasning<br>• 53 % uten å spesifisere PED vs. levert energi<br>• Energiattest-status uomtalt |
| 01 Forretningsplan | 6/10 | • Klart kvalifikasjonsavsnitt 2.4 med tabell<br>• T1-investering tallfestet (9,3 MNOK)<br>• Enova-tilleggsstøtte koblet til kvalifikasjonen | • Hopper rett til «PED-reduksjon = 53 %» uten å vise at levert energi ≈ PED<br>• Klimatilpasningsrisiko (flom/Nidelva) ikke nevnt<br>• Energiattest ikke skilt fra energikartlegging |
| 02 Finansieringsplan | 6/10 | • Grønt lån-rabatt eksplisitt priset inn<br>• Kobler Enova energioppgradering til DSCR-banen<br>• NS 3031:2025/Simien Pro nevnt | • Likestiller PED med levert energi uten forbehold<br>• Ingen sensitivitet på utfallet «grønt lån avslås»<br>• Grønt lån-rabatt fortsatt forutsatt i worst-case |
| 03 MVA-strategi | 7/10 | • Ikke kjerneområdet, ren og uavhengig | • Ingen ESG-relevans<br>• Nevner ikke koblingen mellom valet-flåte og scope 1/2-utslipp |
| 04 Konkurrent + marked | 5/10 | • Refererer Stortrack 2025<br>• Gir markedskontekst | • Ingen ESG-vinkling<br>• «Green Storage» nevnt uten sammenligning av FG30s grønne posisjonering |
| 05 Støtteoversikt | 7/10 | • Eget kapittel 5 om grønt lån<br>• Klar kobling til Enova energioppgradering<br>• HRP-rapport tydelig sitert | • DNBs sitat sier «opprinnelig ytelse», men 53 % er mot referansebygg – internt selvmotsigende<br>• «34 % reduksjon mot energimerkekravet» forvirrende formulering |
| 06 Tilskudd som EK | 6/10 | • Solid rettslig oppbygging<br>• Ikke pakkens ESG-kjerne | • Ingen ESG-vinkling<br>• Bærekraftrapportering (CSRD/ESRS) for refinansiering ikke nevnt |
| 07 Grønt lån | 7/10 | • Tydelig sammendragstabell mot rammeverk<br>• Eksplisitt seksjon 1.4 om basistall<br>• Erkjenner PED vs. levert energi-skille | • DNSH-vurderingen kun én setning – ikke gjennomført materielt<br>• Klimatilpasning/flomrisiko for elvenært bryggebygg ikke vurdert<br>• «Bør bekreftes av ESG-rådgiver» – burde vært gjort før utsending |
| 08 Energirapport | 6/10 | • NS 3031:2025/Simien Pro<br>• Uavhengig ekspert (Anne Kristine Amble)<br>• Tre tiltakspakker med klare tall | • Internt sprikende: 5.3.1 sier 34 % kvalifiserer, hovedbudskap er 53 %<br>• HRP signaliserer Simien-usikkerhet<br>• Formell energiattest mangler |

### Hovedanbefalinger til justering før utsending

- **DNSH-vurdering for taksonomi art. 7.2 må gjennomføres skriftlig** – særlig klimatilpasning for elvebryggen
- **Formell energiattest-status må klargjøres** – energiattest ≠ energikartlegging
- **PED vs. levert energi må løses, ikke bare nevnes**
- **HRP-rapportens interne motsetning (34 % vs. 53 %) må ryddes** før eller samtidig med utsending
- **Worst-case må inkludere «grønt lån avslås»** som eget delscenario

---

## Jurist / Legal counsel

**Helhetsvurdering av pakken:** 6/10
**Kort begrunnelse:** Rettskildebruken er gjennomgående mer presis enn i tidligere iterasjoner, men pakken har fortsatt to strukturelle juridiske svakheter banken vil notere seg: fisjonen til Fjordgata 30 AS er omtalt som «planlagt» uten dokumentasjon av fisjonsplan, kreditorvarsel eller skattemessig kontinuitet, og en garanti/kausjon fra KodeWorks Eiendom AS gjennom fisjonsfasen er ikke nevnt.

### Per dokument

| Dokument | Rating | Styrker | Svakheter |
|---|---|---|---|
| 00 Bankhenvendelse | 7/10 | • Avgrenset prinsipiell anmodning – juridisk ryddig at fisjon ikke påvirker svaret<br>• Tydelig avsenderidentifikasjon<br>• Fremlegger originaldokumentasjon på forespørsel | • «Opprettes ved planlagt fisjon før utbetaling» mangler tidsanker (vedtaksdato, fisjonsplan, regnskapsmessig virkningstidspunkt)<br>• Ingen henvisning til hvem som er låntaker juridisk ved utbetaling<br>• «Bestridt» om TBRT-bøter ikke nevnt – kan være materiell info |
| 01 Forretningsplan | 6/10 | • Klar gjennomgang av mval. § 2-3 + § 3-1<br>• Risiko-tabell anerkjenner regulatorisk usikkerhet<br>• Verneklasse C korrekt identifisert | • Pkt. 1.1: «fisjon» mangler henvisning til asl. kap. 14 og sktl. §§ 11-1 ff.<br>• 15,5 MNOK pant: ingen vurdering av samtykke fra eksisterende panthaver<br>• Pkt. 8.2.4: EBA-henvisning overstrekket |
| 02 Finansieringsplan | 6/10 | • Sikkerhetsstruktur i tabell 4.2 klar<br>• Tilbakebetalingsklausuler nevnt som «betinget gjeld»<br>• DSCR-bane konsistent med rentestress | • Pant-prioritet: refinansiering av 15,5 MNOK krever sletting/transport – ikke beskrevet<br>• Kap. 3-tabellen overstrekker EBA-henvisningen<br>• Ingen vurdering av aksjelovens utbytte-/utdelingsregler ved fisjon |
| 03 MVA-strategi | 8/10 | • Solid rettskildebruk: mval. §§ 2-3, 3-1, 3-11, 8-6, 9-1 til 9-5<br>• Skattedirektoratets prinsipputtalelse 18.11.2014 korrekt sitert<br>• 10-årig justeringsrisiko etter mval. § 9-4 mitigert | • Henvisning til Skatteklagenemnda SKNS1-2020-134 (datasenter) som «analogt» er svak<br>• «Vinden opererer denne modellen» er markedsobservasjon, ikke rettskilde<br>• BFU «planlagt Q3 2026» – bør være igangsatt før låneutbetaling |
| 04 Konkurrent + marked | 8/10 | • Faktagrunnlag datert og kildemerket<br>• Tydelig metode-merknad ved utilgjengelige priskilder | • Ingen juridiske svakheter av betydning<br>• Stortrack-rapport krevende verifiserbarhet for banken |
| 05 Støtteoversikt | 7/10 | • Hver ordning har tilsagnsdato, prosjektnummer/saksreferanse og støtteintensitet<br>• Kumulering mot 70 %-statsstøttetak adressert<br>• Tilbakebetalingsvilkår omtalt | • KMF-vedtekter som «tak på 70 %» upresis – EUs statsstøtteregler/GBER er relevant<br>• Endringsmelding «godkjent» – banken vil kreve skriftlig dokumentasjon<br>• Ingen vurdering av at endret formålsbruk kan utløse fornyet vurdering |
| 06 Tilskudd som EK | 6/10 | • NRS 4 + regnskapsloven § 6-2 + skatteloven § 14-42 (3) presist sitert<br>• Klart skille bevilget/utbetalt<br>• Ærlig konklusjon at tilskudd «ikke er egenkapital» | • **Mest alvorlige svakheten**: EBA/GL/2020/06 avsnitt 5.2.7 og 6.1 nevner ikke offentlige tilskudd spesifikt – disse avsnittene regulerer «income-producing real estate» og generelle LTV-prinsipper<br>• Finansforetaksloven § 13-5 er virksomhetsregulering – henvisningen korrekt men mindre konkret enn fremstilt<br>• Ingen henvisning til Finanstilsynets rundskriv |
| 07 Grønt lån | 8/10 | • EU 2020/852 + Delegert forordning 2021/2139 seksjon 7.2 korrekt<br>• Energimerkeforskriften presist datert<br>• Forsiktig formulert konklusjon | • DNSH-kravet nevnt, men ikke konkret dokumentert for FG30<br>• «BREEAM-NOR In-Use International er ikke lenger tilgjengelig i Norge fra 1.1.2026» – bør verifiseres mot Grønn Byggallianse<br>• DNB rammeverk V.5.1 er internt bankdokument |
| 08 Energirapport | 8/10 | • NS 3031:2025-grunnlag og Simien Pro – juridisk uangripelig<br>• Uavhengig ekspert tilfredsstiller EU-taksonomiens krav | • Ingen formell akkreditering av HRP/Amble eksplisitt nevnt<br>• Diskrepansen 53 % og 34 % – ettersendt versjon reduserer dokumentkraften |

### Hovedanbefalinger til justering før utsending

1. **Nedton EBA/GL/2020/06-henvisningen i dokumentene 01, 02 og særlig 06** til «bankens skjønnsmessige LTV-vurdering innenfor EBA/GL/2020/06s rammer»
2. **Dokumenter fisjonen formelt før bankdialog eskaleres** – tidsplan, kreditorvarsel, skattemessig kontinuitet
3. **Avklar pant-prioritet og samtykke fra eksisterende panthaver** for 15,5 MNOK pantelån
4. **Bekreft skriftlig at KMF og BYA har godkjent endret formålsbruk** – innhent og vedlegg
5. **Sett BFU-prosessen i gang nå** – «planlagt Q3 2026» er for sent

---

## Næringseiendomsspesialist (CRE)

**Helhetsvurdering av pakken:** 6/10
**Kort begrunnelse:** Pakken er strukturelt og juridisk solid, men forretningsmodellen hviler tungt på en utestet full-service-tier (70 % av lager-revenue) med en EBITDA-margin (79 %) og cap rate (6,5 %) som er aggressive for en ny aktør i Trondheim. Konkurrentanalyse og markedsforankring er konkret, men premium-prising 2–3× norsk benchmark og belegg-bane over markedsmedian er ikke bottom-up underbygget.

### Per dokument

| Dokument | Rating | Styrker | Svakheter |
|---|---|---|---|
| 00 Bankhenvendelse | 8/10 | • Fokusert prinsippspørsmål, ikke forvirret med kredittsøknad<br>• Klar struktur, eiendomsverdi/LTV i tabell<br>• Henviser tydelig til vedlegg | • 59 MNOK eiendomsverdi presenteres som «base» uten markering at den hviler på utestet EBITDA |
| 01 Forretningsplan | 6/10 | • Komplett, godt strukturert<br>• Tydelig kobling mellom MVA, marked og prising<br>• Erkjenner at margin er over bransjenorm | • EBITDA-margin 79 % forutsetter KodeWorks-subsidiert drift – standalone Fjordgata 30 AS er ikke testet<br>• Belegg-bane 89–92 % ligger over norsk median uten kohort-data fra eksisterende KodeWorks-minilager<br>• «Fortrinnsrett fra 10 kunder» ikke kontraktsfestet – telles likevel som risikoreduksjon |
| 02 Finansieringsplan | 7/10 | • DSCR-bane med IO-periode og rentestress<br>• Worst case-stress vises ærlig<br>• Kontantstrøm gjennom byggefasen synliggjør Q2–Q3 2027-toppen | • DSCR-tabell i 4.4 og 7.4 motstridende tall<br>• Worst case cap rate 9,0 % moderat – sentralt minilager med ny aktør handles trolig 8,5–10 %<br>• Refinansieringsrisiko etter byggefase ikke drøftet |
| 03 MVA-strategi | 9/10 | • Solid rettslig forankring<br>• Vinden brukt som markedsreferanse<br>• Fallback til passiv drift definert | • Justeringsplikt (10 år) kunne vært tydeligere kvantifisert overfor bank |
| 04 Konkurrent + marked | 7/10 | • Konkrete priser, hentet med dato per konkurrent<br>• Avstand-fra-Torget-tabell konkret<br>• Realistisk merknad om Minilager1 XXL-pris | • Norsk benchmark Stortrack 2025 (~120–140 kr/kvm/mnd) vs prismål 300–360 kr – gap ikke underbygget bottom-up<br>• «20–35 % premium for sentralitet» rettferdiggjør ~150 % premium – henger ikke sammen<br>• Trondheim-spesifikk yield/cap rate ikke innhentet |
| 05 Støtteoversikt | 8/10 | • Konkrete saksnumre, datoer, beløp, intensitet<br>• Endringsmelding (KMF/BYA) god risikodempning<br>• Statsstøtte-tak (70 %) sjekket | • UNI revisorbekreftelse ikke fremhevet for bank |
| 06 Tilskudd som EK | 8/10 | • EBA/GL/2020/06, NRS 4, skatteloven, finforetaksloven – komplett kjede<br>• Skiller bevilget/utbetalt-statusene med praktiske implikasjoner<br>• Anerkjenner at tilskudd ikke er EK regnskapsmessig | • «På linje med egenkapital» (avsnitt 4) sterkere språk enn EBA støtter |
| 07 Grønt lån | 8/10 | • DNB rammeverk V.5.1, EU-taksonomi art. 7.2, norsk bankpraksis dekket<br>• Tre ulike basis-tall ærlig presentert<br>• BREEAM-spørsmål håndtert direkte | • 53 % er mot referansebygg-energi etter ombygging – DNB-formulering ambivalent. Banken kan akseptere 34 % – men ikke selges som 53 % uten merknad |
| 08 Energirapport | 7/10 | • Faglig solid (NS 3031:2025, Simien Pro, akkreditert rådgiver)<br>• T1-pakke definert, kostnader spesifisert<br>• Strakstiltak praktisk | • Inntjeningstid >100 år – kommer ikke fram i bankpakka<br>• HRP gir energimerke D = 34 % reduksjon – ikke 53 %<br>• «Kompletterende presentasjons-versjon» bestilt men ikke vedlagt |

### Hovedanbefalinger til justering før utsending

- **Cap rate og eiendomsverdi: korriger til konservativt benchmark for sekundærmarked.** 7,5–8,0 % mer realistisk for ny aktør; gir base 48–51 MNOK
- **Avstem belegg-bane med faktisk kohort fra KodeWorks' eksisterende minilager**
- **Korriger DSCR-tabellene i finansieringsplan 4.4 og 7.4** til samme tallgrunnlag
- ~~**Separer KodeWorks-subsidiert drift fra standalone Fjordgata 30 AS-drift**~~ **ADRESSERT (T122):** KodeWorks subsidierer ikke driften. FG30 kjøper konkrete tjenester (regnskap, administrasjon, IT-support adgangssystem, HR-bistand) fra KodeWorks-strukturen via tjenesteavtale på markedsvilkår. Valet-tjenesten driftes av ekstern operatør på resource-on-demand-kontrakt. Driftskostnad 1,0 MNOK står som reell kostnadsbase – fotnoten i forretningsplan 6.2 er omformulert for å reflektere dette
- **Justér grønt lån-narrativet til 34 %, ikke 53 %**
- **Legg til et eksplisitt exit-/refinansieringskapittel**

---

## Metodikk og forbehold

- LLM-agenter imiterer roller ut fra allmenn kunnskap, ikke 20 års bankerfaring. Output er **idégrunnlag**, ikke autoritativ vurdering.
- Hver agent leser samme materiale men med ulik linse — overlapp i funn er forventet (og styrker funnene som er konsensus).
- Ratings kalibreres på skala 10 = perfekt for rollens behov, 5 = brukbart med betydelige forbehold, 2 = uakseptabelt.
- Ingen agent har domenekunnskap om FG30 utover hva som står i bankpakka — observasjoner kan derfor være feilaktige der konteksten er gitt utenfor pakka.
- Diff mot iterasjon 2 er syntese basert på iterasjons-2 topp-anbefalinger som er dokumentert i T104-historikk, ikke en direkte agent-vs-agent-sammenligning.
- Agent-tool opprettet 7 worktrees per spawn (uunngåelig i denne harness-versjonen). Rydding etter sesjon: se T104 «KRITISK»-seksjon.
