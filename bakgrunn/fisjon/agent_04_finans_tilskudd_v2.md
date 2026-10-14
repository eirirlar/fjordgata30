# Agent 4 — Finans- og tilskuddsanalyst — v2

**Dato:** 2026-10-12\
**Rolle:** Konkret åpningsbalanse-utkast, oppdatert bank- og pantsituasjon, konsernlån-fordeling, MVA-strategi med konkrete tall, framførbart underskudd, tingsinnskudd fra nye aksjonærer, og framdriftsanbefalinger for tilskudd.\
**Scope:** Analyse-only. Lovreferanser [verifiseres fase 10] med unntak av mval. kap. 9 (Agent 1 laster denne i sin helhet).\
**Grunnlag:** v1-leveransen, `review_01.md`, `bruker_input_01.md`, Skatteetatens veiledende svar 11.09.2026, balanse 08.10.2026 (`bakgrunn/okonomi/`), skatteetat-korrespondanse (`bakgrunn/2026-08-25_skatteetaten_korrespondanse_2023_2026.md`).

v2 bygger videre på v1 — vesentlige antagelser i v1 er korrigert mot faktiske tall. v1-strukturen (tilsagnsbrev-analyse, byggesak, Riksantikvar, MVA-driftsmodell, framtidige søknader, framdriftsrapporter) står. v2 fokuserer der v1 var antakelsesbasert eller feilaktig.

---

## 1. Oppdatert bank- og pantsituasjon (korrigering fra v1)

### 1.1 Faktum per 08.10.2026

v1 antok at pantelånet 15,5 MNOK var en heftelse på Fjordgata 30. **Dette var feil.** De faktiske forholdene er:

- **DNB-lån 8210.58.15383**, saldo 15 233 691 kr per 08.10.2026, med beregnede renter 831 546 kr YTD (konto 2222). Pantesikkerheten er **Grønnegata 10**, ikke Fjordgata 30.
- **Fjordgata 30 er ubelastet.** Ingen pant per 08.10.2026 ifølge regnskapet. Dette er en vesentlig gevinst for fisjonen fra bankperspektiv: Fjordgata 30 kan overføres til et nytt selskap uten at panthaveren involveres i FG30-sporet.
- **DNB er bekreftet samarbeidspartner** på overføring. Brukeren har allerede snakket med DNB om å flytte lånet til nytt selskap (Grønnegata 10 AS). Overføringsklausul-problematikken fra v1 seksjon 4 bortfaller for Fjordgata 30 og håndteres som en isolert transaksjon i Grønnegata 10-sporet.

### 1.2 DNB — overføring av lån og pant til Grønnegata 10 AS

Fisjonens hjemmelsovergang Grønnegata 10 → Grønnegata 10 AS krever to parallelle grep:

1. **DNBs skriftlige samtykke til debitorbyttet.** Standard låneavtaler har klausul om endring i låntakers rettslige status eller eierskifte som utløser samtykkeplikt. DNB har signalisert vilje, men samtykket må være skriftlig og dekke både hjemmelsovergang og debitorbyttet. Praktisk form: tillegg til låneavtale eller nytt gjeldsbrev.
2. **Revidert lånevilkårsavtale.** Trolig vil DNB bruke anledningen til å reforhandle rentemargin, sikkerhetsstillelse (nytt pantedokument tinglyst med Grønnegata 10 AS som pantsetter), og eventuelle covenants (f.eks. kontantstrøm- eller egenkapitalkrav). Prisene i markedet pr. 2026 ligger typisk 100–200 bp over 3M NIBOR for næringsutleie med stabile leietakere. Hvis DNB tilbyr samme eller bedre vilkår enn eksisterende lån, er dette uproblematisk. Hvis vilkår skjerpes, må merkostnaden budsjetteres hos Grønnegata 10 AS.
3. **Dokumentavgift-fritak** for hjemmelsovergang ved fisjon (dokumentavgiftsloven § 7 [verifiseres fase 10]) gjelder begge eiendommene. Nytt pantedokument skal utstedes med Grønnegata 10 AS som pantsetter — dette er en separat tinglysning som påløper tinglysningsgebyr men ikke dokumentavgift.

### 1.3 FG30 AS — ingen pant, framtidig bankfinansiering er separat spor

Fjordgata 30 AS vil trenge **byggelån ca. 13–30 MNOK** basert på forretningsplanens kostnadsestimater (byggebudsjett ca. 30 MNOK ekskl. MVA, se seksjon 5). Dette er et separat finansieringsspor som ikke er forutsetning for fisjonsgjennomføring:

- Fisjonen gjennomføres med Fjordgata 30 som rent aktivum i FG30 AS (ingen pant, ingen eksisterende banklån).
- Byggelån-sondering starter etter at MVA-registrering er på plass i FG30 AS og tilskudds-overføring er godkjent — fisjonsgevinsten (ren åpningsbalanse, bekreftet MVA-strategi, 2,25 MNOK tilsagn flyttet over) styrker byggelånssøknaden.
- Brukerens bruk av DNB som bank gir ikke lock-in — FG30 AS kan sondere flere banker (SpareBank 1 SMN, Sparebanken Møre, Nordea) og grønt lån-ordninger uavhengig av DNB-relasjonen i Grønnegata-sporet.

### 1.4 Oppsummerende tabell — pant og bank

| Eiendom | Pant per 08.10.2026 | Bank | Overføringsmetode | Risiko |
|---|---|---|---|---|
| Fjordgata 30 (gnr/bnr 401/149) | Ingen | – | Fisjonsgjennomføring med fritak for dokumentavgift | Lav — ingen tredjepart involvert |
| Grønnegata 10 | DNB-lån 15,2 MNOK + beregnede renter 0,8 MNOK | DNB | Hjemmelsovergang + debitorbytte + nytt pantedokument i Grønnegata 10 AS | Moderat — avhengig av DNBs vilkår for debitorbyttet, men DNB har signalisert vilje |

**Konsekvens for prosjektleder- og fisjonsjurist-sporet.** v1s observasjoner i seksjon 4 (varsling av bank før fisjonsvedtak, formell samtykkedokumentasjon, fersk grunnboksutskrift) står fortsatt — men gjelder kun Grønnegata-sporet.

---

## 2. Åpningsbalanse-utkast — tre selskaper

Dette er v2s signatur-leveranse. Utkastet bygger på balanse 08.10.2026 og forutsetter at fisjonen gjennomføres rett etter. Åpningsbalansene i hvert selskap må justeres etter faktisk gjennomføringsdato, men proporsjoner og struktur holder.

### 2.1 Utgangspunkt — balanse 08.10.2026 for KodeWorks Eiendom AS

**Eiendeler (anleggsmidler og omløpsmidler):**

| Konto | Navn | Verdi (kr) |
|---|---|---:|
| 1160 | Fjordgt. 30 bygg | 7 333 401 |
| 1172 | Renovering Fjordgata 30 | 817 151 |
| 1164 | Grønnegata 10 bygg | 16 822 620 |
| 1167 | Grønnegata 10 fast teknisk installasjon | 1 329 633 |
| 1250 | Pinball-maskin | 17 703 |
| 1251 | Møbler/inventar Grønnegata 10 | 207 424 |
| 1260 | Fast bygningsinventar Grønnegata 10 | 318 409 |
| 1299 | Kalkulatoriske avskrivninger (akk. 2026) | –651 438 |
| 1396 | Depositum | 24 000 |
| 1500 | Kundefordringer | 27 000 |
| 1580 | Avsetning tap på kundefordringer | –29 900 |
| 1921 | Bankinnskudd DNB | 705 655 |
| **Sum eiendeler** | | **26 921 658** |

**Egenkapital og gjeld:**

| Konto | Navn | Verdi (kr) |
|---|---|---:|
| 2000 | Aksjekapital | –30 000 |
| 2030 | Annen innskutt egenkapital | –43 836 |
| 2050 | Annen egenkapital | –26 164 |
| 2221 | Lån DNB 8210.58.15383 | –15 233 691 |
| 2222 | Beregnet renter lån DNB | –831 546 |
| 2400 | Leverandørgjeld | –487 947 |
| 2600 | Forskuddstrekk/skyldig arbeidsgiveravgift/feriepenger (samlet 2600–2940) | ca. –34 000 |
| 2700/2710 | MVA utgående/inngående — netto | ca. –66 000 |
| 2900 | Forskudd fra kunder | –101 000 |
| 2923 | Gjeld KodeWorks AS (konsernlån) | –10 603 122 |
| 2950 | Påløpt rente konsernlån | –88 932 |
| **Sum egenkapital og gjeld** | | **–27 546 238** |

Balansen er avstemt i regnskapet. Egenkapitalen er bokført tynn (minus 100 000 i bokført EK før årets resultat), men driftsresultatet YTD gir en negativ bunnlinje som belaster EK ytterligere. Pr. 08.10.2026 er den bokførte egenkapitalen reelt negativ dersom årets resultat innarbeides — dette er en forsvarlighetsvurdering som revisor må gjøre (aksjeloven § 3-4 og § 3-5 [verifiseres fase 10]).

**Note om tvangsmulkt.** Påløpt tvangsmulkt kr 184 000 (bero-saken) er ikke avsatt i det bokførte regnskapet. Dette er en bestridt forpliktelse og regnskapsmessig behandles den som usikker (noteopplysning), ikke avsetning. Hvis klagen tapes, må forpliktelsen avsettes. For fisjonsplanen plasseres den eksplisitt hos fortsettende KWE (Alt 1A fra Agent 3).

### 2.2 Åpningsbalanse — Fortsettende KodeWorks Eiendom AS (holding)

Formål etter fisjon: konsernholding uten operasjonell virksomhet. Må ha dekning for tvangsmulktforpliktelsen og eventuell etterfølgende innkreving.

**Eiendeler:**

| Post | Verdi (kr) | Kommentar |
|---|---:|---|
| Bankinnskudd (andel) | 150 000 | Holdes tilbake for drift og eventuell dekning av påløpt tvangsmulkt |
| Aksjer i FG30 AS | 30 000 | Aksjekapital-innskudd ved stiftelse via fisjon |
| Aksjer i Grønnegata 10 AS | 30 000 | Aksjekapital-innskudd ved stiftelse via fisjon |
| **Sum eiendeler** | **210 000** | |

**Egenkapital og gjeld:**

| Post | Verdi (kr) | Kommentar |
|---|---:|---|
| Aksjekapital | 30 000 | Beholdes uendret |
| Annen innskutt egenkapital | 43 836 | Beholdes |
| Annen egenkapital | 26 164 | Beholdes |
| Tvangsmulktforpliktelse (bestridt, noteopplyst) | – | Avsettes ikke før klagen er avgjort; ingen bokført verdi i åpningsbalansen |
| Andel konsernlån fra KodeWorks AS | 110 000 | Residual |
| **Sum egenkapital og gjeld** | **210 000** | |

**Observasjon:** Fortsettende KWE blir et tomt holdingselskap med ca. 100 000 i bokført EK og 110 000 i konsernlån. Dette er en strukturelt sårbar konstruksjon — enhver materiell etterfølgende innkreving (f.eks. tvangsmulkt som tapt i klage) må enten dekkes av konsernet, av aksjonærinnskudd, eller føre til konkurs.

**Alternativ 1A fra Agent 3 forutsetter at fortsettende KWE har reell dekning for den plasserte forpliktelsen.** Med denne åpningsbalansen er dekningen svak. Tre praktiske grep for å forsterke:

1. **Hold konsernfordring eller andre inntektsgivende aktiva i fortsettende KWE.** Hvis mellomregning Kodeworks Drift AS gjenoppstår, eller konsernintern fordring etableres som del av fisjonen, kan dekningen forsterkes uten at Grønnegata 10 trekkes inn.
2. **Bruk Grønnegata 10 AS som nedbetalings-engine.** Grønnegata-driften gir avgiftspliktig salg (del av 8,74 MNOK YTD) og dermed kontantstrøm som over tid kan tilbakeføres til morselskap via konsernbidrag eller utbytte. Men dette krever framtidige disposisjoner og hjelper ikke dekningsgrunnlaget i selve åpningsbalansen.
3. **Aksjonærinnskudd eller konsernbidrag fra KodeWorks AS (morselskapet)** på fisjonstidspunktet, hvis morselskapet har kapasitet. Dette krever morselskapets vilje og regulering.

**Flagget til Agent 1 og Agent 3.** Alt 1As robusthet er avhengig av at dekningen bygges opp i løpet av fisjonsplanen, ikke bare at tvangsmulkten plasseres der. Dette er ikke løst med bokførte tall per 08.10.2026.

### 2.3 Åpningsbalanse — Fjordgata 30 AS

Formål etter fisjon: minilager-drift. Opprinnelig heleid datter av KodeWorks AS (via fisjonsgjennomføring), senere emisjon mot tingsinnskudd fra nye aksjonærer (se seksjon 7).

**Eiendeler:**

| Post | Verdi (kr) | Kommentar |
|---|---:|---|
| 1160 Fjordgt. 30 bygg | 7 333 401 | Overføres med skattemessig kontinuitet (sktl. § 11-7) |
| 1172 Renovering Fjordgata 30 | 817 151 | Aktiverte påkostninger |
| 1250 Pinball-maskin | 17 703 | Hører operasjonelt hjemme på Fjordgata 30 |
| Fordring på KMF-tilskudd 750 000 | 0 | **Ikke bokført som fordring** — tilsagnet er bindende men utbetales etterskuddsvis mot dokumenterte kostnader. Regnskapsmessig oppføres først ved konkret utbetalingsgrunnlag |
| Fordring på BYA 500 000 | 0 | Samme logikk som KMF |
| Fordring på UNI 100 000 | 0 | Samme logikk |
| Fordring på Enova KL 400 000 | 320 000 | 80 % kan anmodes utbetalt mot sluttrapport (ferdig siden mai 2026). Regnskapsmessig kan dette oppføres som fordring hvis anmodning sendes før fisjon |
| Fordring på Enova OM 500 000 | 0 | Prosjektet ikke avsluttet; ingen bokført fordring |
| Bankinnskudd (andel) | 400 000 | Opprinnelig arbeidskapital for drift |
| **Sum eiendeler bokført** | **8 888 255** | Pluss 320 000 kr Enova KL-fordring hvis utbetaling anmodes før fisjon, slik at fordringen er aktivert |

**Egenkapital og gjeld:**

| Post | Verdi (kr) | Kommentar |
|---|---:|---|
| Aksjekapital | 30 000 | Minimum etter aksjeloven § 3-1 [verifiseres fase 10] |
| Overkurs / annen innskutt EK | Residual | Må settes slik at egenkapitalen er forsvarlig (asl. § 3-4) |
| Andel konsernlån fra KodeWorks AS | 2 500 000 | Fordeling som drøftet i seksjon 3 under — foreløpig forslag |
| Leverandørgjeld relatert til FG30 | 150 000 | Andel av totalt 487 947, basert på leverandører som har levert tjenester til Fjordgata 30 (må gjennomgås faktura for faktura) |
| **Sum egenkapital og gjeld** | **8 888 255 (med 320 000 Enova KL)** | |

**Residual egenkapital:** 8 888 255 – 2 500 000 (konsernlån) – 150 000 (lev.gjeld) – 30 000 (aksjekapital) ≈ **6 208 255 kr annen innskutt egenkapital.**

Dette gir FG30 AS en bokført egenkapital på ca. 6,24 MNOK ved fisjonsgjennomføring, forutsatt at Enova KL-anmodning er aktivert og at konsernlån-fordelingen følger forslaget. Dette er en forsvarlig egenkapital for et minilager-selskap uten pant og med byggebudsjett 30 MNOK — selv om det ikke er stort nok til å finansiere byggefasen uten ekstern finansiering.

**Observasjon:** FG30 AS fremstår som det «ryddige» selskapet i trippel-utfisjoneringen. Dette er heldig for bank, tilskuddsgivere og framtidige nye aksjonærer. **Men** egenkapital-residualen er direkte avhengig av fordelingsnøkkelen for konsernlånet (seksjon 3) — jo mer konsernlån som plasseres i FG30 AS, desto svakere egenkapital.

### 2.4 Åpningsbalanse — Grønnegata 10 AS

Formål etter fisjon: eier og driver kontoreiendom.

**Eiendeler:**

| Post | Verdi (kr) | Kommentar |
|---|---:|---|
| 1164 Grønnegata 10 bygg | 16 822 620 | |
| 1167 Grønnegata 10 fast teknisk installasjon | 1 329 633 | |
| 1251 Møbler, inventar, Grønnegata 10 | 207 424 | |
| 1260 Fast bygningsinventar, Grønnegata 10 | 318 409 | |
| 1299 Kalkulatoriske avskrivninger akk. (Grønnegata-andel) | –651 438 | **Hele kalkulatoriske avskrivninger henføres til Grønnegata-eiendelene** — bygget er fullt utleid og i drift. Fjordgata 30 har ikke avskrivninger (bygget er under rehabilitering). Verifiseres med revisor |
| Kundefordringer relatert til kontorleietakere | 27 000 | Hele konto 1500 antas tilknyttet Grønnegata-utleien |
| 1580 Avsetning tap på kundefordringer | –29 900 | |
| 1396 Depositum | 24 000 | Depositum knyttet til Grønnegata-driften (må verifiseres) |
| Bankinnskudd (andel) | 155 655 | Residual av 705 655 etter at FG30 AS har fått 400 000 og fortsettende KWE 150 000 |
| **Sum eiendeler** | **18 203 403** | |

**Egenkapital og gjeld:**

| Post | Verdi (kr) | Kommentar |
|---|---:|---|
| Aksjekapital | 30 000 | Minimum |
| 2221 Lån DNB | 15 233 691 | Hele DNB-lånet |
| 2222 Beregnet renter lån DNB | 831 546 | |
| 2900 Forskudd fra kunder | 101 000 | Antas å gjelde forskudd fra kontorleietakere (kontoens motpart er konto 3690 «Forskuddsfakturert leie») |
| Leverandørgjeld relatert til Grønnegata | 337 947 | Resterende leverandørgjeld etter at 150 000 er henført til FG30 |
| Diverse arbeidsgiveravgift/feriepenger (operasjonelt) | 34 000 | Driftsrelatert — plasseres hos det selskap som overtar driften |
| MVA-oppgjør netto | 66 000 | Hele MVA-saldoen antas tilknyttet Grønnegata-driften |
| Andel konsernlån fra KodeWorks AS | 1 500 000 | Fordeling som drøftet i seksjon 3 |
| Overkurs / annen innskutt EK (residual) | 69 219 | |
| **Sum egenkapital og gjeld** | **18 203 403** | |

**Residual egenkapital:** 30 000 (aksjekapital) + 69 219 (annen innskutt) ≈ **99 000 kr samlet bokført egenkapital.**

**Observasjon:** Grønnegata 10 AS har en bokført egenkapital nær null etter at DNB-lånet er fullt overført. Dette er regnskapsmessig tynt men ikke underkapitalisert hvis man vektlegger at:

- Grønnegata-eiendommens virkelige markedsverdi antas å ligge over bokført (kjøpt 2020 for 14,1 + 5,5 = 19,6 MNOK; bokført 18,7 MNOK før avskrivninger).
- Kontordriften genererer kontantstrøm — i 2025 var samlet avgiftspliktig omsetning (3000) 2,21 MNOK pluss forskuddsfakturert leie, og driften er stabil.
- EBITDA fra Grønnegata-driften (eks. renter og avskrivninger) kan dekke renter og avdrag på DNB-lånet.

**Flagget til revisor:** vurdere om det kreves tilført frisk EK (f.eks. aksjonærinnskudd fra KodeWorks AS) i Grønnegata 10 AS for å få revisorbekreftelse etter asl. § 2-6 og § 14-3 [verifiseres fase 10]. Dette er en konkret regnskapsmessig vurdering som avhenger av markedsvurdering av eiendommen (bruk av bokført vs. virkelig verdi).

### 2.5 Avskrivninger akkumulert (konto 1299)

Konto 1299 «Kalkulatoriske avskrivninger» har saldo –651 438 kr per 08.10.2026. Dette er kalkulatoriske skattemessige avskrivninger på eiendelene som er regnskapsført i 2026.

**Fordeling.** Avskrivningene fordeles mellom selskapene etter hvor eiendelene plasseres. Konkret: Fjordgata 30-bygget avskrives separat fra Grønnegata-bygget, og avskrivningssaldoene følger eiendelene.

**Verifisering mot revisor nødvendig.** Konto 1299 er aggregert — regnskapsfører må dekomponere mellom (a) avskrivninger på Fjordgt. 30 bygg (1160), (b) avskrivninger på Grønnegata-eiendelene (1164, 1167, 1251, 1260). Resultatregnskapet YTD viser 4 867 438 kr på konto 6000 «Avskrivning på bygninger og annen fast eiendom» — denne skal også fordeles.

**Antakelse i utkastet:** Siden Fjordgata 30 er under rehabilitering (ikke i drift før september–november 2027), antas kalkulatoriske avskrivninger å gjelde kun Grønnegata-eiendelene. Men dette er en antakelse som revisor må verifisere mot avskrivningsbilaget.

### 2.6 Oppsummerende sammenligning

| Post | KWE fortsettende | FG30 AS | Grønnegata 10 AS | Sum | Avstemming mot 08.10.2026 |
|---|---:|---:|---:|---:|---|
| Eiendeler | 210 000 | 8 568 255 (bokført før Enova KL-anmodning) | 18 203 403 | 26 981 658 | Avviker 60 000 fra 26 921 658 pga. 2x aksjekapitalinnskudd 30 000 i nystiftede selskaper — justeres mot egenkapital-residual |
| Gjeld (ekskl. EK) | 110 000 (konsernlån) | 2 650 000 | 18 104 184 | 20 864 184 | Vs. 27 546 238 – 100 000 (EK før fisjon) = 27 446 238 — avstemming må gjøres mot faktisk fordeling av leverandørgjeld, mva, arbeidsgiveravgift o.l. i detalj. Dette utkastet er et strukturforslag, ikke en avstemt balanse |
| Egenkapital | 100 000 | 5 918 255 (bokført før Enova KL-anmodning) | 99 219 | 6 117 474 | Må revideres når konto-fordelingen er endelig fastlagt |

**Totalkonsernverdi uendret.** Fisjonens kjennetegn er at konsernet samlet sett har samme bokførte verdier før og etter — det er bare fordelingen som endres. Åpningsbalansen må gi en avstemt eiendelsside = gjeldsside i hvert selskap, og summene må matche moderverdien per fisjonstidspunkt.

**Hovedsvakhet i utkastet:** Konsernlåns-fordeling (seksjon 3) er den enkeltvariabelen som dominerer egenkapital-residualen i hvert selskap. Fordelingen må besluttes før åpningsbalansene kan ferdigstilles.

---

## 3. Konsernlånet fra KodeWorks AS (10,6 MNOK) — fordeling

### 3.1 Status

Per 08.10.2026:

- Hovedstol: **10 603 122 kr** (konto 2923).
- Påløpt rente: **88 932 kr** (konto 2950).
- Rentekostnad YTD: **970 850 kr** (konto 8130). Rentesats implisert ca. 9,2 % årlig basert på gjennomsnittlig saldo — høyt, men ikke uvanlig for konsernintern finansiering.

**Historikk fra regnskap:**
- 31.12.2024: 11 740 737 kr
- 31.12.2025: 10 330 295 kr (nedbetalt 1,4 MNOK i 2025)
- 08.10.2026: 10 603 122 kr (opp 272 827 kr i 2026 — rente kapitalisert, ingen nedbetaling)

### 3.2 Konsekvens av fordeling

Hvis hele konsernlånet blir i fortsettende KWE: fortsettende blir illikvid fra start (ingen operasjonell virksomhet, 10,6 MNOK gjeld, nær null bokført EK). Alt 1A for tvangsmulkt-plassering (Agent 3) blir ikke lenger forsvarlig — fortsettende har ikke dekning for noe som helst.

Hvis hele konsernlånet fordeles mellom FG30 AS og Grønnegata 10 AS: fortsettende KWE blir et tomt holdingselskap, men med null operasjonell gjeld. Dette fjerner likviditets-overbelastning, men krever at kreditor (KodeWorks AS, morselskap) samtykker til gjeldsfordeling.

Hvis konsernlånet fordeles proporsjonalt etter eiendomsverdi: ca. 32 % FG30 (bokført 8,15 MNOK) + ca. 68 % Grønnegata (bokført 18,68 MNOK). Dette gir ca. 3,4 MNOK til FG30 AS og ca. 7,2 MNOK til Grønnegata 10 AS.

### 3.3 Konkret anbefaling — tredelt fordeling

**Forslag:**

| Selskap | Andel konsernlån (kr) | Begrunnelse |
|---|---:|---|
| Fortsettende KWE | 6 603 122 | Hovedandelen av konsernlånet beholdes hos fortsettende som en «indre fordring» mellom morselskapet KodeWorks AS og det tomme KWE-holdingselskapet. Siden kreditor er konsernintern, kan vilkårene reforhandles (lavere rente, betinget nedbetaling, konvertibelt osv.) uten eksternt godkjenningskrav |
| FG30 AS | 2 500 000 | Representerer en andel som FG30 AS bærer for byggerelaterte kostnader finansiert gjennom konsernet. Nedbetales via driftsinntekter og eventuelt byggelån |
| Grønnegata 10 AS | 1 500 000 | Komplementært beløp som dekker Grønnegata-relaterte påkostninger finansiert gjennom konsernet. Nedbetales via kontorutleieinntekter |

**Forutsetninger:**

1. **Kreditor (KodeWorks AS) må samtykke** til fordelingen. Dette er en konserninternaffære, og hvis morselskapets styre er enig med fisjonsplanen, er samtykket formalia.
2. **Vilkårene for det nye underlånet** mellom KodeWorks AS og hvert selskap må defineres: rentesats (anbefales lavere enn dagens 9,2 %, f.eks. markedsrente 5–6 % for å gi driftsmessig pusterom), løpetid, nedbetalingsplan.
3. **Dekningslovsvurdering** [verifiseres fase 10]: hvis konsernlånet overføres på vilkår som avviker fra det opprinnelige, kan det reises spørsmål om kreditorsvik eller omstøtelse. Fordelt proporsjonalt etter netto bokført verdi, og med vilkår som ikke er dårligere enn det opprinnelige, skal dette være i orden — men dette er juridisk Agent 1-vurdering.

### 3.4 Konsekvens for Alt 1A (fortsettende dekker tvangsmulkt)

Med forslaget over har fortsettende KWE:

- Aksjer i FG30 AS: 30 000 (bokført)
- Aksjer i Grønnegata 10 AS: 30 000 (bokført)
- Bankinnskudd: 150 000
- **Minus:** konsernlån 6 603 122 til KodeWorks AS

Netto bokført EK: ca. 100 000. Dekningen for en materiell tvangsmulkt (kr 184 000 påløpt, potensielt 500 000+ hvis klagen tapes og innkreving gjenoppstås med tilbakevirkende effekt) er dermed **ikke robust fra et bokført perspektiv**.

Reell dekning kan likevel være til stede dersom:

- Aksjene i FG30 AS og Grønnegata 10 AS har virkelig verdi over bokført — særlig FG30 AS vokser i verdi når byggefasen og MVA-strategien har effekt.
- KodeWorks AS (morselskap) stiller konsernintern garanti.

**Flagget til Agent 1 og Agent 3:** Alt 1A er plausibel men ikke risikofri gitt bokført EK i fortsettende. Alternativ 1B (plassere forpliktelsen hos FG30 AS, som har bedre bokført EK) kan være en strategisk reserve hvis Alt 1A viser seg juridisk sårbar.

---

## 4. Framførbart underskudd — fordeling og avskjæringsvurdering

### 4.1 Status

Skatteetatens varsel 13.07.2026 (jf. `bakgrunn/2026-08-25_skatteetaten_korrespondanse_2023_2026.md`):

- Fremført underskudd fra tidligere år: endret 2 830 173 → **2 462 256 kr** (inntektsår 2024).
- Underskudd til fremføring: endret 2 874 407 → 2 506 490 kr.
- Reduksjonen (kr 367 917) skyldes at ny skattemelding 2023 ikke ble innlevert og Skatteetaten endret inntekten med samme beløp.

Driftsresultat YTD 2026 viser betydelige kostnader (avskrivninger, renter) uten tilsvarende inntekter — framførbart underskudd forventes å vokse ytterligere ved årsavslutning 2026. Grovt estimat: dagens akkumulerte skattemessige underskudd ved utgangen av 2026 kan være i størrelsesorden **3,0–3,5 MNOK** når 2026-tapet legges til.

### 4.2 Fordeling ved fisjon

**Hovedregel (sktl. §§ 11-4 og 11-7) [verifiseres fase 10]:** Ved skattefri fisjon fordeles framførbare skatteposisjoner (herunder underskudd til fremføring) mellom overtakende og fortsettende selskaper **etter nettoverdien av eiendelene** som overføres til hvert selskap. Dette er standardfordelingen.

Netto bokført verdi tilført hvert selskap i forslaget:

- Fortsettende KWE: ca. 100 000
- FG30 AS: ca. 5,9 MNOK (bokført) — eller mer hvis Enova KL-fordringen aktiveres
- Grønnegata 10 AS: ca. 100 000 (bokført etter DNB-lån)

**Proporsjonal fordeling** gir dermed overveldende til FG30 AS — ca. 97 % av underskuddet. Men dette er basert på bokførte verdier; hvis virkelige verdier brukes (Grønnegata 10 har markedsverdi over bokført pga. 5,5 MNOK oppussing, og FG30 har framtidig verdi 53 MNOK i forretningsplanen), kan fordelingen endre seg vesentlig.

**Alternativ regel:** Ved fisjon kan skatteposisjonene plasseres **etter avtale** i fisjonsplanen, forutsatt at det ikke bryter med sktl. § 14-90 (avskjæring av underskudd ved transaksjoner som har som overveiende motiv å utnytte skatteposisjonen) [verifiseres fase 10].

### 4.3 Anbefaling

**Plasser framførbart underskudd i FG30 AS.** Begrunnelse:

1. **Driftsøkonomisk forventning:** FG30 AS vil ha skattepliktig overskudd fra lagringsdrift fra 2027–2028 (etter at bygget er i drift). Underskuddet kan motregnes mot framtidige overskudd og gir konkret skattebesparelse (22 % av 2,46 MNOK = ca. 541 000 kr).
2. **Grønnegata 10 AS har allerede overskuddskapasitet** fra kontordriften, men marginalt — DNB-renter og avskrivninger belaster bunnlinjen betydelig. Underskuddet gir mindre effekt der.
3. **Fortsettende KWE** vil ikke generere overskudd uten operasjonell virksomhet; underskuddet er verdiløst her.

### 4.4 Avskjæringsrisiko (sktl. § 14-90)

**Sktl. § 14-90** [verifiseres fase 10] gir Skatteetaten adgang til å avskjære framførbart underskudd dersom en transaksjon har som **overveiende motiv** å utnytte skatteposisjonen. For en fisjon må det kunne demonstreres reell forretningsmessig begrunnelse ut over skatteposisjonen.

For denne fisjonen er det reell forretningsmessig begrunnelse:

- **MVA-strategien** (seksjon 5) krever skille mellom lagringsvirksomheten og øvrig drift.
- **Risikoseparasjon** (brannsak, tvangsmulkt, pågående DSB-/Sivilombud-saker) krever skille mellom Grønnegata-driften og FG30-rehabiliteringen.
- **Nye aksjonærer** (Kristian Brandsegg, Ole Morten Lagmannssveen) skal inn i FG30 AS med tingsinnskudd (seksjon 7); dette krever at FG30 AS er et eget selskap.
- **Bankfinansiering** av byggefasen krever rent panteobjekt uten historiske forpliktelser.

**Vurdering:** Avskjæringsregelen er sannsynligvis ikke anvendelig så lenge disse begrunnelsene dokumenteres i fisjonsplanen og i fase-dokumentasjon. Men dette er Agent 1-vurdering i detalj. Finansielt sett er risikoen moderat men ikke høy.

### 4.5 Flagg til Agent 1

Hvis Skatteetaten vurderer fordelingen som skattemotivert, kan en konkret konsekvens være at **hele** underskuddet avskjæres — ikke bare den delen som er «overflyttet». Dette er et tap i størrelsesorden 500 000 kr i effektiv skattebesparelse (22 % x 2,46 MNOK). Grundig dokumentasjon av forretningsmessig begrunnelse er derfor viktig.

---

## 5. MVA-strategien — konkretisert med tall

### 5.1 Grunnlag

Skatteetatens veiledende svar 11.09.2026 (saksref. 2026/5205691) bekrefter:

- **Aktiv lagringstjeneste («valet storage», 70 % av lagringsenhetene — 335 av 478):** avgiftspliktig etter mval. § 3-1 første ledd. Full fradragsrett for inngående MVA på kostnader knyttet til dette segmentet.
- **Selvbetjent bodutleie B2B (30 % — 143 boder):** unntatt etter mval. § 3-11 første ledd. Næringsleietakere kan omfattes av frivillig registrering § 2-3 (gjelder for leietakere som selv er MVA-registrert i Merverdiavgiftsregisteret).
- Skatteetaten bemerker eksplisitt at BFU er unødvendig — regelverket er klart.

**Driftsmodell per søknad:**
- 335 valet-enheter (ca. 70 %) + 143 selvbetjente boder (ca. 30 %) = 478 lagringsenheter totalt (ca. 1 008 kvm)
- 193 kvm kontor i 1. etasje
- 152 kvm krypkjeller for båtutstyr

### 5.2 Tidspunkt for MVA-registrering

**Hovedregel:** FG30 AS skal MVA-registreres **etter fisjon**, slik at:

- Ingen justeringsforpliktelse etter mval. kap. 9 utløses i KWE (fordi KWE ikke blir MVA-registrert).
- Hele byggefasens inngående MVA kan kreves fradrag via **tilbakegående avgiftsoppgjør etter mval. § 8-6** [verifiseres fase 10 — unntatt: Agent 1 laster mval. kap. 9 og tilgrensende paragrafer per brukerinput].
- MVA-registreringen trer i kraft fra registreringsdato; tilbakegående oppgjør for kostnader påløpt opp til 3 år tilbake (ikke 6 måneder — dette er bruker-/Agent-oppfatning fra v1 som verifiseres i fase 10 mot mval. § 8-6).

**Tidslinje-logikk:**

1. Fisjon registrert i Enhetsregisteret.
2. FG30 AS stiftet som nytt selskap med Fjordgata 30 som aktivum.
3. Byggearbeid igangsettes (eller fortsetter) i FG30 AS.
4. MVA-registrering av FG30 AS: ordinær registrering § 2-1 for valet-storage-omsetningen når denne overstiger terskel (50 000 kr), eller frivillig registrering § 2-3 for næringsutleien til MVA-registrerte leietakere.
5. Tilbakegående avgiftsoppgjør aktiviseres: fradragsføring av inngående MVA på byggefasens kostnader inntil 3 år tilbake (ca. 25.10.2024 til og med registreringstidspunktet).

### 5.3 Fradragsnøkkel — hvor mye kan refunderes?

**Byggebudsjett per forretningsplan:** 30 MNOK ekskl. MVA. Dette gir inngående MVA på 7,5 MNOK (25 % av 30 MNOK).

**Fradragsrett er avhengig av arealfordeling og driftsformål:**

Arealoversikt per søknad til Skatteetaten:
- Lagringsenheter totalt: 1 008 kvm (74,5 % av 1 353 kvm total)
- Kontor: 193 kvm (14,3 %)
- Krypkjeller: 152 kvm (11,2 %)

**Fradragsnøkkel på lagringsarealet (1 008 kvm):**

- Valet storage (70 % av enhetene): avgiftspliktig § 3-1 — **full fradragsrett** → 70 % x 1 008 = 706 kvm med full fradrag.
- B2B-boder (30 %): unntatt § 3-11, men frivillig registrering § 2-3 for næringsleietakere → **fradragsrett avhengig av andel MVA-registrerte leietakere**. Konservativt antakes 50 % av bodene leies ut til MVA-registrerte foretak → 50 % x 30 % x 1 008 = 151 kvm med fradrag.

Lagringsareal med fradrag: ca. **857 kvm (85 % av lagringsarealet)**.

**Kontor (193 kvm):** forventet utleid til næringsdrivende som er MVA-registrert; omfattes av frivillig registrering § 2-3. **Full fradragsrett** på kontorets andel.

**Krypkjeller (152 kvm):** usikker klassifisering. Hvis det brukes til båtopplag eller lagring med aktiv tjenestekomponent (henting, oppsyn), omfattes det av oppbevaringstjenester § 3-1. Hvis det er ren bodutleie, § 3-11. For konservativ fradragsvurdering antas **halv fradragsrett** (76 kvm).

**Samlet fradragsareal:**
- 857 (lagring) + 193 (kontor) + 76 (krypkjeller) = **1 126 kvm** av 1 353 kvm total
- **Fradragsandel ca. 83 %** av arealet

**Estimert MVA-refusjon:**
- 83 % x 7,5 MNOK = **ca. 6,2 MNOK**

Dette er i tråd med brukerens tidligere estimat (5–6 MNOK). Hvis flere B2B-leietakere er MVA-registrerte enn de 50 % antatt, nærmer vi oss 7 MNOK. Hvis færre, synker vi mot 5 MNOK.

**Hovedusikkerhet:** faktisk MVA-status til framtidige B2B-leietakere på fisjonstidspunktet. Dette kan avklares først når reelle leietakere er signert, men det kan antas en fornuftig andel for budsjettformål.

### 5.4 Tilbakegående avgiftsoppgjør — kostnader påløpt før fisjon

**Mval. § 8-6** [verifiseres fase 10] gir mulighet for tilbakegående fradragsføring på kostnader påløpt opp til 3 år tilbake (ikke 6 måneder som v1 skrev — dette var feil og rettes i v2).

Dette er sentralt fordi FG30-prosjektet har pådratt kostnader fra 2024 og framover:

- 2024 akkumulert renovering: 0 (ikke aktivert i 2024-balansen)
- 2025 akkumulert renovering: 0 (aktivert pr. 31.12.2025 = 347 100 kr i 2026)
- 2026 YTD renovering: 817 151 kr på konto 1172

I tillegg kommer kostnader til brannkonsept, prosjektering (HRP), ansvarlig søker (SAHAA), energikartlegging (HRP) som er ført andre steder i regnskapet.

**Grovt estimat for inngående MVA påløpt 2024–2026 YTD:** basert på byggerelaterte kostnader ca. 1,0–1,5 MNOK ekskl. MVA (fra renovering, prosjektering, konsulenter) → inngående MVA 250–375 000 kr fradragsberettiget retroaktivt.

Hovedvolumet av byggebudsjettet (ca. 28 MNOK av 30 MNOK) påløper i 2027 — dette fradragsføres løpende etter at MVA-registreringen trer i kraft. Hvis MVA-registrering skjer i Q1 2027, får FG30 AS løpende fradragsrett for alt som faktureres fra dette tidspunktet.

### 5.5 Hvis MVA-registrering utsettes

Hvis fisjonen trekker ut i tid og byggearbeidet starter opp i FG30 AS før MVA-registrering er på plass:

- Fradragsretten for pågått inngående MVA kan fortsatt reddes gjennom tilbakegående oppgjør, forutsatt at 3-årsfristen holder.
- Men hvis bygget tas i bruk (ferdigstillelse) uten MVA-registrering, mister FG30 AS **sitt helhetlige fradragsgrunnlag** for den perioden. Dette er kritisk å unngå.

**Konkret anbefaling:** MVA-registrering senest 1–2 måneder før ibruktakelse. Forventet ibruktakelse september–november 2027 (per søknaden til Skatteetaten) → MVA-registrering senest Q2 2027. Dette gir rikelig med tid etter fisjon og uten press.

### 5.6 Konsekvens for åpningsbalansen

Åpningsbalansen for FG30 AS trenger **ikke** å ha egen MVA-fordring; dette oppstår først etter registrering. Men driftsforutsetningen om 6,2 MNOK MVA-refusjon må inngå i den finansielle planen som bank og framtidige nye aksjonærer vurderer.

---

## 6. Tilskudd og framtidige søknader — oppdatert prioritetsplan

### 6.1 Reviderte prioriteter

v1 seksjon 7 skisserte rekkefølgen; v2 reviderer med konkrete datoer og lav/høy prioritet:

| Nr. | Oppgave | Tidsramme | Prioritet | Begrunnelse |
|---|---|---|---|---|
| 1 | **Enova KL — anmod 80 % utbetaling (ca. 320 000 kr)** | Umiddelbart (okt 2026) | Høy | Sluttrapport ferdig siden 05.05.2026. Utbetaling fra KodeWorks Eiendom AS før fisjon forenkler. 20 % holdes tilbake til sluttrapport-vurdering (frist 25.12.2026). Dette er den eneste av de fem tilskuddene som kan generere kontantstrøm **nå** |
| 2 | **Enova OM — søk forutgående skriftlig samtykke til mottakerendring** | Nov–des 2026 | Høy | Enovas vilkårsdokument krever forutgående samtykke (OM-klausulen 3.2). Må være på plass før fisjonsgjennomføring. Enovas interne behandlingstid for selskapsrettslige endringer er ikke verifisert — anta 4–8 uker |
| 3 | **Enova KL sluttrapport** | Innen 25.12.2026 | Høy | Fra KodeWorks Eiendom AS hvis fisjonen ikke er gjennomført innen fristen. Alternativt fra FG30 AS etter mottakerendring |
| 4 | **Fisjonsvedtak og registrering** | Nov 2026 – Q1 2027 | Høy | Timing styres av Enova OM-samtykke og konkursvarsel-stabilisering (Agent 3 og Agent 1) |
| 5 | **KMF, BYA, UNI — melding om fisjon og anmodning om videreføring** | Umiddelbart etter fisjonsregistrering | Moderat | Skriftlig anmodning til hver tilskuddsgiver med redegjørelse. Lav risiko gitt godvilje etablert i tidligere korrespondanse |
| 6 | **Enova OM sluttrapport** | 25.02.2027 | Moderat | Fra FG30 AS hvis mottakerendring er godkjent; ellers fra fortsettende KWE. Prosjektets gjennomføring (mulighetsstudie ombruk) må være dokumentert |
| 7 | **Framtidige søknader (KMF 2/3, BYA 2/3, UNI 2, Enova Yrkesbygg, Trøndelag fylke, Riksantikvar håndverksopplæring, Skattefunn, Innovasjon Norge)** | Q1–Q4 2027 | Moderat–lav | Alle fra FG30 AS. Prioriteres etter søknadsfrister og driftsrelevans |
| 8 | **MVA-registrering FG30 AS** | Q1–Q2 2027 | Høy | Må skje før ibruktakelse. Tilbakegående oppgjør aktiveres samtidig |

### 6.2 Observasjoner

- **Enova KL er den enkeltposten som kan utbetales raskest.** 320 000 kr i løpet av Q4 2026 er en håndgripelig gevinst og bidrar til likviditet hos fortsettende KWE eller FG30 AS (avhengig av fisjonstiming).
- **KMF, BYA, UNI er «lagret kapital»** — ikke umiddelbart aktuelle for utbetaling (etterskuddsvis mot dokumenterte kostnader). Overføringsanmodning er administrativ.
- **Framtidige tilskudd (ca. 6,8–10,3 MNOK potensial per `bakgrunn/stotte/2026-06-26-fg30-stotte.md`)** forutsetter at fisjonen er gjennomført før søknadene sendes fra FG30 AS. Dette setter en «myk deadline» på fisjonen rundt årsskiftet.

### 6.3 Trøndelag fylke brannsikring — kritisk søknadsfrist

Trøndelag fylkes brannsikringstilskudd har søknadsfrist **1. november** (per `bakgrunn/stotte/2026-06-26-fg30-stotte.md`). Hvis fisjonen ikke er gjennomført innen da, må søknaden sendes fra KodeWorks Eiendom AS med klar presisering om framtidig overføring til FG30 AS.

**Anbefaling:** For Trøndelag-søknaden som løper i 2026, send fra KodeWorks Eiendom AS. Dette er en konkret unntakssituasjon fra regelen om «alt skal sendes fra FG30 AS etter fisjon» og tåler i dette tilfellet overføring etter faktureringssyklusen.

---

## 7. Nye aksjonærer med tingsinnskudd — Brandsegg og Lagmannssveen

### 7.1 Strukturering

Brukerinput seksjon 4 bekrefter at Kristian Brandsegg (KMTE, prosjektleder) og Ole Morten Lagmannssveen (HRP, PGL) skal inn som aksjonærer i FG30 AS med tingsinnskudd. Hovedsesjonens kortvurdering (brukerinput 4.3) anbefaler **fisjon først, deretter emisjon** — to separate transaksjoner, for å bevare skattemessig kontinuitet etter sktl. kap. 11.

Dette er riktig fra et skattejuridisk perspektiv og bekreftes finansielt av følgende:

**Hvis Brandsegg/Lagmannssveen tas inn som del av fisjonen:**
- Skattefri fisjon forutsetter identisk eierstruktur før og etter (sktl. § 11-7 [verifiseres fase 10]).
- Opptak av nye aksjonærer bryter kontinuiteten → fisjonen blir skattepliktig.
- Realisasjon av Fjordgata 30 utløser gevinstbeskatning. Hvis virkelig verdi ligger over bokført (bokført 8,15 MNOK; forretningsplan antar 53 MNOK ved ferdigstillelse — men dagens virkelige verdi er lavere), kan skattekonsekvensen bli materiell.

**Hvis emisjon kommer etter fisjon:**
- Skattefri fisjon beholdes.
- Emisjonen behandles separat: FG30 AS utsteder nye aksjer mot tingsinnskudd fra Brandsegg og Lagmannssveen. Ny aksjekapital og evt. overkurs beregnes basert på virkelig verdi av innskuddet.

### 7.2 Hva består tingsinnskuddet i?

Brukerinput åpner spørsmålet om hva tingsinnskuddet faktisk består i. Fra finansperspektiv er dette den avgjørende klassifikasjonen:

**Alternativ A — Fysiske eiendeler eller immaterielle verdier:**
- Verktøy, maskiner, software, patenter, kunderelasjoner, konsesjoner.
- Verdifastsettes etter markedsverdi.
- Krever revisorerklæring (asl. § 2-6 [verifiseres fase 10]) som bekrefter at verdien minst tilsvarer det som aksjene gir rett til.
- Rent regnskapsmessig: eiendelen aktiveres i FG30 AS, egenkapital økes tilsvarende.
- Ingen skattemessig problemstilling for innskyter (eventuell gevinst fra privat til selskap må vurderes individuelt, men normalt er dette uten direkte skatt).

**Alternativ B — Arbeidsinnskudd / arbeidsplikt:**
- Lovlighet: aksjeloven [verifiseres fase 10] krever at tingsinnskudd kan verdsettes økonomisk. **Arbeidsinnskudd er ikke anerkjent** som gyldig tingsinnskudd i norsk aksjelovgivning; aksjonæren må yte noe som har økonomisk verdi for selskapet (jf. prinsipp i aksjelovgivningen om kapitalbinding).
- Hvis «arbeidsinnskudd» tolkes som avstått krav på godtgjørelse for allerede utført arbeid (dvs. en bestående fordring Brandsegg/Lagmannssveen har mot FG30 AS eller morselskapet), kan dette eventuelt behandles som konvertering av fordring til aksjer (gjeldsemisjon). Men dette krever at fordringen allerede er dokumentert, bokført og fakturert.
- Hvis det tolkes som fremtidig arbeid (arbeidsplikt), er dette ikke tingsinnskudd — det må klassifiseres som arbeidsavtale, og aksjene kan ikke utstedes mot dette uten også å kreve ordinær lønn og skattetrekk.

**Alternativ C — Avkall på fordring:**
- Hvis Brandsegg/Lagmannssveen har pågått arbeid for prosjektet uten fullt oppgjør, og de avstår fra kravet mot å få aksjer, er dette gjeldskonvertering. Dette er tingsinnskudd i aksjelovens forstand og lovlig.
- Krever revisorerklæring og fakturadokumentasjon.

### 7.3 Praktisk anbefaling

**Spørsmål til bruker:**

1. Hva nøyaktig består Brandsegg og Lagmannssveen sine tingsinnskudd av? Fysisk utstyr, immaterielle verdier, eller gjeldskonvertering fra pågått prosjektarbeid?
2. Hvis det er arbeidsinnskudd / arbeidsplikt — er planen i realiteten å gi dem aksjer «mot framtidig arbeid» (ikke tingsinnskudd men lønn/opsjon), eller er det en konvertering av eksisterende krav (gyldig tingsinnskudd)?

### 7.4 Finansiell konsekvens for FG30 AS

**Positiv effekt på egenkapital:**
Hvis tingsinnskuddet verdifastsettes til f.eks. 2 MNOK (hver aksjonær bidrar med 1 MNOK), vokser FG30 AS' bokførte egenkapital til ca. 8,2 MNOK. Dette styrker bankforhandlings-posisjonen betydelig når byggelån skal sondes.

**Fordeling av eierskap:**
Hvis Brandsegg/Lagmannssveen skal eie f.eks. 10 % hver etter emisjon (20 % totalt), må aksjeemisjonen settes slik at deres innskudd + evt. overkurs matcher dette andelen av fullutvannet selskap. Dette er en forhandlingssak mellom aksjonærene.

**Risiko for omstøtelse (dekningsloven kap. 5) [verifiseres fase 10]:**
Hvis emisjonen skjer like etter fisjonen og innenfor omstøtelsesvinduet, kan kreditor hevde at fisjon + emisjon er én sammenhengende disposisjon designet for å trekke verdier ut av kreditorens dekning. Dette er særlig relevant hvis det er bestående krav mot morselskapet KodeWorks Eiendom AS på fisjonstidspunktet.

**Konkret:** Agent 1 bør vurdere om Brandsegg/Lagmannssveen-emisjonen bør utsettes til etter at omstøtelsesvinduet er passert — eller alternativt gjennomføres med særlige vilkår (f.eks. kontantinnskudd parallelt) for å nøytralisere dekningsrisiko-argumentet.

### 7.5 Skatt for innskytere

Dersom tingsinnskuddet er fysiske eiendeler, kan Brandsegg/Lagmannssveen ha skattepliktig gevinst/tap ved overføringen (sktl. § 10-30 ff. [verifiseres fase 10] — avhengig av eiendelstype). Dette er personlig skatt og må vurderes individuelt. Egne aksjer mottatt som vederlag teller som anskaffelseskost ved framtidig realisasjon.

Dette er en problemstilling for innskytere personlig, ikke for FG30 AS. Flagges likevel som del av helhetsvurderingen.

### 7.6 Aksjonæravtale

Når nye aksjonærer tas inn, må aksjonæravtale på plass **før emisjon** gjennomføres. Aksjonæravtalen regulerer bl.a.:

- Styresammensetning og stemmerett.
- Utbyttepolitikk.
- Forkjøpsrett ved salg av aksjer.
- Konkurranseklausul og non-compete.
- Exit-mekanisme (drag-along, tag-along, prisfastsettelse ved exit).
- Rettigheter ved ekstraordinære hendelser (konkurs hos én aksjonær, dødsfall, osv.).

Dette er dokumentasjonsjobb for Agent 2 (operativt) og juridisk gjennomgang for Agent 1.

---

## 8. Framførbart underskudd og MVA i et konsernperspektiv

### 8.1 Internprisingsforhold mellom KodeWorks AS, KWE og FG30 AS

Dagens struktur har konsernlån med 9,2 % effektiv rente mellom KodeWorks AS og KWE (seksjon 3.1). Ved fisjon fordeles dette lånet; vilkårene bør reforhandles samtidig:

**Internprising (sktl. § 13-1 [verifiseres fase 10]):** Konsernintern finansiering skal skje til armlengdes vilkår. 9,2 % er høyt sammenlignet med markedsrente for næringseiendom (3M NIBOR + 150–250 bp = ca. 6,5–7,5 % på fisjonstidspunktet). Et markant avvik kan Skatteetaten tolke som utnyttelse av skatteforhold.

**Konkret anbefaling:** Juster konsernlånsrenten ned til markedsrente ved fisjon, ca. 6 %. Dette:
- Reduserer renteutgift i FG30 AS → bedre bunnlinje → raskere opptjening av framførbart underskudd når det er fordelt dit.
- Reduserer renteutgift i Grønnegata 10 AS → bedre bunnlinje → styrker nedbetalingskapasitet.
- Fjerner internprisingsrisiko.

### 8.2 Fjordgata 30 AS som MVA-registrert selskap — konsernmessig gevinst

Når FG30 AS er MVA-registrert og refusjon på 6,2 MNOK gjennom byggefasen aktiviseres, oppstår en konsernintern kontantstrømgevinst som kan brukes til:

- Nedbetaling av konsernlån til KodeWorks AS.
- Styrking av arbeidskapital.
- Reduksjon av behov for ekstern byggelånfinansiering.

**Timing:** Første MVA-refusjon kommer typisk 1–2 måneder etter første MVA-melding (2-mnd terminer). Hvis MVA-registrering skjer Q2 2027 og byggearbeidet er aktivt, kan første refusjonstransaksjon ligge rundt sommeren/høsten 2027.

### 8.3 Konsekvens for bankfinansiering

Et MVA-registrert FG30 AS med sikker refusjonsrett og 2,25 MNOK i tilsagn er en bedre bankklient enn et usikkert selskap. Dette er ikke bare «bankpakka» — det er en reell drifts- og likviditetsgevinst som styrker FG30 AS' solvens.

---

## 9. Endringer fra v1

| v1-element | v2-endring | Begrunnelse |
|---|---|---|
| **Seksjon 4 (bank og pant):** v1 antok 15,5 MNOK pant på FG30 | Omskrevet: DNB-lånet er på Grønnegata 10. FG30 går ubelastet | Faktakorreksjon fra brukerinput Q6 |
| **Seksjon 5.2 (BFU-status):** v1 forutsatte BFU-prosess pågående | BFU bortfalt. Skatteetatens veiledende svar 11.09.2026 bekrefter strategien | Faktum fra brukerinput Q9 |
| **Seksjon 5.3 (betydning av veiledningssvar):** v1 var hypotetisk | Veiledningssvar foreligger. MVA-strategien bekreftet | Faktum fra brukerinput |
| **Seksjon 7 (framtidige søknader):** v1 var kvalitativ | v2 har konkret prioritet-tabell med datoer og estimater | Praktisk aktualisering |
| **Seksjon 8 (åpningsbalanse):** v1 hadde skisse uten tall | v2 har konkret åpningsbalanse-utkast for alle tre selskaper med reelle tall fra balanse 08.10.2026 | Faktagrunnlag fra brukerinput Q7 |
| **Seksjon 9 (timing-scenarier):** v1 drøftet tre scenarier | v2 ignorerer timing-vinkelen (ligger hos Agent 2); fokuserer på strukturforslag | Scope-prioritering |
| **Mval. § 8-6 — tilbakegående oppgjør:** v1 skrev «6 måneders frist» | v2 oppdaterer til **3 års frist** (standard forståelse av mval. § 8-6 [verifiseres fase 10]) | Standard forståelse av regelen; v1 var feil |
| **Nye seksjoner i v2:** konsernlån-fordeling (seksjon 3), framførbart underskudd (seksjon 4), tingsinnskudd (seksjon 7) | Alle nye | Prioritert i prompt |

---

## 10. Åpne spørsmål

1. **Konsernlån-samtykke fra KodeWorks AS.** Fisjonsplanen forutsetter at morselskapet KodeWorks AS samtykker til fordelingen av konsernlånet (seksjon 3.3). Kan dette tas for gitt siden brukeren kontrollerer begge selskapene, eller må det foreligge formell styrevedtak i KodeWorks AS?
2. **Konsernlåns-rente justering.** Skal rentesatsen reforhandles ned til markedsrente (ca. 6 %) ved fisjon? Dette er et skattejuridisk/forretningsmessig valg som interagerer med sktl. § 13-1 (internprising). Agent 1 bør drøfte.
3. **Tingsinnskudd-klassifikasjon.** Hva består Brandsegg og Lagmannssveen sine tingsinnskudd av? (Fysiske eiendeler / gjeldskonvertering / arbeidsplikt / annet?) Dette avgjør om det er lovlig tingsinnskudd, om det krever revisorerklæring, og hvilken skattemessig behandling det får.
4. **Kalkulatoriske avskrivninger (konto 1299) fordeling.** Må kundens regnskapsfører dekomponere konto 1299 (–651 438 kr) og konto 6000 (4 867 438 kr) mellom Fjordgata 30 og Grønnegata-eiendelene. Dette er et konkret spørsmål til regnskapsfører Heidi Venås Eggen.
5. **Dekomponering av konto 1500 (kundefordringer), 2400 (leverandørgjeld), 2700/2710 (MVA) og 2900 (forskudd fra kunder).** Hvilke poster hører hjemme hos FG30-sporet og hvilke hos Grønnegata-sporet? Må gjennomgås med regnskapsfører.
6. **Fradragsnøkkel på B2B-boder — faktisk MVA-status til leietakere.** Verifisering vil først være mulig når reelle leietakere er på plass. For åpningsbalanse-formål holder antakelsen 50 % MVA-registrerte leietakere.
7. **Enova OM-samtykke behandlingstid.** Hvor lang tid tar det Enova å gi forutgående samtykke til mottakerendring? Dette styrer tidligste fisjonstidspunkt. Dialog med Enova må åpnes.
8. **DNB-vilkår for debitorbyttet.** Hvilke nye lånevilkår krever DNB i forbindelse med at lånet flyttes til Grønnegata 10 AS? Rentesats, sikkerhetsstillelse, covenants?
9. **Enova KL — kan 80 % utbetales nå?** Praktisk forretningsgang med Enova må avklares; sluttrapport er klar men formalia må gjennomgås.
10. **Aksjonæravtale.** Hvilket oppdrag skal advokaten ha for utarbeidelse av aksjonæravtale når Brandsegg/Lagmannssveen tas inn? Dette er en jobb som er egne forhandlinger utover selve fisjonen.

---

## 11. Interaksjoner med andre agenter

- **Agent 1 (Fisjonsjurist):** Avhenger av (a) juridisk vurdering av konsernlåns-fordelingen og om kreditor-samtykke må være skriftlig, (b) rentejustering som del av fisjonsplanen og konsekvens for internprising (sktl. § 13-1), (c) framførbart underskudd og avskjæringsregelen sktl. § 14-90, (d) tingsinnskudd — klassifikasjon og juridisk form (asl. § 2-6, § 10-2 ff. [verifiseres fase 10]), (e) dekningslovsvurdering for sekvensen fisjon → emisjon og om nye aksjonærer bidrar til økt omstøtelsesrisiko, (f) mval. § 8-6 verifisering av 3-årsfristen.
- **Agent 2 (Prosjektleder):** Avhenger av (a) tidsplan for DNB-dialog og eventuell reforhandling av lånevilkår, (b) tidsplan for aksjonæravtale-utarbeidelse og emisjon, (c) regnskapsfører-oppdrag for dekomponering av balansekonti, (d) revisor-oppdrag for forsvarlighetsvurdering av egenkapital i hvert selskap, (e) prioritering av Enova KL-utbetaling i Q4 2026.
- **Agent 3 (Tvangsmulkt-strateg):** Avhenger av (a) om Alt 1A er robust gitt den tynne bokførte egenkapital i fortsettende KWE (seksjon 2.2) — vurder om Alt 1B (plassering hos FG30 AS) er mer forsvarlig gitt bokførte tall, (b) hvordan bero-saken samspiller med konsernlåns-vilkår og om påløpt tvangsmulkt bør avsettes før fisjonsplanen signeres.

---

*Agent 4 — v2 — ferdigstilt 2026-10-12.*
