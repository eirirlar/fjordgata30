---
tittel: Iterasjon 02 — merge av fire v2-leveranser
fase: Fase 5 (hovedsesjonens merge 2)
dato: 2026-10-12
scope: >
  Tematisk sammenstilling av Agent 1 v2 (Fisjonsjurist), Agent 2 v2
  (Prosjektleder), Agent 3 v2 (Tvangsmulkt-strateg) og Agent 4 v2
  (Finans- og tilskuddsanalyst). Bygger på `iterasjon_01_merged.md`
  og `bruker_input_01.md`. Motsigelser og hull løftes i `review_02.md`.
  Lovreferanser markert [verifiseres fase 10] med unntak av mval. kap. 9
  (lastet ned verbatim av Agent 1).
---

# Iterasjon 02 — merge av fire v2-leveranser

Fase 4 har levert et vesentlig mer konkret bilde enn fase 1: faktiske regnskapstall, bekreftet MVA-strategi, kjent pantesituasjon, konkrete åpningsbalanse-utkast, konsernlåns-restrukturering, nye aksjonærer, og en rangert djevelens advokat-forberedelse. Dette er grunnlaget hovedsesjonen og brukeren bruker for å beslutte om fase 7 (djevelens advokat) kan starte.

---

## 1. Oppsummering

**Fisjonen er juridisk og operativt gjennomførbar.** Minimum realistisk tidsramme: fisjon ferdig ca. midten av mars 2027, emisjon ca. 2–8 uker etter (uenighet om minimum avstand — Agent 1 anbefaler 6–8 uker, Agent 2 skrev 2–4 uker). Totalkostnad: ca. 350 000–470 000 kr (median 410 000), opp fra 345 000 i fase 1 pga. ny emisjon og tingsinnskudd-dokumentasjon.

**Hovedutfordringer identifisert i fase 4:**

1. **Fortsettende KWE blir strukturelt insolvent** med den foreløpige fordelingen (bokført EK ca. –10,8 MNOK). Dette utløser styreansvar (asl. § 17-1) og dekningslov § 5-9-risiko. Må løses før fisjonsvedtak.
2. **Konsernlånet 10,6 MNOK** fra KodeWorks AS er den enkeltvariabelen som dominerer egenkapital-residualen i hvert selskap. To hovedalternativer: konvertering til EK (Agent 1 anbefaler) eller proporsjonal fordeling (Agent 3/4 anbefaler).
3. **Nye aksjonærer med tingsinnskudd:** fisjon først + emisjon etter er den eneste veien som bevarer skattefri status. Men tidsmessig avstand må være 6–8 uker (Agent 1), ikke 2–4 (Agent 2).
4. **Arbeidsplikt er ikke lovlig tingsinnskudd** (asl. § 2-7). Hva Brandsegg/Lagmannssveen faktisk tilfører må avklares av brukeren.
5. **MVA-strategi bekreftet:** FG30 AS registreres etter fisjon ved driftsstart (Q2 2027), med tilbakegående avgiftsoppgjør etter mval. § 8-6 (3-årsfrist, ikke 6 mnd som i v1). Grønnegata 10 AS må registreres **samtidig med** Brreg-registrering for å unngå justering etter mval. § 9-2.
6. **Konto 1172 (Renovering FG30, 817 151 kr):** må verifiseres om det er bokført inkl. eller ekskl. MVA. Agent 1 antar inkl. MVA (ingen fradrag tatt) — hvis ekskl., må justeringsavtale lages også for FG30.
7. **Intrum-sporet er fortsatt kritisk sti.** Konkursvarsel-fristen 27.10.2026 avgjør om fisjonsarbeid kan fortsette (grønt/gult/rødt lys-beslutningstre fra Agent 3).

**Robust konvergens på tvers av agentene:**

- Alt 1A plassering av påløpt tvangsmulkt hos fortsettende KWE (beskytter partsstatus i DSB-/Sivilombud-saker).
- Fisjon først, emisjon etter (bevarer skattefri status).
- Grønnegata-isolering oppnås praktisk (ikke formelt) gjennom eksplisitt plassering i fisjonsplanen + robust dekning hos fortsettende.
- Timing: Scenario A modifisert, gitt grønt lys fra Intrum-sporet (TBRT instruerer stans). Scenario B som backup.

---

## 2. Juridisk prosedyre og rammer — oppdatert

### 2.1 Dekningsloven kap. 5 — presise frister

Agent 1 har levert tabell basert på standard forståelse (verifiseres fase 10):

| Hjemmel | Disposisjon | Frist mot ordinære | Frist mot nærstående |
|---|---|---|---|
| § 5-2 | Gaver, gaveliknende disposisjoner | 1 år før fristdag | 2 år |
| § 5-3 | Utbetaling/vederlagsfri overføring til nærstående aksjonær | — | 2 år |
| § 5-5 | Ekstraordinær betaling av gjeld | 3 måneder | 2 år |
| § 5-6 | Pantsettelse til sikkerhet for eldre gjeld | 3 måneder | 2 år |
| § 5-7 | Betaling/sikkerhet etter tvangsfullbyrdelse | 3 måneder | — |
| § 5-9 | Utilbørlige disposisjoner (subjektiv omstøtelse) | **2 år** | **10 år** |

For denne fisjonen er FG30 AS og Grønnegata 10 AS nærstående til fortsettende KWE etter dekningsloven § 1-5 [verifiseres fase 10] (konsernforhold). Hovedhjemmelen er § 5-9 med 10 års tilbakevirkende frist. 3-mnd-vinduet gjelder parallelle disposisjoner (gjeldsbetalinger, pantestillelser) — ikke selve fisjonen.

### 2.2 Styreansvar (asl. § 17-1) og handleplikt (asl. § 3-5)

Hvis fisjonen gjennomføres med strukturelt insolvent fortsettende KWE, utløses både handleplikt og styreansvar. Agent 1 har beskrevet syv krav til styreprotokollen for å beskytte seg:

1. Forretningsmessig begrunnelse (MVA, bank, tilskudd, risikoseparasjon) med konkrete beløpsestimater.
2. Forsvarlighetsvurdering etter asl. § 3-4 — forventet EK i hvert selskap basert på virkelige verdier.
3. Revisor-vurdering etter asl. § 14-4 jf. § 2-6.
4. Juridisk vurdering fra selskapsadvokat.
5. Konkret vurdering av tvangsmulkt-plassering.
6. Konkret vurdering av Intrum-saken (dokumentert stabilisert før vedtak).
7. **Styreforsikring (D&O)** anbefales tegnet før fisjonsvedtak. Premie ca. 15–40 TNOK/år.

### 2.3 Strafferettslig grense — strl. kap. 31

Agent 1 har identifisert fire handlinger som ville flytte fisjonen mot kreditorsvik:

- Dumpet verdi hos fortsettende KWE etter konkursfare er påvist.
- Ekstraordinær betaling til nærstående (konsernlån) i 3-mnd-vinduet før fisjonsvedtak.
- Sen ettergivelse/konvertering av konsernlån **etter** TBRT har reist krav.
- «Tom skalk»-fortsettende uten reell driftsevne.

Planlagt fisjon ligger innenfor lovlig side forutsatt: Intrum stabilisert, konsernlån restrukturert parallelt, forretningsmessig begrunnelse dokumentert, kreditorvarsel kjørt korrekt.

### 2.4 Dokumentavgift

Fritaket for selskapsrettslige omorganiseringer gjelder både Fjordgata 30 og Grønnegata 10. Dokumentavgift ved tinglysing: 0 kr, forutsatt korrekt påføring av kontinuitet. Skjult risiko hvis dokumentasjonen svikter: 2,5 % av markedsverdi (potensielt 625 000–1 250 000 kr).

---

## 3. Praktisk gjennomføringsplan

### 3.1 Oppdatert tidslinje (uke-for-uke)

Antakelse: Konkursvarsel stabilisert innen uke 1 (27.10.2026). Fisjonsstikkdag 01.01.2027. Fisjon gjennomført ca. 15.03.2027.

| Uke | Dato (ca.) | Milepæl | Kritisk? |
|---|---|---|---|
| 42 | 12.–19.10.2026 | Pågående: Intrum-anmodning TBRT, bestridelse Intrum, Namsfogden-anmodning. Bestill grunnbokutskrift. Bestill saldobalanse 30.09.2026 fra regnskapsfører | ✓ |
| 43 | 20.–26.10.2026 | TBRT-svar/ikke-svar på Intrum-anmodning. Begynn utvelgelse av advokat og revisor | ✓ |
| 44 | 27.10.–02.11.2026 | **Konkursvarsel-fristen utløper 27.10.** Må være håndtert. Engasjer selskapsadvokat og revisor. Første advokat-møte (fisjonsstruktur, aksjonæravtale, konsernlån-restrukturering) | ✓ |
| 45–47 | 03.–23.11.2026 | Utarbeidelse av fisjonsplan. Åpningsbalanser. Revisorerklæringer forberedes. DNB-dialog (bekreftelsesbrev om debitorbytte Grønnegata). Enova OM-samtykke søkes | — |
| 48 | 24.–30.11.2026 | Revisorerklæringer ferdigstilles. Varselbrev til KMF, BYA, UNI, Enova KL. **Konsernlån-restrukturering** gjennomføres parallelt (konvertering til EK eller fordeling). Styreforsikring (D&O) tegnes | — |
| 49 | 01.–07.12.2026 | Styrevedtak og GF-vedtak i KWE og KodeWorks AS. Melding til Brreg. Kreditorvarsel kunngjøres | ✓ |
| 50 | 08.12.2026 – uke 5 | **6 ukers kreditorfrist løper** (jul påvirker — forvent 7–8 uker reell tid) | ✓ |
| 6–8 | 02.–22.02.2027 | Samordnet registermelding til Brreg. Brreg-behandlingstid 2–4 uker | ✓ |
| 9–11 | 23.02.–15.03.2027 | Brreg registrerer fisjonen. Tinglysing. Grønnegata 10 AS MVA-registreres samtidig med Brreg (justeringsavtale mval. § 9-3). Byggesak-overføring. Tilskuddsoverføring | ✓ |
| 12–14 | 16.03.–05.04.2027 (Agent 2) eller 16.04.–01.05.2027 (Agent 1) | **Emisjon av nye aksjer** i FG30 AS mot tingsinnskudd. Tidsmessig avstand omstridt (se seksjon 4.3) | — |

**Realistisk sluttdato:** fisjon ca. 15. mars 2027; emisjon enten 1.–15. april (Agent 2) eller 1.–15. mai 2027 (Agent 1-anbefaling 6–8 uker). FG30 AS MVA-registreres Q2 2027 (før driftsstart).

### 3.2 Kostnadsestimat

| Post | Lavt | Sannsynlig | Høyt |
|---|---:|---:|---:|
| Selskapsadvokat (fisjon, Brreg, justering) | 80 000 | 150 000 | 250 000 |
| Advokat eiendomsoverføring (skjøter × 2) | 15 000 | 25 000 | 40 000 |
| Revisor (fisjonsplan, åpningsbalanser) | 40 000 | 70 000 | 120 000 |
| Revisor — tingsinnskudd-erklæring (ny) | 10 000 | 18 000 | 25 000 |
| MVA-spesialist (redusert fra v1) | 10 000 | 20 000 | 40 000 |
| Skatteadvokat — konsernlån-restrukturering (ny) | 10 000 | 20 000 | 40 000 |
| Regnskapsfører (ekstra) | 20 000 | 40 000 | 70 000 |
| Advokat emisjon + aksjonæravtale (ny) | 30 000 | 45 000 | 60 000 |
| Brreg (gjennomføring + nystiftelser) | 5 000 | 7 000 | 10 000 |
| Brreg (kapitalforhøyelse emisjon, ny) | 0 | 2 500 | 3 000 |
| Kunngjøring Brreg | 1 000 | 1 500 | 2 000 |
| Tinglysing skjøter × 2 | 1 300 | 1 300 | 1 300 |
| Dokumentavgift (fritak) | 0 | 0 | 0 |
| DNB bekreftelsesbrev + revidert lånedokument (redusert) | 2 000 | 5 000 | 10 000 |
| Styreforsikring D&O (ny, årlig premie) | 15 000 | 25 000 | 40 000 |
| Diverse buffer | 2 000 | 5 000 | 10 000 |
| **Sum** | **~241 000** | **~435 000** | **~721 000** |

Sentralt kostnadsintervall: **375 000–495 000 kr**. Må vektes mot MVA-fordelen (ca. 6,2 MNOK potensielt refusjon i byggefasen).

### 3.3 Praktiske fallgruver (fase 4-oppdatering)

Fra v1 beholdt (ti punkter), pluss ny i v2:

- **Fallgruve 11 (ny):** Konto 1172 Renovering FG30 bokført ekskl. MVA (fradrag tatt) — da må justeringsavtale lages også for FG30, og FG30 AS må MVA-registreres samtidig med Brreg. **Må verifiseres med regnskapsfører før fisjonsvedtak.**
- **Fallgruve 12 (ny):** Fortsettende KWE strukturelt insolvent uten konsernlåns-restrukturering → styreansvar og dekningslov § 5-9. Må løses i uke 48 parallelt med fisjonsvedtak.
- **Fallgruve 13 (ny):** Emisjon for tett opp mot fisjonsvedtak → serietransaksjon → kontinuitetsbrudd → realisasjonsskatt (1,5–5 MNOK). Minimum avstand 6–8 uker (Agent 1).

---

## 4. Håndtering av tvangsmulkt — konkretisert

### 4.1 Plassering (bekreftet Alt 1A)

| Krav | Plassering | Begrunnelse |
|---|---|---|
| Påløpt tvangsmulkt kr 184 000 (3 innkrevinger) | Fortsettende KWE | Beskytter partsstatus i DSB-/Sivilombud-saker |
| Tilbakevirkende innkreving (opptil kr 428 000 for bero-perioden) | Fortsettende KWE via eksplisitt klausul i fisjonsplanen | Agent 3 anbefaling; Agent 1 bekrefter at klausulen regulerer intern regress (ikke binder TBRT som tredjepart) |
| Pålegg om brannsikring (08.11.2024) | Fjordgata 30 AS (følger eiendommen) | Pålegg er eiendomsknyttet etter brann- og eksplosjonsvernloven § 37 |
| Fremtidig løpende tvangsmulkt (hvis bero oppheves 01.01.2027) | FG30 AS (nytt vedtak fra TBRT mot ny eier) | Pålegget følger eiendommen; tvangsmulktvedtaket må gjentas mot FG30 AS |

### 4.2 Dekning hos fortsettende KWE (fase 4-vurdering)

Fortsettende KWE blir strukturelt insolvent uten tiltak. Dekningsmekanismer (Agent 3 anbefaler kombinasjon):

**A — Konsernlån-restrukturering (må gjøres uansett).** To hovedalternativer:
- **Konvertering til egenkapital** (Agent 1 anbefaler, mest robust). KodeWorks AS konverterer hele 10,6 MNOK fordring til aksjekapital/overkurs i KWE. Krever styrevedtak i både KodeWorks AS og KWE. Etter konvertering er fortsettende KWE bokført solvent.
- **Proporsjonal fordeling** (Agent 3 og 4 anbefaler som alternativ). Konsernlånet fordeles 69,6 % Grønnegata 10 AS / 30,4 % Fjordgata 30 AS (Agent 3) eller 62 % fortsettende KWE / 24 % FG30 AS / 14 % Grønnegata (Agent 4-forslag). Krever KodeWorks AS-samtykke til debitorbytte.

**B — Bankinnskudd (705 655 kr) blir i fortsettende KWE.** Umiddelbar dekning for 184 000 kr + buffer.

**C — Morselskapsgaranti fra KodeWorks AS på 1 MNOK** (Agent 3 anbefaling). Dekker både påløpt (184 TNOK) og tilbakevirkende (428 TNOK) + buffer. Må:
- Være skriftlig, selvskyldner, første-påkrav.
- Beregne markedsmessig provisjon (1 % × 1 MNOK = 10 TNOK/år) for å nøytralisere skatterisikoen etter asl. § 3-9 og sktl. § 10-11.
- To varianter: (a) til fortsettende KWE som sikkerhet mot tredjeparter, (b) direkte til TBRT som begunstiget. Agent 1 anbefaler variant (a) — mer fleksibel.

**Kombinasjon A (konvertering) + B + C** gir en robust dekning: dekningsgrad 2,9× over kjent eksponering på 612 TNOK (184 + 428). Hovedsesjonens valg mellom konvertering vs. fordeling behandles i review_02.

### 4.3 Varslingsstrategi

**Nivå 1 (obligatorisk):** Brreg-kunngjøring av fisjonsplan utløser 6 ukers kreditorfrist (asl. § 14-7). TBRT får kreditorvarsel uansett.

**Nivå 2 (anbefalt, timing utsatt per brukerinput Q2):** Direkte brev til TBRT, DSB, Sivilombudet 2–4 uker før Brreg-registrering, når fisjonsplanen er ferdig utkastet. Signal for å ta beslutningen: når DSB-sakens status er kjent, når Sivilombudet har meldt om videre behandling, når Intrum-saken er stabilisert.

**Nivå 3 (valgfritt):** Direkte underretning til Intrum, Namsfogden, DNB, tilskuddsgivere avhengig av strategisk vurdering.

---

## 5. Finans, bank, pant og tilskudd — fase 4-oppdatering

### 5.1 Bank og pant — avklart

- **DNB** er bank for Grønnegata 10 (lån 15,2 MNOK + renter 831 TNOK). Brukeren har bekreftet med DNB at lånet flyttes til Grønnegata 10 AS. Praktisk: skriftlig samtykke, revidert lånedokument, nytt pantedokument tinglyst med Grønnegata 10 AS som pantsetter.
- **Fjordgata 30:** ingen pant. Går fritt til FG30 AS.
- Framtidig byggelån til FG30 AS: separat spor, ikke forutsetning for fisjon.

### 5.2 Åpningsbalanser (Agent 4-utkast)

**Fortsettende KodeWorks Eiendom AS:**
- Eiendeler: bankinnskudd 150 000 + aksjer FG30/Grønnegata 60 000 = **ca. 210 000**
- Gjeld (med konvertering): 0 konsernlån + 184 000 (tvangsmulkt, bestridt — ikke avsatt bokført) + 110 000 andel andre poster = **ca. 110 000 bokført** (184 TNOK som noteopplysning)
- Egenkapital bokført: **ca. 100 000 bokført + 10,6 MNOK fra konvertering = ca. 10,7 MNOK EK** (hvis konvertering gjennomføres)
- Egenkapital med fordeling (ikke konvertering): **sterkt negativ (ca. –10,76 MNOK)** — ikke levedyktig.

**Fjordgata 30 AS:**
- Eiendeler: bygg 7,33 + renovering 0,82 + evt. Enova KL-fordring 0,32 + bank 300–400 + pinball 0,02 = **ca. 8,47–8,89 MNOK**
- Gjeld: andel konsernlån 2,5 (hvis fordeling) eller 0 (hvis konvertering) + leverandørgjeld 150–350 TNOK
- Egenkapital: **5,9–6,2 MNOK bokført** (med fordeling) eller **ca. 8,2 MNOK** (med konvertering)

**Grønnegata 10 AS:**
- Eiendeler: bygg 16,82 + teknisk 1,33 + inventar 0,53 – avskrivninger 0,65 + depositum 0,02 + kundefordringer netto –0,003 + bank 155–256 = **ca. 18,2 MNOK**
- Gjeld: DNB 15,23 + renter 0,83 + leverandørgjeld 88–338 TNOK + forskudd 101 + konsernlån-andel 1,5 (hvis fordeling) + diverse 100 TNOK = **ca. 17,9–18,1 MNOK**
- Egenkapital: **ca. 99 000 – 2,4 MNOK** avhengig av fordeling og virkelig verdi-vurdering

### 5.3 Tilsagnsbrev — status uendret fra fase 1

| Tilskudd | Beløp | Overføring til FG30 AS |
|---|---:|---|
| KMF | 750 000 | Skriftlig anmodning etter fisjon. Lav risiko. |
| BYA | 500 000 | Skriftlig anmodning etter fisjon. MVA-klausul informasjonsplikt. |
| UNI | 100 000 | Melding via portal/forretningsfører. |
| Enova KL (26/2548) | 400 000 | 80 % (ca. 320 000) kan anmodes utbetalt **nå** fra KWE før fisjon (Agent 4 anbefaler). Sluttrapport frist 25.12.2026. |
| Enova OM (26/2555) | 500 000 | Forutgående samtykke før fisjon (styrende i tidsplan). |

### 5.4 Framførbart underskudd

Status: 2 462 256 kr fremført fra 2024 (Skatteetatens varsel 13.07.2026). Forventet vekst til ca. 3,0–3,5 MNOK ved utgangen av 2026.

**Fordeling:** Agent 1 og Agent 4 enige: plasser i FG30 AS. Begrunnelse: FG30 AS vil ha skattepliktige overskudd fra lagringsdrift 2027–2028. Skattebesparelse ca. 541 TNOK ved 22 % selskapsskatt. Avskjæringsrisiko sktl. § 14-90 lav gitt reell forretningsmessig begrunnelse (MVA, bank, risikoseparasjon, nye aksjonærer).

---

## 6. MVA-strategien — konkretisert

### 6.1 Rammer bekreftet

Skatteetatens veiledende svar 11.09.2026:
- Aktiv lagringstjeneste (valet storage, 70 % av enhetene) = avgiftspliktig § 3-1. Full fradragsrett.
- Selvbetjent bodutleie B2B (30 %) = unntatt § 3-11, frivillig registrering § 2-3 mulig for næringsleietakere.
- BFU unødvendig.

### 6.2 Fradragsnøkkel (Agent 4-estimat)

Byggebudsjett 30 MNOK ekskl. MVA → inngående MVA 7,5 MNOK. Fradragsareal:
- Valet storage: 100 % fradrag → 706 kvm
- B2B-boder (50 % MVA-registrerte leietakere antatt): 151 kvm
- Kontor (frivillig § 2-3): 193 kvm
- Krypkjeller (halv fradrag): 76 kvm
- **Totalt: 1 126 av 1 353 kvm = 83 % → ca. 6,2 MNOK estimert refusjon**

### 6.3 Tidsrekkefølge (Agent 1 avklart med verbatim mval. kap. 9)

**Grønnegata 10 AS må MVA-registreres samtidig med Brreg-registrering** (ikke uke 10 som Agent 2 skrev):
- Grønnegata-eiendom er kapitalvare etter mval. § 9-1 (2) b (fradragsført MVA på oppussing siden 2020).
- Overføring til Grønnegata 10 AS utløser samlet justering etter § 9-2 (3) hvis mottaker ikke er MVA-registrert ved overføring.
- **Justeringsavtale etter mval. § 9-3 (1)** signeres samme dag som Brreg-registrering, med Grønnegata 10 AS som registrert mottaker som overtar justeringsforpliktelsen.

**Fjordgata 30 AS registreres ikke ved fisjon** (ikke driftsklar):
- Avventer MVA-registrering til Q2 2027 (før driftsstart september–november 2027).
- Tilbakegående avgiftsoppgjør etter mval. § 8-6 (**3 års frist**, ikke 6 mnd som v1 hadde) løfter inngående MVA på byggefase-kostnader påløpt fra ca. 25.10.2024.
- Forutsetter at konto 1172 Renovering FG30 **ikke er fradragsført** (bokført inkl. MVA). Hvis fradragsført: FG30 AS må registreres samtidig med Brreg og justeringsavtale lages også for FG30 → mer kompleks timing.

### 6.4 Konsekvens hvis justeringsavtale Grønnegata ikke på plass

Samlet justering utløses i KWE etter § 9-5 (2). Beregnet eksponering: 4/10 av fradragsført MVA på 5,5 MNOK oppussing = ca. **550 TNOK tilbakebetaling** til Skatteetaten. Kontantutlegg som gjør fortsettende KWE enda mer insolvent. **Må unngås.**

---

## 7. Nye aksjonærer — Brandsegg og Lagmannssveen

### 7.1 Hovedanbefaling

**Fisjon først, emisjon etter.** Begrunnelse: skattemessig kontinuitet (sktl. § 11-7) krever samme aksjonærstruktur før og etter fisjon. KodeWorks AS må være eneeier i alle tre selskaper etter fisjonen; nye aksjonærer bryter kontinuiteten og utløser realisasjonsskatt (1,5–5 MNOK).

### 7.2 Tingsinnskuddets form

**Lovlige:** Kontanter, fysiske eiendeler, immaterielle rettigheter (patent, varemerke, kundelister), fordringer (gjeldskonvertering).

**Ikke lovlig (asl. § 2-7):** Arbeid eller arbeidsplikt. Ikke anerkjent som gyldig tingsinnskudd.

**Alternativer hvis egentlig arbeidsinnskudd:**
1. Opsjonsavtale — ansattopsjoner på markedsvilkår.
2. **Konsulentkontrakt + senere gjeldskonvertering** (Agent 1 anbefaler): Brandsegg/Lagmannssveen fakturerer timer; fordring konverteres til aksjer senere. Ordinær lønnsbeskatning på fakturerte timer.
3. «Founder stock» — aksjer kjøpes kontant til lav emisjonskurs. Fordelsbeskatningsrisiko hvis under markedsverdi.

**Åpent spørsmål til bruker:** Hva består Brandsegg/Lagmannssveens tingsinnskudd faktisk av?

### 7.3 Tidsmessig avstand fisjon → emisjon

**Uenighet mellom agenter:**
- Agent 2: 2–4 uker.
- Agent 1: **minst 6–8 uker**, med 3 uker som absolutt minimum.

Agent 1 argumenterer med serietransaksjonsrisiko (sktl. § 13-2) hvis fisjon + emisjon framstår som én sammenhengende disposisjon. Hovedsesjonen leaner mot Agent 1s linje (mer forsiktig, lite ekstra kostnad for sikkerhet).

**Formelle krav uansett avstand:**
- Fisjonsvedtaket inneholder ingen henvisning til planlagt emisjon.
- Emisjonsbeslutningen fattes etter Brreg-registrering, dokumentert som selvstendig forretningsmessig vurdering.
- Aksjonæravtale signeres etter fisjonsregistreringen, ikke før.

### 7.4 Omstøtelsesrisiko

Hvis emisjonen skjer innenfor dekningslov-vinduet, kan kreditor hevde at tingsinnskuddet er over-verdsatt og at FG30 AS er utvannet uten reell tilførsel. Mitigering: markedsmessig verdsettelse + revisorerklæring + dokumentert driftsmessig behov + avstand fra fisjon.

---

## 8. Konsernlån-restrukturering (10,6 MNOK)

Dette er den enkeltvariabelen som dominerer alle åpningsbalanser. Alternativene fra fase 4:

### 8.1 Alternativ 1 — Konvertering til egenkapital (Agent 1 anbefaler)

KodeWorks AS konverterer hele fordringen til aksjekapital/overkurs i KWE **før eller samtidig med** fisjonsvedtak.

**Juridiske konsekvenser:**
- I KWE: tingsinnskudd via fordringsavkall. Krever styre- og GF-vedtak. Revisorerklæring (asl. § 2-6).
- I KodeWorks AS: avhending av fordring, mottak av aksjer med samme verdi. Normalt ingen skatt.
- Omstøtelsesrisiko: lav. Ikke gave (verdi mottatt).
- Fortsettende KWE blir **bokført solvent** umiddelbart etter konvertering.
- Reduserer rentekostnad ca. 970 TNOK/år.

**Styrke:** Mest robust mot omstøtelse og styreansvar. Elimineringsfaktor på dekningslov § 5-9-angrepet.

### 8.2 Alternativ 2 — Proporsjonal fordeling (Agent 3/4 forslag)

Konsernlånet fordeles proporsjonalt mellom selskapene:
- Agent 3: 69,6 % Grønnegata 10 AS (7,38 MNOK), 30,4 % FG30 AS (3,22 MNOK), 0 fortsettende KWE.
- Agent 4: 62 % fortsettende KWE (6,6 MNOK), 24 % FG30 AS (2,5 MNOK), 14 % Grønnegata 10 AS (1,5 MNOK).

**Krav:** KodeWorks AS må samtykke til debitorbytte (konsernintern, formalia).

**Juridisk konsekvens:** Fordelt gjeld følger bokførte aktiva. Omstøtelsesrisiko lav hvis proporsjonal. Krever at renten reforhandles til markedsrente (ca. 6 %) for å nøytralisere internprising-risiko etter sktl. § 13-1.

### 8.3 Alternativ 3 — Ettergivelse (Agent 1 fraråder)

KodeWorks AS ettergir hele eller deler. Skattemessig problematisk: ikke fradrag i KodeWorks AS (nærstående), skattepliktig inntekt i KWE (med mulig motregning mot framførbart underskudd 2,46 MNOK). Signal om insolvens overfor bank og tilskuddsgivere.

### 8.4 Hovedsesjonens vurdering

Alternativ 1 (konvertering) er juridisk mest robust og operativt enkleste. Agent 2s plan uke 48 ikke dekker eksplisitt konvertering som eget trinn — må legges inn. Agent 4s åpningsbalanse-tabeller må revideres hvis konvertering velges (konsernlån forsvinner som gjeld; EK øker tilsvarende).

---

## 9. Djevelens advokat — rangert liste (fase 7-input)

Agent 1 (seks angrep) + Agent 3 (fem angrep) overlapper vesentlig. Konsolidert ni angrepspunkter rangert etter kombinert styrke:

| # | Angrep | Hjemmel | Styrke | Mitigering |
|---|---|---|---|---|
| 1 | «Fortsettende KWE er en tom skalk» — fisjonen gjør selskapet strukturelt insolvent | Dekningsloven § 5-9 | 5/5 | Konsernlån-konvertering + morselskapsgaranti 1 MNOK + bankinnskudd. Dekningsgrad 2,9×. |
| 2 | Styreansvar — fisjonsvedtak under illikviditetsformodning | asl. § 17-1 | 4/5 (personlig) | Intrum stabilisert + dokumentert styreprotokoll + D&O-forsikring + alle 7 dokumentasjonskrav |
| 3 | Bero-brudd — fisjonen svekker realismen i prosjektet | TBRTs bero-brev 25.06.2026 | 4/5 | Dokumentert byggeframdrift (kontrakter, prosjektering). MVA-strategi som forutsetning for brannsikringsfinansiering |
| 4 | MVA-justeringsavtale Grønnegata mangler eller er feil | mval. § 9-2, § 9-3, § 9-5 | 4/5 | Justeringsavtale signert samme dag som Brreg-registrering + Grønnegata 10 AS MVA-registrert samtidig |
| 5 | Omstøtelse av fisjon — Intrum-saken innenfor omstøtelsesvinduet | Dekningsloven kap. 5 (§ 5-9) | 4/3 | TBRT instruerer Intrum-stans før fisjonsvedtak + dokumentert dekningsgrad |
| 6 | Kontinuitetsbrudd — fisjon→emisjon som serietransaksjon | sktl. § 11-7, § 13-2 | 3/5 | Minst 6–8 uker avstand + ingen henvisning i fisjonsplanen + separat dokumentasjon av emisjonen |
| 7 | DSB-/Sivilombud-opplysningssvikt | — | 2/5 | Statusbrev 08.10.2026 har varslet; proaktiv underretning etter fisjonsplan er ferdig |
| 8 | Konto 1172 fradragsført — justeringsavtale FG30 utløses | mval. § 9-2 (3), § 9-7 | 3/4 (hvis fradragsført) | Verifiser med regnskapsfører. Hvis fradragsført: lag justeringsavtale FG30 og MVA-reg FG30 AS samtidig |
| 9 | Strafferettslig kreditorsvik | strl. § 401, § 402 | 1/5 som sak, 3/5 som intimidering | Alle 6 forsvarsargumenter oppfylt (markedspris, solidaransvar, kreditorvarsel, forretningsmessig begrunnelse, dokumentert styreprotokoll) |

**Felles tema:** Nøkkelmitigering for alle ni angrepspunkter er konsernlån-konvertering + Intrum-stabilisering + dokumentert styreprotokoll + 6–8 ukers avstand emisjon + MVA-dokumentasjon korrekt timet.

---

## 10. Timing-scenarier

### 10.1 Scenario A modifisert (anbefalt)

Fisjonsvedtak uke 49 (desember 2026) etter at:
- Konkursvarselet er stabilisert via TBRT-instruert Intrum-stans.
- Konsernlån-restrukturering er på plass (konvertering eller fordeling).
- Enova OM-samtykke er innhentet.
- Styreforsikring (D&O) er tegnet.
- Varselbrev til TBRT/DSB/Sivilombudet er sendt 2–4 uker før Brreg-registrering.

Fisjon registrert ca. 15.03.2027. Emisjon ca. 1.–15. mai 2027 (etter Agent 1-anbefaling om 6–8 uker avstand).

### 10.2 Scenario B (backup)

Hvis Intrum-saken ikke stabiliseres (TBRT nekter å instruere stans), utsett fisjonsvedtak til etter DSB-svar. Realistisk tidspunkt: vinter/vår 2027.

- Aksepter MVA-tap for forsinkelsen (hver måned uten MVA-register = tap av fradragsrett for løpende byggekostnader).
- Risiko: Byggesaken (BYGG-26/81377) kan være i IG-fase når fisjonen vedtas — tiltakshaver-endring midt i kritisk periode.
- Byggelån kan være nær lukking — bank blir utålmodig.

### 10.3 Scenario C (siste utvei)

Vent til bero-slutt 01.01.2027 og eventuell ny mulktbegjæring fra TBRT. Dyrest både i mulkt og MVA. Brukerens kategoriske Q4-svar («MVA er alfa og omega») gjør denne mindre attraktiv.

### 10.4 Hovedanbefaling

**Scenario A modifisert**, gitt grønt lys fra Intrum-sporet (TBRT instruerer stans). Hvis gult eller rødt lys fra Intrum-sporet: Scenario B.

---

## 11. Intrum-beslutningstre (Agent 3-detalj)

Scenarier for uke 42–44:

| Scenario | Hva skjer | Handling | Lys |
|---|---|---|---|
| (a) | TBRT svarer ikke innen 15.10.2026 | Purring 16.10 + begynn planlegge betaling | Gult |
| (b) | TBRT svarer nei | Klage på TBRT + rettslig stans begjæres + reserveplan betaling | Rødt |
| (c) | TBRT instruerer Intrum om stans | Bekreftelse innhentes. Fisjonsarbeid fortsetter | Grønt |
| (d) | Intrum nekter stans | TBRT direkte stansvedtak + midlertidig forføyning + reserveplan | Rødt |
| (e) | Namsfogden gjennomfører utlegg innen 27.10 | Delta med dokumentasjon + midlertidig forføyning | Rødt |

**Grønt lys (c):** fisjonsarbeid fortsetter ryddig. **Gult (a):** planlegg i parallell, men ikke registrer. **Rødt (b, d, e):** pause fisjonsarbeid, prioriter stabilisering.

---

## 12. Åpne spørsmål — oppsummert

Full liste i `review_02.md`. Hovedtemaer:

- Konto 1172 inkl./ekskl. MVA (regnskapsfører).
- Historisk fradragsført MVA Grønnegata (regnskapsfører).
- Tingsinnskuddets natur fra Brandsegg/Lagmannssveen (bruker).
- Konvertering vs. fordeling av konsernlån (bruker/skatteadvokat).
- Fisjon-emisjon-avstand (hovedsesjonens anbefaling 6–8 uker, bruker beslutter).
- Styreforsikring D&O (finnes? Pris?).
- KodeWorks AS' balanse — soliditet for 1 MNOK garanti.
- Timing av varselbrev til TBRT (brukerens Q2 utsatt).

---

*Merge ferdigstilt 2026-10-12. Alle paragrafhenvisninger utenom mval. kap. 9 markert [verifiseres fase 10]. Hovedsesjonen leverer `review_02.md` som følgedokument.*
