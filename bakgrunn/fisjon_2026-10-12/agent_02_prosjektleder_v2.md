# Agent 2 — Prosjektleder v2: Oppdatert operasjonell plan

**Rolle:** Prosjektleder — regnskapsfører, revisor, selskapsadvokat, Brreg, Skatteetaten, tinglysing, bank. Praktisk gjennomføring: hvem gjør hva, i hvilken rekkefølge, til hvilken pris. \
**Dato:** 2026-10-12 (iterasjon 2) \
**Scope:** Fase 4 — analyse-only. Ingen kontakt med eksterne. Lovreferanser som ikke er verifisert mot Lovdata i verifikasjonsfasen er merket. Dette dokumentet erstatter ikke v1 — det bygger på det. \
**Nøkkelendring vs. v1:** Bank-usikkerheten er i stor grad borte (DNB bekrefter overtakelse av Grønnegata-lån). BFU-sporet er droppet (Skatteetatens veiledning av 11.09.2026 er bekreftelse nok). Faktiske regnskapstall per 08.10.2026 ligger til grunn. To nye aksjonærer (Brandsegg, Lagmannssveen) kommer inn i FG30 AS etter fisjonen gjennom etterfølgende emisjon mot tingsinnskudd.

---

## 1. Oppdatert aktørliste med rolle og konkret leveranse

Diff vs. v1: bank-rollen krympes fra forhandlingspart til bekreftelsesmottaker; MVA-spesialist beholdes men med redusert scope; MVA-spesialist for justeringsavtale beholdes selv om fisjon-før-registrering gjør justeringsavtale unødvendig — fordi tidsrekkefølgen må kvalitetssikres; **emisjonsadvokat/selskapsadvokat for emisjon** og **tingsinnskudd-revisor** legges til som eksplisitte roller etter fisjon.

| Aktør | Rolle i v2 | Konkret leveranse |
|---|---|---|
| **Selskapsadvokat** (ekstern — fisjon kan ikke egen-utføres) | Hovedansvarlig for fisjonsplan + etterfølgende emisjon | Som i v1 + aksjonæravtale FG30 AS, kapitalforhøyelses-protokoll, nye vedtekter FG30 AS, dokumenter til emisjon mot tingsinnskudd |
| **Revisor** (statsautorisert) | Attestasjon fisjonsplan og åpningsbalanser; i tillegg: tingsinnskudd-erklæring til emisjon | Som i v1 + revisorerklæring etter asl. § 2-6 (tingsinnskudd) [verifiseres mot Lovdata] ved emisjon av nye aksjer til Brandsegg/Lagmannssveen |
| **Regnskapsfører** (nåværende regnskapsbyrå) | Som i v1, men nå med konkret saldobalanse 08.10.2026 som utgangspunkt | Oppdatert saldobalanse per fisjonsstikkdag (foreslått 01.01.2027), fordelingsmodell basert på eksisterende kontoposter, åpningsbalanser i tallformat, bistand ved MVA-melding i overdragelsesterminen, nye regnskapsoppsett for FG30 AS og Grønnegata 10 AS |
| **Brønnøysundregistrene — Foretaksregisteret** | Som i v1 — ingen endring | Som i v1 |
| **Skatteetaten — Næring** | **BFU dropet.** Vanlig MVA-registrering av FG30 AS etter fisjon. Ingen justeringsavtale fordi KWE ikke blir MVA-registrert før fisjon. | (1) Mottar skatteopplysninger om fisjon (kontinuitet etter sktl. kap. 11); (2) registrerer FG30 AS i MVA-registeret etter fisjon (ordinær § 2-1 for valet storage; frivillig § 2-3 for kontor og B2B-boder); (3) registrerer Grønnegata 10 AS i MVA-registeret (frivillig § 2-3 for kontorutleie) |
| **Kartverket — Tinglysing** | To skjøter, som i v1 | Hjemmelsoverføring Fjordgata 30 til FG30 AS og Grønnegata 10 til Grønnegata 10 AS, med dokumentavgiftsfritak |
| **DNB** (bank) | **Bekreftelsesrolle.** Flytter lån 8210.58.15383 (15,2 MNOK + renter) fra KodeWorks Eiendom AS til Grønnegata 10 AS | Skriftlig samtykke til hjemmelsoverføring Grønnegata 10, revidert lånedokument med Grønnegata 10 AS som debitor, revidert pantedokument med ny eier som pantsetter. Fjordgata 30: ingen bankrolle (ingen pant). |
| **Byggesakskontoret, Trondheim kommune** | Som i v1 | Melding om endret tiltakshaver fra KWE til FG30 AS |
| **Riksantikvaren** | Som i v1 | Underretning etter fisjonsgjennomføring |
| **Tilskuddsgivere** (KMF, BYA, UNI, Enova KL, Enova OM) | Som i v1 | Som i v1 — særlig Enova OM-samtykkebrev må prioriteres |
| **TBRT og innkreving** | Fortsatt kreditor; krav på kr 184 000 (hvorav kr 103 452,03 på 3. innkreving) | Får ordinært kreditorvarsel via Brreg-kunngjøringen. Proaktiv tilleggsvarsling evalueres når fisjonsplanen nærmer seg ferdig (jf. bruker-input Q2) |
| **Namsfogden** | Som i v1 | Avhengighet: konkursvarsel-fristen 27.10.2026 |
| **Styret og generalforsamlingen** i KWE og KodeWorks AS | Som i v1 | Styret innstiller fisjonsplan; generalforsamlingen vedtar |
| **Nye aksjonærer: Brandsegg og Lagmannssveen** | Kommer inn etter fisjon via emisjon mot tingsinnskudd | Signatur på aksjonæravtale FG30 AS; dokumentasjon av tingsinnskuddets verdi for revisor |
| **Advokat for emisjon og aksjonæravtale** (kan være samme som selskapsadvokat) | Emisjonsprotokoll, aksjonæravtale, dokumentasjon av tingsinnskudd | Egen leveransepakke etter fisjonsgjennomføring |

---

## 2. Fordeling av eiendeler og gjeld — konkret utkast per 08.10.2026

### 2.1 Prinsipp

Brukerens krav fra fase 2: Grønnegata 10 AS skal ikke være solidaransvarlig for noe annet enn seg selv. Aksjeloven § 14-11 [verifiseres mot Lovdata] gir solidaransvar som default, men beløpsmessig begrenset til hvert selskaps nettoverdi. For å minimere Grønnegata 10 AS' eksponering:

1. Alle kjente forpliktelser fordeles **eksplisitt** i fisjonsplanen (gjør solidaransvaret subsidiært).
2. Konsernintern gjeld (10,6 MNOK + påløpt rente 89 TNOK) blir **i fortsettende KWE** — dette tjener som dekningsgrunn for fortsettende og reduserer omstøtelsesrisikoen (Grønnegata 10 AS kan ikke like lett angripes hvis det fortsettende har reell dekning).
3. Påløpt tvangsmulkt (kr 184 000) blir i **fortsettende KWE** — konsistent med Alt 1A fra fase 1 og beskytter partsstatus i DSB-/Sivilombud-sakene.
4. Alle driftsmessig allokerbare poster følger den eiendommen de hører til.

### 2.2 Konkret fordeling (basert på balanse 08.10.2026)

| Konto | Post | Fortsettende KWE | FG30 AS | Grønnegata 10 AS | Kommentar |
|---|---|---:|---:|---:|---|
| 1160 | Fjordgt. 30 bygg | | 7 333 401 | | Følger eiendommen |
| 1172 | Renovering FG30 | | 817 151 | | Aktivert påkostning følger eiendommen |
| 1164 | Grønnegata 10 bygg | | | 16 822 620 | Følger eiendommen |
| 1167 | Grønnegata 10 fast teknisk | | | 1 329 633 | Følger eiendommen |
| 1251 | Møbler/inventar Grønnegata | | | 207 424 | Følger virksomheten |
| 1260 | Fast bygningsinventar Grønnegata | | | 318 409 | Følger eiendommen |
| 1250 | Pinball-maskin | 17 703 | | | Ikke-stedbundet; blir i KWE (lav verdi, driftsnøytral) |
| 1299 | Kalkulatoriske avskrivninger | | –325 719 | –325 719 | 50/50 fordeling, kan justeres etter faktisk bygg-andel (ca. 44/56) |
| 1396 | Depositum (24k) | | | 24 000 | Antar depositum knyttet til kontorutleie — bruker verifiserer |
| 1500 | Kundefordringer (27k) | | 10 000 | 17 000 | Følger faktura-opphav; bruker/regnskapsfører fordeler |
| 1580 | Avsetning tap kundefordringer | | –11 000 | –18 900 | Følger kundefordringer forholdsmessig |
| 1921 | Bankinnskudd DNB (706k) | 150 000 | 300 000 | 255 655 | Fortsettende KWE beholder minimum driftslikviditet; resten fordeles. **Må revideres mot likviditetsbehov per fisjonsstikkdag** |
| 2000 | Aksjekapital | –30 000 | nystiftet | nystiftet | KWE beholder sin AK; FG30 AS og Grønnegata 10 AS stiftes med min. kr 30 000 hver |
| 2030 | Annen innskutt egenkapital | –43 836 | | | Historisk; blir i KWE |
| 2050 | Annen egenkapital | –26 164 | | | Historisk; blir i KWE |
| 2221 | DNB-lån Grønnegata | | | –15 233 691 | **DNB bekrefter overflytting.** Følger eiendommen og pantet |
| 2222 | Påløpt rente DNB | | | –831 546 | Følger lånet |
| 2400 | Leverandørgjeld (488k) | 50 000 | 350 000 | 88 000 | Fordeles etter faktura-opphav; bruker/regnskapsfører må gå gjennom leverandørreskontro. **Grovt estimat her — stor andel antas FG30-relatert (byggefase)** |
| 2900 | Forskudd fra kunder (101k) | | | 101 000 | Antas knyttet til kontorleie Grønnegata (konto 3690) — bruker verifiserer |
| 2923 | Konsernlån fra KodeWorks AS | –10 603 122 | | | **Blir i fortsettende KWE** som dekning |
| 2950 | Påløpt rente konsernlån | –88 932 | | | Følger konsernlånet |
| | **Påløpt tvangsmulkt (ikke bokført, 184 000)** | **–184 000** | | | Alt 1A: beskytter partsstatus i DSB/Sivilombud |

### 2.3 Preliminær egenkapital i hvert selskap

**Fjordgata 30 AS:**
- Eiendeler: bygg 7 333 401 + renovering 817 151 – avskrivninger 325 719 + bank 300 000 + fordringer netto –1 000 = **8 123 833**
- Gjeld: leverandørgjeld 350 000 = **350 000**
- **Netto egenkapital ca. 7,77 MNOK** før aksjekapital
- Av dette settes kr 100 000 til aksjekapital, resten (ca. 7,67 MNOK) til overkurs/annen egenkapital

**Grønnegata 10 AS:**
- Eiendeler: bygg 16 822 620 + teknisk 1 329 633 + inventar 525 833 – avskrivninger 325 719 + bank 255 655 + depositum 24 000 + fordringer netto –1 900 = **18 630 122**
- Gjeld: DNB-lån 15 233 691 + påløpt rente 831 546 + leverandørgjeld 88 000 + forskudd kunder 101 000 = **16 254 237**
- **Netto egenkapital ca. 2,38 MNOK** før aksjekapital
- Av dette settes kr 100 000 til aksjekapital, resten (ca. 2,28 MNOK) til overkurs

**Fortsettende KodeWorks Eiendom AS:**
- Eiendeler: pinball 17 703 + bank 150 000 = **167 703**
- Gjeld: konsernlån 10 603 122 + påløpt rente 88 932 + leverandørgjeld 50 000 + påløpt tvangsmulkt 184 000 = **10 926 054**
- Eksisterende EK før fisjon: aksjekapital 30 000 + annen innskutt 43 836 + annen EK 26 164 = 100 000
- **Netto egenkapital etter fisjon: sterkt negativ (ca. –10,76 MNOK)**

### 2.4 Insolvensproblematikken i fortsettende KWE

Dette er den største risikoen i den foreslåtte fordelingen. Fortsettende KWE blir **teknisk insolvent** med negativ egenkapital på ca. 10,8 MNOK, hovedsakelig fordi konsernlånet fra morselskapet blir værende. Konsekvenser:

- **Styreansvar etter asl. § 17-1 og § 3-4/§ 3-5 (handleplikt ved tap av egenkapital)** blir reell personlig risiko [verifiseres mot Lovdata].
- **Omstøtelsesrisiko** forsterkes hvis en kreditor tar konkurs på fortsettende KWE i omstøtelsesvinduet — mest aktuelt TBRT (184 TNOK krav) eller Intrum (103 452 kr).
- **Konsernlånet er intern — morselskapet KodeWorks AS kan konvertere gjeld til egenkapital (ettergivelse eller tingsinnskudd av fordringen)** og dermed gjøre fortsettende KWE solvent. Dette må koordineres med fisjonen.

**Konkret anbefaling (ny vs. v1):** Morselskapet KodeWorks AS må parallelt med fisjonen enten (a) konvertere hele eller deler av konsernfordringen til egenkapital i fortsettende KWE, eller (b) ettergi den helt eller delvis. Minimumsmål: netto egenkapital i fortsettende KWE skal være positiv per fisjonsstikkdag, med realistisk likviditetsreserve til å dekke tvangsmulkt-krav + driftskostnader fram til DSB/Sivilombudet-saken er avgjort.

Dette er en vesentlig juridisk/skattemessig vurdering som må kjøres parallelt med fisjonsplanen. Agent 1 bør dekke dette i sin v2.

### 2.5 Åpne poster for brukeren å avklare

- **Konto 1396 Depositum (24k):** knyttet til kontorutleie Grønnegata eller noe annet? Antakelse: Grønnegata.
- **Konto 2900 Forskudd fra kunder (101k):** fra hvilke kunder? Antakelse: Grønnegata (korrelerer med konto 3690 Forskuddsfakturert leie).
- **Konto 1500 Kundefordringer (27k):** fra hvilke kunder? Fordeling FG30/Grønnegata/felles ikke avklart.
- **Konto 2400 Leverandørgjeld (488k):** faktura-for-faktura fordeling kreves fra regnskapsfører.
- **Konsernintern restrukturering:** kan KodeWorks AS konvertere eller ettergi deler av 10,6 MNOK-fordringen før/samtidig med fisjonen? Krever vurdering fra skatteadvokat.

---

## 3. Konkret uke-for-uke handlingsplan — oppdatert mot ny tidslinje

Antakelse: Beslutning fattes i løpet av uke 44 (slutt oktober 2026) etter at konkursvarsel-fristen er håndtert. Fisjonsstikkdag 01.01.2027 (årsskiftet er regnskapsvennlig). Mål: fisjonen rettslig gjennomført ca. midten av mars 2027.

### Uke 42 (12.–19.10.2026) — pågående

- Konkursvarsel forkynt 13.10.2026. **14-dagersfrist utløper 27.10.2026** — kritisk.
- Pågående utgående:
  - Anmodning til TBRT om Intrum-stans (sendt 07.10.2026, svarfrist 15.10.2026).
  - Bestridelse til Intrum (sendt 11.10.2026).
  - Namsfogden-anmodning (sendt 11.10.2026).
  - Sivilombud-klage.
  - DSB-søknad om frafall tvangsmulkt (sendt 12.10.2026).
- **Prosjektlederoppgaver:**
  - Oppfølging med TBRT 15.10.2026 på svarfristen.
  - Bestill fersk grunnbokutskrift Fjordgata 30 og Grønnegata 10 fra Kartverket (bekrefter at FG30 er pantefri og at Grønnegata har DNB-pant).
  - Bestill saldobalanse per 30.09.2026 fra regnskapsfører som utgangspunkt for åpningsbalanse-utkast.

### Uke 43 (20.–26.10.2026) — stabilisering + startarbeid

- Få svar/ikke-svar fra TBRT. Hvis TBRT instruerer Intrum: konkursvarselet faller bort som akutt risiko.
- Hvis TBRT ikke instruerer: valgsituasjon:
  - **(a) Betaling av 103 452 kr** (lovmessig trygg men bruker likviditet; kan omstøtes senere).
  - **(b) Rettslig stans via tingretten** (krever advokat; kan kjøpe tid men dyrt).
  - **(c) Nedbetalingsavtale med Intrum** (hvis Intrum vil forhandle etter bestridelsen).
  - **Prosjektlederanbefaling:** (a) hvis TBRT ikke instruerer og tiden er knapp. Beløpet er lite nok til at omstøtelsesrisikoen er håndterbar; bruker får samtidig åpnet veien for fisjon uten konkurs-trussel.
- Grunnbokutskrift mottatt → bekreft pantsituasjon.
- Saldobalanse 30.09.2026 mottatt → oppstart detaljert fordelingsarbeid.
- **Begynn utvelgelse av advokat og revisor.** Forespørsler til 2–3 kandidater hver.

### Uke 44 (27.10.–02.11.2026) — kritisk uke

- 27.10.2026: Konkursvarsel-fristen utløper. **Må være håndtert.**
- Engasjer selskapsadvokat (eiendomsfisjon + MVA-overføring) — kontraktssignering, retainer.
- Engasjer revisor (statsautorisert, med fisjon-kapasitet før jul).
- Første møte advokat–brukeren om:
  - Fisjonsstruktur (trippel-utfisjonering som i v1).
  - Aksjonæravtale FG30 AS (Brandsegg, Lagmannssveen).
  - Konsernlån-restrukturering (konvertering/ettergivelse fra KodeWorks AS).
  - Håndtering av påløpt tvangsmulkt i åpningsbalanse.

### Uke 45–47 (03.–23.11.2026) — utarbeidelse av fisjonsplan

- Advokat utarbeider fisjonsplan med vedlegg:
  - Åpningsbalanser for alle tre selskaper (basert på detaljert fordelingstabell).
  - Verdifastsettelser (bokført verdi — kontinuitet).
  - Fordelingsnøkkel.
  - Kreditorvarsel-utkast.
- Regnskapsfører gir utkast til saldobalanse per fisjonsstikkdag (foreløpig: ekstrapolert fra 30.09.2026).
- Revisor begynner gjennomgang parallelt (ikke vente til ferdig advokatutkast).
- **DNB-dialog:** be om skriftlig bekreftelse på overflytting av lån til Grønnegata 10 AS, med vilkår og timing. Enkeltbrev, trenger ingen forhandling.
- **Enova OM-samtykke:** utkast til samtykkebrev fra brukeren, med vedlegg om fisjonsstruktur og bekreftelse på at prosjektet videreføres uendret. Send tidlig i uke 45 — Enova må ha tid til å svare.

### Uke 48 (24.–30.11.2026) — forberedelse til vedtak

- Revisorerklæringer utarbeides parallelt (fisjonsplan + hver åpningsbalanse).
- Varselbrev til KMF, BYA, UNI, Enova KL — likelydende brev om pågående fisjon og transport av tilsagn til FG30 AS.
- Agent 1 (fisjonsjurist) bør ha avklart i v2: hvorvidt proaktiv varsling til TBRT skal skje nå eller senere.

### Uke 49 (01.–07.12.2026) — vedtak

- Revisorerklæringer ferdigstilles.
- Styrevedtak og generalforsamlingsvedtak i KWE (eneeier KodeWorks AS beslutter skriftlig).
- Melding om fisjonsbeslutning til Brreg; kreditorvarsel kunngjøres.

### Uke 50 (08.–14.12.2026) til uke 5 (26.01.–01.02.2027) — kreditorperiode

- **6-ukers kreditorfrist løper** (asl. § 14-7) [verifiseres mot Lovdata]. Jul-perioden gir reell forsinkelse — forvent at effektiv tilgjengelig behandlingstid i perioden er 4,5–5 uker.
- Prosjektleder følger opp kreditor-henvendelser løpende. Hvis TBRT reiser krav om sikkerhet (reell risiko gitt bero-slutt 01.01.2027): advokat utarbeider svar/sikkerhetstilbud.
- Dialog med DNB på overflytting av lån bekreftes skriftlig.
- Dialog med Enova OM følges opp — samtykke bør foreligge innen uke 4 (januar 2027).

### Uke 6–8 (02.–22.02.2027) — Samordnet registermelding og Brreg-behandling

- Når kreditorperioden utløper (ca. 25.–30.01.2027): Samordnet registermelding sendes til Brreg med endelig åpningsbalanse, revisorerklæring og nye vedtekter.
- Brreg behandlingstid 2–4 uker. Flaskehals.

### Uke 9–11 (23.02.–15.03.2027) — gjennomføring

- Brreg registrerer fisjonen; tildeler org.nr. til FG30 AS og Grønnegata 10 AS.
- Hjemmelsoverføring til Kartverket (skjøter × 2).
- MVA-registrering FG30 AS (ordinær § 2-1 + frivillig § 2-3) og Grønnegata 10 AS (frivillig § 2-3).
- Byggesak-overføring (ny tiltakshaver FG30 AS).
- Underretning til Riksantikvar.
- Transport av tilskudd til FG30 AS (KMF, BYA, UNI, Enova KL, Enova OM).

### Uke 12–14 (16.03.–05.04.2027) — etterarbeid

- **Emisjon av nye aksjer i FG30 AS mot tingsinnskudd fra Brandsegg og Lagmannssveen.** Tidsmessig avstand fra fisjonsgjennomføring: minst 2–4 uker, for å unngå at Skatteetaten anser fisjon + emisjon som én sammenhengende transaksjon med brudd på kontinuitet. Praktisk minimum: 3 uker etter Brreg-registrering.
  - Aksjonæravtale signeres av alle parter.
  - Styrevedtak og generalforsamlingsvedtak om kapitalforhøyelse i FG30 AS.
  - Revisorerklæring (asl. § 2-6) [verifiseres mot Lovdata] om tingsinnskuddets verdi.
  - Melding til Brreg om kapitalforhøyelse.
- Nye vedtekter FG30 AS registreres.

**Realistisk sluttdato: ca. 15. mars 2027 for fisjonsgjennomføring; emisjon ca. 1.–15. april 2027.**

---

## 4. Oppdatert kostnadsestimat

Diff vs. v1:
- Bankforhandlings-posten reduseres fra 5–40 TNOK til 2–5 TNOK (bare bekreftelsesbrev og revidert lånedokument).
- BFU-advokattid utgår (0 TNOK) — fase 1 inkluderte ikke en egen BFU-post, men MVA-rådgivning kan reduseres noe fordi strategien er bekreftet.
- Ny post: emisjonsdokumentasjon og aksjonæravtale (30–60 TNOK).
- Ny post: tingsinnskudd-revisorerklæring (10–25 TNOK, kan dekkes av fisjonsrevisor).
- Potensielt ny post: konsernlån-restrukturering (skatteadvokat 10–30 TNOK).

| Post | Lavt | Sannsynlig | Høyt | Kommentar |
|---|---:|---:|---:|---|
| Selskapsadvokat — fisjonsplan, protokoller, Brreg-dialog, justeringsavtaler (hvis aktuelt) | 80 000 | 150 000 | 250 000 | Som i v1. Scope er fortsatt stort (to overtakende, konsernlån-restrukturering parallelt) |
| Advokat eiendomsoverføring — skjøter, pantebok, Kartverk | 15 000 | 25 000 | 40 000 | To eiendommer |
| Revisor — fisjonsplan, åpningsbalanser | 40 000 | 70 000 | 120 000 | Som i v1 |
| **Revisor — tingsinnskudd-erklæring (emisjon)** | **10 000** | **18 000** | **25 000** | Ny post. Kan samkjøres med fisjonsrevisor for rabatt |
| MVA-spesialist | 10 000 | 20 000 | 40 000 | Redusert fra v1 (strategi bekreftet, men tidsrekkefølgen må kvalitetssikres) |
| **Skatteadvokat — konsernlån-restrukturering** | **10 000** | **20 000** | **40 000** | Ny post. Kan dekkes av selskapsadvokat med skattekompetanse |
| Regnskapsfører — ekstra arbeid | 20 000 | 40 000 | 70 000 | Som i v1 |
| **Advokat emisjon + aksjonæravtale** | **30 000** | **45 000** | **60 000** | Ny post. Standardarbeid for selskapsadvokat; kan rabatteres hvis samme firma |
| Brreg — melding fisjonsbeslutning | 0 | 0 | 0 | Gratis |
| Brreg — gjennomføring + nystiftelser | 5 000 | 7 000 | 10 000 | Som i v1 |
| Brreg — kapitalforhøyelse FG30 AS (emisjon) | 0 | 2 500 | 3 000 | Ny post |
| Kunngjøringsgebyr Brreg | 1 000 | 1 500 | 2 000 | Som i v1 |
| Tinglysingsgebyr skjøter × 2 | 1 300 | 1 300 | 1 300 | Som i v1 |
| Dokumentavgift | 0 | 0 | 0 | Fritak ved kontinuitet |
| **DNB — bekreftelsesbrev + revidert lånedokument** | **2 000** | **5 000** | **10 000** | Redusert fra v1-estimatet 5–40 TNOK |
| Oversettelse/diverse | 2 000 | 5 000 | 10 000 | Som i v1 |
| **Sum** | **~226 000** | **~410 000** | **~681 000** | |

**Sentralt kostnadsintervall: 350 000–470 000 kr.** Noe høyere enn v1 pga. ny emisjon og tingsinnskudd. Dette må fortsatt vektes mot MVA-fordelen (ca. 5–6 MNOK refusjon i byggefasen).

**Risikofaktorer uendret fra v1:** dokumentavgift-risiko ved feil kontinuitetspåføring (750 TNOK+), kreditor-krav om sikkerhet i kreditorperioden, Brreg-tilleggsrunder.

**Ny risiko:** konsernlån-restrukturering (konvertering/ettergivelse) kan utløse skattekonsekvenser i KodeWorks AS (gevinst/tap på fordring). Agent 1 må vurdere i v2.

---

## 5. Oppdatert dokumentliste

Diff vs. v1: fem nye dokumenter knyttet til emisjonen og aksjonæravtalen; ett nytt dokument knyttet til DNB-bekreftelse; eventuelt dokument for konsernlån-restrukturering.

| Dokument | Hvem utarbeider | Hvem signerer | Når |
|---|---|---|---|
| Fisjonsplan med vedlegg | Advokat | Styret | Uke 47 |
| Åpningsbalanser for FG30 AS, Grønnegata 10 AS, fortsettende KWE | Regnskapsfører → advokat → revisor | Styret (vedlegg) | Uke 47 |
| Verdifastsettelser av eiendeler | Styret med regnskapsfører | Styret | Uke 46 |
| Revisorerklæring til fisjonsplanen (asl. § 14-4) [verifiseres mot Lovdata] | Revisor | Revisor | Uke 48 |
| Revisorerklæring til hver åpningsbalanse | Revisor | Revisor | Uke 48 |
| Styreprotokoll med innstilling | Advokat (mal), styret | Styret | Uke 49 |
| Generalforsamlingsprotokoll KWE | Advokat (mal) | Møteleder, protokollfører | Uke 49 |
| Generalforsamlingsprotokoll KodeWorks AS (eneeier beslutter) | Advokat (mal) | Eneeier | Uke 49 |
| Stiftelsesdokument FG30 AS | Advokat | Stifter (KodeWorks AS) | Uke 49 |
| Stiftelsesdokument Grønnegata 10 AS | Advokat | Stifter | Uke 49 |
| **Vedtekter FG30 AS** (nye, med formål for lagring + utleie) | Advokat | Stifter | Uke 49 |
| **Vedtekter Grønnegata 10 AS** (nye, med formål for utleie kontor) | Advokat | Stifter | Uke 49 |
| **Dokument om konsernlån-restrukturering** (konvertering til EK eller ettergivelse) | Skatteadvokat/selskapsadvokat | Styret i KWE og KodeWorks AS | Uke 48 |
| Melding om fisjonsbeslutning til Brreg | Advokat | Signert elektronisk | Uke 49 |
| Kreditorvarsel-utkast (publiseres av Brreg) | Advokat | — | Uke 49 |
| Samordnet registermelding — fisjon + nystiftelser | Advokat | Signert elektronisk | Uke 6 (02.2027) |
| Skjøte Fjordgata 30 | Advokat | Styret KWE → FG30 AS | Uke 10 (03.2027) |
| Skjøte Grønnegata 10 | Advokat | Styret KWE → Grønnegata 10 AS | Uke 10 (03.2027) |
| MVA-registreringsmelding FG30 AS | Regnskapsfører/advokat | Daglig leder | Uke 10 |
| MVA-registreringsmelding Grønnegata 10 AS | Regnskapsfører/advokat | Daglig leder | Uke 10 |
| Underretningsbrev tilskuddsgivere (KMF, BYA, UNI, Enova KL, Enova OM, TBRT, byggesak, Riksantikvar) | Prosjektleder (bistand advokat) | Daglig leder | Uke 11 |
| Oppdatering byggesak (ny tiltakshaver) | Advokat/prosjektleder | Daglig leder | Uke 11 |
| **DNB-bekreftelsesbrev** (hjemmelsoverføring + debitorbytte Grønnegata) | DNB | DNB | Uke 46 (bestilles tidlig) |
| **Enova OM-samtykkebrev** | Enova | Enova | Uke 48 (bestilles i uke 45) |
| **Aksjonæravtale FG30 AS** (Brandsegg, Lagmannssveen, KodeWorks AS) | Advokat | Alle aksjonærer | Uke 12 (03.2027) |
| **Kapitalforhøyelses-protokoll FG30 AS** (styrets forslag + GF-vedtak) | Advokat | Styret og GF | Uke 12 |
| **Revisorerklæring tingsinnskudd (asl. § 2-6)** [verifiseres mot Lovdata] | Revisor | Revisor | Uke 12 |
| **Verdifastsettelse av tingsinnskudd** (dokumentert gjennom styrebeslutning) | Styret FG30 AS med advokat | Styret | Uke 12 |
| **Nye vedtekter FG30 AS etter emisjon** | Advokat | Styret | Uke 13 |
| **Melding Brreg om kapitalforhøyelse** | Advokat | Daglig leder | Uke 13 |

---

## 6. Endringer fra v1

Explicit diff mellom v1 og v2:

### Fjernet eller redusert

- **Bank-forhandling som åpent spørsmål** (v1 seksjon 5.4): DNB har bekreftet overflytting. Reduseres til bekreftelsesbrev.
- **BFU-vurdering** (v1 seksjon 5.5): Fjernet. MVA-strategi bekreftet via veiledende svar.
- **Pantesituasjon som usikkerhet for FG30** (v1 seksjon 5.4 og flere steder): FG30 går uten pant. Oppdatert fordeling.
- **Antakelsen om 3–6 måneders BFU-ventetid** (v1 seksjon 2 og 5.5): Utgår. Tidslinjen kan presses tilsvarende.

### Lagt til

- **Emisjon som eget trinn etter fisjon** (seksjon 3 uke 12–14 i v2). Brandsegg og Lagmannssveen kommer inn via emisjon mot tingsinnskudd, ikke som del av fisjonen. Begrunnelse: skattemessig kontinuitet (sktl. kap. 11) [verifiseres mot Lovdata] krever eneeier-identitet i fisjonen.
- **Konsernlån-restrukturering parallelt med fisjon** (seksjon 2.4): Nødvendig for å gjøre fortsettende KWE solvent. KodeWorks AS må konvertere eller ettergi deler av 10,6 MNOK-fordringen.
- **Konkret fordelingstabell basert på faktiske regnskapstall** (seksjon 2.2): Erstatter v1-tabellens placeholder-logikk.
- **Preliminær egenkapital-beregning per selskap** (seksjon 2.3): Konkrete tall.
- **Oppdatert dokumentliste med 7 nye dokumenter** (seksjon 5).
- **Oppdatert kostnadsestimat med 4 nye poster** (seksjon 4).

### Oppdatert

- **Tidslinje** (seksjon 3): Komprimert med 1–2 måneder grunnet bortfall av BFU-ventetid. Sluttdato ca. 15.03.2027 (fisjon) + 15.04.2027 (emisjon).
- **Aktørliste** (seksjon 1): DNB endrer rolle; nye roller for emisjonsadvokat og tingsinnskudd-revisor.
- **MVA-strategi i åpningsbalanse-logikken** (seksjon 2): KWE blir **ikke** MVA-registrert før fisjon, så ingen justeringsavtale er nødvendig. FG30 AS registreres etter fisjon.

### Fortsatt uavklart (overlappende med v1)

- Dokumentavgift-risikoen: krever advokatens kvalitetssikring.
- Fordeling av tvangsmulkt-gjeld: valgt Alt 1A, men krever Agent 1-/Agent 3-bekreftelse i v2.
- Omstøtelsesrisikoen i konkurs-scenario: fortsatt gjeldende; forsterket av konsernlån-plasseringen.

---

## 7. Åpne spørsmål

1. **Konsernlån-restrukturering:** Må KodeWorks AS konvertere hele 10,6 MNOK til EK, eller delvis ettergi? Hvilken skattekonsekvens får dette i KodeWorks AS (gevinst/tap på fordring, mulig fradrag etter sktl. § 6-2)? Agent 1 må dekke.
2. **Tingsinnskuddets innhold:** Hva skal Brandsegg og Lagmannssveen faktisk tilføre som tingsinnskudd? Kontanter, utstyr, immaterielle verdier, framtidig arbeidsplikt? Må klargjøres av brukeren før aksjonæravtale kan utkastes. Arbeidsplikt kan ikke være tingsinnskudd (asl. § 2-6 krever at innskudd er noe som eiendeleselskapet skal få eiendomsrett i; arbeidsplikt oppstår først senere) [verifiseres mot Lovdata].
3. **Fordeling av fordringer og leverandørgjeld:** Faktura-for-faktura gjennomgang kreves fra regnskapsfører for å få eksakt fordeling av konto 1500, 2400 og 2900.
4. **Fisjonsstikkdag:** 01.01.2027 anbefalt. Hvis beslutning drar ut i tid og vedtak først fattes i januar 2027, må stikkdagen flyttes til 01.02.2027 eller lignende — eller tilbake-dateres med skriftlig støtte fra revisor.
5. **Proaktiv TBRT-varsling:** Følger bruker-input Q2 (evalueres senere), men Agent 1 bør gi en skarp vurdering i v2 om når senest varslingen bør gjøres.
6. **Depositum, forskudd og pinball:** Antakelser i fordelingstabellen (seksjon 2.2) må verifiseres av brukeren.
7. **Likviditetsplanlegging:** Fortsettende KWE trenger likviditet nok til å dekke tvangsmulkt-krav + driftskostnader fram til DSB-/Sivilombud-saken avgjøres (potensielt mars–juni 2027). Hvor mye bankinnskudd må være i fortsettende KWE per fisjonsstikkdag? Grovt estimat: minst 300–500 TNOK, pluss likvide konsernlån-restfordringer.
8. **Enova OM-samtykketidspunkt:** Hvor lang behandlingstid må forventes? Hvis Enova trenger 6–8 uker, må forespørsel sendes i uke 45 for å ha svar innen GF-vedtak uke 49.
9. **Hvis TBRT reiser krav om sikkerhet i kreditorperioden:** Prosjektleder trenger en forhåndsvurdert plan. Bankgaranti? Depot? Sikkerhet i pinball-maskin? (Spøk — men poenget er at fortsettende KWE har lite å stille som sikkerhet uten konsernlån-restrukturering.)

---

## 8. Interaksjoner med andre agenter

### Agent 1 (Fisjonsjurist v2)

Prosjektleder trenger spesifikke avklaringer:

- **Konsernlån-restrukturering:** Hvilken juridisk form (konvertering vs. ettergivelse) er mest effektiv, og hvilke skatte-/avgiftskonsekvenser utløser hver variant? Særlig: er konvertering (gjeld → EK) nøytral etter sktl. kap. 11 hvis gjennomført som del av fisjonsprosessen, eller må den gjøres separat?
- **Tingsinnskudd ved emisjon:** Hvilke former er lovlige (asl. § 2-6 og § 2-7) [verifiseres mot Lovdata]? Er framtidig arbeidsplikt definitivt utelukket, eller finnes alternative strukturer (f.eks. opsjonsavtale, incentivordning)?
- **Avstand mellom fisjon og emisjon:** Hva er juridisk forsvarlig minsteavstand for at Skatteetaten ikke anser fisjon + emisjon som én transaksjon med brudd på kontinuitet (sktl. kap. 11)?
- **Fortsettende KWEs insolvensrisiko:** Vurder styreansvarsrisikoen (asl. § 17-1 + handleplikt § 3-4/§ 3-5) hvis konsernlån-restrukturering **ikke** gjennomføres parallelt. Konkret: er det styreansvar fra fisjonsvedtakstidspunktet, eller først etter at fisjonen er registrert?
- **Omstøtelsesrisikoen:** Konkret vurdering av om foreslått fordeling (seksjon 2.2) tåler et omstøtelseskrav fra TBRT, Intrum eller framtidig bostyrer. Særlig: er påløpt tvangsmulkt på 184 TNOK i fortsettende KWE tilstrekkelig dekning, eller må mer verdier beholdes?

### Agent 3 (Tvangsmulkt-strateg v2)

- **Alt 1A bekreftelse:** Agent 3 bør bekrefte at påløpt tvangsmulkt (184 000) plasseres i fortsettende KWE er riktig for å beskytte partsstatus i DSB-/Sivilombud-sakene. Hvis Alt 1A forblir anbefalt: er det tilstrekkelig dekning i fortsettende KWE etter konsernlån-restrukturering?
- **Framtidig tvangsmulkt (fra 01.01.2027 hvis bero oppheves):** Hvor plasseres denne? Hvis fisjonen er registrert innen 15.03.2027, påløper mulkten i fortsettende KWE fra 01.01. til 15.03. (ca. 143 TNOK ved 2 TNOK/dag), deretter i FG30 AS. Agent 3 bør vurdere om dette skjæringspunktet trenger spesiell håndtering.
- **Varselbrev-timing:** Agent 3 bør gi konkret anbefaling om når varselbrev til TBRT skal sendes — før eller etter GF-vedtak, før eller etter kreditorvarsel i Brreg.

### Agent 4 (Finans- og tilskuddsanalyst v2)

- **Verifisere fordelingstabellen (seksjon 2.2):** Agent 4 har tilgang til regnskaps- og tilskuddsdata og bør kryssjekke om fordelingen av bankinnskudd, kundefordringer, leverandørgjeld, forskudd og depositum er realistisk.
- **Enova OM-samtykkeprosess:** Prosjektleder trenger Agent 4s vurdering av Enova OMs faktiske behandlingstid på endringssøknader (precedens-saker, kontaktpersoner).
- **Transportinstruksjon per tilskuddsgiver:** For hver av KMF, BYA, UNI, Enova KL, Enova OM: hvilken form må transport-instruksjonen ha? Standard brev eller spesifikt skjema?
- **Likviditetsframskrivning:** Hvor mye bankinnskudd trenger fortsettende KWE for å overleve 6–12 måneder uten eksterne tilførsler, gitt at ingen store inntekter forventes?
- **Nye aksjonærers tingsinnskudd:** Finansiell vurdering av verdien på det Brandsegg og Lagmannssveen tilfører — hvis det er immaterielle verdier (kompetanse, nettverk), hvordan dokumenteres de for revisorerklæringen?

---

## Oppsummering

v2-planen er betydelig mer konkret enn v1 fordi faktiske regnskapstall og bank-/MVA-avklaringer er på plass. Hovedrisikoer er flyttet fra «ekstern usikkerhet» (bank, MVA-strategi) til «intern struktur»: konsernlån-restrukturering og tingsinnskudd-emisjon må begge gjennomføres korrekt for at helheten skal fungere. Fortsettende KWE blir teknisk insolvent uten konsernlån-restrukturering — dette er den største nye problemstillingen vs. v1.

Tidslinjen presses til gjennomføring ca. midten av mars 2027; emisjon ca. 2–4 uker etterpå. Totalkostnad: 350–470 TNOK (medianestimat 410 TNOK), opp fra 345 TNOK i v1 pga. ny emisjon og tingsinnskudd-dokumentasjon.

*Dokumentet er fase 4-leveranse. Alle lovreferanser som ikke eksplisitt er merket verifisert mot Lovdata, må kontrolleres i verifikasjonsfasen før de brukes i leveranser til eksterne parter.*
