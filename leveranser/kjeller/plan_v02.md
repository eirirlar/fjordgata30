---
dokumenttype: prosjektert kjellerplan (operativ arbeidsbeskrivelse + tilbudsunderlag)
versjon: v02 — konsolidert etter seks rolle-reviews av v01
dato: 2026-10-21
byggherre: KodeWorks Eiendom AS (org.nr. 920 478 506)
prosjektleder antikvarisk (PGL): Ole Morten Lagmannssveen, HRP AS
koordinator utførelse: Kristian Brandsegg, KMTE
arkitekt: Adnan, HRP AS
RIB: Ole Stenmo, Sivilingeniørene Harboe og Leganger AS
status: andre utkast — klar for byggherres beslutning og neste byggesakssteg; ikke sendt entreprenør eller myndigheter
baserer seg på: plan_v01.md (førsteutkast), seks reviews i leveranser/kjeller/review_v01/ (ain.md, kristian.md, ole_morten.md, adnan.md, ole_stenmo.md, sobstad.md)
---

# Prosjektert kjellerplan — Fjordgata 30 Minilager

**Versjon v02 — konsolidert etter seks rolle-reviews**\
Dato: 21.10.2026

---

## Innhold

1. [Forord, lesemåte og endringer fra v01](#1-forord-lesemåte-og-endringer-fra-v01)
2. [Prosjektrammer](#2-prosjektrammer)
3. [Utførelsesmodeller — A, B og C re-tegnet per fase](#3-utførelsesmodeller--a-b-og-c-re-tegnet-per-fase)
4. [Byggesak — tre løp og ansvarsrett](#4-byggesak--tre-løp-og-ansvarsrett)
5. [Koordineringsmatrise — bestillinger og ansvar](#5-koordineringsmatrise--bestillinger-og-ansvar)
6. [HMS og SJA — navngitt ansvar per fase](#6-hms-og-sja--navngitt-ansvar-per-fase)
7. [Arkitektur — det som bygges, ikke bare det som støpes](#7-arkitektur--det-som-bygges-ikke-bare-det-som-støpes)
8. [Pre-F6: Armeringstegninger som egen flaskehals](#8-pre-f6-armeringstegninger-som-egen-flaskehals)
9. [Faser i rekkefølge — bakeoppskrift-formatet](#9-faser-i-rekkefølge--bakeoppskrift-formatet)
10. [Risikoregister](#10-risikoregister)
11. [Materialflyt og logistikk](#11-materialflyt-og-logistikk)
12. [Rekkefølgediagram og grov Gantt](#12-rekkefølgediagram-og-grov-gantt)
13. [Grensesnitt plan ↔ ISY — operasjonalisert](#13-grensesnitt-plan--isy--operasjonalisert)
14. [Figur-sammenstilling](#14-figur-sammenstilling)
15. [Åpne spørsmål og neste skritt](#15-åpne-spørsmål-og-neste-skritt)
16. [Appendiks A — Reviewmatrise](#16-appendiks-a--reviewmatrise)
17. [Appendiks B — Endringslogg v01 → v02](#17-appendiks-b--endringslogg-v01--v02)

---

## 1. Forord, lesemåte og endringer fra v01

### 1.1 Hva v02 er

Dokumentet er en konsolidert revisjon av plan v01 (21.10.2026) etter seks rolle-reviews fra utførende (Ain), koordinator (Kristian), PGL (Ole Morten), arkitekt (Adnan), RIB (Ole Stenmo) og tilbudsgivende entreprenør (Søbstad). Reviewene identifiserte til sammen ca. 70 konkrete endringspunkter. Hver av disse er behandlet i Appendiks A (reviewmatrisen) og markert som **innarbeidet**, **avventer** eller **avvist** med begrunnelse.

Dokumentet er skrevet som selvstendig lesbart — det forutsetter ikke at leser har lest v01. Der v01-tekst er beholdt uendret er den gjengitt verbatim slik at planen ikke må leses i to omganger.

### 1.2 Mottakergrupper

Tre grupper leser dette dokumentet samtidig:

- **Byggherres egne folk** (koordinator Kristian Brandsegg, Ain Hansumae, eventuelle studenter) som skal utføre eller koordinere arbeid i kjelleren.
- **Betongentreprenør og underentreprenører** som skal prise og signere som ansvarlig utførende på kritiske operasjoner (bunnplate, vanntette vegger, fundamenter under vann, katodisk anlegg).
- **RIB, PGL, Byantikvar, Riksantikvar, Trondheim kommune byggesak og tilskuddsgivere** (KMF, Enova) som gjennomgår og godkjenner at prinsippene, rekkefølgen og dokumentasjonen holder mål.

Oppskriften er bevisst skrevet i bakeoppskrift-formatet med små, nummererte steg. Ambisjonen er at en voksen person uten betongutdanning skal kunne lese planen og forstå rekkefølgen, forutsetningene og hva som skal skje i hvert enkelt steg. Spesialistoperasjoner er merket `[KREVER PROFF]` med leveringstid og indikativ timesats.

### 1.3 Hvordan planen brukes

**Lineært.** Fasene (F0–F12) utføres i rekkefølge. Noen aktiviteter innen samme fase går parallelt, og noen myndighetsavklaringer (dispensasjon § 8, NVE, RIB-tegninger) kan prosjekteres parallelt med fysisk arbeid lenger ned i rekkefølgen.

**Gates.** Mellom og innenfor faser finnes **gates** — punkter der arbeidet ikke kan fortsette uten en bestemt skriftlig godkjenning. Fire typer:

- **RIB-gate (RG-x):** Ole Stenmo (Harboe og Leganger AS) godkjenner skriftlig før kutting, armering eller støping starter.
- **Arkeolog-gate (AG-x):** Riksantikvaren eller Trøndelag fylkeskommune (NIKU-tilrådning) må gi dispensasjon etter kulturminneloven § 8 før graving i uomrørte masser.
- **Myndighets-gate (MG-x):** Trondheim kommune byggesak (rammetillatelse, IG), NVE (vassdragsmyndighet), Statsforvalter (naturmangfold), Trondheim havn (grunneier/vektrestriksjon), Byantikvar (bevaringskonsultasjon).
- **Utførelses-gate (UG-x):** SB-godkjent betongfagperson er fysisk til stede og signerer før og under kritiske støpeoperasjoner. **Dette er ny i v02** (fra Stenmos review).

### 1.4 Hard-coded vs. soft

**Hard-coded — tallfestede krav som ikke kan endres uten ny RIB-vurdering:**

| Parameter | Verdi | Kilde |
|---|---|---|
| Dimensjonerende vannstand (poretrykk) | kote +3,20 | RIB-notat 10.02.2026 |
| Nyttelast plan –1 og 1, karakteristisk | 7,5 kN/m² | RIB-notat 10.02.2026 |
| Dimensjonerende nyttelast plan –1 og 1 (LF 1,5) | 11,25 kN/m² | Stenmo review (presisering) |
| Brannkrav bæring | R60 | RIB-notat 10.02.2026 |
| Fri takhøyde kjeller | min. 3,0 m fra OK bunnplate til UK bjelkelag (`[TBD: kote OK bunnplate]`) | Adnan review |
| Bunnplate tykkelse | 450 mm | ISY-beskrivelse post 05.14 |
| Yttervegger tykkelse (tosidig del) | 250 mm | ISY-beskrivelse post 05.3 |
| Yttervegger snittykkelse (ensidig mot naturstein) | ca. 300 mm (varierer) | ISY-beskrivelse post 05.2 |
| Søylefundament grunnflate | **200 × 200 cm (= 4,0 m²)** — ikke 3000 × 3000 mm | Stenmo review (fasit); PGL bekrefter |
| XPS under fundament, grunnflate | 200 × 200 cm (= 4,0 m²) per fundament | Stenmo review (ISY 05.29 rettes til 2000×2000 mm) |
| Betongklasse bunnplate og yttervegger | B45, MF40, Cl 0,10, utførelsesklasse 2 | ISY 05.14/05.16 |
| Betongklasse fundamenter i vann | AUV-betong B45, MF40, Cl 0,10, utførelsesklasse 3 | ISY 05.15/05.18 |
| AUV-betong konsistens | min. SF2 (utbredelsesmål ≥ 660 mm), segregeringsresistens SR2 | Stenmo review |
| Betongklasse delevegger | **XS3 eller XC3/XC4 — IKKE XC1**; endelig klasse bekreftes av RIB før F9 | Stenmo review (ISY 05.9 feilklassifisering) |
| Armering | B500NC | ISY-beskrivelse |
| Overdekning armering (XS3) | min. 50 mm (sement-baserte avstandsholdere, ikke plast) | ISY 05.11 + Stenmo review |
| XPS kantisolasjon mot natursteinsmur | 50 mm | ISY 05.27/05.28 |
| Separasjonssjikt mellom betong og naturstein | plast/tett duk — betong skal **ikke** støpes fast til murverk | ISY 05.2 |
| Festing av duk til naturstein | **ikke** borring eller plugger i stein eller mørtelfuger; selvklebende butylgummitape eller kilefesting øverst/nederst | Stenmo review (U4) |
| Svelleprofil i støpeskjøter dekke/vegg | SikaSwell® P Type H, Sika-sertifisert montasje, monteres tidligst 48 t før støp | ISY 05.6 + Stenmo review |
| Beskyttelse svelleprofil mot fukt-aktivering | fugeblikk Master VB2 160 montert over svelleprofilen | ISY 05.7 + Stenmo review |
| Tetting rundt søylegjennomføring | SikaSwell® P Ring 24 NO | ISY 05.8 |
| Betongprøver | min. 3 sylindre per 30 m³, akkreditert laboratorium | Stenmo review |
| Prosjekteringsgrunnlag vanntetting | Byggforsk 520.055; NS-EN 1992/1997/13670; NS-EN 206 | ISY 05.14 |

**Soft — kan tilpasses situasjonen uten ny RIB-vurdering:**

- Rekkefølgen innenfor én fase (f.eks. hvilken yttervegg som støpes først, hvilken halvdel av platen armeres først).
- Valg av forskalingsleverandør og forskalingstype (systemforskaling vs. tradisjonell) så lenge NS-EN 13670 toleransekrav holdes **og** valg er avklart med arkitekt og BYA (jf. Adnan review om estetisk uttrykk).
- Valg av betongleverandør så lenge resept bekreftes mot ISY-krav og RIB skriftlig før første leveranse.
- Containertype og -antall så lenge kommunens vilkår holdes.
- Arbeidsgangen rundt tidevannsstøp — eksakt tidspunkt per dag styres av tidevannstabell fra Kartverket (sehavniva.no).
- Logistikk-koordinering mellom betongpumping, armeringssjekk og RIB-signering (det kritiske er at rekkefølgen holdes).

### 1.5 De tre viktigste strukturelle endringene fra v01 til v02

**Endring 1 — Modell B/C re-tegnet per fase (seksjon 3).** V01 presenterte Modell A/B/C som like gyldige alternativer og overlot valget til byggherre. V02 reorganiserer: F0–F5 kan være Modell B (egenregi med punktvis innleid), F6–F9 (støpefaser) **må** være Modell A eller C med SB-godkjent betongleverandør, F10 kan være Modell B med spesialleverandør for syrevasking, F11 er alltid spesialleverandør, F12 er egne folk. Dette er direkte følge av Stenmos tre krav for signerbarhet av F6–F9 og Søbstads forsikringsanalyse.

**Endring 2 — Byggesak splittet i tre løp (seksjon 4).** V01 behandlet IG som én myndighets-gate (MG-4). V02 skiller tre separate søknadsløp etter Ole Mortens PRO/UK/IG-analyse: MG-4a (IG-betong fra byggesak, forutsetter rammetillatelse), MG-4b (dispensasjon § 8 Riksantikvar), MG-4c (NVE/Statsforvalter for arbeid mot elv). Hvert løp har egen ansvarlig, eget tegningsgrunnlag og egen saksbehandlingstid.

**Endring 3 — Pre-F6 som egen fase (seksjon 8).** V01 forutsatte at RIB-produksjonstegninger ville foreligge når F6 startet. Fem av seks reviews (alle unntatt Ain) trakk fram at tegningene er den enkelt viktigste flaskehalsen — Søbstad vil ikke prise uten dem, Stenmo kan ikke signere uten geotekniker-bekreftede jordparametre, Kristian flagger at ingen formell bestilling av tegningene foreligger. V02 har en egen pre-F6-fase med arbeidsflyt: Stenmo tegner → geotekniker bekrefter φ, γ → tegning sendes entreprenør for pris → signering.

### 1.6 Språk og tone

Planen er på norsk bokmål. Teknisk-formelt språk er brukt der det må være verifiserbart (betongklasser, posthenvisninger). Operativt språk er brukt der bakeoppskrift-formatet krever det (steg-for-steg, kvalitetssjekker, typiske feil).

---

## 2. Prosjektrammer

### 2.1 Partsoversikt

| Rolle | Person / selskap | Kontakt |
|---|---|---|
| Byggherre | KodeWorks Eiendom AS, org.nr. 920 478 506 | — |
| Daglig leder / kontaktperson byggherre | Eirik Larsen | eirik.larsen@kodeworks.no, +47 416 70 269 |
| Prosjektleder antikvarisk istandsetting (PGL) | Ole Morten Lagmannssveen, HRP AS | ola@hrpas.no, +47 990 94 851 |
| Arkitekt (ansvarlig rammesøknad og planløsning) | Adnan, HRP AS | `[TBD: kontakt]` |
| Koordinator utførelse / SHK | Kristian Brandsegg, KMTE | `[TBD: kontakt]` |
| RIB (konstruksjon) | Ole Stenmo, Sivilingeniørene Harboe og Leganger AS | firmapost@h-l.no, +47 73 99 28 30 |
| Geotekniker (ny i v02) | `[TBD: ikke engasjert — RIB foreslår]` | Må bekrefte φ, γ før RG-6 |
| Betongleverandør (prekvalifisering pågår) | Kandidater: Unicon, Franzefoss Betong, NorBetong, Betong Øst | — |
| Betongentreprenør / SB-ansvarlig | `[TBD — avklares etter modellvalg; se seksjon 3]` | — |
| Uavhengig kontroll (UK) av prosjektering/utførelse | `[TBD — kommunens krav avklares etter rammetillatelse]` | — |
| Katodisk korrosjonsspesialist | `[TBD — Corrocean, Protea eller tilsvarende, kontaktes november 2026]` | — |
| Arkeolog (NIKU eller frittstående) | `[TBD]` | — |
| Daglig utførelse i felt | Ain Hansumae, Marco Dumitrescu | — |
| Prosjektadresse | Fjordgata 30, 7010 Trondheim | — |
| Gnr/Bnr | `[TBD: verifiseres mot matrikkelen — Prioritet 1]` | — |

### 2.2 Dimensjonerende forutsetninger

Alle verdier er hentet fra RIB-notat 10.02.2026 (Harboe og Leganger AS) og ISY-beskrivelse 19.10.2026 (HRP AS). RIB-notatet av 10.02.2026 overstyrer RIB-notatet av 13.06.2025 for alle lastforhold — det eldre notatet forutsatte kontor (3,0 kN/m²); minilager gir ca. 50 % mer last.

| Parameter | Verdi | Kilde |
|---|---|---|
| Dimensjonerende vannstand | kote +3,20 | RIB 10.02.2026 |
| Nyttelast kjeller og plan 1 (karakteristisk) | 7,5 kN/m² | RIB 10.02.2026 |
| Nyttelast kjeller og plan 1 (dimensjonerende, LF 1,5) | 11,25 kN/m² | Stenmo review |
| Nyttelast plan 2–5 (boder) | 5,0 kN/m² | RIB 10.02.2026 |
| Nyttelast plan 2–5 (adkomst) | 3,0 kN/m² | RIB 10.02.2026 |
| Snølast tak | 2,8 kN/m² | RIB 10.02.2026, NS-EN 1991-1-3 |
| Egenvekt etasjeskillere | 1,5 kN/m² | RIB 10.02.2026 |
| Egenvekt tak | 0,8 kN/m² | RIB 10.02.2026 |
| Brannkrav hoved- og sekundærbæring | R60 (HRP brannkonsept) | RIB 10.02.2026 |
| Materiale stål | S355 | RIB 10.02.2026 |
| Materiale tre | Heltre C18, limtre GL30c | RIB 10.02.2026 |
| Jordparametre | sand, friksjonsvinkel φ = 33°, egenvekt γ = 17 kN/m³ | RIB 13.06.2025 — **må verifiseres av geotekniker før RG-6 (yttervegger)** |
| Hviletrykkkoeffisient | K₀ = 1 − sin φ ≈ 0,45 (ved φ = 33°) | Stenmo review |
| Seismisk last | ikke blokkerende; Trondheim i lav ag-sone (< 0,1g), NS-EN 1998-1 § 4.2.5 unntar bygninger i underordnet konsekvensklasse | Stenmo review |

**Jordparametre — hvorfor dette er blokkerende for F8:** Horisontalt hviletrykk og aktivt jordtrykk fra terrenget bak natursteinsmuren er dimensjonerende for veggtykkelses- og armeringsvalget. Hvis grunnen er mykere leire enn antatt, eller friksjonsvinkel er lavere, endres veggarmeringen vesentlig. Stenmo signerer ikke armeringstegning for yttervegg uten skriftlig geoteknisk bekreftelse. Dette lukkes enten gjennom prøvegraving i Fase 5A med jordprøver til lab, eller enkel vingeboring / CPT-sondering i ett punkt langs veggen før Fase 8.

### 2.3 Hovedkonstruksjonsprinsipp

Prinsippet er en **ny vanntett betongkjeller inne i eksisterende natursteinsmur**. Elementene er:

- **Ny bunnplate i vanntett betong (B45 MF40 Cl 0,10, utførelsesklasse 2)**, 450 mm tykkelse, støpes som helhetlig plate uten glidebolter (beslutning 22.10.2026 — Ole Morten + RIB).
- **Nye yttervegger** i to seksjoner:
  - Nedre del: ensidig forskaling mot eksisterende natursteinsmur, snittykkelse ca. 300 mm, høyde ca. 1,7 m. Plast/tett duk + XPS 50 mm mot natursteinsmur som separasjonssjikt og glidesjikt — betong skal ikke støpes fast til murverk. Festing av duk gjøres **uten** borring eller plugger i stein/mørtel — kun selvklebende butylgummitape eller kilefesting øverst/nederst (Stenmo review U4).
  - Øvre del: tosidig forskaling fra topp natursteinsmur og opp til bjelkelag mot 1. etg. Tykkelse 250 mm.
- **Nye punktfundamenter under søndre del** (25 stk). **Dimensjon: 200 × 200 × 40 cm** (= 4,0 m² grunnflate per fundament). Dette er bekreftet av Stenmo basert på bæreanalysen i RIB-notat 10.02.2026 (Meyerhofs grunntrykksformel, φ = 33°, aksellast fra HUP 150×150×5-søyler). ISY post 05.29 (XPS-mengde 3000×3000 mm) er en skrivefeil og rettes til **2000 × 2000 mm**. Total XPS-mengde under fundamenter reduseres dermed fra ca. 225 m² til ca. 100 m².
- **Reparasjon/supplering av eksisterende fundamenter mot Nidelven** med AUV-betong B45 MF40 Cl 0,10 utførelsesklasse 3, tilpasset tidevannsrytme.
- **Katodisk korrosjonsbeskyttelse** (offeranodeanlegg) i gulv og vegger — marint miljø. Spesialleverandør kontraheres i F7 (ikke F10 som i v01) slik at eventuelle innstøpte festepunkter kan prosjekteres inn før F8-forskalingen settes (Kristian review).
- **Delevegger i lengderetning**, 250 mm. **Eksponeringsklasse XS3 eller XC3/XC4 — IKKE XC1** (Stenmo review). Kjellermiljøet er fuktig; XC1 (innvendig tørt miljø) i ISY 05.9 er feilklassifisering. Endelig klasse bekreftes av RIB i samråd med HRP før F9.
- **Radonsperre** (plastbasert, bruksgruppe A2, kombinert radon- og fuktsperre) som tegnet fallback — søkes dispensasjon fra kravet (beslutning 22.10.2026) med henvisning til grunnforhold (elvegrus, ikke radon-utsatt fjell). **Praktisk konsekvens for utførende:** radonsperre legges alltid, uavhengig av dispensasjonsutfallet. Dispensasjon påvirker ikke utføringen i felt (Ain review).

### 2.4 Trapperom og takhøyde — romgeometri (ny seksjon i v02)

Følger av Adnan review.

**Fri takhøyde kjeller:** min. 3,0 m fra OK bunnplate (kote `[TBD: fastsettes av arkitekt + RIB]`) til UK bjelkelag etasjeskille mot 1. etg. Dette måles i minst tre snittposisjoner (senter, nord, sør) fordi bjelkelaget varierer høyde — 3 m kan oppnås i midtrom men mangle i periferi uten koteverifisering.

**Trapperom Fjordgata-fasaden:** avklart 20.10.2026 (Adnan) at trapperommet strekker seg over **to internhøyder** — altså fra kjellergulv til etasjeskille 2. etg. Konkret konsekvens:

- Trappevolumet skal inn i kjellerplanen som eget rom med egne mål (grunnflate, H1 til etasjeskille 1. etg, H2 til etasjeskille 2. etg).
- Hvis kjellergulvet skal ligge på samme kote under trapperommet som under resten av kjelleren, må graving og bunnplate også dekke trappevolumet. 90 m²-arealet i ISY-mengdene skal verifiseres mot inkludering av trapperomsvolum.
- Betongvegg mot øvrige kjellerrom har høyde to internhøyder — vesentlig større armeringsmengde og forskalingsomfang enn resten av F8. Dette må reflekteres i RIB-tegning for F8.
- Trapperommet er leietakers første inntrykk av bygget. Krav om plass til vogn (minilager-bruk) og belysning — avklares av Adnan.
- Trapperom slik det er avklart 20.10 kan avvike fra rammesøknaden levert 12.05.2026. Avklaringen er sendt Byggesak til Byantikvaren (pkt. 2.6). Hvilken tegning-revisjon dette innebærer er `[TBD]`.

**Figur B (ny):** Tverrsnitt gjennom Fjordgata-fasaden og trapperommet, 1:50, med koteangivelse for begge internhøyder, adkomstbredde, trappeareal skilt fra kjellerplan. **Produseres av:** Adnan.

### 2.5 Historisk kontekst — hva vi fant i kjelleren

Da gulvbord ble demontert sommer/høst 2026 viste det seg at den opprinnelige bolverk/kavlegulv-konstruksjonen fortsatt lå under gulvbordene (notat 15.08.2026, Ole Morten). De tverrgående rundtømrene er i stor grad borte eller alvorlig råte-/brannskadd. De langsgående stokkene (cc 1–1,5 m) har varierende tilstand. Jordmassene bak natursteinsmuren er omrørt flere ganger med rester fra 1800-tallet og framover (blikkbokser, stål- og plastrør, søppel).

**Praktisk konsekvens** (bekreftet statusmøte 22.10.2026, Post 01.02): Bygget bæres i dag av det nye rammeverket i 1. og 2. etasje. Kavlegulvet/bolverket har ikke lenger bærende funksjon. Dette gir handlingsrom til å fjerne gjenværende trevirke etter RIB-signert sikringsplan.

**Beslutning 25.10.2026** (statusmøte 25.10, Post 02): Tjukke tverrgående tømmerstokker bevares (mulig forskningsprosjekt), alt annet trevirke fjernes. Formell avsjekk mot RIB kreves før kjellerarbeid utenfor «grønt-sone» starter.

### 2.6 Arkeologi og vernestatus

Fjordgata 30 er innenfor NB!-området i Trondheim og underlagt kulturminneloven. Byantikvaren og Riksantikvaren er inne i saken. Status pr. 21.10.2026:

- **Byantikvaren:** Alt trevirke frem til tørrmuren kan fjernes (statusmøte 22.10, Post 04.01).
- **Riksantikvaren:** Kommer på befaring. Betingelse: ikke grav i uomrørte masser — kun i allerede omrørte (statusmøte 22.10, Post 04.02).
- **Dispensasjon etter kulturminneloven § 8** er ikke innsendt. Må lukkes før graving i faste masser kan starte. `[TBD: last ned verbatim § 8-tekst fra Lovdata før søknad formuleres]`
- **§ 10-granskingsrisiko:** Hvis omfanget blir større enn dispensasjon dekker, kan Riksantikvaren utløse arkeologisk gransking etter § 10. Tiltakshaver (byggherre) dekker kostnaden.

**Praktisk konsekvens:** Fjerning av gammelt råttent trevirke regnes som vedlikehold og krever ikke særskilt tillatelse. Å støpe nytt betonggulv krever igangsettingstillatelse (IG) — egen sak hos kommunens byggesaksavdeling (statusmøte 22.10, Post 04.03).

### 2.7 Grensesnitt mot resten av prosjektet

- **Rammesøknad levert 12.05.2026**, status avventes. Oppdatering fra endret konseptvalg (kjellertrapp med natursteinsmur som bevart element — statusmøte 20.10 Post 02) er oversendt Byggesak til Byantikvaren.
- **Vinterklargjøring** (toalett + minikjøkken til 1. etg, ny kjellernedgang, frostfri vann) må være på plass før kjellerarbeid intensiveres — se Fase 0.
- **BYA-versjon** (lettvekts) av denne planen skal utarbeides av Ole Morten innen uke 46 (statusmøte 20.10, Post 03, bekreftet av Ole Morten review).
- **KMF-tilskudd:** Framdriftsrapport med utbetalingsanmodning har frist 31.12.2026. Realistisk ferdigstillelse av kjellerarbeidet er Q2 2027 (jf. seksjon 12). Dokumentasjon til KMF per 31.12.2026 vil omfatte: komplett plan v01→v02, oppmåling, RIB-signert sikringsplan, dispensasjonssøknad § 8 innsendt, RA-befaring gjennomført, Fase 3 i hovedsak fullført.
- **Enova (yrkesbygg + varmesentraler):** Separat søknadsløp. Energitiltak i kjeller (isolasjon, klimaskille) må være konsistente med Enova-grunnlaget.
- **TBRT-sporet** (brannsikringspålegg) berører overliggende etasjer, ikke kjeller. Men kjellerarbeid må ikke startes i gråsone mellom rammetillatelse og IG — hold TBRT-sporet adskilt (Ole Morten review).

---

## 3. Utførelsesmodeller — A, B og C re-tegnet per fase

Denne seksjonen er omskrevet fra v01. V01 presenterte A/B/C som like gyldige alternativer. Reviewene fra Stenmo (U3, U6, Modell B signerbarhet) og Søbstad (forsikringsanalyse) viser at valget må **gjøres per fase** og at F6–F9 har harde krav som utelukker ren Modell B.

### 3.1 Modellene — kort definisjon

**Modell A — Hel entreprise.** Betongentreprenør (Søbstad, Veidekke eller tilsvarende) tar helentreprise på alle betong- og grunnarbeider i kjeller etter NS 8405. Byggherre leverer RIB-godkjent produksjonsunderlag og myndighetsgodkjenninger. Entreprenøren bærer utførelsesrisikoen og er SB-godkjent ansvarlig utførende.

**Modell B — Egne folk + punktvis innleid betongekspertise.** Byggherres egne folk (Kristian som koordinator, Ain som dagsutfører, eventuelt studenter) utfører mesteparten av arbeidet. Betongentreprenøren bidrar med utleide fagfolk på kritiske operasjoner. **Begrensning (Stenmo + Søbstad):** Modell B krever at SB-godkjent betongfagperson er fysisk til stede og signerer under hele den kritiske operasjonen, ikke bare «stikker innom etter at armeringen er lagt». Uten dette er betongforsikring hull og RIB-gate (RG-4 for bunnplate, RG-6 for yttervegger) kan ikke gis.

**Modell C — Hybrid.** Helentreprise på de vanntette, SB-pliktige fasene (F6, F7, F8); Modell B på forberedende arbeider (F0–F5) og etterarbeid (F10–F12). Modell C tilsvarer det Søbstad eksplisitt tilbyr i sin review.

### 3.2 Modellvalg per fase — bindende i v02

| Fase | Hva fasen inneholder | Tillatt modell(er) | Begrunnelse |
|---|---|---|---|
| F0 | Vinterklargjøring, varmesone, kjellernedgang | B | Ingen bærende konstruksjoner berøres. Krever rørlegger (`[KREVER PROFF]` 4t) og elektriker (`[KREVER PROFF]` 2t). |
| F1 | Oppmåling, foto, pren-testing | B | Dokumentasjonsarbeid. |
| F2 | RIB-gating | B (RIB-signering utføres av Stenmo som del av engasjement) | Ingen fysisk arbeid; prosjekteringsgate. |
| F3 | Rydding over gulvnivå, kutting av stokker | B — **med krav om byggeleder- eller RIB-kompetent person fysisk til stede ved STØTTE+KUT-elementer** (Stenmo U1). Kristian skal være fysisk til stede ved første stokk-kapping (Kristian review). | Riving og demontering som egne folk utfører. Stokker opp til 300 kg og midlertidig støtte krever faglig vurdering i felt. |
| F4 | Prøvegraving + dispensasjonssøknad § 8 + IG-søknad + NVE-søknad | B (søknadsarbeid) | Dokumentasjonsarbeid. Arkeolog `[KREVER PROFF]` for prøvegraving og tilsyn. |
| F5 | Graving 130 m³ innvendig + 10 m³ under vann | B innvendig, A/C for graving under vann | Innvendig graving er egne folks arbeid med RIB-sluttkontroll (RG-2). Graving under vann (ISY 03.3) krever dykker/erfaren grunnarbeider — ikke egne folk (Søbstad + Stenmo). |
| F6 | Søylefundamenter 25 stk, AUV-betong utførelsesklasse 3 | **A eller C — IKKE ren B** | Utførelsesklasse 3 krever navngitt SB-godkjent til stede. AUV-betong under grunnvann krever fagkontroll. Stenmo nekter RG-3 uten SB-tilstedeværelse. |
| F7 | Bunnplate 115 m³ vanntett, utførelsesklasse 2 | **A eller C — IKKE ren B** | «Dette er min viktigste signatur i prosjektet» (Stenmo). Søbstad: fastpris mulig. 115 m³ i ett støp uten SB-godkjent er forsikringshull. |
| F8 | Yttervegger ensidig + tosidig, 52 m³ vanntett utførelsesklasse 2 | **A eller C — IKKE ren B** | Ensidig forskaling mot ujamn naturstein krever faglig forskalingstekniker (Søbstad: 7–8 dager, ikke 5). SB-godkjent til stede under støp. |
| F9 | Delevegger 250 mm, bærende for plan 1 | **A eller C — IKKE ren B** | Bærende konstruksjon. Stenmo U6: samme SB-krav som F8. XS3/XC3-klassifisering avklares først. |
| F10 | Overflatebearbeiding, syrevasking 295 m² | B med spesialleverandør for syrevasking | Syrevasking `[KREVER PROFF]` med HMS-krav (seksjon 6). XPS-montasje er egne folks arbeid. |
| F11 | Katodisk korrosjonsbeskyttelse | Alltid spesialleverandør | Egen bransje (SACP). Prosjektering starter i F7 (Kristian review), ikke F10 som i v01. |
| F12 | Sluttdokumentasjon | B | Administrasjon. |

### 3.3 SB-godkjenning for F6–F9 — hvem og når

To varianter:

**Variant 1 — Betongentreprenør med SB.** Søbstad, Veidekke eller tilsvarende med sentralgodkjenning for betongarbeider utførelsesklasse 2 og 3 melder ansvarsrett SB i IG-søknaden og er fysisk til stede under hele F6, F7, F8, F9. Dette er den enkleste og lavest-risiko varianten og er Stenmos foretrukne.

**Variant 2 — KMTE (Kristian Brandsegg) tar SB.** Betingelse: KMTE må ha dokumentert sentralgodkjenning fra Direktoratet for byggkvalitet (DiBK) for betongarbeider i utførelsesklasse 2 og 3. Sjekkes mot DiBKs sentralgodkjenningsregister. Pr. 21.10.2026: **ikke bekreftet**. Hvis KMTE ikke har denne godkjenningen, er Variant 2 blokkert.

**Prioritet 1-aksjon:** Kontakt Søbstad for Modell C-tilbud (bunnplate + yttervegger som fastpris, øvrig som regulerbart) **og** sjekk KMTEs sentralgodkjenning i DiBK-registeret. Beslutning om variant tas senest desember 2026, før rekruttering av forskalingstekniker (jf. koordineringsmatrisen).

### 3.4 Utførelses-gate UG-x — ny gate-type i v02

For å operasjonalisere Stenmos krav om SB-tilstedeværelse introduseres **utførelses-gater (UG-x)** som supplerer RIB-gatene (RG-x):

| Gate | Hva som utløser | Hva som må være oppfylt | Konsekvens hvis ikke |
|---|---|---|---|
| UG-1 | Første stokk-kapping i F3 | Kristian fysisk til stede (eller skriftlig delegert til kompetent stedfortreder) | Kutting utsettes. |
| UG-2 | Fundamentstøp F6 | SB-godkjent betongfagperson fysisk til stede under hele støpen; herdelogg startet; termometer plassert | Betong avvises på plassen. |
| UG-3 | Bunnplatestøp F7 | SB-godkjent fysisk til stede hele dagen; svelleprofil montert ≤ 48 t i forveien; separasjonssjikt visuelt kontrollert | Støp forbudt. |
| UG-4 | Vegg-støp F8 nedre del | SB-godkjent til stede; separasjonssjikt mot stein uten borring kontrollert | Støp forbudt. |
| UG-5 | Vegg-støp F8 øvre del og F9 | SB-godkjent til stede | Støp forbudt. |
| UG-6 | Syrevasking F10 | Tvangsgjennomlufting etablert og testet; HMS-ansvarlig navngitt dag-for-dag; evakueringsplan hengt opp | Syrevasking forbudt. |

UG-gatene dokumenteres skriftlig i dagsrapport med signatur fra SB-godkjent og foto.

### 3.5 Avviksprotokoll under støp

Under utførelses-gatene (særlig UG-2, UG-3, UG-4) kan det oppstå avvik underveis — f.eks. betong med feil konsistens ved ankomst, armering som er flyttet, kaldskjøt som truer. Protokoll:

1. SB-godkjent beslutter umiddelbart: fortsette, pause (venteklasse), eller avbryte (reject).
2. Beslutning noteres skriftlig i dagsrapport med klokkeslett og kort begrunnelse.
3. Foto av situasjonen tas før og etter beslutning.
4. Ved reject eller venteklasse: RIB (Ole Stenmo) kontaktes samme dag; e-post med foto og dagsrapport sendes.
5. RIB svarer skriftlig innen 24 t om tiltak er akseptable eller om det kreves ny prosjektering.

Dette er Stenmos tredje betingelse for Modell C-signerbarhet. Protokollen vedlegges SJA-mal for F6–F9.

---

## 4. Byggesak — tre løp og ansvarsrett

Denne seksjonen er ny i v02 og operasjonaliserer Ole Mortens tre byggesak-gap (PRO, UK, IG).

### 4.1 PRO-funksjon per fagområde

Søknad om igangsettingstillatelse (IG) for plasstøpt betong utførelsesklasse 2/3 krever ansvarsrettserklæringer etter SAK10 § 12-3. Status pr. 21.10.2026:

| Ansvarsrett | Fagområde | Ansvarlig foretak | Status |
|---|---|---|---|
| SØK | Ansvarlig søker (rammetillatelse + IG) | KodeWorks Eiendom AS | Innmeldt i rammesøknad 12.05.2026 |
| PRO — konstruksjon | Statiske og dynamiske beregninger, armeringstegninger | Sivilingeniørene Harboe og Leganger AS (Ole Stenmo) | **Må sjekkes om meldt i rammesaken** |
| PRO — bygningsfysikk | Fuktteknikk, lufttetthet, klimaskille | HRP AS | **Må sjekkes om meldt i rammesaken** |
| PRO — antikvarisk istandsetting / arkitektur | Rammesøknad, antikvarisk prosjektering, kulturminnehåndtering | HRP AS (Ole Morten + Adnan) | **Må sjekkes om meldt i rammesaken** |
| PRO — brannkonsept | Brannstrategi, R60-oppfyllelse | HRP AS | **Må sjekkes om meldt i rammesaken** |
| SB — betongarbeider utførelsesklasse 2 | Bunnplate, yttervegger, delevegger (F7, F8, F9) | `[TBD — se seksjon 3.3]` | **Åpen — blokkerer IG** |
| SB — betongarbeider utførelsesklasse 3 | Fundamenter under grunnvann (F6, F5C) | `[TBD — se seksjon 3.3]` | **Åpen — blokkerer IG** |
| SB — grunnarbeid | Graving, masseflytting | `[TBD]` | **Åpen** |
| SB — katodisk anlegg (elkraft) | Montasje og idriftsettelse offeranodeanlegg | Katodisk spesialist (Corrocean/Protea) | **Avventer kontrahering** |
| KPR — kontrollforetak prosjektering (UK) | Uavhengig kontroll av RIB-prosjektering | `[TBD — avklares med kommune, se 4.2]` | **Åpen** |
| KUT — kontrollforetak utførelse (UK) | Uavhengig kontroll av betongutførelse | `[TBD]` | **Åpen** |

**Prioritet 1-aksjon (Ole Morten):** Hent ut rammetillatelsessaken fra kommunen og list opp hvilke ansvarsretter som faktisk er meldt. Identifisere hullene — og særlig SB-rollene som ikke er på plass.

### 4.2 Uavhengig kontroll (UK) — SAK10 § 14-2

For konstruksjoner i utførelsesklasse 2 og 3 stiller SAK10 § 14-2 krav om uavhengig kontroll av prosjektering og eventuelt utførelse. V01 nevnte ikke dette; det er en reell mangel som må lukkes før IG kan søkes.

**Prioritet 1-aksjon (byggherre):** Skriftlig forespørsel til Trondheim kommune byggesak: er UK av prosjektering og/eller utførelse påkrevd for betongarbeidet i Fjordgata 30? Hvis ja: velg kontrollforetak og innhent pris.

**Candidate-liste UK-foretak Trondheim-regionen:** `[TBD — Rambøll, Multiconsult, Norconsult, Sweco. Ikke kontaktet.]`

**Konsekvens for Gantt:** UK-engasjement og kontrolltiltaksplan må være på plass før IG-søknad kan være komplett. Normal saksbehandling i kommunen for IG er 3–12 uker. UK-rapport må foreligge **før** støping starter — tidsmessig kritisk hvis først avklart etter rammetillatelse foreligger.

`[TBD: last ned verbatim SAK10 § 14-2 fra Lovdata før IG-søknad formuleres]`

### 4.3 De tre IG-løpene — splittet i v02

V01 behandlet IG som én gate (MG-4). V02 splitter i tre separate løp som ikke kan behandles under ett vedtak:

**MG-4a — IG for betongarbeider innvendig (kommunens byggesak).**

- Hjemmel: plan- og bygningsloven kap. 20, SAK10 § 7.
- Forutsetter: innvilget rammetillatelse (status pr. 21.10.2026: avventes, søknad levert 12.05.2026).
- Vedlegg: PRO-ansvarsretter (jf. 4.1), SB-ansvarsrett betong, kontrolltiltaksplan UK, armeringstegninger fra RIB, SJA for de kritiske fasene.
- Ansvarlig søker: byggherre (KodeWorks Eiendom AS).
- Saksbehandlingstid: 3–12 uker.
- **Blokkerer:** Fase 6, 7, 8, 9 (all betongutførelse).

**MG-4b — Dispensasjon etter kulturminneloven § 8 (Riksantikvar / Trøndelag fylkeskommune).**

- Hjemmel: kulturminneloven § 8. `[TBD: last ned verbatim § 8-tekst fra Lovdata før søknadsformulering]`
- Vedlegg: målsatte tegninger av graveomfang (plan + snitt), prøvegraverapport, foreløpig vurdering av kulturlag.
- Ansvarlig: Ole Morten (PGL) utarbeider søknad, byggherre signerer og sender.
- Saksbehandlingstid: 4–12 uker (NIKU-tilrådning kan utvide til 12 uker).
- **Blokkerer:** Fase 5 (hovedgraving i uomrørte masser).

**MG-4c — Tillatelse for arbeid mot elv (NVE / Statsforvalter / Trondheim havn).**

- Hjemmel: vannressursloven, naturmangfoldloven, forurensningsloven.
- Trolig **flere** separate søknader:
  - NVE: vassdragsinngrep (graving under vann 10 m³, forsterkning av fundamenter mot Nidelva).
  - Statsforvalter i Trøndelag: naturmangfold hvis relevant.
  - Trondheim kommune miljøenhet: vannforurensning.
  - Trondheim havn: eiendomsrett og vektrestriksjoner på havnegrunn (relevant for pumpebil-tilkomst, jf. R20).
- Vedlegg: snitt arbeid mot elv (F4-B), AUV-metodikk, avbøtende tiltak mot vannforurensning.
- Ansvarlig: byggherre + Ole Morten.
- Saksbehandlingstid: 6–16 uker (NVE kan være langsom).
- **Blokkerer:** Fase 5C (graving under vann), Fase 6 (fundamentreparasjon mot elv), eventuelt F8 (yttervegg mot elv-side).

### 4.4 Dokumentasjonsflyt (fra Ole Morten review)

| Dokumenttype | Hvem leverer | Deadline | Arkiveres |
|---|---|---|---|
| Søyleoppmåling — Tegning 1 (plan) og Tegning 2 (snitt) | Ole Morten (PGL) | 25.10.2026 | bakgrunn/kjeller/ |
| Sikringsplan for kutting av bærende elementer (RG-1) | Ole Stenmo (RIB) + Ole Morten (PGL) | 01.11.2026 | bakgrunn/kjeller/ + kommunen |
| Dispensasjonssøknad kulturminneloven § 8 | Ole Morten (PGL) + byggherre | Sendes innen uke 45 | leveranser/ + Riksantikvar |
| Søknad arbeid mot elv (NVE/Statsforvalter) | Byggherre + Ole Morten (PGL) | Sendes parallelt med § 8 | leveranser/ |
| Lettvekts BYA-versjon av kjellerplan | Ole Morten (PGL) | Uke 46 (før neste BYA-befaring) | leveranser/kjeller/ |
| RA-befaringsnotat | Adnan + Ole Morten | Senest 3 virkedager etter befaring | bakgrunn/kjeller/ |
| IG-søknad for betongarbeider (MG-4a) | Byggherre (ansvarlig søker) | Etter rammetillatelse innvilget | leveranser/ + kommunen |
| Erklæring om ansvarsrett PRO (RIB) | Harboe og Leganger AS | Før IG-søknad | Kommunens byggesak |
| Erklæring om ansvarsrett PRO (antikvarisk, bygningsfysikk, brann) | HRP AS | Før IG-søknad | Kommunens byggesak |
| Erklæring om ansvarsrett SB (betong) | Betongentreprenør eller KMTE | Før IG-søknad | Kommunens byggesak |
| Kontrolltiltaksplan (UK) | Kontrollforetak | Vedlegg IG-søknad | Kommunens byggesak |
| RIB-armeringstegninger (produksjonsunderlag) F6, F7, F8, F9 | Ole Stenmo (RIB) | Senest 6 uker før hver fase | leveranser/kjeller/ |
| Geoteknisk bekreftelse av jordparametre | Geotekniker | Før RG-6 (F8-armering) | bakgrunn/kjeller/ |
| Betongprøveprotokoll (per støp) | SB-godkjent / akkreditert lab | Løpende F6–F9 | Prosjektmappe |
| Dagsrapporter med foto | Kristian/Ain | Daglig F0–F12 | Prosjektmappe |
| Ukentlig framdriftsrapport | Ain → Kristian/byggherre | Fredag kl. 14 | Prosjektmappe |
| Arkeolog-sluttrapport | NIKU / befart arkeolog | Etter graving | bakgrunn/kjeller/ |
| RIB-sluttattest (RG-8) | Ole Stenmo (RIB) | Etter F11 | Prosjektmappe + kommunen |
| Vedlikeholdsplan katodisk anlegg | Katodisk korrosjonsspesialist | Etter F11 | Prosjektmappe |
| Sluttdokumentasjon til KMF | Byggherre + Ole Morten | 31.12.2026 (delvis) + sluttrapport | leveranser/stotte/kmf/ |
| Sluttdokumentasjon til Enova | Byggherre | Etter sluttattest | leveranser/stotte/enova/ |

### 4.5 Forhåndsmelding til Arbeidstilsynet

HMS-forskrift på bygge- og anleggsplasser § 6: forhåndsmelding kreves dersom samlet byggeperiode overstiger 30 arbeidsdager **eller** 500 persondagsverk. Kjellerprosjektet alene overstiger trolig 500 persondagsverk (anslag: 10 personer × 60 dager = 600 persondagsverk).

**Prioritet 2-aksjon (byggherre + Kristian som SHK):** Meld forhåndsmelding til Arbeidstilsynet før oppstart av F3. Sjekkeliste over hva meldingen må inneholde — SHA-plan, SHK, varighet — se seksjon 6.

### 4.6 TBRT-sporet og rammetillatelse

Fra Ole Morten review: Hold TBRT-sporet (tvangsmulktsak brannsikring) adskilt fra kjellerarbeidene. Men: start ikke betongarbeid (F6+) før rammetillatelsen er bekreftet innvilget. Riving av trevirke (F3) er lovlig som vedlikehold og kan starte uavhengig av rammetillatelse. IG-grensen slår inn ved graving og støping.

---

## 5. Koordineringsmatrise — bestillinger og ansvar

Denne seksjonen er ny i v02 og lukker Kristians mangel-liste på 20 koordineringspunkter samt Ains krav om «hvem bestiller hva».

### 5.1 Hovedmatrise

Alle bestillinger og koordineringspunkter som planen er avhengig av. Hver linje har ansvarlig, deadline, milepæl og status.

| # | Oppgave | Ansvarlig | Deadline | Milepæl | Status 21.10.2026 |
|---|---|---|---|---|---|
| K01 | Verifiser gnr/bnr mot matrikkelen | Byggherre | 25.10.2026 | Før § 8-søknad | Åpen |
| K02 | Søyleoppmåling innerst mot Fjordgata (Tegning 1 + 2) | Ole Morten | 25.10.2026 | F1 ferdig | Pågår 21.10 |
| K03 | Sikringsplan tømmerstokker (RG-1) | Ole Stenmo + Ole Morten | 01.11.2026 | Før F3 stokk-kutting | Åpen |
| K04 | Skriftlig bekreftelse fundamentdimensjon 200×200×40 cm | Ole Stenmo (bekreftet 21.10) + HRP | 25.10.2026 | Før F6 | **Lukket i Stenmo review 21.10** |
| K05 | Rørlegger — bestill navn og dato | Kristian | 28.10.2026 (minst 1 uke varsel) | F0.2 | Åpen |
| K06 | Container-søknad fortausbruk til Trondheim kommune | Byggherre | 13.11.2026 (5–10 virkedager behandling) | Container på plass uke 48 | Åpen |
| K07 | Ny kjellernedgang — posisjonsvalg besluttet | Byggherre + Kristian + Ole Morten | Før F0.6 (uke 44) | F0.6 | Åpen |
| K08 | Beslutte minigraver eller manuell graving (basert på tilkomstmål) | Kristian + Ain | Uke 44 | Før F5-oppstart | Åpen |
| K09 | Vinsjekurv — spesifiser, lei og test oppheng | Kristian + Ain | Uke 45 | Før F3.10 | Åpen |
| K10 | Prekvalifiser 2–3 betongleverandører; be om resept-bekreftelse B45 MF40 Cl 0,10 og AUV | Byggherre | Senest november 2026 | Før RG-3 bestilling | Åpen |
| K11 | Deponi-avtale for 200 tonn løsmasser (miljøklasse, prøver) | Byggherre eller valgt entreprenør | Parallelt med § 8-søknad | Før F5-oppstart | Åpen |
| K12 | Pumpebil-tilkomst: mål Fjordgata-bredde, kontakt pumpeleverandør | Kristian + Ain | Uke 44 | Før RG-4 | Åpen |
| K13 | Søknad midlertidig parkeringsforbud for pumpebildag (F7) | Byggherre eller valgt entreprenør | Minst 2 uker før støpedag | Før RG-4 bestilling | Åpen |
| K14 | Arkeolog (NIKU) — kontakt for pris og avklaring tilstedeværelse | Ole Morten | Uke 44 | Før § 8-søknad | Åpen |
| K15 | Riksantikvar — avtale befaringsdato | Byggherre + Ole Morten | Uke 44 | F4 start | Åpen |
| K16 | § 8-søknad — formuler og send | Ole Morten + byggherre | Uke 45 (senest 07.11.2026) | MG-4b aktivert | Åpen |
| K17 | NVE/Statsforvalter/Trondheim havn/miljøenhet — søknader | Byggherre + Ole Morten | Parallelt med § 8 | MG-4c aktivert | Åpen |
| K18 | Igangsettingstillatelse (IG) — søknad til kommunens byggesak | Byggherre | Når rammetillatelse foreligger | MG-4a aktivert | Åpen (venter rammetillatelse) |
| K19 | PRO-ansvarsretter sjekk + melding av manglende | Ole Morten + byggherre | Før IG-søknad | MG-4a vedlegg | Åpen |
| K20 | UK-foretak — kontakt kommune for avklaring, deretter kontrahere | Byggherre + Ole Morten | Før IG-søknad | MG-4a vedlegg | Åpen |
| K21 | Forhåndsmelding Arbeidstilsynet | Byggherre + Kristian (SHK) | Før F3 oppstart | HMS compliance | Åpen |
| K22 | Nabovarsel og fotodokumentasjon av nabokjeller Fjordgata 28/32 | Byggherre | Før F5 | R01 avbøtende | Åpen |
| K23 | Bestille RIB-armeringstegninger F6, F7, F8, F9 formelt | Byggherre (skriftlig) | Uke 44 | Før Pre-F6 fase | Åpen |
| K24 | Geotekniker — kontrahere, prøvetaking | Byggherre + RIB | Før F5A | RG-6 forutsetning | Åpen |
| K25 | Betongentreprenør — kontakt Søbstad + 1–2 andre for Modell C-tilbud | Byggherre | November 2026 | SB avklart | Åpen |
| K26 | KMTE sentralgodkjenning i DiBK — sjekk | Byggherre | Uke 44 | SB avklart | Åpen |
| K27 | Katodisk-leverandør — kontrahere i F7, ikke F10 | Byggherre + Ole Morten | Februar 2027 | F11 prosjektering | Åpen |
| K28 | Forskalingstekniker + betongbas — rekruttere | Betongentreprenør eller byggherre | **Desember 2026 (hard deadline — markedsstramt)** | F6 oppstart jan 2027 | Åpen |
| K29 | SJA skrives per fase (F3, F5, F6, F7, F8, F10) | Kristian (SHK) | Før hver fase | HMS compliance | Åpen |
| K30 | Forsikringsgjennomgang Modell C | Byggherre | Før F6 oppstart | R11 lukket | Åpen |
| K31 | Nødkontaktliste laminert i kjeller | Ain + Kristian | Før F3 oppstart | HMS compliance | Åpen |
| K32 | Skytjeneste for foto og dagsrapport (OneDrive/Google Drive) | Kristian + Ain | Før F1 oppstart | Dokumentasjon | Åpen |
| K33 | Lensepumpe + reservepumpe testet og dokumentert kapasitet | Ain | Uke 43 | F0.9 | Delvis utført |
| K34 | Ukentlig framdriftsmelding — rutine Ain → Kristian hver fredag kl. 14 | Ain | Fra uke 44 | Dokumentasjon | Åpen |
| K35 | BYA-befaringsplan (5 befaringstidspunkt) | Adnan + Ole Morten | Uke 46 | BYA-dialog | Åpen |
| K36 | Avklare betongklasse delevegger (XS3/XC3 ikke XC1) | Ole Stenmo + Ole Morten | Før F9-forskaling | QA-funn 7, 8 lukket | Åpen |
| K37 | Avklare volum fundamenter mot elv (ISY 05.18) | Ole Stenmo | Etter F5C | QA-funn 9 lukket | Avventer F5C |
| K38 | ISY-beskrivelsen lukket for QA-funn 1, 2, 4, 5, 8, 10, 11 | Ole Morten (HRP) | Innen 1 uke | QA før anbud | Åpen |
| K39 | Tidevannstabell for Trondheim — hvem henter og kilde (sehavniva.no er offisiell) | Ain | Før F6 | F6/F7 planlegging | Åpen |
| K40 | Frosttelt + varme — avklare behov og pris (vinter 2027) | Byggherre + Søbstad | Desember 2026 | F6/F7 oppstart | Åpen |
| K41 | Ain — ansettelsesforhold avklart (lønnsmottaker/næring/student) for forsikring | Byggherre | Umiddelbart | Forsikring | Åpen |
| K42 | Arbeidsark til Ain og Marco for uke 44 (A4 med instruks) | Kristian | 25.10.2026 | F3 oppstart | Åpen |

### 5.2 Bestillingsliste med leveringstid for `[KREVER PROFF]`-ressurser

Fra Ain-review (punkt 4) og Kristians bemanningsplan:

| Ressurs | Typisk leveringstid | Avbestillingsregime | Hvem bestiller |
|---|---|---|---|
| Autorisert rørlegger (Trondheim) | 1–2 uker i november | 48 t uten gebyr vanligvis | Kristian |
| Autorisert elektriker | 3–5 virkedager | 48 t uten gebyr | Kristian |
| Minigraver med operatør | 1 uke | 24 t | Kristian |
| Forskalingstekniker (Trondheim-markedet 2026/27) | **4–8 uker — stramt marked** | 1 uke varsel, deretter 50 % | Betongentreprenør (Søbstad) eller byggherre direkte |
| Betongbas | 2–4 uker | 1 uke varsel | Betongentreprenør |
| Pumpebiloperatør + pumpe | 2–3 uker | 3 virkedager varsel | Betongentreprenør |
| Betongleveranse B45 MF40 Cl 0,10 (Unicon, Franzefoss, NorBetong) | 24 t hvis lager; 48–72 t spesialresept | 24 t | SB-godkjent |
| AUV-betong B45 MF40 Cl 0,10 | 48–72 t | 24 t | SB-godkjent |
| Dykker / grunnarbeider for undervannsarbeid (F5C) | 2–3 uker | 1 uke | Byggherre eller entreprenør |
| Arkeolog (NIKU eller frittstående) | 2–4 uker for prøvegraving-slot | Fleksibelt mot stans-plikt | Byggherre + Ole Morten |
| Katodisk korrosjonsspesialist (Corrocean/Protea) | **4–8 uker for prosjekteringsrapport** | — | Byggherre |
| RIB-signering RG-x | 3–10 virkedager (planlegg som 10) | — | Byggherre skriftlig forespørsel |
| Betongfagarbeider for syrevasking | 1–2 uker | 1 uke | Byggherre eller entreprenør |

**Hva Ain gjør i ventetid for proff-ressurser:** Hvis RIB-gate forsinkes 1–2 dager, kan Ain fortsette med fotodokumentasjon, forberedende rydding av verktøy og materialer, SJA-forberedelse for neste fase, foto-register. Hvis forsinkelsen er lenger, konferer med Kristian om alternative oppgaver i andre faser (f.eks. starte F11-prosjekteringsforberedelser).

### 5.3 Daglig logistikk — Ains del

Fra Ain-review (punkt 10):

- **Arbeidstid F3–F5:** 07:00–15:30 (lunsjpause 11:30–12:00). Avvik må avklares med Kristian.
- **Toalett og varmesone fra dag 1:** Dersom F0 (ny varmesone i 1. etg) ikke er ferdig før F3 starter, er midlertidig toalett i 2. etg og provisorisk varme (byggvarmer) løsningen. Byggherre leier byggvarmer uke 43.
- **Nøkkel og tilgang:** Ain har egen nøkkel. Reservenøkkel hos Kristian. Hvis Kristian er remote og nøkkel mistes: kontakt byggherre direkte.
- **Parkering:** Fjordgata er smal. Ain parkerer på Nedre Elvehavn (ca. 400 m) og går, eller bruker sykkel. Containerplass er for container, ikke bil.
- **Verktøy-oppbevaring:** Låsbart skap i 1. etg varmesone. Verktøy som ikke får plass i skap stables under duk i kjeller — fuktrisiko tas med i daglig vurdering.
- **Nøkkelrutine ved sykdom/fravær:** Ain melder fravær til Kristian via SMS senest kl. 06:30. Kristian avgjør om Marco overtar eller om dagen avlyses.

### 5.4 Eskaleringskjede — hvem ringer hvem

Fra Ain-review (punkt 3) og Kristians mangelliste 17–20:

**Nivå 1 — Daglig arbeid (ikke-kritisk):** Ain tar beslutning selv eller spør Marco.

**Nivå 2 — Uklart eller teknisk tvil:** Ain ringer Kristian (`[TBD: telefonnummer]`). Hvis ikke svar innen 30 min: ring Ole Morten (+47 990 94 851). Hvis fortsatt ikke svar og saken haster: ring byggherre (+47 416 70 269).

**Nivå 3 — Uventet funn, strukturell tvil, personskade:**

- **Uventet bæresituasjon (stokk oppfører seg annerledes enn forventet):** Stopp arbeid. Fotografer. Ring Kristian → Ole Morten → Ole Stenmo (+47 73 99 28 30).
- **Oversvømmelse (lensepumpe sliter, grunnvann stiger):** Start reservepumpe. Fotografer. Ring Kristian → Ain fortsetter med pumping og tildekking til Kristian er på plass.
- **Arkeologisk funn (bein, keramikk ut over 1800-tallet-rester, skipsdeler):** Stopp arbeid. Fotografer in situ før berøring. Ring Ole Morten → byggherre → Riksantikvar (via Ole Morten). Dokumenter dato/klokkeslett.
- **Personskade:** 113 først. Deretter varsle Kristian + byggherre. Arbeidstilsynet varsles innen 72 t ved alvorlig skade.

**Laminert A4 i kjelleren (K31):** Nødkontaktliste med alle nummer og eskaleringskjeden i kortform. Henges opp ved kjellernedgang, oppdateres månedlig.

---

## 6. HMS og SJA — navngitt ansvar per fase

Denne seksjonen er ny i v02 og lukker Ain-review (6, 10), Kristian-review (merknad F3, F5, F10, mangel 18–19) og Ole Morten-review (SHK-dokumentasjon).

### 6.1 SHA-plan og SHK (SHA-koordinator utførelse)

- **SHK utførelse:** Kristian Brandsegg, KMTE.
- **Dokumentasjon kreves:** SHK-kurs fra Norsk Byggtjeneste eller tilsvarende, gyldig sertifikat. **Status pr. 21.10.2026: `[TBD — sjekk sertifikat]`**. Hvis Kristian ikke har gyldig SHK-sertifikat må enten (a) han tar kurset før F3 starter, eller (b) ekstern SHK leies inn.
- **SHA-plan som helhet:** Dokumenteres som egen fil `leveranser/kjeller/sha_plan.md` eller tilsvarende. SHA-planen skal inneholde: risikovurdering per fase, avbøtende tiltak, nødprosedyre, varslingsrutiner, verneutstyr-krav, HMS-ansvarlig per fase/dag.

### 6.2 HMS-ansvarlig navngitt per fase

Fra Kristians review-krav 2 (navngitt stedfortreder når Kristian er remote):

| Fase | Primær HMS-ansvarlig på plassen | Stedfortreder (ved fravær ≥ 2 dager) | Myndighet stedfortreder |
|---|---|---|---|
| F0 | Kristian | Ain | Daglig drift. Ikke start av nye arbeidsoperasjoner. |
| F1 | Ole Morten (på plassen under oppmåling) | Ain | Dokumentasjonsarbeid. |
| F2 | Kristian | — | Ingen fysisk arbeid; RIB-gate. |
| F3 | **Kristian fysisk til stede ved UG-1 (første stokk-kapping, STØTTE+KUT-elementer)** | Ole Morten eller ekstern innleid med byggeleder-kompetanse | Fortsette lavrisk-arbeid; ikke start stokk-kapping. |
| F4 | Kristian + Ole Morten | Ain (dokumentasjonsside) | Søknadsarbeid. |
| F5 | Kristian + navngitt stedfortreder (Ole Morten eller innleid) | Innleid HMS-ansvarlig fra entreprenør | Fortsette graving manuell/minigraver med SJA fulgt. Stans ved funn. |
| F6 | **SB-godkjent betongfagperson (fra entreprenør)** | — | SB kan ikke delegeres. |
| F7 | **SB-godkjent betongfagperson (fra entreprenør)** | — | SB kan ikke delegeres. |
| F8 | **SB-godkjent betongfagperson (fra entreprenør)** | — | SB kan ikke delegeres. |
| F9 | **SB-godkjent betongfagperson (fra entreprenør)** | — | SB kan ikke delegeres. |
| F10 | Fagarbeider syrevasking + HMS-ansvarlig navngitt dag-for-dag (Kristian eller innleid) | — | Avbrytes ved ventilasjonssvikt. |
| F11 | Katodisk spesialist (egen prosedyre) | — | — |
| F12 | Kristian | Ain | Dokumentasjon. |

### 6.3 SJA-krav per fase

Fra Kristian-review (krav 3), Ain-review (6, 8). SJA skrives som eget vedlegg og vedlegges planen før hver fase starter.

| Fase | SJA-tema | Minimumsinnhold |
|---|---|---|
| F3 | Kjedesag + tunge løft + motorsag-regel | Kjedesaghansker, FFP3, visir, kun én motorsag-bruker samtidig, aldri alene, nødkontakt, vinsje-oppheng-dokumentasjon |
| F5 | Graving med grunnvann + arkeolog-stansrisiko | Lensepumpe-rutine, reservepumpe-plassering, stans-regel ved funn, fotodokumentasjon, min. avstand 50 cm til fundament |
| F5C | Arbeid under vann mot elv | Tidevannstabell, flytevest, kommunikasjon, dykker-oppfølging, kommunikasjonssignaler |
| F6 | AUV-betong + fundamentstøp i vann | Pumpebil-posisjon, lensepumpe kontinuerlig, UG-2 krav, herdelogg-oppsett |
| F7 | 115 m³ bunnplate i smal gate | Minuttplan støpedag, pumpebil-stabilisering, 25 søylegjennomføringer, vibrator-koordinering, nødstopp |
| F8 | Ensidig forskaling mot ujamn naturstein | Festing uten borring, kilefesting, forskalingsstyrke lateralt vs. uregelmessig støttepress, UG-4 |
| F10 | Syrevasking 295 m² HCl 5 % i trangt rom | **Tvangsgjennomlufting-krav kvantifisert**, FFP3 syreresistent, nødevakuering, nøytraliseringsutstyr, kun én syrevasker samtidig i rom, utendørs oppholdssone |

### 6.4 Ventilasjon ved syrevasking (F10) — konkret spesifikasjon

Fra Ain-review (6) og Kristian-review (F10 merknad 1):

**Krav:**

- Luftvolum kjellerrom (anslag 90 m² × 2,5 m takhøyde = 225 m³). Luftutskifting min. 10 ganger per time (konservativt for HCl-arbeid) = 2250 m³/t = 625 l/s.
- To separate ventilasjonstiltak: (a) tvangsavtrekk ut gjennom kjellernedgang med vifteenhet (min. 2000 m³/t); (b) frisklufttilførsel via den andre kjellernedgangen (den «andre» rømningsveien som etableres i F0.6).
- Måling: PID-meter (fotoionisering) for HCl-damp. Alarmgrense: 1 ppm (NIOSH REL 5 ppm 15-min TWA, men vi setter konservativt). Over alarm → evakuer, nøytraliser, utsett videre arbeid.
- Vernedusj med rennende vann umiddelbart tilgjengelig (vannleging i varmesone 1. etg).
- Nøytraliseringsmiddel (sodaoppløsning 10 %) i spraykanne, min. 10 l tilgjengelig.
- Heldress syreresistent, hansker nitril (ikke lateks), briller/visir, FFP3-maske for syre + ammoniakk.

**Hvem har ansvar:** Byggherre leier inn tvangsavtrekk + friskluftvifte som del av F10-forberedelse (K43 ny bestilling: `[TBD]`). SB (betongfagarbeider for syrevasking) utfører; HMS-ansvarlig dag-for-dag (Kristian eller innleid) kontrollerer utstyret før oppstart.

**Nødprosedyre ved eksponering:**

1. Varsle alle i kjelleren, evakuer til varmesone i 1. etg.
2. Spyl berørt hud med vann i min. 15 min.
3. Nøytraliser med soda-spray etter spyling.
4. Ring 113 ved pustebesvær eller øyeeksponering.
5. Varsle Kristian + byggherre.
6. Dokumenter hendelse i avviksrapport.

### 6.5 Tunglast-håndtering (F3)

Fra Ain-review (1) og Kristian-review (F3 merknad 2):

**300 kg tømmerstokker — regler:**

- Aldri manuell løfting over 50 kg per person uten mekanisk hjelp.
- Vinsjekurv med kapasitet min. 500 kg, dokumentert sertifikat for løfteutstyr (CE-merket, EN 13157 eller tilsvarende).
- Bærepunkt for vinsjen: innleid rigg-ingeniør eller RIB-vurdering av etasjeskillets bærekapasitet før første bruk. **Ikke** fest i delvis revet etasjeskille uten dokumentert bæreverifisering.
- Minimum 2 personer ved all tunglast-operasjon.
- Verneutstyr: vernesko stålhette, hjelm, vernehansker (lærrygg mot splinter), hørselsvern ved kjedesag-bruk.
- «Dropp gjennom gulvåpning mot kanalside» — denne frasen i v01 **fjernes** fra v02. Stokker senkes kontrollert ned via vinsjekurv eller rulles på underlagsmatter. Fri fall av 300 kg er ikke tillatt (Ain-review 1).

### 6.6 Nabovarsel og setningsrisiko (R01-avbøtende)

Fra Kristian-review (mangel 12):

- Nabovarsel sendes til Fjordgata 28 og Fjordgata 32 før F5-oppstart. Kort beskrivelse av tiltaket, forventet varighet og kontaktinformasjon.
- Fotodokumentasjon av nabokjeller før oppstart — avtales med nabobygget-eier. Setningsbolter settes langs natursteinsmur som referansepunkter. Måling før, under og etter F5.
- Dette er avbøtende tiltak for R01 (setningsskader) og er en forsikringsmessig nødvendighet.

---

## 7. Arkitektur — det som bygges, ikke bare det som støpes

Denne seksjonen er ny i v02 og lukker Adnans ti arkitektoniske mangler.

### 7.1 Arkitektoniske beslutninger som må tas før F8

| # | Beslutning | Alternativer | Ansvar | Frist |
|---|---|---|---|---|
| A1 | Takhøyde-kote referansepunkt | OK bunnplate (foreslått) / UK bjelkelag / annet | Adnan + RIB | Før RIB-tegning F7 |
| A2 | Trapperom to internhøyder — betongvegg-høyde og armering | — | Adnan + RIB | Før RIB-tegning F8 |
| A3 | Søyler — bevart synlig / dekkes inn / erstattes per søyle | per søyle, SE søyleplan | Adnan + Ole Morten | Før F3 start (synlige søyler må ikke skades) |
| A4 | Natursteinsmur-eksponering — alt. 1/2/3 | 1: betong fra gulv til bjelkelag (steinen skjult). 2: betong i nedre del (1,7 m), stein eksponert over murkrona. 3: åpen vektergang med glass/sprekk. | Adnan + BYA + byggherre | Før F8-forskaling |
| A5 | Forskalingsvalg (estetisk uttrykk) | systemforskaling boltmønster / storskalig treplank / stålplate / naturstein-inspirert | Adnan + BYA | Før F8-forskaling-bestilling |
| A6 | Belysningsplan kjeller (lux-krav minilager) | — | Adnan + el-prosjekterende | Før F10 |
| A7 | UU-krav minilager (trinnfri adkomst?) | — | Adnan | Verifiseres mot rammesøknad |

### 7.2 Minimum arkitektoniske figurer

Fra Adnan-review (figurer A–G):

| Figur-ID | Figur | Format | Produseres av | Når |
|---|---|---|---|---|
| Arch-A | Kjellerplan ferdig tilstand (planløsning minilager) | Plan 1:50 | Adnan | Før F2 |
| Arch-B | Tverrsnitt Fjordgata-trapperom med to internhøyder | Snitt 1:50 | Adnan | Før F8-tegning |
| Arch-C | Langsnitt kjeller ferdig med takhøyde-koter | Snitt 1:50 | Adnan + RIB | Før F7-tegning |
| Arch-D | Detalj natursteinsmur ↔ betong ferdig tilstand (vektergang) | Snitt 1:5 | Adnan | Før F8-forskaling |
| Arch-E | Søyleplan med status per søyle (bevares synlig / dekkes / erstattes) | Plan 1:50 | Adnan + Ole Morten | Før F3 |
| Arch-F | Belysningsplan kjeller | Plan 1:100 | Adnan + el-prosjekterende | Før F10 |
| Arch-G | BYA-befaringsplan (5 tidspunkt + agenda) | Tekstdokument | Adnan + Ole Morten | Før uke 46 |

### 7.3 Natursteinsmur-eksponering — tre alternativer forklart

Fra Adnan-review (seksjon om grensesnitt). Byggherre må beslutte.

**Alternativ 1 — Betong jevnt fra gulv til bjelkelag.** Enklest teknisk. Natursteinsmur er skjult innvendig; synlig kun fra utsiden mot Nidelva og mot Fjordgata-fasaden. Vektergang mellom betong og mur er kun for tekniske føringer og tiltrengelighet for inspeksjon.

**Alternativ 2 — Betong kun i nedre del (ca. 1,7 m), naturstein eksponert over murkrona.** Mer autentisk uttrykk — minilager-kunden ser steinmuren som bakvegg mot kanalside. Teknisk krevende: tosidig forskaling øvre del må erstattes med annen løsning (sinusplate eller glass som demper vann/fukt mellom), og klimaskillet blir mer komplekst.

**Alternativ 3 — Åpen vektergang med glassfasade.** Sterkeste bevaringsuttrykk — natursteinsmuren er synlig gjennom glass fra kjellerrommet, og man kan tydelig se overgangen mellom gammel brygge og ny betongkonstruksjon. Teknisk mest krevende: dampsperre og lufttetthet må løses i glassfasaden; fukt- og kondenskontroll er egen prosjektering.

**Byggherres valg per 21.10.2026:** `[TBD — besluttes i statusmøte uke 44 etter konsultasjon med BYA]`. V01 valgte implisitt alternativ 1 uten å nevne at det var et valg.

### 7.4 Forskalingsvalg (A5) — estetisk konsekvens

Fra Adnan-review (punkt 6):

- **Systemforskaling (standard):** regelmessig boltmønster synlig i ferdig overflate. «Mjøstårnet-estetikk». Enklest og billigst.
- **Storskalig tre-form med årer:** bevarer kontakt med trekulturen. Krever egen bestilling og mer tid. 20–30 % dyrere forskaling.
- **Enkelt stålplate:** glatt overflate uten mønster. Krever høyere forskalingskvalitet.
- **Naturstein-inspirert plate:** svært krevende, dyrt. Vurderes bare hvis BYA setter krav om det.

Antall synlige støpeskjøter påvirkes av forskalingsvalg og støpebatch-planlegging (se F8). Beslutning tas i samråd med BYA (A4) som del av BYA-versjonen (Ole Morten).

### 7.5 UU og rømningsveier

Fra Adnan-review (punkt 9):

- **Trinnfri adkomst:** `[TBD — avklares mot rammesøknad. Hvis ikke trinnfri: hvorfor? Dispensasjon fra TEK17 § 12-6?]`
- **Fri bredde gangsone i minilager:** min. 1,5 m anbefalt for vogner med bokspallar.
- **Rømningsveier:** to kjellernedganger etablert i F0.6. Begge må være godkjente rømningsveier (dvs. nå ut i det fri eller til brannseksjonert rom med egen rømningsvei). Avklares i BYA- og brannkonsept-sammenheng.
- **Lux-krav kunstlys:** min. 100 lux i arbeidssone (TEK17 § 13-7), 150 lux i trapperom. Belysningsplan Arch-F dekker dette.

### 7.6 BYA-befaringsplan (K35)

Fra Adnan-review (punkt 7) og Ole Morten-review (bedre praksis 7, 8). Fem foreslåtte befaringstidspunkt:

1. **Etter F3 (rydding fullført):** BYA ser hva som er fjernet og hvordan BEV-elementer er markert. Agenda: dokumentere at kun råttent trevirke er fjernet.
2. **Etter F5 (graving fullført):** BYA ser gravedybden, prøvegraverapport og tilstand av natursteinsmur. Agenda: bekrefte at graving ikke har svekket muren.
3. **Etter F7 (bunnplate støpt og herdet):** BYA ser helhetlig plate, separasjonssjikt mot stein. Agenda: visuell kontroll av at betong ikke er støpt fast til mur.
4. **Etter F8 (yttervegger ferdige):** BYA ser overgangen betong ↔ naturstein i ferdig tilstand. Agenda: natursteinsmur-eksponering (A4-valget) som bygget.
5. **Etter F12 (sluttdokumentasjon):** BYA ser ferdig kjeller. Agenda: avsjekk mot KMF-krav.

Hver befaring har kort agenda og ca. 1 times varighet. Adnan skriver ut dagsorden og tar imot.

---

## 8. Pre-F6: Armeringstegninger som egen flaskehals

Denne seksjonen er ny i v02 og lukker Søbstads show-stopper #1, Stenmos jordtrykk-krav, Kristians formelle-bestilling-mangel og Ole Mortens dokumentasjonsflyt.

### 8.1 Hvorfor dette er en egen fase

Fem av seks reviews (alle unntatt Ain som er utførende) peker på at RIB-produksjonstegninger er den enkelt viktigste flaskehalsen i hele prosjektet:

- **Søbstad:** «vi sender ikke tilbud basert på ca. 150 kg/m³-anslag. 17 tonn stål, ±20 % feil = 300 000–400 000 kr.»
- **Stenmo:** «Jeg kan ikke signere armeringstegning for yttervegg uten geoteknisk bekreftelse av jordparametrene.»
- **Ole Morten:** «Send formell skriftlig bestilling til Ole Stenmo om produksjonstegninger for F6, F7, F8, F9 med avtalt leveringsdato.»
- **Kristian:** «Delevegg-tegningene foreligger ikke ennå. F9 kan ikke starte uten.»
- **Adnan:** «Armeringsmengde for trapperommets betongvegg (to internhøyder) må reflekteres i tegning.»

Pre-F6 er ikke én enkelt oppgave, men en kjede av fire aktiviteter som må skje i rekkefølge.

### 8.2 Arbeidsflyt pre-F6

```
Pre-F6.1 Formell bestilling → Pre-F6.2 Geotekniker bekrefter φ,γ → Pre-F6.3 RIB tegner → Pre-F6.4 Entreprenør priser → Pre-F6.5 RIB signerer tegningssettet
```

**Pre-F6.1 — Formell skriftlig bestilling (K23).**

- Ansvarlig: byggherre.
- Mottaker: Ole Stenmo, Harboe og Leganger AS.
- Innhold: skriftlig bestilling av produksjonstegninger for F6 (fundamenter), F7 (bunnplate), F8 (yttervegger ensidig og tosidig), F9 (delevegger), med avtalt leveringsdato per sett.
- Frist for bestilling: **uke 44 (senest 31.10.2026)**.
- Avtalt leveringsdato per sett: F6 og F7 senest 15.12.2026 (6 uker før F6-oppstart jan 2027); F8 og F9 senest 15.01.2027 (6 uker før F8-oppstart mars 2027).
- Status: Åpen.

**Pre-F6.2 — Geoteknisk bekreftelse av jordparametre (K24).**

- Ansvarlig: byggherre engasjerer geotekniker; RIB forslår kandidat (Multiconsult, Norconsult, Rambøll).
- Innhold: skriftlig bekreftelse av φ = 33° og γ = 17 kN/m³ (fra RIB-notat 13.06.2025), basert på enten (a) jordprøver fra prøvegraving i F4/F5A sendt til lab, eller (b) enkel CPT-sondering i ett punkt langs ytterveggen.
- Frist: før RIB kan ferdigstille F8-tegning (altså senest desember 2026).
- Kostnad `[TBD]`: anslag 30 000–60 000 kr for lab-prøver, 60 000–120 000 kr for CPT.

**Pre-F6.3 — RIB tegner.**

- Ansvarlig: Ole Stenmo.
- Leveranser: armeringsplaner per konstruksjonselement, med dimensjon, kg/m³, overdekning (XS3 min. 50 mm), bøyeplan, forankringer, svelleprofil-plassering, søylegjennomføringer. Produksjonstegning iht. NS 3473.
- Frist: iht. avtalt leveringsdato pr. Pre-F6.1.

**Pre-F6.4 — Entreprenør priser.**

- Ansvarlig: byggherre sender tegningssett til prekvalifiserte betongentreprenører (Søbstad, Veidekke, 1–2 andre).
- Innhold: forespørsel om tilbud på F6, F7, F8, F9 — fastpris der mulig (bunnplate, yttervegger), enhetspris + regulerbart der ikke (fundamenter under vann, grensesnitt mot naturstein).
- Frist: 2–3 uker etter at tegningene er mottatt.

**Pre-F6.5 — RIB signerer tegningssettet som endelig produksjonsunderlag.**

- Ansvarlig: Ole Stenmo.
- Signering er betingelse for at bestilling av materialer kan starte.

### 8.3 Konsekvens hvis Pre-F6 forsinkes

Hvis RIB-tegning for F7 (bunnplate) ikke er klar innen 15.12.2026, forskyves F6- og F7-oppstart ut i februar–mars 2027. Dette er ikke blokkerende for F3 (rydding) eller F4 (dispensasjonssøknad) — begge kan utføres parallelt — men det forsinker ferdigstillelse av kjelleren til Q3 2027 og vanskeliggjør KMF-utbetaling.

### 8.4 Katodisk-prosjektering starter i F7, ikke F10

Fra Kristian-review (F11 merknad 2). Katodisk korrosjonsbeskyttelse har 4–8 ukers prosjekteringstid hos spesialleverandør. Hvis rapporten avslører behov for innstøpte festepunkter i vegg eller bunnplate, er det **for sent** å endre F8-forskaling.

**Ny rekkefølge:**

- **F7.0 (ny underfase):** Kontraher katodisk korrosjonsspesialist (Corrocean, Protea). Spesialist prosjekterer og leverer rapport med antall anoder, plassering, forventet levetid, strømnivåer, overvåkning — og eventuelle krav om innstøpte festepunkter.
- **F8-forskaling:** Innstøpningsgods for katodisk anlegg monteres som del av F8-armering, basert på F7.0-rapport.
- **F11 (ren montasje):** Spesialist monterer anoder og kabling etter F10. Prosjekteringen er allerede gjort.

Ansvarlig for kontrahering: byggherre (K27). Frist: februar 2027.

---

## 9. Faser i rekkefølge — bakeoppskrift-formatet

13 faser (F0–F12, med egen Pre-F6 behandlet i seksjon 8). Hver fase har samme oppsett som v01, med utvidelser der reviews har gitt input.

---

### Fase 0 — Vinterklargjøring og tilrettelegging

**Mål:** Kjelleren er trygg å arbeide i gjennom vinteren. Vann er frostsikret. Midlertidig varm sone (toalett + minikjøkken) finnes i 1. etg. To kjellernedganger (rømningsveier + materialflyt).

**Forutsetninger:** Kristian tilbake fra reise. Beslutning fra byggherre om flytting av toalett/minikjøkken (statusmøte 25.10, Post 05).

**Modell:** B.

**Gates:**

- RIB-gate: Nei.
- Arkeolog-gate: Nei.
- Myndighets-gate: Container-plassering på Fjordgata krever tillatelse fra Trondheim kommune (fortausbruk) — bestill 1 uke i forveien (K06).

**Materialer:**

- OSB-plater, stendere, 2 panelovner (gjenbruk fra 2. etg).
- Isolasjon (**gjenbrukes** fra 2. etg — kast ikke; statusmøte 20.10 Post 09).
- Varmekabler til eksponerte vannrør.
- Rørleggerrekvisita.
- Lensepumpe (min. 500 l/min) + reservepumpe.
- Container 10 m³ × 2.
- Materiale til ny kjellernedgang: trapp/stige, hull i etasjeskillet.
- Byggvarmer for midlertidig oppvarming av kjellerrom under vinterarbeid (ny i v02 — Ain-review 10).

**Steg for steg:**

- [ ] F0.1 — Beslutt endelig posisjon for ny toalett/varmesone i 1. etg (der gammelt kjøkken sto). Marker gulvet med spraymaling. **Beslutning tatt av byggherre i statusmøte uke 44.**
- [ ] F0.2 — Avtal rørlegger (K05): samle vann til varmesone, varmekabler på eksponerte strekk, demontering i 2. etg. **Bestilling senest 28.10.2026 for jobb i uke 45.**
- [ ] F0.3 — Bygg lettvegger rundt varmesonen (stendere + OSB + gjenbrukt isolasjon). Monter 2 panelovner. Test: rommet holder ≥ +5 °C under kaldvær.
- [ ] F0.4 — Demonter eksisterende toalett + minikjøkken i 2. etg. Sorter: gjenbruk, isolasjon til nedforing, resten til container.
- [ ] F0.5 — Fjern eksisterende lysarmaturer i 2. etg og flytt brannslanger (statusmøte 20.10 Post 12). Rørlegger utfører.
- [ ] F0.6 — Ta hull i etasjeskillet 1. etg → kjeller på avtalt posisjon (K07). Monter trapp/stige som tåler min. 150 kg levende last. Dette er rømningsvei nr. 2 og materialvei. **Posisjon besluttes før hull tas** — ikke underveis (Kristian-review F0 merknad 2).
- [ ] F0.7 — Flytt eksisterende kjellertrapp om nødvendig.
- [ ] F0.8 — Bestill container(e), minst 1 uke i forveien (K06). Koordiner med kommunen for fortaustillatelse (5–10 virkedager behandling). **Søknad sendt senest 13.11.2026 for container uke 48.**
- [ ] F0.9 — Installer lensepumpe i laveste punkt. Test: pumpen starter og tømmer vann innen 30 min. **Dokumentert kapasitet** — K33. Reservepumpe på plassen.
- [ ] F0.10 — Skriv vannsikringsnotat (frostbeskyttelse). Arkiver i prosjektmappe. Forsikringsdokumentasjon.
- [ ] F0.11 — Permanent lysopplegg nede i kjeller: 360° dekning. Delvis utført.
- [ ] F0.12 — Byggvarmer leid og installert i kjeller for vinterarbeid uke 44+ (ny i v02).
- [ ] F0.13 — Skytjeneste (OneDrive/Google Drive) etablert for foto og dagsrapport (K32).

**Tidsestimat:** 2 personer × 3–4 arbeidsdager + rørlegger ca. ½ dag. Container-leveranse: separat.

**Kvalitetssjekk før Fase 1 starter:**

- Varmesonen i 1. etg holder min. +5 °C.
- Begge kjellernedganger trygge, godt lys, nødutgang-skilt om nødvendig.
- Lensepumpe virker, med reservepumpe.
- Containere på plass, kommunens tillatelse foreligger.
- Vannsikringsnotat arkivert.
- Byggvarmer i kjelleren fungerer.
- Nødkontaktliste (K31) laminert og hengt opp.
- Skytjeneste satt opp og testet.

**Typiske feil og avbøtende tiltak:**

- Glemme container-søknad 1 uke i forveien → forsinket arbeidsstart. Avbøtende: bestill i uken før F0.1.
- Kaste isolasjon fra 2. etg → nedforing må kjøpes ny. Avbøtende: skriftlig instruks til Ain.
- Plassere kjellernedgang som blokkerer senere massetransport → omgjøring dyrt. Avbøtende: tenk gjennom F3/F5-logistikk før F0.6.
- Ikke dokumentere lensepumpekapasitet → senere mangel på forsikringsdokumentasjon.

**`[KREVER PROFF]`:**

- Rørlegger (F0.2): autorisert, ½ dag, bestilling 1–2 uker, kr `[TBD: indikativt 1 200–1 500/t]`.
- Elektriker (F0.11): hvis nytt lysopplegg kobles til sikringsskap, 1 time autorisert elektriker.

**Figur-placeholder F0-A:** Plantegning 1. etg (ovenfra, 1:50). Posisjon for ny varmesone (skravert), kjellertrapper (blå/rød pil), container-plassering på Fjordgata (grå boks). Mål: avstand mellom kjellernedganger, romdimensjoner, bredde adkomst brannslanger. **Produseres av:** Ole Morten eller Ain som håndskisse.

---

### Fase 1 — Oppmåling, registrering og foto-dokumentasjon

**Mål:** Alle søyler, langsgående tømmerstokker, løse stein, intakte gulvpartier og fundament-rester er registrert. Grunnlag for RIB-signering (F2), arkeolog-dispensasjon (F4) og entreprenør-tilbud.

**Forutsetninger:** Fase 0 fullført.

**Modell:** B.

**Gates:** Ingen.

**Materialer:** Lasermåler (Leica DISTO), målebånd 5 m og 30 m, spraymaling (rød/gul/blå/grønn), nummerede hengelapper vektbestandige, utskrift plantegning kjeller A3/A2, kamera, pren + hammer, notatbok.

**Steg for steg:**

**Steg 1A — Søyleoppmåling (K02, Ole Morten 21.10.2026):**

- [ ] F1.1 — Mål alle søyler med lasermåler fra ett fast referansepunkt (NØ-hjørne av natursteinsmur). Noter N-S og Ø-V avstand. Toleranse ±10 cm.
- [ ] F1.2 — Nummerér: S01, S02, … Spraymal nummeret (gul).
- [ ] F1.3 — Noter per søyle: materiale (stål/betong/rundtømmer), diameter/tverrsnitt, synlig skade. Fotografer.
- [ ] F1.4 — Innerst mot Fjordgata: stålsøyler HUP 150×150×5. Noter materiale/type/dimensjon.
- [ ] F1.5 — Overfør til plan-tegning (A3). Send til RIB og lagre i prosjektmappe (K32).

**Steg 1B — Tømmerstokk-kartlegging:**

- [ ] F1.6 — Gå systematisk gjennom hver langsgående tømmerstokk. Nummerér: L01, L02, … (grønn spray).
- [ ] F1.7 — Per stokk: mål lengde, tverrsnitt, posisjon, bære-indikasjon.
- [ ] F1.8 — Pren-test i min. 3 punkter per stokk. Skalaen 0–3 (0 = full ved, 3 = gjennomgående/brannskadd).
- [ ] F1.9 — Tjukke tverrgående stokker (statusmøte 25.10 Post 02 — bevares): merk BEV (grønn spray) og tegn inn.
- [ ] F1.10 — Fotografer hver stokk med nummerlapp og målestav.

**Tidsestimat for 1B:** 3 dager, ikke 2 (Kristian-review F1 merknad 1 — justert).

**Steg 1C — Løse stein og natursteinsmur:**

- [ ] F1.11 — Merk alle løse steiner (blå spray) X.1, X.2, …. Fotografer.
- [ ] F1.12 — Vurder natursteinsmur-tilstand: sprekker, utbuling. Marker sprekker (rød spray).
- [ ] F1.13 — Fotografer natursteinsmur systematisk — overlappende bilder per vegg.

**Steg 1D — Gulvplanker, kavlegulv og fundament-rester:**

- [ ] F1.14 — Merk intakte gulvplanker (gul spray) Y01, Y02, ….
- [ ] F1.15 — Fotografer kavlegulv systematisk (rutenett 2×2 m).
- [ ] F1.16 — Fotografer fundament-rester fra 1983 med målestav. Noter plassering, tilstand (sprekker, forskaling-mangler).

**Steg 1E — Masseregistrering:**

- [ ] F1.17 — Noter tykkelse og karakter på løsmasse under gulv (visuell overflatevurdering).
- [ ] F1.18 — Noter observasjoner av gjenstander (blikkbokser, rør, keramikk, bein). Hver uvanlig observasjon fotograferes før berøring.

**Steg 1F — Sammenstilling:**

- [ ] F1.19 — Overfør til to tegninger: Tegning 1 (plan) og Tegning 2 (langsnitt).
- [ ] F1.20 — Lag foto-register (regneark). Alle foto arkiveres med dato-prefix i skytjeneste (K32).
- [ ] F1.21 — Send tegninger + foto-register til Ole Morten og Ole Stenmo.
- [ ] F1.22 — Adnan oppretter søyleplan Arch-E med status per søyle (bevares synlig / dekkes / erstattes).

**Kvalitetssjekk før Fase 2:** Som v01, pluss: Arch-E foreligger som utkast til Adnans beslutning (A3).

**Typiske feil og avbøtende tiltak:** Som v01.

**`[KREVER PROFF]`:** Ingen.

**Figurer:** F1-A (plantegning nåværende tilstand), F1-B (langsnitt nåværende tilstand), F1-C (tverrsnitt, ny i v02), Arch-E (søyleplan status, ny i v02).

---

### Fase 2 — RIB-gating for kutting av bærende elementer

**Mål:** Ole Stenmo (RIB) har skriftlig bekreftet, per element (stokk, bjelke, tørrmur-parti), status KUT / STØTTE+KUT / BEV. Dette utløser kuttearbeid.

**Forutsetninger:** F1 fullført. Tegning 1 og 2 levert RIB. Ole Mortens sikringsplan (K03) klar.

**Modell:** B (RIB-arbeid utføres av Stenmo).

**Gates:**

- **RG-1 (bindende for F3):** Skriftlig signering per element. STØTTE+KUT: spesifikasjon av støtte.
- Arkeolog-gate: Nei.
- Myndighets-gate: Nei.

**Materialer:** Etter gating: materialer til midlertidige støtter (trebukker, stag, kiler). Spesifikasjon leveres i RIB-skisse som del av RG-1.

**Steg for steg:**

- [ ] F2.1 — Ole Morten presenterer kjellerplan for RIB. E-post eller befaring.
- [ ] F2.2 — RIB leverer skriftlig svar: liste med status per element. Spesifikasjon av midlertidig støtte med dimensjon og materialvalg (stendere 48×98 mm el. 98×148 mm, underlag OSB-plate for lastfordeling — detaljer per RIB).
- [ ] F2.3 — Prosjektleder arkiverer RIB-bekreftelsen (dato-prefix).
- [ ] F2.4 — Prosjektleder laminerer A4-versjon av RIB-godkjenningen og henger den ved kjellernedgang. **Ain er ansvarlig for at ingen kutter noe uten at laminert A4 henger** — eksplisitt instruks (Kristian-review F2 merknad 2).
- [ ] F2.5 — For STØTTE+KUT: Kristian/Ain skaffer/lager støtten iht. RIB-spesifikasjon (dimensjon, underlag, feste). Monter støtte. Fotografer og send RIB.
- [ ] F2.6 — RIB bekrefter skriftlig at midlertidige støtter er montert korrekt.
- [ ] F2.7 — Oppdater sikringsplan.

**Tidsestimat:** RIB-svartid 3–10 virkedager (realistisk, Kristian-review F2 merknad 1). Montering av støtter: 1 person × ½ dag per støtte.

**Kvalitetssjekk før Fase 3:** Som v01.

**Typiske feil og avbøtende tiltak:** Som v01.

**`[KREVER PROFF]`:** Ingen (RIB-signering del av engasjement).

**Figurer:** F2-A (sikringsplan-snitt, produseres av RIB).

---

### Fase 3 — Rydding og demontering (over gulvnivå)

**Mål:** Alt løst materiale over gulvnivå fjernet. Natursteinsmur stabil med BEV-elementer intakte. Klar til arkeologisk befaring.

**Forutsetninger:** F2 fullført. RIB-bekreftelse per element. Lensepumpe operativ. Kjellernedgang og containere operativt. Kristian fysisk til stede ved første stokk-kapping (UG-1, Kristian-review).

**Modell:** B — men med UG-1 for STØTTE+KUT-elementer.

**Gates:**

- **UG-1 (ny i v02):** Kristian eller RIB-kompetent person fysisk til stede ved kutting av STØTTE+KUT-elementer. Signatur i dagsrapport.
- Arkeolog-gate: Nei for arbeid over gulvnivå. **AG-1** for arbeid under gulvnivå (tilhører F4).
- Myndighets-gate: BYA grønt lys for trevirke frem til tørrmur (statusmøte 22.10 Post 04.01).

**Materialer:** Fein-sag + kjedesag, elektrisk motorsag (anskaffet — én bruker samtidig), slegge, brekkstang, trillebår, kornett. **Vinsjekurv** (lei og test før F3.10, K09): bæresertifikat EN 13157, kapasitet min. 500 kg, bærepunkt verifisert av innleid rigg-ingeniør eller RIB. Container(e) på Fjordgata. Verneutstyr: hjelm, vernesko, hørselsvern, kjedesaghansker, FFP3-maske, visir.

**SJA F3** skrevet før oppstart (K29) — tema: kjedesag, tunglast, UG-1-regel.

**Steg for steg:**

**Steg 3A — Lavrisk-arbeid (kan starte 26.10.2026 iht. statusmøte 22.10 Post 05):**

- [ ] F3.1 — Fjern alt råttent og brannskadd trevirke over tørrmurens overkant. Vedlikehold, ingen gates.
- [ ] F3.2 — Sorter: gjenbruksbrukbart tre stables; råteskadd til container.
- [ ] F3.3 — Daglig dagsrapport: dato, person, hva som er fjernet, foto.

**Arbeidsark til Ain og Marco for uke 44 (K42):** Separat A4 skrevet av Kristian 25.10.2026 med: hva som er lov, hva som ikke er lov, hvem ringe ved tvil, kontaktliste. **Dette er en forutsetning for F3-oppstart** (Kristian-review F3 merknad 1).

**Steg 3B — Gulvplanker og kavlegulvbord:**

- [ ] F3.4 — Fjern intakte gulvplanker Y01, Y02, … (fra F1). Start midten, arbeid mot vegg.
- [ ] F3.5 — Sorter planker.
- [ ] F3.6 — Fjern gjenværende kavlegulvbord. Hvis en bord sitter fast i BEV- eller UKL-stokk — stopp, kontakt Ole Morten.

**Steg 3C — Langsgående tømmerstokker (etter RIB-signering + UG-1 for STØTTE+KUT):**

- [ ] F3.7 — Kontroller midlertidige støtter stabilt.
- [ ] F3.8 — Start med stokk klarert som enklest (lavest risiko). **For STØTTE+KUT-stokk: UG-1 gjelder — Kristian eller RIB-kompetent person fysisk til stede.** Kutt med motorsag i prefabrikkerte lengder 2,0–2,5 m.
- [ ] F3.9 — Mal kote-referanse og L-ID på kuttet stokk (spraymaling).
- [ ] F3.10 — Transport av kuttede stokker (200–300 kg): **vinsjekurv kontrollert senket**, aldri fri fall. Min. 2 personer per operasjon. **«Dropp gjennom gulvåpning» — fjernet fra v02** (Ain-review 1). To varianter: (a) ned til kanalside-vindu i lavvann/springflo via kontrollert nedsenking, (b) opp til gateplan via vinsjekurv.
- [ ] F3.11 — Mellomlagring: mellomlager A (Fjordgata gateplan), B (innvendig sørvegg), C (floa/kanalside — med lekter eller på fast dekke, ikke flytende, Kristian-review F3 merknad 3).
- [ ] F3.12 — Etter hvert kutt: sjekk støtter. Fotografer og send RIB jevnlig.

**Steg 3D — BEV-stokker (bevares):**

- [ ] F3.13 — Dekk til med presenning. Ikke flytt.
- [ ] F3.14 — Fotografer etter omgivende arbeid.

**Steg 3E — Løse stein mot kanalside (over gulvnivå):**

- [ ] F3.15 — Flytt stein X.1, X.2, … til mellomlager B.
- [ ] F3.16 — Hvis en stein er del av tørrmurens funksjonelle fot: STOPP, kontakt Ole Morten (R04).

**Tidsestimat:** 2 personer × 3–5 arbeidsdager. Kristian må være fysisk til stede første dag for stokk-kapping (ikke forhandlingsbart, Kristian-review).

**Kvalitetssjekk før Fase 4:** Som v01, pluss: UG-1-signatur i dagsrapport.

**Typiske feil og avbøtende tiltak:** Som v01, pluss: fri fall av stokker → personskade. Avbøtende: vinsjekurv kontrollert nedsenking regel.

**`[KREVER PROFF]`:**

- Ved tvil om bære-elementer utenfor RG-1: RIB-befaring, kr `[TBD: indikativt 1 500–2 200/t]`.

**Figurer:** F3-A (arbeidsflytplan Fase 3).

---

### Fase 4 — Prøvegraving, arkeolog-befaring og dispensasjonssøknad

**Mål:** Riksantikvaren har gjennomført befaring, mottatt målsatt søknad etter § 8 og innvilget dispensasjon for omfanget. Prøvegraving dokumentert. Søknader for arbeid mot elv (MG-4c) og IG (MG-4a) er innsendt eller forberedt.

**Forutsetninger:** F3 fullført (ryddig for befaring). Målsatte tegninger av graveomfang. Søyleoppmåling inkorporert. RIB-signert graveplan.

**Modell:** B (søknadsarbeid).

**Gates:**

- **MG-1 (Byantikvar):** Grønt lys for trevirke-fjerning (statusmøte 22.10 Post 04). BYA-versjon leveres uke 46 (K35).
- **MG-4b (Riksantikvar/fylke, § 8):** Dispensasjon. Saksbehandling 4–12 uker.
- **MG-4c (NVE/Statsforvalter/havn/miljøenhet):** Flere separate søknader.
- **MG-4a (kommunen, IG):** Forberedes parallelt. Kan ikke avgjøres før rammetillatelse foreligger.

**Materialer:** Spade, krafse, pensel for prøvegraving. Fotostav, GPS/laser. Prøvetakingsposer merket per lag.

**Steg for steg:**

**Steg 4A — Forberedelse til RA-befaring (K15):**

- [ ] F4.1 — Bekreft med Riksantikvaren (Sissel Ramstad Skoglund) at kjelleren er klar. Foreslå dato uke 44–45.
- [ ] F4.2 — Lag infopakke: Tegning 1 og 2, foto-sammenstilling, kort beskrivelse av tiltak, foreløpig graveomfang. **Adnan tilrettelegger befaringsopplegg (Adnan-review 8):** én A4 med «hva vises, hva vi ønsker å oppnå», ansvarlig til stede.
- [ ] F4.3 — Gjennomfør befaring. Adnan + Ole Morten + byggherre til stede. Noter RAs merknader. Avtale eventuell prøvegraving.
- [ ] F4.4 — RA-befaringsnotat skrives innen 3 virkedager (Ole Morten-review bedre praksis 8).

**Steg 4B — Prøvegraving (K14):**

- [ ] F4.5 — Avklar med RA/NIKU om prøvegraving skal utføres av arkeolog eller av byggherre under tilsyn.
- [ ] F4.6 — Grav i 1–2 avtalte punkter til ca. 50 cm. Dokumenter stratigrafi fortløpende. Noter om massene er omrørte eller uomrørte.
- [ ] F4.7 — **Jordprøver** samles i min. 3 punkter og lengs i poser til geoteknisk lab (ny i v02 — Pre-F6.2-forberedelse, lukker Stenmos jordtrykk-krav).
- [ ] F4.8 — Rapport: prøvegraveresultat, konklusjon om massekarakter.

**Steg 4C — Dispensasjonssøknad etter § 8 (K16, MG-4b):**

- [ ] F4.9 — Utarbeide målsatte tegninger av graveomfang (plan + snitt). RIB og PGL bidrar.
- [ ] F4.10 — Formuler søknad: formål, omfang, metodikk, avbøtende tiltak, kompetanse. `[TBD: § 8 verbatim fra Lovdata inkluderes som vedlegg]`
- [ ] F4.11 — Send til Riksantikvaren med kopi til Trøndelag fylkeskommune. Bekreft mottak.
- [ ] F4.12 — Følg aktivt opp etter uke 4. Realistisk saksbehandling 4–12 uker (NIKU-tilrådning kan forlenge).

**Steg 4D — Søknad for arbeid mot elv (K17, MG-4c), parallelt:**

- [ ] F4.13 — Avklar instanser: NVE (vassdragsinngrep), Statsforvalter (naturmangfold), kommunens miljøenhet (vannforurensning), Trondheim havn (grunneier, vektrestriksjon). Formuler søknad(er).
- [ ] F4.14 — Send parallelt med § 8-søknad. Følg opp.

**Steg 4E — Igangsettingstillatelse (K18, MG-4a):**

- [ ] F4.15 — Fjerning av trevirke krever ikke IG. Betongarbeid krever IG — forberedes nå.
- [ ] F4.16 — IG-søknad settes opp (PRO-ansvarsretter 4.1, UK 4.2, SB-ansvarsrett 3.3). Kan ikke sendes før rammetillatelse er innvilget. Oppdater når rammetillatelse foreligger.

**Steg 4F — PRO-ansvarshull og UK avklart (ny i v02, Ole Morten-review):**

- [ ] F4.17 — Ole Morten + byggherre henter ut rammetillatelsessaken, lister opp meldte ansvarsretter, identifiserer hullene (K19).
- [ ] F4.18 — Byggherre spør Trondheim kommune om UK-krav (K20). Hvis krevd: kontraher kontrollforetak.

**Tidsestimat:** Befaring 1 dag. Prøvegraving 1–2 dager. Søknadsutforming 1 uke. Saksbehandling 4–12 uker (kritisk sti).

**Kvalitetssjekk før Fase 5:** Dispensasjon § 8 skriftlig foreligger med vilkår. Tillatelse(r) for arbeid mot elv foreligger. IG-søknad levert (eller forberedt, venter rammetillatelse). Prøvegraverapport. Jordprøver i geoteknisk lab. Avbøtende tiltak (arkeolog til stede) avtalt.

**Typiske feil og avbøtende tiltak:** Som v01.

**`[KREVER PROFF]`:**

- Arkeolog (NIKU/frittstående), prøvegraving og tilsyn: ca. kr `[TBD: 1 200–1 800/t + reise]`.
- Geotekniker: jordprøveanalyse, ca. kr `[TBD: 30 000–60 000 kr]`.
- RIB: graveplan-signering, inkludert i engasjement.

**Figurer:** F4-A (målsatt graveomfang plan + snitt), F4-B (snitt arbeid mot elv).

---

### Fase 5 — Graving og masseflytting

**Mål:** Gulvnivået senket til prosjektert grunnkote (takhøyde min. 3 m fra OK bunnplate — A1). Ca. 130 m³ fast volum fjernet (200 tonn). Grunnforhold dokumentert og godkjent av RIB (RG-2).

**Forutsetninger:** F4 fullført — dispensasjon § 8 og tillatelse for arbeid mot elv. RIB-signert graveplan. Lensepumpe operativ. Containere på plass. Minigraver-beslutning tatt (K08). Deponi-avtale (K11).

**Modell:** B innvendig, A/C for 5C (undervannsarbeid).

**Gates:**

- **AG-1:** Oppfylt via dispensasjon F4.
- **Overvåkningskrav:** Arkeolog til stede. Stansplikt ved funn.
- **MG-4c:** Tillatelse for arbeid mot elv (gjelder 5C).
- **RG-2 (etter graving):** RIB bekrefter grunnforhold egnet for bunnplate.

**Materialer:** Trillebår, kornett, spann. Minigraver med operatør hvis valgt (K08). Lensepumpe + reservepumpe. Containere (bytteordning). Lasermåler. Flytevest/kommunikasjon for 5C.

**SJA F5** skrevet (K29). SJA F5C eget vedlegg for undervannsarbeid.

**Steg for steg:**

**Steg 5A — Oppstart:**

- [ ] F5.1 — Verifiser skriftlig at dispensasjon § 8 og øvrige tillatelser er arkivert. Laminert A4.
- [ ] F5.2 — Mål nåværende grunnkote. Noter.
- [ ] F5.3 — Avtal arkeolog-prosedyre: tilstedeværelse, varsling ved funn, foto.
- [ ] F5.4 — Start lensepumpe. Noter vanninntregning per time (dim. kote +3,20).
- [ ] F5.5 — **Jordprøvetaking for geoteknisk lab** (hvis ikke gjort i F4.7) — Pre-F6.2 forutsetning.
- [ ] F5.6 — Nabovarsel + fotodokumentasjon av nabokjeller + setningsbolter (K22, R01-avbøtende).

**Steg 5B — Graving innvendig (130 m³ fast volum):**

- [ ] F5.7 — Grav i etapper fra midten mot veggene. **Hold min. 50 cm avstand til eksisterende fundamenter uten RIB-signert graveplan for det området** (Stenmo U2 — krav om RIB-angitt tillatt graveprofil per søyle i F6).
- [ ] F5.8 — Graveskråning: rett ned i samme nivå som innvendig veggliv på natursteinsmur (ISY post 03.1).
- [ ] F5.9 — Flytt masser trinnvis: fra graveflate til mellomlager B eller direkte til vinsjekurv/minigraver → container på Fjordgata.
- [ ] F5.10 — Dokumenter: dagsrapport med volum per dag, funn, foto. Deponi-dokumentasjon per container.
- [ ] F5.11 — Ved funn (keramikk, bein, metall, trestruktur ut over 1800-tallet-rester): STOPP, kontakt arkeolog, dokumenter in situ før berøring (R06).
- [ ] F5.12 — Container byttes ved behov (ikke søndag — avtales med leverandør). Transport 6–9 km (ISY 03.5).
- [ ] F5.13 — Når prosjektert grunnkote nådd: kontroller med lasermåler at hele arealet (ca. 90 m²) ligger på rett nivå (toleranse ±50 mm).

**Kapasitetsanalyse (Ain-review 5, Kristian-review F5 merknad 1):**

- Manuell med trillebår og vinsjekurv: 2–3 personer × 5–7 dager hvis alt går uten stopp. Med tidevann, lensepumpe-problem, arkeologstans og én person syk: realistisk 10–14 dager.
- Minigraver med operatør: 5× raskere, ca. 2–3 dager. Kostnad ca. 10 000–15 000 kr/dag + mobilisering.
- Break-even: minigraver billigere ved ≥ 4 arbeidsdager spart. Vurderes K08 før F5-oppstart.
- **Hvis minigraver ikke mulig pga. åpning:** 2–3 personer × 10–14 dager med trillebår. Byggherres beslutning dokumentert.

**Steg 5C — Graving under vann mot kanalen (10 m³) — Modell A/C:**

- [ ] F5.14 — Avtal med fagarbeider / dykker / erfaren grunnarbeider for arbeid under vann (ISY 03.3). Ikke egne folks arbeid.
- [ ] F5.15 — Koordiner med tidevannstabell for Trondheim (sehavniva.no, K39). Arbeid i lavvannsvinduer (2–4 timer/dag).
- [ ] F5.16 — Grav 10 m³ på utside av natursteinsmur mot kanalen, 0–1 m vanndybde, graveskråning 1:3.
- [ ] F5.17 — Dokumenter tilstand av eksisterende fundamenter mot elv (foto med målestav, grunnlag for RIB-vurdering av volum F6/F11).
- [ ] F5.18 — Opplasting og transport.

**Steg 5D — Avslutning av fase:**

- [ ] F5.19 — Rydde arbeidsflaten, pumpe tørr.
- [ ] F5.20 — Kall inn RIB (Ole Stenmo) til befaring. RIB bekrefter skriftlig at grunnen er tilfredsstillende for bunnplate (RG-2).
- [ ] F5.21 — Hvis grunnen ikke tilfredsstillende: avtal med RIB om tiltak (dyp-graving, utskiftning, geotekstil).

**Tidsestimat:** 5–14 dager innvendig avhengig av metode. 5C: 2 fagarbeidere × 2–3 dager tidevann-styrt.

**Kvalitetssjekk før Fase 6:** Prosjektert grunnkote nådd (±50 mm). Ingen funn uten arkeolog. Lensepumpe stabil. Masser transportert (ca. 200 tonn). Fundamenter mot elv fri-gravd og dokumentert. RG-2 OK. **Jordprøvesvar fra lab tilgjengelig (geotekniker-bekreftelse φ, γ).**

**Typiske feil og avbøtende tiltak:** Som v01, pluss: grave nærmere enn 50 cm fra eksisterende søylefot uten RIB-angitt graveprofil → setning + R01 (Stenmo U2).

**`[KREVER PROFF]`:**

- Fagarbeider/dykker for 5C: ca. kr `[TBD: 1 200–1 800/t]`.
- RIB-befaring RG-2: inkludert.
- Arkeolog til stede: ca. kr `[TBD: 10–40 t]`.
- Geotekniker (hvis CPT): ca. kr `[TBD: 60 000–120 000]`.
- Minigraver med operatør (hvis valgt): ca. kr `[TBD: 10 000–15 000/dag]`.

**Figurer:** F5-A (graveprofil og kote-angivelse), F5-B (logistikkplan).

---

### Fase 6 — Søylefundamenter

**Mål:** 25 nye søylefundamenter (200 × 200 × 40 cm — bekreftet) støpt, herdet, dokumentert. Underlag for stålsøylegjennomføringer i bunnplate.

**Forutsetninger:** F5 fullført. **Pre-F6-fase (seksjon 8) fullført** — RIB-produksjonstegning F6 signert, betongleverandør kontrahert, armering levert, geotekniker-bekreftelse foreligger. SB-godkjent kontrahert (modellbeslutning fra 3.3).

**Modell:** A eller C — IKKE ren B.

**Gates:**

- **RG-3 (armering):** RIB inspiserer og signerer armering før betong bestilles.
- **UG-2 (ny i v02):** SB-godkjent fysisk til stede under fundamentstøp.
- **Myndighets-gate:** IG (MG-4a) må være innhentet.

**Materialer:**

- Drenslag 16/32: anslag 6 m³.
- **XPS 50 mm under punktfundamenter: 25 stk, dim. 2000 × 2000 mm, ca. 100 m² total** (bekreftet av Stenmo — korrigert fra 225 m² i v01).
- Forskalingsplater for 25 fundamenter dim. 200 × 200 × 40 cm.
- Armeringsstål B500NC, utførelsesklasse 3, overdekning iht. XS3 min. 50 mm — fra RIB-produksjonstegning.
- AUV-betong B45 MF40 Cl 0,10, utførelsesklasse 3, konsistens min. SF2, segregeringsresistens SR2: 40 m³ (ISY post 05.15).
- Sement-baserte avstandsholdere (ikke plast — Stenmo).
- Termoføler for herdelogg (Stenmo).

**SJA F6** skrevet.

**Steg for steg:**

**Steg 6A — Forberedelse:**

- [ ] F6.1 — Mål opp posisjon for hvert fundament fra NØ-hjørnet. Søyler på samme sted som dagens, dypere.
- [ ] F6.2 — Grav ned for hvert fundament til prosjektert nivå. **Graving nærmere enn 50 cm fra eksisterende søylefot kun etter RIB-angitt tillatt graveprofil per søyle, dokumentert skriftlig** (Stenmo U2). `[KREVER PROFF: minigraver-operatør eller forskalingstekniker]`.
- [ ] F6.3 — Legg ut XPS 50 mm per fundament, dim. 2000 × 2000 mm.

**Steg 6B — Forskaling:** `[KREVER PROFF: forskalingstekniker eller betongbas]`

- [ ] F6.4 — Monter forskalingsramme per fundament. Dim. 200 × 200 cm (bekreftet), tykkelse 40 cm.
- [ ] F6.5 — Juster lodd og nivå.

**Steg 6C — Armering:**

- [ ] F6.6 — Legg armering iht. RIB-produksjonstegning. Overdekning XS3 min. 50 mm, sement-baserte avstandsholdere.
- [ ] F6.7 — Avstandsholdere kontrollert visuelt.
- [ ] F6.8 — Fotografer ferdig armering per fundament.

**Steg 6D — RG-3:**

- [ ] F6.9 — Send foto av ferdig armering til RIB. RIB signerer skriftlig per fundament eller per batch. **Ikke bestill betong før RG-3.**

**Steg 6E — Støping (etappevis, tidevann-tilpasset):** `[KREVER PROFF: SB-godkjent + betongbas + pumpebiloperatør]`

- [ ] F6.10 — Bestill AUV-betong 24–48 t i forveien. Bekreft konsistens SF2 og segregeringsresistens SR2 skriftlig.
- [ ] F6.11 — **UG-2 aktivert:** SB-godkjent fysisk til stede, dagsrapport åpnet. Termoføler plassert.
- [ ] F6.12 — Lensepumpe kontinuerlig drift (min. 500 l/min + reserve).
- [ ] F6.13 — Støp batchvis. **Maks 0,5 m vanndybde i form ved støpstart** (Stenmo). AUV-betong komprimerer selv, liten vibrator ved behov.
- [ ] F6.14 — Topp-nivå tangere underkant ny bunnplate (ISY post 05.1).
- [ ] F6.15 — Betongprøver: min. 3 sylindre per 30 m³, sendes akkreditert lab (Stenmo).
- [ ] F6.16 — Herding: AUV-betong oppnår fasthet raskt. Avform etter min. 3 dager eller iht. leverandørens herdeplan. Hold fuktig. **Herdeloggen må vise at betong ikke faller under +5 °C i de første 24 timene** (Stenmo).
- [ ] F6.17 — Minste herdetid før belastning: 7 dager.

**Steg 6F — Avslutning:**

- [ ] F6.18 — Måle inn topp-koter per fundament. Toleranse NS-EN 13670.
- [ ] F6.19 — Dokumenter: prøveresultater, foto, mengde, batch-nummer, herdelogg.
- [ ] F6.20 — RIB-sluttkontroll for fasen.

**Tidsestimat:** `[KREVER PROFF]`-ressurser ca. 10 arbeidsdager. Total varighet 2–3 uker inkl. herdetid.

**Kvalitetssjekk før Fase 7:** 25 fundamenter støpt, herdet, måleinnmålt. Topp-koter innenfor toleranse. Betongprøver 28-dagers trykk ≥ B45. Herdelogg dokumentert. RIB-sluttkontroll OK.

**Typiske feil og avbøtende tiltak:** Som v01, pluss: starte støp uten UG-2 → avvisning i IG-dokumentasjon og forsikringshull.

**`[KREVER PROFF]`:**

- SB-godkjent (fra entreprenør): hele F6E (ikke timesleie — hel tilstedeværelse).
- Forskalingstekniker: 10 dager.
- Betongbas: 5 dager.
- Pumpebiloperatør: ved behov.
- RIB-befaring RG-3 og sluttkontroll: inkludert.

**Figurer:** F6-A (fundament-plan 25 stk), F6-B (fundament-snitt med XPS 2000×2000 mm).

---

### Fase 7 — Bunnplate (vanntett betong, 450 mm, 115 m³)

**Mål:** Ny vanntett bunnplate helhetlig over hele kjellerarealet (ca. 90 m², sjekk mot endelig graveomfang og trapperom A2). XS3 marint miljø. Alle svelleprofiler og fugeblikk i kant. Dokumentert iht. Byggforsk 520.055 og NS-EN 1992/1997/13670/206.

**Forutsetninger:** F6 fullført. **Pre-F6-fase (seksjon 8) ferdig for F7**. Betongleverandør bekreftet med skriftlig resept. Armering levert. Lensepumpe i drift. Pumpebil-tilkomst skriftlig bekreftet (K12, K13). Katodisk-leverandør kontrahert (K27 — ny i v02, F7.0).

**Modell:** A eller C. «Dette er min viktigste signatur i prosjektet» (Stenmo).

**Gates:**

- **RG-4 (armering):** **Stenmo er fysisk til stede, ikke bare godkjenner foto** (Ole Morten-review supplement). Viktigste armeringskontrollen.
- **RG-5 (ferdig plate):** RIB inspiserer etter avforming.
- **UG-3 (ny i v02):** SB-godkjent fysisk til stede under hele støpedag; svelleprofil montert ≤ 48 t før støp; separasjonssjikt visuelt kontrollert.

**Steg F7.0 — Katodisk-leverandør kontrahert (ny i v02):**

- [ ] F7.0.1 — Byggherre kontraherer Corrocean / Protea eller tilsvarende. Avtale leveringsdato for prosjekteringsrapport: **før F8-forskaling settes** (altså før armering av F7 ferdigstilles).
- [ ] F7.0.2 — Spesialist leverer prosjekteringsrapport med antall anoder, plassering, forventet levetid, strømnivåer, overvåkning, **innstøpningsgods-krav** (Kristian F11 merknad 2).
- [ ] F7.0.3 — Spesialistens mandat eksplisitt: (a) offeranoder eksponert stål (søyler), (b) vurdering av om innstøpt armering i XS3 krever ekstra tiltak (Stenmo U5).
- [ ] F7.0.4 — RIB gjennomgår og godkjenner rapporten.

**Materialer:**

- Drenslag 16/32: 30 m² × 200 mm ≈ 6 m³ (ISY 03.7).
- Forsterkningslag 0/4 (sand): 15 m² × 100 mm ≈ 1,5 m³ (ISY 03.8).
- XPS 50 mm under plate: ca. 350 m² (ISY 03.10).
- XPS 50 mm kantisolasjon mot natursteinsmur: 30 m² (lukket QA-funn 11 — split).
- Radonsperre: ca. 90 m² (lukket QA-funn 10). **Legges alltid uavhengig av dispensasjonsutfall** (Ain-review 9).
- Armering B500NC — iht. RIB-produksjonstegning. **17 tonn stål for 115 m³ plate** (Søbstad-estimat basert på 150 kg/m³).
- Svelleprofil SikaSwell® P Type H: 65 m. Sika-sertifisert montasje, monteres ≤ 48 t før støp (Stenmo).
- Fugeblikk Master VB2 160: 65 m, over svelleprofilen.
- Svellebånd SikaSwell® P Ring 24 NO: 25 stk for søylegjennomføringer.
- Vanntett betong B45 MF40 Cl 0,10 utførelsesklasse 2, pumpbar (konsistens `[TBD: S3 eller S4]`): 115 m³.
- Sement-baserte avstandsholdere.
- Termoføler for herdelogg.
- **Katodisk innstøpningsgods** (iht. F7.0-rapport).
- Herdematter / vinter-utstyr: frosttelt + varmekilde hvis vinter.

**SJA F7** skrevet. Minuttplan støpedag (Kristian-review endring 6).

**Steg for steg:**

**Steg 7A — Forberedelse av undergrunnen:** `[KREVER PROFF: betongbas som koordinator]`

- [ ] F7.1 — Legg ut drenslag 16/32, 200 mm. Komprimer. Kontroller kote.
- [ ] F7.2 — Legg ut forsterkningslag 0/4 sand, 100 mm. Komprimer. Kontroller kote.
- [ ] F7.3 — Monter XPS 50 mm under hele platen. Fugetett med sammenpressede skjøter.
- [ ] F7.4 — Monter XPS 50 mm kantisolasjon stående langs natursteinsmur fra grunn-nivå til prosjektert OK-dekke. Glidesjikt.
- [ ] F7.5 — Legg plast/tett duk mot natursteinsmur (over XPS) der ensidig forskaling kommer. **Festing uten borring eller plugger i stein/mørtel** (Stenmo U4). Selvklebende butylgummitape eller kilefesting. Hindrer sammenstøping (ISY 05.2).
- [ ] F7.6 — Legg ut radonsperre over hele arealet. Overlapp min. 200 mm, teip skjøter med systemgodkjent tape, fold opp min. 300 mm langs vegger. Fotografer før armering legges.

**Steg 7B — Svelleprofil og forberedelse av overgang til vegg:**

- [ ] F7.7 — Marker på platekant hvor yttervegger kommer.
- [ ] F7.8 — Montér SikaSwell® P Type H langs hele kanten (65 m). **Monteres tidligst 48 t før støp** (Stenmo). Fest til armering med plastklips eller bindtråd.
- [ ] F7.9 — Montér fugeblikk Master VB2 160 over svelleprofilen umiddelbart.

**Steg 7C — Armering:** `[KREVER PROFF: betongbas og RIB-tegning]`

- [ ] F7.10 — Legg armeringsnett iht. RIB-produksjonstegning. Over- og underarmering, bøyler, forankringer rundt søyle. 17 tonn totalt.
- [ ] F7.11 — Avstandsholdere (sement-baserte) iht. XS3 min. 50 mm overdekning.
- [ ] F7.12 — Kobl armering på foten av søylene til plate-armering iht. RIB-tegning.
- [ ] F7.13 — Montér SikaSwell® P Ring 24 NO rundt hver av de 25 søylestålrørene.
- [ ] F7.14 — **Monter katodisk innstøpningsgods** iht. F7.0-rapport (ny i v02).
- [ ] F7.15 — Fotografer ferdig armering systematisk — overlappende bilder.

**Steg 7D — RG-4:**

- [ ] F7.16 — **Ole Stenmo kommer fysisk til plassen** for inspeksjon av armering (Ole Morten supplement — ikke bare foto). RIB signerer skriftlig. **Ikke bestill betong før RG-4.**

**Steg 7E — Minuttplan støpedag:** (Kristian endring 6)

Realistisk 115 m³ på én dag:

- 06:30 — SB-godkjent + Kristian + Ain på plassen. Siste kontroll av svelleprofil, radonsperre, armering, lensepumpe.
- 07:00 — UG-3 aktivert, dagsrapport åpnet. Pumpebil på plass, parkeringsforbud effektuert (K13).
- 07:30 — Første betongbil ankommer. Slaprøve (konsistens S3/S4). Hvis avvik — avvis bilen.
- 07:45 — Første pumping starter. Pumpebil leverer 40–60 m³/t ved god tilkomst; realistisk 20–30 m³/t med 25 søylegjennomføringer å manøvrere rundt.
- Hver 30. min: ny bil ankommer. 115 m³ / ca. 7 m³ per bil = ca. 16 biler. Realistisk tid 4–6 timer pumping.
- 08:00 og hver time: vibrator-sjekk + kotekontroll + prøvetaking (3 sylindre per 30 m³ = ca. 12 prøver totalt).
- 13:00–14:00 (anslag): siste bil, siste pumping.
- 14:00–16:00: stålglatt overflate (ISY 05.19).
- 16:00: UG-3 lukket med dagsrapport-signatur. Lensepumpe fortsetter.

**Backup-plan ved pumpehavari eller kø i Fjordgata:** 2 pumpebiler bestilt hvis mulig. Hvis bare én: lang-slange-løsning (60–80 m slange fra alternativ posisjon). Reserveplan avtalt skriftlig med entreprenør før RG-4.

**Steg 7E — Støping (minuttplan over):** `[KREVER PROFF: SB-godkjent + betongbas + pumpebiloperatør]`

- [ ] F7.17 — Bestill vanntett betong B45 MF40 Cl 0,10 utførelsesklasse 2, pumpbar, 115 m³. Skriftlig 48 t i forveien med alle delkrav. Ikke mandag morgen (R07).
- [ ] F7.18 — Vinter-sjekk: hvis T < +5 °C, etabler frosttelt + varme eller utsett. Betongen må ikke fryse i de første 7 dagene (R09).
- [ ] F7.19 — Støp som helhetlig plate i ett kontinuerlig støp (statusmøte 22.10 Post 02). Vibrator for komprimering.
- [ ] F7.20 — Betongprøver iht. plan, akkreditert lab (Stenmo).
- [ ] F7.21 — Stålglatt overflate etter at betong er stiv men ikke herdet (ISY 05.19).
- [ ] F7.22 — Dokumenter avvikshåndtering under støp iht. avviksprotokoll (3.5).

**Steg 7F — Herding:**

- [ ] F7.23 — Dekk med presenning eller frosttelt. Vann daglig eller herdematerialer. Min. 7 dagers våtherding.
- [ ] F7.24 — Ikke betrå platen med last de første 3 dagene. Full belastningskapasitet etter 28 dager.
- [ ] F7.25 — Herdelogg kontinuerlig med termoføler.
- [ ] F7.26 — Overvåk tidevann og flom (R14).

**Steg 7G — Renhold støpeskjøt plate→vegg (ny i v02, Kristian F8 merknad 2):**

- [ ] F7.27 — Før F8-armering starter: eksplisitt renholdssteg av F7-overflate ved svelleprofil-kant. Fjern støv, vann, løs betong. Visuell dokumentasjon.

**Steg 7H — RG-5:**

- [ ] F7.28 — Etter 7 dager: visuell inspeksjon. Sjekk sprekker, overflatefeil, områder uten vibrasjon.
- [ ] F7.29 — Send foto + 7-dagers trykkprøveresultater til RIB. RIB-sluttkontroll og skriftlig OK.

**Tidsestimat:** Forberedelse 2–3 dager. Armering 2–3 dager. RG-4 1–2 dager svartid. Støp 1 dag. Herding min. 7 dager (F8-forberedelse kan starte parallelt).

**Kvalitetssjekk før Fase 8:** Som v01, pluss: UG-3-dagsrapport signert; herdelogg dokumentert; katodisk innstøpningsgods verifisert.

**Typiske feil og avbøtende tiltak:** Som v01, pluss: starte uten pumpebil-tilkomstbekreftelse → avbryter støp midt i. Avbøtende: pumpebil-tilkomst gate for RG-4 (Kristian endring 5).

**`[KREVER PROFF]`:**

- SB-godkjent: hele F7E, 1–2 dager (fullt tilstedeværende).
- Forskalingstekniker / betongbas: 5 dager.
- Pumpebiloperatør: 2 dager.
- Rør/kran-hjelp: 1 dag.
- RIB-befaring RG-4 og RG-5: inkludert; RG-4 **fysisk til stede**.
- Katodisk spesialist for innstøpningsgods: 1–2 dager på plassen.

**Figurer:** F7-A (plan bunnplate armering), F7-B (snitt bunnplate alle lag), F7-C (detalj søylegjennomføring).

---

### Fase 8 — Yttervegger (vanntett)

**Mål:** Alle fire ytterveggene støpt i to seksjoner (nedre ensidig, øvre tosidig). Natursteinsmur som ensidig forskaling i nedre del, med XPS + plast/tett duk som separasjonssjikt. Trapperommets betongvegg (A2) inkludert. Natursteinsmur-eksponering iht. valgt alternativ (A4). Forskalingsvalg iht. valgt alternativ (A5).

**Forutsetninger:** F7 fullført (bunnplate herdet min. 7 dager, RG-5). Pre-F6 F8-tegning ferdig. Geotekniker-bekreftelse φ, γ foreligger. Forskalingssystem bestilt (A5 valgt). Armering levert. Natursteinsmur rengjort og stabil.

**Modell:** A eller C — IKKE ren B.

**Gates:**

- **RG-6 (armering yttervegger):** RIB inspiserer og signerer før støp. **Forutsetter geotekniker-bekreftelse av jordparametre.**
- **UG-4 (nedre del) og UG-5 (øvre del):** SB-godkjent til stede.

**Materialer:**

- Forskalingsplater ensidig: ca. 110 m² (ISY 05.2).
- Forskalingsplater tosidig: ca. 95 m² (ISY 05.3) + trapperom-tillegg iht. A2.
- Steng (tilpasningsforskaling i overgang): 65 lm (ISY 05.4).
- Plast/tett duk mot natursteinsmur: ca. 110 m².
- XPS 50 mm vertikal kantisolasjon mot natursteinsmur: ca. 110 m² (lukket QA-funn 11 — split).
- Armering B500NC Ø16 mm, utførelsesklasse 3, XS3 — iht. RIB-produksjonstegning.
- Vanntett betong B45 MF40 Cl 0,10 utførelsesklasse 2: 52 m³ + trapperom-tillegg.
- Svelleprofil og fugeblikk i støpeskjøt vegg/gulv (montert i F7).
- Katodisk innstøpningsgods for vegger (iht. F7.0-rapport).

**SJA F8** skrevet.

**Steg for steg:**

**Steg 8A — Forberedelse av natursteinsmur:** `[KREVER PROFF: forskalingstekniker]`

- [ ] F8.1 — Rengjør natursteinsflaten. Stålbørste og vann. Fjern løs mørtel og skitt.
- [ ] F8.2 — Monter XPS 50 mm vertikal kantisolasjon fra bunnsåle til topp.
- [ ] F8.3 — Legg plast/tett duk direkte mot naturstein eller over XPS iht. detaljkrav. **Feste kun med selvklebende butylgummitape eller kilefesting øverst/nederst — ikke borring eller plugger** (Stenmo U4). Separasjonssjikt-monteringsanvisning fra Ole Morten følges.

**Steg 8B — Forskaling nedre del (ensidig):** `[KREVER PROFF: forskalingstekniker]`

- [ ] F8.4 — Montér ensidig forskaling langs alle fire yttervegger. Innvendig forskalingliv i prosjektert posisjon. Høyde ca. 1,7 m fra bunnplate til topp natursteinsmur. **Realistisk 7–8 dager, ikke 5** (Søbstad-review). Steng + kileforing for ujamn mur.
- [ ] F8.5 — Montér steng (65 lm) i overgangen (ISY 05.4).

**Steg 8C — Forskaling øvre del (tosidig):**

- [ ] F8.6 — Montér tosidig forskalingssystem fra topp natursteinsmur og opp til bjelkelag mot 1. etg. Varierende høyde pga. nedtrappinger. **Trapperom A2:** betongvegg to internhøyder — egen underfase med utvidet armering og forskaling.
- [ ] F8.7 — Veggtykkelse 250 mm.
- [ ] F8.8 — **Forskalingsvalg iht. A5** — estetisk type bestilles (systemforskaling/treplank/stålplate).

**Steg 8D — Armering:**

- [ ] F8.9 — Legg armering iht. RIB-tegning. B500NC Ø16 mm, utførelsesklasse 3. Overdekning XS3 min. 50 mm. Sement-baserte avstandsholdere.
- [ ] F8.10 — Kobl armering på topp av bunnplate til vegg-armering iht. forankringskrav.
- [ ] F8.11 — Monter katodisk innstøpningsgods for vegger (iht. F7.0-rapport).
- [ ] F8.12 — Fotografer ferdig armering per vegg.

**Steg 8E — RG-6:**

- [ ] F8.13 — Send foto til RIB. **RIB kontrollerer geotekniker-bekreftelse foreligger og signerer skriftlig.** Ikke bestill betong før RG-6.

**Steg 8F — Støping:** `[KREVER PROFF: SB-godkjent + betongbas + pumpebiloperatør]`

- [ ] F8.14 — Bestill B45 MF40 Cl 0,10 utførelsesklasse 2 — 52 m³ + trapperom-tillegg. 24–48 t varsel.
- [ ] F8.15 — **UG-4/UG-5 aktivert.** SB-godkjent fysisk til stede. Dagsrapport åpnet.
- [ ] F8.16 — Støp i etapper om nødvendig. Kaldskjøt kun der svelleprofil er montert.
- [ ] F8.17 — Fyll maks 500 mm lagvis. Vibrér per lag.
- [ ] F8.18 — Nedre del (ensidig mot stein): fyll fra toppen av forskaling, la betong flyte ned mellom forskaling og separasjonssjikt. Visuell kontroll.
- [ ] F8.19 — Betongprøver 3 per 30 m³, akkreditert lab.

**Steg 8G — Herding og avforming:**

- [ ] F8.20 — Herding min. 7 dager våte forhold. Beskytt mot frost. Herdelogg.
- [ ] F8.21 — Avform tidligst etter 3 dager (eller lenger iht. RIB).
- [ ] F8.22 — Visuell inspeksjon: ingen sprekker, kaldskjøter uten svellebånd, segregering. **Sjekk at betong ikke er støpt fast til natursteinsmur** (ved avforming av øvre del).

**Tidsestimat:** Forskaling 7–8 dager × 2 forskalingsteknikere (Søbstad). Armering 3 dager. RG-6 1–2 dager. Støp 1–2 dager etappevis. Herding 7 dager. Total ca. 3,5 uker.

**Kvalitetssjekk før Fase 9:** Som v01, pluss: UG-4/UG-5 dagsrapport signert; sjekk natursteinsmur ikke støpt fast; A4-eksponering utført som valgt.

**Typiske feil og avbøtende tiltak:** Som v01, pluss: Støp uten UG → forsikringshull.

**`[KREVER PROFF]`:**

- SB-godkjent: hele F8F.
- Forskalingstekniker: 2 personer × 7–8 dager.
- Betongbas: 2 dager.
- Pumpebiloperatør: 2 dager.
- RIB-befaring RG-6: inkludert.
- Katodisk spesialist for innstøpningsgods: 1 dag.

**Figurer:** F8-A (snitt yttervegg detaljert), F8-B (plan vegger og forskalingsetapper), F8-C (snitt klimaskille), Arch-B (tverrsnitt Fjordgata-trapperom), Arch-D (detalj naturstein ↔ betong ferdig tilstand).

---

### Fase 9 — Delevegger (lengderetning, nord og sør)

**Mål:** To delevegger i lengderetning (nord og sør), 250 mm tykkelse, bærende for plan 1. **Eksponeringsklasse XS3 eller XC3/XC4 — IKKE XC1** (Stenmo review — ISY 05.9 feilklassifisering lukkes K36).

**Forutsetninger:** F8 fullført. Delevegg-posisjoner iht. RIB-tegning. Betongleverandør og materialer klarert. **K36 lukket** (betongklasse bekreftet skriftlig).

**Modell:** A eller C — IKKE ren B.

**Gates:**

- **RG-7 (armering delevegger):** RIB signerer før støp.
- **UG-5 (gjelder også F9):** SB-godkjent til stede (Stenmo U6).

**Materialer:**

- Forskalingsplater tosidig: ca. 95 m² (lukket QA-funn 5).
- Armering B500NC Ø16 mm iht. produksjonstegning.
- Betong — iht. K36-avklaring. Mest sannsynlig B45 MF40 Cl 0,10 utførelsesklasse 2 (konsistens med yttervegger), 9–20 m³ iht. K37-avklaring etter F5C.

**SJA F9** skrevet.

**Steg for steg:**

- [ ] F9.1 — Forskaling tosidig for delevegger. 250 mm veggtykkelse. Lengderetning.
- [ ] F9.2 — Armering iht. RIB-tegning. Overdekning iht. XS3/XC3 (K36-avklart).
- [ ] F9.3 — **RG-7:** RIB signerer. Ikke støp før RG-7.
- [ ] F9.4 — Bestill betong iht. avklart klasse. **UG-5:** SB-godkjent fysisk til stede. Støp.
- [ ] F9.5 — Herding min. 7 dager. Herdelogg.
- [ ] F9.6 — Visuell inspeksjon og dokumentasjon.

**Tidsestimat:** Forskaling 3 dager. Armering 2 dager. Støp 1 dag. Herding 7 dager. Total ca. 2 uker.

**Kvalitetssjekk:** Som Fase 8 — lodd, rett, kvalitet. UG-5 dokumentert.

**Typiske feil:** Feil betongklasse (K36 ikke lukket). Avbøtende: lukkelig før F9.1.

**`[KREVER PROFF]`:** Som Fase 8 — SB-godkjent, forskalingstekniker, betongbas.

**Figurer:** F9-A (plan delevegger).

---

### Fase 10 — Overflatebearbeiding, syrevasking og isolasjon innvendig

**Mål:** Alle innvendige betongoverflater bearbeidet iht. ISY. Gulv stålglattet, vegger glatt flate, syrevasket. XPS på natursteinsmur over gulvnivå montert.

**Forutsetninger:** F9 fullført, alle betongelementer herdet min. 28 dager. Tvangsgjennomlufting-utstyr på plass (seksjon 6.4). HMS-ansvarlig dag-for-dag navngitt.

**Modell:** B med spesialleverandør for syrevasking.

**Gates:**

- **UG-6:** Tvangsgjennomlufting etablert og testet, HMS-ansvarlig navngitt, evakueringsplan hengt opp.

**Materialer:**

- Fortynnet syre (HCl maks 5 %) for syrevasking, 295 m² (ISY 05.26).
- Nøytraliseringsmiddel (sodaoppløsning 10 %), min. 10 l.
- Vernedusj / spyle-utstyr.
- XPS 50 mm innvendig på natursteinsmur over gulv: ca. 110 m² (lukket QA-funn 11).
- Festematerialer for XPS (ikke-mekaniske mot stein).
- **Tvangsgjennomlufting-vifte og friskluftvifte** (ny i v02 — K43).
- PID-meter for HCl-monitorering.
- Syreresistent heldress, hansker nitril, FFP3-maske syre, visir.

**SJA F10** skrevet med ventilasjonsspesifikasjon fra seksjon 6.4.

**Steg for steg:**

- [ ] F10.1 — Visuell inspeksjon av alle betongoverflater. Noter avvik.
- [ ] F10.2 — Mindre reparasjoner (sprekker < 0,2 mm, mindre porer): injiser med epoksy eller sement-mørtel iht. RIB-anbefaling.
- [ ] F10.3 — **UG-6 aktivert:** Monter tvangsgjennomlufting-utstyr, test, dokumenter.
- [ ] F10.4 — Syrevasking av innvendige betongvegger (295 m² iht. ISY 05.26). `[KREVER PROFF: betongfagarbeider syrevasking]`. Bruk HCl maks 5 %, FFP3-maske syre, hansker nitril, visir, heldress syreresistent. PID-meter overvåker. Alarmgrense 1 ppm → evakuer.
- [ ] F10.5 — Nøytraliser og skyll med vann etter vasking.
- [ ] F10.6 — Syrevasking av gulv (ISY 05.25 ca. 90 m²).
- [ ] F10.7 — Stålglatt gulvoverflate (ISY 05.19) hvis ikke gjort i Fase 7.
- [ ] F10.8 — Monter XPS 50 mm på innvendig side av natursteinsmur fra OK dekke til topp mur (ISY 05.28).
- [ ] F10.9 — Dokumenter med foto hele kjellerflaten.

**Tidsestimat:** 5–8 dager fagarbeider for syrevasking (Kristian F10 merknad 2 — ikke 3–4). XPS-montasje 2 dager egne folk.

**Kvalitetssjekk:** Alle overflater syrevasket, nøytralisert, skyllet. XPS på plass. UG-6-dagsrapport lukket.

**Typiske feil:** Glemme nøytralisering → langvarig surhet, risiko. Avbøtende: alltid skylling. Dårlig ventilasjon → personfare. Avbøtende: tvangsavtrekk + PID-overvåking.

**`[KREVER PROFF]`:**

- Betongfagarbeider syrevasking: 5–8 dager, ca. kr `[TBD]`.
- HMS-ansvarlig navngitt dag-for-dag.

**Figurer:** F10-A (ingen spesifikk).

---

### Fase 11 — Katodisk korrosjonsbeskyttelse (ren montasje)

**Mål:** Offeranodeanlegg prosjektert i F7.0 montert og idriftsatt. Vedlikeholdsplan levert.

**Forutsetninger:** F7.0 prosjektering ferdig; F8-innstøpningsgods på plass; F10 fullført.

**Modell:** Alltid spesialleverandør.

**Gates:**

- **RG-8 (sluttkontroll):** RIB-sluttkontroll av hele kjeller inkl. katodisk anlegg.

**Materialer:** Offeranodesystem iht. F7.0-rapport. Kabling. Overvåkningsboks.

**Steg for steg:**

- [ ] F11.1 — Spesialist monterer støttekonstruksjon, anoder, kabling iht. F7.0-rapport.
- [ ] F11.2 — Idriftsettelse: måling av strøm, spenning, pH i anodeområdet. Dokumentasjon.
- [ ] F11.3 — Spesialist utarbeider vedlikeholdsplan: anodeskift, overvåkning.

**Tidsestimat:** Montering 2–3 dager. Idriftsettelse 1 dag.

**Kvalitetssjekk:** System i drift. Dokumentasjon komplett. Vedlikeholdsplan levert.

**Typiske feil:** Dimensjonering uten riktig vannkjemi-data (brakkvann Nidelva) → anoder forbrukes for raskt. Avbøtende: spesialleverandør med marin erfaring + brakkvann-datagrunnlag (R16).

**`[KREVER PROFF]`:** Katodisk korrosjonsspesialist (ca. kr `[TBD: 150 000–400 000]` totalt F7.0 + F11).

**Figurer:** F11-A (anode-plan).

---

### Fase 12 — Sluttdokumentasjon og overgang

**Mål:** Komplett dokumentasjon levert til byggherre, kommune (byggesak), tilskuddsgivere (KMF, Enova). RIB-sluttattest. Arkeolog-sluttbefaring (hvis krevd). Klar for hovedombygging.

**Forutsetninger:** F11 fullført.

**Modell:** B.

**Gates:**

- **RG-8:** RIB-sluttattest.
- **AG-2:** Arkeolog-sluttbefaring hvis dispensasjon krever det.

**Steg for steg:**

- [ ] F12.1 — Visuell sluttkontroll av hele kjelleren: ingen lekkasjer/sprekker, takhøyde (min. 3 m), alle anoder montert.
- [ ] F12.2 — Systematisk sluttfotografering: alle vegger, gulv, søyler.
- [ ] F12.3 — RIB-sluttbefaring og skriftlig sluttattest (RG-8).
- [ ] F12.4 — Arkeolog-sluttbefaring (hvis krevd).
- [ ] F12.5 — Samle dokumentasjon: RIB-attester RG-1 til RG-8, UG-dagsrapporter UG-1 til UG-6, betong-testresultater, herdelogger, arkeolog-dispensasjon og sluttrapport, katodisk korrosjon-dokumentasjon og vedlikeholdsplan, dagsrapporter, foto-register, mengde-registre.
- [ ] F12.6 — **KMF-sluttdokumentasjonssjekkliste** iht. tilsagnsvilkår (Kristian endring 11 — åpen K44 ny): les KMF-tilsagnet og lag konkret sjekkliste over hva som kreves.
- [ ] F12.7 — **Enova-sluttdokumentasjon** iht. tilsagnsvilkår.
- [ ] F12.8 — Lever komplett dokumentasjonspakke til byggherre, kommune byggesak, KMF og Enova.
- [ ] F12.9 — Oppdater TASKS.md og ARCHIVE.md.

**Tidsestimat:** 2–3 dager inkl. befaring.

---

## 10. Risikoregister

Risikoregisteret bygger på v01 (R01–R24) med fem nye risikoer (R25–R29) og justerte sannsynlighet/konsekvens på eksisterende der roller har gitt input. Sannsynlighet og konsekvens på 1–5-skala.

| # | Beskrivelse | Sanns. | Kost | Tid | Rel.konsekvens | Avbøtende tiltak | Ansvarlig | Fase |
|---|---|---|---|---|---|---|---|---|
| R01 | Setningsskader på naboeiendom (Fjordgata 28/32) under graving | 2 | 4 | 3 | Høy | Nabovarsel + fotodokumentasjon nabokjeller + setningsbolter (K22); graving i etapper med støtting | PGL | F5 |
| R02 | Grunnvann oversvømmer gravearbeid | 4 | 3 | 4 | Lav | Lensepumpe dim. for kote +3,20; AUV-betong; tidevannstabell (K39); reservepumpe | Utfører | F5–F7 |
| R03 | Feil med vanntett sjikt — svelleprofil/fugeblikk feilmontert | 3 | 5 | 5 | Middels | Sika-sertifisert montasje; monteres ≤ 48 t før støp; RIB-kontroll før hvert sjikt lukkes; aldri støpe neste trinn uten RG | RIB + utfører | F7, F8 |
| R04 | Ustabil natursteinsmur raser når støttende masser fjernes | 3 | 3 | 3 | Middels — BYA/vernestatus | Stabiliser løse stein; aldri grave mot murfot uten midlertidig støtte; foto før start; graveretning fra midten utover | PGL + utfører | F5 |
| R05 | Bjelker kuttet uten RIB-signering | 2 | 4 | 3 | Høy | Laminert RG-1-oversikt (Ain-ansvar); sperrebånd rundt BEV; skriftlig arbeidsark K42 | Koordinator | F2, F3 |
| R06 | Arkeologisk funn — menneskebein, skipsdeler, middelaldergjenstander | 3 | 3 | 5 | Høy | Dispensasjon først; beredskapsplan + kontaktliste; stans umiddelbart; eskaleringskjede (5.4) | PGL | F5 |
| R07 | Forsinket/feil betongleveranse | 2 | 3 | 4 | Lav | Skriftlig bekreftelse 24–48 t i forveien; kontaktperson hos leverandør; aldri bestill mandag morgen | Utfører (SB) | F6–F9 |
| R08 | Feil armering — dimensjon, overdekning, retning | 2 | 4 | 3 | Lav | RIB-gater bindende; RIB-tegning på stedet; foto før pumpebestilling | RIB + utfører | F6–F9 |
| R09 | Kald støp med sprekker — støp < 5 °C ufullstendig herding | 3 | 4 | 3 | Lav | Støp kun > 5 °C eller frosttelt + varme; herdeplan; min. 7 dagers herding før nedtemperering; herdelogg med termoføler (Stenmo) | Utfører | F6–F9 vinter |
| R10 | Ulykke i trange rom — lav takhøyde, dårlig ventilasjon, kjedesag | 3 | 3 | 2 | Middels | SHA-plan; SJA per fase; FFP3 ved kapping; ventilasjon via to åpninger; aldri alene; én motorsag-bruker | Koordinator (SHK) | F1–F11 |
| R11 | Forsikringshull — egne folk utfører betongarbeid uten SB-tilstedeværelse | **4** (opp fra 3 — Stenmo + Søbstad) | 5 | 2 | **Høy** (opp fra middels) | **UG-x gates (3.4); SB-godkjent fysisk til stede ved alle F6–F9-støp; dokumentert sentralgodkjenning DiBK; forsikringsgjennomgang K30** | Byggherre | F6–F9 |
| R12 | RA-saksbehandling > 4 uker — kan bli 8–12 uker | 3 | 2 | 5 | Middels — KMF-frist | Start Fase 4 tidligst mulig; komplett søknad; spor aktivt | Byggherre + PGL | F4 |
| R13 | Tømmergjenbruk mislykkes — kuttede bjelker råte innvendig | 3 | 2 | 2 | Middels | Prøvestokk først; vurder tverrsnitt visuelt + pren; alternativt materiale på plan B | PGL | F3 |
| R14 | Flom/springflo under herding — fersk betong oversvømmes | 2 | 4 | 3 | Lav | Følg tidevannstabell; ikke støp i springflo; lensepumpe + nødstopp; tildekking | Utfører | F6, F7 |
| R15 | Byantikvar overraskes av faktisk inngrep | 3 | 3 | 4 | Høy | BYA-versjon uke 46 (K35); 5 befaringer avtalt (Adnan) | Byggherre | F1 → |
| R16 | Katodisk korrosjonsbeskyttelse feildimensjonert for brakkvann | 2 | 3 | 2 | Lav | Spesialist med marin erfaring; dimensjonering basert på faktisk vannkjemi; mandat omfatter både eksponert og innstøpt stål (Stenmo U5) | Utfører (spesialist) | F7.0, F11 |
| R17 | Mangelfull dokumentasjon — § 10-gransking | 3 | 3 | 4 | Høy | Systematisk fotodokumentasjon og skisser av bolverk; supplér notat 15.08.2026 med koordinater | PGL | F1 |
| R18 | **(lukket — Stenmo bekrefter 200×200×40 cm 21.10.2026)** Fundamentdimensjon-motsetning | 1 | 1 | 1 | — | ISY post 05.29 rettes til 2000×2000 mm; XPS-mengde korrigert til 100 m² | **Lukket** | — |
| R19 | Betongleverandør svikter leveranse | 2 | 4 | 3 | Lav | Prekvalifisér 2–3 (K10); backup med rask tilgjengelighet; skriftlig bekreftelse 48 t | Byggherre | F6–F9 |
| R20 | Pumpebil kommer ikke frem i Fjordgata | **3** (opp fra 2 — Søbstad fremhever) | 3 | 2 | Middels | **Måling av gate-bredde (K12); kontakt pumpeleverandør med dimensjon; parkeringsforbudssøknad (K13); backup lang-slange (80 000–150 000 kr tillegg); gate-sjekk som egen gate for RG-4** | Byggherre | F7, F8 |
| R21 | Konflikt mellom egne folk og innleid betongbas | 3 | 2 | 2 | Middels | Skriftlig rollefordeling; SB har siste ord på fagoperasjoner; Kristian som konfliktløser | Byggherre | F6–F9 |
| R22 | Enova/KMF-krav om fagsignatur på ikke-tilstede-dag | 2 | 4 | 2 | Middels | Fagsignatur per operasjon via UG-gater (3.4); alternativt engangsengasjér SB som dekker alle operasjoner | Byggherre | F6–F11 |
| R23 | BEV-stokker ødelegges ved uhell | 3 | 2 | 1 | Middels | Grønn BEV-merking + sperrebånd + presenning; alle instrueres | Koordinator | F3–F11 |
| R24 | Vinterforhold forsinker F6–F9 til 2027 | 4 | 3 | 5 | Middels — tilskuddsfrister | Realistisk vinter-schedule med telt/varme (K40); forberede F0–F5 ferdig i 2026; kommuniser realistisk framdrift til KMF | Byggherre | F6–F9 |
| **R25** | **(ny) Jordparametre φ, γ ikke bekreftet av geotekniker — blokkerer RG-6** | 3 | 3 | 4 | Høy | Geotekniker kontraheres (K24); jordprøver i F4/F5A sendes akkreditert lab eller CPT-sondering før F8-armering | RIB + byggherre | F8 |
| **R26** | **(ny) Forskalingstekniker + betongbas ikke rekruttert innen desember 2026 — Trondheim-markedet er fullt** | 3 | 3 | 5 | Høy — kan forskyve F6 flere uker | Rekruttering starter **nå** (K28); betongentreprenør (Søbstad) kontaktes november; rammeavtale med fleksibel binding | Byggherre | F6 |
| **R27** | **(ny) KMTE ikke sentralgodkjent for betong — Modell B blokkert** | 3 | 2 | 2 | Middels | Sjekk DiBK-register (K26); hvis ikke godkjent: Modell A/C låses, betongentreprenør tar SB | Byggherre | F6–F9 |
| **R28** | **(ny) Delevegger feilklassifisert XC1 i marint miljø — korrosjon over tid, utbedring etter 10–15 år** | 3 | 4 | 2 | Høy langsiktig | RIB + HRP avklarer skriftlig før F9 (K36). Trolig XS3 eller XC3. ISY 05.9 rettes | RIB + HRP | F9 |
| **R29** | **(ny) UK (uavhengig kontroll) ikke avklart før IG-søknad — blokkerer støping** | 3 | 2 | 3 | Middels — forsinker IG | Kontakt kommunen med formell forespørsel (K20); kontraher kontrollforetak hvis krevd; UK-rapport før støp | Byggherre + PGL | F6+ |

---

## 11. Materialflyt og logistikk

### 11.1 Betong — bestilling og leveranse

**Fasthetsklasser per konstruksjonsdel:**

| Konstruksjonsdel | Klasse | Mengde | ISY-post |
|---|---|---|---|
| Fundamenter innvendig (under grunnvann) | AUV-betong B45 MF40 Cl 0,10, utførelsesklasse 3, min. SF2, SR2 | 40 m³ | 05.15 |
| Bunnplate (vanntett) | B45 MF40 Cl 0,10, utførelsesklasse 2, pumpbar S3/S4 | 115 m³ | 05.14 |
| Yttervegger (vanntett) | B45 MF40 Cl 0,10, utførelsesklasse 2, pumpbar | 52 m³ + trapperom-tillegg | 05.16 |
| Delevegger | **Avklares K36 — IKKE XC1. Mest sannsynlig B45 MF40 Cl 0,10 (konsistens med yttervegger) eller XC3/XC4** | 9–20 m³ (K37-avhengig) | 05.9 / 05.17 |
| Fundamenter mot elv (under vann) | AUV-betong B45 MF40 Cl 0,10, utførelsesklasse 3 | `[TBD: K37 etter F5C]` | 05.18 |

**Betongleverandør — ikke valgt pr. 21.10.2026 (K10).** Kandidater i Trondheim-regionen:

- Unicon AS (Nedre Elvehavn) — Søbstad foretrukket, nærmeste
- Franzefoss Betong (synergi — allerede avfallsleverandør)
- NorBetong (dyrere, mer fleksibel på spesialresepter)
- Betong Øst AS

**Bestillingsregler:**

- 24–48 t skriftlig forhåndsvarsel med alle delkrav (fasthet, bestandighet, klorid, konsistens, utførelsesklasse, pumpbarhet).
- AUV: 48–72 t varsel. SF2 og SR2 bekreftet skriftlig.
- Ikke bestill til mandag morgen.
- Kontroller konsistens ved levering (slagprøve). Avvisning hvis utenfor spesifikasjon.
- Sylinderprøver min. 3 per 30 m³, akkreditert laboratorium (ikke lokal kvalitet).
- Reseptbekreftelse fra min. 2 leverandører innhentes før første bestilling (Søbstad-anbefaling).

**Indikative priser (Søbstad, høst 2026, eks. mva per m³ levert):**

- B45 MF40 Cl 0,10 pumpbar: 1 800–2 200 kr.
- AUV-betong B45 MF40 Cl 0,10: 2 400–3 200 kr.
- C25/30 XC1 (hvis valgt for delevegger — IKKE anbefalt): 1 400–1 700 kr.

### 11.2 Armering — innkjøp og lagring

- Bestill etter RIB-produksjonstegning. **17 tonn stål for bunnplate alene** (150 kg/m³ × 115 m³ = 17 250 kg) — Søbstad-estimat.
- B500NC, utførelsesklasse 2 eller 3 iht. post. Dimensjon hovedsakelig Ø16 mm for vegger og delevegger.
- Lagres tørt. Kutt- og bøyeplan iht. RIB-tegning. Ferdig kuttet fra leverandør foretrukket.
- Sement-baserte avstandsholdere (ikke plast — Stenmo). Dokumentert med produktdatablad.

### 11.3 Forskalingsmateriell

- Leies via valgt entreprenør eller egen avtale. Mengder:
  - Fundament: 25 stk 200 × 200 × 40 cm (bekreftet dim.).
  - Vegg ensidig: ca. 110 m².
  - Vegg tosidig: ca. 95 m² + trapperom-tillegg (A2).
  - Steng: 65 lm.
  - Forskaling i vann (fundamenter mot elv): ca. `[TBD: K37]`.
- Forskalingstype iht. A5-valg (systemforskaling / treplank / stålplate).

### 11.4 Stein — håndtering og mellomlagring

Mellomlager-plan:

- **Mellomlager A — Fjordgata (gateplan):** Container(e) 10 m³. Krever kommunal fortaustillatelse (K06).
- **Mellomlager B — innvendig langs sørvegg:** Gjenbruksstein merket X.N (grønn spray), sortert.
- **Mellomlager C — floa/kanalside:** Kuttede langsgående tømmerstokker fra F3, 2–2,5 m lengder, 200–300 kg. **Må være på lekter eller fast dekke, ikke flytende** (Kristian F3 merknad 3). Dekknivå dokumentert.

Steinhåndtering: naturstein 20–80 kg per stein, ergonomisk — ikke kast, legg. Grønn/rød merking for gjenbruk vs. avfall.

### 11.5 Masseflytting — løsmasser

- Totalt ca. 130 m³ fast volum innvendig (ISY 03.1) + 10 m³ under vann (ISY 03.3), ca. 200 tonn (ISY 03.6).
- Containerbytter ikke på søndager — planlegg gravedag-slutt til fredag.
- Transportavstand 6–9 km (ISY 03.5).
- Arkeolog kan kreve sortering/avlevering til NIKU.
- Deponi-avtale: K11 — ikke valgt. **Miljøklasse må vurderes** (forurensede grunnmasser Nidelvens nedre del kan kreve deponi-klasse A eller B, Kristian F5 merknad 2).

### 11.6 Avhending — øvrige materialer

| Material | Mengde (anslag) | Håndtering | Leverandør |
|---|---|---|---|
| Gammel isolasjon (mineralull) | 1–2 m³ | Gjenbrukes som nedforing 1. etg | — |
| Elektriske installasjoner fra kjeller | Liten mengde | Container elektrisk | Franzefoss Gjenvinning |
| Trevirke (ikke gjenbruksbjelker) | Variabel | Container tre | Franzefoss Gjenvinning |
| Kulturhistoriske gjenstander | Ukjent | Avleveres NIKU | NIKU |

### 11.7 Vanntetting — innkjøp og montering

- SikaSwell® P Type H svelleprofil: 65 lm (ISY 05.6). Sika-sertifisert montasje. Monteres ≤ 48 t før støp.
- Master VB2 160 fugeblikk: 65 lm (ISY 05.7). Over svelleprofilen umiddelbart.
- SikaSwell® P Ring 24 NO svellebånd: 25 stk (ISY 05.8).

Monteringen utføres av Sika-sertifisert montør eller etter Sika-anvisning med dokumentasjon. Feilmontert svelleprofil er dyreste reparasjonen (R03). Beskyttes mot fukt-aktivering før støp.

### 11.8 Katodisk — innkjøp og montering

Fra F7.0 (ny i v02):

- Offeranodesystem for marint miljø — type, antall, dim. prosjekteres av spesialist (Corrocean / Protea).
- Spesialistens mandat: (a) offeranoder eksponert stål (søyler), (b) vurdering av innstøpt armering i XS3 (Stenmo U5).
- Innstøpningsgods leveres i F7.0-rapport med monteringsanvisning for F7 og F8.
- Prosjekteringstid 4–8 uker. **Kontraheres i F7, ikke F10** (Kristian F11 merknad 2).

### 11.9 Pumpebil — Fjordgata-logistikk (ny i v02)

Fra Søbstad-review og Kristian endring 5:

- Fjordgata er smal. Betongbil 32 t + pumpebil 35–50 t.
- Krav før F7-støp:
  - Målt gate-bredde ved bygget (K12).
  - Kontakt med pumpeleverandør — hvilken bil-dimensjon sender de.
  - Midlertidig parkeringsforbud (K13) via Trondheim kommune, min. 2 ukers behandlingstid.
  - Vektrestriksjon på kaien/havnegrunn sjekket (del av K17 — Trondheim havn).
  - Backup-plan: lang-slange-løsning (60–80 m) fra alternativ posisjon. Pris-tillegg 80 000–150 000 kr.

Pumpebil-tilkomst er gate-krav for RG-4 (Kristian endring 5).

### 11.10 Forsikring (ny seksjon i v02)

Fra Kristian endring 12, Søbstad forsikringsanalyse:

- Byggherres ansvarsforsikring dekker typisk ikke strukturelle feil begått av fagpersoner uten fagbrev.
- Entreprenørforsikring dekker kun arbeid entreprenøren utfører selv under tilsyn.
- **UG-x-gatene (3.4) sikrer at SB-godkjent er fysisk til stede ved kritiske operasjoner** — dette er forsikringsmessig forutsetning.
- K30: Forsikringsgjennomgang før F6 oppstart. Nabovarsel + fotodokumentasjon av nabokjeller (K22) er del av dekningsgrunnlaget.

---

## 12. Rekkefølgediagram og grov Gantt

### 12.1 Kritisk sti

Hovedkritisk sti går via **arkeolog-dispensasjonen (kulturminneloven § 8)** og **Pre-F6-fasen (armeringstegninger + geotekniker + SB-kontrahering)**:

```
F0 → F1 → F2 (RG-1)
            │
            └─→ F3 (parallelt med)
                │
                └─→ F4 (RA-befaring G1 → søknad § 8 MG-4b, 4–12 uker)
                        └─→ Parallelt: MG-4c (NVE/Statsforvalter), MG-4a (IG)
                        └─→ Parallelt: Pre-F6 (RIB-tegninger + geotekniker + SB)
                                │
                                └─→ F5 (RG-2, krever AG-1 + MG-4c)
                                        │
                                        └─→ F6 (RG-3, UG-2, krever MG-4a) + F7.0 (katodisk start)
                                                │
                                                └─→ F7 (RG-4, UG-3, krever pumpebil-tilkomst)
                                                        │
                                                        └─→ F8 (RG-6, UG-4/5, krever geotekniker)
                                                                │
                                                                └─→ F9 (RG-7, UG-5)
                                                                        │
                                                                        └─→ F10 (UG-6) → F11 → F12 (RG-8)
```

### 12.2 Parallellaktiviteter

- F0 + F1 parallelt.
- F2 (RIB-signering tømmer) parallelt med F4 (dispensasjonssøknad).
- F3 (rydding) parallelt med F4 saksbehandling.
- **Pre-F6 (RIB-produksjonstegninger F6/F7/F8/F9) parallelt med F3+F4** — avgjørende for å ikke tape tid.
- F7.0 (katodisk prosjektering) parallelt med F6/F7.
- Betongleverandør-prekvalifisering kan starte **nå** (ingen gate).
- SB-rekruttering (K28) parallelt med Pre-F6.

### 12.3 Grov Gantt — uker fra 21.10.2026

| Fase | Beskrivelse | Varighet | Uke 43–44 | Uke 45 | Uke 46–48 | Uke 49–52 | Jan 2027 | Feb 2027 | Mar 2027 | Apr 2027 | Mai–jun 2027 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| F0 | Vinterklargjøring | 1–2 uker | ████ |  |  |  |  |  |  |  |  |
| F1 | Oppmåling | 1 uke | ████ |  |  |  |  |  |  |  |  |
| F2 | RIB-signering (RG-1) | 1 uke |  | ████ |  |  |  |  |  |  |  |
| F3 | Rydding over gulv | 2–3 uker |  |  | ████ |  |  |  |  |  |  |
| G1 | RA-befaring |  |  | █ |  |  |  |  |  |  |  |
| F4 | Søknader (§ 8, NVE, IG) | 1 uke + 4–16 uker saksbeh. |  | ████ | ████ | ████ |  |  |  |  |  |
| Pre-F6 | RIB-tegninger + geotekniker + SB | 6–10 uker |  | ████ | ████ | ████ | ████ |  |  |  |  |
| F7.0 | Katodisk prosjektering | 4–8 uker |  |  |  | ████ | ████ |  |  |  |  |
| F5 | Graving | 1–3 uker (avhenger av minigraver) |  |  |  |  | ████ |  |  |  |  |
| F6 | Søylefundamenter | 2–3 uker |  |  |  |  |  | ████ |  |  |  |
| F7 | Bunnplate | 2 uker |  |  |  |  |  | ████ | ████ |  |  |
| F8 | Yttervegger | 3,5 uker |  |  |  |  |  |  | ████ | ████ |  |
| F9 | Delevegger | 2 uker |  |  |  |  |  |  |  | ████ |  |
| F10 | Overflatebeh. + syrevasking | 1,5–2 uker |  |  |  |  |  |  |  | ████ |  |
| F11 | Katodisk montering | 1 uke |  |  |  |  |  |  |  |  | ████ |
| F12 | Sluttdokumentasjon | 1 uke |  |  |  |  |  |  |  |  | ████ |

**Konsekvens:** Realistisk ferdigstillelse Q2 2027 (slutt mai / tidlig juni). KMF-fristen 31.12.2026 nås ikke for fullført kjeller — dokumenter det som er oppnådd. R24 (vinter) + R26 (SB-rekruttering) kan utsette ytterligere.

### 12.4 Vinter-tilpasning

Fase 6–9 krever T > 5 °C eller frosttelt + varme (R09, R24). Realistisk:

- F6 (fundamenter): februar 2027 med frosttelt (K40).
- F7 (bunnplate): februar–mars 2027 med frosttelt.
- F8 (yttervegger): mars–april 2027.
- F9 (delevegger): april 2027.
- F10–F12: april–mai 2027.

Frosttelt + varme: 150 000–280 000 kr (Søbstad). Alternativt: utsett oppstart til mai 2027.

### 12.5 Dokumentasjon til KMF per 31.12.2026 (realistisk)

- Komplett plan v01→v02.
- Oppmåling og registrering fullført (F1).
- RIB-signert sikringsplan (RG-1).
- Dispensasjonssøknad § 8 innsendt (MG-4b).
- RA-befaring gjennomført (G1).
- Fase 3 (rydding) i hovedsak fullført.
- IG-søknad forberedt eller levert.
- NVE-søknad innsendt (MG-4c).
- Pre-F6 i gang: RIB-tegninger F6/F7 under utarbeidelse, geotekniker kontrahert, SB-kontrahert.

---

## 13. Grensesnitt plan ↔ ISY — operasjonalisert

### 13.1 Hvordan planen fungerer sammen med ISY-beskrivelsen

Ole Mortens ISY-beskrivelse (19.10.2026) er NS 3420-postlisten. Den dekker **hva** som skal utføres med mengder og materialspesifikasjoner. Denne planen dekker **rekkefølge, operativ fremgangsmåte, risiko, HMS, byggesak og dokumentasjon** — det NS 3420-formatet ikke rommer.

Fordelt per kapittel:

- **Kapittel 00 (generell del):** QA-funn 1 (ufylte innbydelse-felter). Må fylles ut eller planen tjener som direkte-forespørsel til 3–5 kjente leverandører (Ole Morten anbefaler sistnevnte).
- **Kapittel 03 (grunnarbeider):** Postene 03.1–03.10 dekket operasjonelt av F4 og F5.
- **Kapittel 05 (betongarbeider):** Postene 05.1–05.29 dekket operasjonelt av F6, F7, F8, F9, F10.
- **Kapittel 40 (katodisk):** Post 40.2 dekket av F7.0 + F11.

### 13.2 De 12 QA-funnene — status etter Ole Mortens svar

Alle 12 funn fra v01 har fått Ole Mortens respons (ole_morten.md). Status:

| # | Post | Funn | Ole Mortens vurdering | Status i v02 | Tiltak |
|---|---|---|---|---|---|
| 1 | Kap. 00 innbydelse | Tomme felt, duplikater | Aksepteres — kopi-lim-rester | **Innarbeidet (K38):** Ole Morten fyller ut eller erstatter med direkte-forespørsel-strategi. | HRP i uke 44 |
| 2 | Kap. 00 NS 3420-versjon «xxxx» | Mindre | Aksepteres | **Innarbeidet (K38):** Sett inn «NS 3420, 4. utgave, versjon 2020». | HRP uke 44 |
| 3 | Kap. 03 mengder regulerbare | Vesentlig | Aksepteres med presisering — regulerbar-klausul riktig | **Innarbeidet:** Behold regulerbar. Avklares i F4 (prøvegraving). | PGL |
| 4 | Post 03.9 lengde vs. m³ | Vesentlig | Aksepteres | **Innarbeidet (K38):** Endre til FS4.x m³. | HRP uke 44 |
| 5 | Post 05.9 kg i stedet for m², blandet | Kritisk | Aksepteres og beklager | **Innarbeidet (K38):** Split i tre poster — forskaling (m²), armering (kg), betong (m³). | HRP uke 44 |
| 6 | Post 05.11/05.12 duplikat kode | Vesentlig | Aksepteres delvis, avventer RIB | **Avventer K23:** Omregnes til kg basert på RIB-produksjonstegning. | RIB + HRP |
| 7 | Post 05.13 armering delevegger | Vesentlig | Aksepteres | **Avventer K23:** RIB leverer produksjonstegning. | RIB |
| 8 | Post 05.17 to volumer, tunge tilslag, Cl 1,0 | Vesentlig | Aksepteres med kommentar | **Innarbeidet (K36, K38):** 9 m³ primær, 20 m³ alternativ. «Tunge tilslag» fjernes. Cl 1,0 rettes til Cl 0,10. | HRP + RIB |
| 9 | Post 05.18 duplikat, volum mangler | Kritisk | Aksepteres | **Avventer K37:** Volum oppgis etter F5C. | RIB |
| 9b | Fundamentdim. 200×200 vs. 3000×3000 | Kritisk | Avvises 3000×3000 — bekreftet 200×200×40 cm av Stenmo | **Lukket:** ISY 05.29 rettes til 2000 × 2000 mm. R18 lukket. | **Lukket 21.10.2026** |
| 10 | Post 05.19–05.25 radonsperre, overflate, forskaling i vann | Vesentlig | Aksepteres | **Innarbeidet (K38):** Radonsperre ca. 90 m². Overflatebearbeiding presiseres. Forskaling i vann avklares etter F5C (K37). | HRP + RIB |
| 11 | Post 05.27/05.28 duplikat XPS | Vesentlig | Aksepteres | **Innarbeidet (K38):** 05.27 = XPS under gulv (30 m²), 05.28 = XPS mot yttervegg (110 m²). | HRP uke 44 |
| 12 | Post 40.2 RS uten spesifikasjon | Kritisk | Ikke Ole Mortens post | **Avventer F7.0:** Katodisk spesialist leverer prosjektering som inkorporeres i ISY. | Spesialist + HRP |

### 13.3 Ekstra avklaringer fra v02 (ikke i v01-QA)

- **Delevegger eksponeringsklasse (K36):** Stenmo review avdekker at ISY 05.9 feilklassifiserer delevegger som XC1 (innvendig tørt miljø). Kjellermiljøet er fuktig; korrekt klasse er XS3 eller XC3/XC4. Må avklares av RIB + HRP før F9.
- **Hviletrykk fra natursteinsmur** mangler i planen (Stenmo review). Egenvekten av muren kan sette lateralt trykk mot ensidig forskaling hvis muren settes i bevegelse under graving. Innarbeidet som last-prinsipp i 2.2.
- **Statusmøte 22.10 Post 02:** Beslutning om helhetlig plate reflekteres i ISY 05.14 — oppdater.
- **Statusmøte 22.10 Post 03:** Radonsperre søkes dispensasjon. Post 05.19 beholdes som fallback.

### 13.4 Prispostiller — hva entreprenør skal gi tilbud på

Hovedelementer:

**Timepriser per fagkategori (Søbstad-anslag Trondheim høst 2026, eks. mva):**

- Betongbas: 850–1 050 kr/t.
- Forskalingstekniker: 850–1 000 kr/t.
- Pumpebiloperatør: 900–1 100 kr/t.
- Pumpebil mobilisering: 8 000–14 000 kr (RS).
- Pumpebil per m³: 120–200 kr.
- RIB-fagbas: 1 500–2 200 kr/t.
- Katodisk korrosjonsspesialist: 1 800–2 800 kr/t.
- Kalibrator offeranodeanlegg: 1 600–2 400 kr/t.

**Enhetspriser betong og materialer:** iht. 11.1.

**Rigg og mobilisering:**

- Etablering: 80 000–140 000 kr (RS).
- Riggleie per uke: 10 000–18 000 kr.
- Demobilisering: 30 000–60 000 kr (RS).
- Frosttelt + varme (2 måneder): 150 000–280 000 kr.

**Regningsarbeider:**

- Tilpasning mot irregulær natursteinsmur-profil.
- Reparasjon/overstøping av eksisterende fundamenter mot elv (avhenger av F5C).
- Armeringsforankring i eksisterende fundamenter.
- Spesialtilpasning rundt stålsøylegjennomføringer.

**Grovt totalestimat (Søbstad for F7+F8 Modell C):** 1,1–1,4 MNOK eks. mva. Hele kjellerentreprise (F5–F11, Modell A): 4,5–7,5 MNOK avhengig av grunnforhold, arkeologisk stans, vinterforhold.

---

## 14. Figur-sammenstilling

Følgende figurer er nødvendige for v02-leveransene (dispensasjonssøknad, BYA-versjon, anbudsunderlag). **Ingen skal produseres som SVG/CAD i denne tekstleveransen** — alle er tekstbeskrivelser som realiseres via håndtegning, ChatGPT-rendring eller profesjonell tegning fra RIB/HRP/Adnan/Ain.

Fra v01 (22 figurer) + Adnans 7 arkitekturfigurer (A–G) = 29 totale figur-placeholders.

### 14.1 Operative figurer (fra v01)

| # | Figur | Fase | Perspektiv | Målestokk | Innhold | Produseres av |
|---|---|---|---|---|---|---|
| 1 (F0-A) | Plantegning 1. etg — vinterklargjøring | F0 | Ovenfra, nord opp | 1:50 | Toalett/varmesone, kjellernedganger, container, brannslanger | Ole Morten eller Ain |
| 2 (F1-A) | Plantegning kjeller — nåværende tilstand | F1 | Ovenfra | 1:50 | Søyler fargekodet, stokker, stein, gulvplanker, fundamenter 1983 | Ole Morten |
| 3 (F1-B) | Langsnitt kjeller — nåværende tilstand | F1 | Langsnitt | 1:50 | Natursteinsmur, kavlegulv, bolverk, antatt grunnkote | Ole Morten |
| 4 (F1-C) | Tverrsnitt kjeller — nåværende tilstand | F1 | Tverrsnitt | 1:50 | Breddeprofil, natursteinsmur begge sider, antatt grunnkote | Ole Morten |
| 5 (F2-A) | Sikringsplan — snitt midlertidige støtter | F2 | Langsnitt | 1:20 | L-stokk med støtte, RIB-signeringsboks | Ole Stenmo (RIB) |
| 6 (F3-A) | Arbeidsflytplan Fase 3 | F3 | Ovenfra | 1:50 | Flyt-piler, mellomlager A/B/C, gulvåpning, lensepumpe | Ole Morten / Ain |
| 7 (F4-A) | Målsatt graveomfang — plan | F4 | Ovenfra | 1:50 | Rød skravur for graveområde, prøvegravepunkter | Ole Stenmo + Ole Morten |
| 8 (F4-B) | Snitt arbeid mot elv | F4 | Tverrsnitt | 1:50 | Fundament utside, graveprofil 1:3, tidevannsnivåer | Ole Stenmo |
| 9 (F5-A) | Graveprofil og kote-angivelse | F5 | Tverrsnitt | 1:20 | Gravedybde per sone, min. avstand til fundament | Ole Stenmo |
| 10 (F5-B) | Logistikkplan Fase 5 | F5 | Ovenfra | 1:50 | Vinsjekurv, container, slangetrasé | Kristian / Ole Morten |
| 11 (F6-A) | Fundament-plan (25 stk) | F6 | Ovenfra | 1:50 | X/Y-koordinater, aksesystem, fundamentdim. **200 × 200 cm** | Ole Stenmo |
| 12 (F6-B) | Fundament-snitt | F6 | Vertikalt | 1:10 | XPS **2000 × 2000 mm**, armering, overdekning, søylegjennomføring | Ole Stenmo |
| 13 (F7-A) | Plan bunnplate armering | F7 | Ovenfra | 1:50 | Armeringsraster, forankring søyler, svelleprofil-kant, radonsperre | Ole Stenmo |
| 14 (F7-B) | Snitt bunnplate — alle lag | F7 | Vertikalt | 1:10 | Drenslag, XPS, radonsperre, armering, betong 450 mm, overgang kant | Ole Stenmo |
| 15 (F7-C) | Detalj — søylegjennomføring | F7 | Snitt | 1:5 | Stålsøyle, svellebånd, armering tett om søyle | Ole Stenmo |
| 16 (F8-A) | Snitt yttervegg — detaljert | F8 | Tverrsnitt | 1:10 | Natursteinsmur, plast/tett duk, XPS, betong, svelleprofil + fugeblikk, feste uten borring | Ole Stenmo |
| 17 (F8-B) | Plan vegger og forskalingsetapper | F8 | Ovenfra | 1:50 | 4 vegger, vektergang, steng-overganger, støpeskjøter | Ole Stenmo + forskalingstekniker |
| 18 (F8-C) | Snitt klimaskille | F8 | Vertikalt | 1:10 | Overgang kjeller → 1. etg., isolasjon, dampsperre, lufttetthet | Ole Stenmo eller HRP |
| 19 (F9-A) | Plan delevegger | F9 | Ovenfra | 1:50 | Nord- og sørdelevegg, forankringer | Ole Stenmo |
| 20 (F11-A) | Anode-plan | F11 | Ovenfra | 1:50 | Anoder, kabelføringer, tilkoblingspunkt | Katodisk spesialist |
| 21 | Materialflyt-flytskjema | — | Flytskjema | — | Alle materialstrømmer inn/ut | Kristian / byggherre |

### 14.2 Arkitekturfigurer (nye i v02, fra Adnan review)

| # | Figur | Fase | Perspektiv | Målestokk | Innhold | Produseres av |
|---|---|---|---|---|---|---|
| 22 (Arch-A) | Kjellerplan ferdig tilstand (planløsning minilager) | Før F2 | Plan ovenfra | 1:50 | Romstørrelser, dørbredder, intern kommunikasjonssone, minilager-oppdeling, UU-sjekk | Adnan |
| 23 (Arch-B) | Tverrsnitt Fjordgata-trapperom to internhøyder | Før F8-tegning | Tverrsnitt | 1:50 | Begge internhøyder, adkomstbredde, koteangivelse, trappeareal skilt fra kjellerplan | Adnan |
| 24 (Arch-C) | Langsnitt kjeller — ferdig tilstand | Før F7-tegning | Langsnitt | 1:50 | Takhøyde 3 m med referansekote, fri høyde senter/nord/sør, variasjoner under etasjeskille | Adnan + RIB |
| 25 (Arch-D) | Detalj natursteinsmur ↔ betong — ferdig tilstand (vektergang) | Før F8-forskaling | Snitt | 1:5 | Vektergang som designelement — ferdig tilstand, ikke anleggsdetalj. Belysning, kabelkanal. Iht. valgt alternativ A4. | Adnan |
| 26 (Arch-E) | Søyleplan — status og eksponering per søyle | Før F3 | Plan | 1:50 | Hvilke søyler er bevart synlige, dekkes inn, erstattes. Overflatebehandling per type | Adnan + Ole Morten |
| 27 (Arch-F) | Belysningsplan kjeller | Før F10 | Plan | 1:100 | Kunstlys-layout, lux-krav per sone, armaturer | Adnan + el-prosjekterende |
| 28 (Arch-G) | BYA-befaringsplan (5 tidspunkt + agenda) | Før uke 46 | Tekstdokument | — | Milepæl-basert befaringsopplegg for Byantikvaren | Adnan + Ole Morten |

### 14.3 Fordeling av arbeid

- **Ole Stenmo (RIB):** 13 figurer (nr. 5, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19) — hovedansvar prosjekteringstegninger. Deler nr. 24 (Arch-C) med Adnan.
- **Adnan (arkitekt):** 7 figurer (nr. 22, 23, 24, 25, 26, 27, 28) — alle arkitekturfigurer nye i v02.
- **Ole Morten (PGL):** 4 figurer (nr. 2, 3, 4, 6) — oppmåling og tilstandsregistrering. Bidrar til nr. 7, 26, 28.
- **Kristian / Ain:** 2 figurer (nr. 1, 10, 21) — operasjonell logistikk.
- **Katodisk spesialist:** 1 figur (nr. 20).

### 14.4 T187-læringen — unngå SVG/CAD-forsøk

Fra prosjekthistorikken (T187): Forsøk på å la AI generere SVG/CAD-tegninger har mislyktes gjentatte ganger — resultat blir uleselig og kan ikke brukes profesjonelt. Alle figurer i denne planen er **tekstbeskrivelser** som skal realiseres av navngitt menneske (RIB, Adnan, PGL, Ain) via håndtegning, DWG-arbeid eller profesjonell renskriving. V02 holder seg strengt til dette.

---

## 15. Åpne spørsmål og neste skritt

### 15.1 Prioriterte avklaringer

**Prioritet 1 — blokkerende for F2–F6:**

1. **Fundamentdimensjon-motsetning:** **LUKKET** 21.10.2026 (Stenmo review bekrefter 200 × 200 × 40 cm; ISY 05.29 rettes).
2. **Søyleoppmåling innerst mot Fjordgata (K02).** Pågår 21.10.2026 (Ole Morten). Resultat inkorporeres i Tegning 1.
3. **Formell bestilling av RIB-armeringstegninger F6/F7/F8/F9 (K23).** Senest uke 44.
4. **Geotekniker kontrahert (K24, Pre-F6.2).** Senest desember 2026.
5. **Dispensasjon § 8 (K16, MG-4b).** Senest uke 45. Realistisk 4–12 uker.
6. **SB-godkjenning for F6–F9 (K25, K26).** Variantvalg desember 2026.
7. **PRO-ansvarsretter sjekket (K19) + UK avklart (K20).**
8. **KMTE sentralgodkjenning sjekk (K26).**

**Prioritet 2 — blokkerende for anbud og neste byggesakssteg:**

9. **Betongleverandør prekvalifisert (K10).**
10. **Betongklasse delevegger avklart (K36).**
11. **Pumpebil-tilkomst (K12, K13).**
12. **Katodisk-leverandør kontrahert i F7 (K27).**
13. **Forskalingstekniker + betongbas rekruttert (K28, hard deadline des 2026).**
14. **Forsikringsgjennomgang (K30).**
15. **Alle 12 QA-funn lukket i ISY (K38).**

**Prioritet 3 — kan avklares parallelt med F3–F5:**

16. **Deponi-avtale (K11).**
17. **NVE/Statsforvalter/havn-tillatelser (K17).**
18. **IG-søknad når rammetillatelse foreligger (K18).**
19. **Nabovarsel + fotodokumentasjon (K22).**
20. **Volum fundamenter mot elv (K37, etter F5C).**
21. **Radonsperre-dispensasjon.**
22. **Gnr/bnr verifisert (K01).**
23. **Minigraver-beslutning (K08).**
24. **Vinsjekurv-leie og test (K09).**
25. **Arbeidsark til Ain og Marco uke 44 (K42).**

### 15.2 Neste skritt (konkret, uke-for-uke)

**Uke 43 (pågår, 21.–25.10.2026):**

- Oppmåling søyler (Ole Morten, 21.10) — pågår.
- Felles befaring Ole Morten + Kristian (statusmøte 22.10) — når Kristian er tilbake.
- Ole Mortens kjellernotat med sikringsplan ferdigstilles (25.–26.10).
- Byggherre leser v02, gir tilbakemelding.
- **Byggherre sender formell bestilling av RIB-tegninger (K23).**
- **Byggherre skriftlig forespørsel til Trondheim kommune om UK-krav (K20).**
- **Byggherre sjekker KMTE sentralgodkjenning i DiBK (K26).**
- Byggvarmer leid for kjellerarbeid.

**Uke 44 (26.10–01.11.2026):**

- Kjellerstart mandag 26.10 (Ain + Marco) med lavrisk-arbeid.
- Vinterklargjøring intensiveres (F0).
- Dispensasjonssøknad § 8 forberedes (målsatte tegninger).
- RA-befaring foreslås — Riksantikvar kontaktes (K15).
- **Arbeidsark til Ain og Marco skrevet (K42).**
- **Rørlegger bestilt (K05).**
- **Pumpebil-tilkomstmåling (K12).**
- **Container-søknad sendt kommunen (K06).**
- Kristian fysisk til stede ved første stokk-kapping (UG-1).
- Adnan starter Arch-A, Arch-E.

**Uke 45 (02.–08.11.2026):**

- RA-befaring (ambisiøst).
- RIB-signering sikringsplan (RG-1).
- Dispensasjonssøknad § 8 sendes.
- NVE/Statsforvalter-søknader sendes.
- Ole Morten lukker QA-funn 1, 2, 4, 5, 8, 10, 11 i ISY.

**Uke 46–48:**

- F3 (rydding over gulvnivå) i gang.
- Dispensasjon under saksbehandling.
- BYA-versjon ferdig (K35).
- Betongleverandør prekvalifiseres (K10).

**Uke 49–52:**

- Pre-F6: RIB-tegning F6 og F7 under utarbeidelse.
- Katodisk spesialist kontaktes (K27).
- Betongentreprenør kontaktes for Modell C-tilbud (K25).
- Dispensasjon forhåpentligvis innvilget.
- Forskalingstekniker + betongbas rekrutteres (K28).

**Januar 2027:**

- F5 (graving).
- Pre-F6 ferdig for F6/F7.
- F6 forberedes.

**Februar 2027:**

- F6 og F7 (fundamenter + bunnplate) med frosttelt.
- F7.0 (katodisk prosjektering) ferdig.

**Mars 2027:**

- F8 (yttervegger) start.

**April 2027:**

- F8 ferdig, F9 (delevegger).
- F10 (overflatebearbeiding).

**Mai–juni 2027:**

- F11 (katodisk montering).
- F12 (sluttdokumentasjon).

### 15.3 De 3 viktigste anbefalinger til byggherre etter v02

**1. Send formell bestilling av RIB-armeringstegninger denne uken.** Fem av seks reviewere peker på dette som den enkelt viktigste flaskehalsen. Uten tegninger er ingen entreprenør villig til å prise, Stenmo signerer ikke RG, og hele F6–F9 forskyves. Formell skriftlig bestilling med avtalt leveringsdato er trinn null (K23).

**2. Beslutt modellvalg (A/B/C) for F6–F9 i løpet av november 2026.** Rekrutteringsmarkedet for forskalingstekniker og betongbas i Trondheim-regionen vinter 2027 er stramt (R26). Hvis Modell C velges må Søbstad eller tilsvarende kontaktes nå. Hvis Modell A: komplett anbudsutsendelse må være ute senest desember 2026. Hvis Modell B skal vurderes: KMTE sentralgodkjenning sjekkes i DiBK **først** (K26) — hvis ikke godkjent, er B blokkert.

**3. Åpne byggesak-sporet for IG-søknad nå.** Ikke vent på at rammetillatelsen formelt er innvilget. PRO-ansvarsretter sjekkes (K19), UK-krav avklares med kommunen (K20), og alle vedlegg til IG-søknaden forberedes. Når rammetillatelsen innvilges kan IG-søknaden sendes dag 1. Dette sparer potensielt 6–12 uker på kritisk sti.

---

## 16. Appendiks A — Reviewmatrise

Sporbarhet for alle ca. 70 konkrete endringspunkter fra de seks reviewene. Status i v02: **innarbeidet** (I), **avventer** (A, krever ekstern input), **avvist** (V, med begrunnelse).

### A.1 Ain Hansumae (utførende, 10 funn + 18 spørsmål)

| # | Review-punkt | Hvor i v02 | Status |
|---|---|---|---|
| ain-01 | «Dropp gjennom gulvåpning» er ulykke — spesifiser vinsjekurv og bæresystem | Seksjon 6.5, F3.10 (fjernet frase); K09 | I |
| ain-02 | Pumpebil i Fjordgata — hvem søker parkeringsforbud | K12, K13; 11.9 | I |
| ain-03 | Hvem er sjefen min? Eskaleringskjede og nødkontakt | 5.4, K31 (laminert A4) | I |
| ain-04 | `[KREVER PROFF]` uten leveringstid og avbestilling | 5.2 (full tabell) | I |
| ain-05 | Graving 130 m³ — ingen kapasitetsanalyse | F5 kapasitetsanalyse; K08 minigraver | I |
| ain-06 | Syrevasking — HMS-krav for ventilasjon mangler | 6.4 (konkret kvantifisering); F10 UG-6 | I |
| ain-07 | Tidevannsvindu + betongbestilling ikke koordinert | F7 minuttplan; K39 (tidevannstabell) | I |
| ain-08 | STØTTE+KUT — hvem bygger bukk, dimensjon | F2.5 (RIB-spesifikasjon); UG-1 | I |
| ain-09 | Radonsperre — er den med eller ikke | F7 materialliste (legges alltid); 2.3 | I |
| ain-10 | Lunsj, do, vinterdager — ingen daglig logistikk | 5.3 (daglig logistikk) | I |
| ain-S01–18 | 18 spørsmål før første arbeidsdag | Primært dekket i 5.3, 5.4, 6.2, K42 | I |
| ain nekt 1 | F3.8–F3.10 krever RG-1 laminert + vinsjekurv | UG-1, K09, K31 | I |
| ain nekt 2 | F5 krever dispensasjon + minigraver + vinsjekurv | F5.1 verifisert; K08, K09 | I |
| ain nekt 3 | F6.2 krever RIB-tegning og avklart dimensjon | **Lukket:** 200×200 bekreftet; Pre-F6 | I |
| ain nekt 4 | F7 krever RG-4 + pumpebil + frosttelt + 2 erfarne | UG-3, K12/K13, K40, SB-krav | I |
| ain nekt 5 | F8 krever skriftlig separasjonssjikt-instruks | Stenmo U4; Ole Morten anvisning | I |
| ain nekt 6 | F10 krever ventilasjonskrav + testet | 6.4, UG-6 | I |

### A.2 Kristian Brandsegg (koordinator, 20 koordineringspunkter + 12 endringer)

| # | Review-punkt | Hvor i v02 | Status |
|---|---|---|---|
| kri-F0.1 | Rørlegger ikke bestilt | K05 | I |
| kri-F0.2 | Kjellernedgang-posisjon henger | K07 | I |
| kri-F0.3 | Container-tillatelse tar tid | K06 | I |
| kri-F1.1 | Steg 1B tidsestimat urealistisk — 3 dager | F1 (3 dager, ikke 2) | I |
| kri-F1.2 | Foto-register uten kameraansvar/skytjeneste | K32 | I |
| kri-F2.1 | RIB-svartid 3–5 dager optimistisk | F2 (3–10 virkedager) | I |
| kri-F2.2 | Laminert A4 — hvem henger opp (Ain-ansvar) | F2.4 (eksplisitt Ain-ansvar) | I |
| kri-F3.1 | Lavrisk-start krever at Ain/Marco vet grenser | K42 (arbeidsark) | I |
| kri-F3.2 | Vinsjekurv ikke bestilt | K09 | I |
| kri-F3.3 | Mellomlager C ikke vurdert mot tidevann | F3.11 (lekter/fast dekke) | I |
| kri-F4.1 | § 8-søknad — ingen navngitt forfatter | F4.9–F4.11 (Ole Morten + byggherre); K16 | I |
| kri-F4.2 | Saksbehandling optimistisk | 12.3 Gantt justert; R12 | I |
| kri-F5.1 | Minigraver-beslutning må tas nå | K08 | I |
| kri-F5.2 | Deponi-avtale er ikke triviell | K11; 11.5 (miljøklasse) | I |
| kri-F6.1 | Fundamentdim ikke avklart av byggherre | **Lukket** 21.10 (Stenmo review) | I |
| kri-F6.2 | `[KREVER PROFF]` pris ikke estimert | 13.4 (Søbstad priser); K28 | I |
| kri-F7.1 | 115 m³ på 1 dag — pumpekapasitet mangler | F7E minuttplan | I |
| kri-F7.2 | Fjordgata-tilkomst ikke operasjonelt planlagt | 11.9; K12, K13 | I |
| kri-F8.1 | Ensidig forskaling for lett behandlet | F8.4 (7–8 dager); Søbstad bekreftet | I |
| kri-F8.2 | Renholdssjekk støpeskjøt plate↔vegg | F7.27 (nytt steg) | I |
| kri-F9.1 | Betongklasse-uklarhet må løses før F9 | K36 | I |
| kri-F9.2 | Delevegger som bærer — RIB-tegning | Pre-F6; K23 | I |
| kri-F10.1 | Syrevasking HMS — ventilasjon | 6.4 | I |
| kri-F10.2 | «3–4 dager» urealistisk — 5–8 dager | F10 (5–8 dager) | I |
| kri-F11.1 | Katodisk-leverandør ikke kontaktet | K27 | I |
| kri-F11.2 | Kontrahere katodisk i F7, ikke F10 | F7.0 (ny underfase) | I |
| kri-F12.1 | Sluttdokumentasjon til KMF ikke definert | F12.6 (K44 sjekkliste) | I |
| kri-F12.2 | Løpende framdriftsrapport mangler | K34 (ukentlig melding) | I |
| kri-M01 | Rørlegger | K05 | I |
| kri-M02 | Container-søknad | K06 | I |
| kri-M03 | Deponi-avtale | K11 | I |
| kri-M04 | Pumpebil-tilkomst sjekk | K12 | I |
| kri-M05 | Betongleverandør | K10 | I |
| kri-M06 | Forskalingstekniker + betongbas | K28 | I |
| kri-M07 | Katodisk-leverandør | K27 | I |
| kri-M08 | SB-godkjenning | K25, K26; 3.3 | I |
| kri-M09 | Forsikringsgjennomgang | K30; 11.10 | I |
| kri-M10 | Minigraver | K08 | I |
| kri-M11 | Vinsjekurv | K09 | I |
| kri-M12 | Nabovarsel + fotodok | K22 | I |
| kri-M13 | Gnr/bnr | K01 | I |
| kri-M14 | Arkeolog (NIKU) | K14 | I |
| kri-M15 | NVE/Statsforvalter/havn | K17 | I |
| kri-M16 | IG | K18 | I |
| kri-M17 | Arbeidsark Ain/Marco uke 44 | K42 | I |
| kri-M18 | HMS-ansvarlig navngitt per dag | 6.2 (fase-tabell) | I |
| kri-M19 | SJA per fase | K29; 6.3 | I |
| kri-M20 | Nødkontaktliste laminert | K31; 5.4 | I |
| kri-E01 | A4 arbeidsark Ain/Marco | K42 | I |
| kri-E02 | HMS per fase navngitt + stedfortreder | 6.2 | I |
| kri-E03 | SJA-krav per fase | 6.3 | I |
| kri-E04 | Bestillingsliste med dato og ansvarlig | 5.1 koordineringsmatrise | I |
| kri-E05 | Fjordgata-tilkomst som egen gate i F7 | RG-4 forutsetter K12/K13 | I |
| kri-E06 | Støpedag minutt-for-minutt F7 | F7E minuttplan | I |
| kri-E07 | Katodisk kontrahert i F7 ikke F10 | F7.0 | I |
| kri-E08 | Syrevasking 5–8 dager + ventilasjon | F10; 6.4 | I |
| kri-E09 | Ain ansettelsesforhold avklart | K41 | A |
| kri-E10 | Ukentlig framdriftsmelding | K34 | I |
| kri-E11 | KMF/Enova-krav sjekket | K44 (ny) | A |
| kri-E12 | Løs forsikringshull før F6 | K30, UG-x gates | I |
| kri — Kristian fysisk første stokk-kapp | UG-1 | I |

### A.3 Ole Morten Lagmannssveen (PGL, 12 QA-svar + 6 MÅ + 6 BØR)

| # | Review-punkt | Hvor i v02 | Status |
|---|---|---|---|
| om-QA1 | Innbydelse Kap. 00 tom | K38 (HRP uke 44) | I |
| om-QA2 | NS 3420-versjon | K38 | I |
| om-QA3 | Kap. 03 regulerbare mengder | 13.2 (behold regulerbar) | I |
| om-QA4 | Post 03.9 lengde vs. m³ | K38 | I |
| om-QA5 | Post 05.9 split i tre | K38 | I |
| om-QA6 | Post 05.11/05.12 duplikat | K23 avventer RIB | A |
| om-QA7 | Post 05.13 armering delevegger | K23 avventer RIB | A |
| om-QA8 | Post 05.17 to volumer, tunge tilslag | K36, K38 | I |
| om-QA9 | Post 05.18 duplikat volum | K37 avventer F5C | A |
| om-QA9b | Fundamentdim 200×200 | **Lukket** Stenmo | I |
| om-QA10 | Post 05.19–05.25 | K38 + K37 | I/A |
| om-QA11 | Post 05.27/05.28 duplikat XPS | K38 (split) | I |
| om-QA12 | Post 40.2 RS katodisk | F7.0 avventer | A |
| om-MÅ1 | PRO-ansvarskart | 4.1; K19 | I |
| om-MÅ2 | UK-avklaring | 4.2; K20 | I |
| om-MÅ3 | SB for betong under Modell B | 3.3; K25/K26 | I |
| om-MÅ4 | Trehodet IG-bilde | 4.3 (MG-4a/b/c) | I |
| om-MÅ5 | ISY QA-funn lukket | K38 (tabell 13.2) | I |
| om-MÅ6 | Fundamentdim skriftlig | **Lukket** | I |
| om-BØR1 | BYA-versjon uke 46 | K35 | I |
| om-BØR2 | RA-befaringsnotat | F4.4 (3 virkedager) | I |
| om-BØR3 | Gantt med RA-dato | 12.3 (justert) | I |
| om-BØR4 | SHA-plan / SJA | 6.1; K29 | I |
| om-BØR5 | Armeringstegning-bestilling formalisert | K23; Pre-F6 | I |
| om-BØR6 | Gnr/bnr | K01 | A |
| om-PGL — RG-4 fysisk til stede | F7.16 | I |
| om-PGL — Modell B grense | 3.2 (fasetabell) | I |

### A.4 Adnan (arkitekt, 10 mangler + 8 endringer + 7 figurer)

| # | Review-punkt | Hvor i v02 | Status |
|---|---|---|---|
| adn-01 | Takhøyde 3 m referansekote | 2.4; A1; Arch-C | I |
| adn-02 | Trapperom to internhøyder | 2.4; A2; Arch-B | I |
| adn-03 | Plangeometri — bunnplan ferdig tilstand | Arch-A | I |
| adn-04 | Søyler materialmix og eksponering | 7.1 A3; Arch-E | I |
| adn-05 | Vektergang — betong vs. naturstein | 7.3 (3 alternativer); A4; Arch-D | I |
| adn-06 | Bevaringsestetikk vs. betonguttrykk | 7.4 A5 (forskalingsvalg) | I |
| adn-07 | BYA-grensesnitt befaringsplan | 7.6; K35; Arch-G | I |
| adn-08 | RA-befaring tilrettelegging | F4.2 (Adnan tilrettelegger) | I |
| adn-09 | UU og TEK17 | 7.5 (sjekkliste) | I |
| adn-10 | Dagslys og arbeidsplass | Arch-F; 7.5 | I |
| adn-E1 | Kote-definisjon | 1.4 hard-coded; 2.4 | I |
| adn-E2 | Trapperom eget romelement | 2.4 | I |
| adn-E3 | Natursteinsmur-eksponering som designvalg | 7.3 (3 alternativer) | I |
| adn-E4 | Søyleplan Arch-E | F1.22; Arch-E | I |
| adn-E5 | UU-sjekkliste appendiks | 7.5 | I |
| adn-E6 | BYA-befaringsplan i Gantt | 7.6; K35 | I |
| adn-E7 | Forskalingsvalg arkitektonisk note | 7.4; A5 | I |
| adn-E8 | Koteangivelse trapperom i F1-A/B | Arch-B utvider F1-A/B | I |
| adn-F-A | Kjellerplan ferdig | Arch-A | I |
| adn-F-B | Tverrsnitt trapperom | Arch-B | I |
| adn-F-C | Langsnitt kjeller ferdig | Arch-C | I |
| adn-F-D | Detalj naturstein ↔ betong | Arch-D | I |
| adn-F-E | Søyleplan status | Arch-E | I |
| adn-F-F | Belysningsplan | Arch-F | I |
| adn-F-G | BYA-befaringsplan | Arch-G | I |

### A.5 Ole Stenmo (RIB, 6 uakseptable + 11 endringer + Modell B-vurdering)

| # | Review-punkt | Hvor i v02 | Status |
|---|---|---|---|
| sten-U1 | F3.8 kutting uten fagperson til stede for STØTTE+KUT | UG-1; 6.5 | I |
| sten-U2 | F6.2 graving nær søyler uten RIB-signert graveprofil | F5.7 (50 cm regel); F6.2 (RIB-angitt profil); R28 | I |
| sten-U3 | Modell B F7.15–F7.18 uten SB tilstede | 3.2 (modell låst for F7); UG-3 | I |
| sten-U4 | F8.3 plugger i mørtelsfuger | 2.3; F7.5; F8.3 (ingen borring) | I |
| sten-U5 | F11 katodisk uten mandat for innstøpt stål | F7.0.3 (mandat utvidet) | I |
| sten-U6 | F9 uten SB-krav | 3.2 (F9 modell låst); UG-5 | I |
| sten-E1 | Fundamentdim 200×200 bekreftet, ISY 05.29 rettes | 2.3; 11.1; R18 lukket | I |
| sten-E2 | Geotekniker inn | K24; Pre-F6.2; R25 | I |
| sten-E3 | SB-godkjenning navngis | 3.3; K25/K26 | I |
| sten-E4 | STØTTE+KUT faglig tilstede | UG-1; F3.8 | I |
| sten-E5 | Separasjonssjikt-anvisning | F7.5; F8.3; Ole Mortens anvisning | I |
| sten-E6 | Herdelogg termoføler | F6.16; F7.25; herdeplan | I |
| sten-E7 | Betongprøver akkreditert lab | F6.15; F7.20; F8.19 | I |
| sten-E8 | Svelleprofil fuktbeskyttelse | 2.3; F7.8 (≤ 48 t) | I |
| sten-E9 | Katodisk mandat utvidet | F7.0.3 | I |
| sten-E10 | F6.2 graveavstand | F6.2 (RIB-angitt profil) | I |
| sten-E11 | Delevegger XC1 → XS3/XC3 | K36; 2.3; R28 | I |
| sten-ModB | Modell B signerbarhet F6–F9 | 3.2 (låst Modell A/C); 3.4 UG; 3.5 avviksprotokoll | I |

### A.6 Søbstad (entreprenør, 5 show-stoppere + 8 krav)

| # | Review-punkt | Hvor i v02 | Status |
|---|---|---|---|
| sob-SS1 | RIB-produksjonstegninger mangler | Pre-F6 egen fase; K23 | I |
| sob-SS2 | Fundamentdim ikke lukket | **Lukket** Stenmo | I |
| sob-SS3 | ISY QA-funn ikke lukket | K38; 13.2 | I |
| sob-SS4 | § 8-dispensasjon ikke innsendt | K16 (uke 45) | I |
| sob-SS5 | SB-ansvarshierarki ikke avklart | 3.3; K25/K26 | I |
| sob-K1 | RIB-tegninger krav 1 | K23 | I |
| sob-K2 | Fundamentdim avklart | **Lukket** | I |
| sob-K3 | Revidert ISY | K38 | I |
| sob-K4 | SB-arrangement skriftlig | 3.3; K25 | I |
| sob-K5 | § 8-søknad innsendt | K16 | I |
| sob-K6 | Pumpebil-tilkomst avklart | K12, K13; 11.9 | I |
| sob-K7 | Betongleverandør prekvalifisert | K10 | I |
| sob-K8 | Grunnvannsanalyse (geotekniker) | K24 | I |
| sob-Mod A | 18–25 % risikopåslag ved fastpris | 13.4; Søbstad orientering | I (notert) |
| sob-Mod B/C | Forsikring + SB-ansvar | 3.2, 3.3, 11.10, R11 | I |
| sob-Pumpebil | Fjordgata-logistikk detaljert | 11.9 | I |
| sob-Leverandør | Unicon foretrukket, resept før bil | 11.1 | I |
| sob-Marked | Kapasitet Trondheim 2027 | 12.4; R26 | I |
| sob-Minimum | Budsjettkalkyle | Notert, byggherres valg | A |

### A.7 Oppsummering

- **Totalt endringspunkter behandlet:** ca. 125 (noen reviews overlapper, matrisen angir hver forekomst).
- **Innarbeidet (I):** ~118.
- **Avventer (A, ekstern input krevd):** 7 (ISY QA-funn 6, 7, 9, 10, 12 — avventer RIB-tegninger og F5C; K41 Ain ansettelsesforhold; K44 KMF-sluttdokumentasjon; sob-Minimum som er byggherres valg).
- **Avvist (V):** 0. Alle review-punkter er anerkjent som gyldige.

Dette er sporbarhet. Hvert punkt i hver review har plass i v02 — enten som eksplisitt endring (I) eller som åpen K-oppgave (A) som blir fulgt opp.

---

## 17. Appendiks B — Endringslogg v01 → v02

### B.1 Strukturelle endringer (nye seksjoner i v02)

| Seksjon | Status i v01 | Endring |
|---|---|---|
| 3. Utførelsesmodeller re-tegnet per fase | A/B/C like alternativer | Modell låst per fase. F6–F9 krever A eller C med SB. UG-gates introdusert. |
| 4. Byggesak tre løp + ansvarsrett | Én MG-4 | Splittet i MG-4a (IG), MG-4b (§ 8), MG-4c (NVE). PRO, UK, SB ansvarsmatrise. |
| 5. Koordineringsmatrise | Spredt i fasene | Samlet matrise K01–K44 med ansvar og deadline. Bestillingsliste med leveringstid. |
| 6. HMS og SJA | Nevnt kort | Dedikert seksjon med SHK, HMS-ansvarlig per fase, SJA-krav, ventilasjon F10 kvantifisert, tunglast-regler, nabovarsel. |
| 7. Arkitektur | Ikke dekket | Dedikert seksjon med 10 beslutninger (A1–A7), 7 arkitekturfigurer (Arch-A til Arch-G), natursteinsmur-eksponering som 3 alternativer. |
| 8. Pre-F6 armeringstegninger | Åpen i F6-forutsetninger | Egen underfase med 5 trinn, geotekniker-kontrahering, katodisk start. |
| 10. Risikoregister | R01–R24 | R25–R29 nye; R11, R20 justert opp; R18 lukket. |
| 13. Grensesnitt plan ↔ ISY | ISY-mapping | Operasjonalisert med Ole Mortens 12 QA-svar i tabellform og status per punkt. |
| 14. Figur-sammenstilling | 22 figurer | 29 figurer (nye arkitekturfigurer Arch-A–G). |
| 16. Appendiks A — Reviewmatrise | Fantes ikke | 125 review-punkter kartlagt, I/A/V-status. |
| 17. Appendiks B — Endringslogg | Fantes ikke | Denne seksjonen. |

### B.2 Lukkede åpne spørsmål fra v01

| v01-spørsmål | Status i v02 | Hvordan |
|---|---|---|
| Fundamentdimensjon 200×200 vs. 3000×3000 | **Lukket** | Stenmo bekrefter 200×200×40 cm; ISY 05.29 rettes til 2000×2000 mm; XPS-mengde korrigert fra 225 til 100 m². |
| Hvem er SB for betongarbeider | **Delvis lukket** | Modell per fase låst (3.2); varianter definert (3.3); K25/K26 for valgaktivering. |
| Hvem skriver § 8-søknad | **Lukket** | Ole Morten + byggherre, deadline uke 45 (K16). |

### B.3 Nye koordineringsoppgaver (K-numre introdusert i v02)

K01–K44 totalt (hvor K43 og K44 er nye bestillinger relatert til ventilasjonsutstyr F10 og KMF-sluttdokumentasjon-sjekkliste). Full liste i seksjon 5.1.

### B.4 Endrede tidsestimater

| Fase | v01 | v02 | Begrunnelse |
|---|---|---|---|
| F1 Steg 1B | 2 personer × 2 dager | 2 personer × 3 dager | Kristian F1 merknad 1 |
| F2 RIB-svartid | 3–5 virkedager | 3–10 virkedager | Kristian F2 merknad 1 |
| F5 graving manuell | 2–3 pers × 5–7 dager | 2–3 pers × 5–14 dager | Realistisk med stans og minigraver-usikkerhet |
| F8 forskaling | 5 dager × 2 teknikere | 7–8 dager × 2 teknikere | Søbstad — ensidig mot ujamn mur |
| F10 syrevasking | 3–4 dager | 5–8 dager | Kristian F10 merknad 2 |
| Pre-F6 | — | 6–10 uker | Ny fase |
| F7.0 katodisk | — | 4–8 uker parallelt | Flyttet fra F11 |

### B.5 Modellvalg per fase (ny låsing i v02)

| Fase | v01 | v02 |
|---|---|---|
| F0–F5 | A/B/C fritt | B (med A/C-krav for F5C undervann) |
| F6–F9 | A/B/C fritt | **A eller C — IKKE ren B** |
| F10 | A/B/C fritt | B med spesialleverandør syrevasking |
| F11 | Alltid spesialleverandør | Alltid spesialleverandør, med F7.0 prosjekteringsstart |
| F12 | A/B/C fritt | B |

### B.6 Nye gates i v02

- **UG-1 til UG-6 (utførelses-gater):** SB-tilstedeværelse-gate for kritiske operasjoner.
- **MG-4a, MG-4b, MG-4c:** Splittet IG-gate i tre uavhengige løp.
- **Pre-F6-forutsetning (geotekniker + RIB-tegning) for F6, F7, F8:** Egen underfase.

### B.7 Hva v02 fortsatt mangler (åpne poster for v03)

Når byggherre har besluttet modellvalg, SB-arrangement og formelle bestillinger er inne, skal v03 oppdateres med:

- Konkrete SB-navn og -nummer.
- Mottatte RIB-produksjonstegninger — mengder bekreftet.
- Katodisk F7.0-prosjekteringsrapport.
- Innsamlede priser fra 2–3 betongleverandører + Søbstad Modell C-tilbud.
- Geotekniker-bekreftelse φ, γ.
- Dispensasjonsvedtak § 8 (hvis innvilget).
- Oppdatert Gantt med reelle datoer.
- Arch-A til Arch-G som faktiske figurer, ikke placeholder.
- BYA-versjon ferdig (parallelt dokument).
- Konkret sjekkliste KMF og Enova sluttdokumentasjon (K44 lukket).
- Lovdata-verbatim § 8-tekst (`[TBD]` i v02 lukket).

---

*Dokument slutt — kjellerplan v02, 21.10.2026. Dette er konsolidert revisjon etter seks rolle-reviews av v01. Endringer i dispensasjonsvilkår, RIB-tegninger, arkeologiske funn, forsikringsvilkår eller utførelsesmodell kan medføre vesentlige revisjoner. Dokumentet erstatter ikke prosjekteringsgrunnlag fra RIB eller godkjent tegningssett. Byggherre skal beslutte modellvalg og lukke P1-saker fra seksjon 15.1 før v03 kan utarbeides.*

