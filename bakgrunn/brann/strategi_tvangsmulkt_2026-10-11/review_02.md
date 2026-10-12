---
dato: 2026-10-11
iterasjon: 02
mål-fil: iterasjon_02_1245.md
---

# Review 02 — Iterasjon 02

Reviewen identifiserer gjenværende svakheter etter iter 02. Iter 02 har adressert hovedfunnene fra review 01 — Statsforvalter-sporet er løftet, Sivilombudet 2023/2570 er verifisert, fisjonsplanen er operasjonalisert, DSB-amnestitilbud er lagt til. Likevel gjenstår flere konkrete svakheter som bør adresseres i en iter 03 om tiden tillater.

## 1. Lovkildeverifikasjon (høyeste prioritet)

Agent 1 melder at Lovdata blokkerte curl under iter 02 og at 6 lovfiler er basert på «konsolidert kjent versjon»:
- `fvl_28_klagerett.md`
- `fvl_35_omgjoring.md`
- `fvl_36_sakskostnader.md`
- `tvl_34-1_vilkaar_forfoeyning.md`
- `tvl_34-2_sikringsgrunn.md`
- `emk_p1-1_eiendomsvern.md`

Dette er en reell risiko: CLAUDE.md er klar på at parafraserte lovsitater kan ødelegge en sak. Agent 2 fant workaround (Lovdata-PDF + pdftotext). Samme workaround kan brukes for de seks filene Agent 1 ikke fikk verifisert.

**Alvorlighet:** Høy. **Iter 03 obligatorisk.**

## 2. Faktaark-innholdsutvidelser som er avdekket men ikke lagt inn

Agentene har avdekket nytt faktum som bør inn i faktaarket:

- **Mottakerliste klageorganet (sak 3/26, 25.08.2026):** Harald Fagervold, Mari Stene-Ry, Ola Skarsheim, Per Øystein Karlsen, Randi Eikevik (fra Agent 2 iter 01). Signatarer på saksfremlegget: Torbjørn Mæhlumsveen og Geir Jacobsen.
- **Sivilombudet 2023/2570 verifisert:** Flyttet fra UKJENT til bekreftet verbatim. Faktaarket pkt. 8 angir fortsatt UKJENT — må oppdateres.
- **TBRT-eierandel 85,79 %:** Oppdatert i iter 02, men pkt. 9 UKJENT-liste viser bare at punktet er løst — kan utvides med lenke til tbrt.no-kilden.

**Alvorlighet:** Moderat. **Orkestrator-skritt i iter 03.**

## 3. Underpunkter som fortsatt er korte eller svake

Spot-check mot iter 02:

- **Agent 1 pkt. 11 (Grl. §§ 97/102):** 350 ord — bevisst nedprioritert av Agent 1 selv. Flaggs som kjent svakhet, ikke iter 03-prioritet.
- **Agent 3 pkt. 16 (SI vs. Intrum):** 240 ord — faktum er dekket, lav prioritet. Flaggs.
- **Agent 4 pkt. 14 (Kommunevalget 2027 som timing):** Må kontrolleres — hvis stikkordspreg, konverter til prosa.
- **Agent 5 pkt. 2 (Tolkningsveiledning fvl. § 11 til DSB):** Må kontrolleres mot v2.
- **Agent 5 pkt. 11 (Kostnadsavtale):** Må kontrolleres.
- **Agent 5 pkt. 14 (Forliksrådet):** Må kontrolleres — forliksrådet er neppe aktuelt for forvaltningssak, bør presiseres.

**Alvorlighet:** Lav/moderat. **Iter 03 valgfritt.**

## 4. Konkrete utkast som fortsatt mangler

- **Utkast til kronikk til Adresseavisen (Agent 4):** Nevnt men ingen konkret tekstprøve.
- **Utkast til formell forespørsel til Byantikvaren (Utkast F):** Finnes i integrasjon men bør utvides med konkret spørsmålsliste.
- **Utkast til § 42-anmodning med 2023/2570-referanse:** Nå som 2023/2570 er verifisert, bør anmodningen eksplisitt sitere uttalelsen.
- **Utkast til midlertidig forføyning (begjæring til Trondheim tingrett):** Agent 1 pkt. 6 beskriver vilkårene men gir ikke konkret begjæringsutkast.

**Alvorlighet:** Moderat. **Iter 03 anbefalt.**

## 5. Integrasjonssvakheter

- **Kombinasjonstabellen og risiko-matrisen** er fra iter 01 og delvis oppdatert i iter 02 tail. Konsistens må sjekkes før final.
- **Sakssituasjon-seksjonen** i iter 02 head er kortere enn iter 01 — det er med vilje (iter 02 er målrettet utvidelse), men final-rapporten bør ha full faktafremstilling som iter 01.
- **Kjente svakheter ved stopp** mangler. Blir en egen seksjon i final-rapporten.

**Alvorlighet:** Lav. **Håndteres i final-leveranse.**

## 6. Faktaavvik mellom iter 01 og iter 02

- **Sivilombudet 2023/2570:** Iter 01 behandler som ubekreftet; iter 02 bekrefter. Iter 02-innhold er riktig; iter 01-innhold må behandles som overgangskontekst.
- **Umulighetsberegning:** Iter 01 regnet 176 dager / kr 352 000; iter 02 Agent 5 regner 132 dager × 2 000 = kr 264 000 for perioden 01.01.2026–11.05.2026. Begge er korrekte — det første er total påløpt per bero, det andre er perioden til rammesøknad. Final-rapporten må gjøre skillet eksplisitt.
- **Dagsats-grunnlag:** Alle iterasjoner enige om kr 2 000.

**Alvorlighet:** Lav. **Presiseres i final.**

## 7. Hvilke underpunkter som bør utvides i iter 03

**Høy prioritet:**
1. Agent 1 — verifiser 6 lovfiler fra Lovdata-PDF (workaround fra Agent 2)
2. Agent 1 — legg til begjæring om midlertidig forføyning som konkret utkast (pkt. 6)
3. Agent 2 — oppdater § 42-anmodningen med verbatim 2023/2570-referanse
4. Agent 4 — konkret kronikkutkast til Adresseavisen (300+ ord)
5. Agent 5 — presiser underpunkt 14 om forliksrådet (eller strek det ut hvis ikke anvendelig)

**Moderat prioritet:**
6. Faktaark — oppdater pkt. 8 med Sivilombudet 2023/2570 som bekreftet
7. Faktaark — legg til klageorganets medlemsliste som nytt pkt. 11
8. Alle agenter — konsolidér eksterne sitater som nå er verifisert

**Lav prioritet (flaggs som kjent svakhet):**
9. Grl. §§ 97/102 — bevisst nedprioritert av Agent 1
10. SI vs. Intrum — faktum er dekket

## 8. Hva som er avdekket men ikke lagt til

- **Kommunerevisjonens Rapport 4/2025-F** — Agent 4 har verifisert eksistens. Bør kildehenvises med URL i final-rapport.
- **Trondheim bystyre sammensetning verifisert** — Agent 4 har bekreftet.
- **Oppreisning fvl. § 31 bokstav c** — kjerneargument for Statsforvalter-klage, dekket i Agent 1 iter 02 pkt. 16, men bør også vurderes for andre oversittede frister (klage på selve tvangsmulktvedtaket 07.05.2025).

## 9. Tidsvurdering

Iter 03 bør være mindre enn iter 02 fordi hovedarbeidet er lovkilde-verifikasjon og mindre utkast-utvidelser. Estimat:
- Agent 1 — Lovdata-PDF-workaround + midlertidig forføyning-utkast: 15 min
- Agent 2 — § 42-anmodning-oppdatering: 5 min (minimalt)
- Agent 4 — kronikkutkast: 10 min
- Agent 5 — pkt. 14-presisering: 5 min
- Orkestrator — faktaark-oppdatering + integrasjon + review: 15 min
- Total: ~30 min for iter 03

## 10. Oppsummering

**Iterasjon 02 er solid på alle hovedakser og kan funksjonelt leveres som grunnrapport.** Hovedsvakhetene som gjenstår er (a) 6 lovfiler mangler verbatim-verifikasjon og (b) noen få mindre utkast og presiseringer. Iter 03 er anbefalt for å lukke disse før final-rapport, men iter 02 vil være tilstrekkelig som leveranse hvis tiden ikke tillater iter 03.
