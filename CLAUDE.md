# Fjordgata 30 – Prosjektkontekst

## Hva er dette

KodeWorks Eiendom AS rehabiliterer Fjordgata 30 i Trondheim (en gammel brygge) til minilager. Prosjektet drives av Eirik Larsen. Kristian og Ole Morten utfører fysisk arbeid. Rammesøknad ble levert 12. mai 2026.

Se `TASKS.md` for oppgaveliste og status.

---

## Interessenter

| Part | Relasjon | Bekymring |
|------|----------|-----------|
| **Kulturminnefondet** | Har gitt 750 000 kr i tilskudd | Vil se fysisk arbeid før utbetaling; utålmodig |
| **Byantikvaren** | Har gitt 500 000 kr i tilskudd | Vil se fysisk arbeid; bekymret for steinmur i kjeller |
| **Trondheim Brannvesen / TBRT** | Tilsynsmyndighet | Krever sprinkleranlegg; har ilagt dagbøter 2 000 kr/dag (bestridt) |
| **Enova** | Støttegiver | Framdriftsrapportering |
| **Stiftelsen UNI** | Støttegiver | Framdriftsrapportering |
| **Bank** | Finansiør | Trenger oversikt over alle støttemidler |

Alle rapporter og dokumenter skal overbevise om at prosjektet er reelt og fremdriften er god.

---

## Filer og mapper

```
fjordgata30/
├── CLAUDE.md                  – dette dokumentet (prosjektkontekst for AI)
├── TASKS.md                   – oppgaveliste med status
├── status.txt                 – prosjektbeskrivelse og fremdrift
├── referat/                   – møtereferater (Statusmøte 01–05)
├── bakgrunn/                  – søknader, prosjektbeskrivelse, bakgrunnsdokumenter, arbeidslogger
│   ├── arbeid_kristian.txt    – arbeidslogg, Kristian Brandsegg
│   ├── arbeid_ole_morten.txt  – arbeidslogg, Ole Morten Lagmannssveen
│   ├── ai_feedback.txt        – redaksjonelle merknader fra prosjektleder til arbeidsrapport-utkast
│   └── nye/                   – innkommende filer som ikke er klassifisert ennå (opprettes ved behov)
│   └── stotte/                – bakgrunnsdokumenter relatert til støtteprosjekter
├── leveranser/                – ferdige dokumenter produsert i prosjektet (klager, rapporter, brev; .docx genereres ved behov med Pandoc)
│   └── 2026-04-20_fg30_arbeidsrapport.md – arbeidsrapport (Pandoc-klar Markdown)
├── stotte/                    – tilskuddsdata i project_cards.json-format, og annen støtte relatert dokumentasjon. Se også bakgrunn/stotte. Se også ../stotte (annet git prosjekt - fare for at det ikke er sjekket ut). ../stotte har original template for project_cards.json, som vi har divergert litt fra.
└── brann/                     – branndokumentasjon, brannkonsept, TBRT-redegjørelse
```

---

## Arbeidsregler

- **Les disse først:** Ved oppstart av en oppgave, eller når kontekst mangler, les `README.md`, `historikk.md`, `TASKS.md` og `ARCHIVE.md`. README beskriver scripts og dataflyt, historikk gir kronologisk prosjektkontekst, TASKS viser åpne oppgaver, og ARCHIVE inneholder løste oppgaver med løsningsnotat. Søk i ARCHIVE før du starter en ny oppgave for å unngå dobbeltarbeid.
- **Tillatelser:** Spør alltid om tillatelse før du kjører kode eller rører filer utenfor prosjektmappen (`fjordgata30/`), selv om du kjører med `--dangerously-skip-permissions`. Dette gjelder bl.a. lesing fra `../stotte` eller andre naboprosjekter – les der, men skriv aldri dit uten eksplisitt godkjenning.
- **Kodeendringer krever konfirmasjon:** Ikke gjør endringer i kode eller opprett nye filer uten at brukeren eksplisitt har bedt om det. Hvis brukeren diskuterer, spør eller ber om en beskrivelse/plan, svar med tekst — ikke med kode. Vent på et tydelig "gjør det" eller tilsvarende før du rører filer.
- **Estimer tidsforbruk før du starter:** Før du iverksetter en oppgave, vurder kompleksiteten og gi et grovt estimat på tidsforbruk (f.eks. "dette tar ~30 sekunder" eller "dette er en stor operasjon som kan ta 5–10 minutter"). Hvis estimatet er over ~2 minutter, krev eksplisitt konfirmasjon fra brukeren før du starter — selv om du allerede har fått en generell "gjør det".
- **Task-dokumentasjon:** Når en oppgave er løst, dokumenter løsningen under oppgavens kontekst-seksjon i `TASKS.md` og marker statusen som `[x]`. Ikke bare oppdater status uten å notere hva som ble gjort og hvilke filer som ble opprettet/endret.
- **Task-nummerering:** Før du oppretter en ny task, finn høyeste eksisterende T-nummer på tvers av **begge** `TASKS.md` og `ARCHIVE.md`: `grep -h "^### T" TASKS.md ARCHIVE.md | grep -oP 'T\d+' | sort -t T -k2 -n | tail -1`. Bruk neste ledige nummer.
- **Task-sortering:** Tasks i `TASKS.md` og `ARCHIVE.md` skal alltid være sortert stigende på T-nummer. Når du oppretter en ny task, sett den inn på riktig plass i rekkefølgen – ikke legg den til sist uten å sjekke nummeret. Subtasks (T01.02 o.l.) sorteres under sin hovedtask.
- **Arkivering av tasks:** Løste tasks flyttes fra `TASKS.md` til `ARCHIVE.md` kun når brukeren eksplisitt ber om det. Aldri arkiver på eget initiativ. Søk alltid i `ARCHIVE.md` før du starter en oppgave for å unngå dobbeltarbeid.
- **Ikke start tasks automatisk:** Begynn aldri på en task uten eksplisitt instruksjon fra brukeren i den pågående samtalen. Når en task er ferdig, vent på neste instruksjon – ikke velg og begynn på den neste tasken på egenhånd.
- **README-oppdatering:** Vurder alltid om `README.md` må oppdateres som del av å løse en oppgave. Nye scripts, endrede filnavn, endret filstruktur eller nye avhengigheter skal alltid reflekteres i README.
- **PDF-konvertering:** Bruk alltid `pdftotext` (eller tilsvarende CLI-verktøy) via Bash for å konvertere PDF til tekst. Bruk aldri Read-verktøyet side for side på PDF-filer – det er svært kostbart og mister strukturert tekst. Eksempel: `pdftotext -layout "filnavn.pdf" - > filnavn.txt`
- **Python-kommando (plattformavhengig):** På **Windows**: bruk alltid `uv run python` – aldri `python3` eller `uv run python3` (disse feiler med «Python ble ikke funnet»). På **Linux/macOS**: `python3` fungerer direkte. `uv run python` fungerer på begge plattformer og er trygt å bruke uansett. Bruk Bash-verktøyet, ikke PowerShell, for Python-kjøring.
- **Plattform og skallmiljø varierer:** Brukeren jobber på tvers av Windows (Git Bash, Cygwin, WSL2) og Linux på ulike maskiner. Anta aldri et bestemt operativsystem, skallmiljø eller filsti. Unngå Cygwin-spesifikke stier (`/cygdrive/c/...`). Bash-verktøyet er satt til prosjektmappen — bruk `cd` kun når strengt nødvendig, og bruk da relative stier eller stier som fungerer i Git Bash/Linux (`/c/dev/...` el. absolutte Linux-stier). Memory-filer (`.claude/projects/.../memory/`) er lokale per maskin og følger ikke med git-commits — skriv aldri maskin- eller OS-spesifikke antakelser til memory.
- **Spør før suboptimal fremgangsmåte:** Hvis du ser at du er i ferd med å gjøre noe på en ineffektiv måte (mange trinn, store tokenkostnader, omveier), stopp og spør brukeren om de er sikre på at de vil at du skal fortsette slik – selv om du kjører med `--dangerously-skip-permissions`.
- **Kode og parametere på engelsk:** All kode skrives på engelsk – variabelnavn, funksjonsnavn, kommentarer i koden, og CLI-argumenter/flagg til scripts (f.eks. `--from`, `--to`, `--limit`, ikke `--fra`, `--til`, `--antall`). Dokumentasjon og rapporter til brukere/interessenter skrives på norsk.
- **Scripts samles i `scripts/`:** Alle Python-scripts og andre kjørbare hjelpescripts legges alltid i `scripts/`-mappen, uavhengig av hvilken del av dokumentasjonen de tilhører. Scripts skrives med stier relative til prosjektroten og kjøres alltid derfra (`uv run python scripts/navn.py`). Ikke legg scripts i undermapper som `timer/`, `leveranser/`, `brann/` o.l.
- **Dato-prefix på filer i `bakgrunn/`:** Alle nye filer som legges i `bakgrunn/` skal ha dato-prefix på formen `YYYY-MM-DD_beskrivelse.ext` (f.eks. `2026-06-23_notat_byantikvaren.md`). Eksisterende filer uten dato-prefix skal omdøpes ved neste berøring, og referanser i `historikk.md` og `TASKS.md` oppdateres tilsvarende. Unntak: filer i `bakgrunn/stotte/` (følger prosjektmappestruktur).
- **"Nye oppgaver"-seksjonen i TASKS.md:** Når `TASKS.md` leses, sjekk alltid om `## Nye oppgaver` inneholder uprosesserte punkter (bullet-linjer). Hvis det finnes slike punkter: spør brukeren om de skal prosesseres. Prosessering betyr å konvertere hvert punkt til en nummerert T-task med beskrivelse og slette punktet fra seksjonen.
- **Git og gh er ALDRI tillatt uten eksplisitt tillatelse i den aktuelle samtalen:** Kjør aldri `git`, `gh` eller andre kommandoer som invoker git (inkludert scripts som kaller git internt, og sammensatte Bash-kommandoer der git inngår noe sted – `pwd && git ...` er like forbudt som ren `git ...`). Dette gjelder **alle** operasjoner, også «harmløse» lese-kommandoer: `git status`, `git diff`, `git log`, `git branch`, `git show`, `git ls-files`, `git rev-parse`, `git worktree list`, `gh pr list`, `gh issue view` osv. Før hver Bash-kommando, sjekk eksplisitt om `git` eller `gh` inngår noe sted – hvis ja, stopp og spør om tillatelse, selv om du trenger info raskt. Det er kombinasjonen «trygg lese-kommando» + «rask svar trengs» som er autopilot-fellen. Trenger du info som kunne kommet fra git: bruk Read/Glob/Grep, eller spør brukeren om å lime inn output.
- **Ikke konverter til docx automatisk:** Generer aldri `.docx` av en leveranse (verken via Pandoc, `format_docx.py` eller annet) som del av en task – heller ikke når et eksisterende docx-vedlegg endres og «burde regenereres for konsistens». Markdown-kilden er leveransen; konvertering til docx skjer **kun når brukeren eksplisitt bestiller det**. Ved tvil: nevn at docx ikke er regenerert i sluttoppsummeringen, så brukeren selv kan bestille det.
- **Pandoc er valgt konverteringsverktøy** for `.docx`, `.pptx` og `.pdf`. Bruk pandoc-kommandoer direkte (`pandoc input.md -o output.docx` osv.) når brukeren bestiller konvertering. Ikke foreslå alternative pipelines (LibreOffice, Word-COM, weasyprint, etc.) uten at pandoc-veien er testet og avvist først. PDF-konvertering krever en separat engine (pdflatex/xelatex/wkhtmltopdf) – hvis ingen er tilgjengelig, lever docx og overlat PDF-konvertering til bruker i Word/Office.
- **Rydd opp etter agent-invokasjoner:** Ved tasks som invokerer `Agent`-tool (særlig med `isolation: "worktree"`), sjekk alltid på slutten at `.claude/worktrees/agent-*`-mappene er ryddet. Claude Code-harness rydder normalt automatisk etter agents som ikke gjorde endringer, men det feiler av og til. Når task er ferdig og agentbidrag er konsolidert tilbake til hovedbranchen: list `.claude/worktrees/` og slett gjenstående `agent-*`-mapper relatert til tasken. Dokumentér i task-løsningsnotatet at oppryddingen er gjort.
- **Agent-tool oppretter alltid worktrees – planlegg for opprydding:** Det `Agent`-tool i Claude Code (denne harness-versjonen) oppretter en worktree per spawn uansett, også uten at `isolation: "worktree"` settes eksplisitt. `isolation`-parameteren har bare `"worktree"` som mulig verdi, så det er ingen «ikke-worktree»-modus tilgjengelig. Dette gjelder også agenter som bare leser filer. Konsekvens: hver gang `Agent` invokeres, må det planlegges for opprydding etter at tasken er ferdig (Claude Code-harnessen rydder ikke alltid pålitelig). Etter sesjonen er avsluttet og pid er død, kan worktrees ryddes med: `git worktree repair` → `git worktree unlock` → `git worktree remove --force` → `git branch -D` (og `git worktree prune` til slutt). For Cygwin/Windows-mismatch: kjør oppryddingen i Git Bash, ikke Cygwin.

---

## Tone og format

- Alle dokumenter skrives på norsk (bokmål)
- Rapporter som skal til eksterne parter formateres i Markdown slik at de ser bra ut konvertert til `.docx` med Pandoc
- Vær konkret og faktabasert – ikke prøv å "selge inn" prosjektet med tomme ord, men la faktisk dokumentert arbeid tale for seg
- Adresser stakeholdernes bekymringer direkte i hvert dokument
