# Fjordgata 30 – Oppgaveliste

## Legende
- `[x]` Ferdig
- `[~]` Påbegynt / under arbeid
- `[ ]` Ikke startet

Oppgaver identifiseres med ID på formen **T01**, **T02** osv. Bruk disse ID-ene til å referere til oppgaver i kommunikasjon, commits og dokumentasjon. Løsninger dokumenteres under oppgaven i dette dokumentet.

## Nye oppgaver

### T86 `[ ]` Gjennomgå og strukturer timelister fra HRP

#### Bakgrunn

Ny mappe `timer/` er opprettet med timelister fra HRP. Timelister inneholder personell som ikke er kjent, og arbeid som ikke er bestilt. Vi trenger bedre oversikt.

#### Mål

- Strukturer timelister for oversikt uten å miste informasjon fra beskrivelsene
- Aggreger og grupper på tid og person
- Summer timer per person/kategori
- Konkatener beskrivelser på en lesbar måte
- Lag et forslag til format/script for dette

#### Fremgangsmåte

- Les filene i `timer/`
- Kartlegg personell, arbeidstyper og beskrivelser
- Foreslå aggregeringsstruktur — vurder om dette bør løses som et script eller manuelt i Markdown/CSV

---

### T83 `[ ]` Sammendrag av ../stotte-prosjektet til bruk i stotte/

Les `../stotte/`-repoet (CLAUDE.md, README.md, project_cards.json, project_cards_template.json, kravspek.txt, history-log.md, og relevante filer i src/ og data/) og lag et sammendrag i `stotte/stotte_sammendrag.md`. Sammendraget skal forklare:

- Hva ../stotte-prosjektet er og hvordan det brukes (datamodell, project_cards-format, verktøy)
- Filosofien bak støttekoordinering: hvordan man koordinerer flere støtteordninger mot statsstøtteregelverket for å maksimere samlet støtte
- Kumuleringsprinsippet: når KMF gir 30 %, kan ytterligere 40 % komme fra Byantikvaren, Stiftelsen UNI, Skattefunn, Innovasjon Norge o.l., så lenge samlet intensitet ikke overstiger 70 %-taket
- Hvordan overlapp mellom prosjekter håndteres (samme kostnad kan ikke telles dobbelt, men kan fordeles)
- Praktisk for FG30: hvilke ordninger vi har aktive, hvilke vi vurderer, og hvordan de koordineres

Sammendraget skal være forståelig for en leser uten kjennskap til statsstøtteregelverket (f.eks. KMF-saksbehandler) og brukes som internt referansedokument og grunnlag for vedlegg til støttesøknader.

---

### T84 `[x]` Verifiser at BYA-konverteringer er trofaste (tilsvarende T82 for KMF)

#### Bakgrunn

Samme type konverteringsproblem som ble avdekket i T82 for KMF kan ha rammet BYA-dokumentene. Under T61 (22.06.2026) ble `bya_soeknad.txt`, `bya_tilsagnsbrev.txt`, `bya_akseptskjema.txt` og `bya_utbetalingsskjema.txt` kopiert fra `temp/` og konvertert til .md i `bakgrunn/stotte/bya/`. Det er uklart om konverteringen var trofast eller om innhold ble fjernet/forenklet – de nåværende .md-filene ser «ferdig-formaterte» ut på en måte som minner om den redigerte KMF-søknaden (ikke rå konvertering).

#### Kildefiler og målfiler å sammenlikne

| Kildefil (i `temp/`) | Målfil (`bakgrunn/stotte/bya/`) | Særlig å verifisere |
|---|---|---|
| `bya_soeknad.txt` | `soeknad.md` | Alle seksjoner med? Originalen har trolig mer enn de 7 seksjonene i .md-versjonen (bygningshistorikk, faglig begrunnelse, ev. vedleggsbeskrivelser). Vedleggsliste komplett? |
| `bya_tilsagnsbrev.txt` | `tilsagnsbrev.md` | Alle vilkår og forutsetninger gjengitt fullt ut? |
| `bya_akseptskjema.txt` | `akseptskjema.md` | «Anmodning om sammenslåing»-seksjonen (BYA+KMF+UNI = 1 350 000 kr) – er dette originalt innhold fra skjemaet eller ble det lagt til under konverteringen? |
| `bya_utbetalingsskjema.txt` | `utbetalingsskjema.md` | Alle felt og instruksjoner fra originalskjemaet med? |

#### Fremgangsmåte

- Finn kildefilene: de lå i `temp/Byantikvaren/` (lokal mappe utenfor repoet) – be brukeren bekrefte sti
- Les hver kildefil i sin helhet med Bash (`cat` eller `type`)
- Sammenlign antall hoveddeler, tabeller og detaljer mot .md-versjonen
- Rett eventuelle mangler ved lossless konvertering (jf. T82: bevar alt, ikke omstrukturér, bevar æøå)

#### Avhengigheter

T82 (erfaringer herfra gjelder direkte).

#### Løsning (25.06.2026)

Kildefiler lest fra `../temp/Støtte/Byantikvaren/`. Merk: `Fjordgata 30 - Søknad om tilskudd rehabilitering av bærekonstruksjon(ref. CS0495805).txt` er tilsagnsbrevet (feilnavngitt i temp-mappen); `søknad_byantikvaren.txt` er søknaden.

**soeknad.md** – gjenopprettet:
- Bakgrunn: lagt til tre avsnitt (bygget inngår i bryggerekke, innovasjonshub-fremtidig bruk, fase-strategi for bæring, støttegrad-begrunnelse)
- Tilstand og tiltak: lagt til brannforebyggingsforskriften §8 og brannspredningsrisiko
- Sammenheng: utvidet med TBRT-sitat og TEK17-referanse
- Organisering: lagt til avsnitt om Ole Mortens erfaring fra kulturhistoriske brygger
- Avslutning: hel seksjon gjenopprettet
- Fremdriftsplan (Vedlegg 1): tredje kolonne «Beskrivelse og merknad» gjenopprettet
- Budsjett (Vedlegg 2): «Budsjettprinsipper»-seksjon gjenopprettet

**tilsagnsbrev.md** – gjenopprettet:
- Søknadens omfang: lagt til kontekstparagraf om total søknadsmengde (>12 MNOK søkt, pott 2,2 MNOK) – forklarer hvorfor 500 000 og ikke 750 000 ble innvilget
- Ny seksjon: «Frist for gjennomføring»
- Andre vilkår: utvidet MVA-tekst (inkl. hva som skjer ved statusendring)
- Lagt til vedleggsliste og «Kopi til: Silje Taftø Petersen»

**akseptskjema.md** – rettet:
- Tittel: «Vedlegg 1. Akseptskjema for tilskudd bryggene 2025»
- Seksjonstittel: «Forutsetninger for tilskudd til bygningsmessige tiltak på tak og fasade»
- Lagt til underskriftsfelt («Sted, dato» / «Forpliktende underskrift»)

**utbetalingsskjema.md** – rettet:
- Lagt til fakturainstruks-merknad: anmodningen legges ved den elektroniske fakturaen

---

### T82 `[x]` Rett opp ødelagte KMF-konverteringer og legg inn forhåndskonferanse

#### Hva gikk galt (bakgrunn)

En tidligere runde med .txt→.md-konvertering av KMF-søknadsdokumentene hadde to feil:

1. **Feil kildefil:** Konverteringen brukte `Kulturminnefondet 1.txt` (en eldre eller annen versjon) i stedet for `Tilsvar 1/kulturminnefondet_2.txt` — den endelige, reviderte søknaden som er primærkilden.
2. **Aggressiv konvertering:** Innhold ble fjernet under konverteringen — seksjoner trunkert, æøå-encoding ødelagt, vedleggslister og arbeidspakker delvis slettet. Resultatet i `bakgrunn/stotte/kmf/soeknad_ordinaer.md` var en mangelfull og misvisende gjengivelse av originaldokumentet.

#### Riktig fremgangsmåte (trofast konvertering)

- Les kildefilen i sin helhet med `pdftotext` eller direkte fillesing
- Konverter lossless — ikke forenkle, ikke omstrukturere, ikke fjerne seksjoner som virker utdaterte
- Bevar alt: alle arbeidspakker, budsjett, fremdriftsplan, vedleggslister, æøå-tegn
- Sjekk at resulterende .md inneholder samme antall hoveddeler som kilden

#### Kildefiler for KMF

Hentet fra `temp/Kulturminnefondet/` (lokal temp-mappe utenfor repoet):
- Primærkilde søknad: `Tilsvar 1/kulturminnefondet_2.txt` → `bakgrunn/stotte/kmf/soeknad_ordinaer.md`
- `Kulturminnefondet 1/` inneholder tilsagnsbrev og annet — ikke søknadsteksten
- `Kulturminnefondet 1.txt` er IKKE primærkilden for søknaden — ignorer denne som søknadskilde

#### Løsning (25.06.2026)

**Steg 1 – utført:** `bakgrunn/stotte/kmf/soeknad_ordinaer.md` erstattet med fullstendig trofast konvertering av `kulturminnefondet_2.txt`. Encoding rettet (æøå). Hele «Fremtidig bruk»-seksjonen er med, inkl. kontorplan med fjerning av 3. og delvis 5. etasje og lysinnslipp. Alle fem arbeidspakker, fremdriftsplan, budsjett og alle 11 vedlegg er bevart.

**Steg 2 – ikke utført:** Bruker avklarte at `Kulturminnefondet 1.txt` ikke er interessant og at `soeknad_sikringstiltak.md` kan ignoreres.

**Steg 3 – utført:** `bakgrunn/2023-06-23_forhandskonferanse_presentasjon.md` opprettet fra `forhandskonferanse.txt`. Presentasjon datert 23.06.2023: reguleringsstatus, kulturminnekartet, eksisterende plantegninger (A20-22 t.o.m. A40-14), rammer for utvikling (lyssjakt, åpning til kjeller, fjerning av 3. og 5. etasje), romprogram per etasje for skisseforslaget, og høyder/konstruksjonsdiskusjon.

#### For tilsvarende arbeid med BYA

BYA-kildefilene ble kopiert fra `temp/` til `bakgrunn/stotte/bya/` den 22.06.2026 (se T61 i ARCHIVE.md): `bya_tilsagnsbrev.txt`, `bya_soeknad.txt`, `bya_akseptskjema.txt`, `bya_utbetalingsskjema.txt`. Samme prinsipp gjelder: les kildefilene i sin helhet og konverter lossless til .md — ikke forenkle eller fjerne innhold.

---

### T81 `[ ]` Dokumenter hva som ble gjort med bygget på 1980-tallet

Søk i bakgrunnsdokumentene etter informasjon om hva som faktisk ble gjort under rehabiliteringen etter brannen på 1980-tallet: hvilke tiltak, hvilke materialer, og hvem som utførte arbeidet. Funnene er relevante for å forstå dagens bæresystem (stålbæring, skråavstivere i 3. etasje, betongmur i fundamentering, strekkfisker/stålstag) og for å dokumentere byggets historikk korrekt i rapporter til KMF og Byantikvaren.

**Relevante filer å søke i:** `historikk.md`, `bakgrunn/`-mappen generelt, særlig eiendomsinformasjon, matrikkelen og eventuelle byggesaksarkiver.

---

### T66 `[ ]` Komplett arbeidsøkt-logg – manglende datoer og Ole Mortens rapport

**Mål:** Fylle ut det som mangler i `bakgrunn/2026-06-19_arbeidsokter_kmte.md` slik at alle arbeidsøkter er fullstendig dokumentert med dato og timer.

**Mangler:**
- Eksakte datoer for Kristians Berg 1–4 (vet at de er i 2026 – ber Kristian bekrefte)
- Ole Mortens fullstendige arbeidsøkt-logg med datoer og timer (kalender, HRP-besøk, sweat equity-arbeid)

**Handling:** Be Kristian og Ole Morten sende inn manglende data, deretter oppdatere tabellene i `bakgrunn/2026-06-19_arbeidsokter_kmte.md`.

**Relevante filer:** `bakgrunn/2026-06-19_arbeidsokter_kmte.md`

---

### T01 `[ ]` Arbeidsrapport og utbetalingsanmodning – KMF / UNI / BYA

Alle tre støttegivere krever dokumentasjon på utført fysisk arbeid før utbetaling. Felles kildedokument: `bakgrunn/2026-06-01_arbeidsbeskrivelse.md`. Strukturmal: `leveranser/2026-04-20_fg30_arbeidsrapport.md` (levert til TBRT april 2026).


#### T01.02 `[ ]` Stiftelsen UNI – arbeidsrapport og utbetalingsanmodning
**Mottaker:** Stiftelsen UNI (100 000 kr, ref UNI-38702)

Tilskuddet gjelder brannsikring. Rapporten må:
- Dokumentere framdrift på brannsikringstiltak (kilde: `bakgrunn/2026-06-01_arbeidsbeskrivelse.md`, brannkonsept)
- Vise plan for sprinkelanlegg og rømningsveier
- Utbetaling krever revisor/regnskapsfører-bekreftelse; anmodes via søknadsportalen («Be om utbetaling»)

#### T01.03 `[ ]` Byantikvaren – arbeidsrapport og utbetalingsanmodning
**Mottaker:** Byantikvaren (500 000 kr, saksnr 2025/5928)

BYA er særlig opptatt av steinmuren i kjeller. Anmodningen må:
- Dokumentere utført fysisk arbeid med antikvarisk relevans (kilde: `bakgrunn/2026-06-01_arbeidsbeskrivelse.md`)
- Adressere steinmur-spørsmålet direkte: rammesøknaden foreslår bevaring med betong foran for bæring
- Vise at antikvariske verdier ivaretas gjennom hele prosessen
- Fylle ut Vedlegg 2-skjema + rapport + faktura/regnskap → byantikvaren.kart@trondheim.kommune.no

---

### T02 `[ ]` Utbetalingsanmodning – Kulturminnefondet
**Mottaker:** Kulturminnefondet (750 000 kr)

Har gitt tilskudd for lenge siden og er utålmodig. Krav om at fysisk arbeid dokumenteres før utbetaling. De siste 6 månedene har det faktisk blitt utført fysisk arbeid (se `2026-04-16_arbeid_kristian.txt` og `2026-04-16_arbeid_ole_morten.txt`). Anmodningen må:
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

### T05 `[x]` Framdriftsrapport – Byantikvaren
**Mottaker:** Byantikvaren

Se T04 for kontekst.

**Løst 2026-06-25:** `stotte/2026-06-25_bya_framdriftsrapport.md`. Dekker: bygningshistorikk, prosjektteam med kulturminneansvarlig (HRP/Ole Morten Lagmannssveen), utført arbeid 2025–2026 (rydding, hulltaking, grunnundersøkelser, demontasje), kulturminnefaglige funn (natursteinsmur bekreftet bevart, strekkfisker avdekket, bæresystem bedre enn antatt), fremdriftsplan og fotodokumentasjon. Rapport adresserer Byantikvarens særlige bekymring om steinmuren direkte.
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

### T12 `[ ]` Igangsettingssøknad (IG)
Planlegges parallelt med byggesaksbehandling av rammesøknad. Inkluderer: detaljert brannplan, fundamentering, ventilasjon, fasader, dekker, etasjeoppretting. Estimert leveranse ca. 3,5 mnd etter rammesøknad.
---

### T15 `[ ]` Dokumentere arbeidsøkter med studenter
Lag rapport/logg over hva studentene har gjort og lært.
---

### T16 `[ ]` Legge inn bilder i rapporter
Bilder skal inn i arbeidsrapport og evt. framdriftsrapporter.
---

### T19 `[x]` Søk om utsettelse av prosjektperiode – Kulturminnefondet
**Mottaker:** Kulturminnefondet

**Løst 2026-06-25:** Løst sammen med T20 i `stotte/2026-06-25_kmf_endringsmelding.md`. Søker om forlengelse til 31.12.2026. Begrunnet med: kompleks bygningskonstruksjon, konseptendring til minilager (krevde ny planlegging), myndighetsdialog. Viser til at prosjektet nå er konkret med rammesøknad levert 12. mai 2026 og IG planlagt september 2026. Framdriftsrapporten (T01.01) er vedlegg.
---

### T20 `[x]` Søk om endring av støtteintensitet – Kulturminnefondet
**Mottaker:** Kulturminnefondet

**Løst 2026-06-25:** Del 2 og Del 3 i `stotte/2026-06-25_kmf_endringsmelding.md`. Del 2 melder konseptendring (kontor → minilager), argumenterer for at de støttede tiltakene er uendret og at minilager er bevaringsmessig bedre. Del 3 søker eksplisitt om nedjustering av budsjett fra kr 5 000 000 til kr 2 500 000, med tre begrunnelser: endret sluttprodukt, avdekking/demontering større enn estimert, bæresystemet i bedre stand enn antatt. Støtteintensitet økes fra 15 % til 30 %. Webskjema for omdisponeringssøknad i `stotte/2026-06-25_kmf_endringsmelding_webskjema.md`. Vedlegg: `stotte/2026-06-25_kmf_omdisponering_vedlegg.md/.docx` (begrunnelse for endret budsjett og utførende, inkl. skifte fra Riis Eiendom til HRP/KMTE/SAHAA/HL/KWE) og `stotte/2026-06-25_kmf_omdisponering_finansiering.md/.docx` (finansieringsplan med koordinering av KMF/BYA/UNI mot 70 %-taket).
---

### T85 `[x]` Søk om endring av støtteintensitet – Byantikvaren

**Mottaker:** Byantikvaren, Trondheim kommune (saksbehandler Elisabeth Kahrs, ref. 2025/5928)

#### Mål

Redusere godkjent budsjett fra **kr 2 285 714** til **kr 1 666 667**, slik at støtteintensiteten øker fra 21,9 % til **30 %** (500 000 / 1 666 667 = 30,0 %).

#### Bakgrunn

BYA innvilget 500 000 kr mot et søknadsbudsjett på 2 285 714 kr – dette gir 21,9 % intensitet. Tilsvarende endringsanmodning for KMF (T20, løst 2026-06-25) reduserte KMF-budsjettet fra 5 MNOK til 2,5 MNOK og økte intensiteten til 30 %. BYA har ikke publisert standardprosedyre for budsjettendriger (jf. T78-kartlegging) – kontakt saksbehandler direkte.

#### Fremgangsmåte

1. **Avklar prosessen** – ring/e-post Elisabeth Kahrs for å bekrefte at budsjettreduksjon kan søkes om skriftlig og uten nytt vedtaksmøte.
2. **Skriv endringsmelding** – kombiner med T21 (utsettelse) i ett brev. Strukturér som:
   - Del 1: statusoppdatering (rammesøknad levert 12. mai 2026, IG planlagt sept. 2026, steinmur-status)
   - Del 2: søknad om utsettelse til 31.12.2026 (jf. T21)
   - Del 3: søknad om budsjettnedskriving fra 2 285 714 til 1 666 667 kr
3. **Begrunnelse for budsjettreduksjon** (tilsvarende KMF T20):
   - Konseptendring fra generell istandsetting til minilager har endret omfanget av tiltak
   - Avdekkingsarbeider og demontering har vist at bæresystemet er i bedre stand enn antatt på søknadstidspunktet
   - Mer fokusert kostnadsprogram etter detaljert prosjektering

#### Regnestykke

| | Nå | Etter endring |
|---|---|---|
| Godkjent budsjett (BYA-program) | kr 2 285 714 | **kr 1 666 667** |
| Tilskudd | kr 500 000 | kr 500 000 |
| Støtteintensitet | 21,9 % | **30,0 %** |
| Egenandel + øvrig finansiering | kr 1 785 714 | kr 1 166 667 |

#### Dokumenter som skal produseres

- `stotte/[dato]_bya_endringsmelding.md` – brev til BYA (kombinerer T21 + T85)
- Oppdatert finansieringsplan (jf. `stotte/2026-06-25_kmf_omdisponering_finansiering.md`) som viser koordinering KMF/BYA/UNI mot 70 %-taket

#### Avhengigheter

- **T21** (utsettelse BYA) – løses i samme brev
- **T20** (KMF-endringsmelding, løst) – mal for fremgangsmåte og begrunnelse
- **T78** (kartlegging maks intensitet, løst) – dokumenterer at BYA aksepterer budsjettendringer

**Løst 2026-06-25:** Del 3 i `stotte/2026-06-25_bya_endringsmelding.md`. Løst sammen med T21. Søker nedjustering av budsjett fra 2 285 714 til 1 666 667 kr. Tre begrunnelser: endret sluttprodukt (minilager vs. kontor), avdekking var mer enn estimert, bæresystemet bedre enn antatt. Støtteintensitet økes fra 21,9 % til 30 %. Sendes til byantikvaren.kart@trondheim.kommune.no (ingen nettskjema for BYA).

**Merk:** BYA har ikke standardprosedyre for budsjettendringer — ta telefonkontakt med Elisabeth Kahrs (saksref. 2025/5928) for å bekrefte at prosessen er riktig før innsending.

---

### T21 `[x]` Søk om utsettelse av prosjektperiode – Byantikvaren
**Mottaker:** Byantikvaren

Samme situasjon som KMF (T19). Prosjektperioden for Byantikvaren-tilskuddet (500 000 kr) må forlenges. Se T19 for kontekst om årsaker. I tillegg bør brevet adressere steinmur-spørsmålet fra rammesøknaden slik at Byantikvaren er oppdatert på prosjektets nåværende form.

**Løst 2026-06-25:** Del 1 og Del 2 i `stotte/2026-06-25_bya_endringsmelding.md`. Løst sammen med T85. Del 1 søker forlengelse til 31.12.2026 med tre begrunnelser (kompleks bygg, konseptendring, myndighetsdialog). Del 2 melder konseptendring (kontor/innovasjonshub → minilager), bekrefter at støttede tiltak er uendret, argumenterer for at minilager er bevaringsmessig bedre, og bekrefter at natursteinsmuren vil stå synlig.
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

### T32 `[ ]` Fisjon av KodeWorks Eiendom AS
**Ansvarlig:** Eirik / regnskapsfører / advokat

KodeWorks Eiendom AS eier i dag både Fjordgata 30 og Grønnegata 10. Selskapet skal fisjoneres slik at:
- **Fjordgata 30 AS** (nytt orgnummer) overtar eierskapet til Fjordgata 30 og blir juridisk byggherre for ombyggingen
- **KodeWorks Eiendom AS** beholder dagens orgnummer og eier Grønnegata 10
- Grønnegata 10 kan skilles ut som et tredje selskap ved behov

Alle pågående støtteordninger (KMF, Byantikvaren, Enova, UNI) skal overføres til Fjordgata 30 AS. Banklån søkes i Fjordgata 30 AS. Fisjonen bør gjennomføres før IG-søknad leveres (T12) slik at riktig juridisk enhet er byggherre fra starten.
---

### T59 `[ ]` Gjennomgå og innarbeid bakgrunnsfiler fra rot

Fire filer er flyttet fra prosjektroten til `bakgrunn/nye/` for gjennomgang:

| Fil | Innhold |
|---|---|
| `2026-04-16_ai_feedback.txt` | Tilbakemeldinger fra AI-verktøy brukt underveis i prosjektet |
| `2026-04-16_arbeid_kristian.txt` | Arbeidslogg for Kristian Brandsegg |
| `2026-04-16_arbeid_ole_morten.txt` | Arbeidslogg for Ole Morten Lagmannssveen |
**Hva som skal gjøres per fil:**
- `2026-04-16_arbeid_kristian.txt` og `2026-04-16_arbeid_ole_morten.txt`: Vurder om innholdet er innarbeidet i `historikk.md`. Arbeidsloggene er allerede kildehenvist som `[^52]`. Dersom innholdet er dekket, konverter til `.md` og behold i `bakgrunn/`.
- `2026-04-16_ai_feedback.txt`: Vurder om noe av innholdet bør innarbeides i prosjektdokumentasjon. Slett hvis innholdet er foreldet.

**Merk:** `fg30_arbeidsrapport.md` er skilt ut til T60.

**Avhengigheter:** Ingen.
---
