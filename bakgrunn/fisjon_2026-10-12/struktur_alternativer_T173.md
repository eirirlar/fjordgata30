---
tittel: Strukturvurdering — tre alternativer for konsernoppsett etter fisjon
dato: 2026-10-12
rolle: Agent 6 — Strukturanalytiker
scope: >
  Vurdere tre strukturalternativer (A, B, C) for fisjonen av KodeWorks
  Eiendom AS langs ti dimensjoner, og gi en begrunnet anbefaling.
  Analyse-only; ingen eksterne henvendelser. Lovreferanser utenom
  mval. kap. 9 markeres [verifiseres fase 10].
input: >
  bruker_input_02.md, agent_01_fisjonsjurist_v2.md,
  agent_04_finans_tilskudd_v2.md, iterasjon_02_merged.md,
  mva_forelopig_svar_skattetaten.md, mval_kap9 verbatim.
---

# Strukturvurdering — tre alternativer

## 1. Felles kontekst

Fisjonen deler KodeWorks Eiendom AS (KWE) sin eiendomsmasse i to driftsenheter — Fjordgata 30 (rehabilitering til minilager) og Grønnegata 10 (kontorutleie). Spørsmålet som avgjøres her er **hvor de to nye selskapene plasseres i konsernet** og **hva som skjer med KWE som rettssubjekt**. Dette styrer åpningsbalansene, risikobildet, dekningsgrunnlaget for TBRTs tvangsmulkt, konsernlåns-strukturen, og mulighetene for å ta Brandsegg og Lagmannssveen inn som nye aksjonærer senere.

### 1.1 Nøkkelforutsetninger

Følgende er bestemt av brukerinput 2 og rammer alle tre alternativene likt:

- **Konsernlånet KW→KWE (10,6 MNOK) skal bevares uendret.** Konvertering til egenkapital er forkastet. Agent 1s hovedanbefaling (Alternativ 1 i seksjon C1) er dermed ikke tilgjengelig.
- **Ingen advokater.** AI produserer dokumentasjonen, Varder AS er revisor og kvalitetssikrer, Orkla Regnskap leverer tall.
- **Fisjon først, deretter emisjon** mot tingsinnskudd fra Brandsegg og Lagmannssveen. Dette gjelder i alle alternativer — aksjonærkontinuitet etter sktl. § 11-7 [verifiseres fase 10] krever at nye aksjonærer tas inn utenfor fisjonen.
- **Rentejustering** av konsernlånet fra 9,2 % ned mot markedsrente (ca. 6 %) anbefales uansett struktur (internprising etter sktl. § 13-1 [verifiseres fase 10]).
- **Fisjonsstikkdag:** 01.01.2026 hvis Varder bekrefter at tilbakedatering er mulig; ellers 01.01.2027.

### 1.2 Felles risikoer uansett alternativ

- **5. oktober-fristen er passert med 7 dager** per 12.10.2026 — alle alternativer må inn ASAP; Alt C har noe lengre operativ gjennomføringstid som drøftes nedenfor.
- **Konkursvarsel fra Intrum** forkynt 13.10.2026, frist 27.10.2026. Må stabiliseres parallelt med struktur-arbeidet i alle tre alternativer — valg av struktur endrer ikke behovet for å nøytralisere konkursvarselet før fisjonsvedtak.
- **Partsstatus** i DSB-søknad (frafall tvangsmulkt), Sivilombud-klage og TBRTs tvangsmulktsak er stilet til KWE som juridisk person. Alt som bryter denne identiteten utløser risiko for partsendring i verserende saker.
- **MVA-justeringsavtale** for Grønnegata 10 (fradragsført MVA på historisk oppussing) må på plass i alle alternativer der Grønnegata-eiendommen overføres til ny juridisk person — se mval. § 9-3 verbatim.

---

## 2. Alternativ A — Trippel-utfisjonering under KodeWorks AS

```
KodeWorks AS
├── KodeWorks Eiendom AS (fortsettende, holding)
├── Fjordgata 30 AS (nytt)
└── Grønnegata 10 AS (nytt)
```

Standard fisjon med nystifting etter aksjeloven kap. 14 [verifiseres fase 10]. KWE forblir som overdragende/fortsettende selskap. Vederlagsaksjer i FG30 AS og GG10 AS utstedes til aksjonæren i KWE, dvs. KodeWorks AS. Resultatet er at KodeWorks AS blir direkte eier av alle tre.

### 2.1 Skatterettslig gjennomførbarhet

Rett fram. Skattefri fisjon etter sktl. kap. 11 [verifiseres fase 10] med skattemessig kontinuitet. Aksjonærkontinuitet er bevart (KodeWorks AS er eneeier både før og etter — bare utvider porteføljen med to nye datterselskaper). Omgåelsesnorm (sktl. § 13-2 [verifiseres fase 10]) er lite relevant så lenge fisjonen har reell forretningsmessig begrunnelse (MVA-strategi, risikoseparasjon, nye aksjonærer — alle dokumentert).

### 2.2 Dokumentavgift

Fritak for selskapsrettslig omorganisering (dokumentavgiftsloven § 7 [verifiseres fase 10]) gjelder for begge hjemmelsoverganger (Fjordgata 30 til FG30 AS, Grønnegata 10 til GG10 AS). Standard anvendelse, lav risiko.

### 2.3 MVA-konsekvenser

Grønnegata 10 har historisk fradragsført MVA. Overføringen til GG10 AS utløser i utgangspunktet justering etter mval. § 9-2 tredje ledd ved overdragelse av kapitalvare etter § 9-1 andre ledd bokstav b. Dette unngås ved justeringsavtale etter § 9-3 — overtakende GG10 AS overtar justeringsforpliktelsen. GG10 AS må være MVA-registrert eller frivillig registrert etter § 2-3 ved overtakelse (siden kontorene leies ut til næringsdrivende leietakere, er frivillig registrering på plass).

FG30 AS registreres etter fisjon — ingen justeringsplikt utløses i KWE fordi KWE ikke har vært MVA-registrert for Fjordgata 30-prosjektet. Tilbakegående avgiftsoppgjør etter mval. § 8-6 [verifiseres fase 10 — 3-årsfrist] i FG30 AS fanger byggefasens inngående MVA (estimert 6,2 MNOK over hele byggefasen; retrospektivt 2024–2026 YTD ca. 250–375 TNOK).

### 2.4 Konsernlånet KW→KWE (10,6 MNOK)

**Kjerneproblemet i Alt A.** Siden konvertering til EK er avvist, må lånet enten:

1. **Bli hos fortsettende KWE** — da blir KWE «tom skalk»: eier bare aksjer i to datterselskaper (bokført 2 × 30 000 kr) pluss litt bank, men skylder 10,6 MNOK til morselskapet. Bokført EK blir sterkt negativ (anslagsvis –10,5 MNOK før aksjeverdiene regnes med). Dette er strukturell insolvens og utløser handleplikt etter asl. § 3-5 [verifiseres fase 10] og styreansvar etter asl. § 17-1 [verifiseres fase 10].
2. **Fordeles mellom de tre selskapene** — proporsjonalt etter netto bokført verdi eller etter en annen nøkkel. Agent 4 har foreslått 6,6 MNOK / 2,5 MNOK / 1,5 MNOK (KWE/FG30/GG10). Krever skriftlig samtykke fra kreditor KodeWorks AS til debitorbytte (standard obligasjonsrettslig prinsipp — kreditor må samtykke). Siden samme konsernkontrollør står bak begge selskaper, er samtykket formalia — men styrevedtak i KodeWorks AS må protokolleres.

Både 1 og 2 har et felles svakhetspunkt: fortsettende KWE ender uansett med en negativ eller marginal bokført EK som vanskeliggjør forsvarlighetsvurdering etter asl. § 3-4 [verifiseres fase 10]. Varders fisjonserklæring kan bli vanskelig å få signert hvis bokført EK er klart negativ. Mitigering krever enten (a) morselskapsgaranti fra KodeWorks AS, (b) aksjonærinnskudd fra KodeWorks AS inn i KWE samtidig med fisjonen, eller (c) at Varder godtar virkelige verdier av aksjene i datterselskapene som dekning (= Alt C-tankegangen uten mellomholdings-strukturen).

### 2.5 Tilskuddsoverføring

Tilsagn stilet til KWE: KMF 750 TNOK, BYA 500 TNOK, UNI 100 TNOK, Enova KL 400 TNOK, Enova OM 500 TNOK. I Alt A må alle fem flyttes fra KWE til FG30 AS. Dette krever:

- Skriftlig anmodning til hver tilskuddsgiver med redegjørelse for fisjonsgjennomføring og overføring av prosjektansvar.
- Enova OM krever **forutgående skriftlig samtykke** per Enovas standardvilkår — behandlingstid 4–8 uker (ikke verifisert; må åpnes dialog).
- Enova KL sluttrapport (frist 25.12.2026) må leveres fra enten KWE (hvis fisjon ikke er ferdig) eller FG30 AS (etter mottakerendring). Agent 4s anbefaling om å anmode 80 % utbetaling (ca. 320 TNOK) **før fisjon** fra KWE er praktisk — forenkler sluttoppgjøret.

Dette er administrativt tungt men gjennomførbart. Standardprosedyre som tilskuddsgivere forventer ved selskapsrettslige omorganiseringer.

### 2.6 Partsstatus i pågående saker

KWE forblir som rettssubjekt — partsstatus i DSB-søknad, Sivilombud-klage, Intrum konkursvarsel og TBRT tvangsmulktsak bevares ved fisjonen. Dette er en klar styrke ved Alt A. Men tvangsmulktvedtaket må overføres til ny eier (FG30 AS) som pliktsubjekt fra fisjonstidspunktet; selve det påløpte beløpet (184 TNOK) og eventuell tilbakevirkende innkreving (428 TNOK) blir hos fortsettende KWE etter Agent 3s Alt 1A.

### 2.7 Omstøtelsesrisiko (dekningsloven kap. 5)

**Dette er Alt As største svakhet.** Dekningsloven § 5-9 [verifiseres fase 10] rammer utilbørlige disposisjoner som forringer bomassen for kjent krav. 10-årsfristen gjelder mot nærstående etter § 1-5. Hvis fortsettende KWE ender med bokført EK –10,5 MNOK (konsernlånet hos KWE) eller nær null (konsernlånet fordelt), har fisjonen *skapt* en konstruksjon der TBRT som kreditor har strukturelt dårligere dekning enn før fisjonen. Dette er den sterkeste juridiske angrepsvinkelen i Agent 1s D1.

Agent 1s forsvar var konvertering av konsernlånet til EK. Siden dette nå er forkastet, må Alt A finne annen dekning:

- Morselskapsgaranti fra KodeWorks AS på minst 1 MNOK direkte til TBRT (Agent 3s mekanisme C). Krever at KodeWorks AS er solvent og at garantien beregnes på markedsvilkår (asl. § 3-9 [verifiseres fase 10], ellers risiko for omklassifisering til utbytte etter sktl. § 10-11 [verifiseres fase 10]).
- Aksjeverdiene i FG30 AS og GG10 AS kan hevdes å gi reell dekning dersom virkelige verdier legges til grunn. Men bokført dekning er svak, og en konkursbobestyrer kan utnytte avviket.

### 2.8 Operativ kompleksitet

Mellomnivå. Dokumenter som må produseres:

- Fisjonsplan med vedlegg (begrunnelse, åpningsbalanser × 3, revisorerklæring etter asl. § 14-4 [verifiseres fase 10]).
- Styrevedtak og generalforsamlingsvedtak i KWE og KodeWorks AS.
- Debitorbytte-avtale for konsernlånet hvis det fordeles (eller samtykkedokumentasjon fra KodeWorks AS hvis det ligger i fortsettende KWE).
- Justeringsavtale etter mval. § 9-3 for Grønnegata-eiendommen.
- DNB-samtykke og nytt gjeldsbrev for Grønnegata-lånet.
- Melding til Brreg (én fisjonsmelding dekker alle tre selskaper).
- Varder-attestasjon (ett konsolidert oppdrag).

Tidsramme: fisjonsvedtak uke 44–46, kreditorfrist 6 uker, Brreg-registrering medio februar 2027. Dette er brukerens ambisjon og er innenfor «noen dager/uker over 5.10-fristen» per Varder.

### 2.9 Framtidige søknader og bankfinansiering

Fjordgata 30 AS blir «ryddig» selskap: ingen pant, bokført EK ca. 6,2 MNOK (etter konsernlån-andel 2,5 MNOK fordeles dit), ren MVA-situasjon etter registrering. Framtidige KMF/BYA/Enova/Skattefunn-søknader går fra FG30 AS. Byggelån-sondering i Q2–Q3 2027.

**Bankvennlighet:** DNB-dialogen for Grønnegata er allerede på plass. FG30 AS kan sondere flere banker fritt — ingen cross-collateral problematikk siden Fjordgata 30 var ubelastet.

### 2.10 Konsekvens for Brandsegg/Lagmannssveen-emisjonen

Emisjon i FG30 AS 6–8 uker etter fisjonsregistrering (Agent 1 B2.4-anbefaling for å unngå serietransaksjonsrisiko etter sktl. § 13-2). Resultat: Brandsegg og Lagmannssveen eier aksjer i FG30 AS; KodeWorks AS fortsatt majoritetseier. Verdifastsettelse av tingsinnskudd (fysisk inventar + rapporter/planverk/tegninger) må gjennomføres av Varder etter asl. § 2-6 [verifiseres fase 10]. Dokumentasjon av eiendomsrett for immaterielle verdier er en kjent utfordring (må være personlige, ikke levert gjennom KMTE/HRP som ledd i konsulentoppdrag).

### 2.11 Samlet styrke/svakhet — Alt A

**Styrker:**
- Standardløsning. Varder har «sannsynligvis gjort dette før».
- Partsstatus bevart i KWE.
- Fjordgata 30 AS blir «ryddig» og enkelt å bygge bankrelasjon og tilskuddsstruktur rundt.
- Dokumentavgift-fritak greit.
- Én fisjonsmelding dekker alt.

**Svakheter:**
- **Fortsettende KWE blir strukturelt sårbart** uansett om konsernlånet ligger der i helhet eller fordeles. Bokført EK blir enten sterkt negativ eller marginal.
- **Dekningslov-angrep (§ 5-9) står svakt forsvart** når konvertering er forkastet. Krever morselskapsgaranti og/eller aksjonærinnskudd for å oppnå dekning.
- Styreansvar- og handleplikt-risiko (asl. § 17-1, § 3-5) forblir høy dersom konsernlånet blir i KWE.
- Varders fisjonserklæring kan bli vanskelig uten tilleggsgrep.
- Fem tilskudd må flyttes administrativt.

---

## 3. Alternativ B — Dobbel fisjon uten fortsettende KWE

```
KodeWorks AS
├── Fjordgata 30 AS (nytt)
└── Grønnegata 10 AS (nytt)
```

KWE opphører som rettssubjekt. Alle eiendeler og forpliktelser fordeles mellom FG30 AS og GG10 AS.

### 3.1 Skatterettslig gjennomførbarhet

«Likvidasjonsfisjon» eller «full fisjon» — asl. kap. 14 [verifiseres fase 10] regulerer både fisjon der overdragende fortsetter og der det oppløses. Full fisjon skal også være skattefri etter sktl. kap. 11 forutsatt kontinuitet. Aksjonærkontinuitet bevart (KodeWorks AS eier begge nye selskaper, i stedet for ett som nå).

Vilkårene er imidlertid mer krevende: siden overdragende selskap opphører, må **alle** eiendeler og forpliktelser plasseres eksplisitt i fisjonsplanen. Ingen plass til glemte poster. Pågående saker må overføres til ny part. Dette er bokføringsmessig og juridisk mer krevende enn Alt A.

### 3.2 Dokumentavgift

Fritak gjelder som i Alt A. Samme eiendomsoverganger (Fjordgata 30 til FG30 AS, Grønnegata 10 til GG10 AS), bare med forskjell at «avgiverselskapet» etter fisjon ikke eksisterer. Dette endrer ikke avgiftsfritaket.

### 3.3 MVA-konsekvenser

Som i Alt A: justeringsavtale etter mval. § 9-3 for Grønnegata, FG30 AS registreres etter fisjon, tilbakegående oppgjør etter § 8-6 for byggefasen. Men i Alt B må alle MVA-forpliktelser i KWE (konto 2700/2710 — netto 66 TNOK) uttrykkelig plasseres hos ett av de to overtakende selskapene, siden KWE opphører.

### 3.4 Konsernlånet KW→KWE (10,6 MNOK)

Må fordeles mellom FG30 AS og GG10 AS. KWE kan ikke beholde noe av lånet siden selskapet opphører. Fordeling krever KodeWorks AS' samtykke (debitorbytte). Mulig fordeling: proporsjonalt etter netto bokført verdi — anslagsvis 3,2 MNOK / 7,4 MNOK eller tilsvarende. Dette gjør **begge** nye selskaper tyngre belastet enn i Alt A.

Konsekvens for FG30 AS: hvis 3–4 MNOK konsernlån tildeles der, synker bokført EK fra ca. 5,9 MNOK (Agent 4) til ca. 4,5–5,0 MNOK. Fortsatt forsvarlig, men bankpresentasjonen svekkes.

### 3.5 Tilskuddsoverføring

Samme fem tilskudd må overføres til FG30 AS som i Alt A — operativt samme jobb. Men en **tilleggsutfordring**: siden avgiverselskapet KWE opphører, må tilskuddsgivere forholde seg til at originalmottakeren slutter å eksistere. Enova OM-samtykke-prosessen kan bli mer krevende. Enovas vilkårsdokument krever «forutgående skriftlig samtykke»; hvis prosessen trekker ut og KWE allerede er slettet, kan dette komplisere sluttrapport og utbetaling for Enova KL. **Mindre fleksibilitet enn Alt A.**

### 3.6 Partsstatus i pågående saker

**Dette er hovedproblemet med Alt B.** KWE er part i:

- DSB-søknad om frafall av tvangsmulkt (sendt 12.10.2026).
- Sivilombud-klage (sendt 06.10.2026).
- Intrum konkursvarsel sak S2026-026646 (forkynt 13.10.2026).
- TBRT tvangsmulktsak (184 TNOK påløpt, 428 TNOK tilbakevirkende risiko).

Når KWE opphører, må partsstatus overføres til et nytt selskap. Rettslig skjer dette normalt via universalsuksesjon ved fisjon — overtakende selskap trer inn i overdragendes rettsstilling [verifiseres fase 10]. Men i praksis vil forvaltningsorganer og motpart:

- Måtte informeres om partsendring med nytt orgnr., ny signatur-fullmakt.
- Kunne tolke endringen som «manøver» — særlig TBRT og Intrum som har konflikt med KWE. En argumentasjonsåpning for motparter.
- Få flere formelle grep til å kreve stillingsdokumentasjon og trenere behandling.

Verst for Sivilombud-sporet som er sendt 06.10.2026 og venter på behandling. En partsendring midt i prosess vil minst forsinke, i verste fall gjøre klagen uklar for Sivilombudet. For DSB-sporet (frafall tvangsmulkt sendt 12.10.2026) tilsvarende.

For Intrum-sporet er det en annen risiko: når KWE opphører, må konkursvarselet enten (a) falle bort fordi debitor ikke eksisterer, eller (b) rettes mot overtakende selskap. Standard juridisk forståelse er at konkursvarselet retter seg mot debitoren som eksisterte da det ble forkynt, og at Intrum må reprotokollere mot nytt selskap. Praktisk kan dette **være en fordel** (bryter konkursvarselet) — men det er en risikabel strategi fordi Intrum raskt kan fatte nytt varsel mot det selskapet som overtar fordringen (FG30 AS eller GG10 AS, avhengig av fordeling), med samme krav på kort tid.

### 3.7 Omstøtelsesrisiko (dekningsloven kap. 5)

Potensielt tyngre enn Alt A. Når KWE opphører og «flyter inn» i to nye selskaper, kan en konkursbobestyrer eller kreditor hevde at hele strukturen er en kreditorskadelig disposisjon under § 5-9. Særlig fordi:

- Avgiverselskapet forsvinner uten rest.
- Solidaransvaret etter asl. § 14-11 [verifiseres fase 10] gjelder mellom de to overtakende, men det er likevel krevende å kreve en forpliktelse i et selskap som uttrykkelig ikke er plassert der.
- Hvis tvangsmulktforpliktelsen (184 TNOK + eventuell 428 TNOK tilbakevirkende) plasseres hos ett av selskapene, kan TBRT uansett gå subsidiært på det andre — og i tillegg hevde at hele konstruksjonen er § 5-9-stridig.

### 3.8 Operativ kompleksitet

Høyere enn Alt A. Dokumentasjon må være detaljert og uttømmende fordi avgiverselskapet forsvinner. Varders fisjonserklæring må attestere at *alle* eiendeler og forpliktelser er plassert — en revisor-faglig vanskeligere øvelse enn fordeling der overdragende fortsetter. Flere varslingsbrev må sendes (DSB, Sivilombud, TBRT, Intrum, tilskuddsgivere, DNB, leverandører, kunder, Skatteetaten — alle med partsendrings-dokumentasjon).

Tidsrammen blir sannsynligvis litt tyngre enn Alt A, men ikke dramatisk — Brreg-prosessen er den samme.

### 3.9 Framtidige søknader og bankfinansiering

Som i Alt A — FG30 AS blir ryddig, GG10 AS blir fortsatt bokført tynn. Ingen vesentlig forskjell.

### 3.10 Konsekvens for Brandsegg/Lagmannssveen-emisjonen

Som i Alt A — emisjon 6–8 uker etter fisjonsregistrering. Ingen vesentlig forskjell.

### 3.11 Samlet styrke/svakhet — Alt B

**Styrker:**
- Konsernlånet må fordeles — en «avklaring tvunget fram».
- Ingen tom-skalk-holdingsselskap å begrunne.
- Mulig taktisk fordel at Intrums konkursvarsel kan bli stilt mot ikke-eksisterende debitor (men dette er trolig kortvarig gevinst).

**Svakheter:**
- **Partsstatus-problem er alvorlig.** Fire pågående saker får partsendring midt i prosess. Sivilombud-sporet er særlig sårbart.
- **Omstøtelsesrisiko høyere** enn Alt A fordi avgiverselskapet forsvinner uten rest.
- **Operativt mer krevende** — uttømmende plassering av alle poster, flere varslingsbrev.
- **Mindre fleksibilitet overfor tilskuddsgivere** (Enova OM-samtykkeprosessen blir tyngre).
- Ingen klar netto-gevinst over Alt A for driftsformål — fordelingen av konsernlånet må gjøres uansett.

Alt B gir i praksis en marginal operativ forskjell fra Alt A, mens den juridiske og saksbehandlingsmessige risikoen øker vesentlig. **Lite tiltalende.**

---

## 4. Alternativ C — FG30 AS og GG10 AS som datterselskaper av KWE

```
KodeWorks AS
└── KodeWorks Eiendom AS (mellomholding)
    ├── Fjordgata 30 AS (nytt)
    └── Grønnegata 10 AS (nytt)
```

KWE forblir som rettssubjekt og mellomholding. Datterselskapene eier eiendommene direkte.

### 4.1 Mekanismeanalyse — hvordan oppnå strukturen?

Standard fisjon etter aksjeloven kap. 14 utsteder vederlagsaksjer til aksjonæren i overdragende selskap. For KWE betyr dette KodeWorks AS, ikke KWE selv. En «fisjon til seg selv» (KWE som både overdragende og mottakende av aksjene i de nye selskapene) er ikke mulig innenfor aksjelovens standardfisjon.

For å oppnå Alt C må derfor én av følgende mekanismer brukes:

#### Mekanisme C1 — Konserninternoverdragelse (sktl. § 11-21) [verifiseres fase 10]

KWE stifter to datterselskaper (FG30 AS og GG10 AS) med minimum aksjekapital og overdrar hver eiendom som tingsinnskudd mot aksjer i datter («drop-down»). Kjent også som konserninternoverdragelse etter konsernforskriften — sktl. § 11-21 [verifiseres fase 10] (ikke § 11-2 som preamblet feilaktig antok; § 11-2 regulerer fusjon). Betingelsene er typisk:

- Overdragende og mottakende må være i samme skattekonsern (eieinnflytelse ≥ 90 %).
- Skattemessig kontinuitet (inngangsverdier videreføres).
- Oppfylles kravene, utløses ingen realisasjonsbeskatning.

Dette er **ikke en fisjon** men en virksomhetsoverdragelse — regnskapsmessig behandlet som salg av eiendel til datter mot aksjer. Operativt rimelig enkelt: stiftelsesdokument + tingsinnskuddserklæring (asl. § 2-6) + revisorattestasjon av eiendomsverdi for hver eiendom.

**Kjent risiko:** Konserninternoverdragelse etter sktl. § 11-21 har andre betingelser enn fisjon etter kap. 11-4 flg. — kontinuitet er fullstendig, men hvis selskapet går ut av konsernet innen bindingstid (typisk 3 år; må verifiseres fase 10), kan skattefriheten reverseres med tilbakevirkende kraft. Dette er mindre relevant for FG30/GG10-strukturen siden begge forblir heleide datterselskaper i overskuelig framtid — men Brandsegg/Lagmannssveen-emisjonen i FG30 AS reduserer KWEs eierandel. Verifisering: er det nok at **KodeWorks AS-konsernet** fortsatt har ≥ 90 % eierkontroll, eller må **KWE direkte** eie ≥ 90 % av FG30 AS kontinuerlig? Dette er en avgjørende detalj som må avklares med Varder.

#### Mekanisme C2 — Fisjon først (Alt A), deretter tingsinnskudd av aksjer fra KodeWorks AS til KWE

Gjennomfør Alt A som standard fisjon → KodeWorks AS blir direkte eier av FG30 AS og GG10 AS → deretter overfører KodeWorks AS aksjene i de to datterselskapene til KWE som tingsinnskudd (kapitalforhøyelse i KWE etter asl. § 10-2 flg. [verifiseres fase 10]).

Dette er to konsekutive transaksjoner. Skattekonsekvens:

- Fisjonen er skattefri etter sktl. kap. 11 (standard).
- Tingsinnskuddet (aksjer fra morselskap til datter) kan være skattefritt etter fritaksmetoden (sktl. § 2-38 [verifiseres fase 10]) siden KodeWorks AS er aksjeselskap og aksjene i datterselskapene er «kvalifiserende aksjer».
- Men hvis innskuddet behandles som realisasjon hos KodeWorks AS, kan det utløse en bokført transaksjon selv om skatten er null.

Operativt: først fisjonsmelding til Brreg, så etter registrering en kapitalforhøyelses-melding for KWE med tingsinnskudd av aksjer. To separate Brreg-prosesser. Tidstillegg: trolig 4–8 uker etter fisjonsregistrering før Alt C-strukturen er på plass.

#### Mekanisme C3 — Fisjon-fusjon (asl. kap. 13 + 14)

Overdragende KWE fisjoneres og de utskilte delene fusjoneres samtidig inn i to allerede eksisterende selskaper (som da ville vært KodeWorks AS og en nystiftelse). Men dette passer *ikke* strukturelt for Alt C — her vil overtakerselskapene bli KodeWorks AS, ikke KWE som mellomholding. Mekanismen oppnår Alt A, ikke Alt C. **Forkastet.**

#### Vurdering av mekanismene

Mekanisme **C1 (konserninternoverdragelse)** er den enkleste tekniske veien. Det er den mest praktiske realiseringen av Alt C og unngår å måtte gå via fisjon først. Men den har en vesentlig juridisk konsekvens: **det er ikke en fisjon**. Dermed bortfaller alle fisjonsspesifikke virkemidler — særlig **solidaransvaret etter asl. § 14-11** mellom selskapene (som gir TBRT subsidiær tilgang til hele konsernet), og de særlige **MVA-overføringsreglene i mval. § 9-3** som er skrevet for fisjon/fusjon. Konserninternoverdragelse er en vanlig eiendomsoverdragelse der justeringsplikten utløses med mindre overtakende selskap er MVA-registrert *og* avtale om overføring av justeringsforpliktelsen inngås — § 9-3 åpner for dette også ved alminnelig overdragelse mellom MVA-registrerte, så dette fungerer så lenge GG10 AS er frivillig registrert når overføringen skjer.

Mekanisme **C2 (fisjon først, så aksjeinnskudd)** er juridisk sikrere på fisjons-delen men innebærer to konsekutive prosesser som totalt gir lengre tidsbruk. Dekningslov-vinkelen på aksjeinnskudd-delen må vurderes — hvis KodeWorks AS flytter aksjer med verdi til KWE, kan en kreditor mot KodeWorks AS angripe det (men KodeWorks AS er ikke part i noen pågående sak, så dette er mindre relevant).

Dokumentavgift: **I begge mekanismer** gjelder fritaket (dokumentavgiftsloven § 7 [verifiseres fase 10] — fritak for omorganisering av selskap med skattemessig kontinuitet). Men **C1** innebærer én hjemmelsovergang (KWE → FG30 AS; KWE → GG10 AS), mens **C2** innebærer samme én hjemmelsovergang i fisjonen (KWE → FG30 AS/GG10 AS) men ingen hjemmelsovergang i aksjeinnskuddet (aksjer er løsøre, ikke fast eiendom). Dokumentavgift-mengden er den samme.

**Anbefalt mekanisme for Alt C: C1 (konserninternoverdragelse)** fordi den unngår å måtte avregistrere KWE som eiendomseier i to omganger og er en enklere forretningsmessig transaksjon. Men hvis Varder vurderer at bindingstidvilkårene i sktl. § 11-21 er problematiske for Brandsegg/Lagmannssveen-emisjonen (dvs. at FG30 AS-aksjer kommer utenfor konsernet), bør C2 velges som fallback.

### 4.2 Skatterettslig gjennomførbarhet

Avhenger av mekanisme. C1 krever at vilkårene for konserninternoverdragelse etter sktl. § 11-21 oppfylles — særlig eierandel og bindingstid [verifiseres fase 10]. C2 bygger på standard fisjon og aksjeinnskudd. Begge er skattefrie når de utføres korrekt.

Omgåelsesnorm (sktl. § 13-2) er lite relevant så lenge forretningsmessig begrunnelse er dokumentert.

### 4.3 Dokumentavgift

Samme fritaksgrunnlag som Alt A. Lav risiko.

### 4.4 MVA-konsekvenser

Samme som Alt A. GG10 AS må være frivillig registrert ved overtakelsen, og justeringsavtale etter mval. § 9-3 må signeres samtidig. For FG30 AS registreres selskapet etter overdragelsen og tilbakegående oppgjør etter mval. § 8-6 fanger byggefasens inngående MVA.

### 4.5 Konsernlånet KW→KWE (10,6 MNOK)

**Dette er Alt Cs hovedstyrke.** Lånet forblir uendret i KWE. Ingen debitorbytte, ingen fordeling, ingen reforhandling som del av fisjonsprosessen. Rentejustering (ned mot markedsrente) kan gjøres som egen beslutning uavhengig av struktur-oppsettet. Internprising-vurdering etter sktl. § 13-1 bør gjøres uansett, men dette er en adskilt sak.

**Dekningsgrunnlag:** KWE eier aksjer i FG30 AS og GG10 AS med reell virkelig verdi. Agent 4s skisse: aksjer FG30 AS ca. 7–8 MNOK, aksjer GG10 AS ca. 2–3 MNOK — totalt 9–11 MNOK i aksjeverdier mot 10,6 MNOK konsernlån. Bokført EK i KWE blir dermed marginal (–0,5 til +0,5 MNOK) men nær null, ikke sterkt negativ som i Alt A med lånet værende hos KWE. Virkelig verdi gir margin — særlig når FG30 AS' bygg og driftsplan modnes.

Dette gir handleplikt (asl. § 3-5) og styreansvar (asl. § 17-1) mye bedre fundament enn Alt A: KWE er ikke tom skalk, det eier reelle driftsselskaper. Forsvarlighetsvurdering (asl. § 3-4) blir vesentlig lettere å dokumentere positivt.

### 4.6 Tilskuddsoverføring

Litt mer nyansert enn Alt A. Alt C har to muligheter:

**Mulighet C.i — Tilskudd blir hos KWE som mellomholding.** KWE forblir mottaker og formelt ansvarlig for tilskuddsgjennomføring; de fem tilsagn trenger ikke overføres til FG30 AS. Praktisk innebærer dette at FG30 AS fakturerer KWE for byggearbeid, KWE betaler og krever tilskudd. Dette er mer kronglete regnskapsmessig og tilskuddsgivere kan motsette seg at prosjektgjennomføringen er i et annet selskap enn mottaker. Særlig Enova-sporet har klausuler om prosjektansvar.

**Mulighet C.ii — Tilskuddene flyttes til FG30 AS likevel.** Operativt som i Alt A. Dette er sannsynligvis det tilskuddsgivere ønsker — det er FG30 AS som gjennomfører prosjektet, og tilskuddsgivere liker å se mottaker = gjennomfører.

**Anbefaling:** Flytt tilskuddene til FG30 AS uansett (C.ii). Alt C gir ingen reell fordel på tilskuddsiden — administrativt samme jobb som Alt A.

**Men:** Enova OM-samtykke-prosessen blir **marginalt enklere** i Alt C fordi KWE forblir som rettssubjekt gjennom endringen. Hvis Enova krever at mottakerendring forankres i overdragende selskaps styrevedtak, er dette lettere å dokumentere i Alt C enn i Alt A (hvor KWE's styre også eksisterer, men vedtakene koordineres annerledes).

### 4.7 Partsstatus i pågående saker

Som i Alt A — KWE forblir rettssubjekt. Partsstatus i DSB-, Sivilombud-, Intrum- og TBRT-sakene er bevart. **Likeverdig styrke med Alt A på dette punktet.**

### 4.8 Omstøtelsesrisiko (dekningsloven kap. 5)

**Dette er Alt Cs sterkeste punkt.** KWE etter omorganisering har aksjer i to driftsselskaper med samlet virkelig verdi 9–11 MNOK (anslag Agent 4). Konsernlånet 10,6 MNOK er dekket av dette. Fortsettende KWE er **ikke** strukturelt insolvent — bokført EK marginalt negativ men virkelig verdi positiv.

Dekningslov § 5-9-angrepet mot «tom skalk» (Agent 1 D1) **nøytraliseres** — fisjonen flytter verdier fra én balanse til to datterselskaper, og KWE som eier av aksjene har samme totalverdi som før (bortsett fra at Brandsegg/Lagmannssveen-emisjonen senere utvanner FG30 AS-andelen noe).

**Dette er sentralt gitt at brukeren har forkastet konvertering av konsernlånet.** Alt A har mistet sin standardforsvar mot § 5-9; Alt C har en strukturell løsning.

**Risiko-rest i Alt C:** Hvis Brandsegg/Lagmannssveen senere får en vesentlig andel i FG30 AS (f.eks. 20 %), reduseres KWEs aksjeverdi i FG30 AS tilsvarende. Men dette skjer mot *motytelse* (tingsinnskudd fra Brandsegg/Lagmannssveen), så KWE får samme nettoverdi så lenge innskuddet er markedsmessig verdsatt. Dekningsgrunnlaget forblir intakt.

### 4.9 Operativ kompleksitet

Avhenger av mekanisme.

**Mekanisme C1 (konserninternoverdragelse):**
- Stiftelse av FG30 AS og GG10 AS med minimum aksjekapital.
- Tingsinnskuddserklæring for hver eiendom (asl. § 2-6).
- Revisorattestasjon av eiendomsverdi (Varder).
- Overdragelsesdokumenter (kjøpekontrakt / overdragelsesavtale) KWE → datter for hver eiendom.
- Hjemmelsovergang til Kartverket for hver eiendom (dokumentavgift-fritak etter dokumentavgiftsloven § 7).
- Justeringsavtale mval. § 9-3 for Grønnegata.
- DNB-samtykke og nytt gjeldsbrev for Grønnegata-lånet.
- Melding til Brreg (stiftelsesmeldinger for FG30 AS og GG10 AS; ingen fisjonsmelding).
- Ikke kreditorvarsel-perioden på 6 uker som ved fisjon etter asl. kap. 14 — dette er en operativ tidsgevinst. Men dette skal verifiseres: § 11-21-konserninternoverdragelse kan ha egne kreditorbeskyttelsesregler [verifiseres fase 10].

**Mekanisme C2 (fisjon + aksjeinnskudd):**
- Alle dokumenter i Alt A.
- Pluss kapitalforhøyelses-protokoll og tingsinnskuddserklæring i KWE for aksjene i FG30 AS og GG10 AS.
- Pluss ny Brreg-melding for KWE kapitalforhøyelsen etter at fisjonen er registrert.
- Totalt lengre tidsbruk.

**Tidsramme:**
- C1: kan være raskere enn Alt A siden ingen fisjon og dermed ingen 6-ukers kreditorfrist (hvis § 11-21 ikke har egen kreditorfrist — verifiseres). Realistisk gjennomføring: 4–8 uker fra oppstart.
- C2: Alt A-tidsramme + 4–8 uker ekstra for aksjeinnskudd. Totalt 3–5 måneder.

**Varders rolle:** Varder må være komfortabel med mekanismen. Konserninternoverdragelse er mindre vanlig enn fisjon og krever at Varder bekrefter at vilkårene for sktl. § 11-21 oppfylles. Hvis Varder foretrekker standard fisjon, blir C2 den aktuelle veien.

**Risiko ved AI-produsert dokumentasjon uten advokat:** Konserninternoverdragelse etter § 11-21 har formelle krav som er mindre godt dokumentert i åpne kilder enn vanlig fisjon. AI-produksjon må kompensere med særlig grundig verbatim lovreferanse-nedlasting i fase 10, og Varders kompetanse må dekke dette området konkret. Hvis Varder sier «fisjon kan jeg, § 11-21 har jeg mindre erfaring med», bør Alt A velges fremfor Alt C via C1.

### 4.10 Framtidige søknader og bankfinansiering

**Marginalt bedre enn Alt A** på bankforhandling: FG30 AS er fremdeles «ryddig» og uten pant. Byggelån-forhandlinger er like greit. Men:

- Banken kan kreve **morsselskapsgaranti** fra KWE (ikke KodeWorks AS) ved byggelån, siden KWE er direkte eier. KWE som mellomholding har aksjer og dermed garantevne, men ikke like sterk som KodeWorks AS. Hvis bank krever morsselskapsgaranti opp i tredje ledd (KodeWorks AS), gir Alt C ingen fordel over Alt A.
- Cross-collateral mellom FG30 AS og GG10 AS kan foreslås av bank siden begge er i samme eierlinje. Dette er standard byggelån-vilkår. Men brukeren kan motsette seg det — kan reforhandles.

Framtidige tilskuddssøknader fra FG30 AS er like greit som i Alt A. KMF/BYA/Enova-forhold påvirkes ikke av struktur-nivået over FG30 AS.

### 4.11 Konsekvens for Brandsegg/Lagmannssveen-emisjonen

Emisjon i FG30 AS endrer eierfordelingen *innenfor* FG30 AS: KWE får en lavere andel (f.eks. 80 % i stedet for 100 %). KodeWorks AS' indirekte eierskap i FG30 AS er dermed også 80 % (via KWE som fremdeles er 100 % eid av KodeWorks AS).

**Konsernkontroll-implikasjon for sktl. § 11-21:** Hvis vilkåret for konserninternoverdragelse er at **KWE direkte** eier ≥ 90 % av FG30 AS, må Brandsegg/Lagmannssveen-andelen holdes under 10 % — begrenset. Hvis vilkåret er **konsernmessig** ≥ 90 % (dvs. KodeWorks AS-konsernet samlet eier ≥ 90 %), har det samme utfallet siden KWE er heleid av KodeWorks AS.

**Dette er en kritisk detalj Varder må avklare.** Hvis bindingstid-vilkåret bygges på direkte KWE-eierskap, kan Brandsegg/Lagmannssveen-emisjonen reversere skattefriheten etter sktl. § 11-21 for FG30 AS-dropdown. Hvis vilkåret bygges på konsernmessig eierskap, er det ingen konflikt — konsernet eier fortsatt 100 % av KWE, og KWE eier ≥ 90 % av FG30 AS.

**Tidsmessig avstand mellom konserninternoverdragelse og emisjon** bør være minst 3–6 måneder for å unngå serietransaksjon-argumentet etter sktl. § 13-2. Litt kortere enn Alt A (6–8 uker fra fisjon til emisjon) kan kreves fordi § 11-21-bindingstiden er lenger — men dette avhenger av om bindingstiden tolkes som absolutt skranke mot utvanning eller som skranke mot *konsernutgang*.

**C2-fallback:** Hvis dette blir en reell bekymring, kan Alt C via C2 (fisjon først, så aksjeinnskudd fra KodeWorks AS til KWE) løse det — § 11-21 er da ikke anvendelig på FG30 AS-trinnet. Da gjelder fisjonsregelverket, og Brandsegg/Lagmannssveen-emisjonen bruker Agent 1 B2.4-avstanden (6–8 uker).

### 4.12 Samlet styrke/svakhet — Alt C

**Styrker:**
- **Konsernlånet forblir uendret** — eksakt brukerens ønske.
- **Dekningslov § 5-9-angrepet nøytraliseres** fordi KWE eier reelle aksjeverdier.
- **Styreansvar og handleplikt** vesentlig redusert sammenlignet med Alt A.
- **Partsstatus bevart** i alle pågående saker.
- **Varders fisjonserklæring blir enklere** å få signert fordi forsvarlighetsvurderingen er lettere.
- **Operativt enklere konsernlåns-struktur** (ingen debitorbytte-dokumentasjon).

**Svakheter:**
- **Mekanisme må velges med omhu.** C1 er den tekniske veien; krever at Varder er komfortabel med sktl. § 11-21.
- **Konsernmessig eierandel-vilkår** i § 11-21 må avklares — kan påvirke Brandsegg/Lagmannssveen-emisjonen.
- **Litt lengre tidsramme hvis C2 velges** (fisjon + aksjeinnskudd = to Brreg-prosesser).
- **Mindre kjent mekanisme** for mange, inkludert Varder sannsynligvis mer erfaring med fisjon. Hvis Varder foretrekker fisjonsveien, må C2 velges.
- **Alt A-styrker beholdes** men ikke forsterkes på bank/tilskudd/MVA-fronten.

---

## 5. Sammenligningstabell

| Dimensjon | Alt A — Trippel | Alt B — Dobbel | Alt C — Mellomholding |
|---|---|---|---|
| 1. Skatterett | Rett fram (sktl. kap. 11) | Rett fram men krever uttømmende fordeling | Avhenger av mekanisme (C1 § 11-21 eller C2 fisjon+aksjeinnskudd); begge kan være skattefri |
| 2. Dokumentavgift | Fritak | Fritak | Fritak |
| 3. MVA | Standard — § 9-3 justeringsavtale, § 8-6 tilbakegående | Standard, men KWE-saldi (f.eks. konto 2700/2710) må plasseres eksplisitt | Som Alt A |
| 4. Konsernlån | Må fordeles eller bli i tom KWE — begge problematiske | Må fordeles mellom FG30 og GG10 — begge belastes | **Uendret i KWE** — eksakt brukerønske |
| 5. Tilskudd | Alle fem flyttes til FG30 AS | Som Alt A, men avgiverselskap forsvinner → mer kronglete | Alle fem flyttes (eller forblir i KWE med mindre fleksibilitet) |
| 6. Partsstatus | Bevart i KWE | **Krever partsendring i 4 saker** | Bevart i KWE |
| 7. Dekningslov § 5-9 | **Svakt forsvar** uten konvertering | Potensielt tyngste angrep (ingen rest-skalk) | **Nøytralisert** — KWE eier aksjeverdier |
| 8. Operativ kompleksitet | Mellomnivå | Høyere (uttømmende, flere varsler) | C1 moderat/raskt; C2 lengre |
| 9. Bank/framtid | Fjordgata 30 AS ryddig | Som Alt A | Som Alt A; marginalt bedre dekning |
| 10. Nye aksjonærer | Standard 6–8 uker etter fisjon | Som Alt A | **C1 krever avklaring av § 11-21-eierandelsvilkår**; C2 som Alt A |

**Oppsummering:** Alt A er «standardløsningen» med kjent svakhet på dekningslov-fronten. Alt B legger til partsstatus-risiko uten tilsvarende gevinst. Alt C løser dekningslov-problemet strukturelt, krever litt mer forarbeid på mekanisme-valget, men adresserer samtidig brukerens hovedkrav (konsernlånet uendret) direkte.

---

## 6. Hovedanbefaling

**Anbefalt struktur: Alt C — FG30 AS og GG10 AS som datterselskaper av KWE.**

**Begrunnelse:**

1. **Konsistens med brukerinput.** Brukeren har eksplisitt forkastet konvertering av konsernlånet. Alt C er den eneste strukturen som bevarer konsernlånet uendret *og* nøytraliserer dekningslov-§ 5-9-angrepet. Alt A tvinger valget mellom bokført insolvent fortsettende KWE eller en fordeling som krever KodeWorks AS-samtykke og likevel ikke løser bokført EK-problemet fullt ut.

2. **Styreansvar- og handleplikt-reduksjon.** Agent 1s styreansvarsvurdering (seksjon A3, Scenario 2) klassifiserte Alt A-fisjon uten konsernlåns-restrukturering som «høy risiko». Alt C eliminerer dette scenarioet fordi KWEs bokførte EK ikke blir sterkt negativ — aksjer i to driftsselskaper gir dekning, og forsvarlighetsvurdering (asl. § 3-4) kan dokumenteres positivt.

3. **Partsstatus beskyttet.** DSB-søknad, Sivilombud-klage, Intrum-sak og TBRT tvangsmulktsak forblir uberørt av struktur-endringen. Alt B utelukkes på dette punktet alene.

4. **Operativ gjennomførbarhet.** Mekanisme C1 (konserninternoverdragelse etter sktl. § 11-21) er teknisk enklere enn fisjon og kan være raskere hvis kreditorbeskyttelsesreglene ikke pålegger samme 6-ukers kunngjøring. Mekanisme C2 (fisjon først, så aksjeinnskudd) er fallback og legger 4–8 uker til tidslinjen.

5. **MVA- og dokumentavgift-fritak like gode.** Alt C har samme fordeler som Alt A på disse frontene.

**Betingelser for anbefalingen:**

- **Varder må bekrefte** at konserninternoverdragelse etter sktl. § 11-21 er en gjennomførbar mekanisme for KWEs eiendomsmasse, og hvilke bindingstidvilkår som gjelder. Hvis Varder foretrekker fisjon fordi det er bedre kjent, velges mekanisme C2.
- **Konsernmessig eierandel-vilkåret** i sktl. § 11-21 må avklares eksplisitt før Brandsegg/Lagmannssveen-emisjonen tidsplanlegges.
- **DNB må samtykke** til at Grønnegata 10 overføres til GG10 AS som datterselskap av KWE (ikke som direkte datter av KodeWorks AS). Dette er mest sannsynlig uproblematisk, men formell signatur må på plass.
- **Rentejustering av konsernlånet** (fra 9,2 % til ca. 6 %) utføres som egen beslutning med dokumentasjon av internprising etter sktl. § 13-1. Dette gjøres uansett struktur og er ikke et Alt C-spesifikt grep.

**Mekanisme-valg innenfor Alt C:**

Primær: **C1 — konserninternoverdragelse etter sktl. § 11-21.** Rimelig enkel, unngår fisjonsprosedyre, bevarer konsernlånet. Krever Varder-bekreftelse.

Fallback: **C2 — standard fisjon etter aksjeloven kap. 14, deretter tingsinnskudd av aksjer fra KodeWorks AS til KWE.** Lengre tidsramme (4–8 uker ekstra). Velges hvis Varder ikke er komfortabel med § 11-21 eller hvis bindingstidvilkåret er problematisk for Brandsegg/Lagmannssveen-emisjonen.

**Mellomform:** Alt A med morselskapsgaranti og aksjonærinnskudd. Hvis ingen av mekanismene i Alt C er anvendbare, må Alt A likevel implementeres, men da forsterkes med 1 MNOK morsselskapsgaranti fra KodeWorks AS direkte til TBRT og minst 1–2 MNOK aksjonærinnskudd i KWE samtidig med fisjonsvedtaket for å løfte bokført EK i fortsettende KWE opp mot positiv. Dette er en nest-best løsning som Agent 1 og Agent 3 har tegnet opp konturene av.

---

## 7. Åpne spørsmål

Følgende må avklares av Varder eller andre parter før strukturen låses:

1. **Vilkårene i sktl. § 11-21 for konserninternoverdragelse.** Særlig: eierandels-vilkår (direkte vs. konsernmessig), bindingstid, og formelle krav. Dette avgjør om mekanisme C1 er anvendelig for FG30 AS på en måte som overlever Brandsegg/Lagmannssveen-emisjonen.
2. **Varders komfort med konserninternoverdragelse** vs. fisjon. Hvis Varder foretrekker fisjon, må C2 brukes.
3. **Dokumentavgift-fritak** etter konserninternoverdragelse — gjelder dokumentavgiftsloven § 7 på samme måte som ved fisjon? Antatt ja [verifiseres fase 10].
4. **Kreditorbeskyttelsesregler** ved konserninternoverdragelse. Fisjon etter aksjeloven kap. 14 har 6-ukers kreditorvarsel; har § 11-21-overdragelser tilsvarende?
5. **DNBs holdning** til at Grønnegata 10 flyttes til GG10 AS som datterselskap av KWE (ikke KodeWorks AS). Krever skriftlig samtykke.
6. **Enova OM-samtykke-prosessen.** Behandlingstid 4–8 uker antatt; ikke verifisert. Må åpnes dialog uansett struktur.
7. **Konsernlåns-rentejustering.** Markedsrente 6 % er anbefalt; må protokolleres mellom KodeWorks AS og KWE med dokumentasjon av internprising etter sktl. § 13-1. Skje som egen avtale, uavhengig av struktur-valget.
8. **Fisjonsstikkdag.** Hvis Alt C via C1: ingen fisjonsstikkdag, men overdragelsesdato for hver eiendom. Hvis Alt C via C2: fisjonsstikkdag 01.01.2026 eller 01.01.2027 etter Varders vurdering.
9. **Framførbart underskudd (2,46 MNOK)** — hvordan plasseres det ved mekanisme C1 (konserninternoverdragelse)? Standardregelen for fisjon (fordeling etter nettoverdi tilført) gjelder ikke direkte her. Underskuddet forblir i KWE — kan brukes hvis KWE får skattepliktig inntekt (f.eks. konsernbidrag eller utbytte fra datter — begrenset nytteverdi) eller må flyttes gjennom konsernbidrag etter sktl. § 10-4 flg. [verifiseres fase 10]. Dette er en konkret svakhet ved C1 som må vurderes.

---

## 8. Konsekvens for fase 7 og rapport_final

### 8.1 Hvis Alt C vedtas

- **Agent 1 (Fisjonsjurist)** må oppdatere seksjon C1 (konsernlåns-restrukturering) med vurdering av at lånet forblir i KWE uendret. Seksjon A2 (insolvensvurdering) må reformuleres — fortsettende KWE er ikke insolvent når aksjeverdier regnes med. Seksjon D1 (dekningslov § 5-9) nedgraderes fra 5/5 til moderat styrke. Hvis mekanisme C1 velges, må Agent 1 lage egen vurdering av sktl. § 11-21-vilkårene i fase 10-nedlasting av lovteksten.
- **Agent 2 (Prosjektleder)** oppdaterer tidslinje: hvis C1, kan fisjonsvedtak forseres til uke 44 fordi ingen kreditorfrist (hvis bekreftet); hvis C2, legges 4–8 uker til for aksjeinnskudd-prosessen.
- **Agent 3 (Tvangsmulkt-strateg)** opprettholder Alt 1A (tvangsmulktforpliktelsen hos fortsettende KWE) men styrker begrunnelsen med at KWE har reell dekning via aksjeverdier. Morselskapsgaranti kan nedgraderes fra «anbefalt» til «valgfri».
- **Agent 4 (Finans/tilskudd)** omregner åpningsbalanse for KWE: eier aksjer i FG30 AS (bokført 7–8 MNOK virkelig verdi) og GG10 AS (bokført 2–3 MNOK virkelig verdi), skylder 10,6 MNOK til KodeWorks AS. Bokført EK i KWE marginalt negativ men virkelig verdi positiv. Framførbart underskudd blir i KWE (ved mekanisme C1) med redusert praktisk nytteverdi — flagges som konkret svakhet.

### 8.2 Hvis Alt A velges likevel

Alle fase 4-leveranser står. Agent 3s Alt 1A må kompletteres med morsselskapsgaranti fra KodeWorks AS på 1 MNOK direkte til TBRT og aksjonærinnskudd fra KodeWorks AS inn i KWE som del av fisjonsvedtaket (helst 1–2 MNOK) for å løfte bokført EK over null og dokumentere forsvarlighet.

### 8.3 Konsekvens for djevelens advokat (fase 7)

Hvis Alt C vedtas, mister djevelens advokat ett av de sterkeste angrepspunktene (D1 i Agent 1 v2 — strukturell insolvens). To nye angrepsvinkler blir aktuelle:

- **«Konserninternoverdragelse er en omvei for å unngå kreditorbeskyttelses-prosedyre i fisjon.»** Hvis § 11-21-mekanismen velges fordi den unngår 6-ukers kreditorfrist, kan dette tolkes som kreditorsvik. Motangrep: forretningsmessig begrunnelse er klar (MVA-strategi, risikoseparasjon, nye aksjonærer), og § 11-21 er en lovfestet rett som ikke er «omvei» i omgåelsesnormforstand.
- **«Alt C flytter verdier til lavere konsernnivå → KodeWorks AS mister direkte kontroll og dekningsgrunnlag.»** Men KodeWorks AS har aldri hatt driftsinntekter fra Fjordgata 30 — kontrollen går uansett gjennom KWE. Motangrep: strukturen reflekterer eksisterende driftsrealitet.

### 8.4 Rapport_final

Rapport_final må ha en egen seksjon «Valgt struktur» tidlig som fastlegger Alt A, B eller C med begrunnelse. Alle etterfølgende seksjoner (åpningsbalanser, konsernlån, dekning, tidsplan) bygger på strukturvalget.

**Anbefaling for rapport_final-utarbeidelse:** Vent med utkast til brukeren har besluttet strukturvalget. Alternativt: produser rapport_final i to varianter (Alt A med mitigering vs. Alt C), slik at Varder-dialog kan ta utgangspunkt i begge.

---

## 9. Sammendrag av anbefaling

| Spørsmål | Svar |
|---|---|
| Hvilken struktur anbefales? | **Alt C — mellomholding** |
| Hvilken mekanisme? | **C1 (konserninternoverdragelse etter sktl. § 11-21)** primært; **C2 (fisjon + aksjeinnskudd)** som fallback |
| Hvorfor ikke Alt A? | Dekningslov § 5-9-angrepet står svakt forsvart når konsernlånet ikke konverteres; bokført EK i fortsettende KWE blir strukturelt sårbart |
| Hvorfor ikke Alt B? | Partsstatus i fire pågående saker ødelegges; omstøtelsesrisiko høyere; ingen klar netto-gevinst |
| Hovedbetingelser | Varder bekrefter § 11-21-anvendelighet; eierandels-vilkår avklares; DNB samtykker |
| Hvis Alt C ikke er mulig | Alt A med morsselskapsgaranti 1 MNOK og aksjonærinnskudd 1–2 MNOK fra KodeWorks AS |
| Tidsramme Alt C via C1 | Vedtak uke 44–45; gjennomføring medio desember 2026 (hvis ingen kreditorfrist) |
| Tidsramme Alt C via C2 | Vedtak uke 44–46; gjennomføring medio mars 2027 |
| Konsekvens for emisjon | Brandsegg/Lagmannssveen-emisjon 6–8 uker etter overdragelse, med forbehold om § 11-21-bindingstid |

Hovedbeslutningen hos brukeren er: **Alt C eller Alt A med forsterkning?** Begge er juridisk gjennomførbare; Alt C er den strukturelt mest robuste gitt forkastelsen av konsernlåns-konvertering.

---

*Leveransen produsert 2026-10-12 som Agent 6 — Strukturanalytiker.*
