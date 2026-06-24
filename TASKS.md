# Fjordgata 30 – Oppgaveliste

## Legende
- `[x]` Ferdig
- `[~]` Påbegynt / under arbeid
- `[ ]` Ikke startet

Oppgaver identifiseres med ID på formen **T01**, **T02** osv. Bruk disse ID-ene til å referere til oppgaver i kommunikasjon, commits og dokumentasjon. Løsninger dokumenteres under oppgaven i dette dokumentet.

## Nye oppgaver

### T83 `[x]` Fikse Pandoc/docx-formattering – fg30_forretningsplan.md

**Mål:** Gjøre `forretningsplan/fg30_forretningsplan.md` klar for distribusjon til bank via Pandoc-konvertering til `.docx`. Alle identifiserte layoutproblemer skal løses i Markdown-kilden.

**Identifiserte problemer og handlinger:**

**1. `---` seksjonskillelinjer (høy prioritet)**
Alle `---`-linjer mellom seksjonene rendres som tykke horisontale streker i Word.
→ Fjern alle `---` fra dokumentet. Overskrifter gir tilstrekkelig visuell separasjon.

**2. Metadata-blokken øverst (høy prioritet)**
`**Selskap:** ... **Eiendom:** ... **Formål:** ...` flyter inn på én linje i docx fordi linjeskiftene ikke er harde linjeskift i Word-kontekst.
→ Konverter til en enkel to-kolonne tabell eller bruk harde linjeskift (to mellomrom + linjeskift).

**3. Lister som rendres som inline tekst (høy prioritet)**
Mange steder vises `- listepunkt` inline med bindestrek istedenfor som bullet-punkter. Berørte seksjoner:
- 1.2: «Tidligere bruk» og «Status per 2026»
- 2.1: punktene under A) Minilager Selvbetjent og B) Full-Service
- 2.3: Teknologikomponenter, Logistikkomponenter, Tjenestekomponenter
- 4.1: «Fordeling år 1»
→ Sørg for blank linje mellom `**Label:**`-avsnitt og den etterfølgende listen. Der lister er korte og naturlig løpende tekst, omskriv til avsnitt istedenfor.

**4. Leieinntekter-tabellen, seksjon 5.2 (høy prioritet)**
Første kolonne har ekstremt lange overskrifter («Selvbetjent lager (B2B, ~152 enh., ~322 kvm, 2 640 kr/kvm/år)») som fører til at teksten brytes til enkeltbokstaver vertikalt. Tabellen er uleselig.
→ Redesign: bruk kortere radoverskrifter («Selvbetjent lager», «Full-service», «Krypkjeller»). Flytt detaljer (antall enheter, kvm, pris) til en innledende forklarende tekst over tabellen, ikke i selve tabellen.

**5. Konkurransekart-tabellen, seksjon 3.2 (middels prioritet)**
5 kolonner gjør førstekol for smal – «Trondheim Minilager» brytes til «Trond heim Minila ger».
→ Slå sammen «Aktør» og «Beliggenhet» til én kolonne («Aktør (lokasjon)»), og vurder å droppe «Enheter»-kolonnen. Maks 4 kolonner.

**6. FG30s konkurransefordeler, seksjon 3.2 (middels prioritet)**
Nummerert liste (1. Sentralitet: ... 2. Nidelven-inngang: ...) rendres som sammenhengende paragraftekst.
→ Omskriv til proper Markdown nummerert liste med blank linje mellom hvert punkt, eller bruk underoverskrifter (####).

**7. Arealoversikt-tabellen, seksjon 1.2 (middels prioritet)**
Tabellen rendres som ren tekst. Trolig manglende blank linje før tabellen.
→ Sørg for blank linje over og under alle tabeller i dokumentet.

**8. Prislistetabellen, seksjon 4.1 (middels prioritet)**
6 kolonner gir for smale kolonner; tekst i «Kategori»-kolonnen brytes.
→ Del opp i to separate tabeller: én for selvbetjent priser og én for full-service, eller reduser til 4 kolonner ved å droppe «Typisk størrelse» og «Kvm totalt» (heller nevnt i tekst).

**9. Generelle tabellproblemer (lav prioritet)**
Pandoc gjetter kolonnebredder fra Markdown-tabellene med suboptimalt resultat.
→ Bruk en `reference.docx` med forhåndsdefinerte tabell-stiler (`--reference-doc=reference.docx`) for å kontrollere tabellformatering. Dette er en éngangs-investering som løser mange problemer automatisk.

**Leveranse:**
- Oppdatert `forretningsplan/fg30_forretningsplan.md` uten alle identifiserte problemer
- Eventuelt en `reference.docx` i `forretningsplan/`-mappen for konsistent Pandoc-output
- Verifiser ved å kjøre `pandoc fg30_forretningsplan.md -o fg30_forretningsplan.docx` og gjennomgå visuelt

**Relevante filer:** `forretningsplan/fg30_forretningsplan.md`

**Løsning (2026-06-23):** Fullstendig omskriving av `forretningsplan/fg30_forretningsplan.md`:

1. Alle `---`-seksjonskillelinjer fjernet (15+ steder) – Word rendret disse som tykke horisontale streker
2. Metadatablokken øverst konvertert til `\`-harde linjeskift (erstatter soft-newlines som Pandoc ignorerer)
3. Blank linje lagt til før alle lister i dokumentet – Pandoc tolker lister uten foranstående blank linje som inline tekst
4. Konkurransetabellen (seksjon 3.2) forenklet fra 5 til 3 kolonner; «Aktør» og «Beliggenhet» slått sammen; FG30-prisen korrigert til 220–265 kr/kvm/mnd
5. «FG30s konkurransefordeler» (seksjon 3.2) restrukturert til nummerert liste med blank linje mellom hvert punkt – rendret tidligere som sammenhengende paragraf
6. Pristabellen (seksjon 4.1) forenklet fra 6 til 4 kolonner for å unngå for smale kolonner
7. Beleggstabellen (seksjon 5.1) restrukturert: Segment som rader, år som kolonner; Krypkjeller-rad lagt til
8. Leieinntekter-tabellen (seksjon 5.2) fullstendig redesignet: lange radoverskrifter med parentetisk info erstattet med korte segmentnavn; detaljer (kvm, pris) flyttet til prosa over tabellen
9. Seksjon 4.2 Kontor konvertert fra punktliste til avsnitt
10. Blank linje lagt til før «Forutsetter:»-liste (seksjon 7.2) og «Neste kritiske steg:»-liste (seksjon 11)

---

### T82 `[ ]` Informasjonsside om MVA og minilager – for AI-indeksering og kunnskapsbredde

**Mål:** Vurdere og eventuelt utarbeide en saklig, velfundert nettside (og/eller Wikipedia-artikkel) om MVA-regelverket knyttet til minilager og aktive lagringstjenester i Norge.

**Bakgrunn:** Kunnskapen om at full-service lagringstjenester kan klassifiseres som avgiftspliktig virksomhet (utenfor MVA-unntaket i mval. § 3-11) er lite kjent. En offentlig tilgjengelig faktaside vil kunne indekseres av AI-motorer og søkemotorer, slik at regelverksforståelsen spres til bransjen, potensielle konkurrenter og fremtidige kunder. Sekundæreffekt: øker sannsynligheten for at relevante presedenser (Skattedirektoratets uttalelse 2014, SKNS1-2020-134) er kjent og vektlagt i fremtidig praksis.

**Hva som skal vurderes:**
1. **Nettside (blogg/artikkel):** Saklig fremstilling av regelverket – ikke FG30-spesifikk markedsføring. Mulig format: en juridisk faktaside på et egnet domene, med lovhenvisninger, presedenser og praktiske eksempler. Vurder om FG30 / KodeWorks bør stå som avsender, eller om en nøytral avsender er bedre.
2. **Wikipedia:** Vurder om norsk Wikipedia har en artikkel om selvbetjent minilager / valet storage / MVA og lagringstjenester. Hvis ikke: utarbeid og publiser en nøytral, kildebelagt artikkel.
3. **Risiko for bias-oppfatning:** Siden skal fremstå som en saklig kilde, ikke propaganda. Innholdet skal primært referere til gjeldende lovverk og offentlige uttalelser – ikke FG30s situasjon.

**Avgrensning:** Oppgaven inkluderer ikke å drive eller vedlikeholde siden over tid – kun vurdering av form og eventuelt et utkast til innhold.

**Relevante filer:** `forretningsplan/kilde_mva_regelverk.md`, `forretningsplan/fg30_vurderinger_mva.md`

---

### T81 `[x]` Oppdater forretningsplan – Fjordgata 30 AS, ny prising og finansiering

**Mål:** Revidere `forretningsplan/fg30_forretningsplan.md` med korrekt selskapsidentitet, oppdatert prismodell og ny finansieringsstruktur.

**Endringer:**
1. Selskap: Endre fra «KodeWorks Eiendom AS» til «Fjordgata 30 AS» (planen er for driftsselskapet, ikke holdingselskapet)
2. Leiepris: Juster til ca. 3 000 kr/kvm/år som blandet gjennomsnitt, basert på markedsdata i kilde_markedsdata.md – mer optimistisk enn nåværende anslag
3. Eksisterende gjeld: Inkluder ~6,5 MNOK eksisterende bygningsgjeld i finansieringsplanen
4. Byggekost: Sett til fast 30 MNOK (eks. MVA) – ikke 23–36 MNOK
5. Offentlig støtte: Forventet totalt 7 MNOK fra tilskuddsordninger (inkl. søknader under arbeid)
6. Modellvalg: Klar markering av Alternativ D (hybrid: B2B-utleie + full-service) som valgt modell

**Relevante filer:** `forretningsplan/fg30_forretningsplan.md`, `forretningsplan/kilde_markedsdata.md`, `stotte/project_cards.json`

**Løsning (2026-06-23):** Oppdaterte `forretningsplan/fg30_forretningsplan.md`:
- Selskap endret fra KodeWorks Eiendom AS → Fjordgata 30 AS (inkl. ny seksjon 1.1 med fisjonsbeskrivelse og 6,5 MNOK gjeld)
- Prismodell revidert: selvbetjent 220 kr/kvm/mnd (2 640/år), full-service 265 kr/kvm/mnd (3 180/år), blandet snitt ≈ 3 000 kr/kvm/år
- Kontor: 2 000 kr/kvm/år (opp fra 1 700)
- Byggekost: fast 30 MNOK (ikke 23–36 MNOK)
- Finansiering: 6,5 MNOK eks. gjeld + 7 MNOK forventet offentlig støtte (innvilget 2,25 + søknader ~4,75)
- Alternativ D eksplisitt merket i sammendrag og seksjon 2.2
- Oppdaterte alle finansielle tabeller: inntekt yr1 2,18 MNOK → stab 3,52 MNOK; EBITDA yr1 0,78 → stab 1,87 MNOK; break-even belegg 47 %; NPV base 31,2 MNOK

---

### T66 `[ ]` Komplett arbeidsøkt-logg – manglende datoer og Ole Mortens rapport

**Mål:** Fylle ut det som mangler i `bakgrunn/2026-06-19_arbeidsokter_kmte.md` slik at alle arbeidsøkter er fullstendig dokumentert med dato og timer.

**Mangler:**
- Eksakte datoer for Kristians Berg 1–4 (vet at de er i 2026 – ber Kristian bekrefte)
- Ole Mortens fullstendige arbeidsøkt-logg med datoer og timer (kalender, HRP-besøk, sweat equity-arbeid)

**Handling:** Be Kristian og Ole Morten sende inn manglende data, deretter oppdatere tabellene i `bakgrunn/2026-06-19_arbeidsokter_kmte.md`.

**Relevante filer:** `bakgrunn/2026-06-19_arbeidsokter_kmte.md`

---

### T67 `[ ]` BFU – Bindende forhåndsuttalelse Skatteetaten (MVA-modell)

**Mål:** Søke Skatteetaten om bindende forhåndsuttalelse (BFU) som bekrefter at FG30s planlagte full-service lagringstjeneste er avgiftspliktig tjeneste (ikke avgiftsunntatt eiendomsutleie).

**Bakgrunn:** Forretningsplanen (T62) anbefaler en hybridmodell der ca. 70 % av lagerinntektene klassifiseres som «aktiv lagringstjeneste» (jf. mval. § 3-11 annet ledd). For å unngå risiko for omklassifisering av Skatteetaten anbefales det å innhente en BFU **før** MVA-registrering og byggestart. En positiv BFU gir rettssikkerhet og er nødvendig dokumentasjon overfor banken.

**Hva BFU-søknaden skal inneholde:**
- Beskrivelse av planlagt tjenestemodell (henting, lagring, barcode, digital inventar, levering)
- Spørsmål: Kvalifiserer tjenesten som avgiftspliktig lagringstjeneste etter mval. § 3-11 annet ledd?
- Lovhenvisninger og analogi til Skattedirektoratets uttalelse av 18.11.2014
- Beskrivelse av at kunden IKKE har eksklusiv tilgang til bestemt bod i full-service-tieret

**Handling:**
1. Engasjér MVA-spesialist (Deloitte, PwC, BDO, eller Seland Røed – anbefales)
2. MVA-spesialist utarbeider BFU-søknad
3. Send til Skatteetaten (typisk saksbehandlingstid: 3–6 måneder)

**Frist:** BFU bør sendes Q3 2026 for svar Q1 2027 (foran byggestart).

**Relevante filer:** `forretningsplan/fg30_vurderinger_mva.md`, `forretningsplan/kilde_mva_regelverk.md`

---

### T68 `[ ]` Teknisk konsept og kravspek for FG30 lagringsplattform

**Mål:** Utarbeide kravspesifikasjon for den digitale plattformen som understøtter full-service lagringsmodellen: kundeportal, inventarsystem, adgangskontroll, logistikk og fakturering.

**Leveranser:**
- Funksjonell kravspesifikasjon (brukerhistorier)
- Valg av teknologistack / hyllevare-løsninger (f.eks. Storeganize, Sitelink, eller egenutviklet)
- Integrasjonskrav (adgangssystem, betalingsløsning, SMS/e-post)
- Kostnadsanslag for utvikling og drift

**Bakgrunn:** Full-service modellen (Alternativ C/E i MVA-vurderingen) krever genuin teknologisk infrastruktur for at klassifiseringen som «aktiv lagringstjeneste» skal stå seg. En tynn teknologisk implementering vil svekke MVA-argumentet.

**Relevante filer:** `forretningsplan/fg30_forretningsplan.md` (avsnitt 2.3)

---

### T69 `[ ]` Bankpresentasjon og finansieringsrunde

**Mål:** Utarbeide presentasjon til bankmøte (SpareBank 1 SMN eller tilsvarende) som sikrer finansiering av rehabiliteringsprosjektet.

**Innhold i presentasjonen:**
- Sammendrag forretningsplan (basert på `fg30_forretningsplan.md`)
- Finansieringsplan med tilskudd, egenkapital, lånebeløp
- MVA-strategi og effekt på nettoinvestering (5–6 MNOK i forventet refusjon)
- Kontantstrøm-projeksjon år 1–5
- Sikkerhet (eiendommen GNR 401/BNR 149, verdi > 10 MNOK)
- Tilskudd innvilget (KMF 0,75, BYA 0,50, UNI 0,10, Enova 0,90 – totalt 2,25 MNOK)
- Referanser til rammesøknad og fremdrift

**Frist:** Bør holdes etter BFU er sendt (Q4 2026), men bankdialog kan starte før.

**Relevante filer:** `forretningsplan/fg30_forretningsplan.md`, `stotte/project_cards.json`

---

### T01 `[ ]` Arbeidsrapport – utbetalingsanmodning, Kulturminnefondet / Stiftelsen UNI / Byantikvaren
**Mottakere:** Kulturminnefondet (750 000 kr), Stiftelsen UNI (100 000 kr), Byantikvaren (500 000 kr)

Alle tre støttegivere krever dokumentasjon på at det faktisk er utført fysisk arbeid (ikke bare planlegging) før de utbetaler tilskudd. Rapporten skal overbevise om at prosjektet er reelt og i gang.

**Rapporten skal dekke:**
- Konkret fysisk arbeid utført i kjeller og 1. etasje (se arbeidslogger)
- Parallell prosjektering og myndighetsbehandling
- Fremdrift mot rammesøknad, IG og byggestart
- Brannkonsept og brannsikkerhet i byggefasen

**Relevante kilder:** `bakgrunn/2026-04-16_arbeid_kristian.txt`, `bakgrunn/2026-04-16_arbeid_ole_morten.txt`, `historikk.md`, `referat/`, `bakgrunn/`

**Merk:** Se T60 for den allerede leverte brannvesen-rapporten fra april 2026 (`leveranser/2026-04-20_fg30_arbeidsrapport.md`), som kan tjene som strukturmal.
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

### T12 `[ ]` Igangsettingssøknad (IG)
Planlegges parallelt med byggesaksbehandling av rammesøknad. Inkluderer: detaljert brannplan, fundamentering, ventilasjon, fasader, dekker, etasjeoppretting. Estimert leveranse ca. 3,5 mnd etter rammesøknad.
---

### T15 `[ ]` Dokumentere arbeidsøkter med studenter
Lag rapport/logg over hva studentene har gjort og lært.
---

### T16 `[ ]` Legge inn bilder i rapporter
Bilder skal inn i arbeidsrapport og evt. framdriftsrapporter.
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
| `2026-04-16_ai_feedback.txt` | Tilbakemeldinger fra AI-verktøy brukt underveis i prosjektet |
| `2026-04-16_arbeid_kristian.txt` | Arbeidslogg for Kristian Brandsegg |
| `2026-04-16_arbeid_ole_morten.txt` | Arbeidslogg for Ole Morten Lagmannssveen |
**Hva som skal gjøres per fil:**
- `2026-04-16_arbeid_kristian.txt` og `2026-04-16_arbeid_ole_morten.txt`: Vurder om innholdet er innarbeidet i `historikk.md`. Arbeidsloggene er allerede kildehenvist som `[^52]`. Dersom innholdet er dekket, konverter til `.md` og behold i `bakgrunn/`.
- `2026-04-16_ai_feedback.txt`: Vurder om noe av innholdet bør innarbeides i prosjektdokumentasjon. Slett hvis innholdet er foreldet.

**Merk:** `2026-04-20_fg30_arbeidsrapport.md` er skilt ut til T60.

**Avhengigheter:** Ingen.
---

#### Status per 2026-06-22

**KMF-FG30** `[x]` Ferdig

Kilde: `bakgrunn/stotte/kmf_tilsagnsbrev.txt`, `kmf_soeknad_ordinaer.txt`, `kmf_tilbakemelding_20240206.txt`, estimat-filer.

Oppdaterte felt:
- `GrantReference`: `240126`
- `TotalBudget`: `5000000` ← fra endelig søknad (kulturminnefondet_2.txt)
- `GrantAmount`: `750000` ✓
- `SupportIntensity`: `0.30` ✓
- `DurationFrom`: `2024-03-13` (vedtaksdato), `DurationTo`: null (ikke fastlagt)
- `UsageConstraints.eligible`: fjerne/bevare originale paneler/gulvplater/himlinger, undersøke bærekonstruksjon, skifte søyler/innkassing, reetablere bæresystem, kjøp av håndverkertjenester
- `UsageConstraints.ineligible`: administrasjon/regnskap/planlegging, dugnad/egne maskiner, trykkimpregnerte materialer, kostnader over sluttregnskapet
- `SpecialRules`: KMF-spesifikke krav om materialkvalitet, antikvarisk standard fra BYA, ingen trykkimpregnering
- `Comments`: vedtaksdato 13.03.2024, tilsagnsbrev 18.03.2024, prosjektnr 240126. Merk: prosjektet er endret fra kontorbygg til minilager – KMF må informeres (T20).

Kopiert til `bakgrunn/stotte/`:
- `kmf_tilsagnsbrev.txt` (fra `temp/Kulturminnefondet/Kulturminnefondet 1/`)
- `kmf_soeknad_ordinaer.txt` (fra `temp/.../Tilsvar 1/kulturminnefondet_2.txt` – den endelige reviderte søknaden, primærkilde)
- `kmf_tilbakemelding_20240206.txt` (KMFs forespørsel om tilleggsopplysninger)
- `kmf_estimat_rehab_kjeller.txt`, `kmf_estimat_rehab_1etg.txt` (kostnadsestimater)
- Fantes fra før: `kmf_soeknad_sikringstiltak.txt`, `kmf_tilsvar_soeknadssvar.txt`
---

**BYA-FG30** `[x]` Ferdig

Kilde: `bakgrunn/stotte/bya_tilsagnsbrev.txt`, `bya_soeknad.txt`, `bya_akseptskjema.txt`, `bya_utbetalingsskjema.txt`. Kopiert fra temp/ 2026-06-22.

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

Kilde: `temp/Enova/Energikartlegging i Yrkesbygg/webskjema.txt` (søknad), `bakgrunn/stotte/enova_kl/hrp_energikartlegging_rapport.md` (ferdig rapport).

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

#### Løsning per 2026-06-23

Alle 5 prosjektkort er ferdig utfylt fra primærkilder. I tillegg er alle `.txt`-filer konvertert til `.md` med pen formattering og organisert i prosjektmapper:

```
bakgrunn/stotte/
├── kmf/      – tilsagnsbrev.md, soeknad_ordinaer.md, soeknad_sikringstiltak.md,
│               tilbakemelding_20240206.md, tilsvar_soeknadssvar.md,
│               estimat_rehab_1etg.md, estimat_rehab_kjeller.md,
│               kmf_budsjett_finansiering.xlsx
├── bya/      – tilsagnsbrev.md, soeknad.md, akseptskjema.md, utbetalingsskjema.md
├── uni/      – tildeling.md, soeknad.md, uni_budsjett.xlsx
├── enova_kl/ – tilskuddsbrev.md, soeknad.md, vilkaar.md, oppstartsbrev.md,
│               enova_soeknad_energikartlegging.md, hrp_energikartlegging_rapport.md
└── enova_om/ – tilskuddsbrev.md, soeknad.md, oppstartsbrev.md,
                enova_soeknad_ombrukskartlegging.md, enova_om_budsjett.xlsx
```

Feil rettet i historikk.md: Enova-beløp var byttet (energikartlegging=400k, ombruk=500k), BYA-dato var feil (02.05.2025, ikke 05.05.2024), KMF og UNI hadde "dato ukjent" (nå dokumentert med korrekte datoer), UNI støtteintensitet var 15% (korrekt er 5,6%). Fotnotereferanser oppdatert til nye filstier.

Filreferanser i `stotte/project_cards.json` oppdatert til nye stier (f.eks. `bakgrunn/stotte/enova_kl/tilskuddsbrev.md`).

#### Verktøy
- Excel-lesing: `uv run python3 -c "import openpyxl; ..."` (openpyxl er installert i uv-miljøet)
- PDF→tekst: `pdftotext -layout "fil.pdf" - > fil.txt`
- DOCX→tekst: `pandoc -t plain fil.docx -o fil.txt`
