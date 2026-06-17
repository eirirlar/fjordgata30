# Fjordgata 30 – Oppgaveliste

## Legende
- `[x]` Ferdig
- `[~]` Påbegynt / under arbeid
- `[ ]` Ikke startet

Oppgaver identifiseres med ID på formen **T01**, **T02** osv. Bruk disse ID-ene til å referere til oppgaver i kommunikasjon, commits og dokumentasjon. Løsninger dokumenteres under oppgaven i dette dokumentet.

---

## Selskapsstruktur og MVA

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

## Tilskuddsforvaltning

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

## Rapporter og utbetalingsanmodninger

### T01 `[x]` Arbeidsrapport
**Mottaker:** Kulturminnefondet, Byantikvaren, Brannvesen
`fg30_arbeidsrapport.md` / `.docx` ferdig.

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

### T09 `[ ]` Oversikt støttemidler – Bank
**Mottaker:** Bank

Trenger en samlet oversikt over alle innvilgede tilskudd og finansieringskilder for å dokumentere prosjektøkonomi. Bruk `../stotte`-prosjektet som kilde for tall.

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

## Søknader

### T11 `[x]` Rammesøknad minilager
Levert 12. mai 2026.

---

### T12 `[ ]` Igangsettingssøknad (IG)
Planlegges parallelt med byggesaksbehandling av rammesøknad. Inkluderer: detaljert brannplan, fundamentering, ventilasjon, fasader, dekker, etasjeoppretting. Estimert leveranse ca. 3,5 mnd etter rammesøknad.

---

## TBRT (Trondheim Brannvesen)

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

### T34 `[x]` Dokumenter relevant lovverk for T31
**Mappe:** `bakgrunn/lovverk/`

Lag separate `.md`-filer for hvert lovverk som er relevant for klage på tvangsmulkt-innkrevingene (T31). Filene skal inneholde fulltekst eller utdrag av de relevante paragrafene, med kort forklaring av hvorfor de er relevante for saken vår.

**Filer som skal opprettes:**

| Filnavn | Innhold |
|---|---|
| `brann_eksplosjonsvernloven.md` | §§ 1, 6, 37, 39, 41, 42 |
| `forskrift_brannforebygging.md` | §§ 4, 5, 6, 8, 9, 10 (§ 6 om risikobasert tilnærming for eldre bygg) |
| `forvaltningsloven.md` | §§ 16, 17, 24–25, 28, 29, 34, 35, 36, 42, 51 (4. ledd) |
| `tvangsfullbyrdelsesloven.md` | §§ 7-2, 13-14 |
| `grunnloven.md` | § 98 (likhet for loven) |
| `emk.md` | Artikkel 6 (rettferdig rettergang, tilstrekkelig tid til forsvar), Tilleggsprotokoll 1 artikkel 1 (vern om eiendomsretten) |
| `plan_bygningsloven.md` | §§ 29-4, 31-3, 31-4 (særregler for eksisterende byggverk, herunder vernede bygg) |
| `ulovfestede_prinsipper.md` | Forholdsmessighetsprinsippet, likhetsprinsippet, myndighetsmisbrukslæren, saklighetsprinsippet, kontradiksjonsprinsippet – med korte forklaringer og relevans for saken |

**Kontekst:** Fjordgata 30 er verneklasse B (plan- og bygningsloven, ikke kulturminneloven §§ 17–19). Vernet medfører at inngrep i bygningskroppen (f.eks. sprinklerinstallasjon) krever Byantikvarens godkjenning og byggetillatelse. TBRT kan ikke kreve at dette gjennomføres uten de nødvendige tillatelsene på plass. Dette spenningsforholdet mellom to offentlige myndigheters krav er et sentralt argument i T31.

---

### T35 `[x]` Beskriv hvorfor relevant lovverk gjelder for prosjektet
**Filnavn:** `bakgrunn/lovverk/prosjektrelevans.md`  
**Avhenger av:** T34 (lovverkfilene bør finnes først)

Lag ett samlet dokument som forklarer hvorfor hvert lovverk er relevant for Fjordgata 30-prosjektet som helhet – ikke bare for klagesaken mot TBRT. Dokumentet skal gi en leser (bank, støttegiver, advokat, ny prosjektdeltaker) en rask oversikt over hvilke rettslige rammer prosjektet opererer innenfor.

**Struktur per lovverk:**
- Hva loven/forskriften regulerer
- Konkret hvordan den treffer Fjordgata 30 (hvilke krav, hvilke myndigheter, hvilke prosesser)
- Eventuelle spenninger mellom ulike myndigheters krav

**Lovverk som skal dekkes:**
- Brann- og eksplosjonsvernloven – tilsynsplikt, pålegg, tvangsmulkt
- Forskrift om brannforebygging – dokumentasjonskrav, risikobasert tilnærming for eldre bygg
- Plan- og bygningsloven – byggesøknadsprosessen, særregler for eksisterende byggverk, verneklasse B
- Forvaltningsloven – partens rettigheter i møte med offentlig myndighet, klagerett, utredningsplikt
- Grunnloven og EMK – likhet for loven, rett til forsvar, vern om eiendomsretten
- Merverdiavgiftsloven – MVA-fritak/-plikt ved utleie av lagerplass (se T33)
- Ulovfestede forvaltningsrettslige prinsipper – forholdsmessighet, saklighet, kontradiksjon

---

### T28 `[x]` Arkiver vedtak om tvangsmulkt fra TBRT
**Mottaker/kilde:** Trondheim Brannvesen / TBRT

Det opprinnelige vedtaket om tvangsmulkt (dagbøter 2 000 kr/dag) finnes ikke i prosjektet. Finn dokumentet (e-post, brev eller portal) og legg det i `bakgrunn/` med filnavn `tbrt_vedtak_tvangsmulkt.pdf` eller `.txt`. Dokumentet er viktig bakgrunn for T07 (framdriftsrapport til TBRT) og for eventuelle klageprosesser.

**Løsning (2026-06-17):** `bakgrunn/2025-05-07_vedtak_tvangsmulkt.md` (konvertert fra PDF, datert 07.05.2025). I tillegg: `bakgrunn/2024-11-08_paalegg_brannsikring.md` og `bakgrunn/2024-01-24_tilsynsrapport_tbrt.md` gir historikk forut for vedtaket.

---

### T29 `[x]` Arkiver klage på vedtak om tvangsmulkt
**Mottaker/kilde:** Trondheim Brannvesen / TBRT / klageinstans

Klagen på vedtaket om tvangsmulkt finnes ikke i prosjektet. Finn klagebrevet (sendt av KodeWorks eller advokat) og legg det i `bakgrunn/` med filnavn `tbrt_klage_tvangsmulkt.pdf` eller `.txt`. Nødvendig for å forstå vår juridiske posisjon og argumentasjon mot dagbøtene.

**Løsning (2026-06-17):** `bakgrunn/2025-05-26_klage_vedtak_tvangsmulkt.md` (konvertert fra docx, datert 26.05.2025). Også relevant: `bakgrunn/2025-10-09_krav_om_ny_behandling.md`.

---

### T30 `[x]` Arkiver oversikt over påløpte tvangsmulkter
**Mottaker/kilde:** Intern / TBRT

Lag eller hent en oversikt over alle tvangsmulkter som har løpt: dato de startet, sats (2 000 kr/dag), eventuelle avbrudd/pauser, og samlet beløp til dags dato. Legg oversikten i `bakgrunn/tbrt_tvangsmulkt_oversikt.md`. Viktig for prosjektøkonomi og for å beregne konsekvensen dersom dagbøtene ikke stoppes.

**Løsning (2026-06-17):** `bakgrunn/2026-06-03_3gangs_innkreving_tvangsmulkt.md` dokumenterer 3. gangs innkreving for perioden 15.04.2026–26.05.2026. For komplett oversikt over alle perioder, les også `bakgrunn/2025-05-07_vedtak_tvangsmulkt.md`. En samlet `tbrt_tvangsmulkt_oversikt.md` er ikke laget – kan lages som eget tiltak ved behov.

---

## Dokumentasjon og intern rapportering

### T15 `[ ]` Dokumentere arbeidsøkter med studenter
Lag rapport/logg over hva studentene har gjort og lært.

---

### T16 `[ ]` Legge inn bilder i rapporter
Bilder skal inn i arbeidsrapport og evt. framdriftsrapporter.

---

## Filstruktur og opprydding

### T17 `[x]` Splitt bakgrunn/merged_files til enkeltfiler

De to filene `merged_files_1.txt` (~10 900 linjer) og `merged_files_2.txt` (~4 500 linjer) ble opprinnelig laget som samlet kontekst til en Custom GPT. De inneholder flere separate dokumenter som bør splittes ut:

**Antatt innhold i `merged_files_1.txt`:**
| Foreslått filnavn | Beskrivelse |
|---|---|
| `kmf_tilsvar_soeknadssvar.txt` | Tilsvar på søknadssvar fra Kulturminnefondet (feb 2024) |
| `kmf_soeknad_sikringstiltak.txt` | Søknad til Kulturminnefondet – Sikringstiltak, bærekonstruksjon |
| `nettside_om_prosjektet.txt` | Beskrivelse av prosjektet (nettsidekopi, "above/below fold") |
| `tilstandsanalyse_kalkyle.txt` | Tilstand og kalkyle (bygningsdeler, TG-vurderinger) |
| `notat_va_skred_flom.txt` | Notat om VA, skred- og flomvurdering |
| `brannkonsept_fjordgata30.txt` | Brannkonsept Fjordgata 30 (stort dokument) |

**Antatt innhold i `merged_files_2.txt`:**
| Foreslått filnavn | Beskrivelse |
|---|---|
| `tilstandsanalyse_nivaa1.txt` | Tilstandsanalyse nivå 1, utarbeidet av Ole Morten m.fl. |
| `naeringsmegling_markedsanalyse.txt` | Næringsmegling / markedsanalyse |

**Gjennomføring:** Les gjennom filene, identifiser dokumentgrenser, skriv hvert dokument til egen fil i `bakgrunn/`. Slett `merged_files_1.txt` og `merged_files_2.txt` når splitting er ferdig og verifisert.

**Løsning (2026-06-17):** Splittet i 12 filer i `bakgrunn/`:
- `kmf_tilsvar_soeknadssvar.txt` – Tilsvar til Kulturminnefondet (feb 2024)
- `kmf_soeknad_sikringstiltak.txt` – KMF søknad (sikringstiltak)
- `uni_soeknad.txt` – Stiftelsen UNI søknad
- `tradisjonsbygg_referanseliste.txt` – Tradisjonsbygg AS prosjektreferanser
- `kodeworks_selskapsbeskrivelse.txt` – Om Oss, personalhåndbok, prosjektoversikt
- `fondsoknader.txt` – Adolf Øiens Fond, Kavlifondet, DOGA DIP
- `rammesoknad_kontor_2023_beskrivelse.txt` – Nabovarsel + søknadsbeskrivelse (kontorbygg, 2023)
- `rammesoknad_kontor_2023_vedlegg_F.txt` – F-02, F-04–F-09 (flom, VA, el, ventilasjon)
- `rammesoknad_kontor_2023_brannkonsept.txt` – Brannkonsept til rammesøknad (2023)
- `rammesoknad_kontor_2023_vedlegg_I.txt` – I-01–I-05 (Riksantikvaren, slokkevann, Byantikvaren m.fl.)
- `naeringsmegling_markedsmateriell.txt` – Kodeverket markedsmateriell + DNB salgsprospekt
- `tilstandsanalyse_nivaa1.txt` – Tilstandsanalyse nivå 1 (HRP/Ole Morten)
- `dnb_verdivurdering_2022.txt` – DNB Næringsmegling verdivurdering (aug 2022)

`merged_files_1.txt` og `merged_files_2.txt` er slettet. Oppdatert 2026-06-17: `kmf_uni_soknader.txt` splittet videre til `kmf_soeknad_sikringstiltak.txt` og `uni_soeknad.txt`.

---

### T18 `[ ]` Fjern kontorbygg-dokumenter fra bakgrunn/

Dokumentene fra 2023-rammesøknaden gjelder kontorbygg-prosjektet som ble skrinlagt. De er ikke lenger relevante som bakgrunn nå som prosjektet er minilager. Filene bør slettes:

- `rammesoknad_kontor_2023_beskrivelse.txt`
- `rammesoknad_kontor_2023_vedlegg_F.txt`
- `rammesoknad_kontor_2023_brannkonsept.txt`
- `rammesoknad_kontor_2023_vedlegg_I.txt`

Nyere versjoner av F- og I-vedleggene (for minilager-søknaden) finnes nå i `bakgrunn/` med datoprefix (f.eks. `2026-02-06_notat_va.txt`, `2026-02-09_notat_ventilasjon.txt`, `2023-06-28_uttalelse_riksantikvaren_graving.txt` m.fl.). Bekreft at ingenting unikt forsvinner før sletting.

---

### T25 `[x]` Arkiver HRP-rapport energikartlegging
Rapport fra HRP/RiEn om energikartlegging og energimerking skal inn i prosjektet. Motta filen fra HRP (eller Eirik) og legg den i `bakgrunn/` med et fornuftig filnavn (f.eks. `hrp_energikartlegging_rapport.pdf`). Oppdater T23 med status når rapporten er mottatt.

**Løsning (2026-06-17):** PDF lå allerede i `bakgrunn/` under filnavnet `Energikartlegging Fjordgt 30.pdf`. Les alle 30 sider og konvertert til `bakgrunn/hrp_energikartlegging_rapport.md`. Rapporten inneholder nå-tilstand (energikarakter G, 252 000 kWh/år), alle 12 tiltak med kostnader og besparelser, tre tiltakspakker (T1–T3), og finansieringsinfo (Enova, grønne lån). T23 er fortsatt åpen – avklar med HRP om rapporten er levert til Enova.

---

### T26 `[x]` Arkiver Enova-søknader
Søknadsdokumentene til Enova (for både energikartlegging og ombrukskartlegging) finnes ikke i prosjektet per nå – trolig i Enova-portalen eller e-post. Last ned og legg i `bakgrunn/` med filnavn:
- `enova_soeknad_energikartlegging.pdf`
- `enova_soeknad_ombrukskartlegging.pdf`

**Løsning (2026-06-17):** Søknadstekstene lå som `bakgrunn/webskjema (1).txt` (energikartlegging) og `bakgrunn/webskjema.txt` (ombrukskartlegging). Konvertert til:
- `bakgrunn/enova_soeknad_energikartlegging.md`
- `bakgrunn/enova_soeknad_ombrukskartlegging.md`

---

### T27 `[ ]` Konverter alle bakgrunn-filer fra .txt til .md
**Format:** Markdown, egnet for manuell lesing og fremtidig redigering

Alle filer i `bakgrunn/` som fortsatt er `.txt` bør konverteres til `.md` for enklere lesing og redigering. Bruk `pandoc` eller bare rename der innholdet allerede er rent tekst. Slett originale `.txt`-filer etterpå.

**Nåværende `.txt`-filer i `bakgrunn/` (per 2026-06-17):**

Søknader og korrespondanse (høy prioritet):
- `kmf_tilsvar_soeknadssvar.txt`
- `kmf_soeknad_sikringstiltak.txt`
- `uni_soeknad.txt`
- `fondsoknader.txt`
- `2026-01-26_dispensasjonssoknad.txt`
- `2026-01-26_folgebrev_nabovarsel.txt`
- `2026-02-09_folgebrev_rammesoknad.txt`
- `byantikvaren_tilbakemelding_rammesoknad.txt`
- `2026-06-11 forberedelse til  TBRT statusmøte.txt`

Tekniske notater (fra minilager-rammesøknad):
- `2026-02-06_notat_va.txt`
- `2026-02-09_notat_ventilasjon.txt`
- `2026-02-10_notat_el-kraft.txt`
- `2026-02-10_notat_rib.txt`
- `2026-02-02_sjekkliste_ribr.txt`
- `2026-02-16_brannkonsept_bkl3_tek17.txt`
- `2026-02-16_brannkonsept_vedlegg_a.txt`
- `2026-02-17_brannprosjektering_minilager.txt`
- `2026-02-26_notat_brannsikring_gjennomforingsfasen.txt`
- `2026-02-26_redegjoerelse_tbrt.txt`

Vedlegg fra riksantikvaren / Byantikvaren:
- `2023-06-15_notat_slokkevann.txt`
- `2023-06-28_uttalelse_riksantikvaren_graving.txt`
- `2023-07-05_notat_skred_flomfare.txt`

Markedsmateriell og bakgrunn (lav prioritet):
- `kodeworks_selskapsbeskrivelse.txt`
- `tradisjonsbygg_referanseliste.txt`
- `naeringsmegling_markedsmateriell.txt`
- `dnb_verdivurdering_2022.txt`
- `tilstandsanalyse_nivaa1.txt`
- `situasjonskart.txt`
- `situasjonsplan.txt`

Skal slettes (kontorbygg 2023, dekkes av T18):
- `rammesoknad_kontor_2023_beskrivelse.txt`
- `rammesoknad_kontor_2023_vedlegg_F.txt`
- `rammesoknad_kontor_2023_brannkonsept.txt`
- `rammesoknad_kontor_2023_vedlegg_I.txt`
