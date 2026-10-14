# Mappestruktur – prosjektdokumentasjon

Oversikt over hvor prosjektets dokumenter, leveranser og bakgrunnsmateriale ligger. For kode- og dataoppsett (scripts/, data/, venvs), se `README.md` eller `docs/referanse.md`.

```
fjordgata30/
├── CLAUDE.md                  – prosjektkontekst og arbeidsregler for AI
├── TASKS.md                   – oppgaveliste med status
├── ARCHIVE.md                 – arkiv over løste oppgaver
├── historikk.md               – kronologisk prosjekthistorikk
├── README.md                  – oversikt over kode/verktøy + lenker til docs/
├── docs/                      – utdypende dokumentasjon og arbeidsregel-detaljer
│   ├── interessenter.md       – stakeholder-oversikt
│   ├── mappestruktur.md       – dette dokumentet
│   ├── oppsett.md             – førstegangsoppsett per maskin
│   ├── aktivering.md          – aktivering per terminalvindu
│   ├── bildescoring.md        – bruk av bildescoring-pipelinen
│   ├── transkribering.md      – bruk av WhisperX
│   ├── dokumentkonvertering.md – Pandoc-oppsett og kommandoer
│   ├── analyseverktoy.md      – areal/konkurranse/tegninger
│   ├── referanse.md           – dataflyt, datafiler, kjente feil
│   └── arbeidsregler/         – utdyping av enkeltregler fra CLAUDE.md
├── saker/                     – indekser for flerdomene-saker (ingen filer, bare pekere)
│   ├── tvangsmulkt/OVERSIKT.md   – TBRT → klage → Sivilombud + DSB → Intrum
│   └── kjeller-ra/OVERSIKT.md    – kjellerarbeid + Riksantikvar-dialog
├── referat/                   – møtereferater (Statusmøte 01–05)
├── bakgrunn/                  – søknader, prosjektbeskrivelse, bakgrunnsdokumenter, arbeidslogger
│   ├── arbeid_kristian.txt    – arbeidslogg, Kristian Brandsegg
│   ├── arbeid_ole_morten.txt  – arbeidslogg, Ole Morten Lagmannssveen
│   ├── ai_feedback.txt        – redaksjonelle merknader fra prosjektleder til arbeidsrapport-utkast
│   ├── nye/                   – innkommende filer som ikke er klassifisert ennå (opprettes ved behov)
│   ├── brann/                 – all branndokumentasjon samlet: brannkonsept, brannprosjektering, brannteknisk vurdering, HRPs notat om brannsikring i gjennomføringsfasen, TBRTs pålegg og saksdokumenter i tvangsmulkt-saken (inkl. rammesøknad-vedlegg som underbygger klagen)
│   ├── tbrt/                  – TBRT/TekØk-korrespondanse 2018–2022: tilsynsrapporter, purringer, tiltaksplanakseptbrev, TekØk-skjema. Historisk opptakt til tvangsmulkt-saken.
│   ├── eiendom/               – historiske eiendomsdokumenter 2013–2015: matrikkel, grunnbok, kjøpekontrakt, prospekt, situasjonskart, skattetakst, IK-kontroll Trondheim Båtforening
│   ├── fisjon/                – fisjonsanalysen 2026-10 (agenter, iterasjoner, review, rapport_final, dokumentavgift-research, MVA-justering)
│   ├── okonomi/               – regnskapsdata (kw, kwe) 2019–2026
│   ├── stotte/                – bakgrunnsdokumenter relatert til støtteprosjekter (tilsagn, vilkår)
│   ├── lovverk/               – lovtekster og forskrifter (verbatim fra Lovdata)
│   ├── enova/                 – bakgrunnsdokumenter Enova-søknader
│   └── mva/                   – bakgrunnsdokumenter MVA-vurdering
├── leveranser/                – ferdige dokumenter produsert i prosjektet (klager, rapporter, brev; .docx genereres ved behov med Pandoc)
│   ├── 2026-04-20_fg30_arbeidsrapport.md – arbeidsrapport (Pandoc-klar Markdown)
│   └── brann/                 – branndokumentasjon vi selv produserer: byggeplassinstruks, brann-ROS, sjekklister, fotodokumentasjon av branntekniske tiltak, Sivilombuds-klage og DSB-pakke
└── stotte/                    – tilskuddsdata i project_cards.json-format, framdriftsrapporter og endringsmeldinger. Se også `bakgrunn/stotte/` for mottatt underlag (tilsagn, vilkår). Se også `../stotte` (annet git-prosjekt – fare for at det ikke er sjekket ut); mal for project_cards.json kommer derfra.
```

**Prinsipper for når filer legges hvor:**

- **`bakgrunn/`** = mottatt underlag + prosjekt-interne analyser og notater. Flat dato-prefix for toppnivå; tematiske undermapper (`brann/`, `tbrt/`, `eiendom/`, `fisjon/`, `okonomi/`, `stotte/`, `lovverk/`, `enova/`, `mva/`) for sammenhengende serier.
- **`leveranser/`** = ferdige dokumenter vi sender ut (klager, søknader, brev, rapporter).
- **`saker/`** = indekser for saker som krysser flere mapper. Peker inn i `bakgrunn/`, `leveranser/`, `bakgrunn/lovverk/`, osv. Dupliserer aldri filer.
- **`forretningsplan/`, `bank/`, `stotte/` på rotnivå** = levende dokumentmasser med egen regenereringssyklus.

**Branndokumentasjon – hvor ting ligger.** Det finnes ingen `brann/`-mappe på rotnivå. Skillet er:

- **Mottatt underlag og saksdokumenter** ligger samlet i `bakgrunn/brann/` med dato-prefix: brannkonsept, brannprosjektering, brannteknisk vurdering fra TekØk, TBRTs pålegg og støttebrev, tvangsmulkt-saken (klage, bero-beslutning, saksfremlegg, møteprotokoller, orientering), samt rammesøknad-vedlegg (situasjonskart, planer, snitt, fasade, nabovarsel, ansvarsrett) som ble lagt ved klagen av 18.06.2026. Det viktigste for byggefasen er `bakgrunn/brann/2026-02-26_notat_brannsikring_gjennomforingsfasen.txt` (HRP). Eldre TBRT-korrespondanse (tilsynsrapporter, purringer, aksept av tiltaksplaner 2018–2022) er samlet i `bakgrunn/tbrt/`.
- **Det vi selv produserer** legges i `leveranser/brann/`.
