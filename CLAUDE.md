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
├── leveranser/                – ferdige dokumenter produsert i prosjektet (klager, rapporter, brev; .docx genereres ved behov med Pandoc)
│   └── 2026-04-20_fg30_arbeidsrapport.md – arbeidsrapport (Pandoc-klar Markdown)
├── stotte/                    – tilskuddsdata i project_cards.json-format (speil av ../stotte for FG30)
└── brann/                     – branndokumentasjon, brannkonsept, TBRT-redegjørelse
```

---

## Arbeidsregler

- **Tillatelser:** Spør alltid om tillatelse før du kjører kode eller rører filer utenfor prosjektmappen (`fjordgata30/`), selv om du kjører med `--dangerously-skip-permissions`. Dette gjelder bl.a. lesing fra `../stotte` eller andre naboprosjekter – les der, men skriv aldri dit uten eksplisitt godkjenning.
- **Kodeendringer krever konfirmasjon:** Ikke gjør endringer i kode eller opprett nye filer uten at brukeren eksplisitt har bedt om det. Hvis brukeren diskuterer, spør eller ber om en beskrivelse/plan, svar med tekst — ikke med kode. Vent på et tydelig "gjør det" eller tilsvarende før du rører filer.
- **Estimer tidsforbruk før du starter:** Før du iverksetter en oppgave, vurder kompleksiteten og gi et grovt estimat på tidsforbruk (f.eks. "dette tar ~30 sekunder" eller "dette er en stor operasjon som kan ta 5–10 minutter"). Hvis estimatet er over ~2 minutter, krev eksplisitt konfirmasjon fra brukeren før du starter — selv om du allerede har fått en generell "gjør det".
- **Task-dokumentasjon:** Når en oppgave er løst, dokumenter løsningen under oppgavens kontekst-seksjon i `TASKS.md` og marker statusen som `[x]`. Ikke bare oppdater status uten å notere hva som ble gjort og hvilke filer som ble opprettet/endret.
- **Task-nummerering:** Før du oppretter en ny task, finn høyeste eksisterende T-nummer på tvers av **begge** `TASKS.md` og `ARCHIVE.md`: `grep -h "^### T" TASKS.md ARCHIVE.md | grep -oP 'T\d+' | sort -t T -k2 -n | tail -1`. Bruk neste ledige nummer.
- **Arkivering av tasks:** Løste tasks flyttes fra `TASKS.md` til `ARCHIVE.md` kun når brukeren eksplisitt ber om det. Aldri arkiver på eget initiativ. Søk alltid i `ARCHIVE.md` før du starter en oppgave for å unngå dobbeltarbeid.
- **README-oppdatering:** Vurder alltid om `README.md` må oppdateres som del av å løse en oppgave. Nye scripts, endrede filnavn, endret filstruktur eller nye avhengigheter skal alltid reflekteres i README.
- **PDF-konvertering:** Bruk alltid `pdftotext` (eller tilsvarende CLI-verktøy) via Bash for å konvertere PDF til tekst. Bruk aldri Read-verktøyet side for side på PDF-filer – det er svært kostbart og mister strukturert tekst. Eksempel: `pdftotext -layout "filnavn.pdf" - > filnavn.txt`
- **Python-kommando (plattformavhengig):** På **Windows** (dette prosjektet): bruk alltid `uv run python` – aldri `python3` eller `uv run python3` (disse feiler med «Python ble ikke funnet»). På **Linux/macOS**: `python3` fungerer direkte. Bruk Bash-verktøyet, ikke PowerShell, for Python-kjøring.
- **Spør før suboptimal fremgangsmåte:** Hvis du ser at du er i ferd med å gjøre noe på en ineffektiv måte (mange trinn, store tokenkostnader, omveier), stopp og spør brukeren om de er sikre på at de vil at du skal fortsette slik – selv om du kjører med `--dangerously-skip-permissions`.
- **Kode og parametere på engelsk:** All kode skrives på engelsk – variabelnavn, funksjonsnavn, kommentarer i koden, og CLI-argumenter/flagg til scripts (f.eks. `--from`, `--to`, `--limit`, ikke `--fra`, `--til`, `--antall`). Dokumentasjon og rapporter til brukere/interessenter skrives på norsk.
- **Dato-prefix på filer i `bakgrunn/`:** Alle nye filer som legges i `bakgrunn/` skal ha dato-prefix på formen `YYYY-MM-DD_beskrivelse.ext` (f.eks. `2026-06-23_notat_byantikvaren.md`). Eksisterende filer uten dato-prefix skal omdøpes ved neste berøring, og referanser i `historikk.md` og `TASKS.md` oppdateres tilsvarende. Unntak: filer i `bakgrunn/stotte/` (følger prosjektmappestruktur).
- **"Nye oppgaver"-seksjonen i TASKS.md:** Når `TASKS.md` leses, sjekk alltid om `## Nye oppgaver` inneholder uprosesserte punkter (bullet-linjer). Hvis det finnes slike punkter: spør brukeren om de skal prosesseres. Prosessering betyr å konvertere hvert punkt til en nummerert T-task med beskrivelse og slette punktet fra seksjonen.
- **Git og gh er forbudt uten eksplisitt tillatelse:** Kjør aldri `git`, `gh` eller andre kommandoer som invoker git (f.eks. scripts som kaller git internt) uten at brukeren eksplisitt har gitt tillatelse i den aktuelle samtalen. Dette gjelder alle git-operasjoner: commit, add, status, log, diff, push, pull, checkout osv.

---

## Tone og format

- Alle dokumenter skrives på norsk (bokmål)
- Rapporter som skal til eksterne parter formateres i Markdown slik at de ser bra ut konvertert til `.docx` med Pandoc
- Vær konkret og faktabasert – ikke prøv å "selge inn" prosjektet med tomme ord, men la faktisk dokumentert arbeid tale for seg
- Adresser stakeholdernes bekymringer direkte i hvert dokument
