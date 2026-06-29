# Sammendrag: ../stotte-prosjektet

*Lest fra `../stotte/` (CLAUDE.md, README.md, kravspek.txt, project_cards_template.json, history-log.md) 2026-06-27. Internt referansedokument – brukes som grunnlag for vedlegg til støttesøknader og som veiledning for koordinering av FG30s tilskudd.*

---

## 1. Hva er ../stotte?

`../stotte` er et regnskapssystem for å spore kostnader, timer og rapporteringsforpliktelser på tvers av alle tilskuddsfinansierte prosjekter i tre selskaper: **Sunlit Sea AS**, **EnerSky AS** og **KodeWorks Eiendom AS**.

Systemet består av to komponenter:

1. **Google Sheets-arbeidsbok** (produseres av `src/build_sunlit.py`): Interaktivt regneark der man importerer data fra regnskapssystemet (Tripletex) og timelister (Werkz), og manuelt allokerer bilag og timer til tilskuddsprosjekter og arbeidspakker.

2. **Python-referansemotor** (`src/engine.py`): Implementerer samme logikk som regnearkformler, men over CSV-input. Brukes til å validere at regnearkformlene er korrekte. Python-motoren er semantisk fasit; regnearkformelen er leveransen.

### Datamodell

**`project_cards.json`** er masterregisteret for alle tilskudd. Hvert prosjektkort inneholder:

| Felt | Beskrivelse |
|---|---|
| `ProjectID` | Stabilt identifikator (f.eks. `KMF-FG30`) |
| `ProjectName` | Offisielt prosjektnavn |
| `Company` | Selskap |
| `SchemeID` | Tilskuddsordning (`ENOVA`, `KMF`, `BYA` osv.) |
| `GrantReference` | Offisiell referanse fra tilskuddsgiver |
| `TotalBudget` | Godkjent totalbudsjett |
| `GrantAmount` | Bevilget tilskudd |
| `SupportIntensity` | Støtteintensitet som desimal (f.eks. `0.30` = 30 %) |
| `DurationFrom/To` | Prosjektperiode |
| `ReportingDates` | Rapporteringsfrister med type, mottaker og mal |
| `PaymentDates` | Utbetalingsfrister med trigger og status |
| `UsageConstraints` | Hva som er støtteberettiget/ikke-støtteberettiget |
| `SpecialRules` | Ordningsspesifikke dokumentasjonskrav |
| `workpackages` | Arbeidspakker med budsjett, periode og deltakere |
| `budget_categories` | Kostnadskategorier (a1, a3, b, c1, c2, c3, e) |

FG30 har divergert noe fra malen i `../stotte/project_cards_template.json`, men bruker det samme grunnformatet.

---

## 2. Filosofien bak støttekoordinering

Målet er å koordinere **flere støtteordninger mot det samme prosjektet** slik at samlet offentlig støtte maksimeres, uten å overstige taket for statsstøtte.

### Grunnprinsippet

Alle godkjente kostnader i prosjektet er potensielt støtteberettigede under én eller flere ordninger. Systemet allokerer kostnader (bilag) og timer til de ordningene de er berettiget under, og beregner for hvert kostnadselement den **kombinerte støtteintensiteten**:

```
KombinertIntensitet = Σ (beløp krevd av ordning × intensitet) / totalkostnad
```

Denne intensiteten sammenlignes med taket – og systemet viser «headroom» (rom for ytterligere støtte) og flagger brudd.

### Viktig: Ingen bilag kan telles dobbelt

Én kostnad kan **ikke** kreves refundert av to ordninger for samme beløp. Den kan imidlertid **fordeles** mellom ordninger – f.eks. 50 % til KMF og 50 % til BYA – så lenge summen ikke overstiger 100 % av kostnaden.

---

## 3. Kumuleringsprinsippet

**Kumulering** betyr at støtte fra flere ordninger på den *samme* kostnad legges sammen. Statsstøtteregelverket setter et tak for samlet støtteintensitet (GGE = Gross Grant Equivalent):

| Aktivitetstype | Tak (stor bedrift) | Tak (liten/middels) |
|---|---|---|
| Kulturminnerehabiltering (EU-regelverk) | 50–70 % | Opp til 70 % |
| Industriell forskning (R&D) | 50 % | 70 % |
| Eksperimentell utvikling (R&D) | 25 % | 45 % |

For FG30 (verneklasse B, rehabilitering) er det mest relevante taket **70 %** (Kulturminnefondet vedtekter, FOR-2003-06-27-801).

### Praktisk eksempel

En kostnad på 1 000 000 kr:
- KMF bevilger 30 % → 300 000 kr
- BYA bevilger 30 % → 300 000 kr
- UNI bevilger 10 % → 100 000 kr
- **Samlet intensitet: 70 %** → opp til taket, lovlig

Men: 30 % (KMF) + 40 % (BYA) + 10 % (UNI) = 80 % → **BRUDD** – må redusere én av ordningene.

### Konsekvens for FG30

For å nærme seg 70 %-taket på flest mulig kostnader, bør alle fakturaer og lønnskostnader allokeres **på tvers av alle aktive ordninger** i den grad de er støtteberettigede under hver ordning. Dette gjøres *etter* at kostnader er kjent – ikke løpende.

---

## 4. Håndtering av overlapp mellom prosjekter

### Regler

1. **Samme kostnad kan ikke dekkes 100 % av to ordninger.** Ordningene må ha separate budsjetter.
2. **Kostnader kan fordeles.** En faktura for ryddearbeid i kjeller kan f.eks. allokeres 50 % til KMF-FG30 og 50 % til BYA-FG30 – men kun hvis begge ordningene tillater denne kostnadstypen.
3. **Støtteberettigede kostnader er ordningsspesifikke.** KMF tillater innkjøp av håndverkertjenester; BYA tillater forsterking av fundamenter. Overlapp finnes, men grensene er ulike.
4. **Dokumentasjonskrav kumuleres.** Alle ordninger krever faktura + kvittering + fotodokumentasjon. Det holder med én dokumentasjonspakke per kostnad, men den må oppfylle alle ordningenes krav.

### Systemets rolle

`voucher_alloc.csv` og `hour_alloc.csv` (i `../stotte/`-prosjektet) inneholder bilagstilordninger og timeavdelinger per prosjekt. Systemet beregner automatisk om kombinert intensitet per kostnadselement er innenfor taket.

---

## 5. FG30: Aktive ordninger og koordinering

Per 2026-06-27:

| Ordning | Tilskudd | Intensitet | Godkjent budsjett | Status |
|---|---|---|---|---|
| Kulturminnefondet (KMF) | 750 000 kr | 30 % | 2 500 000 kr (revidert) | Aktiv – utbetaling ikke anmodet |
| Byantikvaren (BYA) | 500 000 kr | 30 % (revidert) | 1 666 667 kr (revidert) | Aktiv – utbetaling ikke anmodet |
| Stiftelsen UNI | 100 000 kr | 5,6 % | 1 785 000 kr | Aktiv – utbetaling ikke anmodet |
| Enova Energikartlegging | 400 000 kr | 50 % | 800 000 kr | Rapport ferdig – utbetaling mulig |
| Enova Ombrukskartlegging | 500 000 kr | 50 % | 1 000 000 kr | Status uavklart |

**Koordinering KMF + BYA + UNI:**
Disse tre ordningene gjelder delvis overlappende kostnader (bærende konstruksjoner, kulturminneverdier, brannsikring). For å nå 70 %-taket bør en FG30-rehabiliteringsfaktura allokeres slik:
- 30 % KMF (kulturminnetiltak generelt)
- 30 % BYA (bærekonstruksjon, steinmur, antikvariske tiltak)
- 10 % UNI (brannsikringsrelaterte tiltak)
- = **70 % samlet** → maks lovlig

**Enova:**
Støttes ikke av KMF/BYA/UNI for de samme kostnadene – andre kostnadstyper (energikartlegging, ombrukskartlegging = rådgivningstjenester, ikke byggearbeider).

### Vurderte fremtidige ordninger

| Ordning | Vurdering |
|---|---|
| SkatteFunn 2026 | Søknadsskisse laget (T70). FoU-spor: digital lagringsplattform. Potensielt 285–570k NOK i skattefradrag. |
| Innovasjon Norge Oppstartstilskudd | Søknadsskisse laget (T71). 200–250k NOK potensielt. |
| Mer fra KMF og BYA | Begge har antydet interesse for ny runde etter at IG er innvilget. |
| Enova ytterligere | Energioppgradering (T1-pakken: 53 % reduksjon, energimerke D) kan gi nye søknadsmuligheter. |

---

## 6. Verktøy og filer

| Fil/mappe | Innhold |
|---|---|
| `../stotte/project_cards.json` | Masterregister for alle tilskudd (Sunlit Sea, EnerSky, KodeWorks Eiendom) |
| `../stotte/project_cards_template.json` | Template med feldbeskrivelser og instruksjoner |
| `../stotte/kravspek.txt` | Kravspesifikasjon for systemet |
| `stotte/project_cards.json` | FG30-spesifikk kopi med litt avvik fra malen |
| `stotte/project_cards.json` | Oppdatert fra primærkilder (tilsagnsbrev, budsjetter) under T61 |

### Merk: Divergens fra ../stotte-malen

FG30s `stotte/project_cards.json` har divergert noe fra `../stotte/project_cards_template.json`. Forskjellene er primært:
- Feltnavngivning (noen FG30-spesifikke felt er lagt til)
- Rapporteringsstruktur (tilpasset norske kulturminnefond-ordninger)
- Ingen `workpackages`-struktur (FG30 har ikke EU-liknende arbeidspakker)

---

## 7. Praktisk veiledning for FG30

1. **Legg alle fakturaer i det godkjente budsjettet** for minst én ordning. Sjekk `UsageConstraints.eligible` i project_cards.json per ordning.
2. **Allokér bilag på tvers av ordninger** så nær 70 % samlet intensitet som mulig, uten å overstige.
3. **Dokumentér alt med bilag + foto** – dette er den minste felles nevner for alle ordningene.
4. **Send utbetalingsanmodning** etter at tilstrekkelig arbeid er dokumentert. For KMF/BYA/UNI: rapport + regnskapsbilag. For Enova: via Enovas søknadsportal.
5. **Oppdater `stotte/project_cards.json`** med faktiske utbetalte beløp og rapporteringsstatuser.
