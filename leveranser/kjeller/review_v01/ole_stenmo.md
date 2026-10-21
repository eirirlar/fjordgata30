---
dokumenttype: RIB-gjennomgang av kjellerplan v01
revisjonsobjekt: leveranser/kjeller/plan_v01.md
reviewer: Ole Stenmo, Sivilingeniørene Harboe og Leganger AS
dato: 2026-10-21
status: intern — ikke sendt til byggherre eller myndigheter
---

# RIB-gjennomgang — Kjellerplan v01, Fjordgata 30

**Ole Stenmo, sivilingeniør, Harboe og Leganger AS**\
Signaturansvar: RIB (konstruksjon), Fjordgata 30 Minilager\
Dato: 21.10.2026

---

## Oppsummering

Planen er solid strukturert for et internt arbeidsdokument og gjenspeiler at forfatteren har lest mitt notat av 10.02.2026 nøye. Hard-coded-tabellen er korrekt gjengitt og fasekonstruksjonen gir gode operasjonelle grep. Det som bekymrer meg profesjonelt er ikke strukturen, men det som mangler i den: lastforutsetningene er ufullstendige (jordtrykksparametrene er ubekreftet av geotekniker), betongarbeidet under grunnvannspeil er ikke operasjonalisert langt nok til at det kan utføres uten ytterligere avklaringer, og Modell B slik den er beskrevet inneholder fem til seks trinn der jeg i dag ikke kan gi RIB-signatur over hodet på utførelse uten ansvarlig utførende betong (SB-godkjenning). Planen er for lenge siden klar til videre arbeid i F0–F3; for F6–F9 er den et godt utgangspunkt, ikke et ferdig underlag.

**Score konstruksjonssikkerhet: 6 / 10** (for v01 som internt utkast). V02 med lukkede avklaringspunkter og mottatte armeringstegninger vil ligge nærmere 8–9.

---

## Lastforutsetninger — er disse riktig gjengitt?

- **Dimensjonerende vannstand kote +3,20** — korrekt. Bekreftet i mitt notat 10.02.2026. Dette er en tidvis oversvømmelseskote basert på registrert 100-årsflom kombinert med stormflo fra Meteorologisk institutt og NVE-data for Nidelva. Verdien brukes som dimensjonerende poretrykk mot bunnplate og yttervegger.

- **Nyttelast kjeller og plan 1 — 7,5 kN/m²** — korrekt. Merk at dette gjelder hele kjellerdekket og plan 1. Planen nevner ikke at 7,5 kN/m² er en *karakteristisk* nyttelast; dimensjonerende last med LF = 1,5 er dermed 11,25 kN/m². Denne distinksjonen skal ikke være i arbeidsdokumentet, men det er viktig at utfører ikke blander karakteristisk og dimensjonerende.

- **Nyttelast plan 2–5** — 5,0 / 3,0 kN/m² — korrekt.

- **Snølast 2,8 kN/m²** — korrekt, iht. NS-EN 1991-1-3 og Trondheims sone.

- **Jordtrykksparametrene (sand, φ = 33°, γ = 17 kN/m³)** — dette er verdiene fra mitt *gamle* notat av 13.06.2025, og planen selv skriver «må verifiseres av geotekniker». Jeg vil understreke at dette ikke er en «anbefalt til å løse seg selv»-kommentar — dette er et **blokkerende punkt** for Fase 7 og 8. Horisontalt hviletrykk (K₀ = 1 − sin φ ≈ 0,45) og aktivt jordtrykk fra terrenget bak natursteinsmuren er dimensjonerende for veggtykkelses- og armeringsvalget. Hvis grunnen er mykere leire enn antatt, eller friksjonsvinkel er lavere, endres veggarmeringen vesentlig. Jeg kan ikke signere armeringstegning for yttervegg uten geoteknisk bekreftelse av jordparametrene.

  **Krav til v02:** Geotekniker (ikke RIB) bekrefter jordparametrene skriftlig basert på prøvegraving i Fase 5A — eller det utføres enkel vingeboring / CPT i ett punkt langs veggen *før* armeringstegning for F8 låses.

- **Hviletrykk fra natursteinsmur** — **mangler i planen.** Natursteinsmuren er ikke selv dimensjonert som last mot den nye betongsiden. Egenvekten av muren kan sette et lateralt trykk mot den ensidige forskalingsflaten i nedre del dersom muren er satt i bevegelse under graving. Dette er ivaretatt i min separasjons-detalj (XPS + plast/duk), men planen dokumenterer ikke dette eksplisitt som et laste-prinsipp.

- **Brannkrav R60** — korrekt. Gjelder hoved- og sekundærbæring. Betongens dekke iht. XS3 (min. 50 mm) er tilstrekkelig for R60 forutsatt at armeringsdiameter og konstruksjonshøyde er som tegnet.

- **Egenvekter** — korrekt gjengitt.

- **Seismisk last** — ikke nevnt, men Trondheim er i seismisk sone med lav ag (< 0,1g per kart), og NS-EN 1998-1 § 4.2.5 unntar bygninger i underordnet konsekvensklasse. Relevant for arkivering, men ikke blokkerende.

---

## RIB-signeringsmatrisen — min versjon

Nedenfor er den matrisen jeg *faktisk* er villig til å signere, sammenlignet med det planen forutsetter. Planen er i all hovedsak riktig, men den utelater «dokumentert av hvem» og «konsekvens hvis ikke» i tilstrekkelig grad for et juridisk ansvarsdokument.

| Gate | Handling som utløser gate | Hva jeg signerer | Hva må foreligge skriftlig | Konsekvens hvis signatur mangler |
|---|---|---|---|---|
| RG-1 | Kutting av bærende tømmerstokker | Skriftlig per element: KUT / STØTTE+KUT / BEV. Støttespesifikasjon ved STØTTE+KUT. | Fase 1-tegninger (T1 + T2), sikringsplan fra PGL, foto av alle elementer | Kutting er **forbudt**. Ulykke = RIB-ansvar og HL-ansvar. |
| RG-2 | Graving til prosjektert bunnkote fullført | Skriftlig bekreftelse at grunnforholdene er tilfredsstillende for bunnplate | Fase 5-befaring med meg til stede, foto, kotelogg | Bunnplate støpes ikke. Annet tiltak kan bli nødvendig. |
| RG-3 | Armering fundamenter F6 | Skriftlig per fundament-batch | Ferdig armering iht. min produksjonstegning, foto med målestav, avstandsholdere kontrollert | Betongbestilling avbrytes. |
| RG-4 | Armering bunnplate F7 | Skriftlig godkjenning. **Dette er min viktigste signatur i prosjektet.** | Komplett armeringsplan som-lagt sendt meg med overlappende foto, svelleprofil montert og synlig på foto, søylegjennomføringer med svellebånd på plass | Betongbestilling avbrytes. Støp er **forbudt**. |
| RG-5 | Bunnplate ferdig herdet (7 dager) | Skriftlig visuell godkjenning | Foto av hele platen, 7-dagers prøveresultater sendt meg, ingen synlige kaldskjøter uten svellebånd | F8 (vegger) starter ikke. |
| RG-6 | Armering yttervegger F8 | Skriftlig per vegg-batch | Armeringsplan som-lagt, foto, avstandsholdere kontrollert, separasjonssjikt XPS + duk synlig | Betongbestilling avbrytes. |
| RG-7 | Armering delevegger F9 | Skriftlig | Armeringsplan som-lagt, foto | Betongbestilling avbrytes. |
| RG-8 | Sluttkontroll hele kjeller | Skriftlig sluttattest | Komplette testresultater (28-dagers), katodisk dokumentasjon, dokumentert tetthet (visuell + ingen lekkasjer etter 30 dager), alle foregående RG-attester samlet | Ferdigattest til kommune utstedes ikke fra RIB. |

**Signering under Modell B — mitt standpunkt:**

Jeg signerer *prosjektering* uansett modell. Jeg signerer *utførelsesgodkjenning* (armerings- og støpe-gate) kun der det er en person med SB-godkjenning for betong til stede under den kritiske operasjonen. Jeg er ikke ansvarlig utførende — jeg er RIB. Hvis det ikke finnes noen SB-godkjent på plassen ved støping av bunnplate og yttervegger, nekter jeg å gi RG-4 og RG-6. En e-post fra Kristian med foto uten at en SB-godkjent har observert støpeprosessen, gir ikke tilstrekkelig grunnlag for min signatur.

---

## Fundamentdimensjonsmotsetningen — fasit

ISY post 05.1 sier **200 × 200 × 40 cm** (= 2 m × 2 m × 0,4 m). ISY post 05.29 sier **3000 × 3000 mm** (= 3 m × 3 m) for XPS-isolering under de *samme* fundamentene.

**Mitt svar basert på bæreanalysen i notatet 10.02.2026:**

Fundamentene er dimensjonert for aksellast fra stålsøyler HUP 150×150×5 (innerst mot Fjordgata) og HUP-søyler i søndre del, med nyttelast 7,5 kN/m² og akkumulert lastareal per søyle beregnet ut fra søylenes akseavstand (ca. 3 m c/c). Med trykkfast kapasitet på sand φ = 33° på antatt 1,0–1,5 m dybde og en konservativ grunntrykksformel (Meyerhof) ga min beregning grunnflate per fundament i området 3,5–4,5 m². Det betyr at **200 × 200 cm = 4,0 m²** er korrekt dimensjon — dette er *ikke* en skrivefeil.

**Konklusjon: 200 × 200 × 40 cm (post 05.1) er den riktige dimensjonen.** Post 05.29 med 3000 × 3000 mm er en feil, sannsynligvis fordi forfatteren av ISY-beskrivelsen har skrevet XPS-dimensjonen som om den tilsvarer hele fundamentets bunnareal, men satt inn et for stort tall. XPS 50 mm legges under fundamentet og har dermed *samme* grunnflate som fundamentet, altså 200 × 200 cm. Rett post 05.29 til **2000 × 2000 mm**.

Konsekvens for prosjektet: Den totale XPS-mengden under fundamenter er ca. 25 × (2,0 × 2,0) = ca. 100 m², ikke ca. 225 m². Dette er en vesentlig mengdeforskjell som påvirker anbudssum.

---

## Betongarbeid under grunnvannspeil — minimumskrav

### Hva utfører MÅ gjøre

1. **Lensepumpe i kontinuerlig drift under hele støpeoperasjonen.** Kapasitet: minimum 500 l/min, med reservepumpe dimensjonert for samme kapasitet. Grunnvannspeil i Nidelv-nærhet kan i springflo-perioder stige raskt. En lensepumpe som feiler under støp gir katastrofal situasjon.

2. **AUV-betong (Anti-Undervann-støping) der vann kan stå i formene.** Planen nevner B45 MF40 Cl 0,10 AUV-betong for fundamenter. Dette er korrekt. AUV-betong er selvkomprimerende og tåler kontakt med begrenset vannmengde. Krav til leverandør: konsistensklasse minst SF2 (utbredelsesmål ≥ 660 mm per NS-EN 206), og segregeringsresistens (SR2). Dette er **ikke** standard pumpe-betong — si dette eksplisitt til leverandøren.

3. **Støping i steg — aldri mer enn 0,5 m vanndybde i form ved støpstart.** Pumpe til formen pumpes ned til under 10 cm vann før betong tilsettes. Det er utfører (SB-godkjent) som avgjør når dette er oppfylt.

4. **Armeringsoverdekning 50 mm minimum (XS3).** Planen sier dette er bekreftet av RIB — korrekt, men det er *jeg* som bekrefter per produksjonstegning. Ingen avstandsholder av plast med lavere c-mål enn 50 mm skal brukes. Avstandsholdere skal dokumenteres med produktdatablad og type (sement-baserte avstandsholdere anbefales i marint miljø fremfor plasttyper).

5. **Herdetemperaturlogg.** For betong under grunnvannspeil er raskt varmetap en risiko. Hvis temperatur i betong faller under +5 °C innen de første 24 timene etter støp, er det porevannet som fryser og bryter kapillarstrukturen. Krav: termometer i betongen (plasser en termoføler i betongen) eller bruk av herdelogg-apparat, med dokumentasjon levert meg.

6. **Betongprøver.** Minimum 3 sylindre per 30 m³. Prøvene sendes til akkreditert laboratorium (ikke egne folk som presser). 28-dagers trykkresultater sendes meg som del av RG-3 og RG-4 sluttdokumentasjon.

7. **Støpeskjøt med svelleprofil.** Svelleprofil (SikaSwell P Type H) skal beskyttes mot aktivering av fukt **før** støp — monteres tidligst 48 timer før støping, og beskyttes med Master VB2 160 fugeblikk som angitt i planen. Krav: Sika-sertifisert montør eller kontrollert av Sika-tekniker, med dokumentasjon. En svelleprofil som aktiverer seg selv under lagring eller montasje er ubrukelig.

8. **Separasjonssjikt mot natursteinsmur.** XPS 50 mm + plastduk er hard-coded. Kontrollen min (RG-6) vil inkludere visuell sjekk av at duken er hel og at det ikke er hull der betong kan flyte inn mot stein. Revner i duken tettes med selvklebende butylgummitape — ikke vanlig teip.

### «Nice to have» men ikke absolutt krav

- Vanninntrengningstest (permeabilitetstest) på laboratorieprøver av betongresepten fra leverandøren, dokumentert med w/c < 0,45 og faktisk W/B-tall.
- Bruken av krympereduserende middel (Sika Plastiment® eller tilsvarende) for bunnplate — reduserer autogen krymping og bedrer vanntetthet ytterligere. Anbefales men er ikke krav i NS-EN 206.
- Ultralydscanning av ferdig plate for hulromdeteksjon (Pulse Velocity Test) — aktuelt hvis 28-dagers prøver viser lavere fasthet enn forventet.

---

## Uakseptable steg i planen

Følgende trinn slik de er beskrevet per v01 er etter min vurdering uakseptable uten tilleggskrav eller modifikasjon:

**U1 — F3.8: Kutting av tømmerstokker basert på RIB-signert liste, uten krav om fagperson til stede under selve kuttingen.**

Planen beskriver at RG-1 er klarert i Fase 2, og at Kristian/Ain deretter kutter. Det er riktig at jeg signerer per element i forkant. Men planen sier ikke noe om at en faglig ansvarlig person (HMSK-kompetent person som kan vurdere konstruktiv atferd under og etter kutting) skal være til stede der det gjelder elementer med STØTTE+KUT. Stokken kan oppføre seg annerledes enn forventet.

*Krav til v02:* For STØTTE+KUT-elementer: en person med byggeleder- eller RIB-kompetanse (ikke nødvendigvis meg) skal være til stede under selve kuttingen og signere dagsrapporten.

**U2 — F6.2: Graving for fundamenter uten spesifisert avstand til eksisterende søyler.**

Planen sier «grav ned for hvert fundament til prosjektert nivå» uten å angi at graving i nærheten av eksisterende søyler (som i dag bærer etagsekillene i 1. og 2. etg.) krever ytterligere forsiktighet og RIB-kontroll per søyle. Setningsrisiko er ikke null.

*Krav til v02:* Eksplisitt krav om at graving nærmere enn 50 cm fra eksisterende søylefot kun skjer med fagarbeider og etter at jeg har angitt tillatt graveprofil per søyle. Dette må inn som et eget mini-gate i F6.

**U3 — Modell B: F7.15–F7.18 (armeringskontroll og støping av bunnplate) uten klar SB-godkjent til stede.**

Planen beskriver at byggherre sender foto til meg og jeg signerer (RG-4). Men under selve støpingen (F7.18) er det kun nevnt «betongbas» som `[KREVER PROFF]`. En betongbas er ikke det samme som en ansvarlig utførende (SB-godkjent) for betongarbeider. Bunnplaten er utførelsesklasse 2, og NS-EN 13670 krever at det er et system for produksjonskontroll — ikke bare en fagarbeider som styrer pumpebilen.

*Krav til v02:* I Modell B må det eksplisitt stå hvem som bærer SB-godkjenning for betongarbeider under F6, F7, F8, F9. Hvis Kristians firma KMTE ikke har SB-godkjenning for betong, må det leies inn et firma som har det og som signerer som ansvarlig utførende. Uten dette gir jeg ikke RG-4.

**U4 — F8.3: Plast/tett duk festes med «plugger i mørtelsfuger».**

I en kulturminnevernkontekst er mekanisk opprykk av mørtelsfuger i eksisterende natursteinsmur et inngripende tiltak som kan svekke murens stabilitet. Fuging med plugg kan spalte fugemørtel som allerede er svak. Borremetode i stein er enda verre.

*Krav til v02:* Fastgjøring av separasjonssjikt til natursteinsmur skal kun skje med metoder godkjent av PGL og Byantikvar — f.eks. selvklebende butylgummitape eller kilefesting øverst og nederst uten borring i mur. Jeg anbefaler at PGL Ole Morten skriver en kort monteringsanvisning.

**U5 — F11: Katodisk korrosjonsbeskyttelse uten RIB-kontroll av stål-eksponert areal som inngangsvariabel.**

Planen sier at spesialist prosjekterer «basert på eksponert stålareal (25 søyler Ø 150–200 mm...)». Men armeringsstålet i bunnplate og vegger er *også* stål i marint miljø, selv om det er innstøpt. Katodisk beskyttelse av innstøpt armering er et eget fagfelt (SACP — Sacrificial Anode Cathodic Protection for reinforced concrete) og skiller seg fra offeranoder for eksponert stål. Det er ikke gitt at én spesialist dekker begge.

*Krav til v02:* Spesialistens mandat presiseres: (a) offeranoder for eksponert stål (søylene), (b) vurdering av om innstøpt armering i XS3-miljø krever ekstra tiltak. Mitt engasjement inkluderer teknisk gjennomgang av spesialistens rapport (F11.4) — dette er allerede i planen, men mandatpresisjonen er ikke.

**U6 — Modell B generelt: F9 (delevegger) er beskrevet uten krav om SB-godkjenning.**

Delevegger bærer laster fra plan 1 iht. mine tegninger. Det er dermed en bærende konstruksjon, og utførelsesfeil her er ikke trivielle. Planen sier «som Fase 8 — forskalingstekniker og betongbas». Det er ikke tilstrekkelig.

*Krav til v02:* Delevegger (F9) har samme krav til SB-godkjent tilstedeværelse som yttervegger (F8).

---

## Konkrete endringer jeg vil ha i v02

1. **Fundamentdimensjon: korriger ISY post 05.29 til 2000 × 2000 mm.** Oppgi eksplisitt at 200 × 200 cm er riktig mål, med referanse til min beregning fra 10.02.2026. Korrigerte mengder for XPS under fundamenter beregnes til ca. 100 m² (25 stk × 4 m²).

2. **Geotekniker inn i prosjektet.** Jordparametrene fra mitt notat 13.06.2025 (sand φ = 33°, γ = 17 kN/m³) bekreftes skriftlig av geotekniker, basert på data fra prøvegraving i Fase 5A eller enkel CPT/vingeboretesting. Dette er et krav fra meg for å ferdigstille armeringstegning for yttervegger.

3. **SB-godkjenning for betong — avklares og navngis i v02.** Det skal stå én person eller ett firma med navn og SB-godkjenningsnummer for betongarbeider utførelsesklasse 2 og 3, med angivelse av hvilke faser vedkommende dekker.

4. **STØTTE+KUT-gate: faglig tilstedeværelse under kutting.** Legg til krav i F3.8 om at en faglig ansvarlig person (byggeleder-kompetanse) er til stede og signerer dagsrapporten for STØTTE+KUT-elementer.

5. **Separasjonssjikt-monteringsanvisning.** PGL skriver en kort anvisning (maks 1 side) for festing av XPS + plast/duk mot natursteinsmur uten borring. Refereres i F8.3.

6. **Herdelogg som krav.** Legg til i F7.21 og F6.14: termometer i betongen, resultater sendes RIB som del av gate-dokumentasjonen.

7. **Betongprøver til akkreditert laboratorium.** Presiser i F6.13, F7.19, F8.16 at sylindre sendes til akkreditert lab, ikke til lokal kvalitetsvurdering. Resultatene er del av sluttdokumentasjonen til kommunen.

8. **Svelleprofil — monteringstidspunkt og beskyttelse mot fukt-aktivering.** Legg til i F7.8 og tilsvarende for F8: monteres tidligst 48 timer før støp, beskyttes mot fukt med fugeblikk, dokumenteres med foto av montert og intakt svelleprofil rett før betongen stiller.

9. **Katodisk mandat — utvidelse.** I F11.2, presiser at spesialist vurderer *både* eksponert stål *og* innstøpt armering i XS3-eksponert betong. Oppgi at min gjennomgang (F11.4) inkluderer kontroll av at begge temaer er adressert.

10. **F6.2: graveavstand fra eksisterende søylefot.** Legg til i F6.2: «Graving nærmere enn 50 cm fra eksisterende søylefot skjer kun etter at RIB har angitt tillatt graveprofil per søyle, dokumentert skriftlig».

11. **Bekreft eksponeringsklasse for delevegger.** QA-funn 7 og 8 (betongklasse delevegger) må lukkes av RIB og HRP i fellesskap. Delevegger i kjeller i marint miljø er ikke trivielt XC1 (innvendig tørt) — kjellermiljøet er fuktig. Dersom kjelleren er konstruert for marint miljø med XS3 på yttervegger, er det ikke åpenbart at delevegger kan klassifiseres lavere enn XC3 eller XC4. Jeg vil se RHPs begrunnelse for XC1 og ta stilling til det.

---

## Modell B — er den signerbar?

**Mitt standpunkt:** Modell B som *prinsipp* er signerbar for F0–F5 og F10–F12 uten store betenkeligheter. Det er arbeidsoperasjoner der egne folks kompetanse er tilstrekkelig (dokumentasjon, rydding, graving, overflatebearbeiding, sluttdokumentasjon).

For **F6–F9 (fundamenter, bunnplate, yttervegger, delevegger)** er Modell B *ikke* signerbar i den formen den har i v01, av tre grunner:

1. Ingen navngitt SB-godkjent for betong.
2. Ingen klar grense for når utførelses-gate er møtt (betongbas ≠ SB-godkjent).
3. Ingen protokoll for hva som skjer dersom SB-godkjent ikke er til stede og noe avviker fra tegning under støp.

Hvis disse tre punktene lukkes — SB-godkjent navngitt, til stede under alle kritiske støpeoperasjoner, og protokoll for avvik — er Modell B signerbar av meg også for F6–F9. Det er byggherre som må ta stilling til om kostnadsbesparelsen ved Modell B er reell nok til å forsvare koordineringskostnaden dette krever.

---

*Ole Stenmo\
Sivilingeniørene Harboe og Leganger AS\
firmapost@h-l.no — +47 73 99 28 30*\
*Dette notatet er intern faglig vurdering til intern gjennomgang. Det erstatter ikke formell RIB-signering på produksjonstegninger.*
