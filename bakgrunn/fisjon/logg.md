# Logg — Fisjon-analyse (iterativ)

Kort tidslogg og modellvalg per agent-kjøring.

---

## Fase 1 — Første analyse-runde (parallelt)

- **Start:** 2026-10-12
- Alle fire kjørt parallelt uten `isolation: worktree`
- Agent 1 (Fisjonsjurist) — `general-purpose` — 80 300 tokens, 10 tool_uses, 506 s. Fil: `agent_01_fisjonsjurist_v1.md` (47 558 bytes).
- Agent 2 (Prosjektleder) — `general-purpose` — 77 090 tokens, 15 tool_uses, 413 s. Fil: `agent_02_prosjektleder_v1.md` (37 106 bytes).
- Agent 3 (Tvangsmulkt-strateg) — `general-purpose` — 92 541 tokens, 11 tool_uses, 379 s. Fil: `agent_03_tvangsmulkt_v1.md` (36 645 bytes).
- Agent 4 (Finans- og tilskuddsanalyst) — `general-purpose` — 100 287 tokens, 24 tool_uses, 407 s. Fil: `agent_04_finans_tilskudd_v1.md` (36 007 bytes).

**Worktree-sjekk etter fase 1:** `.claude/worktrees/` finnes ikke. Ingen `agent-*`-mapper å rydde.

## Fase 2 — Hovedsesjonens merge og review

- **Levert:** 2026-10-12
- `iterasjon_01_merged.md` — tematisk syntese organisert i 9 seksjoner (sammendrag, juridisk prosedyre, praktisk plan, tvangsmulkt-håndtering, finans/bank/tilskudd, varslingsstrategi, dekningslov/omstøtelse, timing-scenarier, åpne spørsmål).
- `review_01.md` — motsigelser, spenninger, hull og 13 nye spørsmål til bruker. Særlig flagget: (a) Grønnegata-dilemmaet, (b) varsling av TBRT (direkte motsigelse Agent 1 vs. Agent 3), (c) MVA-justeringsavtale, (d) pantesituasjon og bokførte verdier.
- **Stopp i tråd med T172-instruks.** Venter på brukerens innspill før fase 4 starter.

## Brukerinput etter fase 2 (2026-10-12)

- Brukerens svar på 13 Q-er dokumentert i `bruker_input_01.md`.
- Nytt faktagrunnlag identifisert: MVA-vedtak Skatteetaten 11.09.2026 (BFU droppet), regnskapstall 08.10.2026, DNB-lån på Grønnegata (ikke FG30), bokførte verdier for alle poster.
- Nytt tema: nye aksjonærer (Brandsegg + Lagmannssveen) i FG30 AS med tingsinnskudd.
- Nedlastingsbeslutning: mval. kap. 9 (justeringsregelverket) lastes ned verbatim fra Lovdata — unntak fra fase 10-regelen.

## Fase 4 — Målrettet andre iterasjon (parallelt)

- **Start:** 2026-10-12 ca. kl. 14:30
- Alle fire agenter kjørt parallelt uten `isolation: worktree`.
- **Agent 1 (Fisjonsjurist) — første forsøk:** krasjet etter 12 min / 26 tool_uses med `API Error: socket connection closed`. Mval. kap. 9 ble lastet ned til `bakgrunn/lovverk/mval_kap9_justering_av_inngaaende_merverdiavgift.md` (10 267 bytes) før krasjet, men v2-fil ble ikke skrevet.
- **Agent 1 (restart) — fullførte v2:** 196 349 tokens, 14 tool_uses, 622 s. Fil: `agent_01_fisjonsjurist_v2.md` (60 013 bytes).
- **Agent 2 — Prosjektleder v2:** 109 740 tokens, 7 tool_uses, 313 s. Fil: `agent_02_prosjektleder_v2.md` (32 184 bytes).
- **Agent 3 — Tvangsmulkt-strateg v2:** 105 268 tokens, 5 tool_uses, 426 s. Fil: `agent_03_tvangsmulkt_v2.md` (43 677 bytes).
- **Agent 4 — Finans- og tilskuddsanalyst v2:** 145 443 tokens, 13 tool_uses, 507 s. Fil: `agent_04_finans_tilskudd_v2.md` (49 446 bytes).

**Worktree-sjekk etter fase 4:** `.claude/worktrees/` finnes ikke. Ingen rester.

**Nøkkeldivergenser som fase 5 må løse:**
- 2–4 uker (Agent 2) vs. 6–8 uker (Agent 1) mellom fisjon og emisjon.
- Konsernlån: konvertering til EK (Agent 1) vs. fordeling mellom selskaper (Agent 3/4).
- Grønnegata 10 AS MVA-registrerings-timing.
- Tilbakegående avgiftsoppgjør mval. § 8-6: Agent 4 flagger 3 års frist (Agent 1 nevner også 3 år etter mval.-nedlasting); v1 refererte feilaktig til «6 mnd».

## Fase 5 — Hovedsesjonens merge 2 og review 2

- **Levert:** 2026-10-12
- `iterasjon_02_merged.md` — tematisk syntese i 12 seksjoner. Bygger på fase 4-leveransene og brukerinput. Konsolidert djevelens advokat-liste med 9 angrepspunkter rangert.
- `review_02.md` — motsigelser, spenninger, hull. 12 nye spørsmål til bruker (Q14–Q25). Tentative anbefalinger: konvertering, 6 uker avstand.
- **Avstemt divergens som krever bruker-beslutning før fase 7:** Q14 (konsernlån konvertering/fordeling), Q15 (avstand fisjon-emisjon 3 vs. 6–8 uker), Q18 (hva tingsinnskuddet består i).
- **Stopp i tråd med T172-instruks.** Venter på brukerens innspill før fase 7 (djevelens advokat) starter.

## Brukerinput 2 (2026-10-12)

- Dokumentert i `bruker_input_02.md`.
- Konsernlån KW→KWE bevares (ingen konvertering). Agent 1s hovedanbefaling forkastes.
- Tingsinnskudd fra Brandsegg/Lagmannssveen avklart (inventar/løsøre + immaterielle verdier).
- Revisor: Allrevisjon AS → Varder AS. Orkla Regnskap fortsatt regnskapsfører. **Ingen advokater — AI gjør hovedarbeidet.**
- **5. oktober-fristen fra Skatteetaten er passert med 7 dager.** Varder sier «noen dager/uker over er OK». Må inn ASAP. Tidslinjen forseres: fisjonsvedtak uke 44–46.
- **Ny struktur-mulighet (Alt C):** FG30 AS og GG10 AS som datterselskaper av KWE. Lånet KW→KWE forblir uendret.
- **T173 opprettet** for strukturvurdering (Alt A/B/C). Må kjøres før fase 7 slik at djevelens advokat jobber med riktig struktur.
- Nye åpne spørsmål Q26–Q29 om fisjonsstikkdag, Varder-engasjement, revisor-bytte-timing, T173-beslutning.

## T173 — Strukturvurdering

- **Levert:** 2026-10-12
- Agent 6 (Strukturanalytiker) — `general-purpose`, uten `isolation: worktree`. 125 611 tokens, 15 tool_uses, 499 s. Fil: `struktur_alternativer_T173.md` (46 972 bytes).
- Worktree-sjekk: `.claude/worktrees/` finnes ikke.
- **Hovedanbefaling: Alt C (mellomholding)** — FG30 AS og GG10 AS som datterselskaper av KWE. Primær mekanisme C1 (konserninternoverdragelse etter sktl. § 11-21). Fallback C2 (fisjon først, så aksjeinnskudd fra KodeWorks AS til KWE).
- **Alt B utelukket** på partsstatus-problemet alene (fire pågående saker får partsendring midt i prosess uten tilsvarende gevinst).
- **Alt A som nest-best** hvis Alt C ikke er gjennomførbart — krever morselskapsgaranti 1 MNOK fra KodeWorks AS + aksjonærinnskudd 1–2 MNOK i KWE for å løse dekningslov § 5-9-sårbarheten.
- **Nye åpne spørsmål til Varder:** sktl. § 11-21-vilkår (eierandel direkte vs. konsernmessig, bindingstid), kreditorbeskyttelsesregler ved § 11-21-overdragelse, framførbart underskudd-plassering ved C1, DNB-samtykke til KWE som mellomholding.

## Fase 6 — Tredje runde av agentene (Alt C C1)

- **Levert:** 2026-10-12
- Alle fire agenter kjørt parallelt uten `isolation: worktree`. Alt C mekanisme C1 var utgangspunktet.
- Agent 1 (Fisjonsjurist v3) — 154 273 tokens, 15 tool_uses, 689 s. Fil: `agent_01_fisjonsjurist_v3.md` (64 082 bytes).
- Agent 2 (Prosjektleder v3) — 145 966 tokens, 8 tool_uses, 394 s. Fil: `agent_02_prosjektleder_v3.md` (42 603 bytes).
- Agent 3 (Tvangsmulkt-strateg v3) — 126 025 tokens, 5 tool_uses, 443 s. Fil: `agent_03_tvangsmulkt_v3.md` (45 985 bytes).
- Agent 4 (Finans- og tilskuddsanalyst v3) — 148 962 tokens, 10 tool_uses, 497 s. Fil: `agent_04_finans_tilskudd_v3.md` (50 610 bytes).
- Worktree-sjekk: `.claude/worktrees/` finnes ikke.

**Kritisk nytt funn (Agent 1 v3):** Dokumentavgift-fritaket etter dokumentavgiftsloven § 7 jf. stortingsvedtaket henviser eksplisitt til sktl. §§ 11-2 til 11-5, 11-11 og 11-20 — **ikke § 11-21** [verifiseres fase 10 / Varder]. Potensiell eksponering ved C1: 850 TNOK – 1,3 MNOK (2,5 % av 34–52 MNOK samlet eiendomsverdi). Dette endrer mekanisme-avveiningen og **kan tippe anbefalingen mot C2** (fisjon + aksjeinnskudd) som bevarer dokumentavgift-fritak.

**Agent 1 v3 nedgraderinger av djevelens advokat-liste under Alt C:**
- D1 (dekningslov § 5-9 «tom skalk»): 5/5 → 2/5
- D2 (styreansvar): 4/5 → 2/5
- D5 (strafferett): 1/5 → nedgradert ytterligere
- D4 (MVA-justering Grønnegata): 4/5 uendret
- Ny D3 (§ 11-21-bindingstid brutt av Brandsegg/Lagmannssveen-emisjon): 3/5
- Ny: dokumentavgift-risiko ved C1 — potensielt den tyngste gjenværende risikoen

## Dokumentavgift-research (10 agenter parallelt, sonnet)

- **Levert:** 2026-10-12
- 10 forskningsagenter kjørt parallelt uten `isolation: worktree`. Ingen worktree-rester.
- Filer i `bakgrunn/fisjon/dokumentavgift_research/`:
  - `dok_01_lovtekst_stortingsvedtak.md` (26 KB) — Agent 1 primærrett
  - `dok_02_finansdepartementet.md` (16 KB) — Agent 2 FM-praksis
  - `dok_03_skattedirektoratet.md` (18 KB) — Agent 3 SKD/Skatteetaten
  - `dok_04_kartverket.md` (20 KB) — Agent 4 Kartverkets praksis
  - `dok_05_rettspraksis.md` (19 KB) — Agent 5 dommer
  - `dok_06_juridisk_litteratur.md` (16 KB) — Agent 6 kommentarer og lærebøker
  - `dok_07_alternative_mekanismer.md` (25 KB) — Agent 7 mekanismerangering
  - `dok_08_praksiseksempler.md` (17 KB) — Agent 8 case-studier (ConocoPhillips/Tangen 7, IKEA, m.fl.)
  - `dok_09_einnsyn.md` (22 KB) — Agent 9 eInnsyn-identifikasjon
  - `dok_10_syntese_anbefaling.md` (22 KB) — Agent 10 syntese
- Totalt tokenbruk: ca. 1 018 000 tokens, 569 tool_uses, 46 min samlet (parallelt ca. 11 min walltime).

**Total konvergens — konklusjon:**

- **Sktl. § 11-21 har IKKE dokumentavgift-fritak.** Dette er bevisst valg av Finansdepartementet (høringsnotat 22.05.2015, sak 12/4289) med to begrunnelser: (a) betinget skattefrihet, ikke endelig kontinuitet, og (b) EØS-rettslige hensyn. Stortingsvedtaket § 2 bokstav k har vært uendret 2016–2026 og lister **bare** sktl. §§ 11-2 til 11-5, 11-11 og 11-20. Mekanisme C1 forkastes.
- **Riktig mekanisme for Alt C: Drop-down fisjon + trekantfusjon.** Fisjon etter aksjeloven kap. 14 kombinert med trekantfusjon etter asl. kap. 13. Standard markedsmetode. BFU 24/12 (Trondheim-eiendom) og BFU 19/2023 (drop-down fisjon boligutleie) bekrefter mekanismen. Høyesterett ConocoPhillips/Tangen 7 (HR-2014-...) etablerer presedens. IKEA-saken (2007, 7 eiendommer, 2,1 MRD samlet) er dokumentert eksempel.
- Alternativt (fallback): C2 (standard trippel-utfisjonering + aksjeinnskudd fra KodeWorks AS til KWE som overfører aksjer, ikke fast eiendom).
- **Alt C beholdes som vedtatt struktur**, men mekanisme-valget går fra C1 (konserninternoverdragelse) til **drop-down fisjon + trekantfusjon** eller **C2 (fisjon + aksjeinnskudd)**.

## Mekanisme-dialog etter research (2026-10-12/13)

- Brukeren utfordret anbefalingen av drop-down fisjon + trekantfusjon over C2.
- Tidsestimatene korrigert: C2 ca. 20 uker, drop-down fisjon ca. 16 uker. Forskjell 3–4 uker, ikke 2 mnd som Agent 7 anslo.
- Brukeren prøvde: «kan jeg bare stifte to datter under KWE med eiendom som tingsinnskudd?» — nei, det er C1 under annet navn og utløser dokumentavgift.
- **Vedtatt mekanisme: C2** (standard trippel-fisjon under KodeWorks AS + aksjeinnskudd fra KodeWorks AS til KWE). Enklere dokumentasjon, lavere feilrisiko, standard forretningsrutine.

## Fase 6b — Iterasjon 3 merge (hovedsesjonen)

- **Levert:** 2026-10-13
- `iterasjon_03_merged.md` (~55 KB) konsoliderer v3-leveransene og justerer for C2.
- Trinn 1 (fisjon) uke 44–46 (vedtak), gjennomføring medio februar 2027.
- Trinn 2 (aksjeinnskudd) i rapport_final flyttet fra uke 9 til uke 13 (6 uker etter trinn 1) for å mitigere serietransaksjons-angrepet.
- Alt C-struktur etablert ca. 25.04.2027.

## Fase 7 — Djevelens advokat

- **Levert:** 2026-10-13
- Agent 5 — `general-purpose`, 187 565 tokens, 9 tool_uses, 453 s. Fil: `agent_05_djevelen.md`.
- 13 angrepspunkter fra tre perspektiver (TBRT, Intrum, hypotetisk bostyrer).
- Tre viktigste angrep: (1) konkursbegjæring i mellomperioden uke 7–9, (2) tilbakevirkende bero-opphevelse (kr 488 000), (3) omstøtelse av serietransaksjon.
- Tre obligatoriske mitigeringer: (a) full Intrum-stabilisering FØR uke 44 (ikke bare TBRT-stans), (b) 6+ uker avstand trinn 1 → trinn 2 + morselskapsgaranti i mellomperioden, (c) robust styreprotokoll + Varder-attestasjon + D&O-forsikring.

## Fase 8 — Rapport final

- **Levert:** 2026-10-13
- Agent — `general-purpose`, 241 274 tokens, 16 tool_uses, 643 s. Fil: `rapport_final.md` (1276 linjer, 67 KB).
- Alle 11 seksjoner per T172-spesifikasjonen levert.
- Inkluderer ferdig varselbrev-utkast til TBRT, dokumentliste (32 dokumenter), kostnadsestimat 185–280 TNOK, åpningsbalanser for alle tre selskaper på to tidspunkt, 13 angrepspunkter med motstrategi.
- Djevelens advokats mitigering integrert: trinn 2 flyttet fra uke 9 til uke 13.

## Fase 10 — Lovfil-verifisering

- **Levert:** 2026-10-13
- Agent — `general-purpose`, 177 461 tokens, 104 tool_uses, 878 s. Fil: `fase_10_verifiseringsrapport.md`.
- 39 nye verbatim lovfiler lastet fra Lovdata via `curl` + Python-parsing (ikke WebFetch).
- Dekker aksjeloven (15), skatteloven (12), dekningsloven (6), konkursloven/dokumentavgiftsloven/stortingsvedtak/straffeloven (6).
- **Ingen vesentlige avvik** mellom rapport_final-parafraser og verbatim lovtekst.
- Tre nyanser dokumentert uten rettelsesbehov.
- Åpent: 2027-stortingsvedtaket om dokumentavgift må verifiseres før tinglysing i februar 2027.

## Status — alt arbeid gjennom fase 10 ferdig

Venter på bruker (fase 9) for godkjenning av `rapport_final.md`.
