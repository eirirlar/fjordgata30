# Agenter og worktrees

Utdyping av kjerneregelen fra `CLAUDE.md`: start agenter uten worktree som standard, og ikke rydd opp i worktrees uten eksplisitt tillatelse.

## Agenter uten worktree som standard

Start `Agent` **uten** `isolation: "worktree"` med mindre agenten skal gjøre endringer som må holdes adskilt fra hovedmappen. Agenter som bare leser og leverer tekst tilbake, trenger ikke worktree; hovedsesjonen skriver filene.

Uten `isolation` jobber agenten direkte i prosjektmappen, og ingen git-kopi lages.

**Merk:** En eldre harness-versjon ble observert å lage worktree per agent uansett. Sjekk derfor alltid etter agent-kjøringer med `ls .claude/worktrees/` (ikke git) at det ikke ligger igjen `agent-*`-mapper, og noter resultatet i task-løsningsnotatet.

## Opprydding av agent-worktrees (kun ved behov)

Finnes det `agent-*`-mapper i `.claude/worktrees/` etter en task, stopp og spør brukeren — oppryddingen krever git, og git er bare tillatt med eksplisitt tillatelse i samtalen.

Med tillatelse, og etter at sesjonen som laget dem er avsluttet:

1. `git worktree repair`
2. `git worktree unlock`
3. `git worktree remove --force`
4. `git branch -D`
5. `git worktree prune` til slutt

For Cygwin/Windows-mismatch: kjør oppryddingen i Git Bash, ikke Cygwin.
