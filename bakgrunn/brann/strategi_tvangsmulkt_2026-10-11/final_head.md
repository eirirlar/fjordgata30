# Strategianalyse mot tvangsmulkt — TBRT sak 24/1007 — Fjordgata 30

## Metadata

**Dato:** 11. oktober 2026
**Status:** Final-rapport (resultat av iterativ dypdykksprompt T171)
**Iterasjoner gjennomført:** 03 (full iter 01 + målrettede iter 02 og iter 03)
**Faktagrunnlag:** `bakgrunn/brann/strategi_tvangsmulkt_2026-10-11/faktaark.md` (versjon 11.10.2026 med 4 korreksjoner i iter 02 og 2 utvidelser i iter 03)
**Omfang:** ca. 3 000+ linjer prosa + 3 timers arbeid med fem Sonnet-agenter
**Bidragsytere:** Fem parallelle Sonnet-agenter per iterasjon — Maksimalistjurist, Prosessguerilla, Selskapsrettslig arkitekt, Politisk strateg, Djevelens advokat
**Opprettet av:** Opus 4.7 (1M context) som orkestrator, 11.10.2026

### Mål og målgruppe

Formålet er en grundig, operasjonell strategianalyse som dekker alle lovlige måter å unngå, redusere eller forsinke TBRTs tvangsmulkt mot Kodeworks Eiendom AS. Rapporten er skrevet for en jurist eller strategirådgiver som skal handle direkte på innholdet — ikke et sammendrag til styremøte. Hver strategi har hjemmel, konkret handling, forventet motstand, mottrekk, interaksjon med andre strategier og konkret utkast til formulering der det er relevant.

### Iterativt arbeidsmønster

- **Iter 01:** Full første iterasjon med fem parallelle agenter. Produserte 304–530 linjer per agent (totalt 2 076 linjer rådata) som ble integrert til iterasjon_01-rapporten på 2 412 linjer.
- **Iter 02:** Målrettet utvidelse basert på review 01. Fokus: Statsforvalter-sporet, 2023/2570-verifisering, fisjonsmilepælsplan, DSB-amnestitilbud. Produserte oppdaterte v2-rapporter (totalt 2 701 linjer, +625 fra iter 01) og 10 nye lovkilde-filer.
- **Iter 03:** Målrettet utvidelse basert på review 02. Fokus: Lovkildeverifikasjon mot Lovdata, § 42-anmodning med 2023/2570, kronikkutkast til Adresseavisen, forliksrådspresisering. Agent 1 (Lovdata-verifikasjon) traff 32k-token-maks før rapporten var skrevet, men hadde før den gang verifisert alle 6 utestående lovfiler og oppdaget en kritisk feil i tvl. § 34-1 fra iter 02. Agent 2, 4 og 5 leverte v3-rapporter. Agent 3 ble ikke kjørt i iter 03 (ingen funn fra review).

### Avvik mellom iterasjoner (dokumentert og løst)

Fem kritiske avvik ble identifisert underveis:

**Avvik 1 — «vedtak 13.12.2022».** Den tidligere samlede strategianalysen fra 11.10.2026 (den som ga opphav til T171) refererte til et tvangsmulktvedtak fra desember 2022. Dette er en hallusinasjon fra tidligere AI-sesjon. Alle fem agenter har bekreftet at det ikke eksisterer. Eneste gyldige tvangsmulktvedtak er fra 07.05.2025, med dagsats kr 2 000 som løper fra 01.01.2026.

**Avvik 2 — «kr 2,7 MNOK påløpt».** Den tidligere analysen angav ca. kr 2,7 MNOK i påløpt mulkt. Korrekt tall per bero 25.06.2026 er **ca. kr 352 000** (176 dager × kr 2 000). Av dette er kr 184 000 innkrevd gjennom tre runder.

**Avvik 3 — Trondheim kommunes eierandel i TBRT.** Første analyse anga 72 % som UKJENT. Agent 4 i iter 02 verifiserte mot tbrt.no at korrekt andel er **85,79 %**. Faktaarket er oppdatert.

**Avvik 4 — Sivilombudets uttalelse 2023/2570.** Første analyse flaget uttalelsen som ubekreftet. Agent 2 i iter 02 lastet den ned verbatim fra sivilombudet.no og lagret som `bakgrunn/lovverk/sivilombudet_2023-2570.md`. Prinsippet om tilbakevirkende utsatt iverksetting ved forvaltningens treghet er dermed en direkte anvendbar presedens i vår sak.

**Avvik 5 — Lovreferanser (skatteloven § 13-1/13-2, dekningsloven § 9-4/9-6, straffeloven § 406/kap. 31).** Agent 3 i iter 01 flagget at faktaarket hadde upresis hjemmelbruk. Faktaarket er oppdatert i iter 02: skatteloven § 13-2 er riktig omgåelsesnorm, dekningsloven § 9-6 er riktig prioritetsklasse for TBRT-kravet, og straffeloven kap. 31 §§ 402–407 nyanserer kreditorsvik-begrepet.

### Åpne svakheter ved endelig stopp

- **Agent 1 iter 03 traff token-maks:** v3-rapporten ble ikke skrevet, men lovkildene ble verifisert. Konkret forføyning-begjæringutkast til Trondheim tingrett er dermed ikke levert av Agent 1 i iter 03. Vilkårene er grundig drøftet i v2 pkt. 6, men full begjæringutkast må enten utarbeides manuelt av advokat eller være gjenstand for ny agent-kjøring.
- **Agent 1 iter 03 oppdaget feil i tvl. § 34-1 fra iter 02:** Konsolidert versjon fra iter 02 hadde feil tittel («Vilkårene for midlertidig forføyning» — korrekt er «Sikringsgrunn»). Filen er oppdatert med verbatim Lovdata-tekst i iter 03. Alle agentreferanser til tvl. § 34-1 bør kontrolleres mot den nye filen før de siteres i leveranser.
- **Enkelte underpunkter bevisst nedprioritert:** Agent 1 pkt. 11 (Grl. §§ 97/102, ca. 350 ord — bevisst mindre enn 400) og Agent 3 pkt. 16 (SI vs. Intrum, ca. 240 ord). Disse flaggs som kjent svakhet ved stopp.
- **Riksrevisjonsinnslag (Agent 5 pkt. 13 iter 01):** Behandlet kort, kunne vært utvidet med konkret skritt om henvendelse til Stortingets kontroll- og konstitusjonskomité.
- **Enkelte eksterne kontakter:** Nielsen og Lillebråten verifisert i iter 02. Noen få mindre kontakter (f.eks. detaljerte kontaktpunkter i Fortidsminneforeningen DTA) kunne vært supplert.

### Rapportens struktur

- **Metadata** (dette avsnittet)
- **Verifisert sakssituasjon** (full gjengivelse av faktaarket)
- **Umiddelbare prioriteringer** (de neste 7 dager, 11 prioriteringer)
- **Del 1 — Formelle rettsmidler** (Agent 1 v2 — 15 underpunkter + Agent 1 v2 pkt. 16 om Statsforvalter + v2-utvidelsene av pkt. 5, 8, 12)
- **Del 2 — Prosessuelle forsinkelser og saksbehandlingsfeil** (Agent 2 v3 — 16 underpunkter)
- **Del 3 — Selskapsrettslige grep** (Agent 3 v2 — 18 underpunkter)
- **Del 4 — Mediestrategi og politisk mobilisering** (Agent 4 v3 — 18 underpunkter)
- **Del 5 — Kreative/ukonvensjonelle manøvre** (Agent 5 v3 — 18 underpunkter)
- **Kombinasjonsstrategier** (seks kombinasjoner A–F)
- **Hva som er over streken — eksplisitt** (lovlig/ikke lovlig)
- **Forventet motstand og mottrekk** (9 TBRT-trekk + 4 scenarioer for allierte)
- **Risiko- og sannsynlighetsmatrise** (20 strategier, prosa + tabell)
- **Konkrete utkast** (Utkast A–P)
- **Kjente svakheter ved stopp**
- **Kildeliste**

---

## Verifisert sakssituasjon (fra faktaarket, versjon 11.10.2026)

**Partene:**

Kodeworks Eiendom AS (KWE), org.nr. 920 478 506, daglig leder Eirik Larsen (eirik.larsen@kodeworks.no, +47 416 70 269). Besøksadresse: Beddingen 8, 7042 Trondheim. Fisjon til Fjordgata 30 AS er planlagt men ikke registrert.

Trøndelag brann- og redningstjeneste IKS (TBRT), org.nr. 992 047 364. Sluppenvegen 18, 7037 Trondheim. Saksbehandler Morten Knutsen (+47 920 89 414). Signatarer på kjernedokumenter: Anna-Karin Hermansen (leder forebyggende / fungerende brannsjef), Tove-Kristin Reitan (juridisk rådgiver). Saksfremlegg til klageorganet 26.06.2026 er signert av Torbjørn Mæhlumsveen (brann- og redningssjef) og Geir Jacobsen (juridisk rådgiver). Trondheim kommunes eierandel: **85,79 %** (verifisert mot tbrt.no 11.10.2026). Klagenemnda som behandlet sak 3/26 25.08.2026 består av Harald Fagervold, Mari Stene-Ry, Ola Skarsheim, Per Øystein Karlsen og Randi Eikevik.

Fjordgata 30 (matrikkel 5001/401/149): brygge fra 1857, verneklasse B etter Trondheim kommunes arealplan. Innen middelalderbyen Trondheim, hvorfor Riksantikvarens dispensasjon etter kulturminneloven § 8 er nødvendig før igangsettingstillatelse.

**Pålegg og tvangsmulktvedtak:**

Pålegg om brannsikring 08.11.2024 (sak 24/1007-27), hjemmel brann- og eksplosjonsvernloven § 37, frist 01.05.2025. Dekker avvik 1–3 fra tilsynsrapport 24.01.2024 (hjemler i brannforskriften §§ 4, 5, 8, 9, 10).

Vedtak om løpende tvangsmulkt 07.05.2025 (sak 24/1007-28), hjemmel bel. § 39. Dagsats kr 2 000 fra 01.01.2026. Klage på selve vedtaket ble behandlet av klageorganet i TBRT 30.09.2025 og tatt delvis til følge / ikke tatt til følge (eksakt detalj må verifiseres mot `bakgrunn/2025-09-16_saksfremlegg_klageorgan_tbrt.txt`).

**Beløp:**

Tre innkrevinger: 19.03.2026 (kr 36 000, sak 24/1007-45), 17.04.2026 (kr 54 000, sak 24/1007-46), 03.06.2026 (kr 94 000, sak 24/1007-52). Totalt innkrevd: kr 184 000.

Totalt påløpt per bero 25.06.2026: ca. kr 352 000 (176 dager × kr 2 000). Differanse kr 168 000 i påløpt-men-ikke-innkrevd, med TBRT-forbehold om innkreving tilbake i tid.

**Intrum og Namsfogden:**

Intrum sak 45221136 (TBRT kreditorref. 304462), saldo kr 103 452,03. Konkursvarsel sendt 30.09.2026 — gjelder kun hovedkrav fra 3. gangs innkreving (kr 94 000) + renter og salær, ikke hele kr 184 000. Namsfogden i Trøndelag sak S2026-026646, varsel om forkynnelse mottatt 06.10.2026. Dokumentet ikke hentet per 11.10.2026.

**Bero av løpende tvangsmulkt:**

TBRT brev 25.06.2026 (sak 24/1007-63) satte løpende innkreving midlertidig i bero fram til 01.01.2027. Forutsetninger: nødvendige søknader til plan- og bygningsmyndighetene inngis snarest etter rammetillatelse, utførelse av brannsikringen følger umiddelbart etter tillatelsene, brannsikringen prioriteres. TBRT forbeholder seg å kreve inn tilbake i tid ved brudd på forutsetningene. Beroen gjelder ikke de allerede innkrevde kr 184 000 — bare løpende mulkt. Frafall av påløpt mulkt kan ifølge TBRT bare skje ved DSB etter bel. § 39.

**Pågående klager og søknader:**

(a) TBRT-klage på innkrevingene (18.06.2026) → oppreisning og utsatt iverksetting innvilget 26.06.2026 (sak 24/1007-62) → saksfremlegg 26.06.2026 (sak 24/1007-61) → klagenemndsvedtak 25.08.2026 (sak 3/26, ikke tatt til følge) → orientering 02.09.2026 (sak 24/1007-65).

(b) Sivilombudet-klage på TBRTs saksbehandling, sendt 06.10.2026 via sivilombudet.no. Korrigeringsnotat sendt 07.10.2026 for feil paragrafreferanse (brannforskriften § 6 → § 8).

(c) DSB-søknad om frafall etter bel. § 39, sendt 08.10.2026. Fil: `leveranser/brann/dsb/2026-10-08_dsb_soknad_frafall_tvangsmulkt.md`. Følger DSBs momentliste etter Fossegrenda-mal.

(d) Anmodning til TBRT om midlertidig stans i inndriving (Intrum-sak 45221136), sendt 08.10.2026.

(e) Statusbrev til TBRT, sendt 08.10.2026 — orientering om byggeprosjektets fremdrift og dokumentasjon av at bero-forutsetningene er oppfylt.

**Byggesak:**

BYGG-26/81377, rammesøknad levert 12.05.2026 (supplert 19.05.2026). Foreløpig tilbakemelding 16.07.2026 (BYGG-26/81377-5) med krav om: dispensasjonssøknad for ramper, kommunal tillatelse (Eierskapsenheten — henvendelse 25.08.2026), omprosjektering for TEK17 § 12-7. Byantikvarens uttalelse 04.09.2026 om bæresystem endrer premissene. Riksantikvarens dispensasjon etter kulturminneloven § 8 nødvendig før IG. Realistisk tidligste IG-tidspunkt: Q1–Q2 2027.

**Branntekniske tiltak gjennomført:**

HRPs brannsikringsplan for gjennomføringsfasen (notat 26.02.2026). Autronica årskontroll brannalarm 12.05.2026 — ingen avvik. Tensio DLE eltilsyn 18.09.2026 — ingen feil. Rivearbeid 2025–01.10.2026: 38 tonn avfall fjernet. Bygget tomt fra august 2026. Alle avvik 1–3 unntatt sprinkler er lukket iht. TBRTs eget saksfremlegg 16.09.2025.

**Finansiering og tilskudd:**

Kulturminnefondet kr 750 000 (tildelt), Byantikvaren kr 500 000 (tildelt), Enova og Stiftelsen UNI (beløp ukjent). Totalt eksterne tilskudd minst kr 1 250 000.

**Lovkilder (oppdatert etter iter 03):**

Alle sentrale lovkilder (bel. §§ 1, 6, 37, 39, 40, 41, 42; fvl. §§ 6, 11, 11a, 17, 18 c, 24, 25, 27, 28, 29, 31, 35, 36, 41, 42, 51; forskrift om brannforebygging §§ 4, 5, 8, 9, 10; pbl. §§ 20-1, 29-4, 31-2; aksjeloven kap. 14, § 17-1; dekningsloven kap. 5 og 9; skatteloven §§ 11-4, 11-7, 13-1, 13-2; straffeloven kap. 31 §§ 402–407; IKS-loven §§ 3, 7, 13, 15, 38; foreldelsesloven §§ 2, 3, 17; offentleglova §§ 3, 14, 32; sivilombudsloven §§ 4, 8, 9; tvisteloven kap. 15 og 34; tvangsfullbyrdelsesloven §§ 5-11, 7-2, 13-14; rekonstruksjonsloven; konkursloven §§ 60, 61, 63, 64, 65; grunnloven §§ 97, 102, 113; EMK art. 6; EMK P1-1; menneskerettsloven; skadeserstatningsloven § 2-1; tinglysingsloven) er verifisert mot Lovdata og lagret i `bakgrunn/lovverk/`. Sivilombudets uttalelser 2009/848 og 2023/2570 er verifisert verbatim.

---

## Umiddelbare prioriteringer (neste 7 dager)

Prioriteringene er oppdatert fra iter 01 og iter 02. Statsforvalter-sporet står nå som prioritet 4 — reflekterer brukerinput etter iter 01 og Agent 1s utvidede analyse i iter 02 pkt. 16 om at kanalen er lavterskel, komplementær til DSB og Sivilombudet, og slår på en strukturell svakhet i IKS-vedtakskjeden.

**Prioritet 1 — Hent forkynnelsesdokumentet på Heimdal politistasjon** (frist senest 12.–13.10.2026 iht. SMS). Når dokumentet er hentet, les det nøye for å avklare om det er en utleggsbegjæring, et betalingspåbud eller en konkursbegjæring. Dette styrer hvilken innsigelsesprosedyre som brukes. Alle fem agenter understreker at dokumentet ikke må ligge uhentet, fordi forkynnelse anses etter en bestemt frist som skjedd uansett.

**Prioritet 2 — Innsigelse til Namsfogden innen 14 dager fra forkynnelse.** Materielt grunnlag: fvl. § 51 annet ledd om rettslig umulighet. Prosessuelt grunnlag: pågående overprøving ved Sivilombudet (klage 06.10.2026) og DSB (søknad 08.10.2026). Namsfogden plikter å stanse fullbyrdelsen mens innsigelse behandles, jf. tvangsfullbyrdelsesloven § 5-11. Formuleringsutkast som Utkast A/A2 (se «Konkrete utkast» nedenfor og Agent 1 pkt. 7 i Del 1).

**Prioritet 3 — Betaling eller sikkerhetsstillelse for Intrum-kravet kr 103 452.** Depositum eller bankgaranti (Agent 3 pkt. 17 i Del 3 har konkret bankgaranti-tekst) som stanser konkursvarselet uten å erkjenne kravet. Alternativt direkte oppgjør hvis likviditet tillater. Dette er det mest effektive akuttgrepet.

**Prioritet 4 — Statsforvalter-klage og oppreisning av klagefrist.** Agent 1 pkt. 16 (iter 02) operasjonaliserer med fristberegning etter fvl. § 31 bokstav c (manglende klagerettsveiledning etter fvl. § 27 — dokumentert av Agent 2 iter 02 pkt. 14) og 500+ ord brevutkast. Kjernepåstand: TBRT er ikke «kommunen» i bel. § 41 jf. fvl. § 28 annet ledds forstand; Statsforvalteren er potensielt rett klageinstans. Lavterskel, ingen advokatkrav, komplementær til DSB og Sivilombudet.

**Prioritet 5 — Formell § 42-anmodning til TBRT (og subsidiært DSB) om utsatt iverksetting av innkrevingsvedtakene.** Agent 2 pkt. 16 (iter 03) har eksakt behandlingstidsberegning og verbatim 2023/2570-sitat med 450-ords brevutkast. Grunnlag: fvl. § 42 tredje setning (åpner for utsetting ved pågående Sivilombudssak) og Sivilombudets 2023/2570-prinsipp om tilbakevirkende utsatt iverksetting ved forvaltningens treghet. Smalt argument: kr 14 000 for 7 dager uten § 42-avgjørelse. Bredt argument: kr 184 000 for hele den innkrevde perioden.

**Prioritet 6 — Midlertidig forføyning til Trondheim tingrett** mot Intrum-sak 45221136. Beredskapsressurs hvis Prioritet 3 og 5 ikke løser akutt-situasjonen. Hjemmel: tvisteloven kap. 34, §§ 34-1 (sikringsgrunn) og 34-2 (sannsynliggjøring av krav og sikringsgrunn — merk at tvl. § 34-1 har tittelen «Sikringsgrunn», ikke «Vilkårene for midlertidig forføyning», jf. Agent 1 iter 03-korreksjon). Kostnad: rettsgebyr ca. kr 1 274 + advokatbistand kr 20 000–50 000. **Åpen svakhet:** Agent 1 traff token-maks før konkret begjæringsutkast ble levert i iter 03 — vilkårene er dekket i Agent 1 pkt. 6, men full begjæring må utarbeides før innlevering.

**Prioritet 7 — Innsynsoffensiv.** Tre innsynsbegjæringer etter fvl. § 18 c og offentleglova §§ 3, 14 jf. 32: (a) TBRT: intern korrespondanse med DSB og Plan og Bygg, møteprotokoll fra klageorganet 25.08.2026, instruksjonsbrev til Intrum; (b) Trondheim Plan og Bygg: intern kommunikasjon med TBRT; (c) alle habilitetsavklaringer om saksbehandler Knutsen. Utkast G.

**Prioritet 8 — Statusbrev til TBRT om byggesaksprogresjon** (månedlig fram til 01.01.2027). Opprettholder bero-forutsetningene og reduserer risikoen for at TBRT reaktiverer løpende mulkt ved årsskiftet.

**Prioritet 9 — Brev til TBRTs representantskap om omgjøringsbegjæring** etter fvl. § 35. Agent 1 pkt. 3, Agent 4 pkt. 11, Agent 5 pkt. 9. Adressert direkte til Kent Ranum (H, leder) og Sara Shafighi (Ap, nestleder) — ikke til brannsjefen. Utkast E.

**Prioritet 10 — Formell forespørsel til Byantikvaren om uttalelse om søknadsplikten** for sprinklerinstallasjon i verneklasse B-bygg. Agent 5 pkt. 5. Utkast F. Gjør lovspenningen pbl./bel. til dokumentert faktum, ikke bare anførsel.

**Prioritet 11 — DSB-tilleggsbrev med «amnesti mot kommitering»-tilbud.** Agent 5 pkt. 18 (iter 02) med 450-ords brevutkast. Forpliktelse til sprinklerinstallasjon innen fast dato mot DSB-frafall av påløpt mulkt, uten erkjennelse av vedtakets gyldighet. Asymmetrisk gunstig: KWE får amnesti, DSB får faktisk brannsikring, prosjektet realiseres, offentlige midler brukes etter formålet.

**Supplerende operasjonell plan:**

Uke 2–4: Innsynsbegjæringer sendt, bankforhandling om pant, formelle brev til representantskapet og Byantikvaren.

Uke 4–8: Mediesporet forberedes — kronikkutkast klart (Agent 4 pkt. 18 iter 03, 640 ord publiseringsklart), kontakt med Fortidsminneforeningen og Riksantikvaren.

Uke 8–16: Fisjon-milepælsplan gjennomføres (Agent 3 pkt. 18 iter 02, uke-for-uke 12.10.2026–25.01.2027).

Måned 4–12: Oppfølging av Sivilombudet og DSB med ny dokumentasjon. Hvis bero-forutsetningene faller mot 01.01.2027: mediesporet lanseres.

---
