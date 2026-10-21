---
dokumenttype: prosjektert kjellerplan (operativ arbeidsbeskrivelse + tilbudsunderlag)
versjon: v01 — førsteutkast for intern gjennomgang
dato: 2026-10-21
byggherre: KodeWorks Eiendom AS (org.nr. 920 478 506)
prosjektleder antikvarisk (PGL): Ole Morten Lagmannssveen, HRP AS
koordinator utførelse: Kristian Brandsegg, KMTE
RIB: Ole Stenmo, Sivilingeniørene Harboe og Leganger AS
status: førsteutkast — ikke sendt til RIB, entreprenør eller myndigheter
---

# Prosjektert kjellerplan — Fjordgata 30 Minilager

**Versjon v01 — til intern gjennomgang hos byggherre**\
Dato: 21.10.2026

---

## Innhold

1. [Forord og lesemåte](#1-forord-og-lesemåte)
2. [Prosjektrammer](#2-prosjektrammer)
3. [To utførelsesmodeller — side om side](#3-to-utførelsesmodeller--side-om-side)
4. [Faser i rekkefølge — bakeoppskrift-formatet](#4-faser-i-rekkefølge--bakeoppskrift-formatet)
5. [Risikoregister](#5-risikoregister)
6. [Materialflyt og logistikk](#6-materialflyt-og-logistikk)
7. [Rekkefølgediagram og grov Gantt](#7-rekkefølgediagram-og-grov-gantt)
8. [Grensesnitt mot anbudsgrunnlag](#8-grensesnitt-mot-anbudsgrunnlag)
9. [Figur-sammenstilling](#9-figur-sammenstilling)
10. [Åpne spørsmål og neste skritt](#10-åpne-spørsmål-og-neste-skritt)
11. [Appendiks — syntese-notat](#11-appendiks--syntese-notat)

---

## 1. Forord og lesemåte

### 1.1 Hvem er planen for?

Dette dokumentet er en kombinert **arbeidsplan** og **tilbudsunderlag** for kjelleren i Fjordgata 30. Det er skrevet slik at det kan brukes av tre mottakergrupper samtidig:

- **Byggherres egne folk** (koordinator Kristian Brandsegg, Ain Hansumae, eventuelle studenter) som skal utføre eller koordinere arbeid i kjelleren.
- **Betongentreprenør** som skal prise og signere som ansvarlig utførende på kritiske operasjoner (bunnplate, vanntette vegger, fundamenter under vann).
- **RIB, PGL, Byantikvar, Riksantikvar og tilskuddsgivere** (KMF, Enova) som gjennomgår og godkjenner at prinsippene, rekkefølgen og dokumentasjonen holder mål.

Oppskriften er bevisst skrevet i bakeoppskrift-formatet med små, nummererte steg. Ambisjonen er at en voksen person uten betongutdanning skal kunne lese planen og forstå rekkefølgen, forutsetningene og hva som skal skje i hvert enkelt steg. Spesialistoperasjoner er merket med `[KREVER PROFF]` og foreslått timesleie-sum.

### 1.2 Hvordan planen brukes

**Lineært.** Fasene (F0–F11) utføres i rekkefølge. Noen aktiviteter innen samme fase går parallelt, og noen myndighetsavklaringer (dispensasjonssøknad etter kulturminneloven § 8, § 10, RIB-tegninger) kan prosjekteres parallelt med fysisk arbeid lenger ned i rekkefølgen. Det er markert eksplisitt.

**Gates.** Mellom faser og innenfor en fase finnes **gates** — punkter der arbeidet ikke kan fortsette uten en bestemt skriftlig godkjenning. Vi har tre typer:

- **RIB-gate (RG-x):** Ole Stenmo (Harboe og Leganger AS) godkjenner skriftlig før kutting, armering eller støping starter.
- **Arkeolog-gate (AG-x):** Riksantikvaren eller Trøndelag fylkeskommune (NIKU-tilrådning) må gi dispensasjon etter kulturminneloven § 8 før graving i uomrørte masser.
- **Myndighets-gate (MG-x):** Byantikvar, Statsforvalter (NVE for arbeid mot elv), Trondheim kommune byggesak (igangsettingstillatelse IG) må være varslet/innhentet.

### 1.3 Hard-coded vs. soft

**Hard-coded — tallfestede krav som ikke kan endres uten ny RIB-vurdering:**

| Parameter | Verdi | Kilde |
|---|---|---|
| Dimensjonerende vannstand | kote +3,20 | RIB-notat 10.02.2026 |
| Nyttelast plan –1 og 1 | 7,5 kN/m² | RIB-notat 10.02.2026 |
| Brannkrav bæring | R60 | RIB-notat 10.02.2026 |
| Bunnplate tykkelse | 450 mm | ISY-beskrivelse post 05.14 |
| Yttervegger tykkelse (tosidig del) | 250 mm | ISY-beskrivelse post 05.3 |
| Yttervegger snittykkelse (ensidig mot naturstein) | ca. 300 mm (varierer) | ISY-beskrivelse post 05.2 |
| Betongklasse bunnplate og yttervegger | B45, MF40, Cl 0,10, utførelsesklasse 2 | ISY-beskrivelse 05.14/05.16 |
| Betongklasse fundamenter i vann | AUV-betong B45, MF40, Cl 0,10, utførelsesklasse 3 | ISY-beskrivelse 05.15/05.18 |
| Armering | B500NC | ISY-beskrivelse |
| Eksponeringsklasse ytterkonstruksjoner | XS3 (saltvann, tidevann, stormflo) | ISY-beskrivelse 05.11 |
| Overdekning armering | iht. XS3 (min. 50 mm, bekreftes av RIB) | NS-EN 1992 / ISY 05.11 |
| XPS kantisolasjon mot natursteinsmur | 50 mm | ISY-beskrivelse 05.27/05.28 |
| Separasjonssjikt mellom betong og naturstein | plast/tett duk — betong skal **ikke** støpes fast til murverk | ISY-beskrivelse 05.2 |
| Svelleprofil i støpeskjøter dekke/vegg | SikaSwell® P Type H eller tilsvarende | ISY-beskrivelse 05.6 |
| Beskyttelse svelleprofil mot utvasking | Master VB2 160 eller tilsvarende | ISY-beskrivelse 05.7 |
| Tetting rundt søylegjennomføring | SikaSwell® P Ring 24 NO eller tilsvarende | ISY-beskrivelse 05.8 |
| Prosjekteringsgrunnlag vanntetting | Byggforsk 520.055; NS-EN 1992/1997/13670; NS-EN 206 | ISY-beskrivelse 05.14 |

**Soft — kan tilpasses situasjonen uten ny RIB-vurdering:**

- Rekkefølgen innenfor én fase (f.eks. hvilken yttervegg som støpes først, hvilken halvdel av platen armeres først)
- Valg av forskalingsleverandør og forskalingstype (systemforskaling vs. tradisjonell), så lenge NS-EN 13670 toleransekrav holdes
- Valg av betongleverandør (så lenge resept bekreftes mot ISY-krav)
- Containertype og -antall på gateplan, så lenge kommunens vilkår holdes
- Arbeidsgangen rundt tidevannsstøp (eksakt tidspunkt per dag) — styres av tidevannstabell
- Logistikk-koordinering mellom betongpumping, armeringssjekk og RIB-signering (det kritiske er at rekkefølgen holdes, ikke dag-til-dag kalender)

### 1.4 Dette er v01

Dokumentet er førsteutkast for intern gjennomgang. Følgende skritt gjenstår før v02 kan sendes ut:

- Søyleposisjoner innerst mot Fjordgata (målinger 21.10.2026) må inkorporeres
- Fundamentdimensjonsmotsetningen (200×200 cm vs. 3000×3000 mm) må avklares med HRP
- RIB-armeringstegninger og endelig produksjonsunderlag må mottas fra Ole Stenmo
- Kvalitetssikringsfunnene (12 QA-punkter) må returneres til HRP for rettelser i ISY-beskrivelsen
- Betongleverandør må prekvalifiseres og tilbudsresept bekreftes

Alle `[TBD: ...]`-markeringer i dette dokumentet markerer slike punkter som skal lukkes i v02.

### 1.5 Språk, tone og hvordan planen er bygget opp

Planen er på norsk bokmål. Teknisk-formelt språk er brukt der det må være verifiserbart (betongklasser, posthenvisninger). Operativt språk er brukt der bakeoppskrift-formatet krever det (steg-for-steg, kvalitetssjekker, typiske feil).

Når planen er detaljert nok vil den brukes slik:

1. Byggherre godkjenner v02 sammen med RIB og PGL.
2. Byggherre sender ut tilbudsforespørsel til minst 3 betongentreprenører med denne planen som sentralt underlag.
3. Hvis en entreprenør vinner konkurransen og tar helentreprise: planen fungerer som kvalitetssikringsramme for hans arbeid.
4. Hvis byggherre selv utfører med punktvis innleid betongekspertise (Modell B, pkt. 3): planen fungerer som daglig arbeidsplan.
5. Når arbeidet er fullført fungerer planen med vedlagte dagsrapporter, foto og RIB-signeringer som sluttdokumentasjon til kommunens byggesak og tilskuddsgivere.

---

## 2. Prosjektrammer

### 2.1 Partsoversikt

| Rolle | Person / selskap | Kontakt |
|---|---|---|
| Byggherre | KodeWorks Eiendom AS, org.nr. 920 478 506 | — |
| Daglig leder / kontaktperson byggherre | Eirik Larsen | eirik.larsen@kodeworks.no, +47 416 70 269 |
| Prosjektleder antikvarisk istandsetting (PGL) | Ole Morten Lagmannssveen, HRP AS | ola@hrpas.no, +47 990 94 851 |
| Koordinator utførelse | Kristian Brandsegg, KMTE | — |
| RIB (konstruksjon) | Ole Stenmo, Sivilingeniørene Harboe og Leganger AS | firmapost@h-l.no, +47 73 99 28 30 |
| Daglig utførelse | Ain Hansumae, Marco | — |
| Prosjektadresse | Fjordgata 30, 7010 Trondheim | — |
| Gnr/Bnr | `[TBD: verifiseres mot matrikkelen]` | — |

### 2.2 Dimensjonerende forutsetninger

Alle verdier er hentet fra RIB-notat 10.02.2026 (Harboe og Leganger AS) og ISY-beskrivelse 19.10.2026 (HRP AS). RIB-notatet av 10.02.2026 overstyrer RIB-notatet av 13.06.2025 for alle lastforhold — det eldre notatet forutsatte kontor (3,0 kN/m²); minilager gir ca. 50 % mer last.

| Parameter | Verdi | Kilde |
|---|---|---|
| Dimensjonerende vannstand (grunnlag for vanntett konstruksjon) | kote +3,20 | RIB 10.02.2026 |
| Nyttelast kjeller og plan 1 (lager) | 7,5 kN/m² | RIB 10.02.2026 |
| Nyttelast plan 2–5 (boder) | 5,0 kN/m² | RIB 10.02.2026 |
| Nyttelast plan 2–5 (adkomst) | 3,0 kN/m² | RIB 10.02.2026 |
| Snølast tak | 2,8 kN/m² | RIB 10.02.2026 |
| Egenvekt etasjeskillere | 1,5 kN/m² | RIB 10.02.2026 |
| Egenvekt tak | 0,8 kN/m² | RIB 10.02.2026 |
| Brannkrav hoved- og sekundærbæring | R60 (HRP brannkonsept) | RIB 10.02.2026 |
| Materiale stål | S355 | RIB 10.02.2026 |
| Materiale tre | Heltre C18, limtre GL30c | RIB 10.02.2026 |
| Jordparametre | sand, friksjonsvinkel 33°, egenvekt 17 kN/m³ | RIB 13.06.2025 — må verifiseres av geotekniker |

### 2.3 Hovedkonstruksjonsprinsipp

Prinsippet er en **ny vanntett betongkjeller inne i eksisterende natursteinsmur**. Elementene er:

- **Ny bunnplate i vanntett betong (B45 MF40 Cl 0,10)**, 450 mm tykkelse, støypes som helhetlig plate uten glidebolter (beslutning 22.10.2026 — Ole Morten + RIB).
- **Nye yttervegger** i to seksjoner:
  - Nedre del: ensidig forskaling mot eksisterende natursteinsmur, snittykkelse ca. 300 mm, høyde ca. 1,7 m. Plast/tett duk + XPS 50 mm mot natursteinsmur som separasjonssjikt og glidesjikt — betong skal ikke støpes fast til murverk.
  - Øvre del: tosidig forskaling fra topp natursteinsmur og opp til bjelkelag mot 1. etg. Tykkelse 250 mm.
- **Nye punktfundamenter under søndre del** (25 stk). Minimumsmål ifølge ISY post 05.1: **200 × 200 × 40 cm**. ISY post 05.29 (isolering under samme fundamenter) sier **3000 × 3000 mm**. Dette er en motsetning innenfor samme beskrivelse som må avklares med HRP (åpent spørsmål #1).
- **Reparasjon/supplering av eksisterende fundamenter mot Nidelven** med AUV-betong B45 MF40 Cl 0,10, tilpasset tidevannsrytme.
- **Katodisk korrosjonsbeskyttelse** (offeranodeanlegg) i gulv og vegger — marint miljø.
- **Delevegger i lengderetning**, 250 mm, i C25/30 (XC1) eller B45 M40 Cl 1,0 — kvalitet- og mengdeuklarhet skal avklares (QA-funn 7, 8).
- **Radonsperre** (plastbasert, bruksgruppe A2, kombinert radon- og fuktsperre) som tegnet fallback — søkes dispensasjon fra kravet (beslutning 22.10.2026) med henvisning til grunnforhold (elvegrus, ikke radon-utsatt fjell).

### 2.4 Historisk kontekst — hva vi fant i kjelleren

Da gulvbord ble demontert i sommer/høst 2026 viste det seg at den opprinnelige bolverk/kavlegulv-konstruksjonen fortsatt lå under gulvbordene (notat 15.08.2026, Ole Morten). De tverrgående rundtømrene er i stor grad borte eller alvorlig råte-/brannskadd. De langsgående stokkene (cc 1–1,5 m) har varierende tilstand. Jordmassene bak natursteinsmuren er omrørt flere ganger med rester fra 1800-tallet og framover (blikkbokser, stål- og plastrør, søppel).

**Praktisk konsekvens** (bekreftet statusmøte 22.10.2026, Post 01.02): Bygget bæres i dag av det nye rammeverket i 1. og 2. etasje. Kavlegulvet/bolverket har ikke lenger bærende funksjon. Dette gir handlingsrom til å fjerne gjenværende trevirke etter RIB-signert sikringsplan.

**Beslutning 25.10.2026** (statusmøte 25.10, Post 02): Tjukke tverrgående tømmerstokker bevares (mulig forskningsprosjekt), alt annet trevirke fjernes. Formell avsjekk mot RIB kreves før kjellerarbeid utenfor «grønt-sone» starter.

### 2.5 Arkeologi og vernestatus

Fjordgata 30 er innenfor NB!-området i Trondheim og underlagt kulturminneloven. Byantikvaren og Riksantikvaren er inne i saken. Status pr. 21.10.2026:

- **Byantikvaren:** Alt trevirke frem til tørrmuren kan fjernes (statusmøte 22.10, Post 04.01).
- **Riksantikvaren:** Kommer på befaring. Betingelse: ikke grav i uomrørte masser — kun i allerede omrørte (statusmøte 22.10, Post 04.02).
- **Dispensasjon etter kulturminneloven § 8** er ikke innsendt. Må lukkes før graving i faste masser kan starte. `[TBD: last ned verbatim § 8-tekst fra Lovdata før søknad formuleres]`
- **§ 10-granskingsrisiko:** Hvis omfanget blir større enn dispensasjon dekker, kan Riksantikvaren utløse arkeologisk gransking etter § 10. Tiltakshaver (byggherre) dekker kostnaden.

**Praktisk konsekvens:** Fjerning av gammelt råttent trevirke regnes som vedlikehold og krever ikke særskilt tillatelse. Å støpe nytt betonggulv krever igangsettingstillatelse (IG) — egen sak hos kommunens byggesaksavdeling (statusmøte 22.10, Post 04.03).

### 2.6 Grensesnitt mot resten av prosjektet

Kjellerarbeidet henger sammen med:

- **Rammesøknad levert 12.05.2026**, status avventes. Oppdatering fra endret konseptvalg (kjellertrapp med natursteinsmur som bevart element — statusmøte 20.10 Post 02) er oversendt Byggesak til Byantikvaren.
- **Vinterklargjøring** (toalett + minikjøkken til 1. etg, ny kjellernedgang, frostfri vann) må være på plass før kjellerarbeid intensiveres — se Fase 0.
- **BYA-versjon** (lettvekts) av denne planen skal utarbeides før neste BYA-befaring (statusmøte 20.10, Post 03).
- **KMF-tilskudd:** Framdriftsrapport med utbetalingsanmodning har frist 31.12.2026. Dispensasjonsprosessen (§ 8) må være igangsatt og dokumentert innen fristen for at kjellertiltaket skal kunne være med i rapporteringen.
- **Enova (yrkesbygg + varmesentraler):** Separat søknadsløp, men energitiltak i kjeller (isolasjon, klimaskille) må være konsistente med Enova-grunnlaget.

---

## 3. To utførelsesmodeller — side om side

Byggherre vurderer to utførelsesmodeller. Planen i del 4 er skrevet slik at den **fungerer for begge**. Dette avsnittet beskriver hvordan.

### 3.1 Modell A — Hel entreprise

Betongentreprenør (Søbstad, Veidekke eller tilsvarende) tar helentreprise på alle betong- og grunnarbeider i kjeller etter NS 8405. Byggherre leverer prosjektert og RIB-godkjent produksjonsunderlag, samt myndighetsgodkjenninger og dispensasjoner. Entreprenøren bærer utførelsesrisikoen.

**Hva byggherre leverer:**

- RIB-godkjente produksjonstegninger (armerings- og forskalingstegninger) fra Ole Stenmo, signert
- Oppdatert søyleplan med oppmålte koordinater (etter oppmåling 21.10.2026)
- Rammetillatelse (status avventes) og alle dispensasjoner (arkeolog, Byantikvar, Statsforvalter for arbeider mot elv)
- Container, strøm (32A/230V), vann på plassen
- Koordinasjon med andre fagentreprenører (el, VVS)

**Hva entreprenør leverer:**

- All forskaling, armering, betong, svellebånd/fugeblikk, radonsperre, XPS
- Alt arbeidsfaglig personell (betongbas, forskalingstekniker, pumpebiloperatør, kalibrator for katodisk anlegg)
- Rigg, drift, mobilisering, demobilisering
- Dokumentasjon (testing, prøver, sluttdokumentasjon)
- Fagsignatur som ansvarlig utførende (SB)

**Risikoprofil:**

| Risiko | Bærer |
|---|---|
| Ukjente kulturlag, arkeologifunn | Byggherre (regulerbare mengder i NS 3420) |
| Ukjent grunnforhold under bunnivå | Byggherre (regulerbare mengder) |
| Variasjon mot natursteinsmur | Byggherre (regulerbare mengder) |
| Tidevann, kortvarig oversvømmelse | Entreprenør (innkalkulert i enhetspriser) |
| Langsiktig setning / lekkasje | Entreprenør (garantitid 5 år etter NS 8405) |
| Forsinkelse pga. manglende tillatelser | Byggherre |

**Kostnadsprofil:** Fastpris + regulerbare mengder for kap. 03. Prisestimat fra Riis Eiendom AS (15.01.2024) satte rehabilitering av fundamenter til 2,2 MNOK ekskl. mva — det er et minimum siden scope nå er betydelig større.

**Hvordan planen i del 4 brukes:** Som kontraktens tekniske vedlegg sammen med ISY-beskrivelsen. Entreprenøren jobber etter egen detaljplan, men holdes til hard-coded verdier i pkt. 1.3 og til gates/rekkefølge i del 4.

### 3.2 Modell B — Egne folk + punktvis innleid betongekspertise

Byggherres egne folk (Kristian Brandsegg som koordinator, Ain Hansumae som dagsutfører, eventuelt studenter/russ) utfører mesteparten av arbeidet. Betongentreprenøren bidrar med:

- Utleie av spesifiserte fagfolk per time ved kritiske arbeidsoperasjoner (bunnplate-støp, veggstøp, forskaling-oppsett, armeringskontroll)
- Levering av betong, armering, forskaling via rammeavtaler
- Fagsignatur som ansvarlig utførende på hvert kritisk utførelsestrinn

**Hva byggherre leverer:**

- Alt som i Modell A, pluss daglig arbeidsutførelse (grunnarbeid, demontering, enklere betongarbeid under tilsyn)
- SHA-ansvar på plassen (byggherres koordinator)
- Materiallogistikk, containerhandtering

**Hva entreprenør leverer:**

- Betongbas / forskalingstekniker / pumpebiloperatør på timesbasis
- Betong, armering, forskaling som bestilt
- Fagsignatur begrenset til operasjoner der entreprenørens fagperson er fysisk til stede

**Risikoprofil:**

| Risiko | Bærer |
|---|---|
| Utførelsesfeil begått uten entreprenørens tilstedeværelse | Byggherre |
| Utførelsesfeil begått under entreprenørens tilsyn | Entreprenør (begrenset til nettopp det tilsynet) |
| Forsikringshull — egne folk uten fagbrev gjør betongarbeid | **Åpent spørsmål — se pkt. 10** |
| Byggherre-ansvar for SHA | Byggherre fullt ut |

**Kostnadsprofil:** Fakturering per time + materialleveranse til rammeavtalepris. Potensielt vesentlig lavere totalkostnad enn Modell A, men krever at byggherre har kapasitet og at ansvarsforholdene er klarlagt (SB-godkjenning, forsikring, KMF-krav om fagutførelse).

**Hvordan planen i del 4 brukes:** Som daglig arbeidsplan. Hvert `[KREVER PROFF]`-steg utløser bestilling av innleid fagperson. Byggherre må estimere total mengde proff-timer før kontrakt inngås.

### 3.3 Blandet modell (bro mellom A og B)

I praksis forventes en blandet modell: helentreprise på bunnplate og vanntette yttervegger (den mest teknisk krevende delen), timesleie / egne folk på forberedende arbeider (demontering, graving, rydding, deleveggsforskaling). Grensen settes ved **vanntetthet** og **under vann-arbeid** — der kreves fagsignatur på ansvarlig utførende for betongarbeider utførelsesklasse 2/3.

---

## 4. Faser i rekkefølge — bakeoppskrift-formatet

Dette er planens kjerne. 12 faser, nummerert F0–F11. Hver fase beskrives med samme oppsett:

- Mål med fasen
- Forutsetninger
- Gates (RIB-, arkeolog-, myndighets-)
- Materialer (med mengde eller `[TBD]`)
- Steg for steg
- Tidsestimat
- Kvalitetssjekk
- Typiske feil
- `[KREVER PROFF]`-flagging
- Figur-placeholders (presise beskrivelser — ikke tegninger i selve planen)

---

### Fase 0 — Vinterklargjøring og tilrettelegging

**Mål med fasen:** Kjelleren er trygg å arbeide i gjennom vinteren. Vann er frostsikret. En midlertidig varm sone (toalett + minikjøkken) finnes i 1. etg. Det finnes to kjellernedganger slik at det er to rømningsveier og effektiv materialflyt.

**Forutsetninger:** Kristian er tilbake fra reise for koordinering. Beslutning fra Eirik om flytting av toalett + minikjøkken til 1. etg (statusmøte 25.10, Post 05 — forslag ikke besluttet enda).

**Gates:**

- RIB-gate: Nei (ingen bærende konstruksjoner berøres)
- Arkeolog-gate: Nei (ingen graving under gulv)
- Myndighets-gate: Container-plassering på Fjordgata krever tillatelse fra Trondheim kommune (midlertidig bruk av fortau) — ikke blokkerende, bestill 1 uke i forveien

**Materialer:**

- OSB-plater, stendere, 2 panelovner (gjenbruk fra 2. etg)
- Isolasjon (**gjenbrukes** fra 2. etg — kast ikke; statusmøte 20.10 Post 09)
- Varmekabler til eksponerte vannrør
- Rørleggerrekvisita (samle- og frostsikring)
- Lensepumpe (min. 500 l/min kapasitet)
- Container 10 m³ × 2 (på Fjordgata)
- Materiale til ny kjellernedgang: trapp/stige, hull i etasjeskillet

**Steg for steg:**

- [ ] F0.1 — Beslutt endelig posisjon for ny toalett/varmesone i 1. etg (der gammelt kjøkken sto). Marker gulvet med spraymaling. Koordiner med Kristian og Ole Morten.
- [ ] F0.2 — Avtal rørlegger: samle vann til ny varmesone, varmekabler på eksponerte strekk, demontering av eksisterende rør i 2. etg.
- [ ] F0.3 — Bygg lettvegger rundt varmesonen (stendere + OSB + gjenbrukt isolasjon). Monter 2 panelovner. Test: rommet holder ≥ +5 °C under kaldvær.
- [ ] F0.4 — Demonter eksisterende toalett + minikjøkken i 2. etg. Sorter materialer: gjenbruk, isolasjon til nedforing, resten til container.
- [ ] F0.5 — Fjern eksisterende lysarmaturer i 2. etg og flytt brannslanger (jf. statusmøte 20.10 Post 12). Rørlegger utfører etter instruks.
- [ ] F0.6 — Ta hull i etasjeskillet 1. etg → kjeller på avtalt posisjon. Monter trapp/stige som tåler minst 150 kg levende last. Dette gir rømningsvei nr. 2 og materialvei.
- [ ] F0.7 — Flytt eksisterende kjellertrapp (ved sikringsskap) til ny posisjon om nødvendig for arbeidsflate.
- [ ] F0.8 — Bestill container(e), minst 1 uke i forveien. Koordiner med kommunen for midlertidig fortaustillatelse. Mål plassen slik at pumpebil/kranbil fortsatt kommer til.
- [ ] F0.9 — Installer lensepumpe i laveste punkt i kjeller. Test at pumpen starter og tømmer vann innen 30 minutter. Lagre reservepumpe på plassen.
- [ ] F0.10 — Skriv kort vannsikringsnotat (frostbeskyttelse av vannledninger). Lagres i prosjektmappe. Forsikringsdokumentasjon (statusmøte 20.10, Post 08).
- [ ] F0.11 — Permanent lysopplegg nede i kjeller: 360° dekning for kommende arbeid. Delvis utført (statusmøte 20.10).

**Tidsestimat:** 2 personer × 3–4 arbeidsdager + rørlegger ca. ½ dag. Containerleveranse: separat bestilling.

**Kvalitetssjekk før Fase 1 starter:**

- Varmesonen i 1. etg fungerer og holder minimum +5 °C
- Begge kjellernedgangene er trygge (gelender, godt lys, nødutgang-skilt om nødvendig)
- Lensepumpen virker, med reservepumpe tilgjengelig
- Containere på plass og kommunens tillatelse foreligger
- Vannsikringsnotat er skrevet og arkivert

**Typiske feil og avbøtende tiltak:**

- Glemme å bestille container på fortau 1 uke i forveien → forsinket arbeidsstart. Avbøtende: bestill i uken før F0.1 starter.
- Kaste isolasjonen fra 2. etg → nedforingen må kjøpes ny. Avbøtende: statusmøte 20.10 Post 09 slår fast at isolasjon gjenbrukes. Instruér Ain skriftlig.
- Plassere kjellernedgang slik at den blokkerer senere massetransport → omgjøring senere er dyrt. Avbøtende: tenk gjennom F3/F5-logistikk før F0.6 utføres.

**`[KREVER PROFF]`:**

- Rørlegger (F0.2): autorisert for vannleggeng — bestill ½ dag, ca. kr `[TBD: timesleie rørlegger]`
- Elektriker (F0.11): hvis nytt lysopplegg kobles til sikringsskap — ca. 1 time autorisert elektriker

**Figur-placeholder F0-A:** Plantegning 1. etg (ovenfra, 1:50). Viser: posisjon for ny toalett/varmesone (skravert), eksisterende kjellertrapp (blå pil), ny kjellernedgang (rød pil), container-plassering på Fjordgata (grå boks). Mål: avstand mellom kjellernedganger, romdimensjoner for varmesone, bredde adkomst til brannslanger. **Produseres av:** Ole Morten eller Ain som håndskisse ut fra Adnans trapperom-tegning.

---

### Fase 1 — Oppmåling, registrering og foto-dokumentasjon

**Mål med fasen:** Alle søyler, langsgående tømmerstokker, løse stein, intakte gulvpartier og fundament-rester er registrert med posisjon, materiale, dimensjon og tilstand. Dokumentasjonen er grunnlag for RIB-signering (Fase 2), arkeolog-dispensasjon (Fase 4) og entreprenør-tilbud. Alt tap av informasjon ved senere fjerning er forebygget.

**Forutsetninger:** Fase 0 fullført. Permanent lysopplegg nede.

**Gates:**

- RIB-gate: Nei (kun observasjon)
- Arkeolog-gate: Nei (ingen inngrep)
- Myndighets-gate: Nei

**Materialer:**

- Lasermåler (Leica DISTO eller tilsvarende)
- Målebånd 5 m og 30 m
- Spraymaling: rød, gul, blå, grønn (merking)
- Nummerede hengelapper (vektbestandig)
- Utskrift plantegning kjeller (A3/A2)
- Kamera (telefon med godt lavlys-oppsett + eventuell blitz)
- Pren (prøvestikk for treverkskvalitet) og hammer
- Notatbok, blyant, blokk til feltskisser

**Steg for steg:**

**Steg 1A — Søyleoppmåling (Ole Morten, 21.10.2026)**

- [ ] F1.1 — Mål opp alle søyler i kjelleren med lasermåler fra ett fast referansepunkt (NØ-hjørne av natursteinsmur anbefalt). Noter avstand nord-sør og øst-vest per søyle. Toleranse ±10 cm akseptabelt (statusmøte 20.10 Post 04).
- [ ] F1.2 — Nummerér hver søyle fortløpende: S01, S02, …. Spraymal nummeret på søylen (gul).
- [ ] F1.3 — Noter per søyle: materiale (stål / betong / rundtømmer), diameter eller tverrsnitt, synlig skade. Fotografer hver søyle med nummerlapp.
- [ ] F1.4 — Innerst mot Fjordgata: særlig oppmerksomhet. Stålsøyler (HUP 150×150×5 iht. RIB-notat 10.02.2026). Noter materiale, type og dimensjon per søyle.
- [ ] F1.5 — Overfør målinger til plan-tegning (A3). Send til RIB (Ole Stenmo) og lagres i prosjektmappe.

**Steg 1B — Tømmerstokk-kartlegging**

- [ ] F1.6 — Gå systematisk gjennom hver langsgående tømmerstokk som er igjen. Nummerér: L01, L02, … (spraymaling grønn på stokk).
- [ ] F1.7 — Per stokk: mål lengde (eller lengde av det som gjenstår), tverrsnitt (diameter for rundtømmer), posisjon (akse). Noter om stokken ser ut til å bære noe (ligger den mellom to søyler? hviler det noe synlig på den?).
- [ ] F1.8 — Stikk pren inn i stokken i min. 3 punkter per stokk — vurder råte-dybde. Noter skadegrad: 0 = full ved, 1 = overflate-råte, 2 = dyp råte, 3 = gjennomgående/brannskadd.
- [ ] F1.9 — For tjukke tverrgående stokker (statusmøte 25.10 Post 02 — bevares): merk BEV (grønn spray) og tegn inn på plan.
- [ ] F1.10 — Fotografer hver stokk med nummerlapp og målestav.

**Steg 1C — Løse stein og natursteinsmur**

- [ ] F1.11 — Merk alle løse steiner langs veggene (særlig mot kanalsiden) med blå spray. Nummerér X.1, X.2, … Fotografer med målestav.
- [ ] F1.12 — Vurder natursteinsmur-tilstand: sprekker, utbuling, løse partier. Marker sprekker med rød spray.
- [ ] F1.13 — Fotografer natursteinsmur systematisk — én runde med overlappende bilder på hver vegg.

**Steg 1D — Gulvplanker, kavlegulv og fundament-rester**

- [ ] F1.14 — Marker intakte gulvplanker med gul spray («Y01, Y02, …»). Noter om noen er festet til bærende konstruksjon.
- [ ] F1.15 — Fotografer kavlegulv systematisk ovenfra (rutenett 2 × 2 m). Lys nede.
- [ ] F1.16 — Fotografer fundament-rester fra 1983-ombyggingen med målestav. Noter plassering og tilstand (sprekker, mangler forskaling, osv.).

**Steg 1E — Masseregistrering**

- [ ] F1.17 — Noter tykkelse og karakter på gjenværende løsmasse (jord, grus, blandet) under gulv-nivå. Dette er ikke prøvegraving — kun visuell / overfladisk vurdering.
- [ ] F1.18 — Noter observasjoner av gjenstander: blikkbokser, rør, keramikk, bein, trevirke. Hver uvanlig observasjon fotograferes før den berøres (kan være kulturlag-indikator).

**Steg 1F — Sammenstilling**

- [ ] F1.19 — Overfør alt til to tegninger:
  - **Tegning 1 (plan):** søyler, stokker (med retning), stein, gulvplanker, fundamenter, mellomlager-posisjoner.
  - **Tegning 2 (langsnitt):** stokker-høyde, murhøyde, antatt kote under gulv.
- [ ] F1.20 — Lag et foto-register (regneark): foto-ID, hva som vises, dato, fotograf. Alle foto arkiveres med dato-prefix i prosjektmappe.
- [ ] F1.21 — Send begge tegninger + foto-register til Ole Morten og Ole Stenmo (RIB).

**Tidsestimat:** Ole Morten + 1 person × 1 dag (oppmåling søyler, pågår 21.10). Deretter 2 personer × 2 dager (tømmer, stein, gulvplanker, foto). Sammenstilling 2–3 timer.

**Kvalitetssjekk før Fase 2 starter:**

- Alle søyler nummerert, materialklassifisert og posisjonert på tegning
- Alle gjenværende langsgående stokker nummerert, dimensjonsmessig og tilstandsmessig registrert
- Foto-dokumentasjon av natursteinsmur, kavlegulv, fundament-rester er komplett
- Tegning 1 og 2 er sendt til RIB

**Typiske feil og avbøtende tiltak:**

- Måle fra forskjellige referansepunkter → avvik mellom målinger. Avbøtende: ett fast punkt (NØ-hjørne), noter det på tegningen.
- Glemme søyler innerst mot Fjordgata → senere RIB-vurdering mangler data. Avbøtende: egne steg 1A for innerste rad.
- Hoppe over foto før berøring → ikke mulig å dokumentere opprinnelig tilstand om noe går galt. Avbøtende: regel «foto før spray-merking».
- Pren-test uten metodikk → inkonsistente tilstandsvurderinger. Avbøtende: skalaen 0–3 og 3 punkter per stokk.

**`[KREVER PROFF]`:** Ingen. Dette er dokumentasjonsarbeid som utføres av egne folk.

**Figur-placeholder F1-A (Plantegning kjeller, nåværende tilstand):** Vertikalt perspektiv ovenfra, nord opp, 1:50 på A3. Viser: alle søyler (S01–Sxx) fargekodet etter materiale (stål = blå, betong = grå, tre = brun), alle langsgående stokker (L01–Lxx med pil i stokke-retning og tilstandskode 0–3 ved pilhodet), alle løse stein (X.1–X.N med blå prikk), gjenværende gulvplanker (gul skravur), eksisterende fundamenter fra 1983 (stiplet grå). Referansepunkt (NØ-hjørne) markert med rødt kryss. Akselinjer og nord-pil. **Produseres av:** Ole Morten på utskrift fra RIB/arkitekt, deretter håndtegnet og foto-tatt eller renskrevet digitalt.

**Figur-placeholder F1-B (Langsnitt kjeller, nåværende tilstand):** Vertikalt snitt i byggets lengderetning, 1:50. Viser: eksisterende natursteinsmur begge sider (høyde-kote), eksisterende bjelkelag mot 1. etg., alle gjenværende tømmerstokker med posisjon og tilstandskode, kavlegulv i søndre del (hvor det er intakt), antatt gulv-kote, antatt grunn-kote (hvis synlig fra prøvehull). Grafisk målestokk. **Produseres av:** Ole Morten.

---

### Fase 2 — RIB-gating for kutting av bærende elementer

**Mål med fasen:** Ole Stenmo (RIB, Harboe og Leganger AS) har skriftlig bekreftet, per enkelt-element (stokk, bjelke, tørrmur-parti), hvilke som kan kuttes/fjernes, hvilke som krever midlertidig støtte før kutting, og hvilke som skal stå urørt. Dette er den første virkelige gaten og den som utløser kuttearbeid.

**Forutsetninger:** Fase 1 fullført. Tegning 1 og 2 er levert RIB. Ole Mortens sikringsplan (del av kjellernotatet, ferdig 25.–26.10.2026 iht. statusmøte 22.10) ligger ved.

**Gates:**

- **RIB-gate RG-1 (bindende for Fase 3):** Skriftlig signering per element: KUT / BEV / STØTTE+KUT. Hvis STØTTE+KUT: type støtte, plassering, varighet spesifiseres.
- **Myndighets-gate:** Nei (dette er intern konstruksjonssak)
- **Arkeolog-gate:** Nei

**Materialer:** Ingen fysiske materialer før gating er klarert. Etter gating: materialer til midlertidige støtter (trebukker, stag, kiler).

**Steg for steg:**

- [ ] F2.1 — Ole Morten presenterer kjellerplan (Tegning 1 + 2 + sikringsplan) for RIB (Ole Stenmo). E-post eller fysisk befaring.
- [ ] F2.2 — RIB leverer skriftlig svar: liste over elementer med status KUT, STØTTE+KUT eller BEV. For STØTTE+KUT: spesifikasjon av støtte (type bukk/stag, plassering, antall).
- [ ] F2.3 — Prosjektleder arkiverer RIB-bekreftelsen i prosjektmappe med dato-prefix.
- [ ] F2.4 — Prosjektleder laminerer en A4-versjon av RIB-godkjenningen og henger den opp i kjelleren ved kjellernedgang. Alle som jobber i kjelleren skal se den.
- [ ] F2.5 — For elementer merket STØTTE+KUT: Kristian/Ain skaffer/lager støtten iht. RIB-spesifikasjon. Monter støtte. Fotografer og send til RIB.
- [ ] F2.6 — RIB bekrefter skriftlig at midlertidige støtter er korrekt montert.
- [ ] F2.7 — Oppdater sikringsplan med RIB-signerte endringer. Lagre endelig versjon i prosjektmappe.

**Tidsestimat:** RIB-svartid 3–5 virkedager. Montering av midlertidige støtter: 1 person × ½ dag per støtte (anslag).

**Kvalitetssjekk før Fase 3 starter:**

- Skriftlig RIB-bekreftelse per element foreligger
- Alle krevde midlertidige støtter er montert og godkjent av RIB
- Laminert A4 henger synlig i kjelleren
- Sikringsplan versjon 2 er arkivert

**Typiske feil og avbøtende tiltak:**

- Starte kutting basert på muntlig OK → RIB-ansvar glipper, sprekker/havari-risiko. Avbøtende: krav om skriftlig bekreftelse (e-post med «OK» mottatt godkjennes som bevisdokumentasjon).
- Sette opp bukk på feil sted → støtte-funksjon tapes. Avbøtende: følg RIBs skisse eksakt, foto før kutting.
- Glemme BEV-elementene (tjukke tverrgående stokker, statusmøte 25.10 Post 02) → ødelegges ved et uhell. Avbøtende: sprøytemal grønn BEV-merking tydelig, sperrebånd rundt BEV-stokker.

**`[KREVER PROFF]`:** Ingen i selve F2 (RIB-signering er faglig arbeid utført av Harboe og Leganger som del av engasjementet).

**Figur-placeholder F2-A (Snitt gjennom kjeller med sikringsplan):** Langsnitt eller tverrsnitt 1:20, viser: en representativ langsgående tømmerstokk (L-ID), eksisterende etasjeskille over, midlertidig støtte (bukk/stag) under stokken med spesifikasjon, avstand til neste støttepunkt. Annotert med RIB-signeringsdato og -navn. **Produseres av:** Ole Stenmo (RIB) som del av sikringsplanen.

---

### Fase 3 — Rydding og demontering (over gulvnivå)

**Mål med fasen:** Alt løst materiale over gulvnivå er fjernet: gulvplanker, kavlegulvbord, godkjente trestokker (etter RIB-signering). Natursteinsmuren står stabilt med alle BEV-elementer intakte. Kjelleren er klar til arkeologisk befaring (G1 i avhengighetskartet) og dispensasjonssøknad.

**Forutsetninger:** Fase 2 fullført. RIB-bekreftelse per element foreligger. Lensepumpe i drift. Kjellernedgang og containere operativt.

**Gates:**

- **RIB-gate (RG-1):** Allerede klarert i Fase 2.
- **Arkeolog-gate:** **Nei** for arbeid *over* opprinnelig gulvnivå (fjerning av råttent/brannskadd trevirke regnes som vedlikehold, statusmøte 22.10 Post 04.03). **Ja (AG-1)** for arbeid som berører løsmasser *under* opprinnelig gulvnivå — det tilhører Fase 4.
- **Myndighets-gate:** Byantikvar har gitt grønt lys for trevirke frem til tørrmur (statusmøte 22.10 Post 04.01).

**Materialer:**

- Fein-sag (oscillerende) og kjedesag for stokker
- Elektrisk motorsag (anskaffet, statusmøte 25.10 Post 03 — kun én person på plassen bruker den av gangen)
- Slegge, brekkstang, trillebår, kornett
- Vinsjekurv (ca. 500 kg kapasitet) eller rampe med vogn
- Container(e) på Fjordgata
- Personlig verneutstyr: hjelm, vernesko, hørselsvern, kjedesaghansker, FFP3-støvmaske, visir

**Steg for steg:**

**Steg 3A — Lavrisk-arbeid (kan starte 26.10.2026 iht. statusmøte 22.10 Post 05)**

- [ ] F3.1 — Fjern alt råttent og brannskadd trevirke over tørrmurens overkant. Dette regnes som vedlikehold og krever ingen gates.
- [ ] F3.2 — Sorter materialer: gjenbruksbrukbart tre (bra stand) stables ryddig innenfor arbeidssone (langs Fjordgata-innervegg); råteskadd/brannskadd tre direkte til container.
- [ ] F3.3 — Daglig oppsummering i dagsrapportskjema (se vedlegg): dato, person, hva som er fjernet, foto av dagens arbeid.

**Steg 3B — Gulvplanker og kavlegulvbord**

- [ ] F3.4 — Fjern alle intakte gulvplanker merket Y01, Y02, … (jf. Fase 1). Start fra midten, arbeid mot veggene.
- [ ] F3.5 — Sorter planker: gjenbruksbrukbart stables; råteskadd til container.
- [ ] F3.6 — Fjern gjenværende kavlegulvbord. Hvis en bord sitter fast i en BEV- eller UKL-stokk — stopp, kontakt Ole Morten.

**Steg 3C — Langsgående tømmerstokker (etter RIB-signering per stokk)**

- [ ] F3.7 — Kontroller at midlertidige støtter (fra Fase 2) er på plass og stabile. Juster om nødvendig.
- [ ] F3.8 — Start med den stokken RIB har klarert som enklest (lavest risiko). Kutt med kjedesag/elektrisk motorsag i prefabrikkerte lengder 2,0–2,5 m (statusmøte 20.10 Post 05 — tilpasset remontasje mot kanalen).
- [ ] F3.9 — Mal kotereferanse (dvs. originalt plassering, nedre endes høyde) og L-ID med spraymaling på hver kuttet stokk. Dette er nødvendig for eventuell remontasje.
- [ ] F3.10 — Transport av kuttede stokker (200–300 kg per stokk): bruk vinsjekurv eller to-manns-løft med talje. **Aldri manuelt løft over 50 kg uten mekanisk hjelp.** Dropp gjennom gulvåpning mot kanalsiden til springflo, eller heis opp til gateplan via vinsjekurv.
- [ ] F3.11 — Mellomlagring: enten mot kanalvegg utenfor (mellomlager C — floa/lekter) frem til remontasje, eller på gateplan Fjordgata (mellomlager A) om remontasjen er senere.
- [ ] F3.12 — Etter hvert kutt: sjekk at midlertidige støtter fremdeles sitter stabilt. Fotografer og send til RIB med jevne mellomrom.

**Steg 3D — BEV-stokker (bevares)**

- [ ] F3.13 — Tjukke tverrgående stokker: dekk til med presenning eller tape for å beskytte mot støv og vann under videre arbeid. Ikke flytt dem.
- [ ] F3.14 — Fotografer BEV-stokker etter at omgivende arbeid er ferdig — dokumenter at de står intakte.

**Steg 3E — Løse stein mot kanalsiden (over gulvnivå)**

- [ ] F3.15 — Stein merket X.1, X.2, … som ligger synlig over gulvnivå og ikke er en del av bærende tørrmur: flytt til mellomlager B (innvendig, langs sørmur) for sortering senere.
- [ ] F3.16 — Hvis en stein ser ut til å være en del av tørrmurens funksjonelle fot: STOPP og kontakt Ole Morten. Dette aktiverer tørrmur-stabiliseringsvurdering (R04 i risikoregisteret).

**Tidsestimat:** 2 personer × 3–5 arbeidsdager. Avhenger av tilstand og antall stokker.

**Kvalitetssjekk før Fase 4 starter:**

- Alt råttent/brannskadd trevirke over tørrmur-nivå er fjernet
- Alle KUT-stokker er kappet, dokumentert og mellomlagret
- BEV-stokker er merket, dekket og intakt
- Midlertidige støtter er inspisert og OK
- Kjelleren er visuelt klar for arkeologisk befaring
- Dagsrapporter og foto arkiveres daglig

**Typiske feil og avbøtende tiltak:**

- Starte graving mellom løsmasser *under* gulvnivå i løpet av Fase 3 → bryter arkeolog-gate (AG-1). Avbøtende: eksplisitt grense «ikke under opprinnelig gulvnivå i Fase 3».
- Kaste gjenbruksplanker/-stokker → tap av verdifullt materiale (BYA forventer gjenbruk mot kanalen). Avbøtende: nøyere sortering, egen stabel for gjenbruk.
- Løfte stokker manuelt → ryggskade, krise på plassen. Avbøtende: strikt 50-kg-grense manuelt, over det → vinsjekurv.
- Ødelegge BEV-stokker ved uhell → forskningsprosjekt-mulighet tapt. Avbøtende: sperrebånd + grønn BEV-merking.
- Kjedesag-skade på person → alvorlig HMS. Avbøtende: FFP3-maske, kjedesaghansker, aldri alene (statusmøte 25.10 Post 03 — kun én motorsag-bruker av gangen).

**`[KREVER PROFF]`:**

- Ingen i selve F3. Dette er riving og demontering som egne folk utfører. Men: hvis omfanget av riving kommer nær bærende struktur (BEV-grensen) uten at RIB har signert — stopp og kall inn RIB som befaring, ca. kr `[TBD: RIB-timesleie, antagelig kr 1500–2200/t]`.

**Figur-placeholder F3-A (Arbeidsflyt-plan Fase 3):** Plantegning kjeller 1:50 ovenfra. Viser: arbeidsflyt-piler fra arbeidssone til vinsjekurv til container, plassering mellomlager A (Fjordgata) og B (innvendig sørvegg), plassering mellomlager C (floa, kanalside), gulvåpning for stokk-dropp, soner som skal fjernes i Fase 3 (grønn skravur = lavrisk, blå = etter RIB-signering), BEV-elementer (rød sirkel = ikke rør), lensepumpe-plassering. **Produseres av:** Ole Morten eller Ain.

---

### Fase 4 — Prøvegraving, arkeolog-befaring og dispensasjonssøknad

**Mål med fasen:** Riksantikvaren har gjennomført befaring, mottatt målsatt søknad etter kulturminneloven § 8 og innvilget dispensasjon for omfanget av graving som trengs for å oppnå 3 m takhøyde. Prøvegraving er dokumentert.

**Forutsetninger:** Fase 3 fullført (ryddig kjeller for befaring). Målsatte tegninger av graveomfang er klare (plan + snitt). Søyleoppmålinger inkorporert. RIB-signert graveplan foreligger.

**Gates:**

- **Myndighets-gate MG-1 (Byantikvar):** Grønt lys for riving av trevirke frem til tørrmur foreligger (statusmøte 22.10 Post 04). BYA skal også orienteres om graveomfanget — lettvekts BYA-versjon av denne planen leveres før neste BYA-befaring.
- **Myndighets-gate MG-2 (Riksantikvar/fylkeskommune):** Dispensasjon etter kulturminneloven § 8. `[TBD: last ned verbatim § 8-tekst fra Lovdata før søknadsformulering].` Saksbehandlingstid: minimum 4 uker etter fullstendig søknad, realistisk 8–12 uker inkl. NIKU-tilrådning.
- **Myndighets-gate MG-3 (Statsforvalter / NVE / Trondheim kommune for arbeider mot elv):** Tillatelse for graving under vann på utside natursteinsmur, 10 m³ (ISY post 03.3). Omsøkes separat før Fase 5C starter.

**Materialer:**

- Spade, krafse, pensel for arkeologisk prøvegraving
- Fotostav, målestav, GPS/laser for koordinatfesting av funn
- Prøvetakingsposer (merket per lag)

**Steg for steg:**

**Steg 4A — Forberedelse til RA-befaring**

- [ ] F4.1 — Bekreft med Riksantikvaren (Sissel Ramstad Skoglund) at kjelleren er klar for befaring. Foreslå dato uke 44–45 (slutten av oktober, begynnelsen av november).
- [ ] F4.2 — Lag en infopakke til befaringen: Tegning 1 og 2 fra Fase 1, foto-sammenstilling av gjenværende tilstand, kort beskrivelse av tiltaket, foreløpig graveomfang (anslag).
- [ ] F4.3 — Gjennomfør befaring. Noter RAs merknader. Avtal eventuell prøvegraving (sted, dato, hvem er til stede).

**Steg 4B — Prøvegraving**

- [ ] F4.4 — Avklar med RA eller NIKU om prøvegraving skal utføres av arkeolog eller av byggherre under tilsyn. Dette styrer kostnad vesentlig.
- [ ] F4.5 — Grav i 1–2 avtalte punkter til ca. 50 cm dybde. Dokumenter stratigrafi fortløpende (foto, feltskisse). Noter om massene er omrørte (statusmøte 22.10 Post 04.02: ja i de fleste områdene) eller uomrørte.
- [ ] F4.6 — Prøver samles i poser med lag-ID. Oversendes NIKU for sålding/vurdering hvis arkeolog har bedt om det.
- [ ] F4.7 — Rapport skrives: prøvegraveresultat, konklusjon om massekarakter per sone.

**Steg 4C — Dispensasjonssøknad etter § 8**

- [ ] F4.8 — Utarbeide målsatte tegninger av graveomfang (plan + snitt). Krav fra Riksantikvaren per 24.09.2026 (nevnt i utkast C). RIB og PGL bidrar.
- [ ] F4.9 — Formuler søknad: formål, omfang, metodikk, avbøtende tiltak, kompetanse (hvem utfører). Bruk § 8 verbatim-tekst. `[TBD: § 8 lastes ned fra Lovdata.no og inkluderes som vedlegg]`
- [ ] F4.10 — Send søknad til Riksantikvaren med kopi til Trøndelag fylkeskommune. Bekreft mottak.
- [ ] F4.11 — Følg aktivt opp etter uke 4. Hvis NIKU-tilrådning eller § 14-vurdering er involvert, forventet totaltid 8–12 uker.

**Steg 4D — Søknad for arbeid mot elv (parallelt)**

- [ ] F4.12 — Avklar om arbeidet mot kanalen (10 m³ graving under vann, forsterkning av fundamenter mot Nidelva) krever tillatelse fra Statsforvalter, NVE, Trondheim havn, eller andre. ISY post 03.3 slår fast: «må omsøkes i flere instanser».
- [ ] F4.13 — Formuler søknad(er). Trolig: Trondheim kommune (vannforurensing), Statsforvalter (naturmangfold om relevant), NVE (sikkerhet mot flom og vassdragsinngrep).
- [ ] F4.14 — Send søknader parallelt med § 8-søknaden. Følg opp.

**Steg 4E — Igangsettingstillatelse (IG) for betongarbeid**

- [ ] F4.15 — Fjerning av gammelt trevirke krever ikke IG (statusmøte 22.10 Post 04.03). Men å støpe nytt betonggulv krever IG — søk hos Trondheim kommune byggesak.
- [ ] F4.16 — IG kan søkes tidlig, parallelt med § 8-prosessen, så den er klar når graving er fullført.

**Tidsestimat:** Befaring 1 dag. Prøvegraving 1–2 dager. Søknadsutforming 1 uke. Saksbehandling 4–12 uker (kritisk sti — kan ikke komprimeres).

**Kvalitetssjekk før Fase 5 starter:**

- Skriftlig dispensasjon etter § 8 foreligger med klare vilkår
- Tillatelse(r) for arbeid mot elv foreligger
- IG-søknad er levert
- Prøvegraverapport dokumentert
- Avbøtende tiltak (f.eks. arkeolog til stede under graving) er avtalt skriftlig

**Typiske feil og avbøtende tiltak:**

- Søke dispensasjon uten målsatte tegninger → avvisning, forsinkelse. Avbøtende: lag tegningene først, før søknad.
- Starte graving i påvente av svar → lovbrudd (kulturminneloven § 8). Avbøtende: hard stopp, laminert instruks i kjelleren.
- Glemme IG-søknad → betongarbeid må stoppes når det er klar for støping. Avbøtende: søk IG parallelt med § 8.
- Ikke avklare om arkeolog må være til stede under graving → dyrt å løse i siste øyeblikk. Avbøtende: eksplisitt punkt i søknadsformulering.

**`[KREVER PROFF]`:**

- Arkeolog (fra NIKU eller frittstående) for prøvegraving og eventuell tilstedeværelse under hoved-graving, ca. kr `[TBD: anslag kr 1200–1800/t pluss reise]`
- RIB (Ole Stenmo) for graveplan-signering, inkludert i engasjement

**Figur-placeholder F4-A (Målsatt graveomfang-tegning):** Plan 1:50 og snitt 1:50 på A3. Plan: område som skal graves (rød skravur), område som ikke berøres (uskravert), prøvegravepunkter (rødt kryss med ID). Snitt: dagens kote, prosjektert kote etter graving, graveskråning (iht. ISY 03.1: «rett ned i samme nivå som innvendig veggliv på eksisterende natursteinsmur»), fundament-nivå for eksisterende søyler, dim. vannstand kote +3,20. **Produseres av:** Ole Stenmo (RIB) + Ole Morten (PGL) som vedlegg til dispensasjonssøknaden.

**Figur-placeholder F4-B (Snitt arbeid mot elv):** Tverrsnitt 1:50 av byggets nordre fasade mot Nidelven. Viser: eksisterende natursteinsmur, eksisterende fundament under natursteinsmur, graveprofil (1:3 skråning iht. ISY 03.3) 10 m³, forsterkning av fundament med AUV-betong, tidevannsnivåer (høy flo, dim. vannstand +3,20, lav fjære). **Produseres av:** Ole Stenmo (RIB).

---

### Fase 5 — Graving og masseflytting

**Mål med fasen:** Gulvnivået i kjelleren er senket til prosjektert grunnkote slik at takhøyde blir minst 3 m. Totalt ca. 130 m³ fast volum er fjernet og transportert til deponi (200 tonn). Grunnforholdene er dokumentert og godkjent av RIB som underlag for Fase 6/7.

**Forutsetninger:** Fase 4 fullført — dispensasjon etter § 8 og tillatelse for arbeid mot elv foreligger. RIB-godkjent graveplan foreligger. Lensepumpe operativ. Containere på plass.

**Gates:**

- **Arkeolog-gate AG-1:** Oppfylt via dispensasjon fra Fase 4.
- **Overvåkningskrav:** Arkeolog kan være til stede under graving (avklart i Fase 4). Stansplikt ved funn (§ 8 andre ledd).
- **Myndighets-gate MG-3:** Tillatelse for arbeid mot elv — gjelder for Steg 5C.
- **RIB-gate RG-2 (etter graving):** RIB inspiserer grunnforhold og bekrefter at underlag er egnet for bunnplate.

**Materialer:**

- Trillebår, kornett, spann
- Vinsjekurv (ca. 500 kg) eller alternativ heis-løsning
- `[TBD: vurder minigraver — avhenger av om åpning i etasjeskillet tillater det. Minigraver kan trolig gjøre jobben 5× raskere, men krever gjennomtenkt tilkomst]`
- Lensepumpe + reservepumpe
- Containere (bytteordning)
- Måleutstyr for kote (lasermåler eller optisk nivell)

**Steg for steg:**

**Steg 5A — Oppstart**

- [ ] F5.1 — Verifiser skriftlig at dispensasjon § 8 og øvrige tillatelser er arkivert. Laminert A4 i kjelleren.
- [ ] F5.2 — Mål nåværende grunnkote fra kjent referansepunkt. Noter.
- [ ] F5.3 — Avtal med arkeolog om prosedyre: tilstedeværelse, varslingsrutiner ved funn, foto-dokumentasjon.
- [ ] F5.4 — Start lensepumpe. Noter kapasitet og vanninntregning per time — grunnvann vil trenge inn med dim. vannstand kote +3,20.

**Steg 5B — Graving innvendig (130 m³ fast volum)**

- [ ] F5.5 — Grav i etapper fra midten av kjelleren og mot veggene. Hold min. 50 cm avstand til eksisterende fundamenter uten RIB-signert graveplan for det området.
- [ ] F5.6 — Graveskråning: rett ned i samme nivå som innvendig veggliv på natursteinsmur (ISY post 03.1).
- [ ] F5.7 — Flytt masser trinnvis: fra graveflate til mellomlager B (innvendig sørvegg) eller direkte til vinsjekurv → container på Fjordgata.
- [ ] F5.8 — Dokumenter: dagsrapport med volum (anslag per dag), funn, foto.
- [ ] F5.9 — Ved funn (keramikk, bein, metall, trestruktur ut over 1800-tallet-rester): STOPP, kontakt arkeolog, dokumenter in situ før berøring.
- [ ] F5.10 — Container byttes ved behov (ikke på søndager — avtales med leverandør). Transport 6–9 km (ISY post 03.5).
- [ ] F5.11 — Når prosjektert grunnkote er nådd: kontrollér med lasermåler at hele arealet (ca. 90 m² gulv) ligger på rett nivå.

**Steg 5C — Graving under vann mot kanalen (10 m³)**

- [ ] F5.12 — Avtal med fagarbeider / dykker eller erfaren grunnarbeider for arbeid delvis under vann (ISY post 03.3). Dette er ikke egne folks arbeid.
- [ ] F5.13 — Koordiner med tidevannstabell for Trondheim. Arbeid planlegges i lavvannsvinduer.
- [ ] F5.14 — Grav 10 m³ på utside av natursteinsmur mot kanalen, 0–1 m vanndybde, graveskråning 1:3.
- [ ] F5.15 — Dokumenter tilstand av eksisterende fundamenter mot elv — foto med målestav.
- [ ] F5.16 — Opplasting og transport (anbrakt volum, ISY post 03.4).

**Steg 5D — Avslutning av fase**

- [ ] F5.17 — Rydde arbeidsflaten, pumpe tørr.
- [ ] F5.18 — Kall inn RIB (Ole Stenmo) til befaring. RIB bekrefter skriftlig at grunnen er tilfredsstillende som underlag for bunnplate (RG-2).
- [ ] F5.19 — Hvis grunnen ikke er tilfredsstillende (f.eks. bløt sone, uventet dyp løsmasse): avtal med RIB om tiltak (dyp-graving til bæredyktig lag, utskiftning, geotekstil).

**Tidsestimat:** 2–3 personer × 5–7 arbeidsdager for 130 m³ innvendig. Steg 5C: 2 fagarbeidere × 2–3 dager (tidevann-styrt). Total vareighet avhenger av om det brukes minigraver eller manuell drift.

**Kvalitetssjekk før Fase 6 starter:**

- Prosjektert grunnkote nådd over hele arealet (toleranse ±50 mm)
- Ingen uventede konstruksjoner eller funn uten arkeolog til stede
- Lensepumpe i stabil drift, grunnvannsnivå under kontroll
- Masser fjernet og transportert — anslag 200 tonn (ISY post 03.6)
- Fundamenter mot elv er fri-gravd og dokumentert
- RIB har bekreftet skriftlig at grunnforholdene er OK (RG-2)

**Typiske feil og avbøtende tiltak:**

- Grave nærmere eksisterende fundament enn 50 cm uten RIB-signering → setningsrisiko (R01). Avbøtende: fast grense, laminert instruks.
- Underdimensjonert lensepumpe → vanninntregning stopper arbeidet. Avbøtende: dimensjonér for dim. vannstand kote +3,20, ha reservepumpe på plassen.
- Fortsette etter funn uten arkeolog-kontakt → lovbrudd og mediarisk. Avbøtende: hard stopp-regel, kontaktliste laminert.
- Minigraver skader natursteinsmur → irreversibel skade på verneverdig element. Avbøtende: graving nær mur alltid manuell, min. 50 cm sone.
- Containerbytte faller på søndag → masser hoper opp. Avbøtende: planlegg gravedag-slutt til fredag.

**`[KREVER PROFF]`:**

- Fagarbeider / dykker for arbeid under vann (Steg 5C), ca. kr `[TBD: anslag kr 1200–1800/t]`
- RIB-befaring (RG-2), inkludert i engasjement
- Arkeolog til stede under graving (hvis avtalt), ca. kr `[TBD: 10–40 timer avhengig av omfang]`

**Figur-placeholder F5-A (Graveprofil og kote-angivelse):** Tverrsnitt 1:20. Viser: eksisterende grunnkote (stiplet), prosjektert grunnkote (heltrukket), dim. vannstand kote +3,20 (rød stiplet), fundamentdybder for eksisterende søyler, graveskråning i etapper (piler viser graveretning), vanntilsig-piler. Mål: gravedybde per sone, koteangivelse, min. avstand til fundament. **Produseres av:** Ole Stenmo (RIB).

**Figur-placeholder F5-B (Logistikkplan — materialflyt under graving):** Plan 1:50. Viser: fra-graveflate-piler, mellomlager B innvendig, vinsjekurv-posisjon, åpning i etasjeskillet, container på Fjordgata, lensepumpe-plassering, slangetrasé. **Produseres av:** Kristian/Ole Morten.

---

### Fase 6 — Søylefundamenter

**Mål med fasen:** 25 nye søylefundamenter er støpt, herdet og dokumentert. Fundamentene står på samme sted som dagens søyler, men dypere i grunnen (iht. ISY post 05.1 omfangsbeskrivelse). Alle fundamenter er klare som understøtt for de 25 stålsøylegjennomføringene i bunnplate (Fase 7) og de etterfølgende søylene.

**Forutsetninger:** Fase 5 fullført — graving godkjent av RIB. Betongleverandør kontrahert. Armering levert og dokumentert. **ÅPENT:** Fundamentdimensjon-motsetningen (post 05.1: 200×200×40 cm vs. post 05.29: 3000×3000 mm) må være avklart med HRP før F6.4. Dette er en vesentlig forskjell: 4 m² grunnflate vs. 9 m² grunnflate per fundament.

**Gates:**

- **RIB-gate RG-3 (armering):** RIB inspiserer og signerer armering før betong bestilles.
- **Myndighets-gate:** IG må være innhentet (jf. F4.15).

**Materialer:**

- Drenslag 16/32: anslag ca. 6 m³ (bruk «under fundament» hvis ISY-mengden 30 m²/200 mm fordeles mellom bunnplate og fundamenter — avklar)
- XPS 50 mm under punktfundamenter: 25 stk, dim. 3000×3000 mm iht. ISY 05.29 (`[TBD: motsetning med 05.1 — avklar]`), gir ca. 225 m² hvis 3×3-dimensjon stemmer
- Forskalingsplater for 25 fundamenter
- Armeringsstål B500NC — `[TBD: fra RIB-produksjonstegning, utførelsesklasse 3, overdekning iht. XS3]`
- AUV-betong B45 MF40 Cl 0,10, utførelsesklasse 3: 40 m³ (ISY post 05.15)
- Avstandsholdere for armering

**Steg for steg:**

**Steg 6A — Forberedelse**

- [ ] F6.1 — Mål opp posisjon for hvert fundament fra kjent referanse (NØ-hjørnet). Søylene skal stå på samme sted som dagens søyler, men dypere.
- [ ] F6.2 — Grav ned for hvert fundament til prosjektert nivå. `[KREVER PROFF: enten minigraver-operatør eller forskalingstekniker som vet hvor eksisterende søyler står]`
- [ ] F6.3 — Legg ut XPS 50 mm per fundament iht. post 05.29.

**Steg 6B — Forskaling** `[KREVER PROFF: forskalingstekniker eller betongbas]`

- [ ] F6.4 — Monter forskalingsramme per fundament. Dim. iht. endelig avklaring (`[TBD: 200×200 eller 300×300 cm]`), tykkelse 40 cm, overflate glatt.
- [ ] F6.5 — Juster lodd og nivå.

**Steg 6C — Armering**

- [ ] F6.6 — Legg armering iht. RIB-produksjonstegning. Overdekning iht. XS3 (min. 50 mm bekreftes).
- [ ] F6.7 — Bruk avstandsholdere slik at armering ikke berører forskaling.
- [ ] F6.8 — Fotografer ferdig armering per fundament.

**Steg 6D — RIB-gate RG-3**

- [ ] F6.9 — Send foto av ferdig armering til RIB (Ole Stenmo). RIB signerer skriftlig per fundament eller per batch. **Ikke bestill betong før RG-3 er klarert.**

**Steg 6E — Støping (etappevis, tilpasset tidevann for AUV-arbeid i vann)**

- [ ] F6.10 — Bestill AUV-betong B45 MF40 Cl 0,10, utførelsesklasse 3, 24–48 timer i forveien. Bekreft konsistensklasse og alle delkrav skriftlig.
- [ ] F6.11 — Støp fundamenter batchvis. Vibrer forsiktig (AUV-betong komprimerer seg selv, men liten vibrator kan brukes der tilgang tillater).
- [ ] F6.12 — Topp-nivå tangere underkant ny bunnplate (ISY post 05.1).
- [ ] F6.13 — Ta betongprøver (sylindre) minimum 3 stk per 30 m³.
- [ ] F6.14 — Herding: AUV-betong oppnår fasthet raskt. Avform etter min. 3 dager eller iht. leverandørens herdeplan. Hold betong fuktig.
- [ ] F6.15 — Minste herdetid før belastning: 7 dager (eller lenger hvis RIB spesifiserer).

**Steg 6F — Avslutning**

- [ ] F6.16 — Måle inn topp-koter per fundament. Toleranse: iht. NS-EN 13670.
- [ ] F6.17 — Dokumenter: prøveresultater (28 dagers trykk-test), foto, mengde, batch-nummer.
- [ ] F6.18 — RIB-sluttkontroll for fasen.

**Tidsestimat:** `[KREVER PROFF]`-ressurser (forskalingstekniker + betongbas): ca. 10 arbeidsdager. Egne folk som støtte: tilsvarende. Total varighet 2–3 uker inkl. herdetid.

**Kvalitetssjekk før Fase 7 starter:**

- Alle 25 fundamenter støpt, herdet og måleinnmålt
- Topp-koter innenfor toleranse
- Betongprøver 28-dagers trykk ≥ B45-krav
- RIB-sluttkontroll OK

**Typiske feil og avbøtende tiltak:**

- Starte støp uten RG-3 → ansvarsbrudd. Avbøtende: hard regel, laminert.
- Feil fundamentdimensjon pga. uavklart motsetning (200×200 vs. 3000×3000) → kostbar omgjøring. **Avbøtende: BLOKK før F6.4, avklar skriftlig med HRP og RIB. Trolig er 200×200 korrekt (vanlig norsk fundamentdimensjon for stålsøyler), og 3000×3000 i post 05.29 er en skrivefeil.**
- Glemme avstandsholdere → overdekning blir for liten, armeringskorrosjon over tid. Avbøtende: visuell sjekk per fundament før RG-3.
- Bestille feil betongresept → leveranse må avvises på plassen. Avbøtende: skriftlig bekreftelse med alle delkrav.

**`[KREVER PROFF]`:**

- Forskalingstekniker: 10 dager, ca. kr `[TBD]`
- Betongbas: 5 dager (støpedager), ca. kr `[TBD]`
- Pumpebiloperatør (inkl. pumpe), hvis AUV-betong pumpes: ca. kr `[TBD]`
- RIB-befaring RG-3 og sluttkontroll: inkludert

**Figur-placeholder F6-A (Fundament-plan):** Plantegning 1:50. Viser: alle 25 fundamenter sentrisk under tilhørende søyler, X/Y-koordinater per fundament, aksesystem (f.eks. A1–F5), fundamentdimensjon (`[TBD]`), armering-prinsipp (nummerert kryss). **Produseres av:** Ole Stenmo (RIB).

**Figur-placeholder F6-B (Fundament snitt):** Vertikalt snitt 1:10. Viser: eksisterende grunn, XPS 50 mm under, fundament (dim. `[TBD]`, høyde 400 mm), armeringskaper (B500NC, overdekning 50+ mm), topp fundament tangere underkant plate, søylegjennomføring med svellebånd (SikaSwell® P Ring 24 NO) rundt stålrør Ø 150–200 mm. **Produseres av:** Ole Stenmo (RIB).

---

### Fase 7 — Bunnplate (vanntett betong, 450 mm, 115 m³)

**Mål med fasen:** Ny vanntett bunnplate er støpt som helhetlig plate (beslutning statusmøte 22.10 Post 02) over hele kjellerarealet (ca. 90 m² iht. ISY-mengder; sjekk mot endelig graveomfang). Platen tilfredsstiller XS3 i marint miljø, har alle svelleprofiler og fugeblikk i kant, og er dokumentert iht. Byggforsk 520.055 og NS-EN 1992/1997/13670/206.

**Forutsetninger:** Fase 6 fullført. Betongleverandør bekreftet med skriftlig resept. Armering levert og dokumentert. Lensepumpe i drift.

**Gates:**

- **RIB-gate RG-4 (armering):** RIB inspiserer og signerer armering før betong bestilles. Dette er den viktigste armeringskontrollen i prosjektet.
- **RIB-gate RG-5 (ferdig plate):** RIB inspiserer plate etter avforming.

**Materialer:**

- Drenslag 16/32: 30 m² × 200 mm = ca. 6 m³ (ISY post 03.7)
- Forsterkningslag 0/4 (sand): 15 m² × 100 mm = ca. 1,5 m³ (ISY post 03.8)
- XPS 50 mm under hele platen: ca. 350 m² (ISY post 03.10)
- XPS 50 mm kantisolasjon mot natursteinsmur: innenfor 30–110 m² iht. ISY 05.27 (`[TBD: entydig mengde — QA-funn 11]`)
- Radonsperre / fuktsperre (plastbasert, bruksgruppe A2): `[TBD: mengde — QA-funn 10]` m². Tegnes inn selv om det søkes dispensasjon (statusmøte 22.10 Post 03).
- Armering B500NC — `[TBD: fra RIB-produksjonstegning, 150 kg/m³ gir ca. 17 250 kg for 115 m³]`
- Svelleprofil SikaSwell® P Type H (eller tilsvarende): 65 m i overgang dekke/vegg (ISY 05.6)
- Fugeblikk Master VB2 160 (eller tilsvarende): 65 m (ISY 05.7)
- Svellebånd SikaSwell® P Ring 24 NO (eller tilsvarende): 25 stk for søylegjennomføringer Ø 150–200 mm (ISY 05.8)
- Vanntett betong B45 MF40 Cl 0,10, utførelsesklasse 2: 115 m³ (ISY post 05.14)
- Avstandsholdere, bindtråd, hammerstol

**Steg for steg:**

**Steg 7A — Forberedelse av undergrunnen** `[KREVER PROFF: betongbas eller forskalingstekniker som koordinator]`

- [ ] F7.1 — Legg ut drenslag 16/32, inntil 200 mm tykkelse. Komprimer normalt. Kontroller kote.
- [ ] F7.2 — Legg ut forsterkningslag 0/4 sand, inntil 100 mm. Komprimer. Kontroller kote.
- [ ] F7.3 — Monter XPS 50 mm under hele platen. Fugetett med sammenpressede skjøter.
- [ ] F7.4 — Monter XPS 50 mm kantisolasjon stående langs natursteinsmur fra grunn-nivå til prosjektert OK-dekke. Dette er glidesjikt.
- [ ] F7.5 — Legg plast/tett duk mot natursteinsmur (over XPS) der ensidig forskaling kommer. Forankre med tape eller plugger. Dette hindrer sammenstøping (ISY post 05.2).
- [ ] F7.6 — Legg ut radonsperre over hele arealet. Overlapp min. 200 mm, teip alle skjøter med systemgodkjent tape, fold opp min. 300 mm langs vegger. Fotografer før armering legges.

**Steg 7B — Svelleprofil og forberedelse av overgang til vegg**

- [ ] F7.7 — Marker på platekant hvor yttervegger kommer. Her monteres svelleprofil **før** betong støpes, slik at svellebåndet går gjennom støpeskjøten mellom plate og vegg.
- [ ] F7.8 — Montér SikaSwell® P Type H langs hele kanten (65 m anslag). Fest til armering med plastklips eller bindtråd.
- [ ] F7.9 — Montér fugeblikk Master VB2 160 over svelleprofilen etter leverandørens anvisning.

**Steg 7C — Armering** `[KREVER PROFF: Betongbas og RIB-tegning]`

- [ ] F7.10 — Legg armeringsnett iht. RIB-produksjonstegning (over- og underarmering, bøyler, forankringer rundt søyle). Mengde ca. 150 kg/m³ gir ca. 17 250 kg total (ISY 05.11 anslag).
- [ ] F7.11 — Bruk avstandsholdere slik at overdekning iht. XS3 oppnås (min. 50 mm; endelig verdi bekreftes av RIB).
- [ ] F7.12 — Kobl armering på foten av søylene til plate-armeringen iht. RIB-tegning.
- [ ] F7.13 — Montér SikaSwell® P Ring 24 NO rundt hvert av de 25 søylestålrørene som går gjennom platen.
- [ ] F7.14 — Fotografer ferdig armering systematisk — overlappende bilder for hele arealet.

**Steg 7D — RIB-gate RG-4**

- [ ] F7.15 — Send foto + skjema til RIB (Ole Stenmo). RIB bekrefter skriftlig. **Ikke bestill betong før RG-4 er klarert.**

**Steg 7E — Støping** `[KREVER PROFF: Betongbas + pumpebiloperatør]`

- [ ] F7.16 — Bestill vanntett betong B45 MF40 Cl 0,10, utførelsesklasse 2, pumpbar (konsistensklasse `[TBD: trolig S3 eller S4 for 450 mm plate]`), 115 m³ total. Bestill 24–48 timer i forveien, skriftlig med alle delkrav. Kontroller leveringsplan: ikke på mandag morgen (R07).
- [ ] F7.17 — Vinter-sjekk: hvis lufttemperatur < 5 °C, etabler frosttelt og varme eller utsett. Herdeplan må sikre at betong ikke fryser i løpet av første 7 dager (R09).
- [ ] F7.18 — Støp platen i ett kontinuerlig støp (helhetlig plate, ingen glidebolter — statusmøte 22.10 Post 02). Pumpe forventet. Vibrator for komprimering.
- [ ] F7.19 — Ta betongprøver (sylindre), minimum 3 stk per 30 m³ støp — total ca. 12 prøver for 115 m³.
- [ ] F7.20 — Stålglatt overflate etter at betong er stiv men ikke herdet (iht. ISY 05.19 andre del, LG8.5232).

**Steg 7F — Herding**

- [ ] F7.21 — Dekk med presenning eller frosttelt. Vann daglig eller bruk herdematerialer. Minimum 7 dagers våtherding.
- [ ] F7.22 — Ikke betrå platen med last de første 3 dagene. Full belastningskapasitet etter 28 dager.
- [ ] F7.23 — Overvåk tidevann og flom (R14). Hvis springflo varsles under de første 7 dagene — ha ekstra lensepumpekapasitet og tett tildekking.

**Steg 7G — RIB-gate RG-5 (ferdig plate)**

- [ ] F7.24 — Etter 7 dager: visuell inspeksjon av hele platen. Sjekk sprekker, overflatefeil, områder uten vibrasjon.
- [ ] F7.25 — Send foto + 7-dagers trykkprøveresultater til RIB. RIB-sluttkontroll og skriftlig OK (RG-5).

**Tidsestimat:** Forberedelse 2–3 dager. Armering 2–3 dager. RG-4 svartid 1–2 dager. Støp 1 dag. Herding minimum 7 dager (men F8 kan starte parallelt med fuktherding av F7). Total ca. 14 dager.

**Kvalitetssjekk før Fase 8 starter:**

- Platen er støpt helhetlig uten synlige kaldskjøter uten svellebånd
- Alle svelleprofiler i kant er intakt (synlig over støp-topp)
- Alle søylegjennomføringer har svellebånd på plass
- Betongprøver 7 dagers trykk er på sporet mot B45
- RG-5 skriftlig OK

**Typiske feil og avbøtende tiltak:**

- Kaldskjøt uten svellebånd → lekkasje. Avbøtende: aldri avslutte støp midt i plate uten planlagt skjøt + svellebånd. For 115 m³ bør hele platen gå på én dag.
- For liten overdekning → korrosjon over tid. Avbøtende: avstandsholdere, visuell sjekk før RG-4.
- Ikke ta betongprøver → ikke mulig å dokumentere i ettertid. Avbøtende: skriftlig prøveprotokoll, 3 per 30 m³.
- Støp ved < 5 °C uten frosttelt → kapillarsprekker, utett plate. Avbøtende: sjekk langtidsvarsel 48 t før, utsett eller etabler telt.
- Pumpebil kan ikke komme til → støp må avbrytes. Avbøtende: for-sjekk tilkomst og pumpe-rør-lengde (Fjordgata-adkomst er smal).

**`[KREVER PROFF]`:**

- Forskalingstekniker / betongbas: 5 dager
- Betongbas og pumpebiloperatør: 2 dager (forberedelse + støp)
- Rør/kran-hjelp: 1 dag
- RIB-befaring RG-4 og RG-5: inkludert

**Figur-placeholder F7-A (Plan bunnplate armering):** Plan 1:50. Viser: hele platekonturen, armeringsraster (over og under), forankringer rundt søyler, svelleprofil langs kant (rød linje), svellebånd rundt søyler (røde ringer), radonsperre-utbredelse (stiplet). Mål: armeringsdiameter, cc-avstand, overdekning. **Produseres av:** Ole Stenmo (RIB).

**Figur-placeholder F7-B (Snitt bunnplate og underlag — detaljert):** Vertikalt snitt 1:10 fra midten av platen til kanten mot natursteinsmur. Viser lag for lag nedenfra og opp: eksisterende masser, drenslag 16/32 (200 mm), forsterkningslag 0/4 (100 mm), XPS 50 mm, radonsperre (plastbasert), underarmering, overarmering, betong B45 450 mm, stålglattet overflate. Mot kanten: XPS kantisolasjon 50 mm vertikalt, plast/tett duk, natursteinsmur. I overgang vegg/gulv: svelleprofil og fugeblikk. **Produseres av:** Ole Stenmo (RIB).

**Figur-placeholder F7-C (Detalj — søylegjennomføring):** Snitt 1:5 rundt én søylegjennomføring. Viser: stålsøyle Ø 150–200 mm, forankring til fundament (fra Fase 6), svellebånd SikaSwell® P Ring 24 NO rundt søylerøret, plateelementer, armering tett om søylen. **Produseres av:** Ole Stenmo (RIB).

---

### Fase 8 — Yttervegger (vanntett)

**Mål med fasen:** Alle fire ytterveggene er støpt i to seksjoner:

- **Nedre del:** ensidig forskaling mot natursteinsmur, 110 m² total, snittykkelse ca. 300 mm, høyde ca. 1,7 m, vanntett betong B45 MF40 Cl 0,10 (ca. 52 m³ delvis).
- **Øvre del:** tosidig forskaling fra topp natursteinsmur og opp til bjelkelag mot 1. etg., 95 m² total, tykkelse 250 mm.

Alle støpeskjøter har svelleprofil og fugeblikk. Natursteinsmur fungerer som ensidig forskaling i nedre del, med XPS + plast/tett duk som separasjonssjikt — betong er ikke støpt fast til murverket.

**Forutsetninger:** Fase 7 fullført (bunnplate herdet minst 7 dager, RG-5 OK). Forskalingssystem bestilt. Armering levert. Natursteinsmur er rengjort og stabil.

**Gates:**

- **RIB-gate RG-6 (armering yttervegger):** RIB inspiserer og signerer før støp.

**Materialer:**

- Forskalingsplater ensidig (nedre del): ca. 110 m² (ISY 05.2)
- Forskalingsplater tosidig (øvre del): ca. 95 m² (ISY 05.3)
- Steng (tilpasningsforskaling i overgang): 65 lm (ISY 05.4)
- Plast/tett duk mot natursteinsmur: ca. 110 m²
- XPS 50 mm vertikal kantisolasjon mot natursteinsmur: `[TBD: hele veggen = ca. 180 m²; QA-funn 11]`
- Armering B500NC Ø16 mm, utførelsesklasse 3, XS3 — `[TBD: fra RIB-produksjonstegning]`
- Vanntett betong B45 MF40 Cl 0,10, utførelsesklasse 2: 52 m³ (ISY 05.16)
- Svelleprofil og fugeblikk i støpeskjøt vegg/gulv (allerede montert i Fase 7)

**Steg for steg:**

**Steg 8A — Forberedelse av natursteinsmur** `[KREVER PROFF: forskalingstekniker]`

- [ ] F8.1 — Rengjør natursteinsflaten der ny vegg kommer. Stålbørste og vann. Fjern løs mørtel og skitt — betongen må ikke blandes med løstnende partikler.
- [ ] F8.2 — Monter XPS 50 mm vertikal kantisolasjon mot muren fra bunnsåle til topp.
- [ ] F8.3 — Legg plast/tett duk (eller tilsvarende separasjonssjikt) direkte mot naturstein eller over XPS iht. detaljkrav. Fest med tape eller plugger i mørtel-fuger (ikke bor i stein).

**Steg 8B — Forskaling nedre del (ensidig)** `[KREVER PROFF: forskalingstekniker]`

- [ ] F8.4 — Montér ensidig forskaling langs alle fire yttervegger. Innvendig forskalingliv i prosjektert posisjon. Høyde ca. 1,7 m fra bunnplate til topp natursteinsmur.
- [ ] F8.5 — Montér steng (tilpasningsforskaling, 65 lm) i overgangen mellom bunn tosidig forskaling (øvre del) og topp natursteinsmur — slik at det ikke lekker betong gjennom gapet (ISY 05.4).

**Steg 8C — Forskaling øvre del (tosidig)**

- [ ] F8.6 — Montér tosidig forskalingssystem fra topp natursteinsmur og opp til bjelkelag mot 1. etg. Varierende høyde pga. nedtrappinger i etasjeskillet.
- [ ] F8.7 — Veggtykkelse 250 mm.

**Steg 8D — Armering**

- [ ] F8.8 — Legg armering iht. RIB-tegning. B500NC Ø16 mm (anslag fra ISY 05.11). Utførelsesklasse 3. Overdekning iht. XS3.
- [ ] F8.9 — Kobl armering på topp av bunnplate til vegg-armeringen iht. forankringskrav fra RIB.
- [ ] F8.10 — Fotografer ferdig armering per vegg.

**Steg 8E — RIB-gate RG-6**

- [ ] F8.11 — Send foto til RIB. RIB signerer skriftlig. **Ikke bestill betong før RG-6 er klarert.**

**Steg 8F — Støping** `[KREVER PROFF: betongbas + pumpebiloperatør]`

- [ ] F8.12 — Bestill vanntett betong B45 MF40 Cl 0,10, utførelsesklasse 2 — 52 m³ total. 24–48 t forhåndsvarsel.
- [ ] F8.13 — Støp i etapper om nødvendig. Hver etappe tilrettelegges slik at kaldskjøt kun oppstår der svelleprofil er montert.
- [ ] F8.14 — Fyll ikke mer enn 500 mm lagvis — vibrér per lag for å unngå segregering (R07).
- [ ] F8.15 — Særlig for nedre del (ensidig mot natursteinsmur): fyll fra toppen av forskalingen, la betong flyte ned mellom forskaling og separasjonssjiktet. Visuell kontroll av fylling.
- [ ] F8.16 — Ta betongprøver, 3 per 30 m³.

**Steg 8G — Herding og avforming**

- [ ] F8.17 — Herding minimum 7 dager under våte forhold. Beskytt mot frost (R09).
- [ ] F8.18 — Avform tidligst etter 3 dager (eller lenger iht. RIB).
- [ ] F8.19 — Visuell inspeksjon: ingen synlige sprekker, kaldskjøter uten svellebånd, eller segregerte områder.

**Tidsestimat:** Forskaling 5 dager × 2 forskalingsteknikere. Armering 3 dager. RG-6 1–2 dager. Støp 1–2 dager (etappevis). Herding 7 dager. Total ca. 3 uker.

**Kvalitetssjekk før Fase 9 starter:**

- Alle fire vegger støpt, herdet, visuelt uten feil
- Svelleprofiler i støpeskjøter intakt
- Vegger lodd og rett iht. NS-EN 13670 toleransekrav
- Betong er **ikke** støpt fast til natursteinsmur (sjekk ved avforming av øvre del)
- Betongprøver 7 dagers trykk på sporet

**Typiske feil og avbøtende tiltak:**

- Støpe fast natursteinsmur ved uhell → irreversibel skade, termiske spenninger. Avbøtende: XPS + plast/tett duk er hard-coded regel.
- Kaldskjøt uten svellebånd → lekkasje. Avbøtende: planlegg skjøt-plassering med svellebånd montert.
- For raskt fylling → segregering, porer, utett vegg. Avbøtende: 500 mm per lag, vibrator.
- Avforming for tidlig → sprekker. Avbøtende: minst 3 dager, lenger ved kaldt vær.

**`[KREVER PROFF]`:**

- Forskalingstekniker: 5 dager × 2 personer
- Betongbas: 2 dager (støp)
- Pumpebiloperatør: 2 dager
- RIB-befaring RG-6: inkludert

**Figur-placeholder F8-A (Snitt yttervegg — detaljert):** Vertikalt tverrsnitt 1:10. Viser lag utenfra inn (eller nedenfra og opp): natursteinsmur (eksisterende, nedre del), plast/tett duk, XPS 50 mm, betong 300 mm (ensidig del) eller 250 mm (tosidig del), innvendig forskalingliv. Svelleprofil og fugeblikk i overgang plate/vegg. «Vektergang» mellom ny betongvegg og eksisterende bryggevegg (jf. snittegning 28.08.2026). **Produseres av:** Ole Stenmo (RIB).

**Figur-placeholder F8-B (Plan vegger og forskalingsetapper):** Plan 1:50. Viser: alle fire yttervegger med innmål, posisjon «vektergang» mellom betongvegg og bryggevegg, steng-overganger (65 lm total), støpeskjøter markert med dobbelstrek, rekkefølge for forskaling/støp (etappe 1, 2, 3). **Produseres av:** Ole Stenmo (RIB) + forskalingstekniker.

**Figur-placeholder F8-C (Snitt klimaskille):** Snitt 1:10 av overgangen kjeller → 1. etg. der klimaskillet går «litt inn og ut» (jf. snittegning 28.08.2026 klimaskille-variant). Viser: topp av yttervegg, bjelkelag etasjeskille, posisjon klimaskillesjikt (dampsperre), isolasjon, lufttetthetsdetaljer. **Produseres av:** Ole Stenmo (RIB) eller HRP (klimaskille er bygningsfag).

---

### Fase 9 — Delevegger (lengderetning, nord og sør)

**Mål med fasen:** To delevegger i lengderetning (nord og sør) er støpt, 250 mm tykkelse. Delevegger skal bære laster fra plan 1 iht. RIB-tegninger.

**Forutsetninger:** Fase 8 fullført. Delevegg-posisjoner iht. RIB-tegning. Betongleverandør og materialer klarert.

**Gates:**

- **RIB-gate RG-7 (armering delevegger):** RIB signerer før støp.
- **ÅPENT (QA-funn 7, 8):** Betongklasse delevegger — ISY post 05.9 sier C25/30 XC1 (innvendig tørt miljø); ISY post 05.17 sier B45 M40 Cl 1,0 med tunge tilslag. Hvilken gjelder for de ulike deleveggene? Mengde 9 m³ vs. 20 m³ (post 05.17) — hvilken er korrekt? **Avklares med HRP før F9.1.**

**Materialer:**

- Forskalingsplater tosidig: ca. 95 m² `[TBD: QA-funn 5 om feil enhet]`
- Armering B500NC Ø16 mm, utførelsesklasse 3, XS3 (ISY 05.11 anslag)
- Betong `[TBD avklart]` — enten C25/30 XC1 eller B45 M40 Cl 1,0, 9–20 m³

**Steg for steg:**

- [ ] F9.1 — Forskaling tosidig for delevegger. 250 mm veggtykkelse. Lengderetning (nord og sør).
- [ ] F9.2 — Armering iht. RIB-tegning. XS3 overdekning hvis det er tvil om fuktforhold.
- [ ] F9.3 — RG-7: RIB signerer. **Ikke støp før RG-7.**
- [ ] F9.4 — Bestill betong iht. avklart klasse. Støp.
- [ ] F9.5 — Herding minst 7 dager.
- [ ] F9.6 — Visuell inspeksjon og dokumentasjon.

**Tidsestimat:** Forskaling 3 dager. Armering 2 dager. Støp 1 dag. Herding 7 dager. Total ca. 2 uker.

**Kvalitetssjekk:** Som Fase 8 — lodd, rett, kvalitet.

**Typiske feil:** Feil betongklasse pga. uavklart QA-funn. Avbøtende: lukkelig før F9.1.

**`[KREVER PROFF]`:** Som Fase 8 — forskalingstekniker og betongbas.

**Figur-placeholder F9-A (Plan delevegger):** 1:50. Viser nord- og sørdelevegg med lengder, høyder, forankringer til yttervegger og bunnplate. **Produseres av:** Ole Stenmo (RIB).

---

### Fase 10 — Overflatebearbeiding, syrevasking og isolasjon innvendig

**Mål med fasen:** Alle innvendige betongoverflater er bearbeidet iht. ISY: gulv stålglattet, vegger glatt flate etter forskalingsplater, syrevasket. Innvendig XPS på natursteinsmur over gulvnivå er montert.

**Forutsetninger:** Fase 9 fullført, alle betongelementer herdet i min. 28 dager.

**Gates:** Ingen harde gates, men RIB bør konsulteres hvis det oppdages overflatefeil som trenger reparasjon.

**Materialer:**

- Fortynnet syre (HCl maks 5 %) for syrevasking, 295 m² (ISY 05.26)
- Nøytraliseringsmiddel (f.eks. soda-oppløsning)
- Vernedusj / spyle-utstyr
- XPS 50 mm innvendig på natursteinsmur over gulv: ca. `[TBD: avklares med ISY 05.28 — mengde mangler, QA-funn 11]`
- Festematerialer for XPS

**Steg for steg:**

- [ ] F10.1 — Visuell inspeksjon av alle betongoverflater (vegger og gulv). Noter avvik.
- [ ] F10.2 — Mindre reparasjoner (sprekker < 0,2 mm, mindre porer): injiser med epoksy eller sement-mørtel iht. RIB-anbefaling.
- [ ] F10.3 — Syrevasking av innvendige betongvegger (295 m² iht. ISY 05.26) `[KREVER PROFF: betongfagarbeider med erfaring med syrevasking]`. Bruk HCl maks 5 %, åndedrettsvern, hansker, visir, heldress. Nøytraliser og skyll med vann etter vasking.
- [ ] F10.4 — Syrevasking av gulv på grunn (iht. ISY 05.25 anslag ca. 90 m²).
- [ ] F10.5 — Stålglatt gulvoverflate (iht. ISY 05.19 andre del) hvis dette ikke er gjort i Fase 7.
- [ ] F10.6 — Monter XPS 50 mm på innvendig side av natursteinsmur fra OK dekke til topp mur (ISY 05.28).
- [ ] F10.7 — Dokumenter med foto hele kjellerflaten.

**Tidsestimat:** 3–4 dager fagarbeider.

**Kvalitetssjekk:** Alle overflater syrevasket, nøytralisert, skyllet. XPS på plass.

**Typiske feil:** Glemme nøytralisering av syre → langvarig surhet, risiko. Avbøtende: alltid skylle med nøytraliseringsmiddel og vann etter.

**`[KREVER PROFF]`:** Betongfagarbeider for syrevasking, 3 dager, ca. kr `[TBD]`.

**Figur-placeholder F10-A:** Ingen spesifikk figur — overflatearbeid dokumenteres gjennom foto.

---

### Fase 11 — Katodisk korrosjonsbeskyttelse

**Mål med fasen:** Offeranodeanlegg for katodisk korrosjonsbeskyttelse av stål-elementer i kjeller er prosjektert, montert og idriftsatt. Vedlikeholdsplan er levert.

**Forutsetninger:** Fase 10 fullført (overflater syrevasket). Spesialleverandør kontrahert.

**Gates:**

- **RIB-gate RG-8 (overgang til neste etasje):** RIB sluttkontroll av hele kjeller inkl. katodisk anlegg.

**Materialer:**

- Offeranodesystem for marint miljø — type, antall og dim. prosjekteres av spesialist. ISY post 40.2 er RS uten mengder (QA-funn 12).
- Støttekonstruksjon for anoder
- Elektrisk kabling, overvåkningsboks

**Steg for steg:**

- [ ] F11.1 — Kontraher spesialleverandør med marin erfaring (f.eks. Corrocean, Protea, eller tilsvarende). `[KREVER PROFF: katodisk korrosjonsspesialist]`
- [ ] F11.2 — Spesialist prosjekterer anodesystem basert på eksponert stålareal (25 søyler Ø 150–200 mm, pluss armering i gulv/vegg som indirekte beskyttes). Overordnet miljø marint. Brakkvann i Nidelven — bekreft at anoder er dimensjonert for det (R16).
- [ ] F11.3 — Spesialist leverer prosjekteringsrapport med antall anoder, plassering, forventet levetid, strømnivåer, overvåkning.
- [ ] F11.4 — RIB gjennomgår rapporten og godkjenner.
- [ ] F11.5 — Spesialist monterer støttekonstruksjon, anoder, kabling.
- [ ] F11.6 — Idriftsettelse: måling av strøm, spenning, pH i anode-nærområde. Dokumentasjon.
- [ ] F11.7 — Spesialist utarbeider vedlikeholdsplan: hvor ofte skiftes anoder, hvordan overvåkes systemet.

**Tidsestimat:** Prosjektering 2–3 uker (parallelt med andre faser). Montering 2–3 dager. Idriftsettelse 1 dag.

**Kvalitetssjekk:** System i drift, dokumentasjon komplett, vedlikeholdsplan levert.

**Typiske feil:** Dimensjonering uten riktig vannkjemi-data → anoder forbrukes for raskt. Avbøtende: spesialleverandør med marin erfaring + brakkvann-datagrunnlag.

**`[KREVER PROFF]`:** Katodisk korrosjonsspesialist, hele fasen, ca. kr `[TBD: 150 000 – 400 000 totalt, basert på standard offeranodeanlegg]`.

**Figur-placeholder F11-A (Anode-plan):** Plan 1:50. Viser plassering av enkeltanoder (sirkler med ID), kabelføringer (stiplet), tilkoblingspunkt (stjerne), overvåkningsboks. **Produseres av:** Katodisk korrosjonsspesialist.

---

### Fase 12 — Sluttdokumentasjon og overgang

Dette er ikke en «fase» i teknisk forstand, men avslutning og dokumentasjonsinnsamling.

**Mål med fasen:** Komplett dokumentasjon av kjellerarbeidet er levert til byggherre, kommune (byggesak) og tilskuddsgivere. RIB-sluttattest foreligger. Arkeolog-sluttbefaring er gjennomført (hvis krevd i dispensasjonsvilkårene). Kjelleren er klar for at hovedombyggingen tar over.

**Forutsetninger:** Fase 11 fullført.

**Gates:**

- **RIB-gate RG-8:** RIB-sluttattest.
- **Arkeolog-gate AG-2:** Arkeolog-sluttbefaring hvis dispensasjon krever det.

**Steg for steg:**

- [ ] F12.1 — Visuell sluttkontroll av hele kjelleren: ingen lekkasjer, ingen sprekker, korrekt takhøyde (min. 3 m), alle anoder montert.
- [ ] F12.2 — Systematisk sluttfotografering: alle vegger, gulv, søyler.
- [ ] F12.3 — RIB-sluttbefaring og skriftlig sluttattest (RG-8).
- [ ] F12.4 — Arkeolog-sluttbefaring (hvis krevd).
- [ ] F12.5 — Samle dokumentasjon: RIB-attester (RG-1 til RG-8), betong-testresultater, arkeolog-dispensasjon og sluttrapport, katodisk korrosjon-dokumentasjon og vedlikeholdsplan, dagsrapporter, foto-register, mengde-registre.
- [ ] F12.6 — Lever komplett dokumentasjonspakke til byggherre, kommune byggesak, og tilskuddsgivere (KMF, Enova).
- [ ] F12.7 — Oppdatér TASKS.md og ARCHIVE.md i prosjektmappe.

**Tidsestimat:** 2–3 dager inkl. befaring.

---

## 5. Risikoregister

Risikoregisteret bygger på utkast C (17 risikoer) med noen tillegg og justeringer. Sannsynlighet og konsekvens er på en 1–5-skala.

| # | Beskrivelse | Sanns. | Kost | Tid | Rel.konsekvens | Avbøtende tiltak | Ansvarlig | Fase |
|---|---|---|---|---|---|---|---|---|
| R01 | Setningsskader på naboeiendom (Fjordgata 28 eller 32) under graving langs natursteinsmur | 2 | 4 | 3 | Høy — nabo kan stoppe arbeid | Prøvegraving dokumenteres; fotodokumentasjon nabokjeller før start; setningsbolter ved mur; graving i etapper med støtting | PGL | F5 |
| R02 | Grunnvann oversvømmer gravearbeid — tidevann/springflo stiger over laveste gravenivå | 4 | 3 | 4 | Lav | Dimensjonér lensepumpe for kote +3,20; AUV-betong for fundamentstøp; tidevannstabell | Utfører | F5–F7 |
| R03 | Feil med vanntett sjikt — svelleprofil/fugeblikk monteres feil, lekkasje i støpeskjøt | 3 | 5 | 5 | Middels — kostbar utbedring | Monter iht. leverandøranvisning; RIB-kontroll før hvert sjikt lukkes; aldri støpe over neste trinn uten RG-signering | RIB + utfører | F7, F8 |
| R04 | Ustabil natursteinsmur raser når støttende masser fjernes | 3 | 3 | 3 | Middels — BYA og vernestatus | Stabiliser løse stein før graving; aldri grave mot murfot uten midlertidig støtte; foto før start; graveretning fra midten utover | PGL + utfører | F5 |
| R05 | Bjelker kuttet uten RIB-signering (ved uhell eller misforståelse) | 2 | 4 | 3 | Høy — BYA/RA reaksjon, mulig havari | Laminert RG-1-oversikt i kjeller; sperrebånd rundt BEV-stokker; Kristian/Ain skriftlig instruert | Koordinator | F2, F3 |
| R06 | Arkeologisk funn under graving — menneskebein, skipsdeler, middelaldergjenstander | 3 | 3 | 5 | Høy — mange myndighetspartner, media | Dispensasjon først; beredskapsplan + kontaktliste; stans umiddelbart ved funn | PGL | F5 |
| R07 | Forsinket eller feil betongleveranse — konsistens eller resept avviker | 2 | 3 | 4 | Lav | Skriftlig bekreftelse 24–48 t i forveien med alle delkrav; kontaktperson hos leverandør; aldri bestill til mandag morgen | Utfører | F6–F9 |
| R08 | Feil armering — dimensjon, overdekning eller monteringsretning | 2 | 4 | 3 | Lav | RIB-gater (RG-3, RG-4, RG-6, RG-7) er bindende; RIB-tegning på stedet; foto-dokumentasjon før pumpebestilling | RIB + utfører | F6–F9 |
| R09 | Kald støp med sprekker — støp under 5 °C, ufullstendig herding | 3 | 4 | 3 | Lav | Støp kun ved > 5 °C eller frosttelt + varme; herdeplan med isolerende matter; min. 7 dagers herding før nedtemperering | Utfører | F6–F9 (vinter) |
| R10 | Ulykke i trange rom — lav takhøyde, dårlig ventilasjon, kjedesag-skade | 3 | 3 | 2 | Middels — HMS-tilsynsrisk | SHA-plan; FFP3-maske ved kapping; ventilasjon via to åpninger; aldri alene i kjeller; kun én motorsag-bruker | Koordinator (SHA) | F1–F11 |
| R11 | Forsikringshull — egne folk utfører betongarbeid uten fagbrev; forsikring dekker ikke | 3 | 5 | 2 | Middels — forsikringsselskap, byggesak | Ansvarlig utførende (SB) må meldes kommunen; enten innleid firma med fagbrev som SB, eller egne folk begrenses til ikke-strukturelle oppgaver | Byggherre | F6–F9 |
| R12 | Riksantikvar-saksbehandling tar mer enn 4 uker — kan bli 8–12 uker | 3 | 2 | 5 | Middels — KMF-frist 31.12.2026 under press | Start Fase 4 tidligst mulig; komplett søknad ved innsending; spor sak aktivt etter uke 4 | Byggherre + PGL | F4 |
| R13 | Tømmergjenbruk mislykkes — kuttede bjelker råteskadde innvendig | 3 | 2 | 2 | Middels — BYA forventer gjenbruk | Prøvestokk først; vurder tverrsnitt visuelt + pren; alternativt materiale (nytt rundtømmer) på plan B | PGL | F3 |
| R14 | Flom/springflo under herding — fersk betong oversvømmes | 2 | 4 | 3 | Lav | Følg tidevannstabell; ikke støp i springflo-perioder; lensepumpe + nødstopp-plan; tildekking med presenning | Utfører | F6, F7 |
| R15 | Byantikvar overraskes av faktisk inngrep — tilbaketrekning av anbefaling | 3 | 3 | 4 | Høy — BYA er del av KMF-kjeden | Lettvekts BYA-versjon av planen leveres før neste BYA-befaring; invitere BYA til befaring før og etter opprydding | Byggherre | F1 (umiddelbart) |
| R16 | Katodisk korrosjonsbeskyttelse dimensjonert feil for Nidelvens brakkvann | 2 | 3 | 2 | Lav | Spesialist med marin erfaring; dimensjonering basert på faktisk vannkjemi i Nidelva | Utfører (spesialist) | F11 |
| R17 | Mangelfull dokumentasjon av eksisterende konstruksjon — § 10-gransking kan utløses | 3 | 3 | 4 | Høy — § 10-gransking er tiltakshavers kostnad | Systematisk fotodokumentasjon og skisser av bolverk nå (før videre inngrep); supplér notat 15.08.2026 med koordinater og tegninger | PGL | F1 |
| R18 (nytt) | Fundamentdimensjon-motsetning ikke lukket før F6 starter — 200×200 vs. 3000×3000 cm | 4 | 3 | 2 | Lav | Avklares skriftlig med HRP og RIB før F6.4; dokumenter beslutning i prosjektmappe | Byggherre | F6 |
| R19 (nytt) | Betongleverandør svikter leveranse (streik, maskinhavari, feil resept) | 2 | 4 | 3 | Lav | Prekvalifisér 2–3 leverandører; hovedleverandør med rammeavtale, backup med rask tilgjengelighet; skriftlig bekreftelse 48 t før hver leveranse | Byggherre | F6–F9 |
| R20 (nytt) | Pumpebil kommer ikke frem i Fjordgata (smal gate, parkering, lastebegrensninger) | 2 | 3 | 2 | Lav | For-sjekk tilkomst (sjekk oppdatert kommunal informasjon om vektrestriksjon); varsle kommune/politi for midlertidig parkeringsforbud på støpedag; ha reserve-pumperør for lengre strekk | Byggherre | F7, F8 |
| R21 (nytt) | Konflikt mellom egne folk (Modell B) og innleid betongbas om fremgangsmåte | 3 | 2 | 2 | Middels | Skriftlig rollefordeling; betongbas har siste ord på fagoperasjoner; Kristian som konfliktløser | Byggherre | F6–F9 |
| R22 (nytt) | Enova-eller KMF-krav om fagsignatur på ikke-tilstede-dag → avvisning av tilskudd | 2 | 4 | 2 | Middels — tilskuddsrisiko | Fagsignatur per operasjon (ikke pr. dag) dokumenteres; alternativt engangsengasjér SB som dekker alle operasjoner | Byggherre | F6–F11 |
| R23 (nytt) | Tverrgående BEV-stokker ødelegges ved uhell under annet arbeid | 3 | 2 | 1 | Middels — forskningsprosjekt-mulighet tapt | Grønn BEV-merking + sperrebånd + presenning-tildekking; alle som jobber i kjelleren instrueres | Koordinator | F3–F11 |
| R24 (nytt) | Vinterforhold forsinker arbeid lenger enn planlagt — hele F6–F9 skyves til 2027 | 4 | 3 | 5 | Middels — tilskuddsfrister 2026 | Realistisk vinter-schedule med telt/varme; forberede F0–F5 ferdig i 2026 slik at F6+ kan starte så snart dispensasjon er inne; kommuniser til KMF om realistisk framdrift | Byggherre | F6–F9 |

---

## 6. Materialflyt og logistikk

### 6.1 Betong — bestilling og leveranse

**Fasthetsklasser per konstruksjonsdel:**

| Konstruksjonsdel | Klasse | Mengde | ISY-post |
|---|---|---|---|
| Fundamenter innvendig (under grunnvann) | AUV-betong B45 MF40 Cl 0,10, utførelsesklasse 3 | 40 m³ | 05.15 |
| Bunnplate (vanntett) | B45 MF40 Cl 0,10, utførelsesklasse 2, pumpbar | 115 m³ | 05.14 |
| Yttervegger (vanntett) | B45 MF40 Cl 0,10, utførelsesklasse 2, pumpbar | 52 m³ | 05.16 |
| Delevegger (innvendig, tørt eller `[TBD]`) | C25/30 XC1 eller B45 M40 Cl 1,0 — **avklares** | 9–20 m³ | 05.9 / 05.17 |
| Fundamenter mot elv (under vann) | AUV-betong B45 MF40 Cl 0,10, utførelsesklasse 3 | `[TBD: volum mangler i ISY, avklares av RIB]` | 05.18 |

**Betongleverandør — ikke valgt pr. 21.10.2026.** Kandidater i Trondheim-regionen:

- Unicon AS (Nedre Elvehavn / Trondheim)
- Franzefoss Minerals / Franzefoss Betong (allerede avfallsleverandør — mulig synergieffekt)
- Betong Øst AS
- NorBetong

**Bestillingsregler:**

- 24–48 timer forhåndsvarsel skriftlig per leveranse, med **alle** delkrav (fasthet, bestandighet, klorid, konsistens, utførelsesklasse, pumpbarhet)
- Ikke bestill til mandag morgen (produksjonsplan ikke klar søndag)
- Kontroller konsistensklasse ved levering (slagprøve)
- Ta sylinderprøver minimum 3 per 30 m³ for 28-dagers trykktest
- AUV-betong kan ha lengre leveringstid — spesifiser ved forespørsel

### 6.2 Armering — innkjøp og lagring

- Bestill etter RIB-produksjonstegning. Mengde ca. 150 kg/m³ for bunnplate og fundamenter under grunnvann (ISY 05.11): gir ca. 17 250 kg for 115 m³ bunnplate alene.
- B500NC, utførelsesklasse 2 eller 3 iht. post. Dimensjon per element — hovedsakelig Ø16 mm for vegger og delevegger (ISY 05.11).
- Lagres tørt på byggeplass. Kutt- og bøyeplan iht. RIB-tegning.
- `[KREVER PROFF]`-steg: kapping og bøying hvis det ikke kommer ferdig kuttet.

### 6.3 Forskalingsmateriell

- Leies via valgt entreprenør eller egen avtale. Mengder:
  - Fundament: 25 stk forskaling 200×200×40 cm (eller 3000×3000 — se avklaring).
  - Vegg ensidig: ca. 110 m².
  - Vegg tosidig: ca. 95 m².
  - Steng: 65 lm.
  - Forskaling i vann (fundamenter mot elv): varierende, antall uklart i ISY (QA-funn 10).

### 6.4 Stein — håndtering og mellomlagring

Mellomlager-plan:

- **Mellomlager A — Fjordgata (gateplan):** Container(e) 10 m³ for massetransport og generelt avfall. Krever kommunal tillatelse for midlertidig fortausbruk. Bestill 1 uke i forveien.
- **Mellomlager B — innvendig langs sørvegg:** Gjenbruksstein merket X.N (grønn spray), sortert for remontasje senere.
- **Mellomlager C — floa/kanalside:** Kuttede langsgående tømmerstokker fra F3, 2–2,5 m lengder, 200–300 kg hver. Transport via gulvåpning til springflo-vindu.

Steinhåndtering: naturstein 20–80 kg per stein, ergonomisk håndtering (ikke kast — legg). Grønn/rød merking for gjenbruk vs. avfall.

### 6.5 Masseflytting — løsmasser

- Totalt ca. 130 m³ fast volum fra graving innvendig (ISY 03.1), 10 m³ fra graving under vann (ISY 03.3), total ca. 200 tonn (ISY 03.6).
- Containerbytter ikke på søndager — planlegg gravedag-slutt til fredag.
- Transportavstand 6–9 km (ISY 03.5). Leveringssted ikke valgt — opp til entreprenør.
- Arkeolog kan kreve sortering/avlevering til NIKU for sålding.
- `[TBD: deponi-avtale, pris per tonn]`

### 6.6 Avhending — øvrige materialer

| Material | Mengde (anslag) | Håndtering | Leverandør |
|---|---|---|---|
| Gammel isolasjon (mineralull) | 1–2 m³ | Gjenbrukes som nedforing 1. etg (statusmøte 20.10 Post 09) | — |
| Elektriske installasjoner fra kjeller | Liten mengde | Container elektrisk | Franzefoss Gjenvinning |
| Trevirke (ikke gjenbruksbjelker) | Variabel | Container tre | Franzefoss Gjenvinning |
| Kulturhistoriske gjenstander | Ukjent | Avleveres NIKU | NIKU |

### 6.7 Vanntetting — innkjøp og montering

- SikaSwell® P Type H eller tilsvarende svelleprofil: 65 lm (ISY 05.6)
- Master VB2 160 eller tilsvarende fugeblikk: 65 lm (ISY 05.7)
- SikaSwell® P Ring 24 NO eller tilsvarende svellebånd: 25 stk (ISY 05.8)

Monteringen bør utføres av Sika-sertifisert montør eller etter Sika-anvisning. Dette er grensesnittet mellom «proff» og «egne folk»: feilmontert svelleprofil er den dyreste reparasjonen man kan ha (R03).

---

## 7. Rekkefølgediagram og grov Gantt

### 7.1 Kritisk sti

Hovedkritisk sti i prosjektet går via **arkeolog-dispensasjonen (kulturminneloven § 8)**. Alle fysiske graveoperasjoner nedover er blokkert av denne dispensasjonen.

```
G1 (RA-befaring) → F4a (målsatte tegninger) → F4b (søknad § 8) → F4c (saksbehandling 4–12 uker) → AG-1 → F5 → F6 → F7 → F8 → F9 → F10 → F11 → F12
```

### 7.2 Parallellaktiviteter

- F0 (vinterklargjøring) + F1 (oppmåling) kan kjøres parallelt.
- F2 (RIB-signering tømmer) kan starte så snart F1 er levert — parallelt med F4 (dispensasjonssøknad).
- F3 (rydding over gulvnivå) kan starte parallelt med F4 (saksbehandling).
- RIB-produksjonstegninger for F6/F7/F8/F9 kan tegnes parallelt med F4-saksbehandling.
- F11 (katodisk) prosjektering kan starte parallelt med F8/F9.
- Betongleverandør-prekvalifisering kan starte nå (ingen gate).

### 7.3 Grov Gantt — uker fra 21.10.2026

| Fase | Beskrivelse | Varighet | Uke 43 | Uke 44 | Uke 45 | Uke 46 | Uke 47 | Uke 48 | Uke 49–52 | Jan–mar 2027 | Apr–jun 2027 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| F0 | Vinterklargjøring | 1–2 uker | ████ | ████ |  |  |  |  |  |  |  |
| F1 | Oppmåling + registrering | 1 uke |  | ████ |  |  |  |  |  |  |  |
| F2 | RIB-signering tømmer | 1 uke |  |  | ████ |  |  |  |  |  |  |
| F3 | Rydding over gulv | 2–3 uker |  |  |  | ████ | ████ |  |  |  |  |
| G1 | RA-befaring |  |  |  | ██ |  |  |  |  |  |  |
| F4 | Dispensasjonssøknad | 1 uke + 4–12 uker saksbeh. |  |  | ████ | ████ | ████ | ████ | ████ |  |  |
| F5 | Graving | 2–3 uker |  |  |  |  |  |  |  | ████ |  |
| F6 | Søylefundamenter | 2–3 uker |  |  |  |  |  |  |  | ████ |  |
| F7 | Bunnplate | 2 uker |  |  |  |  |  |  |  | ████ |  |
| F8 | Yttervegger | 3 uker |  |  |  |  |  |  |  |  | ████ |
| F9 | Delevegger | 2 uker |  |  |  |  |  |  |  |  | ████ |
| F10 | Overflatebeh. | 1 uke |  |  |  |  |  |  |  |  | ████ |
| F11 | Katodisk | parallelt + 1 uke montering |  |  |  |  |  |  |  |  | ████ |
| F12 | Sluttdokumentasjon | 1 uke |  |  |  |  |  |  |  |  | ████ |

**Konsekvens:** Realistisk ferdigstillelse av kjelleren: Q2 2027. KMF-rapporteringsfrist 31.12.2026 nås ikke med fullført kjeller, men dispensasjonsprosessen og vinterklargjøring kan dokumenteres (R24).

**Hva kan dokumenteres til KMF 31.12.2026:**

- Komplett plan v01→v02
- Oppmåling og registrering fullført
- RIB-signert sikringsplan
- Dispensasjonssøknad etter § 8 innsendt
- RA-befaring gjennomført
- Fase 3 (rydding) i hovedsak fullført

### 7.4 Vinter-tilpasning

Fase 6–9 krever temperatur > 5 °C eller frosttelt + varme (R09). Realistisk:

- F6 (fundamenter): januar–februar 2027 med frosttelt
- F7 (bunnplate): februar–mars 2027 med frosttelt
- F8 (yttervegger): mars–april 2027
- F9 (delevegger): april 2027
- F10–F12: april–mai 2027

Alternativt kan oppstart utsettes til mai 2027 for å unngå frosttelt-kostnad — dette er en kostnad/tid-vurdering for byggherre.

---

## 8. Grensesnitt mot anbudsgrunnlag

### 8.1 Hvordan planen fungerer sammen med ISY-beskrivelsen

Ole Mortens ISY-beskrivelse (19.10.2026) er NS 3420-postlisten. Den dekker **hva** som skal utføres, med mengder og materialspesifikasjoner. Denne planen dekker **rekkefølge, operativ fremgangsmåte, risiko og dokumentasjon** — det som NS 3420-formatet ikke rommer.

Fordelt per kapittel:

- **Kapittel 00 (generell del):** ISY-beskrivelsens innbydelse-seksjoner er ikke fylt ut (QA-funn 1). Må fylles ut før utsendelse — denne planen gir ikke erstatning for det. Formell innbydelse må inneholde: anskaffelsesprosedyre, kunngjøringsmåte, kvalifikasjonskrav, tilbudsmerking, åpningsregler, tilbudsfrist, bindingstid.
- **Kapittel 03 (grunnarbeider):** ISY-postene 03.1–03.10 er dekket operasjonelt av Fase 4 (prøvegraving) og Fase 5 (hovedgraving) i denne planen.
- **Kapittel 05 (betongarbeider):** ISY-postene 05.1–05.29 er dekket operasjonelt av Fase 6 (søylefundamenter), Fase 7 (bunnplate), Fase 8 (yttervegger), Fase 9 (delevegger), Fase 10 (overflater).
- **Kapittel 40 (elkraft, katodisk):** ISY-post 40.2 er dekket av Fase 11 (katodisk).

### 8.2 De 12 QA-funnene i ISY-beskrivelsen

Fra utkast B — alle funn er bekreftet ved krysssjekk mot kildedokumentet. Må behandles før ISY-beskrivelsen sendes til entreprenør:

| # | Post | Funn | Status | Aksjon |
|---|---|---|---|---|
| 1 | Kap. 00 innbydelse | Alle felt tomme, dobbelt angitt | Kritisk | HRP: Fyll ut alle felt, slett duplikater. Alternativ: direkte forespørsel til 3–5 kjente leverandører som ikke krever formell innbydelse. |
| 2 | Kap. 00 NS 3420-versjon | «xxxx» ikke fylt inn | Mindre | HRP: Fyll inn versjonsnummer (NS 3420, 4. utgave, versjon 2020 eller aktuell). |
| 3 | Kap. 03, alle poster | Arkeolog-avklaring mangler, mengder er regulerbare | Vesentlig | Behold regulerbar-klausul; avklares i Fase 4 (denne planen). |
| 4 | Post 03.9 | Feil måleangivelse (lengde vs. m³) | Vesentlig | HRP: Avklar enhet; antakelig m³. Endre kode eller tittel. |
| 5 | Post 05.9 | Feil enhet (kg i stedet for m²), blandet innhold (forskaling + armering + betong i én post) | Kritisk — uleselig | HRP: Split i tre poster — forskaling (m²), betong (m³), armering (kg). |
| 6 | Post 05.11/05.12 | Duplikat kode, to ulike mengder (90 og 205 m²) | Vesentlig | HRP + RIB: Klargjør to separate poster med kg-mengder iht. produksjonstegning. |
| 7 | Post 05.13 | Armering delevegger/yttervegger — mengde mangler | Vesentlig | RIB: Levere armeringsplaner, HRP legger inn kg-mengder. |
| 8 | Post 05.17 | To ulike volumer (9 og 20 m³), tunge tilslag uklart | Vesentlig | HRP + RIB: Avklar volum. Fjern «tunge tilslag» hvis det ikke er strålings-/skjermingshensikt. Kloridklasse Cl 1,0 avvikende fra andre poster — avklar. |
| 9 | Post 05.18 | Duplikat kode av 05.15, volum mangler | Kritisk | RIB: Avklar volum etter dokumentasjon av eksisterende fundamentdimensjoner (del av F1). |
| 10 | Post 05.19–05.25 | Radonsperre uten m², overflatepost = 0 m², forskaling i vann uten antall | Vesentlig | HRP: Reell mengde for radonsperre (ca. 90 m²); overflatebearbeiding — avklar om inkludert i betongpost eller skal ha egen pris; forskaling i vann — antall fundamenter som skal forsterkes. |
| 11 | Post 05.27/05.28 | Duplikat kode, inkonsistente mengder (30 vs. 110 m² i 05.27) | Vesentlig | HRP: Split i to entydige poster: 05.27 for XPS under gulv (ca. 30 m²?), 05.28 for XPS mot yttervegg (ca. 110 m²?). Konsistent. |
| 12 | Post 40.2 | RS uten anodetype, areal eller spesifikasjon | Kritisk | Katodisk korrosjonsspesialist (F11) prosjekterer og leverer mengder/type — innarbeides i oppdatert ISY. |

**Ekstra funn (fra denne synteseoppgaven):**

- **Fundamentdimensjon-motsetning (post 05.1 vs. 05.29):** 200×200×40 cm vs. 3000×3000 mm. Trolig er 05.1 korrekt (vanlig norsk fundamentdimensjon), 05.29 er skrivefeil. Bekreftes av HRP og RIB før F6 starter. **Dette er den viktigste enkeltavklaringen i hele planen.**
- **Statusmøte 22.10 Post 02:** Beslutning om helhetlig plate (uten glidebolter) må reflekteres i ISY-beskrivelse. ISY sier allerede «450 mm armert plate» men ikke eksplisitt «helhetlig». Oppdater post 05.14.
- **Statusmøte 22.10 Post 03:** Radonsperre søkes dispensasjon fra. Post 05.19 beholdes i ISY som fallback.

### 8.3 Prispostiller — hva entreprenør skal gi tilbud på

Denne planen er ikke selve anbudsbrevet, men den gir strukturen for prisstetterspørsel. Hovedelementer entreprenøren skal prise:

**Timepriser per fagkategori:**

- Betongbas / fagarbeider betong
- Forskalingstekniker
- Pumpebiloperatør (inkl. pumpe)
- Kalibrator / korrosjonstekniker (katodisk)
- Kranfører (inkl. kran) hvis tunge forskalingselementer

**Enhetspriser betong og materialer:**

- Ferdigbetong B45 MF40 Cl 0,10 vanntett per m³
- Ferdigbetong AUV B45 MF40 Cl 0,10 per m³
- Ferdigbetong C25/30 XC1 per m³ (delevegger — hvis valgt)
- Armering B500NC per kg (etter diameter)
- Systemforskaling leie per m² per uke
- Svellebånd SikaSwell® P Type H per lm
- Fugeblikk Master VB2 160 per lm
- Svellebånd P Ring 24 NO per stk
- XPS 50 mm per m²
- Radonmembran per m²
- Betongpumping (mobilisering RS + per m³)

**Rigg og drift:**

- Etablering, drift per uke, avrigg
- Mobilisering og demobilisering per innrykk

**Regningsarbeider (nevnt eksplisitt):**

- Tilpasning mot irregulær natursteinsmur-profil
- Reparasjon/overstøping av eksisterende fundamenter mot elv (omfang avhenger av F5C)
- Armeringsforankring (innboring + gysing) inn i eksisterende fundamenter om RIB krever det
- Spesialtilpasning rundt stålsøylegjennomføring Ø avviker fra 150–200 mm

---

## 9. Figur-sammenstilling

Følgende figurer er nødvendige for v02 av denne planen og for dispensasjonssøknaden. **Ingen av disse skal produseres som SVG/CAD i denne tekstleveransen** — alle er tekstbeskrivelser som skal realiseres via håndtegning, ChatGPT-rendring, eller profesjonell tegning fra RIB/HRP/Ain avhengig av type.

| # | Figur | Fase | Perspektiv | Målestokk | Innhold | Produseres av |
|---|---|---|---|---|---|---|
| 1 | Plantegning 1. etg — vinterklargjøring | F0 | Ovenfra, nord opp | 1:50 | Toalett/varmesone, kjellernedganger, container, brannslanger | Ole Morten eller Ain (håndskisse) |
| 2 | Plantegning kjeller — nåværende tilstand | F1 | Ovenfra, nord opp | 1:50 | Alle søyler fargekodet, langsgående stokker, løse stein, gulvplanker, fundamenter 1983 | Ole Morten |
| 3 | Langsnitt kjeller — nåværende tilstand | F1 | Vertikalt langsnitt | 1:50 | Natursteinsmur, kavlegulv, bolverk, antatt grunnkote | Ole Morten |
| 4 | Tverrsnitt kjeller — nåværende tilstand | F1 | Vertikalt tverrsnitt | 1:50 | Breddeprofil, natursteinsmur begge sider, antatt grunnkote | Ole Morten |
| 5 | Sikringsplan — snitt midlertidige støtter | F2 | Langsnitt | 1:20 | Representativ L-stokk med støtte (bukk/stag) under, RIB-signeringsboks | Ole Stenmo (RIB) |
| 6 | Arbeidsflytplan Fase 3 | F3 | Ovenfra | 1:50 | Flyt-piler, mellomlager A/B/C, gulvåpning, lensepumpe | Ole Morten / Ain |
| 7 | Målsatt graveomfang — plan | F4 | Ovenfra | 1:50 | Rød skravur for graveområde, prøvegravepunkter | Ole Stenmo (RIB) + Ole Morten |
| 8 | Målsatt graveomfang — snitt | F4 | Vertikalt tverrsnitt | 1:50 | Dagens kote, prosjektert kote, graveskråning, dim. vannstand | Ole Stenmo (RIB) |
| 9 | Snitt arbeid mot elv | F4 | Vertikalt tverrsnitt | 1:50 | Fundament utside, graveprofil 1:3, tidevannsnivåer | Ole Stenmo (RIB) |
| 10 | Graveprofil og kote-angivelse | F5 | Tverrsnitt | 1:20 | Gravedybde per sone, min. avstand til fundament | Ole Stenmo (RIB) |
| 11 | Logistikkplan Fase 5 | F5 | Ovenfra | 1:50 | Vinsjekurv, container, slangetrasé | Kristian / Ole Morten |
| 12 | Fundament-plan (25 stk) | F6 | Ovenfra | 1:50 | X/Y-koordinater per fundament, aksesystem | Ole Stenmo (RIB) |
| 13 | Fundament-snitt | F6 | Vertikalt snitt | 1:10 | XPS, armering, overdekning, søylegjennomføring | Ole Stenmo (RIB) |
| 14 | Plan bunnplate armering | F7 | Ovenfra | 1:50 | Armeringsraster, forankring søyler, svelleprofil-kant | Ole Stenmo (RIB) |
| 15 | Snitt bunnplate — alle lag | F7 | Vertikalt snitt | 1:10 | Drenslag, XPS, radonsperre, armering, betong 450 mm, overgang kant | Ole Stenmo (RIB) |
| 16 | Detalj — søylegjennomføring | F7 | Snitt | 1:5 | Stålsøyle, svellebånd, armering tett om søyle | Ole Stenmo (RIB) |
| 17 | Snitt yttervegg — detaljert | F8 | Vertikalt tverrsnitt | 1:10 | Natursteinsmur, plast/tett duk, XPS, betong, svelleprofil + fugeblikk | Ole Stenmo (RIB) |
| 18 | Plan vegger og forskalingsetapper | F8 | Ovenfra | 1:50 | Alle fire vegger, vektergang, steng-overganger, støpeskjøter | Ole Stenmo + forskalingstekniker |
| 19 | Snitt klimaskille | F8 | Vertikalt snitt | 1:10 | Overgang kjeller → 1. etg., isolasjon, dampsperre, lufttetthet | Ole Stenmo eller HRP |
| 20 | Plan delevegger | F9 | Ovenfra | 1:50 | Nord- og sørdelevegg, forankringer | Ole Stenmo (RIB) |
| 21 | Anode-plan | F11 | Ovenfra | 1:50 | Anoder, kabelføringer, tilkoblingspunkt | Katodisk spesialist |
| 22 | Materialflyt-flytskjema | — | Flytskjema | — | Alle materialstrømmer inn/ut av byggeplassen | Kristian / Eirik |

**Fordeling av arbeid:**

- **Ole Stenmo (RIB):** 11 figurer (nr. 5, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 20) — hovedansvar for alle prosjekteringstegninger.
- **Ole Morten (PGL):** 4 figurer (nr. 2, 3, 4, 6) — oppmålings- og tilstandsregistrering.
- **Kristian/Ain:** 2 figurer (nr. 1, 11) — operasjonell logistikk.
- **Katodisk spesialist:** 1 figur (nr. 21).
- **Ole Stenmo + forskalingstekniker:** 1 figur (nr. 18) — forskalingsplan.
- **Ole Stenmo eller HRP:** 1 figur (nr. 19) — klimaskille.
- **Kristian + Eirik:** 1 figur (nr. 22) — materialflyt-oversikt.

---

## 10. Åpne spørsmål og neste skritt

### 10.1 Prioriterte avklaringer før v02

Følgende må lukkes før v02 kan ferdigstilles og sendes til RIB, entreprenør eller myndigheter:

**Prioritet 1 — blokkerende for F2–F6:**

1. **Fundamentdimensjon-motsetning (post 05.1: 200×200 cm vs. post 05.29: 3000×3000 mm).** Ansvarlig: Byggherre skriver til HRP og RIB. Frist: før F6 starter.
2. **Søyleoppmåling innerst mot Fjordgata.** Pågår 21.10.2026 (Ole Morten). Resultat inkorporeres i Tegning 1 (Fase 1).
3. **Armeringstegninger fra RIB** (produksjonsunderlag for F6, F7, F8, F9). Ansvarlig: Ole Stenmo. Må være klar før hver fase starter.
4. **Dispensasjon kulturminneloven § 8.** Ansvarlig: Byggherre + PGL. Blokkerer F5. Realistisk saksbehandlingstid 4–12 uker.
5. **SB-godkjenning for betongarbeider** (ansvarlig utførende). Modell A: entreprenøren tar SB. Modell B: enten innleid firma eller Kristians firma KMTE om godkjent (R11, R22). Avklares før F6.

**Prioritet 2 — blokkerende for v02-utsendelse:**

6. **Betongleverandør** — prekvalifiser 2–3 kandidater, be om prøvelevering og slagprøve.
7. **Betongklasse delevegger** — avklar C25/30 XC1 vs. B45 M40 Cl 1,0 (QA-funn 7, 8).
8. **Volum fundamenter mot elv** — RIB må levere mengde (QA-funn 9).
9. **Radonsperre-dispensasjon** — Ole Morten skriver argument som del av rammesøknad-arbeid (statusmøte 22.10 Post 03).
10. **Verifisere gnr/bnr mot matrikkelen.**

**Prioritet 3 — kan avklares parallelt med F3–F5:**

11. **Katodisk korrosjonsspesialist** — kontakt leverandør, be om budsjett-prosjektering.
12. **Deponi-avtale** for 200 tonn løsmasser.
13. **Statsforvalter/NVE-tillatelse** for arbeid mot elv.
14. **Igangsettingstillatelse (IG)** fra Trondheim kommune.
15. **Alle 12 QA-funn** returneres til HRP for innarbeidelse i ISY-beskrivelsen.

### 10.2 Neste skritt (konkret, uke-for-uke)

**Uke 43 (pågår, 21.–25.10.2026):**

- Oppmåling søyler (Ole Morten, 21.10) ✓
- Felles befaring Ole Morten + Kristian (statusmøte 22.10) — tidspunkt når Kristian er tilbake
- Ole Mortens kjellernotat med sikringsplan ferdigstilles (helg/mandag 25.–26.10)
- Byggherre leser v01 av denne planen (dette dokumentet), gir tilbakemelding

**Uke 44 (26.10–01.11.2026):**

- Kjellerstart mandag 26.10 (Ain + Marco) med lavrisk-arbeid (statusmøte 22.10 Post 05)
- Vinterklargjøring intensiveres (Fase 0)
- Dispensasjonssøknad etter § 8 forberedes (målsatte tegninger)
- RA-befaring foreslås — kontakt Riksantikvar

**Uke 45 (02.–08.11.2026):**

- RA-befaring (ambisiøst)
- RIB-signering sikringsplan (G2 / RG-1)
- Dispensasjonssøknad sendes

**Uke 46–48:**

- Fase 3 (rydding over gulvnivå)
- Dispensasjon under saksbehandling

**Uke 49–52:**

- Dispensasjon forhåpentligvis innvilget
- Forberedelse til graving (Fase 5)
- Fase 4-tillatelser for arbeid mot elv kommer inn

**Januar–mars 2027:**

- Fase 5–7 (graving, fundamenter, bunnplate)

**April–juni 2027:**

- Fase 8–12 (vegger, delevegger, overflater, katodisk, sluttdokumentasjon)

---

## 11. Appendiks — syntese-notat

*Dette avsnittet er skrevet til byggherre som gjennomgang. Det forklarer hvilke valg som er tatt når de tre Sonnet-utkastene spriket, hvilke egne tillegg som er gjort, og hva som er anbefalt høyest ROI på neste iterasjon.*

### 11.1 Konsensus mellom de tre utkastene

Alle tre utkastene (A — bakeoppskrift, B — anbud/entreprenør, C — RIB/risiko/materialflyt) er enige om følgende hovedpunkter:

- **Fasestruktur grovt:** forberedelse → RIB-gating → rydding → arkeologgate → graving → fundamenter → bunnplate → vegger → delevegger → overflatebearbeiding → katodisk → sluttdokumentasjon.
- **Hard-coded verdier:** B45 MF40 Cl 0,10 for vanntette konstruksjoner, 450 mm bunnplate, 250 mm yttervegger (tosidig del), kote +3,20 som dim. vannstand, XS3 eksponeringsklasse, R60 brannkrav.
- **Dispensasjon etter kulturminneloven § 8 er kritisk sti.** Alle tre utkastene fremhever dette som den viktigste gating-faktoren.
- **RIB-gates er bindende** før kutting, armering og støping. Alle tre utkastene har eksplisitte RIB-signeringspunkter.
- **Katodisk korrosjonsbeskyttelse** krever spesialist — kan ikke gjøres som DIY (alle tre).
- **Risikoer med høyeste prioritet:** vanntetting (R03), setningsskader (R01), arkeologi (R06), forsikringshull ved egne folks betongarbeid (R11).

Denne konsensusen er sannsynligvis riktig og brukes som grunnlag i v01.

### 11.2 Hvor utkastene spriker — og hva som er valgt

**Antall faser.** Utkast A har 9 faser (F0–F8), utkast C har 11 faser (F0–F11). Utkast B har 9 faser (0–8). Valgt i v01: **12 faser (F0–F12)**, basert på utkast C-strukturen men med egen F12 for sluttdokumentasjon (viktig for KMF/Enova-rapportering) og delevegg som egen fase (F9) i stedet for å blande med yttervegger. Dette gir klarere gates per fase.

**Rekkefølge yttervegger vs. delevegger.** Utkast A behandler alle vegger som én fase. Utkast C skiller delevegger (F9) fra yttervegger (F8). Valgt: utkast C-strukturen, siden yttervegger er XS3 vanntett og delevegger er XC1 eller B45 M40 Cl 1,0 — vesentlig ulike kvalitetskrav og forskalingsutfordringer.

**Fundamentdimensjon.** Utkast A siterer 200×200×40 cm (ISY 05.1), utkast B siterer 2000×2000×400 mm, utkast C henviser til 05.1 (altså 200×200). Men ISY-post 05.29 for isolering under samme fundamenter sier 3000×3000 mm. Ingen av de tre Sonnet-utkastene flaggerer denne motsetningen eksplisitt som blokkerende. Valgt i v01: **flagget som blokkerende før F6 starter (R18)**, med anbefaling om at 200×200 trolig er korrekt (vanlig norsk fundamentdimensjon for stålsøyler) og 3000×3000 i post 05.29 er trolig skrivefeil. Må bekreftes av HRP og RIB.

**Hvor mye av arbeidet er «proff»-krav.** Utkast A plasserer `[KREVER PROFF]` på alle vanntette betongoperasjoner. Utkast B skiller mellom «fagsignatur» og «fagutførelse». Utkast C er mer åpen for hybrid utførelse. Valgt i v01: **detaljert `[KREVER PROFF]`-flagging per steg**, med Modell A (hel entreprise) og Modell B (egne folk + proff-timesleie) som eksplisitte alternativer. Beslutning om modell er byggherres (R11, R22).

**Vinterforhold.** Utkast A nevner frostbeskyttelse kort. Utkast C har egen Del 6 om vinterklargjøring med Prioritet 1/2/3. Utkast B behandler ikke vinter som egen problem-stilling. Valgt: **egen Fase 0 i v01 med detaljert vinterklargjøring**, basert på utkast C og supplert med beslutning fra statusmøte 20.10 Post 07.

**Gantt-struktur.** Utkast A har ukenummer 1–10. Utkast C har ukenummer 43–52 + 2027. Utkast B har indikative uker. Valgt: **utkast C-tilnærmingen med reelle kalenderuker fra 21.10.2026**, med utvidelse til Q2 2027 fordi R24 (vinterforsinkelse) er sannsynlig.

### 11.3 Egne tillegg — ting ingen av Sonnet-agentene hadde dekket

De fem viktigste egne tilleggene i v01:

1. **R18 — Fundamentdimensjon-motsetning som eksplisitt risikopunkt.** Alle tre utkastene nevner inkonsistensen (eller ikke), men ingen behandler den som en separat risiko. I v01 er den rangert som høy sannsynlighet (R18, S=4) fordi den **blokkerer** F6, og med klar aksjon og ansvarlig før F6 starter.
2. **R19–R24 — seks nye risikoer:** betongleverandør svikter, pumpebil kommer ikke frem, konflikt mellom egne folk og innleid betongbas, Enova/KMF-krav om fagsignatur på ikke-tilstede-dag, BEV-stokker ødelegges ved uhell, vinterforhold forsinker hele F6–F9. Disse er alle plausible scenarier som Sonnet-utkastene ikke dekket.
3. **Fase 12 — Sluttdokumentasjon som egen fase.** Verken utkast A, B eller C har eksplisitt sluttdokumentasjon-fase. Dette er kritisk for KMF-tilskudd (dokumentasjon av fagutførelse) og for byggesak (sluttmelding/ferdigattest).
4. **Grensesnitt-tabell mellom plan og ISY (del 8).** Ingen av utkastene lenker fasene i planen eksplisitt til NS 3420-postene i ISY-beskrivelsen. Dette er gjort i v01 for å gjøre QA-funnene operative — hver post vet nå hvilken fase den tilhører og hvilken RIB-gate som gjelder.
5. **Hybrid modell (Modell C i del 3.3) — eksplisitt beskrevet.** Utkast B deler i Modell A og B. I praksis vil prosjektet nok ende i en blandet modell: helentreprise på bunnplate og vanntette yttervegger, timesleie på forberedende arbeider. Dette er beskrevet eksplisitt i v01.

Andre tillegg som ikke var i noen av Sonnet-utkastene:

6. **Pren-testing av stokker (Fase 1, F1.8)** med 0–3 skala for råtegrad — gir objektiv dokumentasjon til RIB.
7. **BEV-grønn-merking** for tjukke tverrgående stokker (beslutning statusmøte 25.10 Post 02) som egen prosedyre.
8. **Alle gates nummerert (RG-x, AG-x, MG-x)** for enklere referanse.
9. **Igangsettingstillatelse (IG) som egen myndighets-gate (MG-4)** — ikke eksplisitt i noen av Sonnet-utkastene.
10. **Vinterschedule som egen diskusjon (del 7.4)** med realistisk anerkjennelse av at kjelleren ikke ferdigstilles i 2026.
11. **Pumpebiltilkomst-sjekk (R20)** som eget risikopunkt — Fjordgata er smal, dette er en reell logistikkutfordring.
12. **Fase 11 (katodisk) som prosjektering-parallell** — kan starte prosjekteringen i F8 for å spare tid.

### 11.4 De 3 viktigste anbefalinger for byggherre etter gjennomlesing

**1. Lukk fundamentdimensjon-motsetningen umiddelbart.** Skriv til HRP (Ole Morten) og RIB (Ole Stenmo) denne uken. Spørsmål: er fundamentmålet 200×200×40 cm (ISY 05.1) eller 3000×3000 mm (ISY 05.29)? Hvis 3000×3000 er korrekt, må alle fundamentmengder (betong, armering, graving, XPS) revideres oppover vesentlig — og det kan påvirke KMF-estimat. Hvis 200×200 er korrekt (sannsynlig), er det en skrivefeil i post 05.29 som enkelt rettes. Dette er den viktigste enkeltavklaringen i hele prosjektet.

**2. Beslutt utførelsesmodell (A, B eller C) raskt — det styrer alt annet.** Modell A (hel entreprise) gir forutsigbarhet men høyest kostnad. Modell B (egne folk + proff-timesleie) gir laveste pris men stor byggherrebelastning og forsikringsrisiko. Modell C (hybrid) er trolig riktig, men krever at **du som byggherre selv tar grepet** og bestemmer hvilke faser som er hvilken modell. Mitt forslag: F0, F1, F2, F3, F4 egne folk; F5 egne folk + arkeolog-tilsyn; F6, F7, F8 hel entreprise eller tung proff-innleie (dette er den vanntette, kritiske delen); F9, F10 egne folk med fagsignatur per operasjon; F11 spesialleverandør; F12 egne folk.

**3. Start dispensasjonssøknad etter § 8 denne uken.** Dette er kritisk sti — hver uke uten innsendt søknad er en uke tapt for ferdigstillelse. Målsatte tegninger kan være ufullstendige — send en foreløpig søknad med «Målsatte tegninger ferdigstilles innen 2 uker» hvis tegningene ikke er klare. Riksantikvaren vil heller ha en søknad under utarbeidelse enn ingen søknad.

### 11.5 Hva v02 bør inneholde

Når byggherre har gått gjennom v01 og besvart hovedavklaringene (fundamentdimensjon, utførelsesmodell, dispensasjonsfremdrift), skal v02 oppdateres med:

- Søyleposisjoner innerst mot Fjordgata (fra oppmålinger 21.10.2026)
- Lukket fundamentdimensjons-motsetning
- Avklart betongklasse delevegger
- Avklart volum fundamenter mot elv
- Innarbeidelse av RIB-produksjonstegninger (når de foreligger)
- Innarbeidelse av katodisk korrosjon-prosjekteringsrapport
- Oppdaterte mengder i materialflyt-oversikten (del 6)
- Første virkelige Gantt med reelle datoer basert på RA-befaringsdato
- Lettvekts BYA-versjon (parallellt — kortere, mindre teknisk)
- Entreprenør-anbudsutsendelse-vedlegg (dette dokumentet + ISY-beskrivelsen med alle QA-funn lukket)

---

*Dokument slutt — kjellerplan v01, 21.10.2026. Dette er førsteutkast til intern gjennomgang hos byggherre KodeWorks Eiendom AS. Endringer i dispensasjonsvilkår, RIB-tegninger, arkeologiske funn eller utførelsesmodell kan medføre vesentlige revisjoner. Dokumentet erstatter ikke prosjekteringsgrunnlag fra RIB eller godkjent tegningssett.*
