# Fjordgata 30 – Oppgaveliste

## Legende
- `[x]` Ferdig
- `[~]` Påbegynt / under arbeid
- `[ ]` Ikke startet

Oppgaver identifiseres med ID på formen **T01**, **T02** osv. Bruk disse ID-ene til å referere til oppgaver i kommunikasjon, commits og dokumentasjon. Løsninger dokumenteres under oppgaven i dette dokumentet.

### T01 `[ ]` Arbeidsrapport – utbetalingsanmodning, Kulturminnefondet / Stiftelsen UNI / Byantikvaren
**Mottakere:** Kulturminnefondet (750 000 kr), Stiftelsen UNI (100 000 kr), Byantikvaren (500 000 kr)

Alle tre støttegivere krever dokumentasjon på at det faktisk er utført fysisk arbeid (ikke bare planlegging) før de utbetaler tilskudd. Rapporten skal overbevise om at prosjektet er reelt og i gang.

**Rapporten skal dekke:**
- Konkret fysisk arbeid utført i kjeller og 1. etasje (se arbeidslogger)
- Parallell prosjektering og myndighetsbehandling
- Fremdrift mot rammesøknad, IG og byggestart
- Brannkonsept og brannsikkerhet i byggefasen

**Relevante kilder:** `bakgrunn/nye/arbeid_kristian.txt`, `bakgrunn/nye/arbeid_ole_morten.txt`, `historikk.md`, `referat/`, `bakgrunn/`

**Merk:** Se T60 for den allerede leverte brannvesen-rapporten fra april 2026 (`leveranser/fg30_arbeidsrapport.md`), som kan tjene som strukturmal.

---

### T02 `[ ]` Utbetalingsanmodning – Kulturminnefondet
**Mottaker:** Kulturminnefondet (750 000 kr)

Har gitt tilskudd for lenge siden og er utålmodig. Krav om at fysisk arbeid dokumenteres før utbetaling. De siste 6 månedene har det faktisk blitt utført fysisk arbeid (se `arbeid_kristian.txt` og `arbeid_ole_morten.txt`). Anmodningen må:
- Dokumentere konkret hva som er gjort
- Overbevise om at prosjektet realiseres
- Vise klar fremdriftsplan fremover

---

### T03 `[ ]` Framdriftsrapport – Kulturminnefondet
**Mottaker:** Kulturminnefondet

Se T02 for kontekst. Samme krav, men fokus på fremdrift fremover snarere enn utbetalingsanmodning.

---

### T04 `[ ]` Utbetalingsanmodning – Byantikvaren
**Mottaker:** Byantikvaren (500 000 kr)

Samme situasjon som Kulturminnefondet (T02). I tillegg er Byantikvaren særlig opptatt av steinmuren i kjeller – rammesøknaden foreslår å bevare muren, men støype betong foran den for bæring. Anmodningen bør adressere dette direkte og vise at antikvariske verdier ivaretas.

---

### T05 `[ ]` Framdriftsrapport – Byantikvaren
**Mottaker:** Byantikvaren

Se T04 for kontekst.

---

### T06 `[ ]` Utbetalingsanmodning / framdriftsrapport – Enova
**Mottaker:** Enova

Støtteordning for energitiltak. Les `../stotte`-prosjektet for å forstå hvordan støtten er registrert og hvilke krav som gjelder for framdriftsrapportering.

---

### T07 `[ ]` Framdriftsrapport / redegjørelse – Trondheim Brannvesen / TBRT
**Mottaker:** Trondheim Brannvesen / TBRT

TBRT har ilagt dagbøter på 2 000 kr/dag, noe vi bestrider som lovstridig. Prosjektet har tatt tid fordi bygget er komplekst og økonomi har vært usikker. Nå er prosjektet konkret: rammesøknad levert 12. mai. Kommunikasjon mot TBRT skal:
- Dokumentere konkret framdrift
- Vise at prosjektet faktisk blir noe av
- Argumentere for at dagbøter ikke bør løpe i mellomtiden (de vil ellers kunne velte prosjektøkonomien)

---

### T08 `[ ]` Framdriftsrapport – Stiftelsen UNI
**Mottaker:** Stiftelsen UNI

---

### T09 `[x]` Oversikt støttemidler – Bank
**Mottaker:** Bank

Trenger en samlet oversikt over alle innvilgede tilskudd og finansieringskilder for å dokumentere prosjektøkonomi. Bruk `../stotte`-prosjektet som kilde for tall. I stotte prosjektet er det også definert struktur og datamodell for prosjekter som er støttet. Dette må forstås, og stotteprosjekter sine "datablad" må formatteres likt. Det bør ligge inn under en ny mappe "stotte".

**Løsning (2026-06-22):**
- Opprettet `stotte/` mappe i prosjektet
- `stotte/schemes.csv` – scheme-definisjoner for KMF, BYA, UNI og ENOVA_KART
- `stotte/project_cards.json` – tilskuddskort i samme format som `../stotte/project_cards.json`, med én entry per tilskudd: KMF-FG30, BYA-FG30, UNI-FG30, ENOVA-KL-FG30, ENOVA-OM-FG30
- `leveranser/fg30_stoetteoversikt_bank.md` – bankfokusert oversikt (Pandoc-klar Markdown → .docx) med tilskuddstabell, forklaring av utbetalingsmekanismen, finansieringsplan og framdriftsplan
- Samlet innvilget: 2 250 000 NOK (KMF 750 000 + BYA 500 000 + UNI 100 000 + Enova 900 000)

---

### T10 `[ ]` Rapport til HRP om støtteordninger som EK
**Mottaker:** HRP (rådgivende ingeniørfirma)
**Filnavn:** `hrp_brev_stoetteordninger_ek.md`

**Bakgrunn:** HRP er rådgivende ingeniørfirma som jobber på Fjordgata 30-prosjektet. De sender fakturaer til KodeWorks Eiendom og forventer betaling innen normale forfallsfrister (typisk 30 dager).

**Problemet:** Prosjektet finansieres delvis gjennom tilskudd (støtteordninger) fra bl.a. Kulturminnefondet, Byantikvaren, Enova og Stiftelsen UNI. Disse tilskuddene fungerer i praksis som egenkapital (EK) i prosjektet – de utbetales ikke på forhånd, men utløses av dokumentert, gjennomført arbeid. Det betyr at prosjektet ikke har likviditeten til å betale leverandørfakturaer på normale vilkår: pengene eksisterer ikke til tilskuddene er utbetalt, og tilskuddene utbetales etter at arbeid er dokumentert og anmodning er sendt.

**Rapporten skal:**
1. Forklare prosjektets finansieringsstruktur – at tilskudd er EK, ikke driftslikviditet
2. Vise konkret hvilke tilskudd som er innvilget, fra hvem, og når de kan forventes utbetalt (se `../stotte` og prosjektets tilskuddsoversikt)
3. Forklare at HRP – som en sentral samarbeidspart – må akseptere utsatte betalingsfrister i takt med at tilskudd utbetales
4. Understreke at dette er en midlertidig situasjon knyttet til prosjektets oppstartsfase, og at betalingsevne vil bedre seg etter hvert som rammesøknad behandles og IG-søknad leveres (T12)
5. Gi HRP nok trygghet til å fortsette arbeidet uten at forholdet forringes

**Relevante kilder:** `status.txt`, `../stotte`, møtereferater i `referat/`, `bakgrunn/`
**Format:** Brev/rapport på norsk, Pandoc-klar Markdown → `.docx`

---

### T11 `[x]` Rammesøknad minilager
Levert 12. mai 2026.

---

### T12 `[ ]` Igangsettingssøknad (IG)
Planlegges parallelt med byggesaksbehandling av rammesøknad. Inkluderer: detaljert brannplan, fundamentering, ventilasjon, fasader, dekker, etasjeoppretting. Estimert leveranse ca. 3,5 mnd etter rammesøknad.

---

### T13 `[x]` Forberedelsesdokument til møte med TBRT
Lag dokument som forbereder møtet: agenda, argumenter mot dagbøter, framdriftsbevis. Se T07 for kontekst om dagbøter og vår posisjon.

**Løsning (2026-06-11):** Dokument lagt inn av Eirik: `bakgrunn/2026-06-11 forberedelse til  TBRT statusmøte.txt`

---

### T14 `[x]` Referat fra møte med TBRT
Transcription finnes – lag formelt referat fra denne.

**Løsning (2026-06-17):** Referat skrevet fra transcript.srt: `referat/tbrt/2026-06-11_referat_statusmote_tbrt.md`. Dekker: status på alle tre avvik, avvikling av drift, rammesøknad, IG-plan, selskapsstruktur, tvangsmulkt-strategi (TBRT anbefaler å klage på 3. gangs innkreving for å kjøpe tid), og dokumentasjonsliste KodeWorks skal levere innen ca. 18. juni 2026. Transcription er halvdårlig/upresis. Vi må berike møtereferatet på bakgrunn av de øvrige bakgrunnsdokumentene. Spør hvis du er usikker på noen berikelser. Renskriv, lagre som .md. Du ser i transcript at det er navngitte personer som sier ting.
SPEAKER_00 = Eirik Larsen, KodeWorks Eiendom AS
SPEAKER_04 = Morten Knutsen, TBRT
Speaker_01 = anna-karin hermansen, TBRT
Speaker_02 = Tove-Kristin Reitan, TBRT
Speaker_03 = Ole Morten Lagmannssveen, HRP

---

### T15 `[ ]` Dokumentere arbeidsøkter med studenter
Lag rapport/logg over hva studentene har gjort og lært.

---

### T16 `[ ]` Legge inn bilder i rapporter
Bilder skal inn i arbeidsrapport og evt. framdriftsrapporter.

---

### T18 `[x]` Lag kronologisk prosjekthistorikk
**Filnavn:** `historikk.md`

**Løsning (2026-06-18):** `historikk.md` opprettet i prosjektets rotmappe. Dekker bygningens tidlige historie fra 1841, alle daterte prosjekthendelser fra 2022 til 11. juni 2026, og en eksplisitt seksjon for udokumenterte hendelser med manglende dato (kjøp av bygget, KMF/UNI/Enova-vedtaksdatoer, m.fl.). Kilder: alle filer i `bakgrunn/`, alle statusmøtereferater (01–05 + TBRT), arbeidslogger (`arbeid_kristian.txt`, `arbeid_ole_morten.txt`), DNB-verdivurdering 2022, rammetillatelse 28.11.2023, rapport til TBRT 2025.

Lag en kronologisk fremstilling av Fjordgata 30-prosjektet fra start til i dag, basert på bakgrunnsmaterialet i `bakgrunn/` og referatene i `referat/`. Dokumentet skal gi en ny leser (bank, støttegiver, advokat) rask oversikt over hva som har skjedd, når, og hvorfor.

**Struktur:** Én seksjon per år (eller naturlig fase), med daterte hendelser som bullets. Dekk minst:
- Kjøp/overtakelse av bygget og tidligste planer
- Søknader om tilskudd – når søkt, når innvilget, beløp og formål (KMF, Byantikvaren, Enova, UNI)
- Arbeidsøkter – når Kristian og/eller Ole Morten har utført fysisk arbeid på bygget (se `arbeid_kristian.txt` og `arbeid_ole_morten.txt`)
- Rammesøknad for kontorbygg – når levert, hva den inneholdt, hvorfor den ble skrinlagt
- Omlegging fra kontorbygg til minilager – beslutning og begrunnelse
- TBRT-tilsyn januar 2024, pålegg november 2024, klage mai 2025, klagebehandling september–oktober 2025, innkrevinger mars–juni 2026
- Rammesøknad for minilager levert 12. mai 2026
- Statusmøte TBRT 11. juni 2026

**Udokumenterte hendelser:** Hendelser som nevnes i dokumenter uten at dato eller kilde er kjent, skal likevel tas med i historikken – men merkes eksplisitt med f.eks. «*(dato ukjent – mangler dokumentasjon)*» eller «*(omtalt i [kilde], ingen dato)*». Eksempler på slike hendelser: første kontakt med støttegivere, beslutningen om å kjøpe bygget, tidlige møter med Byantikvaren eller Riksantikvaren, tidligere TBRT-inspeksjoner før 2024. Målet er at historikk.md synliggjør hull i dokumentasjonen slik at de kan tettes.

**Kilder:** `bakgrunn/` (alle filer inkl. `arbeid_kristian.txt`, `arbeid_ole_morten.txt`), `referat/` (alle møtereferater), `CLAUDE.md` for interessentoversikt.

---

### T19 `[ ]` Søk om utsettelse av prosjektperiode – Kulturminnefondet
**Mottaker:** Kulturminnefondet

Prosjektperioden i KMF-tilskuddet løper ut, men prosjektet er ikke ferdigstilt. Det er nødvendig å sende en formell søknad om forlengelse. Brevet skal:
- Forklare årsaken til forsinkelsen (komplekst bygg, prosjektet endret fra kontorbygg til minilager, tid brukt på planlegging og myndighetsdialog)
- Dokumentere at prosjektet nå er konkret: rammesøknad levert 12. mai 2026
- Angi ny forventet ferdigstillelsesdato
- Relatert: T20 (støtteintensitet) bør avklares samtidig

---

### T20 `[ ]` Søk om endring av støtteintensitet – Kulturminnefondet
**Mottaker:** Kulturminnefondet

Det opprinnelige tilskuddet ble gitt til et kontorbygg-prosjekt. Prosjektet er nå omlagt til minilager. Dette påvirker prosjektets kostnadsbasis og formål. KMF må informeres og eventuelt godkjenne endringen. Brevet skal:
- Informere om omleggingen fra kontorbygg til minilager
- Argumentere for at prosjektets antikvariske kjerneformål (bevaring av bærekonstruksjon, trekonstruksjoner, fasade) er uendret
- Be om bekreftelse på at tilskuddet fortsatt gjelder, og eventuelt be om justering av støtteintensitet
- Løses helst i samme brev/prosess som T19

---

### T21 `[ ]` Søk om utsettelse av prosjektperiode – Byantikvaren
**Mottaker:** Byantikvaren

Samme situasjon som KMF (T19). Prosjektperioden for Byantikvaren-tilskuddet (500 000 kr) må forlenges. Se T19 for kontekst om årsaker. I tillegg bør brevet adressere steinmur-spørsmålet fra rammesøknaden slik at Byantikvaren er oppdatert på prosjektets nåværende form.

---

### T22 `[ ]` Søk om utsettelse – Enova Ombrukskartlegging
**Mottaker:** Enova

Ombrukskartleggingen ble innvilget støtte og skulle gjennomføres av HRP. Per Statusmøte 03 (mars 2026) var HRP klar til å starte i uke 12. Status på gjennomføring er ukjent – avklar med HRP om kartleggingen er ferdig, delvis gjennomført, eller ikke startet. Dersom prosjektperioden utløper før levering, send søknad om utsettelse til Enova.

---

### T23 `[ ]` Søk om utsettelse – Enova Energikartlegging
**Mottaker:** Enova

Energikartleggingen gjennomføres av HRP (RiEn-avdeling). Per Statusmøte 04/05 var RiEn i gang, med planlagt statusoppsummering 17. april 2026. Avklar med HRP om rapport er levert. Dersom prosjektperioden utløper før rapport er klar, send søknad om utsettelse til Enova.

---

### T24 `[ ]` Lag oversikt over alle støtteordninger
**Format:** Dokument/tabell, egnet for intern bruk og som vedlegg til bank (se T09)

Lag en strukturert oversikt over samtlige innvilgede tilskudd med følgende kolonner:
- Støttegiver
- Prosjektnavn (slik det er registrert hos støttegiver)
- Innvilget beløp
- Støtteintensitet (% av kostnad)
- Prosjektperiode (fra–til)
- Kort beskrivelse av hva vi skal gjøre i prosjektet
- Status (aktiv / søkt utsettelse / utbetalt)

Bruk `../stotte`-prosjektet som kilde for tall. Lagres som `stoetteoversikt.md` i prosjektmappen.

---

### T31 `[x]` Klage på alle tre innkrevinger av tvangsmulkt
**Mottaker:** Trøndelag brann- og redningstjeneste IKS  
**Filnavn:** `tbrt_klage_innkrevinger_2026.md`

**Kronologi:**

| Dato | Hendelse | Saksnr / kilde |
|---|---|---|
| 11.01.2024 | TBRT-tilsyn gjennomført | 24/1007-2 |
| 24.01.2024 | Tilsynsrapport – tre avvik dokumentert | 24/1007-2 |
| 15.02.2024 | Frist for å lukke avvik iht. tilsynsrapporten | 24/1007-2 |
| 18.03.2024 | Gjentatt varsel om pålegg fra TBRT | Bekreftet i pålegget 08.11.2024 |
| 05.03.2024 | KodeWorks sender forpliktende handlingsplan | Bekreftet i pålegget 08.11.2024 |
| 04.11.2024 | Statusmøte – avvik fortsatt ikke lukket | Bekreftet i pålegget 08.11.2024 |
| 08.11.2024 | Pålegg om brannsikring, frist 01.05.2025 | 24/1007-27 |
| 28.04.2025 | Møte mellom KodeWorks og TBRT – status gjennomgått | Bekreftet i vedtaket 07.05.2025 |
| 07.05.2025 | Vedtak om tvangsmulkt: 2 000 kr/dag fra 01.01.2026 | 24/1007-28 |
| 26.05.2025 | KodeWorks klager på vedtaket (forvaltningsloven § 28) | 24/1007-28 |
| 16.09.2025 | TBRT sender saksfremlegg til klageorganet – anbefaler å opprettholde vedtaket | 24/1007-33 |
| 30.09.2025 | Klageorganet behandler saken, opprettholder vedtaket | Protokoll vedlagt orientering 08.10.2025 |
| 08.10.2025 | TBRT orienterer KodeWorks om klageorganets vedtak | Bekreftet i krav om ny behandling 09.10.2025 |
| 09.10.2025 | KodeWorks krever ny behandling – mangelfull begrunnelse (forvaltningsloven §§ 25, 34, 41) | 24/1007-28 |
| 30.12.2025 | KodeWorks sender statusbrev – beskriver utført arbeid og planlagt forprosjekt | Bekreftet i TBRT-brev 06.01.2026 |
| 06.01.2026 | TBRT innvilger ny frist til 28.02.2026. Dagmulkt løper fra 01.03.2026 | 24/1007-40 |
| 27.02.2026 | KodeWorks orienterer om minilager-planer og fremdrift på rammesøknad | `2026-02-27_status_fjordgata30.md` |
| 06.03.2026 | Telefonsamtale mellom KodeWorks og TBRT | Bekreftet i TBRT-brev 18.03.2026 |
| 13.03.2026 | KodeWorks sender e-post til TBRT | Bekreftet i TBRT-brev 18.03.2026 |
| 18.03.2026 | TBRT avslår ytterligere utsettelse – mener ingen konkrete tiltak er gjennomført | 24/1007-44 |
| 19.03.2026 | 1. innkreving SENDT (periode 01.03–18.03.2026, kr 36 000) | 24/1007-45 |
| 17.04.2026 | 2. innkreving SENDT (periode 19.03–14.04.2026, kr 54 000) | 24/1007-46 |
| 11.05.2026 | KodeWorks varsler TBRT uformelt om at rammesøknad er klar og vil bli levert | TBRT skriver feilaktig «11.05.2025» i 3. innkreving – bekreftet av KodeWorks at dette er 2026 |
| 12.05.2026 | Rammesøknad for minilager levert til Plan og Bygg | Bekreftet i referat 11.06.2026 |
| 03.06.2026 | 3. innkreving SENDT (periode 15.04–31.05.2026, kr 94 000) | 24/1007-52 |
| 11.06.2026 | Statusmøte KodeWorks / HRP / TBRT | `referat/tbrt/2026-06-11_referat_statusmote_tbrt.md` |

**Formell struktur – tre separate klager i ett brev**

Hvert innkrevingsvedtak er et selvstendig enkeltvedtak med eget saksnummer. Forvaltningsloven § 51, 4. ledd gir særskilt klagerett på den enkelte «ileggelse». Alle tre må påklages separat, men kan samles i ett brev som eksplisitt angir at man klager på sak 24/1007-45, 24/1007-46 og 24/1007-52.

**Klagefrist og status (per 17.06.2026)**

| Innkreving | Sendt | Frist ca. | Status |
|---|---|---|---|
| 1. (01.03–18.03.2026) | 19.03.2026 | ~09.04.2026 | **Frist brutt** – 10 uker siden |
| 2. (19.03–14.04.2026) | 17.04.2026 | ~08.05.2026 | **Frist brutt** – 6 uker siden |
| 3. (15.04–31.05.2026) | 03.06.2026 | ~24.06.2026 | **Ikke brutt** – hastverk |

Fristen er 3 uker fra mottaksdato, jf. forvaltningsloven §§ 29 og 51, 4. ledd. Bekreftet av TBRTs juridiske rådgiver i møtet 11.06.2026.

**Strategi for fristbrutte klager (innkreving 1 og 2)**

Forvaltningsloven § 31 åpner for behandling av for sent inngitte klager dersom:
- **a)** parten ikke kan lastes for å ha oversittet fristen, eller
- **b)** det av særlige grunner er rimelig at klagen prøves

Klagen må fremsettes «uten ugrunnet opphold» etter at hindringen er falt bort.

Argumenter som begrunner sen klage:
1. KodeWorks var i perioden mars–mai 2026 i aktiv konstruktiv dialog med TBRT og fokuserte på å levere rammesøknaden (12. mai) som den faktiske løsningen – ikke på å angripe innkrevingene juridisk. En part som aktivt forsøker å løse saken bør ikke straffes for å ikke simultant ha klaget innen fristen.
2. Rammesøknaden forelå ikke da fristene for innkreving 1 og 2 løp ut – det er et vesentlig nytt faktum som er «særlige grunner» etter § 31 b).
3. KodeWorks er en liten eiendomseier uten heltids juridisk stab; TBRT har juridisk rådgiver i fast stilling. Strukturell asymmetri taler for at fristen bør praktiseres med rimelighet (jf. EMK artikkel 6).
4. Alle tre innkrevingene springer ut av det samme vedtaket og den samme situasjonen – prosessøkonomisk og konsistensmessig bør de ses i sammenheng.
5. TBRT signaliserte i møtet 11.06.2026 at de vil vurdere å sette innkreving i bero – vanskelig å begrunne velvilje fremover uten å revurdere de to allerede innkrevde periodene.

Subsidiært: Be TBRT omgjøre innkrevingene 1 og 2 på eget initiativ etter forvaltningsloven **§ 35** (omgjøring uten klage til gunst for parten).

**Brevets fire elementer:**
1. Formell klage på 3. innkreving (innen fristen – hastverk)
2. Klage på 1. og 2. innkreving med anmodning om behandling til tross for fristoverskridelse (§ 31)
3. Subsidiær anmodning om omgjøring av 1. og 2. innkreving etter § 35
4. Anmodning om utsatt iverksetting av alle tre etter § 42 mens klagebehandling pågår

**Materielle argumenter i klagen:**
- Rammesøknad levert 12. mai 2026 – prosjektet er nå konkret og i gang
- Krav om ny behandling (09.10.2025) ikke tilfredsstillende besvart
- Sprinklerinstallasjon i verneklasse B-bygg er rettslig umulig uten byggetillatelse og Byantikvarens godkjenning – TBRT setter KodeWorks i en umulig skvis mellom to offentlige myndigheter
- Brannforskriften § 6 (risikobasert tilnærming for eldre bygg) er ikke vurdert av TBRT
- Faktafeil i saksfremlegget (16.09.2025): TBRT hevdet at ingen byggesøknad var innlevert
- Tvangsmulkt som kan velte prosjektøkonomien hindrer den brannsikkerhetsoppgraderingen TBRT selv krever (forholdsmessighetsprinsippet, EMK TP1 art. 1)
- Fortsatt innkreving bør stilles i bero frem til klagebehandling er avsluttet

**Relevante kilder:**
- `bakgrunn/2025-05-07_vedtak_tvangsmulkt.md`
- `bakgrunn/2025-05-26_klage_vedtak_tvangsmulkt.md`
- `bakgrunn/2025-09-16_saksfremlegg_klageorgan_tbrt.txt`
- `bakgrunn/2025-10-09_krav_om_ny_behandling.md`
- `bakgrunn/2026-01-06_tbrt_svar_ny_frist.txt`
- `bakgrunn/2026-02-27_status_fjordgata30.md`
- `bakgrunn/2026-03-18_tbrt_svar_ingen_ytterligere_utsettelse.txt`
- `bakgrunn/2026-03-19_1gangs_innkreving_tvangsmulkt.md`
- `bakgrunn/2026-04-17_2gangs_innkreving_tvangsmulkt.md`
- `bakgrunn/2026-06-03_3gangs_innkreving_tvangsmulkt.md`
- `bakgrunn/lovverk/` (alle filer)

---

### T32 `[ ]` Fisjon av KodeWorks Eiendom AS
**Ansvarlig:** Eirik / regnskapsfører / advokat

KodeWorks Eiendom AS eier i dag både Fjordgata 30 og Grønnegata 10. Selskapet skal fisjoneres slik at:
- **Fjordgata 30 AS** (nytt orgnummer) overtar eierskapet til Fjordgata 30 og blir juridisk byggherre for ombyggingen
- **KodeWorks Eiendom AS** beholder dagens orgnummer og eier Grønnegata 10
- Grønnegata 10 kan skilles ut som et tredje selskap ved behov

Alle pågående støtteordninger (KMF, Byantikvaren, Enova, UNI) skal overføres til Fjordgata 30 AS. Banklån søkes i Fjordgata 30 AS. Fisjonen bør gjennomføres før IG-søknad leveres (T12) slik at riktig juridisk enhet er byggherre fra starten.

---

### T33 `[ ]` Utred og dokumenter MVA-refusjon for minilager
**Filnavn:** `mva_minilager_redegjoerelse.md`

Under bygging av Fjordgata 30 til minilager vil det påløpe MVA på bygge- og prosjekteringskostnader. MVA kan kreves refundert dersom bygget ved ferdigstillelse leies ut til en MVA-pliktig leietaker. Dette er ikke automatisk – utleie av fast eiendom er i utgangspunktet unntatt MVA, men det finnes unntak for lagring og visse tilknyttede tjenester.

**Dokumentet skal:**
1. Redegjøre for regelverket: når er utleie av lagerplass MVA-pliktig (mval. § 3-11 og unntakene)
2. Identifisere hvilke leietakermodeller som kvalifiserer – f.eks. aktører som tilbyr logistikktjenester med henting hos kunder, app-baserte lagertjenester (fulfilment), kurerbedrifter el.l.
3. Sannsynliggjøre at Fjordgata 30 AS vil leie ut til slike MVA-pliktige aktører – konkrete eksempler og forretningsmodell
4. Beskrive frivillig registrering i MVA-registeret for utleier (Fjordgata 30 AS) som forutsetning for fradragsrett
5. Beregne estimert MVA-beløp som kan refunderes basert på prosjektbudsjett

**Hent bakgrunnsmateriale fra:** Skatteetaten, Merverdiavgiftsloven, eventuelt skatterådgiver/advokat med MVA-kompetanse.

---

### T44 `[ ]` Dokumenter relevant lovverk – MVA ved utleie av lagerplass
**Mappe:** `bakgrunn/lovverk/`
**Filnavn:** `bakgrunn/lovverk/mva_lagerplass.md`

Hent inn og dokumenter relevant lovverk og praksis knyttet til MVA ved utleie av lagerplass, med særlig fokus på de spørsmålene som er relevante for Fjordgata 30. Dokumentet skal dekke:

1. **Hovedregelen** – utleie av fast eiendom er unntatt MVA (mval. § 3-11)
2. **Unntakene** – når blir lagertjenester/utleie av lager MVA-pliktig (typisk når utleier tilbyr aktive tjenester som henting, pakking, logistikk)
3. **Minilager-modellen** – er ren selvbetjent lagerplass unntatt? Hva kreves for MVA-plikt?
4. **Utleie til tjenesteleverandør** – hva hvis leietaker driver en fulfilment-tjeneste, kurerservice e.l.? Endrer dette MVA-statusen?
5. **Leietaker som ikke finnes enda** – kan frivillig registrering (mval. § 2-3) gjøres før leietaker er på plass? Hvilke krav stilles til dokumentasjon av fremtidig MVA-pliktig bruk?
6. **Frivillig registrering** – vilkår, prosess, konsekvenser for fradragsrett på bygge- og prosjekteringskostnader
7. **Relevante rettskilder** – lovtekst, Skattedirektoratets bindende forhåndsuttalelser (BFU), Merverdiavgiftshåndboken

**Avhenger av / relatert til:** T33 (MVA-redegjørelse for minilager)

---

### T59 `[ ]` Gjennomgå og innarbeid bakgrunnsfiler fra rot

Fire filer er flyttet fra prosjektroten til `bakgrunn/nye/` for gjennomgang:

| Fil | Innhold |
|---|---|
| `ai_feedback.txt` | Tilbakemeldinger fra AI-verktøy brukt underveis i prosjektet |
| `arbeid_kristian.txt` | Arbeidslogg for Kristian Brandsegg |
| `arbeid_ole_morten.txt` | Arbeidslogg for Ole Morten Lagmannssveen |
**Hva som skal gjøres per fil:**
- `arbeid_kristian.txt` og `arbeid_ole_morten.txt`: Vurder om innholdet er innarbeidet i `historikk.md`. Arbeidsloggene er allerede kildehenvist som `[^52]`. Dersom innholdet er dekket, konverter til `.md` og behold i `bakgrunn/nye/` eller flytt til `bakgrunn/`.
- `ai_feedback.txt`: Vurder om noe av innholdet bør innarbeides i prosjektdokumentasjon. Slett hvis innholdet er foreldet.

**Merk:** `fg30_arbeidsrapport.md` er skilt ut til T60.

**Avhengigheter:** Ingen.

---

### T60 `[x]` Gjennomgå og ferdigstill brannvesen-rapport (leveranser/fg30_arbeidsrapport.md)

Rapport sendt til TBRT/brannvesenet ca. 20. april 2026. Filen er konvertert fra `.docx` og har formateringsfeil fra konverteringen. Filen ligger nå i `leveranser/fg30_arbeidsrapport.md`.

**Hva som skal gjøres:**
1. Les hele filen og identifiser alle konverteringsartefakter (stray `<`-tegn, ødelagte avsnitt, manglende mellomrom)
2. Regenerer titler og formatering der det er nødvendig
3. Behold `\newpage`-kommandoer (gyldige for Pandoc → .docx)
4. Verifiser at innholdet samsvarer med det som faktisk ble sendt

**Kjente feil (oppdaget ved opprettelse av tasken):**
- Linje 19: `---<` skal være `---`
- Linje 33: `<som er gjennomført` skal være `som er gjennomført`

**Avhengigheter:** Ingen.

**Løsning (22.06.2026):** Filen gjennomgått i sin helhet. Kun de to kjente konverteringsartefaktene funnet og rettet. Øvrig formatering er korrekt — overskriftshierarki, tabeller og `\newpage`-kommandoer er gyldige og intakte. Filen ble samtidig flyttet fra `bakgrunn/nye/` til `leveranser/`.

---

### T61 `[~]` Populer project_cards.json med primærkildedata for alle tilskudd

**Mål:** `stotte/project_cards.json` skal ha alle felt utfylt fra primærkilder (tilsagnsbrev, søknader, budsjett-xlsx) – ikke fra historikk.md. For hvert prosjektkort: GrantReference, TotalBudget, SupportIntensity, DurationFrom/To, ReportingDates (med datoer og krav), PaymentDates (med triggere og krav), UsageConstraints (eligible/ineligible), SpecialRules.

**Arbeidsregel:** Tilsagnsbrev og budsjettdokumenter er primærkilder. historikk.md er ikke kilde. Kopier kun .txt-filer (ikke PDF) til `bakgrunn/stotte/`.

---

#### Status per 2026-06-22

**KMF-FG30** `[x]` Ferdig

Kilde: `bakgrunn/stotte/kmf_tilsagnsbrev.txt`, `kmf_soeknad_ordinaer.txt`, `kmf_tilbakemelding_20240206.txt`, estimat-filer.

Oppdaterte felt:
- `GrantReference`: `240126`
- `TotalBudget`: `5000000` ← fra endelig søknad (kulturminnefondet_2.txt). **NB: ikke oppdatert ennå i project_cards.json – gjenstår.**
- `GrantAmount`: `750000` ✓
- `SupportIntensity`: `0.30` ✓
- `DurationFrom`: `2024-03-13` (vedtaksdato), `DurationTo`: null (ikke fastlagt)
- `UsageConstraints.eligible`: fjerne/bevare originale paneler/gulvplater/himlinger, undersøke bærekonstruksjon, skifte søyler/innkassing, reetablere bæresystem, kjøp av håndverkertjenester
- `UsageConstraints.ineligible`: administrasjon/regnskap/planlegging, dugnad/egne maskiner, trykkimpregnerte materialer, kostnader over sluttregnskapet
- `SpecialRules`: KMF-spesifikke krav om materialkvalitet, antikvarisk standard fra BYA, ingen trykkimpregnering
- `Comments`: vedtaksdato 13.03.2024, tilsagnsbrev 18.03.2024, prosjektnr 240126. **Merk: prosjektet er endret fra kontorbygg til minilager – KMF må informeres (T20).**

Kopiert til `bakgrunn/stotte/`:
- `kmf_tilsagnsbrev.txt` (fra `temp/Kulturminnefondet/Kulturminnefondet 1/`)
- `kmf_soeknad_ordinaer.txt` (fra `temp/.../Tilsvar 1/kulturminnefondet_2.txt` – den endelige reviderte søknaden, primærkilde)
- `kmf_tilbakemelding_20240206.txt` (KMFs forespørsel om tilleggsopplysninger)
- `kmf_estimat_rehab_kjeller.txt`, `kmf_estimat_rehab_1etg.txt` (kostnadsestimater)
- Fantes fra før: `kmf_soeknad_sikringstiltak.txt`, `kmf_tilsvar_soeknadssvar.txt`

**Gjenstår for KMF-FG30:** Sett `TotalBudget: 5000000` i project_cards.json (bekreftet fra kmf_soeknad_ordinaer.txt: totalbudsjett 5 000 000 NOK, omsøkt KMF-andel 1 500 000, innvilget 750 000).

---

**BYA-FG30** `[x]` Ferdig

Kilde: `temp/Byantikvaren/Fjordgata 30 - Søknad om tilskudd rehabilitering av bærekonstruksjon(ref. CS0495805).txt` (tilsagnsbrev), `søknad_byantikvaren.txt`, `Vedlegg 1 Akseptskjema tilskudd brygger.txt`.

Oppdaterte felt:
- `GrantReference`: `2025/5928`
- `TotalBudget`: `2285714`
- `GrantAmount`: `500000` ✓ (søkte 750 000, fikk 500 000)
- `SupportIntensity`: `0.219` (500 000 / 2 285 714)
- `DurationFrom`: `2025-06-01`, `DurationTo`: `2025-12-31`
- `ReportingDates[0].DeadlineDate`: `2025-12-01` (primært)
- `UsageConstraints.eligible`: forsterking fundamenter, retting skjevheter, fjerning/dok/tilbakeføring av paneler, utskifting råteskadde søyler/bjelker, stabilisere yttervegger/etasjeskillere
- `UsageConstraints.ineligible`: fasade/vinduer/tak, utredningsoppgaver/pilotprosjekter, allerede utførte arbeider, kostnader over sluttregnskapet
- `SpecialRules`: antikvarisk spesialkompetanse påkrevd, løpende dialog med BYA, solceller på tak krever BYA-godkjenning ved IG-søknad
- `PaymentDates`: utbetalingsanmodning på Vedlegg 2-skjema + rapport + faktura/regnskap → byantikvaren.kart@trondheim.kommune.no

**NB:** Alle PDF-filer i temp/Byantikvaren er allerede konvertert til .txt. De relevante har ikke blitt kopiert til bakgrunn/stotte/ ennå – BYA-dokumentene ligger kun i temp/.

---

**UNI-FG30** `[x]` Ferdig

Kilde: `temp/UNI/UNI 2/Tildeling etter styremøte i Stiftelsen UNI.txt`, `Budsjett.xlsx`.
**NB:** `temp/UNI/UNI 1/` er en avslått søknad – irrelevant. Ignorer UNI 1.

Oppdaterte felt:
- `GrantReference`: `UNI-38702`
- `TotalBudget`: `1785000` (hele prosjektbudsjettet fra Budsjett.xlsx: kun «Planlagte kjøp av tjenester» = 1 785 000; alle andre poster = 0)
- `GrantAmount`: `100000` ✓
- `SupportIntensity`: `0.056` (100 000 / 1 785 000) – den gamle verdien 0.15 var feil
- `DurationFrom`: `2024-06-30` (søknadsdato)
- `ProjectName`: rettet til «brannsikring» (formålet er brannsikring, ikke generell restaurering)
- `UsageConstraints.eligible`: brannsikring, sprinkelanlegg, rømningsveier, brannskiller
- `UsageConstraints.ineligible`: dugnad, egne maskiner/materialer, lønn egne ansatte
- `SpecialRules`: utbetaling krever revisor/regnskapsfører-bekreftelse; rapportering via søknadsportal («Be om utbetaling»)
- `ReportingDates`: sluttrapport via søknadsportal, automatisk tilsendt 3 år etter oppstart
- `PaymentDates`: forutsetning – hele prosjektet (1 785 000) finansieres og ferdigstilles; styrevedtak 28.08.2024, brev 03.09.2024

Kopiert til `bakgrunn/stotte/`:
- `uni_tildeling.txt` (fra `temp/UNI/UNI 2/Tildeling etter styremøte i Stiftelsen UNI.txt`)
- `uni_anbefaling.txt` (fra `temp/UNI/UNI 2/Fjordgata+30+-+anbefaling+av+søknad+om+tilskudd.txt`)
- Fantes fra før: `uni_soeknad.txt`

**NB:** `temp/UNI/UNI 2/TilsagnsbrevFastKulturminne (6) (2).txt` er KMFs tilsagnsbrev, ikke et UNI-dokument – ble lagt ved som vedlegg i UNI 2-søknaden.

---

**ENOVA-KL-FG30** `[~]` Påbegynt – ingen tilsagnsbrev tilgjengelig

Kilde: `temp/Enova/Energikartlegging i Yrkesbygg/webskjema.txt` (søknad), `bakgrunn/stotte/hrp_energikartlegging_rapport.md` (ferdig rapport).

Det finnes **ingen tilsagnsbrev eller budsjett-xlsx** for energikartleggingen i temp-mappen. GrantAmount 500 000 NOK er kun kilde historikk.md – ikke verifisert fra primærkilde.

Kjente fakta fra søknad:
- Leverandører: Sastech (energianalyse/rapport), HRP (teknisk gjennomførbarhet), SAHAA (arkitektur), Astra Bygg (kostnadsestimat)
- Ferdigstillelse: innen 8 måneder fra vedtaksdato
- Rapportering: Enovas søknads- og rapporteringssenter
- Alle kostnader er kjøp av rådgivningstjenester

Kjente fakta fra ferdig rapport (HRP, 05.05.2026):
- Energikartleggingsrapporten er **ferdigstilt** (befaring 30.03.2026)
- Utarbeidet iht. Enovas krav og NS 3031:2025
- HRP prosjektnr: 2612200

Gjenstår:
- Finn tilsagnsbrev fra Enova (sjekk Enovas søknadsportal – der ligger referanse og vedtaksdato)
- Oppdater: GrantReference, TotalBudget, DurationFrom, DurationTo
- Legg til UsageConstraints: kjøp av rådgivningstjenester til energikartlegging iht. NS 3031
- Oppdater ReportingDates: rapport ferdig 05.05.2026, klar for innlevering

---

**ENOVA-OM-FG30** `[ ]` Ikke startet

Kilde: `temp/Enova/Mulighetsstudie ombruk og Fleksibilitet/` – inneholder:
- `Mulighetsstudie for ombruk og fleksibilitet _ Enova.txt` (søknad/prosjektbeskrivelse)
- `Vilkår for støtte til Mulighetsstudie.txt` (vilkårsdokument – primærkilde for krav)
- `webskjema.txt` (søknadsskjema)
- `Budsjett ombruk.xlsx` (budsjett – skal leses med openpyxl via `uv run python3`)

Fantes fra før i `bakgrunn/stotte/`: `enova_soeknad_ombrukskartlegging.md`

Kjent: GrantAmount 400 000 NOK (kun fra historikk.md), ferdigstillelse innen 10 måneder fra vedtaksdato.

---

#### Kjente mangler på tvers av alle kort

| Prosjekt | Mangler |
|----------|---------|
| KMF-FG30 | `TotalBudget: 5000000` ikke skrevet inn ennå |
| BYA-FG30 | Dokumenter ikke kopiert til bakgrunn/stotte/ (ligger kun i temp/) |
| ENOVA-KL-FG30 | Tilsagnsbrev mangler – GrantReference og DurationFrom ukjent |
| ENOVA-OM-FG30 | Ikke påbegynt – les alle dokumenter i temp/Enova/Mulighetsstudie |

#### Verktøy
- Excel-lesing: `uv run python3 -c "import openpyxl; ..."` (openpyxl er installert i uv-miljøet)
- PDF→tekst: `pdftotext -layout "fil.pdf" - > fil.txt`
- DOCX→tekst: `pandoc -t plain fil.docx -o fil.txt`
