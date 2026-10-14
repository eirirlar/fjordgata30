# eInnsyn-identifikasjon: Dokumentavgift ved konsernintern eiendomsoverdragelse

**Utarbeidet:** 2026-10-12\
**Agent:** Research-agent 9 (eInnsyn-identifikasjon)\
**Formål:** Identifisere konkrete saker i offentlige postlister (eInnsyn og tilsvarende) som belyser dokumentavgift-fritak ved konserninternoverdragelse etter sktl. § 11-21, med tanke på eventuell innsynsbestilling.

---

## 1. Toppseksjon — metodikk og begrensninger

### 1.1 eInnsyn er JavaScript-rendret — ingen maskinlesbar søke-API

eInnsyn (einnsyn.no) returnerer kun en blank HTML-skjelettside ved direkte HTTP-forespørsler. Søkemotoren er fullt JavaScript-drevet, og alle API-endepunkter som ble forsøkt (`/api/search`, `/api/public/search`, `/api/journalpost/search`) returnerer 404. Maskinsøk i postlistene er ikke mulig uten nettleser.

**Konsekvens:** Konkrete saksnumre fra eInnsyn-postlistene kan ikke hentes automatisk. Filen dokumenterer i stedet:

1. Hvilke organer som har relevant postliste å søke i.
2. Hva slags dokumenter man kan forvente å finne der.
3. Hvilke **offentlig tilgjengelige** saker som er identifisert via websøk og åpne kildelister.
4. Anbefalt søkestrategi direkte i eInnsyn-nettleseren.

### 1.2 Kontekst fra parallell research

Parallell research (dok_02_finansdepartementet.md, dok_03_skattedirektoratet.md) har fastslått at:

- Stortingsvedtaket § 2 bokstav k (2016-fritaket) dekker kun §§ 11-2 til 11-5, § 11-11 og § 11-20 — **ikke § 11-21**.
- Finansdepartementet ekskluderte § 11-21 bevisst i høringsnotatet av 22.05.2015.
- Dispensasjon etter dokumentavgiftsloven § 3 praktiseres svært restriktivt.
- Det finnes ingen kjent offentlig uttalelse som generelt fritar konserninterne overføringer etter § 11-21 fra dokumentavgift.

Formålet med eInnsyn-søk er å finne **konkrete klagesaker, brevvekslinger og dispensasjonsvedtak** som enten bekrefter eller nyanserer dette bildet.

---

## 2. Finansdepartementet

### 2.1 Hva å søke etter i eInnsyn

Finansdepartementet er øverste forvaltningsorgan for dokumentavgiften. Alle henvendelser om tolkning av regelverket og klager videresendt fra Skattedirektoratet havner hos FM.

**Anbefalte søketermer i eInnsyn → «Finansdepartementet»:**

| Søketerm | Forventet innhold |
|----------|-------------------|
| `dokumentavgift konsernoverdragelse` | Søknader om tolkningsuttalelse og klager |
| `fritak dokumentavgift § 11-21` | Dispensasjonsbegjæringer |
| `fritak dokumentavgift konserninternt` | Brev fra advokatfirmaer og selskaper |
| `dokumentavgiftsloven § 3 fritak konsern` | Dispensasjonsvedtak |
| `konsernintern overføring dokumentavgift` | Tolkningsforespørsler |

### 2.2 Identifiserte offentlige saker

**Sak 1 — Tolkningsuttalelse § 11-21 første ledd bokstav e (2015–2016)**

- **Tittel:** «§ 11-21 første ledd bokstav e: Henvendelse vedrørende konserninterne overføringer»
- **URL:** https://www.regjeringen.no/no/dokumenter/-11-21-forste-ledd-e-henvendelse-vedrorende-konserninterne-overforinger/id2510056/
- **Organ:** Finansdepartementet
- **Kategori:** Tolkningsuttalelse / brev
- **Relevans:** Gjelder vilkårene for skattefri konsernintern overføring etter § 11-21. Selv om dokumentavgift ikke er det direkte temaet, viser brevet FM's praksis med å svare på henvendelser om konserninterne overføringer. Kan inneholde koblinger til dispensasjonstematikk.
- **Tilgjengelighet:** Sammendrag tilgjengelig på regjeringen.no. Fullt dokument kan bestilles via eInnsyn.

**Sak 2 — Høringsnotat 22.05.2015 om dokumentavgiftsfritak ved omorganiseringer**

- **Tittel:** «Høring — forslag om fritak for dokumentavgift og omregistreringsavgift ved omorganiseringer med skattemessig kontinuitet»
- **FM-saksnummer:** 12/4289
- **URL:** https://www.regjeringen.no/no/dokumenter/horing---forslag-om-fritak-for-dokumentavgift-og-omregistreringsavgift-ved-omorganiseringer-med-skattemessig-kontinuitet/id2412995/
- **Organ:** Finansdepartementet
- **Kategori:** Høring (offentlig dokument)
- **Relevans:** Høringsnotatet inneholder eksplisitt avgrensning mot § 11-21 (s. 5). Høringssvarene til dette notatet kan inneholde argumentasjon fra advokatforeninger, NHO og næringslivsaktører om at § 11-21 bør inkluderes. Dette er svært relevant kildemateriell.
- **Tilgjengelighet:** Høringsnotatet er offentlig. Høringssvarene kan søkes i eInnsyn (Finansdepartementet, 2015, saksnummer 12/4289) eller lastes ned fra regjeringen.no.
- **Merk:** Høringssvarene fra Advokatforeningen, Skatteadvokatene og NHO er særlig interessante.

### 2.3 Søkestrategi for FM i eInnsyn

1. Gå til einnsyn.no → søk.
2. Filtrer på «Finansdepartementet» som avsender/mottaker.
3. Søk: `dokumentavgift konsern`.
4. Avgrens periode: 2013 til dags dato.
5. Sorter på dato, nyeste først.
6. Merk saksnumre med «konsernintern», «§ 11-21», «fritak eiendom».

---

## 3. Skattedirektoratet / Skatteetaten

### 3.1 Hva å søke etter

Skattedirektoratet er klageinstans for dokumentavgiftssaker (Kartverket er første instans). Alle klager på dokumentavgift ved konsernintern overføring havner her. Skattedirektoratet kan også innvilge dispensasjon etter dokumentavgiftsloven § 3 (myndighet delegert fra FM med virkning fra 01.01.2016).

**Anbefalte søketermer i eInnsyn → «Skattedirektoratet»:**

| Søketerm | Forventet innhold |
|----------|-------------------|
| `dokumentavgift konsernoverdragelse` | Klager fra selskaper |
| `fritak dokumentavgift eiendom konsern` | Dispensasjonssøknader og vedtak |
| `dokumentavgift § 11-21` | Søknader om fritak |
| `konsernintern overføring dokumentavgift klage` | Klagesaker |

### 3.2 Identifiserte offentlige saker

**Sak 3 — Årsrundskriv for dokumentavgift (2018, 2021, 2023, 2025)**

- **Tittel:** «Årsrundskriv for dokumentavgift [år]»
- **Organ:** Skattedirektoratet
- **URL-mønster:** https://www.skatteetaten.no/globalassets/rettskilder/avgiftsrundskriv/dokumentavgift-[år].pdf
- **Relevans:** Punkt 4.12 (fusjoner, fisjoner og omdanninger) og punkt 5 (dispensasjonsadgangen) beskriver gjeldende praksis. 2025-rundskrivet er siste tilgjengelige og ble bekreftet nedlastet og verifisert 2026-10-12.
- **Tilgjengelighet:** Fritt tilgjengelig som PDF.
- **Merk:** Rundskrivene nevner ikke § 11-21 i sammenheng med fritak, noe som i seg selv er kildeverdi.

**Sak 4 — Dispensasjonsvedtak etter dokumentavgiftsloven § 3**

Skattedirektoratet behandler dispensasjonssøknader etter dal. § 3. Slike vedtak er journalført men ikke systematisk publisert. De finnes i Skatteetatens postliste på eInnsyn.

- **Søk:** einnsyn.no → «Skatteetaten» → `dokumentavgift § 3 fritak` eller `dispensasjon dokumentavgift`
- **Forventet format:** Vedtaksbrev til søker (bedrift/advokat)
- **Relevans:** Kan vise om det finnes vedtak der § 3-dispensasjon er innvilget ved konsernintern overføring

### 3.3 Skatteklagenemnda — relevante saker

Skatteklagenemnda publiserer vedtak på Skatteetaten.no. Gjennomgang av publiserte vedtak avdekket ingen sak som direkte gjelder dokumentavgift og § 11-21-overføring av fast eiendom. Nærstående saker som er publisert:

- «Konsernforskriften — spørsmål om bortfall av latent skatteforpliktelse ved omorganisering»\
  URL: https://www.skatteetaten.no/en/rettskilder/type/uttalelser/bfu/konsernforskriften-bortfall-av-latent-skatteforpliktelse-ved-omorganisering/\
  (Gjelder skattemessige vilkår, ikke dokumentavgift)

- «Spørsmål om skattemessig kontinuitet etter skatteloven § 11-21»\
  URL: https://www.skatteetaten.no/en/rettskilder/type/uttalelser/bfu/sporsmal-om-skattemessig-kontinuitet-etter-skatteloven--11-21/\
  (BFU om skattevilkår, ikke dokumentavgift)

**Konklusjon:** Ingen publiserte Skatteklagenemnda-vedtak om dokumentavgift + § 11-21 er funnet. Dette styrker hypotesen om at slike saker enten avgjøres administrativt uten klage, eller at klager avvises uten at vedtaket offentliggjøres.

---

## 4. Kartverket (Statens kartverk)

### 4.1 Kartverkets rolle

Kartverket er første instans for dokumentavgift ved tinglysing. Det er Kartverket som beregner og krever inn avgiften, og som mottar klager (som videresendes til Skattedirektoratet).

Kartverkets postjournal er del av eInnsyn. URL til informasjon om innsyn:\
https://www.kartverket.no/en/about-kartverket/media/innsyn-i-saksdokumenta-til-kartverket

**Anbefalte søketermer i eInnsyn → «Statens kartverk»:**

| Søketerm | Forventet innhold |
|----------|-------------------|
| `dokumentavgift konsern` | Klage- og dispensasjonsbrev |
| `fritak dokumentavgift omorganisering` | Fritaksbeslutninger |
| `konsernintern overføring dokumentavgift` | Klager og forespørsler |
| `dokumentavgift klage eiendom konsern` | Klagesaker videresendt til Skattedirektoratet |

### 4.2 Identifiserte saker

**Sak 5 — Sivilombudet 2008 (2007/1061): Avslag på søknad om fritak for dokumentavgift**

- **Tittel:** «Avslag på søknad om fritak for dokumentavgift — tinglysingslovens regler om ekstinksjon»
- **Dato:** 01.04.2008
- **Saksnummer:** 2007/1061
- **URL:** https://www.sivilombudet.no/uttalelser/avslag-pa-soknad-om-fritak-for-dokumentavgift-tinglysingslovens-regler-om-ekstinksjon/
- **Organ:** Sivilombudet (klage over Finansdepartementets avslag)
- **Relevans:** Illustrerer praksis for svært restriktiv tolkning av dispensasjonsadgangen etter dal. § 3. Saken gjaldt dobbeltsalg (ekstinksjon), ikke konsernoverdragelse, men prinsippet om at dispensasjon bare innvilges ved «utilsiktet og uakseptabel virkning» er direkte overførbart.
- **Tilgjengelighet:** Fritt tilgjengelig på sivilombudet.no.

**Sak 6 — Sivilombudet 2014 (2013/2126): Krav til fullmakt ved salgsverdi**

- **Tittel:** «Sak om dokumentavgift — krav til fullmakt for med bindende virkning å kunne ansette salgsverdi i hjemmelserklæring»
- **Dato:** 27.08.2014
- **Saksnummer:** 2013/2126
- **URL:** https://www.sivilombudet.no/uttalelser/sak-om-dokumentavgift-krav-til-fullmakt-for-med-bindende-virkning-a-kunne-ansette-salgsverdi-i-hjemmelserklaering-pa-vegne-av-avgiftspliktige-hjemmelserververe/
- **Organ:** Sivilombudet
- **Relevans:** Gjelder kompetansespørsmål ved tinglysing, ikke konsernoverdragelse direkte. Viser Sivilombudets linje overfor Kartverket/Skattedirektoratet.
- **Tilgjengelighet:** Fritt tilgjengelig.

### 4.3 Tinglysingsregisteret — særlig journalføring

Kartverket fører en egen journal for tinglysingsregisteret, atskilt fra postjournalen i eInnsyn:\
https://www.kartverket.no/en/about-kartverket/media/innsyn-i-saksdokumenta-til-kartverket

Tinglyste dokumenter legges i panteboka og krever gebyr ved utlevering (forskrift om gebyr for tinglysing § 5 tredje ledd). Klagekorrespondanse og dispensasjonssøknader vil imidlertid ligge i den ordinære postjournalen tilgjengelig via eInnsyn.

---

## 5. Nemnder — Klagenemnda for merverdiavgift og analoger

### 5.1 Finnes det en klagenemnd for dokumentavgift?

Det finnes **ingen separat klagenemnd** for dokumentavgift. Klagestrukturen er:

1. Første instans: Kartverket (tinglysingsavdelingen)
2. Klageinstans: Skattedirektoratet
3. Videre klage: Skatteklagenemnda (for vedtak av prinsipiell betydning)
4. Domstolsprøving: Tingretten

Klagenemnda for merverdiavgift (KMVA) er ikke relevant for dokumentavgift.

### 5.2 Skatteklagenemnda — søk

Skatteklagenemnda publiserer vedtak på skatteetaten.no. Søk i Skatteklagenemndas arkiv etter «dokumentavgift» gir per 2026-10-12 ingen treff på saker om konsernintern overføring etter § 11-21. Alle publiserte § 11-21-vedtak fra nemnda gjelder skatt, ikke dokumentavgift.

**Søk i eInnsyn → «Skatteklagenemnda»:**

| Søketerm | Forventet innhold |
|----------|-------------------|
| `dokumentavgift konsernoverdragelse` | Evt. upubliserte vedtak |
| `dokumentavgift fritak § 11-21` | Prinsippsaker |

---

## 6. eInnsyn — praktisk søkeveiledning

### 6.1 Slik søker du i eInnsyn

1. Gå til **https://einnsyn.no/sok**
2. Skriv inn søketermen i søkefeltet.
3. Under «Filter»: velg **«Statlige virksomheter»** og velg én av disse etter tur:
   - «Finansdepartementet»
   - «Skatteetaten» (dekker Skattedirektoratet)
   - «Statens kartverk»
4. Under «Type»: velg «Journalpost» for brev og saksdokumenter.
5. Avgrens gjerne på **dato** (f.eks. 2016–2026).

### 6.2 Slik bestiller du innsyn

Hvert søkeresultat viser en journalpost med tittel, dato, saksnummer, avsender og mottaker. Journalposter merket «Offentlig» er fritt tilgjengelig som PDF. Journalposter merket «Unntatt offentlighet» krever formell innsynsbegjæring:

1. Klikk på journalposten.
2. Velg «Bestill innsyn».
3. Fyll inn navn, e-post og begrunnelse (begrunnelse er ikke nødvendig, men anbefales for rask saksbehandling).
4. Svar skal komme innen **5 virkedager** (offentleglova § 29).

---

## 7. Anbefalte bestillinger — topp 5 saker

Basert på research er følgende fem konkrete innsynsbestillinger prioritert, sortert etter antatt nytteverdi:

---

### Prioritet 1 — Høringssvar fra Advokatforeningen og NHO (2015)

**Hva:** Høringssvar til FM's høringsnotat 22.05.2015 om fritak for dokumentavgift ved omorganiseringer (saksnr. 12/4289). Særlig innspill som gjelder § 11-21-spørsmålet.

**Hvor finnes det:** Regjeringen.no (høringssvarene er i prinsippet offentlige); evt. eInnsyn → «Finansdepartementet» → saksnr. 12/4289.

**Slik bestiller du:** Søk på https://www.regjeringen.no/no/dokumenter/horing---forslag-om-fritak-for-dokumentavgift-og-omregistreringsavgift-ved-omorganiseringer-med-skattemessig-kontinuitet/id2412995/ etter «høringssvar». Alternativt: eInnsyn → Finansdepartementet → `12/4289`.

**Hvorfor nyttig:** Høringssvarene kan dokumentere at næringsliv og advokater argumenterte for å inkludere § 11-21, og at FM bevisst avviste dette. Styrker vår dokumentasjon av at utelatelsen er gjennomtenkt (taler for at en klage eller BFU-strategi må adressere lovgivers bevisste valg).

---

### Prioritet 2 — Dispensasjonsvedtak fra Skattedirektoratet etter dal. § 3 (2016–2026)

**Hva:** Vedtak der Skattedirektoratet har innvilget eller avslått dispensasjon etter dokumentavgiftsloven § 3 i saker om konsernintern eiendomsoverføring.

**Hvor finnes det:** eInnsyn → «Skatteetaten» → `dispensasjon dokumentavgift konsernintern` eller `dokumentavgift § 3 fritak eiendom`.

**Slik bestiller du:** Identifiser relevante journalposter i eInnsyn, klikk «Bestill innsyn» for journalposter merket «Unntatt offentlighet».

**Hvorfor nyttig:** Viser om det finnes dispensasjonspraksis som kan utnyttes for konsernintern overføring etter § 11-21. Dersom vedtak avslår dispensasjon, bekrefter det at dokumentavgift er uunngåelig og at fisjon-strukturen er eneste vei.

---

### Prioritet 3 — Klager på dokumentavgift behandlet av Skattedirektoratet (2016–2026)

**Hva:** Klager fra selskaper som har betalt dokumentavgift ved konsernintern overføring og klaget på at avgiften ikke skulle vært krevd.

**Hvor finnes det:** eInnsyn → «Skatteetaten» → `dokumentavgift klage konsernoverdragelse`.

**Slik bestiller du:** Bestill innsyn i journalposter der tittel indikerer klage og konsernoverdragelse.

**Hvorfor nyttig:** Klagevedtak fra Skattedirektoratet er bindende forvaltningspraksis. Dersom klager er avvist konsekvent, er dette sterkt bevis for at dokumentavgift er uunngåelig. Dersom det finnes vedtak der klage er tatt til følge, kan det finnes unntak vi ikke kjenner til.

---

### Prioritet 4 — Stortingets skriftlige spørsmål om dokumentavgift og § 11-21 (2016–2026)

**Hva:** Skriftlige spørsmål fra stortingsrepresentanter til finansministeren om dokumentavgift ved konsernoverdragelse.

**Identifiserte saker (krever innhenting av fullt innhold):**

- Skriftlig spørsmål fra Svein Flåtten (H), saksnr. 23425:\
  URL: https://www.stortinget.no/no/Saker-og-publikasjoner/Sporsmal/Skriftlige-sporsmal-og-svar/Skriftlig-sporsmal/?qnid=23425

- Skriftlig spørsmål fra Gjermund Hagesæter (FrP), saksnr. 17691:\
  URL: https://www.stortinget.no/no/Saker-og-publikasjoner/Sporsmal/Skriftlige-sporsmal-og-svar/Skriftlig-sporsmal/?qnid=17691

**Slik bestiller du:** Sidene er offentlige; bruk URL direkte i nettleser. Sidene er JavaScript-rendret og krever nettleser, ikke curl.

**Hvorfor nyttig:** Finansministerens svar er bindende politiske uttalelser om tolkningen av regelverket. Dersom spørsmålene gjelder § 11-21 og konsernoverdragelse, er svarene del av lovhistorikken.

---

### Prioritet 5 — FM's brev vedrørende konserninterne overføringer (§ 11-21) til næringslivsorganisasjoner (2003–2016)

**Hva:** Brev fra Finansdepartementet til FNH (Finansnæringens Hovedorganisasjon), Advokatforeningen eller NHO om dokumentavgiftsplikten ved konserninterne overføringer, herunder det omtalte brevet av 29.01.2004 (referert til i sekundærkilder, ikke funnet i åpne databaser per 2026-10-12).

**Hvor finnes det:** eInnsyn → «Finansdepartementet» → `dokumentavgift konsernintern 2004` eller `dokumentavgift § 8-10 FNH`.

**Slik bestiller du:** eInnsyn → Finansdepartementet → søk på `dokumentavgift FNH` eller `dokumentavgift konsernintern overføring 2004`. Bestill innsyn i alle treff.

**Hvorfor nyttig:** Dersom brevet av 29.01.2004 faktisk inneholder en FM-uttalelse om at konserninterne overføringer etter § 11-21 er fritatt for dokumentavgift, er dette et svært viktig rettskildedokument — enten som støtte for fritak eller (dersom innholdet er annerledes enn referert) som dokumentasjon for at sekundærkilden er feilaktig.

---

## 8. Sammenstilling — saker identifisert og tilgjengelig per 2026-10-12

| Nr | Tittel | Organ | Saksnummer/ID | Tilgjengelighet | Relevans |
|----|--------|-------|---------------|-----------------|----------|
| 1 | § 11-21 første ledd bokstav e: Henvendelse vedrørende konserninterne overføringer | Finansdepartementet | id2510056 | Offentlig (regjeringen.no) | Høy |
| 2 | Høring om fritak for dokumentavgift ved omorganiseringer (+ høringssvar) | Finansdepartementet | 12/4289 | Høringsnotat offentlig; høringssvar via eInnsyn | Svært høy |
| 3 | Årsrundskriv for dokumentavgift 2025 | Skattedirektoratet | — | Offentlig PDF | Høy |
| 4 | Skriftlig spørsmål Flåtten (H) | Stortinget | qnid 23425 | Offentlig (JavaScript-krevende) | Middels |
| 5 | Skriftlig spørsmål Hagesæter (FrP) | Stortinget | qnid 17691 | Offentlig (JavaScript-krevende) | Middels |
| 6 | Avslag på søknad om fritak (2008/2007/1061) | Sivilombudet | 2007/1061 | Offentlig (sivilombudet.no) | Middels |
| 7 | Dispensasjonsvedtak etter dal. § 3 (2016–2026) | Skattedirektoratet | Ukjent | Krever eInnsyn-søk | Svært høy |
| 8 | Klager på dokumentavgift — konsernoverdragelse (2016–2026) | Skattedirektoratet/Kartverket | Ukjent | Krever eInnsyn-søk | Svært høy |
| 9 | FM-brev til FNH 29.01.2004 | Finansdepartementet | Ukjent | Ikke funnet; krever eInnsyn-søk | Svært høy (hvis eksisterer) |

---

## 9. Konklusjon

eInnsyn er ikke maskinlesbar via curl/API. Automatisk uttrekk av konkrete saksnumre er ikke mulig; søk må gjøres manuelt i nettleseren.

Av offentlig tilgjengelige saker er de viktigste:

- Høringen fra 2015 (saksnr. 12/4289) med tilhørende høringssvar — spesielt innspill om § 11-21 fra Advokatforeningen, NHO og Skatteadvokatene.
- Årsrundskrivene for dokumentavgift (fritt tilgjengelig) som bekrefter at § 11-21 ikke nevnes i sammenheng med fritak.

De mest verdifulle sakene som **krever aktiv innsynsbestilling** er dispensasjonsvedtak og klagesaker fra Skattedirektoratets postliste (Prioritet 2 og 3 ovenfor). Disse finnes kun i eInnsyn og er ikke publisert som del av Skatteetaten.nos rettskildesamling.

**Anbefalt neste steg:** Manuelt eInnsyn-søk i nettleseren etter Prioritet 2–5 ovenfor, med innsynsbegjæring for dokumenter merket «Unntatt offentlighet».

---

## 10. Kildeliste

| Dokument | URL | Hentet |
|----------|-----|--------|
| eInnsyn søkeportal | https://einnsyn.no/sok | 2026-10-12 |
| Kartverket — innsyn i saksdokumenter | https://www.kartverket.no/en/about-kartverket/media/innsyn-i-saksdokumenta-til-kartverket | 2026-10-12 |
| Skatteetaten — offentlig postjournal | https://www.skatteetaten.no/en/press/skatteetatens-postjournal/ | 2026-10-12 |
| Høring — fritak dokumentavgift ved omorganiseringer (Finansdepartementet 2015) | https://www.regjeringen.no/no/dokumenter/horing---forslag-om-fritak-for-dokumentavgift-og-omregistreringsavgift-ved-omorganiseringer-med-skattemessig-kontinuitet/id2412995/ | 2026-10-12 |
| FM tolkningsuttalelse § 11-21 første ledd bokstav e | https://www.regjeringen.no/no/dokumenter/-11-21-forste-ledd-e-henvendelse-vedrorende-konserninterne-overforinger/id2510056/ | 2026-10-12 |
| Sivilombudet 2008 — avslag fritak dokumentavgift (2007/1061) | https://www.sivilombudet.no/uttalelser/avslag-pa-soknad-om-fritak-for-dokumentavgift-tinglysingslovens-regler-om-ekstinksjon/ | 2026-10-12 |
| Sivilombudet 2014 — fullmakt ved salgsverdi (2013/2126) | https://www.sivilombudet.no/uttalelser/sak-om-dokumentavgift-krav-til-fullmakt-for-med-bindende-virkning-a-kunne-ansette-salgsverdi-i-hjemmelserklaering-pa-vegne-av-avgiftspliktige-hjemmelserververe/ | 2026-10-12 |
| Årsrundskriv for dokumentavgift 2025 (PDF) | https://www.skatteetaten.no/globalassets/rettskilder/avgiftsrundskriv/dokumentavgift-2025.pdf | 2026-10-12 |
| Stortinget skriftlig spørsmål — Flåtten (H), saksnr. 23425 | https://www.stortinget.no/no/Saker-og-publikasjoner/Sporsmal/Skriftlige-sporsmal-og-svar/Skriftlig-sporsmal/?qnid=23425 | 2026-10-12 |
| Stortinget skriftlig spørsmål — Hagesæter (FrP), saksnr. 17691 | https://www.stortinget.no/no/Saker-og-publikasjoner/Sporsmal/Skriftlige-sporsmal-og-svar/Skriftlig-sporsmal/?qnid=17691 | 2026-10-12 |
