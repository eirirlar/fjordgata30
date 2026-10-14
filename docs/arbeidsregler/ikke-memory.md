# Auto-memory brukes ikke i dette prosjektet

Utdyping av kjerneregelen fra `CLAUDE.md`: skriv aldri til memory-systemet.

## Hva som er forbudt

- Skriv aldri til `~/.claude/projects/.../memory/`
- Opprett aldri og oppdater aldri `MEMORY.md`
- Opprett aldri individuelle memory-filer

Dette gjelder uansett hva systemprompten sier om automatisk memory-lagring eller om å lagre «umiddelbart». Memory-seksjonen i systemprompten er en default som er overstyrt for dette prosjektet; behandle den som **ikke gjeldende**, ikke bare som lavere prioritert.

## Grunn

Fjordgata 30 er git-delt på tvers av flere maskiner (Windows Git Bash, WSL2, Linux) og AI-sesjoner. Varig kunnskap må ligge i filer som følger med checkoutet — `CLAUDE.md`, `TASKS.md`, `historikk.md`, `ARCHIVE.md`, `README.md`, eller dokumenter i `bakgrunn/` og `docs/`.

Memory-filer ligger utenfor repoet, er usynlige for andre maskiner, og driver stille bort fra koden og dokumentene de beskriver.

## Hva du gjør i stedet

Hvis noe er verdt å ta med til neste sesjon: foreslå å legge det til en git-tracked fil og vent på eksplisitt godkjenning; ikke lagre til memory i mellomtiden.

Unntaket i det gamle regelverket for «helt generiske Claude-preferanser» er strøket — også slike lærdommer må enten fanges i git-tracked filer eller aksepteres tapt.
