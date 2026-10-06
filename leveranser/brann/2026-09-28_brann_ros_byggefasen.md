---
title: "Brann-ROS – gjennomføringsfasen Fjordgata 30"
subtitle: "Risiko- og sårbarhetsanalyse for byggeperioden"
author: "KodeWorks Eiendom AS"
date: "28. september 2026"
version: "1.0"
---

## Formål

Denne analysen identifiserer brannscenarier i gjennomføringsfasen for Fjordgata 30, vurderer sannsynlighet og konsekvens, og fastsetter kompenserende tiltak som holder restrisikoen på et forsvarlig nivå så lenge permanente branntekniske installasjoner (ABA, sprinkler, inertgassanlegg) ikke er ferdig etablert.

ROS-en er levende dokumentasjon. Den oppdateres månedlig og ved vesentlige endringer i rigg, arbeidsmetode, åpninger i bygningskropp eller andre forhold som kan påvirke brannrisiko, jf. HRPs notat pkt. 4.

Grunnlag:

- HRP AS: «FG30-Brannsikring i gjennomføringsfasen» (26.02.2026)
- HRP AS: Brannkonsept BKL3/TEK17 og brannprosjektering for minilager (16.–17.02.2026)
- Autronica Fire and Security: Årlig kontroll brannalarmanlegg 12.05.2026 (ingen avvik)
- Tensio TS AS: DLE-tilsynsrapport 20.09.2026 (elektrisk anlegg uten anmerkninger)
- Brannkartlegging Kristian B. Brandsegg (24.09.2026) og Ole Morten Lagmannssveen (25.09.2026)

## Byggets forutsetninger

Fjordgata 30 er et vernet bryggebygg fra 1857 (påbygget 1904) i tett trehusbebyggelse langs Nidelva/kanalen i Midtbyen, Trondheim. Konstruksjonen er laftet tre i 1. og 2. etg., bindingsverk i 3.–5. etg. Rehabiliteringen er en samlet gjennomføringsfase. Bruken gir **brannklasse 3, risikoklasse 2** med sporadisk personopphold i byggefasen.

Særskilt sårbarhet:

- Eldre trekonstruksjoner med skjulte hulrom eksponeres når innervegger fjernes.
- Rask intern brannspredning i lafteverk og gamle tørrhulrom.
- Kort avstand til nabobrygger – fasadespredning og smittebrann er kritisk risiko.
- Sprinkleranlegg dekker kun føringer langs ytterveggene, alle etasjer. Kjeller ikke dekket.
- Permanent ABA ikke etablert; midlertidig deteksjon i aktive arbeidsområder er ikke ferdig anskaffet.
- Byggeperioden strekker seg gjennom vinteren – behov for oppvarming introduserer ny risiko.

## Metodikk

Sannsynlighet og konsekvens vurderes hver på tre nivåer (L = lav, M = middels, H = høy). Risikonivå settes som `S × K`:

| S × K | Beskrivelse |
|---|---|
| Lav (L×L, L×M, M×L) | Akseptabelt – standardtiltak tilstrekkelig |
| Middels (M×M, L×H, H×L) | Krever aktive kompenserende tiltak |
| Høy (M×H, H×M, H×H) | Krever spesifikke tiltak og løpende oppfølging |

Restrisiko er risikonivå etter at kompenserende tiltak er på plass og etterleves.

## Identifiserte scenarier

### S1 – Antennelse fra elektrisk feil i fast anlegg

**Uten tiltak:** Sannsynlighet M, konsekvens H → **høy**. \
**Tiltak:** Tensio DLE-tilsyn 18.09.2026 uten anmerkninger; ingen byggstrøm i drift (kun eksisterende sikringsskap brukes, overflødige koblet ut); årlig internkontroll av elektrisk anlegg. \
**Restrisiko:** L×H → **middels**. Akseptabelt gitt sertifisert kontroll.

### S2 – Antennelse fra midlertidig el-anlegg (skjøteledninger, arbeidslys)

**Uten tiltak:** S H, K H → **høy**. \
**Tiltak:** Kun LED-arbeidslys, forbud mot seriekobling og kveilede skjøteledninger, obligatorisk utkobling ved arbeidsdagens slutt (sluttkontroll-sjekkliste), ukentlig visuell inspeksjon, formalisert rutine (`brann_rutiner_byggefasen.md` rutine 2). \
**Restrisiko:** L×H → **middels**.

### S3 – Antennelse fra byggtørker eller varmeovn i vinter

**Uten tiltak:** S M–H, K H → **høy**. Særlig relevant fra oktober–april. \
**Tiltak:** Byggtørker/varmeovn skal være fastmontert eller veltesikret, minimum 1 m avstand til brennbart materiale, sjekk hver time under drift, avslått ved arbeidsdagens slutt. Se `plan_midlertidig_oppvarming_vinter.md`. \
**Restrisiko:** L×H → **middels**. Rutinen må følges strengt.

### S4 – Antennelse fra sigaretter

**Uten tiltak:** S M, K H → **middels**. \
**Tiltak:** Totalforbud mot røyking inne. Fast røykeplass ute ved hoveddør med askebeger. Kommunisert i byggeplassinstruks. \
**Restrisiko:** L×M → **lav**.

### S5 – Selvantennelse i olje-/impregnerings-holdig avfall

**Uten tiltak:** S L–M, K H → **middels–høy**. \
**Tiltak:** Filler, papir og kluter med olje eller impregnering skal legges i brannsikker beholder. Sluttkontroll-sjekkliste (punkt for dette). Avfallscontainer trukket ut av bygget hver kveld. \
**Restrisiko:** L×H → **middels**.

### S6 – Antennelse under åpning av hulrom i tre-konstruksjon

**Uten tiltak:** S M, K H → **høy**. Bygget har mange skjulte hulrom med gammelt tørt materiale. \
**Tiltak:** Åpning av hulrom skal avklares med brannansvarlig først. Håndslokker skal stå tilgjengelig innen 5 m fra arbeidsplass før åpning starter. Ekstra deteksjon vurderes for lengre arbeid. Totalforbud mot varme arbeider – kun elektrisk motorsag og manuelle verktøy tillatt. \
**Restrisiko:** L×H → **middels**.

### S7 – Påsatt brann / inntrenging utenom arbeidstid

**Uten tiltak:** S M, K H → **høy**. Bygget står midt i sentrum, nær offentlig areal. \
**Tiltak:** Bygget låses hver kveld (Ain og Marco har ansvar). Autronica-sentralen aktiv 24/7 og varsler 110 automatisk ved deteksjon. Innskrivingsliste sikrer at ingen er inne uten kjent identitet. Vurdering av kameraovervåking pågår (HRP-notat pkt. 6). \
**Restrisiko:** L×H → **middels**. Ekstra fysisk sikring av åpninger og stillas prioriteres når rigg endres.

### S8 – Brann i avfallscontainer sprer til bygg

**Uten tiltak:** S L, K H → **middels**. \
**Tiltak:** Containere står minst 1,5 m fra yttervegg, ute av bygget hver kveld (leveres av Franzefoss samme morgen som brukes, hentes samme kveld). Se `brann_rutiner_byggefasen.md`. \
**Restrisiko:** L×M → **lav**.

### S9 – Fasadespredning til nabobrygger

**Uten tiltak:** S L, K H → **middels–høy**. Særlig kritisk gitt tett trehusbebyggelse. \
**Tiltak:** Åpninger i fasade minimeres og tettes midlertidig med brannklassifiserte materialer der praktisk mulig. Der tetting ikke kan etableres: lokal seksjonering og fysisk avskjerming av fasade og stillas. Nabobrygger er orientert via rammesøknad-nabovarsel. Løpende samordning ved arbeid som kan påvirke naboer. \
**Restrisiko:** L×H → **middels**. Krever aktiv samordning.

### S10 – Brann i nabobrygge sprer til Fjordgata 30

**Uten tiltak:** S L, K H → **middels**. Vi kan ikke kontrollere risikoen hos naboer. \
**Tiltak:** Sprinkleranlegget langs yttervegger gir passiv beskyttelse mot smittebrann utenfra (der det er i drift). Autronica varsler 110 automatisk ved deteksjon også utenom arbeidstid. Rømningsveier fra Fjordgata 30 samordnes med nabobryggenes rømningsplaner. \
**Restrisiko:** L×H → **middels**. Kan ikke reduseres ytterligere uten permanente installasjoner.

### S11 – Falsk alarm forsinker respons på reell brann

**Uten tiltak:** S M, K M → **middels**. Falske alarmer fra tildekket eller støvet detektor kan gjøre personell mindre lydhøre. \
**Tiltak:** Tildekkingsprosedyre (`brann_rutiner_byggefasen.md` rutine 1) hindrer utilsiktet tildekking. Alle alarmer behandles som ekte til brannansvarlig bekrefter noe annet. Autronica varsler 110 automatisk, uavhengig av manuell kvittering. \
**Restrisiko:** L×M → **lav**.

### S12 – Utsatt oppdagelse i kjelleren (ikke sprinklerdekket)

**Uten tiltak:** S L–M, K H → **middels**. Kjelleren har detektorer, men ikke sprinkler. \
**Tiltak:** Trådløse midlertidige sensorer skal anskaffes (bestilles av Ole Morten iht. tiltaksplan Trinn 3.1). Byggeplassinstruks framhever ekstra årvåkenhet ved kjellerarbeid. Håndslokker plasseres tilgjengelig i kjelleren under aktivt arbeid. \
**Restrisiko:** L×H → **middels** – går ned til lav etter trådløse sensorer er på plass.

## Risikomatrise – oppsummert restrisiko

| Scenario | Restrisiko | Kommentar |
|---|---|---|
| S1 – El-feil fast anlegg | Middels | DLE-godkjent |
| S2 – El-feil midlertidig anlegg | Middels | Rutine etterleves |
| S3 – Byggtørker/varmeovn vinter | Middels | Krever streng disiplin |
| S4 – Sigaretter | Lav | Regulert |
| S5 – Selvantennelse avfall | Middels | Brannsikker beholder |
| S6 – Antennelse i hulrom | Middels | Slokker tilgjengelig |
| S7 – Påsatt brann | Middels | Låsing + Autronica |
| S8 – Avfallscontainer | Lav | Avstand + ut hver kveld |
| S9 – Fasadespredning ut | Middels | Aktiv samordning |
| S10 – Fasadespredning inn | Middels | Utenfor egen kontroll |
| S11 – Falsk alarm | Lav | Rutine + 110 uansett |
| S12 – Kjeller uten sprinkler | Middels | Midlertidig sensorer bestilles |

**Samlet vurdering:** Restrisikoen ligger på middels for de fleste scenariene og lav for de øvrige. Ingen scenarier ligger på høy restrisiko forutsatt at rutinene etterleves. Det er ingen scenarier der prosjektet må stanse. HRP-notatets prinsipp om at permanente installasjoner etableres først i ferdig bygg, og at gjennomføringsfasen sikres med kompenserende tiltak, holder — men bare så lenge tiltakene er dokumenterbare og etterleves i praksis.

## Kritiske forutsetninger for at analysen holder

1. Byggeplassinstruks henges opp og etterleves.
2. Sluttkontroll-sjekkliste fylles ut hver dag.
3. Tildekkingsprosedyre følges uten unntak.
4. Trådløse midlertidige sensorer anskaffes og settes i drift i aktive arbeidsområder og hulrom (planlagt uke 43).
5. Håndslokker-kontroll gjennomføres iht. tiltaksplan Trinn 2. Sprinklerens overvåkning er testet av Autronica 12.05.2026; separat hydraulisk test av selve tørranlegget vurderes.
6. Avvikslogg føres og gjennomgås månedlig.
7. Brann-ROS oppdateres ved endringer.

Hvis en eller flere forutsetninger svikter, må risikonivået revurderes umiddelbart.

## Revisjonshistorikk

| Versjon | Dato | Endring | Ansvarlig |
|---|---|---|---|
| 1.0 | 28.09.2026 | Første versjon – baseline før vintersesong | Brannansvarlig |

Neste planlagte gjennomgang: **31.10.2026** (månedlig oppdatering).\
Ekstern revisjon utløses ved: åpning av hulrom over 2 m², endring av rømningsveier, oppstart av bygg­tørker/varmeovn, avvik i S1–S12 som er meldt inn.
