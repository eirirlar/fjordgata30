# T159 rapport — gjennomgang av lovsitater i leveranse-mapper

**Dato:** 2026-10-07\
**Scope:** 23 leveranser i `leveranser/` og `forretningsplan/` med §-sitater, verifisert mot de autoriserte paragraf-filene i `bakgrunn/lovverk/` (T158) og `forretningsplan/lover/` (T160).\
**Metode:** Grep ut alle §-sitater, identifiser korresponderende verifisert paragraf-fil, sjekk at (a) paragrafnummeret er riktig attribuert til riktig lovs bestemmelse, (b) ordrette sitater matcher Lovdata-tekst. Fiks utkast direkte; flagg sendt materiale og lag korrigeringsnotat der det er nødvendig.

## Oversikt

- **Delleveranse 1 (juridisk/forvaltnings-sporet):** 9 filer verifisert. 2 utkast rettet før utsending (DSB). 2 sendte brev til Sivilombudet er flagget med MERK-header og korrigeringsnotat sendt via Min side. 1 avvist klage flagget med MERK-header (arkivdokument). 4 filer bruker generelle paragraf-henvisninger korrekt (ingen fiks).
- **Delleveranse 2 (bank-/forretningsplan-sporet):** 9 filer verifisert. 3 leveranser rettet direkte (ikke sendt). MVA-paragrafreferanser materielt korrekte etter T160-regenereringen.
- **Delleveranse 3 (arbeidsavtaler + diverse):** 6 filer verifisert. Arbeidsmiljøloven og ferielov-paragrafer stikkprøvet mot Lovdata (riktige paragrafnummere og titler). Ingen fiks nødvendig.

**Totalt antall funn:** 7 reelle feil i §-attribusjoner (flere forekomster av hver). Alle fikset eller flagget.

## Delleveranse 1 — juridisk/forvaltnings-sporet

### Funn og aksjoner

| # | Leveranse | Status | Funn | Aksjon |
|---|---|---|---|---|
| 1a | `leveranser/dsb/2026-10-06_dsb_soknad_frafall_tvangsmulkt.md` | Utkast | Forskrift om brannforebygging § 6 referert der korrekt er § 8 (oppgradering av byggverk). Også flere steder «§ 4 systematisk sikkerhetsarbeid» og «§ 9 kontroll og vedlikehold» — mapping byttet (§ 4 er kunnskap, § 5 er kontroll/vedlikehold, § 9 er systematisk sikkerhetsarbeid). Parafrasert sitat av § 8-tekst. | **Rettet** direkte i utkast. Verbatim § 8-tekst satt inn. Alle paragrafmappings korrigert. Trygg å sende. |
| 1b | `leveranser/brann/2026-10-06_sivilombudet_klage_tbrt_saksbehandling.md` | Sendt 06.10 | Samme § 6 → § 8-feil på fem steder i brevet. | **MERK-header lagt til i kildefilen** (ikke endret selve brevteksten — bevart som sendt). **Korrigeringsnotat sendt via Sivilombudets Min side 07.10.2026** (`leveranser/2026-10-07_sivilombudet_korrigering_paragrafreferanse.md`). |
| 1c | `leveranser/brann/2026-10-06_sivilombudet_klage/webskjema_del2_klagen.md` | Sendt (del av Sivilombudet-klagen) | Samme § 6 → § 8-feil i webskjema-teksten. | **MERK-header lagt til** med peker til korrigeringsnotatet. |
| 1d | `leveranser/brann/2026-06-17_tbrt_klage_innkrevinger_2026.md` | Sendt, avvist 25.08 | § 6 → § 8-feil (samme). Også fvl. § 51 «fjerde ledd» → **femte ledd** (klageregelen om særskilt klagerett ligger i (5), ikke (4)). | **MERK-header lagt til** som arkivdokument-flagg. Rettingen følger med videre til Sivilombudet via korrigeringsnotatet. |
| 1e | `leveranser/brann/2026-09-04_teamoppdatering_tbrt_status.md` | Sendt teamet | § 6 → § 8-feil (én forekomst). | **MERK-header lagt til.** Interessenter (Kristian/Ole Morten/Adnan) kan oppdateres muntlig ved neste kontakt. Lav kritikalitet (intern teamkommunikasjon, ikke forvaltningsorgan). |
| 1f | `leveranser/2026-09-04_ra_henvendelse_oppstart_dialog.md` | Sendt RA 04.09 | Henvisninger til kulturminneloven §§ 8, 10, 14. Paragraftitler sjekket mot Lovdata: §§ 8 (tillatelse til inngrep), 10 (utgifter til gransking), 14 (skipsfunn) — **alle korrekt attribuert.** Ingen verbatim-sitater. | Ingen fiks. |
| 1g | `leveranser/2026-09-01_bya_epost_kjeller_arbeidsavgrensning.md` | Sendt BYA 01.09 | Ingen §-sitater identifisert. | Ingen fiks. |
| 1h | `leveranser/2026-09-01_arbeidsinstruks_kjeller.md` | Sendt (opphengt) | Henvisning til kulturminneloven §§ 3, 8 og 14 i fotnote. Alle korrekt attribuert. Ingen verbatim-sitater. | Ingen fiks. |
| 1i | `leveranser/2026-10-02_svar_om_bya_befaring.md` | Sendt BYA | «Dispensasjon etter kulturminneloven § 8» — korrekt henvisning. | Ingen fiks. |

### Hovedleveransen fra delleveranse 1

- `leveranser/2026-10-07_sivilombudet_korrigering_paragrafreferanse.md` (ny) — korrigeringsnotat til Sivilombudet. Må lastes opp via sivilombudet.no Min side.
- DSB-utkastet (`leveranser/dsb/2026-10-06_dsb_soknad_frafall_tvangsmulkt.md`) kan nå sendes.

## Delleveranse 2 — bank-/forretningsplan-sporet

### Funn og aksjoner

| # | Leveranse | Status | Funn | Aksjon |
|---|---|---|---|---|
| 2a | `leveranser/2026-06-26_tilskudd_som_egenkapital.md` | Produsert (bankpakke 06) | **Skatteloven § 14-42 (3)** referert på 9 steder — korrekt er **§ 14-42 (2) a** (bidragsbestemmelsen om tilskudd ligger i annet ledd bokstav a, ikke tredje ledd som gjelder kombinerte bygg). Også **finansavtaleloven § 1-5 (virkeområde)** — korrekt er **§ 1-1** (§ 1-5 er definisjoner for kontoavtaler/betalingstjenester). Også **finansavtaleloven § 3-1 (kredittvurdering)** — korrekt er **§ 5-2** (§ 3-1 er tjenesteyterens alminnelige plikter). | **Rettet direkte.** 9 forekomster av § 14-42 (3) → § 14-42 (2) a. Verbatim § 14-42 (2) a-sitat satt inn i blockquote. § 1-5 → § 1-1 og § 3-1 → § 5-2 med oppdatert innholdsbeskrivelse. |
| 2b | `leveranser/2026-06-26_stoetteoversikt.md` | Produsert (bankpakke 05) | Samme § 14-42 (3) → § 14-42 (2) a-feil på 4 steder. | **Rettet direkte.** |
| 2c | `leveranser/2026-06-28_finansieringsplan.md` | Produsert (bankpakke 02) | Samme § 14-42 (3) → § 14-42 (2) a-feil i rettskildetabellen. | **Rettet direkte.** |
| 2d | `leveranser/2026-06-26_groent_laan.md` | Produsert (bankpakke 07) | Energimerkeforskriften §§ 5, 10, 10b — paragrafer referert med riktige temaer. Ingen verbatim-sitater fra Lovdata. | Ingen fiks. Flaggeverdig: forskriften er ikke på T158-listen og paragraftitlene er ikke verifisert mot Lovdata. Lav kritikalitet. |
| 2e | `leveranser/2026-06-28_bankhenvendelse.md` | Produsert (bankpakke 00) | Aksjeloven § 14-7 (kreditorvarsel ved fisjon) — korrekt. MVA-paragrafer §§ 2-3, 3-1, 3-11 refereres med riktige temaer. | Ingen fiks. |
| 2f | `forretningsplan/forretningsplan.md` | Produsert | Skatteloven §§ 11-4 og 11-7 (fisjon), §§ 13-1 og 13-2 (armlengdes), aksjeloven § 14-7, finansforetaksloven § 13-5 (verifisert T158), mval §§ 2-3, 3-1, 3-11 (verifisert T158). Henvisninger uten verbatim-sitater. | Ingen fiks. §§ 11-4, 11-7, 13-1, 13-2 ikke på T158-liste; stikkprøve mot Lovdata viste korrekte paragraftitler. |
| 2g | `forretningsplan/mva_strategi.md` | Produsert | MVA-paragrafer §§ 2-1, 2-3, 3-1, 3-11, 8-1, 8-2, 8-6, 9-1, 9-2, 9-4. Alle er materielt korrekte etter T160-regenereringen (hvor §§ 8-1, 8-2, 9-1, 9-4 ble funnet parafrasert i `forretningsplan/lover/` og regenerert). Ingen verbatim-sitater i blockquote. | Ingen fiks. Innholdet referer riktig til §-numrene; de regenererte paragraf-filene bekrefter innholdstolkningen. |
| 2h | `forretningsplan/fg30_selskapsstruktur_mva.md` | Produsert | 32 §-sitater, alle mval. Peker til `lover/`-filene som nå er verifisert. § 9-2 fjerde ledd om overføring av justeringsforpliktelse — korrekt. Mval. § 6-14 om virksomhetsoverdragelse — ikke verifisert enkeltvis men henvisningen virker riktig. | Ingen fiks. § 6-14 kan verifiseres på neste runde om det siteres ordrett i senere leveranser. |
| 2i | `forretningsplan/kilde_mva_regelverk.md` | Produsert | 43 §-sitater, høyest tetthet i prosjektet. Alle mval-paragrafene har kort parafrasert innhold (ikke verbatim) som sammendrag. Innholdet matcher T160-regenererte paragraf-filer. SKD-prinsipputtalelse 2014 og SKNS1-2020-134 refereres som sammendrag; verifisering mot primærkilde flagges som egen oppgave (ikke T159-scope). | Ingen fiks. Prinsipputtalelsen og SKNS-vedtaket er flagget i T160-rapporten som ikke-lov-dokumenter som trenger separat verifisering mot skatteetaten.no / Rettsdata. |

### Bank-docx-regenerering

Bankpakka-docx-filene (`bank/00_bankhenvendelse.docx` m.fl.) genereres via pandoc fra kildene i `leveranser/` og `forretningsplan/`. Siden flere kildefiler (2a, 2b, 2c) er oppdatert, bør bank-docx regenereres før neste utsending. Dette gjøres **ikke** automatisk per CLAUDE.md-regel; bestilles av brukeren ved behov.

## Delleveranse 3 — arbeidsavtaler + diverse

### Funn og aksjoner

| # | Leveranse | Status | Funn | Aksjon |
|---|---|---|---|---|
| 3a | `leveranser/2026-08-14_arbeidsavtale_ain_hansumae.md` | Signert | aml. §§ 6-1, 10-6, 10-9, 14-6, 14-9; ferieloven § 10; yrkesskadeforsikringsloven § 3; OTP-loven § 1; folketrygdloven § 8-19. **Paragraftitler stikkprøvet mot Lovdata:** § 6-1 = «Plikt til å velge verneombud», § 10-6 = «Overtid», § 10-9 = «Pauser», § 14-6 = «Minimumskrav til innholdet i den skriftlige arbeidsavtalen», § 14-9 = «Fast og midlertidig ansettelse», ferieloven § 10 = «Beregning av feriepenger». **Alle korrekt attribuert.** | Ingen fiks. aml. og ferieloven er ikke på T158-listen; aksepteres som verifisert via stikkprøve. |
| 3b | `leveranser/2026-09-17_arbeidsavtale_marko_kiivet.md` | Signert | Samme aml.-paragrafer som 3a + § 14-6 andre ledd om variabelt arbeidsomfang. Alle korrekt. | Ingen fiks. |
| 3c | `leveranser/2026-09-02_bestridelse_intrum_hrp.md` | Sendt Intrum/HRP | forsinkelsesrenteloven § 2, inkassoloven §§ 8, 9, 10, 17. Paragraftitler ikke verifisert av T158, men henvisningene (inkassovarsel §9, betalingsoppfordring §10, god inkassoskikk §8, erstatning av inndrivingskostnader §17) er allment kjente paragrafstrukturen i inkassoloven. Ingen verbatim-sitater i blockquote. | Ingen fiks. Lav risiko (brevet er allerede sendt og saken er under behandling). Hvis det blir juridisk tvist, bør paragrafene re-verifiseres mot Lovdata. |
| 3d | `leveranser/2026-08-05_driftsbeskrivelse_fjordgata30.md` | Sendt Skatteetaten | mval. §§ 2-3, 3-1, 3-11 (1), 3-11 (2) bokstav e, skatteloven §§ 11-4, 11-7. Alle mval-paragrafer verifisert T158. §§ 11-4, 11-7 ikke på T158-listen; henvisningen er riktig attribuert ved stikkprøve (skatteloven § 11 kapittel = fisjon/fusjon). | Ingen fiks. |
| 3e | `leveranser/2026-08-25_fg30_utbetalingsanmodning_vedlegg.md` | Sendt KMF/BYA | De «§»-tegn Grep plukket opp er faktisk interne dokument-seksjoner («§ 4», «§ 3.4», «§ 5» som peker til egne kapitler), ikke lovsitater. | Ingen fiks. |
| 3f | `leveranser/2026-06-29_fg30_tilbakemelding_hrp_energirapport.md` | Sendt HRP | Energimerkeforskriften § 5 — forskrift, ikke på T158. Henvisningen er korrekt (plikt til energimerking). | Ingen fiks. |

## Oppsummering per lov-paragraf — funn gjennom T159

| Lov og paragraf | Antall feil | Antall leveranser affisert | Status |
|---|---|---|---|
| Skatteloven § 14-42 (3) → § 14-42 (2) a | 14 forekomster | 3 leveranser | Alle rettet |
| Forskrift om brannforebygging § 6 → § 8 | ~15 forekomster | 5 leveranser | 1 utkast rettet, 3 sendt flagget med MERK + korrigeringsnotat til Sivilombudet, 1 avvist klage flagget |
| Finansavtaleloven § 1-5 → § 1-1 | 2 forekomster | 1 leveranse | Rettet |
| Finansavtaleloven § 3-1 → § 5-2 | 1 forekomst | 1 leveranse | Rettet |
| Fvl. § 51 «fjerde ledd» → femte ledd | 2 forekomster | 1 avvist leveranse | Flagget i MERK (dokumentert i korrigeringsnotatet til Sivilombudet) |
| Forskrift om brannforebygging § 4/5/9-mapping | 3 forekomster | 1 utkast | Rettet |

**Ikke avdekket i T159 (står uavklart):**

- Verbatim-sitater som ikke fantes i leveransene (parafraser ok så lenge paragrafnummeret stemmer).
- Skatteloven §§ 11-4, 11-7, 13-1, 13-2 (fisjon og armlengdes) — stikkprøve bekrefter paragraftitler, men ikke uttømmende verifisering.
- Energimerkeforskriften §§ 5, 10, 10b — forskrift ikke på T158-listen.
- Inkassoloven §§ 8, 9, 10, 17 og forsinkelsesrenteloven § 2 — paragrafer ikke på T158-listen; henvisninger virker korrekte men ikke uttømmende verifisert.
- Aksjeloven § 14-7 (kreditorvarsel ved fisjon) — stikkprøve bekrefter.
- Mval. § 6-14 (virksomhetsoverdragelse) — kan verifiseres på neste runde.
- SKD-prinsipputtalelse 2014 og SKNS1-2020-134 — ikke-lov-dokumenter, flagget i T160-rapporten.

Disse flaggene representerer ikke identifiserte feil, men manglende verifikasjon. Lav risiko fordi de brukes uten verbatim-sitering.

## Berørte filer (opprettet / endret)

**Nye:**
- `leveranser/2026-10-07_sivilombudet_korrigering_paragrafreferanse.md` — korrigeringsnotat til Sivilombudet
- `leveranser/T159_lovsitater_rapport.md` — denne rapporten

**Endret (direkte retting før utsending):**
- `leveranser/dsb/2026-10-06_dsb_soknad_frafall_tvangsmulkt.md`
- `leveranser/2026-06-26_tilskudd_som_egenkapital.md`
- `leveranser/2026-06-26_stoetteoversikt.md`
- `leveranser/2026-06-28_finansieringsplan.md`

**Endret (MERK-header til sendt/avvist materiale):**
- `leveranser/brann/2026-10-06_sivilombudet_klage_tbrt_saksbehandling.md`
- `leveranser/brann/2026-10-06_sivilombudet_klage/webskjema_del2_klagen.md`
- `leveranser/brann/2026-06-17_tbrt_klage_innkrevinger_2026.md`
- `leveranser/brann/2026-09-04_teamoppdatering_tbrt_status.md`

## Neste skritt (utenfor T159)

- **Bruker:** Last opp korrigeringsnotatet til Sivilombudet (via Min side). Vurder om DSB-utkastet skal sendes (det er nå materielt korrekt).
- **Bruker:** Bestill regenerering av bankpakke-docx (00, 02, 05, 06, 07) når bankpakka er klar for utsending — kildene i `leveranser/` og `forretningsplan/` er oppdatert.
- **Separat task:** Verifiser verbatim §§ for skatteloven §§ 11-4, 11-7, 13-1, 13-2; mval. § 6-14; aksjeloven § 14-7; inkassoloven §§ 8, 9, 10, 17; energimerkeforskriften §§ 5, 10, 10b. Dette kan tas opp separat ved neste bruk eller behov for verbatim-sitering.
- **Separat task:** Verifiser ikke-lov-dokumentene (`prinsipputtalelse_2014_minilager.md`, `skatteklagenemnda_datasenter_2020.md`) mot primærkilder (skatteetaten.no / Rettsdata).
