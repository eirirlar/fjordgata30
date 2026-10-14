---
rolle: Agent 1 — Fisjonsjurist
fase: 4 (v2, målrettet andre iterasjon)
dato: 2026-10-12
scope: >
  Lukker motsigelser og hull fra `review_01.md`, besvarer brukerinput av 12.10.2026,
  og gir juridisk vurdering på de nye temaene (MVA-justering, nye aksjonærer med
  tingsinnskudd, Grønnegata-isolering, konsernlån-restrukturering, framførbart
  underskudd, overføring av pålegg). Avslutter med en rangert liste av djevelens
  advokats fem sterkeste angrepspunkter.
grunnlag: >
  v1-filen (`agent_01_fisjonsjurist_v1.md`), review og brukerinput (`review_01.md`,
  `bruker_input_01.md`), de tre andre agentenes v2-filer, mval. kap. 9 verbatim
  (`bakgrunn/lovverk/mval_kap9_justering_av_inngaaende_merverdiavgift.md`),
  Skatteetatens veiledende svar 11.09.2026
  (`bakgrunn/mva/mva_forelopig_svar_skattetaten.md`) og balanse 08.10.2026
  (`bakgrunn/okonomi/Balanserapport - 01.01.2026 - 08.10.2026.csv`).
advarsel: >
  Analyse-only. Mval. kap. 9 er lastet verbatim og refereres eksakt. Alle andre
  paragrafhenvisninger er [verifiseres fase 10] — ikke bruk i leveranser før
  verifikasjon.
---

# Fisjonsjurist — analyse v2

Dette er iterasjon 2. Den bygger på v1 og duplikerer ikke stoff som står der.
Fokus er (A) motsigelser og hull review_01 flagget, (B) nye temaer fra brukerinput,
(C) mindre justeringer, og (D) djevelens advokat-input til fase 7.

En vesentlig ny forutsetning fra regnskapet: KWE **er allerede MVA-registrert**
(orgnr. 920 478 506 MVA). Utgående MVA YTD er kr 81 050 (konto 2700), inngående
kr 15 988 (konti 2710/2711). Dette er nesten utelukkende Grønnegata-utleien
(frivillig registrering § 2-3 for kontor). Fjordgata 30 har ingen registrert
drift — konto 1172 (Renovering FG30 kr 817 151) står bokført uten
MVA-fradragsføring, som bekrefter at inngående MVA på FG30-rehabilitering ikke
er løftet. Dette er avgjørende for seksjon B1 under.

---

## A. Lukking av motsigelser og hull

### A1. Dekningsloven kap. 5 — presise frister

Review_01 flagget inkonsistens mellom min v1 og Agent 3 om frister. Agent 3 og
den interne analysen av 2026-10-11 har operert med «3-måneders vindu» som
overordnet rammeverk; min v1 skilte mellom objektive (§§ 5-2 til 5-8) og
subjektive (§ 5-9) regler. Standard-forståelsen (lærebok, Andenæs,
aksjelovskommentar) er følgende [verifiseres fase 10]:

| Hjemmel | Disposisjon | Frist mot ordinære | Frist mot nærstående |
|---|---|---|---|
| § 5-2 | Gaver, gaveliknende disposisjoner | 1 år før fristdag | 2 år før fristdag |
| § 5-3 | Utbetaling/vederlagsfri overføring til nærstående aksjonær | — | 2 år |
| § 5-5 | Ekstraordinær betaling av gjeld | 3 måneder | 2 år |
| § 5-6 | Pantsettelse til sikkerhet for eldre gjeld | 3 måneder | 2 år |
| § 5-7 | Betaling/sikkerhet etter tvangsfullbyrdelse eller krav | 3 måneder | — (ikke egen nærstående-regel) |
| § 5-9 | Utilbørlige disposisjoner (subjektiv omstøtelse) | **2 år** | **10 år** |

Fjordgata 30 AS og Grønnegata 10 AS er nærstående til fortsettende KWE etter
dekningsloven § 1-5 [verifiseres fase 10] (konsernforbindelse, felles
ledelse, delt eierkrets i KodeWorks AS). For denne fisjonen gjelder derfor:

- **§§ 5-5–5-7:** 3-måneders objektiv frist — rammer *tekniske* disposisjoner
  som ekstraordinær betaling eller pantestillelse. Lite relevant for selve
  fisjonen, men kritisk for parallelle handlinger (f.eks. hvis vi
  tilbakebetaler konsernlånet til morselskapet før/samtidig med fisjonen,
  kan dette rammes).
- **§ 5-2:** Gaver — 2-årsfristen gjelder siden overføringen går til nærstående
  selskaper. Nøytraliseres hvis fisjonen er til markedsverdi og med
  solidaransvar beholdt.
- **§ 5-9:** 2-/10-årsfristen. **Dette er hovedhjemmelen** for fisjonen som
  disposisjon. Mot overtakende selskaper (nærstående) løper altså 10 års
  tilbakevirkende frist.

**Konsekvens for Agent 3:** 3-mnd-vinduet er ikke «fisjonsfristen», men
fristen for parallelle disposisjoner som gjeldsbetalinger og pantestillelser.
Vi må være disiplinerte med rekkefølgen hvis konkursvarselet eskalerer til
reell konkursfare: ingen ekstraordinære betalinger til morselskapet eller
andre nærstående i de 3 månedene som ligger nærmest fristdagen. Fisjonen
selv ligger innenfor § 5-9s lange rekkevidde.

### A2. Konkret insolvensvurdering per 08.10.2026

Balanserapporten gir et bestemt bilde:

| Post | Beløp (kr) |
|---|---:|
| Sum eiendeler bokført | ca. 26 921 658 |
| Sum gjeld (ekskl. EK) | ca. 27 446 238 |
| Bokført egenkapital | ca. –524 580 (etter YTD-resultat) |

**Rent bokført er KWE insolvent per 08.10.2026** — negative verdier, selv før
tvangsmulktforpliktelsen (kr 184 000) og eventuell tilbakevirkende
innkreving (kr 428 000) regnes med.

Insolvens etter dekningsloven og konkursloven krever imidlertid *både*
insuffisiens (gjeld > verdi) *og* illikviditet. For denne vurderingen:

**Insuffisiens.** Bokførte verdier undervurderer eiendelene. Grønnegata 10 har
bokført verdi 18,7 MNOK, men ble kjøpt 2020 for 14,1 MNOK + 5,5 MNOK
oppussing = 19,6 MNOK historisk. Siden rentemarkedet har beveget seg og
sentrumsnære kontoreiendommer i Trondheim fortsatt leies ut, er virkelig
verdi sannsynligvis høyere enn bokført. Fjordgata 30 er bokført 8,15 MNOK
men vurderes i forretningsplanen til vesentlig høyere virkelig verdi (en
rehabilitert minilager-eiendom i Fjordgata-fasade). Hvis virkelige verdier
brukes, er KWE **suffisient** med sannsynlig margin på 5–15 MNOK.

**Illikviditet.** Bankinnskudd 706 TNOK + eventuell Enova KL-anmodning 320
TNOK (hvis utbetalt før fisjon) gir noenlunde dekning for driftsutgiftene
på kort sikt. Men Intrums konkursvarsel på kr 103 452 forfalt 27.10.2026 er
indikator på illikviditet overfor den konkrete fordringshaveren hvis det
ikke gjøres opp. Dekning etter konkursloven § 61 [verifiseres fase 10]
presumerer insolvens når skyldner ikke betaler etter konkursvarsel.

**Konklusjon.** KWE er **ikke insolvent i konkursrettslig forstand** per
08.10.2026 — virkelige verdier gir suffisiens, og likviditeten er ikke
akutt. Men illikviditets-formodningen fra Intrum-varselet henger over
situasjonen og må nøytraliseres (betaling, stans eller rettslig
tingrettsstopp) før fisjonsvedtak. Dette er samme konklusjon som v1,
men nå dokumentert mot regnskapet.

**Men:** Agent 2s beregning viser at fortsettende KWE etter fisjonen (med
Agent 2s foreslåtte fordeling som legger hele konsernlånet 10,6 MNOK der)
får bokført egenkapital på ca. **–10,76 MNOK**. Dette er *strukturell*
insolvens skapt av fisjonen, ikke pre-eksisterende. Hvis denne strukturen
ikke endres før fisjonsvedtak, utløser den:

- **Handleplikt** etter asl. § 3-5 [verifiseres fase 10] — styret må
  umiddelbart kalle inn generalforsamling og foreslå tiltak når
  egenkapitalen er lavere enn forsvarlig (eller halvparten av
  aksjekapitalen, dvs. kr 15 000).
- **Styreansvar** etter asl. § 17-1 — gjennomføring av fisjon som gjør
  selskapet insolvent, uten dokumentert forsvarlighetsvurdering, utsetter
  styret for personlig ansvar.
- **Omstøtelsesrisiko** etter dekningsloven § 5-9 — en kreditor eller et
  framtidig konkursbo kan hevde at fisjonen *skapte* insolvensen i
  fortsettende KWE med den konsekvens at kreditorene (TBRT, Intrum,
  leverandører) ikke lenger har reell dekning.

**Juridisk konklusjon.** Fisjonen kan ikke gjennomføres med Agent 2s
foreløpige fordeling. Konsernlånet må restruktureres **før eller samtidig
med** fisjonsvedtaket (se seksjon C under). Minimum er at fortsettende
KWEs netto bokførte egenkapital holdes positiv per fisjonsstikkdag, og at
dette dokumenteres i styreprotokoll og revisorerklæring.

### A3. Styreansvar etter asl. § 17-1 og handleplikt etter § 3-5

Styreansvar etter asl. § 17-1 [verifiseres fase 10] rammer forsettlig eller
uaktsom skadeforvoldelse mot selskapet, aksjonærer eller tredjeparter.
Objektive betingelser:

1. **Pliktforsømmelse.** Styret må ha opptrådt i strid med loven, vedtektene
   eller sine ulovfestede plikter (forsvarlighetsplikten,
   lojalitetsplikten).
2. **Skade.** Konkret økonomisk tap hos selskapet eller tredjemann.
3. **Årsakssammenheng.** Pliktforsømmelsen må ha forårsaket skaden.
4. **Skyld.** Forsett eller uaktsomhet.

For denne fisjonen er risikoscenarioene:

**Scenario 1 — Fisjon mens konkursvarsel er uavklart.** Hvis styret vedtar
fisjonsplan 27.11.2026 og KWE går konkurs 15.01.2027 etter at Intrum tar
ut nytt varsel: kreditorene og boet kan hevde at styret visste om
illikviditet og gjennomførte en kreditorskadelig disposisjon likevel.
Styreansvar-risiko: **moderat** hvis Intrum-sporet er dokumentert håndtert
(betaling, stans, rettslig stopp) før fisjonsvedtak. **Høy** hvis vedtak
treffes uten at Intrum-sporet er avklart.

**Scenario 2 — Fisjon som gjør fortsettende KWE strukturelt insolvent.**
Dette er A2 ovenfor. Styret vedtar en fordeling som flytter alle verdier
til nystiftede selskaper og lar hele konsernlånet 10,6 MNOK bli i et tomt
holdingselskap. Styreansvar-risiko: **høy** uten dokumentert
konsernlån-restrukturering parallelt.

**Scenario 3 — Fisjon som bryter bero-forutsetningene om brannsikring.** Hvis
TBRT senere hevder at fisjonen er disposisjon i strid med beroen og
innkrever tilbakevirkende mulkt kr 428 000, kan boet hevde at styret burde
ha varslet TBRT og innhentet samtykke. Styreansvar-risiko: **lav til
moderat** hvis TBRT er informert via statusbrev 08.10.2026 og
Brreg-kunngjøring.

**Hva må styret dokumentere for å beskytte seg?**

Følgende skal ligge i styreprotokollen for fisjonsvedtaket, med vedlegg:

1. **Forretningsmessig begrunnelse** for fisjonen (MVA-strategi, bank,
   tilskudd, risikoseparasjon, nye aksjonærer). Ikke bare oppramset — med
   konkrete beløpsestimater og kildehenvisninger (Skatteetatens svar
   11.09.2026, bank-dialog med DNB, tilsagn fra KMF/BYA/UNI/Enova).
2. **Forsvarlighetsvurdering etter asl. § 3-4** [verifiseres fase 10] — en
   skriftlig vurdering som:
   - Beregner forventet egenkapital i hvert av de tre selskapene per
     fisjonsstikkdag, basert på virkelige verdier (ikke bare bokførte).
   - Begrunner at hvert selskap har forsvarlig egenkapital og likviditet
     til å møte sine forpliktelser.
   - For fortsettende KWE: viser at konsernlån-restruktureringen
     (konvertering eller fordeling) gjør selskapet solvent per
     fisjonstidspunktet.
3. **Revisor-vurdering** etter asl. § 14-4 jf. § 2-6 [verifiseres fase 10].
   Statsautorisert revisor skal bekrefte at fisjonsplanen er forsvarlig
   og at det er dekning for aksjekapital og øvrig egenkapital i de
   overtakende selskapene.
4. **Juridisk vurdering** fra selskapsadvokat (ikke bare fra denne
   intern-analysen) som konkluderer at fisjonen er lovlig og at
   kreditorene har tilstrekkelig vern.
5. **Konkret vurdering av tvangsmulkt-saken.** Styret må protokollere at
   det er vurdert hvor forpliktelsen plasseres (Alt 1A), hvorfor, og
   hvilken dekningsgrunn fortsettende KWE har.
6. **Konkret vurdering av Intrum-saken.** Styret skal protokollere at
   konkursvarselet er håndtert (metode og dokumentasjon) før fisjon
   vedtas.
7. **Styreforsikring (D&O).** Anbefales før fisjonsvedtak. Dekker ikke
   forsett, men dekker uaktsomhet og rettskostnader. Vanlig premie for
   et konsern av denne størrelsen: 15–40 TNOK per år.

**Konsekvens hvis styret ikke dokumenterer.** Uten disse grepene er
styreansvaret ikke bare teoretisk — det er konkret personlig risiko for
styreleder (prosjektleder) og eventuelle øvrige styremedlemmer.
Praktisk konsekvens i verste fall: Hvis fortsettende KWE går konkurs
innen 2–3 år etter fisjon og boet reiser omstøtelse (dekningsloven § 5-9)
*samtidig* med erstatningssak mot styret (asl. § 17-1), kan styret bli
holdt personlig ansvarlig for kreditorenes tap. Beløpsmessig
eksponering: hele tvangsmulkt-saken + eventuelle leverandørkrav =
potensielt 1–2 MNOK personlig.

### A4. Strafferettslig grense — straffeloven kap. 31

Straffeloven kap. 31 om kreditorsvik [verifiseres fase 10] omfatter særlig:

- **§ 401 Formuesforringelse ved insolvens.** Rammer skyldner som, under
  insolvens eller fare for insolvens, forringer sin formuesstilling på en
  måte som er kreditorskadelig. Forsett eller grov uaktsomhet.
- **§ 402 Boforringelse.** Rammer disposisjoner som har til formål eller
  virkning å unndra formue fra kreditorforfølgning. Typisk «salg» til
  nærstående under markedsverdi, bortgjemming av eiendeler.
- **§ 404 Grovt uaktsom formuesforringelse.** Lavere skyldkrav —
  pliktbrudd i håndtering av eget konkurs- eller
  insolvensutsatt-situasjon.

**Hvor går grensen?** Grensen går mellom lovlig omorganisering og
formuesforringelse. Følgende utgjør markører for lovlig side:

1. **Markedspris og dokumenterbare verdier.** Fisjonsplanen bygger på
   bokførte verdier (skattemessig kontinuitet, sktl. kap. 11) og
   dokumenterbare markedsvurderinger. Ingen under-prising.
2. **Solidaransvar beholdes etter asl. § 14-11.** Ikke forsøk på å avtale
   bort kreditorvern.
3. **Kreditorvarsel kjøres gjennom Brreg** etter asl. § 14-7 — ingen
   skjult fordeling.
4. **Nettoformue hos ultimat eier (KodeWorks AS) uendret.** KodeWorks AS
   eier 100 % av alle tre selskaper etter fisjon. Ingen formue flyttes ut
   av konsernet.
5. **Forretningsmessig begrunnelse.** MVA-strategien (dokumentert ved
   Skatteetatens svar 11.09.2026), bank, tilskudd, nye aksjonærer. Ikke
   «for å unngå kreditorer».

Følgende ville derimot krysse grensen og nærme seg strl. § 401–404:

- **Dumpet verdi hos fortsettende KWE etter at konkursfare er påvist.**
  Hvis fisjonen gjennomføres med den foreløpige fordelingen (hele
  konsernlånet i fortsettende) *og* styret kjenner til at Intrum-saken
  pågår, kan dette tolkes som § 401 — forringelse av formuesstilling
  under fare for insolvens.
- **Betaling av konsernlån eller andre nærstående-krav mindre enn 3
  måneder før fisjonsvedtak.** Rammes av dekningsloven § 5-5 og nærmer
  seg strl. § 402 hvis motivet er å beskytte morselskapets fordring.
- **Ettergivelse eller konvertering av konsernlån *etter* at TBRT har
  reist krav.** Hvis morselskapet nå gir avkall på fordringen for å
  styrke fortsettende KWE *etter* at kreditorene er informert om at
  fordringen eksisterte som dekning, kan det argumenteres at dette er
  manipulasjon av kreditordekning. (Dette er en spennende motsatt
  variant av problemet: å ettergi/konvertere *for sent* kan være like
  problematisk som å ikke gjøre det.)
- **Opprettelse av tomme skalkskapsselskaper med formål å unndra
  tvangsmulkt.** Dette er den tydelige grensen. Hvis fortsettende KWE
  blir et «rent» holdingselskap med den eneste funksjonen å bære
  tvangsmulkten og uten noen reell driftsevne, kan strl. § 402 bli
  anvendelig.

**Juridisk konklusjon.** Planlagt fisjon ligger innenfor lovlig side
**forutsatt at**:

- Intrum-saken håndteres før fisjonsvedtak (ikke under illikviditet).
- Konsernlån restruktureres parallelt så fortsettende KWE blir solvent
  (ikke tom skalk).
- Forretningsmessig begrunnelse dokumenteres i styreprotokoll (ikke
  rene inndrivingshensyn).
- Kreditorvarsel kjøres korrekt (ikke skjult omfordeling).

Hvis disse betingelsene brytes, flyttes handlingen mot § 401–402. Det
betyr ikke at straffeansvar er sannsynlig — i praksis forfølges disse
sakene sjelden når det foreligger formell revisor- og advokatgjennomgang.
Men styreleder/prosjektleder bør være kjent med grensene.

---

## B. Nye temaer fra brukerinput

### B1. MVA-justeringsavtale — med mval. kap. 9 verifisert

Mval. kap. 9 er lastet verbatim fra Lovdata (fil: `bakgrunn/lovverk/mval_kap9_justering_av_inngaaende_merverdiavgift.md`). Følgende er juridisk ryddet opp
på bakgrunn av faktisk lovtekst.

**Hva er kapitalvare?** Etter § 9-1 (2):

- Bokstav a: maskiner/inventar/driftsmidler der inngående MVA av kostpris
  utgjør minst **kr 50 000**.
- Bokstav b: fast eiendom som har vært gjenstand for **ny-, på- eller
  ombygging** der inngående MVA på kostnadene utgjør minst **kr 100 000**.

**Når utløses justeringsplikt?** Etter § 9-2:

- (1) Endring av bruk (fradragsberettiget ↔ ikke-fradragsberettiget).
- (2) Omsetning av løsøre-kapitalvarer (bokstav a), hvis omsetningen er
  avgiftspliktig.
- (3) **Overdragelse av fast eiendom (bokstav b).**
- (4) Overdragelse av kapitalvarer som ledd i virksomhetsoverdragelse
  (fritt-MVA-overdragelse etter § 6-14).

**Hvordan unngås justering ved overdragelse?** Etter § 9-3 (1):

> «Justering etter § 9-2 tredje og fjerde ledd kan unnlates i det
> omfang den som overtar kapitalvaren overtar justeringsforpliktelsen.»

Dvs. overdrager og mottaker inngår en skriftlig **justeringsavtale**
(standardformular) der mottaker forplikter seg til å overta
justeringsforpliktelsen. Da trenger ikke overdrager å tilbakeføre MVA.

**Justeringsperioden** (§ 9-4):

- Løsøre (§ 9-1 (2) a): **5 år** fra anskaffelsesåret.
- Fast eiendom (§ 9-1 (2) b): **10 år** fra fullføringsåret («utstedt
  ferdigattest eller midlertidig brukstillatelse, eller … kapitalvarene
  er tatt i bruk»).

**Tilbakeføringsplikt — § 9-7:**

> «Fradragsført inngående merverdiavgift skal tilbakeføres dersom
> kapitalvarer som nevnt i § 9-1 annet ledd bokstav b *før fullføringen*
> selges eller omdisponeres til bruk som ikke ville gitt fradragsrett.»

Nøkkelen: § 9-7 gjelder før fullføring; § 9-2 (3) og § 9-5 (2) etter
fullføring. For FG30 (ikke fullført) er det § 9-7 som regulerer, hvis det
hadde vært fradragsført noe.

#### B1.1 Faktisk MVA-situasjon i KWE per 08.10.2026

Nye tall fra balanse 08.10.2026:

- **Utgående MVA (konto 2700): kr 81 050 YTD** — fra kontorutleien Grønnegata
  (frivillig § 2-3).
- **Inngående MVA (konti 2710/2711/2712): kr 15 988 YTD** — løpende drift.
- **Oppgjørskonto MVA (konto 2740): ca. 0 kr** — tømt.

KWE er altså **MVA-registrert allerede** (orgnr. 920 478 506 MVA), via
frivillig registrering § 2-3 for Grønnegata-kontorleie. Dette var ikke klart
i bruker-input og endrer analysen vesentlig.

**Konto 1172 Renovering Fjordgata 30 (kr 817 151 YTD).** Dette er bokført
uten MVA-fradrag — det samsvarer med at FG30-rehabiliteringen ikke har
vært omsatt (ikke generert MVA-pliktig leie) og at inngående MVA ikke er
løftet. Rent regnskapsmessig antakelse: kostnadsbilagene har mottatt
25 % MVA fra leverandører, men denne er ikke fradragsført. Beløpet er
bokført brutto (inkl. MVA) på konto 1172. **Dette må verifiseres med
regnskapsfører** — hvis det er bokført netto (ekskl. MVA), er inngående MVA
på FG30-rehab allerede fradragsført, og vi har et stort justeringsproblem.

**Antakelse i analysen:** Beløpet er bokført inkl. MVA (ingen fradrag
tatt). Dette er den vanlige behandlingen for byggekostnader der framtidig
bruk ikke er klarlagt per bokføringstidspunktet. Hvis antakelsen stemmer,
er FG30 **ingen kapitalvare etter § 9-1 (2) b for KWE** fordi det ikke er
fradragsført noen inngående MVA. § 9-7 utløses dermed ikke ved
overdragelsen gjennom fisjon.

**Grønnegata 10 — annerledes.** Grønnegata 10-bygningen ble kjøpt 2020 og
pusset opp 5,5 MNOK. Hvis oppussingen var fradragsført (frivillig § 2-3
for kontorutleie), er bygget en kapitalvare etter § 9-1 (2) b med
justeringsperiode til ca. 2030 (10 år fra fullføring 2020). Overføring til
Grønnegata 10 AS er **overdragelse etter § 9-2 (3)** og utløser i
utgangspunktet samlet justering, med mindre justeringsavtale etter § 9-3.

#### B1.2 Konkret anbefaling for Fjordgata 30

**Hvis konto 1172 er bokført inkl. MVA (ingen fradrag):**

- FG30 er **ikke** kapitalvare for KWE etter § 9-1 (2) b. § 9-2 (3)
  utløses ikke ved fisjonsoverdragelsen. Ingen justeringsavtale er
  nødvendig.
- FG30 AS kan **MVA-registreres etter fisjon** og bruke **tilbakegående
  avgiftsoppgjør etter mval. § 8-6** [verifiseres fase 10 — Agent 4 har
  rettet opp fristen fra 6 mnd (feil i v1) til 3 år] for å løfte
  inngående MVA på byggekostnader påløpt fra ca. 25.10.2024 og framover.
  Beløpet er estimert ca. 250–375 TNOK (seksjon 5.4 Agent 4) på
  pre-fisjons-kostnader, pluss 6,2 MNOK gjennom byggefasen 2027.
- **Dette er den beste strukturen.** KWE unngår justeringsforpliktelse,
  FG30 AS får løftet all MVA i egen regi, ingen avtale trengs.

**Hvis konto 1172 er bokført ekskl. MVA (fradrag tatt — alternativt
scenario):**

- FG30 er kapitalvare for KWE etter § 9-1 (2) b. Fisjonsoverdragelsen
  utløser § 9-2 (3). To muligheter:
  - (a) **Justeringsavtale etter § 9-3 (1)**: KWE og FG30 AS inngår avtale der
    FG30 AS overtar justeringsforpliktelsen. KWE unngår samlet justering;
    FG30 AS må registreres i MVA-registeret senest ved overføringen og må
    opprettholde fradragsberettiget bruk gjennom restperioden
    (10 år fra fullføring).
  - (b) **Tilbakeføring etter § 9-7 (2)** hvis bygget er under fullføring:
    FG30 AS overtar plikten til å tilbakeføre fradragsført MVA hvis
    bruken endres til ikke-fradragsberettiget.

Begge alternativene krever at FG30 AS er **MVA-registrert ved
overføringen**. Dette presser timing.

**Umiddelbar handling:** Regnskapsfører må verifisere om konto 1172 er
bokført inkl. eller ekskl. MVA før fisjonsvedtak. Dette er en kritisk
avklaring som Agent 4 ikke eksplisitt dekket.

#### B1.3 Grønnegata 10 — justeringsavtale er nødvendig

For Grønnegata-eiendommen med teknisk installasjon og inventar er historisk
inngående MVA mye mer sannsynlig fradragsført (bygget har vært utleid med
frivillig § 2-3 siden ca. 2020–2021). Overføring til Grønnegata 10 AS
krever derfor:

- **Justeringsavtale etter mval. § 9-3 (1)** mellom KWE og Grønnegata 10 AS
  for bygget (10-årsperiode) og eventuelt for løsøre-kapitalvarer (konti
  1251, 1260 — 5-årsperiode).
- Grønnegata 10 AS må være MVA-registrert ved overføringen (frivillig
  § 2-3 for samme kontorutleie som KWE i dag).

**Grønnegata 10 AS må altså MVA-registreres samtidig med
fisjonsgjennomføringen**, ikke etterpå. Dette avviker fra Agent 2s plan
(uke 10) — registrering må være på plass før hjemmelsovergangen tinglyses.

#### B1.4 Riktig tidsrekkefølge

Sammenstilt vurdering:

**Mål:** (a) KWE unngår justeringsplikt der det er mulig, (b) FG30 AS får
løfte all MVA på byggefasen, (c) Grønnegata 10 AS beholder MVA-regimet
uten brudd.

**Rekkefølge:**

1. **Før fisjon:** Verifisér at konto 1172 FG30-renovering ikke er
   fradragsført. Dokumenter.
2. **Fisjonsvedtak og registrering i Brreg.** FG30 AS og Grønnegata 10 AS
   får organisasjonsnummer.
3. **Umiddelbart etter Brreg-registrering (samme dag):** Grønnegata 10 AS
   MVA-registreres (frivillig § 2-3 for kontorutleie). Justeringsavtale
   mval. § 9-3 (1) inngås skriftlig mellom KWE og Grønnegata 10 AS for
   byggets kapitalvarer. Avtalen signeres samme dag.
4. **FG30 AS:** Ingen MVA-registrering ved selve fisjonen (fordi
   byggefasen ikke er omsetning ennå). MVA-registrering (ordinær § 2-1
   for valet storage + frivillig § 2-3 for kontor) skjer Q2 2027 når
   bygget nærmer seg ibruktakelse. Tilbakegående avgiftsoppgjør etter
   § 8-6 løfter alle pre-fisjon og pre-registrering byggefase-kostnader.
5. **Tinglysning av hjemmelsovergang** etter at MVA-strukturen er
   dokumentert.

**Dette avviker fra Agent 2s uke 10-plan** (som har MVA-registrering FG30
AS *og* Grønnegata 10 AS i samme uke etter hjemmelsoverføring). Mitt
råd: Grønnegata 10 AS registreres **samtidig med Brreg-registrering**;
FG30 AS registreres **først når driften starter**.

#### B1.5 Konsekvens hvis justeringsavtale ikke lages (Grønnegata)

Hvis Grønnegata 10 AS ikke er MVA-registrert ved overføringen, eller hvis
justeringsavtalen ikke er på plass:

- Samlet justering utløses i KWE etter § 9-5 (2) andre pkt. — hele
  restperioden regnes samlet.
- Beløpet er fradragsført inngående MVA på de resterende år av
  justeringsperioden. For Grønnegata 10 bygg med fullføring 2020 og
  justeringsperiode til 2030, er det ca. 4 år igjen av 10. Hvis
  historisk fradragsført MVA på bygget er f.eks. 1,375 MNOK (25 % av
  5,5 MNOK oppussing), er restforpliktelsen 4/10 × 1,375 = 550 TNOK.
- KWE må tilbakebetale dette til Skatteetaten. **Kontantutlegg som
  gjør fortsettende KWE enda mer insolvent.**

Konklusjon: Justeringsavtalen er obligatorisk ved overdragelse av
Grønnegata — kan ikke glemmes.

### B2. Nye aksjonærer (Brandsegg og Lagmannssveen) — fisjon først eller tingsinnskudd i fisjonen?

#### B2.1 Hvorfor fisjon først er riktig

Skatteloven kap. 11 regulerer skattefri fisjon. § 11-7 [verifiseres fase 10]
krever **aksjonærkontinuitet**: aksjonærene i de overtakende selskapene skal
være de samme som i overdragende, i samme forhold.

KWE er heleid av KodeWorks AS. Hvis Brandsegg/Lagmannssveen tas inn **som
del av fisjonen** (dvs. ved stiftelsesdokumentet for FG30 AS, slik at de
får vederlagsaksjer i FG30 AS):

- Aksjonærkontinuitet brytes — KodeWorks AS eier 100 % før, men etter
  fisjonen er FG30 AS deelt (KodeWorks AS + Brandsegg + Lagmannssveen).
- Fisjonen mister skattefri status etter sktl. § 11-7.
- **Realisasjon utløses:** KWE blir skattepliktig for gevinst på
  FG30-eiendommen. Hvis virkelig verdi er høyere enn bokført (sannsynlig),
  utløses skatt på gevinsten — 22 % selskapsskatt på differansen. For FG30
  med bokført 8,15 MNOK og virkelig verdi 15–30 MNOK er dette 1,5–5 MNOK
  umiddelbar skatt. Vil ødelegge økonomien.
- I tillegg: aksjonæruttaket til KodeWorks AS behandles som utbytte
  (fritaksmetoden etter sktl. § 2-38 vil normalt frita, men selve
  realisasjonen i KWE utløses uansett).

**Konklusjon:** Fisjon først (KodeWorks AS som eneaksjonær i alle tre
selskaper), deretter emisjon mot tingsinnskudd i FG30 AS. Dette er
standardgrepet og det eneste som bevarer skattefri status.

#### B2.2 Hva kan tingsinnskudd bestå i?

Aksjeloven [verifiseres fase 10 — særlig §§ 2-6 og 2-7] regulerer
tingsinnskudd:

- **Lovlige tingsinnskudd:** Kontanter, fysiske eiendeler (verktøy,
  maskiner, inventar, bil), immaterielle rettigheter (patent, varemerke,
  copyright, lisens, konsesjon, kundelister/goodwill der verdifastsettelse
  er dokumenterbar), fordringer (konvertering av eksisterende
  pengefordring mot selskapet til aksjer).
- **IKKE lovlige tingsinnskudd:** **Arbeid og arbeidsplikt** er
  eksplisitt utelukket etter asl. § 2-7 [verifiseres fase 10]. Prinsippet
  er at innskuddet skal være noe selskapet umiddelbart har eiendoms- eller
  rettighetsposisjon i; en fremtidig arbeidsytelse oppfyller ikke
  dette fordi aksjen må ha realdekning fra start.

**For Brandsegg og Lagmannssveen** er dette den første praktiske
problemstillingen. Brukeren må klargjøre:

| Alternativ | Lovlig? | Dokumentasjon |
|---|---|---|
| Kontantinnskudd | Ja | Bankinnskudd — ingen revisorerklæring nødvendig for kontanter alene |
| Verktøy/utstyr (f.eks. tekniske instrumenter) | Ja | Revisorerklæring (asl. § 2-6) med markedsverdi |
| Immateriell verdi: tegninger, prosjektering, planer | Ja — hvis dokumentert og overførbar som eiendomsrett | Revisorerklæring + dokumentasjon av eiendomsrett |
| «Kompetanse», «nettverk», «arbeidsinnsats» | **Nei** | Må struktureres som annet (se under) |
| Avkall på fordring (uttatt timebruk/konsulenthonorar som ikke er betalt) | Ja — gjeldskonvertering | Revisorerklæring + faktura/dokumentasjon av fordringen |

#### B2.3 Hvis det er arbeidsinnskudd — alternativer

Hvis Brandsegg og Lagmannssveen egentlig skal få aksjer som gjenytelse for
*fremtidig* arbeid (ikke tingsinnskudd), finnes tre lovlige strukturer:

1. **Opsjonsavtale.** Ansattopsjoner tildeles mot fremtidige
   milepeler/arbeidsinnsats. Skattemessig krever dette at opsjonen gis
   på markedsvilkår (ellers skattepliktig fordelsbeskatning hos
   mottaker). Opsjonen kan innløses mot kontantinnskudd ved utøvelse.
2. **Konsulentkontrakt med aksjeopptjening.** Brandsegg/Lagmannssveen
   fakturerer timer til FG30 AS. Timene legges i mellomregning. Når
   mellomregningen er stor nok, konverteres den til aksjer via
   gjeldskonvertering (tingsinnskudd i form av fordringsavkall).
   Skattemessig: ordinær lønnsbeskatning på fakturerte timer.
3. **«Sweat equity» via kjøp av aksjer på gunstige vilkår.** Brandsegg
   og Lagmannssveen kjøper aksjer kontant til lav emisjonskurs («founder
   stock»). Skatt på fordelsbeskatning hvis emisjonskursen er under
   markedsverdi. For et nystiftet selskap med beskjeden virkelig verdi
   på emisjonstidspunktet kan dette fungere.

**Mitt råd:** Alternativ 2 (konsulentkontrakt + senere gjeldskonvertering)
er mest ryddig for et byggeprosjekt. Brandsegg og Lagmannssveen får
løpende dokumentasjon av innsats, FG30 AS får konkret økonomisk tilførsel
(timenes verdi i balansen), og konverteringen til aksjer skjer når
innsatsen er dokumentert og revisor kan verifisere beløpet. Dette
tilsvarer brukerinput seksjon 4-anmerkningen om «arbeid eller
arbeidsplikt er ikke lovlig tingsinnskudd».

#### B2.4 Tidsmessig avstand mellom fisjon og emisjon

Agent 2 har anbefalt 2–4 uker. Mitt juridiske råd er **minst 3 uker, helst
6–8 uker**. Begrunnelse:

Skatteetaten (og Lagmannsretten) kan anvende «serietransaksjonslæren»
eller omgåelsesnormen (sktl. § 13-2 [verifiseres fase 10]) hvis det
framstår som at fisjon + emisjon er én sammenhengende disposisjon som
reelt sett bryter aksjonærkontinuiteten. Risikofaktorer:

- **Nære i tid** (dager–uker): øker risikoen for serietransaksjon.
- **Begge disposisjoner planlagt sammen og dokumentert i samme
  styreprotokoll:** øker risikoen vesentlig.
- **Emisjonsvilkårene fastsatt før fisjonen er registrert:** maksimal
  risiko.

For å nøytralisere:

1. **Fisjonsvedtak** inneholder ingen henvisning til planlagt emisjon.
2. **Emisjonsbeslutning** fattes etter at fisjonen er fullt registrert
   i Brreg, og dokumenteres som en selvstendig forretningsmessig
   beslutning (f.eks. «for å finansiere videre drift» eller «for å
   tilføre spesialkompetanse»).
3. **Minst 3 uker** mellom fisjonsregistrering (Brreg) og styrevedtak
   om emisjon. 6+ uker gir større sikkerhet. 8+ uker er «sikker side».
4. **Aksjonæravtalen** signeres etter fisjonsregistreringen, ikke før.

Praktisk konsekvens: Hvis fisjon registreres medio mars 2027,
emisjonsbeslutning tidligst ultimo april 2027. Dette samsvarer med
Agent 2s uke 12–14 (med forsiktighet mot nedre grense).

#### B2.5 Alternativ: forhåndsrettet emisjon i KWE *før* fisjon

Teknisk mulig: Brandsegg og Lagmannssveen tas inn som aksjonærer i KWE
*før* fisjonsvedtak. Da er de aksjonærer i KWE på fisjonstidspunktet, og
får vederlagsaksjer i alle tre selskapene — aksjonærkontinuitet er
bevart.

**Problemer:**

1. Da sitter de også som aksjonærer i Grønnegata 10 AS og fortsettende
   KWE — ikke bare FG30 AS. Ikke ønsket av brukeren.
2. **Omstøtelsesrisiko høy.** Hvis emisjonen i KWE skjer innenfor
   omstøtelsesvinduet (2 år ordinære, 10 år nærstående) og tingsinnskuddet
   er overvurdert eller har svak dekningsvirkning, kan kreditor (TBRT,
   Intrum) angripe emisjonen etter dekningsloven § 5-2 (gaver) eller § 5-9.
3. Krever tingsinnskudd på et beløp som gir fornuftig andel i KWE
   (ellers blir den utvannet andel for liten til å ha verdi i FG30 AS
   etter fisjon). Dette krever større innskudd — ikke egnet for en
   løpende konsulentmodell.

**Konklusjon:** Alternativet er juridisk mulig, men praktisk dårligere.
Fisjon først + senere emisjon i FG30 AS er klart å foretrekke.

#### B2.6 Omstøtelsesrisiko ved etterfølgende emisjon

Hvis emisjonen skjer kort tid etter fisjon og innenfor omstøtelsesvinduet,
kan kreditor hevde at hele strukturen (fisjon + emisjon) er én
sammenhengende disposisjon designet for å verdiuttynning av
morselskapets dekningsgrunn.

Hovedbekymringen: **tingsinnskuddet er over-verdsatt.** Hvis Brandsegg
tilfører «kompetanse verdt 2 MNOK» og får 10 % av FG30 AS mot dette, mens
reell verdi er betydelig mindre, er FG30 AS blitt utvannet uten reell
tilførsel. KodeWorks AS' andel har blitt mindre verdt. Kreditor kan
angripe dette som § 5-9-handling.

**Mitigering:**

- **Markedsmessig verdsettelse av tingsinnskuddet** — revisor må
  bekrefte etter asl. § 2-6.
- **Dokumentert driftsmessig behov** for emisjonen (likviditet,
  nøkkelkompetanse, risikofordeling).
- **Avstand i tid** fra fisjon (seksjon B2.4).
- **Åpenhet mot kreditorer** — TBRT varsles om emisjonen på vanlig vis
  gjennom Brreg-kunngjøring; ingen skjult strukturering.

### B3. Grønnegata-isolering (brukerens Q5)

Brukerens krav: Grønnegata 10 AS skal ikke være solidaransvarlig for
noe annet enn seg selv. Dette er ikke mulig å oppnå *formelt* — asl.
§ 14-11 [verifiseres fase 10] gir solidaransvar mellom overtakende og
fortsettende som ikke kan avtales bort overfor kreditor. Men
*reelt-økonomisk* kan effekten oppnås gjennom:

**Grep 1: Eksplisitt plassering av alle kjente forpliktelser.** Etter asl.
§ 14-11 blir solidaransvaret **subsidiært** når hver forpliktelse er
plassert hos ett bestemt selskap. Fisjonsplanen må plassere eksplisitt
hvert krav. Rangert etter viktighet:

- Konsernlån til KodeWorks AS (10,6 MNOK + rente).
- DNB-lån (15,2 MNOK + rente).
- Påløpt tvangsmulkt (184 TNOK).
- Potensiell tilbakevirkende innkreving (opptil 428 TNOK).
- Leverandørgjeld (ca. 488 TNOK, fordeles faktura-for-faktura).
- Forskudd fra kunder (101 TNOK).
- Alle øvrige påløpte avgifter og trekkforpliktelser.

Hver post plasseres med klart adressat.

**Grep 2: Reell dekningsgrunn hos primærdebitor.** Når en kreditor må gå
subsidiært på et solidaransvarlig selskap, utløses solidaransvaret bare
hvis primærdebitor ikke dekker. Hvis fortsettende KWE kan dekke sin
tvangsmulkt og Fjordgata 30 AS kan dekke sine kostnader, trenger ikke
kreditor noensinne å kreve Grønnegata 10 AS. Grønnegata-isolering er
dermed en **funksjon av dekning hos de andre to selskapene** —
særlig fortsettende KWE.

**Grep 3: Beløpsmessig begrensning.** Solidaransvaret er beløpsbegrenset
til hvert selskaps nettoverdi tilført fra fisjonen. For Grønnegata 10 AS:

- Bokført eiendeler: ca. 18,2 MNOK (bygg 16,8 + teknisk 1,3 + inventar
  0,5 – avskrivninger).
- Overtatt gjeld: ca. 15,2 MNOK (DNB) + eventuelt andel konsernlån etter
  Agent 3s mekanisme A.
- **Nettoverdi tilført: ca. 3–4 MNOK** avhengig av konsernlån-fordelingen.

Dette er «worst case»-eksponering mot Grønnegata 10 AS. Blir aldri
aktualisert hvis fortsettende KWE + Fjordgata 30 AS har dekning.

**Grep 4: Fisjonsplan-klausul om intern regress.** Fisjonsplanen kan
regulere **intern** fordeling mellom selskapene (hvem bærer hva internt),
selv om den ikke kan binde kreditor. Grønnegata 10 AS kan dermed få
regressrett mot fortsettende KWE og Fjordgata 30 AS hvis Grønnegata
tvinges til å betale noe utover sin eksplisitt tilordnede andel. Dette
er en standard-klausul som bør inn.

**Grep 5: Agent 3s dekningsstruktur (A + C).** Konsernlån fordeles
proporsjonalt (slik at fortsettende KWE blir «ren» for konserngjeld) +
morselskapsgaranti fra KodeWorks AS på 1 MNOK direkte til TBRT. Agent 3
har valgt dette, og mitt juridiske råd er at det er den beste
kombinasjonen for Grønnegata-isolering **forutsatt**:

- **KodeWorks AS samtykker eksplisitt** til konsernlånsfordelingen. Dette
  er en avtale om debitorbytte (fra KWE til Grønnegata 10 AS og FG30 AS)
  som krever kreditorens samtykke etter alminnelig obligasjonsrett.
  Siden KodeWorks AS er morselskap og brukeren kontrollerer begge, er
  dette formalia — men styrevedtak i KodeWorks AS må protokolleres.
- **Skattemessig konsekvens for KodeWorks AS** av debitorbyttet må
  vurderes. Avhending av fordring (del av fordringen flyttes fra KWE til
  nye debitorer) kan utløse gevinst/tap i KodeWorks AS. Normalt skal
  bokført verdi matche overførings-verdi, så gevinst/tap bør være
  neglisjerbart hvis vilkårene er like.
- **Morselskapsgaranti** — se neste punkt.

#### B3.1 Morselskapsgaranti — juridisk vurdering

Agent 3 foreslår 1 MNOK selvskyldnergaranti fra KodeWorks AS, enten:
(a) til fortsettende KWE som sikkerhet mot tredjeparter, eller
(b) direkte til TBRT som begunstiget.

**Variant (a) — garanti til fortsettende KWE:**

- Forretningsmessig: KodeWorks AS stiller sikkerhet til fortsettende KWE,
  som dermed kan dekke sine forpliktelser overfor TBRT (og evt. andre
  kreditorer).
- Juridisk: Standard konsernintern garanti. Krever styrevedtak og
  dokumentasjon i garantibrev. Må være skriftlig, uigjenkallelig.
- Omstøtelsesrisiko: Garantien kan angripes etter dekningsloven § 5-2
  (gaver) hvis den stilles **vederlagsfritt** og mens KodeWorks AS er
  insolvent. Dette er lite sannsynlig så lenge KodeWorks AS er solvent.
- **Markedsvilkår:** Etter asl. § 3-9 [verifiseres fase 10] skal
  transaksjoner mellom selskaper i samme konsern skje på vanlige
  forretningsmessige vilkår. En garanti skal normalt beregnes
  **garantiprovisjon** (f.eks. 0,5–1,5 % av garantibeløpet per år).
  Hvis garantien stilles vederlagsfritt, kan Skatteetaten omklassifisere
  det til indirekte utbytte (sktl. § 10-11). Rådet: KodeWorks AS beregner
  provisjon 1 % per år × 1 MNOK = 10 TNOK per år. Marginalt beløp som
  nøytraliserer skatterisikoen.

**Variant (b) — garanti direkte til TBRT:**

- Forretningsmessig: KodeWorks AS stiller selvskyldnergaranti til TBRT på
  inntil 1 MNOK som dekning for tvangsmulktsaken (påløpt + eventuelt
  tilbakevirkende).
- Juridisk: Tredjepartsgaranti; TBRT som begunstiget. Krever samarbeid
  med TBRT (de må akseptere garantien som «betryggende sikkerhet»).
- Fordel: Fjerner TBRTs mulighet til å reise innsigelse i kreditorfristen
  — sikkerheten er allerede stilt. Enklere kommunikasjon.
- Ulempe: Binder KodeWorks AS i et direkte forhold til TBRT. Hvis
  tvangsmulktsaken utvides eller DSB-saken går dårlig, kan garantien
  bli trukket.

**Mitt råd:** **Variant (a) — garanti til fortsettende KWE** er mest
fleksibel. Hvis TBRT senere reiser innsigelse i kreditorfristen, kan
garantien konverteres til Variant (b) ved behov. Variant (a) er også
mindre eksponert mot framtidige saksutvidelser.

**Begge varianter skal:**

- Være skriftlige, selvskyldner, første-påkrav.
- Dekke både påløpt mulkt (184 TNOK) og tilbakevirkende innkreving
  (opptil 428 TNOK) + buffer for salærkostnader (ca. 400 TNOK).
  Totalbeløp: 1 MNOK er riktig estimat.
- Være begrenset i tid (f.eks. gyldig fram til tvangsmulktsaken er
  endelig avsluttet, eller 3 år fra fisjonsregistrering, hva som
  først inntreffer).
- Beregne markedsmessig garantiprovisjon.

---

## C. Mindre temaer

### C1. Konsernlåns-restrukturering (10,6 MNOK)

Flere alternativer, rangert etter juridisk robusthet mot omstøtelse:

**Alternativ 1: Konvertering til egenkapital (debt-to-equity swap).**
KodeWorks AS konverterer sin fordring på KWE til aksjekapital/overkurs
i KWE *før eller samtidig med* fisjonsvedtaket. Dermed:

- Fortsettende KWE blir solvent (gjelden forsvinner, egenkapitalen vokser
  tilsvarende).
- Ingen fordeling mellom selskapene er nødvendig.
- Styreansvarsrisikoen (seksjon A3) elimineres.

Juridiske konsekvenser:

- **I KWE:** Gjeldskonverteringen er aksjetegning etter asl. kap. 10.
  Krever styrevedtak og generalforsamlingsvedtak. Revisorerklæring etter
  asl. § 2-6. Konverteringen er tingsinnskudd i form av fordringsavkall.
- **I KodeWorks AS:** Avhending av fordring. Bokført verdi var 10,6 MNOK
  (plus rente); aksjene mottatt gis samme verdi. Normalt ingen
  skattemessig gevinst/tap hvis vilkårene er korrekte.
- **Omstøtelsesrisiko:** Dekningsloven § 5-2 (gaver) kan angripe hvis
  konverteringen framstår som vederlagsfri gave fra KodeWorks AS til
  KWEs øvrige kreditorer. Men siden KodeWorks AS mottar aksjer med
  samme verdi, er det ikke en gave — det er en jevnbyrdig
  tingsinnskudd.
- **Styrke:** Mest robust fordi gjelden forsvinner fra balansen,
  erstattes med egenkapital. Fortsettende KWE blir **bokført solvent**
  umiddelbart.

**Alternativ 2: Fordeling av konsernlånet (Agent 3s mekanisme A).**
Lånet fordeles proporsjonalt mellom de tre selskapene. KodeWorks AS
samtykker som kreditor.

- **I KWE/overtakende:** Debitorbytte dokumentert i fisjonsplan og
  samtykkebrev fra KodeWorks AS.
- **I KodeWorks AS:** Avhending av én fordring, mottakelse av tre.
  Normalt ingen skatt hvis samlet balanseført verdi uendret.
- **Omstøtelsesrisiko:** Lav hvis fordelingen følger netto bokført
  verdi i hvert selskap (proporsjonalt). Hvis fordelingen avviker
  (f.eks. mer gjeld på det selskapet med best fri verdi), kan det
  reises spørsmål om vilkårlighet.
- **Styrke:** God operativ løsning, men krever at vilkårene er like for
  alle tre delfordringene (rente, forfallstid, pant).

**Alternativ 3: Delvis ettergivelse.** KodeWorks AS ettergir deler av
fordringen (f.eks. 5 MNOK). Resten blir i fortsettende KWE eller
fordeles.

- **I KodeWorks AS:** Tap på fordring — fradragsberettiget etter
  sktl. § 6-2 (1) ved endelig konstatert tap, men ikke umiddelbart
  når fordringen ettergis frivillig til datterselskap. Skatteetaten
  nekter typisk fradrag for ettergivelse til nærstående uten
  dokumentasjon av at fordringen er reelt tapt. Her er den **ikke
  reelt tapt** — KWE kan betjene gjelden hvis strukturen justeres.
  Fradragsrett lite sannsynlig.
- **I KWE:** Gjeldsettergivelse er skattepliktig inntekt etter
  sktl. § 5-1 (gjeldsettergivelse som alminnelig inntekt), med mindre
  spesifikke unntak slår inn. Hvis selskapet har framførbart
  underskudd 2,46 MNOK, kan ettergivelse under dette beløpet
  nøytraliseres gjennom motregning (sktl. § 14-6). Beløp over
  2,46 MNOK blir skattepliktig.
- **Styrke:** Dårlig. Både skattekonsekvens og presedens-signal (bank,
  tilskuddsgivere oppfatter ettergivelse som insolvenstegn).

**Rekommandasjon:** **Alternativ 1 (konvertering til egenkapital).** Den
er mest robust mot omstøtelse, eliminerer styreansvarsrisikoen og
unngår skatt i både KWE og KodeWorks AS. Krever styrevedtak og
revisorerklæring, men er standard aksjelovsgrep.

Beløp å konvertere: Minimum **5 MNOK** for å gjøre fortsettende KWE
bokført solvent etter fisjon. Hele 10,6 MNOK gir margin. Hvis
konsernlånet er priset til 9,2 % (konto 8130), er dette også en
løpende rentebelastning som fjernes — løpende rentekostnad reduseres
med ca. 970 TNOK per år ved full konvertering, som styrker driftsbildet
i alle etterfølgende selskaper.

**Agent 2 og Agent 4:** Noter at Alternativ 1 er juridisk mest
robust. Operativt må styrevedtak i både KodeWorks AS og KWE
samordnes.

### C2. Framførbart underskudd (2,46 MNOK)

Agent 4 anbefaler at underskuddet plasseres i FG30 AS der det får
best skattevirkning (fremtidige lagringsdrifts-overskudd 2027–).

**Juridisk vurdering:**

- Skattelovens hovedregel ved skattefri fisjon: fordeling etter
  nettoverdi tilført (proporsjonalt).
- Men § 11-7 [verifiseres fase 10] åpner for alternativ fordeling i
  fisjonsplanen hvis dette er forretningsmessig begrunnet.
- **Avskjæringsregelen i sktl. § 14-90** [verifiseres fase 10] rammer
  disposisjoner som har som **overveiende** motiv å utnytte
  skatteposisjonen. Nøkkelordet er «overveiende» — hvis det er reell
  forretningsmessig begrunnelse (MVA-strategi, risikoseparasjon,
  tilskudd), er avskjæring usannsynlig.

**For denne fisjonen:**

- Reell forretningsmessig begrunnelse er godt dokumentert (seksjon A4).
- Underskuddet er beskjedent (2,46 MNOK → skattebesparelse ca. 541 TNOK).
- FG30 AS har en konkret og dokumenterbar fremtidig inntektsstrøm
  (lagringsvirksomhet med 6,2 MNOK MVA-refusjonsplan og driftsbudsjett).
- Fordeling til FG30 AS er dermed forretningsmessig forsvarlig.

**Juridisk konklusjon:** Lovlig å plassere framførbart underskudd i FG30
AS. Fisjonsplanen må begrunne hvorfor FG30 AS er riktig mottaker (ikke
Grønnegata 10 AS). Begrunnelse: FG30 AS har størst forventet
overskuddskapasitet, risikoprofilen tilsier at utsatt skatt er en
forretningsmessig gunstig overføring, og tjenesten speiler nettoverdi
tilført når virkelige verdier (ikke bokførte) legges til grunn.

**Risiko ved avskjæring:** Hvis Skatteetaten mener fordelingen er
skattemotivert, kan **hele** underskuddet avskjæres — ikke bare
«overføringsdelen». Men dette er lite sannsynlig gitt den tydelige
forretningsmessige begrunnelsen.

### C3. Pålegg og offentligrettslig overføring

V1 skrev «juridisk uavklart». Agent 3 skriver «følger eiendommen».
Jeg lander v2 på følgende klarere standpunkt:

**Pålegg etter brann- og eksplosjonsvernloven § 37** [verifiseres fase 10]
retter seg mot «eier og bruker» av objektet. Dette er en
**eiendomsknyttet plikt**, ikke en subjekt-knyttet forpliktelse. Når
eierskapet overføres gjennom fisjon:

- **Plikten følger eiendommen.** FG30 AS blir ny pliktsubjekt etter
  overføringen. Pålegget trenger ingen ny materiell behandling for å
  gjelde FG30 AS — plikten ligger i selve eieren-rollen.
- **Men vedtaket** er stilet til KWE som juridisk person. For formell
  klarhet må TBRT **underrette ny eier** om at pålegget nå gjelder
  Fjordgata 30 AS. Dette er administrativt — ikke et «nytt vedtak» i
  materiell forstand, men en bekreftelse av subjekt-identifikasjon.
- **Tvangsmulktvedtaket (07.05.2025)** er en annen sak. Den er en
  **administrativ sanksjon** mot KWE som pliktsubjekt. Tolkningen her er
  mindre entydig:
  - Tolkning 1 (subjektrettet): Vedtaket treffer KWE som rettssubjekt,
    uavhengig av eiendomsoverføring. Fortsettende KWE forblir
    pliktsubjekt for tvangsmulktvedtaket; nytt vedtak må fattes mot
    FG30 AS for ny mulkt framover.
  - Tolkning 2 (tingsrettslig): Siden tvangsmulkten er sanksjonering av
    pålegget og pålegget er eiendomsknyttet, følger mulkten
    eiendommen. FG30 AS trer inn som pliktsubjekt.

**Mitt standpunkt v2:** Tolkning 1 er juridisk mest korrekt for
**tvangsmulktvedtaket** (sanksjon knyttet til et bestemt rettssubjekt),
men Tolkning 2 kan være korrekt for **selve pålegget** (eiendomsknyttet
plikt). I praksis vil TBRT:

1. Underrette FG30 AS om at pålegget nå gjelder dem (eller fatte nytt
   vedtak hvis nødvendig).
2. Behandle fortsettende KWE som ansvarlig for den påløpte mulkten
   (kr 184 000) og eventuell tilbakevirkende innkreving.
3. Fatte **nytt mulktvedtak** mot FG30 AS hvis pålegget ikke oppfylles
   fra fisjonstidspunktet.

**For fisjonsplanen:** Alt 1A fra Agent 3 (påløpt mulkt + tilbakevirkende
hos fortsettende KWE, pålegg + framtidig mulkt hos FG30 AS) er juridisk
riktig fordeling.

Agent 3s klausulforslag — «Alle offentligrettslige krav, påløpte så vel
som tilbakevirkende, … forblir hos fortsettende KodeWorks Eiendom AS» —
er intern mellom konsernet og kan ikke binde TBRT direkte. Men den er
nyttig som dokumentasjon av fisjonsplanens intensjon og regulerer
intern regress mellom selskapene hvis TBRT skulle gå på et «galt»
selskap.

---

## D. Djevelens advokat — fem sterkeste juridiske angrepspunkter

Rangert etter juridisk tyngde og vinnbarhet. Supplerer Agent 3s liste
som fokuserer på tvangsmulkt-vinkelen.

### D1. Dekningsloven § 5-9 — fisjonen gjør fortsettende KWE strukturelt insolvent

**Formulering:** «Fisjonen vedtas med en fordeling som gjør fortsettende
KodeWorks Eiendom AS teknisk insolvent (bokført EK –10,8 MNOK), mens
alle verdier er flyttet til nystiftede selskaper. Dette er en
disposisjon som på en utilbørlig måte forringer bomassen for en bestemt
kreditor (TBRT) som kan dokumentere at krav var kjent på
fisjonstidspunktet. Rammes av dekningsloven § 5-9. 10-årsfrist mot
nærstående etter § 1-5.»

**Styrke:** **5/5.** Dette er den juridisk tyngste angrepsvinkelen hvis
konsernlån-restrukturering ikke gjennomføres.

**Forsvar:** Konvertering av konsernlån til egenkapital (seksjon C1,
Alternativ 1) + morselskapsgaranti 1 MNOK (seksjon B3.1). Fortsettende
KWE blir solvent, dekningsgrad 2,9× på kjent eksponering (Agent 3,
seksjon 4.1). Angrepet nøytraliseres i stor grad.

### D2. Styreansvar etter asl. § 17-1 — fisjonsvedtak under illikviditetsformodning

**Formulering:** «Styreleder i KodeWorks Eiendom AS gjennomfører
fisjonsvedtak på et tidspunkt da konkursvarsel var forkynt 13.10.2026
og ikke stabilisert. Dette er forsettlig gjennomføring av disposisjon
mens illikviditetsformodning foreligger. Styret har forsettlig
disponert kreditorskadelig; personlig erstatningsansvar for styreleder.»

**Styrke:** **4/5.** Direkte personlig risiko for prosjektleder.

**Forsvar:** Konkursvarselet håndteres før fisjonsvedtak (betaling,
rettslig stans, eller TBRT-instruert Intrum-stans). Dokumenteres i
styreprotokoll. Styreforsikring (D&O) tegnes før vedtak. Alle fem
dokumentasjonskrav fra seksjon A3 oppfylt. Angrepet forsvinner i stor
grad.

### D3. Kontinuitetsbrudd ved emisjon — sktl. § 11-7 serietransaksjon

**Formulering:** «Fisjon og etterfølgende emisjon av Fjordgata 30 AS til
Brandsegg og Lagmannssveen er én sammenhengende disposisjon designet
for å ta inn nye aksjonærer i FG30 AS uten å utløse realisasjonsskatt.
Rammes av serietransaksjonslæren og omgåelsesnormen i sktl. § 13-2.
Skattefri status etter § 11-7 oppheves; gevinst på eiendomsoverføringen
beskattes.»

**Styrke:** **3/5.** Hvis emisjon kommer for raskt etter fisjon, og
emisjonsvilkårene er fastsatt før fisjonsregistrering, er dette en
reell risiko.

**Forsvar:** Minst 6–8 ukers avstand mellom fisjonsregistrering og
emisjonsvedtak. Fisjonsplanen inneholder ingen henvisning til planlagt
emisjon. Emisjonsbeslutning dokumenteres som selvstendig
forretningsmessig vurdering. Tingsinnskuddets reelle verdi bekreftes av
revisor (asl. § 2-6). Angrepet nøytraliseres.

### D4. Feil eller manglende MVA-justeringsavtale (Grønnegata)

**Formulering:** «Grønnegata 10-eiendommen er en kapitalvare etter mval.
§ 9-1 (2) b der KWE har fradragsført inngående MVA på oppussing.
Overføring til Grønnegata 10 AS utløser samlet justering etter § 9-2 (3)
og § 9-5 (2) hvis justeringsavtale etter § 9-3 (1) ikke er inngått og
mottaker ikke er MVA-registrert ved overføring. KWE må tilbakebetale
fradragsført MVA for resten av 10-årsperioden (potensielt flere hundre
tusen kroner).»

**Styrke:** **4/5.** Skatteetaten vil fange opp dette hvis
dokumentasjonen ikke er i orden ved overføringstidspunktet.

**Forsvar:** Justeringsavtale etter § 9-3 (1) inngås skriftlig mellom
KWE og Grønnegata 10 AS **samme dag** som Brreg-registrering av fisjon.
Grønnegata 10 AS MVA-registreres samtidig (frivillig § 2-3 for samme
kontorutleie som KWE har i dag). Dokumentert via standardskjema
RF-1241 (eller tilsvarende). Angrepet nøytraliseres.

**Note:** Dette angrepet forutsetter at konto 1172 FG30-renovering er
behandlet riktig (ingen fradragsføring) — hvis det likevel er
fradragsført, må vi ha tilsvarende struktur for FG30. Verifisering med
regnskapsfører er obligatorisk før fisjonsvedtak.

### D5. Strafferettslig — strl. § 401/402 (kreditorsvik ved formuesforringelse)

**Formulering:** «Styret i KWE gjennomfører fisjon mens konkursvarsel er
mottatt og tvangsmulktsak pågår. Fortsettende KWE får beholdt gjelden
(konsernlån + tvangsmulkt) men mister alle verdiene. Dette er
forsettlig formuesforringelse under fare for insolvens. Rammes av strl.
§ 401 — grovt uaktsom boforringelse etter § 404 subsidiært.»

**Styrke:** **1/5 som rettssak.** Strafferettslig forfølgning av
styremedlemmer er sjelden når det foreligger formell revisor- og
advokatgjennomgang. **3/5 som intimideringsargument** — kan brukes av
TBRT, Intrum eller en bostyrer for å presse frem forlik eller stans.

**Forsvar:** Alle seks forsvarsargumenter fra seksjon A4. Særlig:
Markedspris, solidaransvar beholdt, kreditorvarsel kjørt riktig,
forretningsmessig begrunnelse (MVA 6,2 MNOK, bank, tilskudd),
dokumentert styreprotokoll. Angrepet nøytraliseres som rettssak;
intimideringsrisikoen reduseres hvis forsvarspakken er klar fra start.

### D6. Rangert tabell

| # | Angrep | Styrke | Vinnbarhet forsvar | Nøkkelmitigering |
|---|---|---|---|---|
| D1 | Dekningsloven § 5-9 (tom skalk) | 5/5 | Høy | Konvertering av konsernlån + morselskapsgaranti |
| D2 | Styreansvar asl. § 17-1 | 4/5 | Høy | Intrum stabilisert + dokumentert styreprotokoll + D&O-forsikring |
| D3 | Kontinuitetsbrudd fisjon→emisjon | 3/5 | Høy | 6–8 ukers avstand + separat dokumentasjon |
| D4 | MVA-justeringsavtale Grønnegata | 4/5 | Høy | Avtale signert og MVA-reg samtidig med Brreg |
| D5 | Strl. § 401/402 kreditorsvik | 1/5 (sak), 3/5 (intim.) | Høy | Hele forsvarspakken + revisor-/advokatgjennomgang |

**Felles tema:** Alle fem angrep nøytraliseres i stor grad med samme
pakke: (a) Konsernlån-restrukturering, (b) Intrum-stabilisering,
(c) Dokumentert styreprotokoll med forsvarlighetsvurdering,
(d) Revisorerklæringer (fisjon + justeringsavtaler + senere emisjon),
(e) 6–8 ukers avstand fisjon→emisjon, (f) MVA-dokumentasjon korrekt
timet.

---

## Endringer fra v1

| Område | v1-posisjon | v2-posisjon | Grunn |
|---|---|---|---|
| Dekningslovsfrister | Nevner 2 år/10 år; litt diffust | Presis tabell §§ 5-2 til 5-9 med alle frister | Review 01 flagget inkonsistens; Agent 3 koordinering |
| Insolvensvurdering | Antyder «delikat» | Konkret: bokført insolvent, men virkelig suffisient; strukturell insolvens oppstår ved foreløpig fordeling | Regnskapstall tilgjengelig |
| Styreansvar asl. § 17-1 | Flagget som åpent | Full seksjon A3 med dokumentasjonskrav | Nytt mandat |
| Strafferettslig grense | Flagget som åpent | Full seksjon A4 med grensemarkører | Nytt mandat |
| MVA-justering | «må gjøres sammen med MVA-rådgiver» | Konkret analyse mot mval. kap. 9 verbatim; justeringsavtale obligatorisk for Grønnegata, ikke for FG30 (forutsatt konto 1172 inkl. MVA) | Mval. kap. 9 lastet |
| MVA-tidsrekkefølge | Antydet | Grønnegata-reg samtidig med Brreg; FG30-reg i Q2 2027 med tilbakegående § 8-6 (3 års frist, ikke 6 mnd) | Mval. kap. 9 + Agent 4 fristkorrigering |
| Nye aksjonærer | Ikke behandlet | Full seksjon B2: fisjon først, 6–8 ukers avstand, arbeidsplikt utelukket | Nytt mandat |
| Grønnegata-isolering | Ikke behandlet | Full seksjon B3: formelt umulig, reelt mulig via plassering + dekning + regress-klausul + Agent 3s mekanismer | Nytt mandat |
| Konsernlån-restrukturering | Ikke behandlet | Full seksjon C1: anbefaler konvertering til EK (Alternativ 1) | Nytt mandat |
| Framførbart underskudd | Nevnt kort | Full seksjon C2: lovlig å plassere i FG30 AS | Nytt mandat |
| Pålegg og offentligrettslig | «juridisk uavklart» | Standpunkt: pålegget følger eiendommen; tvangsmulktvedtaket følger KWE | Agent 3-koordinering |
| Djevelens advokat | Ikke behandlet | Fem rangerte angrepspunkter med forsvar | Nytt mandat |
| Dekningslov § 5-9 og KWE-insolvens | Overføringsrisiko kvalitativt | Dekningsgrad kvantitativt 2,9× etter mitigering (Agent 3) | Regnskapstall + Agent 3 koordinering |

---

## Åpne spørsmål

1. **Konto 1172 Renovering FG30 — inkl. eller ekskl. MVA?** Må
   verifiseres med regnskapsfører før fisjonsvedtak. Hvis ekskl.
   (fradragsført), er FG30 også kapitalvare og det må lages
   justeringsavtale KWE→FG30 AS samtidig med fisjon.

2. **Historisk fradragsført MVA på Grønnegata 10 bygg og teknisk
   installasjon.** Hvor mye er fradragsført siden 2020? Dette styrer
   restforpliktelsens størrelse hvis justeringsavtale ikke lages. Må
   avklares med regnskapsfører.

3. **Bokføringsformat for konsernlån-vilkårene.** Konvertering til EK
   (Alternativ 1) er juridisk mest robust, men krever styrevedtak i
   KodeWorks AS. Beslutter styreleder (brukeren) om dette er politisk
   gjennomførbart?

4. **Tingsinnskuddets natur (Brandsegg og Lagmannssveen).** Må brukeren
   klargjøre: kontanter, fysiske eiendeler, immaterielle verdier,
   gjeldskonvertering fra pågått arbeid? Dette styrer hele
   emisjonsstrukturen.

5. **Styreforsikring (D&O).** Finnes det allerede? Hvis ikke, må
   tegnes før fisjonsvedtak. Premiespørsmål til bruker.

6. **KodeWorks AS' balanse.** For å stille 1 MNOK morselskapsgaranti må
   KodeWorks AS være solvent og ha realistisk egenkapital. Agent 4
   flagget behov for balansegjennomgang; dette er fortsatt åpent.

7. **Fisjonsstikkdag.** 01.01.2027 anbefalt (Agent 2). Må samordnes med
   konsernlån-konverteringen (må være gjort før eller samme dag).

---

## Interaksjoner med andre agenter

**Agent 2 (Prosjektleder):**

- **Konsernlån-konvertering er juridisk anbefaling.** Agent 2 må legge
  dette inn som egen aktivitet i uke 44–48 (styrevedtak i KodeWorks AS
  + KWE, revisorerklæring). Dette endrer dokumentlisten i Agent 2 v2
  seksjon 5.
- **Grønnegata 10 AS MVA-registrering flyttes fram** — fra Agent 2s
  uke 10 til samtidig med Brreg-registrering av fisjon. Juridisk
  nødvendig for § 9-3-justeringsavtalen.
- **FG30 AS MVA-registrering utsettes** fra uke 10 til Q2 2027 når
  driften starter. Tilbakegående avgiftsoppgjør etter mval. § 8-6 (3
  år) løfter byggefasens MVA.
- **Styreforsikring (D&O) legges inn som dokument i uke 44–45.** Agent 2
  dokumentliste må oppdateres.
- **6–8 ukers avstand fisjon→emisjon:** Agent 2 uke 12–14-plan for
  emisjon kan være for tett (ca. 3 uker etter Brreg). Vurder forlenge
  til uke 16–20 (minst 6 uker etter Brreg).

**Agent 3 (Tvangsmulkt-strateg):**

- **Dekningsstrukturen (A + C) bekreftes juridisk** med tilleggskrav om
  markedsmessig garantiprovisjon (1 % per år) for å nøytralisere
  skatterisikoen i KodeWorks AS.
- **Konsernlåns-fordeling (Agent 3 mekanisme A) erstattes delvis av
  konvertering til EK (Alternativ 1).** Hvis konvertering gjennomføres,
  er fordeling av resten enklere. Dette er en forbedring, ikke en
  avvisning av Agent 3s struktur.
- **Dekningslovsfrister:** Standard forståelse bekreftes
  (§ 5-9 2/10 år; §§ 5-5–5-7 3 måneder objektiv). Verifiseres fase 10.
- **Eksplisitt-klausul i fisjonsplanen om tilbakevirkende innkreving:**
  Bekrefter at klausulen ikke binder TBRT som tredjepart, men regulerer
  intern regress mellom selskapene. Nyttig som dokumentasjon av intensjon.
- **Djevelens advokat-angrep #1 og #4 i Agent 3s liste korresponderer
  med D1 og D4 i min liste.** Konvergens mellom analysene.

**Agent 4 (Finans- og tilskuddsanalyst):**

- **Konto 1172 — inkl. eller ekskl. MVA?** Agent 4 har tilgang til
  regnskapet; bør verifisere og tilbakerapportere.
- **Historisk fradragsført MVA på Grønnegata-eiendelene** — hvor mye
  siden 2020? Styrer restforpliktelsens størrelse.
- **Tilbakegående avgiftsoppgjør mval. § 8-6:** 3-årsfristen bekreftes
  (Agent 4 har rettet v1-feilen 6 mnd → 3 år; dette holder i min
  gjennomgang av kap. 9 og tilgrensende regler).
- **Konvertering av konsernlån:** Agent 4 må oppdatere åpningsbalansene
  i seksjon 2 (fortsettende KWE får konsernlån → aksjekapital/overkurs
  i stedet; andre selskaper får ikke andel av konsernlånet). Dette
  forenkler Agent 4s balansering vesentlig.
- **Internprising-rente:** 9,2 % er høyt sammenlignet med marked (ca.
  6,5–7,5 %). Hvis konvertering ikke gjennomføres og vilkårene
  reforhandles ved fisjon, bør renten justeres til markedsrente.
  Agent 4 har flagget dette; bekreftes juridisk.

---

*Agent 1 — Fisjonsjurist, v2, 2026-10-12. Analyse-only; lovreferanser
utenom mval. kap. 9 verifiseres fase 10. Skrevet direkte til
`agent_01_fisjonsjurist_v2.md`.*
