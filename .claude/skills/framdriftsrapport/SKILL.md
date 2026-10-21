---
name: framdriftsrapport
description: Lag framdriftsrapport, utbetalingsanmodning eller endringsmelding til tilskuddsgiver (KMF, BYA, UNI, Enova, SkatteFunn). Leser tilsagnsvilkår fra bakgrunn/stotte/<giver>/, prosjektstatus fra stotte/project_cards.json, og tidligere rapporter som mal. Produserer Markdown i stotte/ eller leveranser/ klar for Pandoc→docx.
---

# Framdriftsrapport / utbetalingsanmodning til tilskuddsgiver

## Når skill-en skal brukes

Når brukeren ber om å lage:

- **Framdriftsrapport** til en støttegiver (periodisk rapportering)
- **Utbetalingsanmodning** med vedleggsrapport
- **Endringsmelding** (omdisponering, utsettelse, endring av støtteintensitet)
- **Sluttrapport** når tilsagn er fullt gjennomført

Trigger-fraser: «lag framdriftsrapport til KMF», «utbetalingsanmodning til UNI», «endringsmelding til BYA», «rapport til Enova».

## Trinn-for-trinn

### 1. Avklar leveransen

Spør eller bekreft:

- Hvilken støttegiver? (KMF, BYA, UNI, Enova KL, Enova OM, Enova yrkesbygg, SkatteFunn, Innovasjon Norge)
- Hvilken type leveranse? (framdrift, utbetaling, endring, sluttrapport)
- Hvilken periode skal dekkes? (fra forrige rapport til i dag; eller spesifikk)

### 2. Les kildematerialet

- `bakgrunn/stotte/<giver>/` — tilsagnsbrev, vilkår, oppstartsbrev, original søknad. **Særlig vilkårsdokumentet**: det styrer hva som må være med i rapporten.
- `stotte/project_cards.json` — aktuell state for denne støtteordningen (status, utbetalt, gjenstående, dato)
- Siste tidligere framdriftsrapport til samme giver (i `stotte/`) — brukes som mal for struktur og tone
- `bakgrunn/2026-06-01_arbeidsbeskrivelse.md` — autoritativ beskrivelse av utført arbeid (oppdateres mellom runder)
- `bakgrunn/2026-06-19_arbeidsokter_kmte.md` — strukturert arbeidsøkt-logg (dato, timer, hvem)
- `historikk.md` — kronologi for perioden som skal rapporteres

### 3. Hent bildeutvalg

Bilder til rapporten hentes via bildescoring-pipelinen:

```bash
python scripts/select_images.py --from <periode_start> --to <periode_slutt> --count 10
```

Bilder presenteres i Markdown pipe-tabell (se `docs/arbeidsregler/` — bildegrid-regelen i CLAUDE.md). Ikke LaTeX, ikke HTML.

### 4. Generer rapporten

**Målfil:**

- Framdrift/sluttrapport: `stotte/YYYY-MM-DD_<giver>_framdriftsrapport.md`
- Utbetalingsanmodning: `leveranser/YYYY-MM-DD_<giver>_utbetalingsanmodning.md` (hvis frittstående) eller `stotte/YYYY-MM-DD_<giver>_utbetalingsanmodning.md`
- Endringsmelding: `stotte/YYYY-MM-DD_<giver>_endringsmelding.md`

**Standardstruktur** (basert på etablerte rapporter):

1. YAML-frontmatter (tittel, dato, mottaker, saksref)
2. Innledning med saksreferanse og hva denne rapporten dekker
3. Prosjektstatus og konseptendring (hvis relevant)
4. Utført arbeid i perioden – kronologisk, med dato/bilder
5. Kulturminnefaglige funn (for KMF, BYA)
6. Fremdriftsplan videre
7. Kostnadsgjennomføring og evt. omdisponering
8. Vedleggsliste

### 5. Vilkårsavhengig tilpasning

- **KMF**: dokumentere kulturminnefaglig verdi; omtale konseptendringen fra kontor→minilager hvis den berører tilsagnet
- **BYA**: adressér steinmur i kjeller direkte (BYAs eksplisitte bekymring)
- **UNI**: krever revisor/regnskapsfører-bekreftelse ved utbetaling
- **Enova KL/OM**: kobling til energikartlegging/ombrukskartlegging — HRPs rapport legges som vedlegg
- **SkatteFunn**: FoU-fokus, teknisk nyhet, prosjektlogikk

### 6. Oppdater `stotte/project_cards.json`

Hvis rapporten representerer en milestone (utbetalt, endring vedtatt): oppdater prosjektkortet for støtteordningen.

## Regler som gjelder

- **Ikke generer `.docx` automatisk.** Markdown-kilden er leveransen; konvertering skjer kun når brukeren eksplisitt ber (CLAUDE.md).
- **Markdown hard linebreak** i signatur-blokker og adresseblokker (`\` eller blank linje).
- **Ikke navngi brukeren.** Prosjektleder/avsender navngis bare som signatur, ikke som subjekt i prosa.
- **Lovparagrafer** som siteres må være verifisert (`last-ned-paragraf`-skill).
- **Bilder i rapport** = Markdown pipe-tabeller, ikke LaTeX/HTML.

## Historisk referanse

Tidligere framdriftsrapporter og endringsmeldinger som har blitt gjennomgått og godkjent:

- `stotte/2026-06-24_kmf_framdriftsrapport.md`
- `stotte/2026-06-25_bya_framdriftsrapport.md`
- `stotte/2026-06-25_kmf_endringsmelding.md`
- `stotte/2026-06-25_bya_endringsmelding.md`
- `stotte/2026-06-25_kmf_omdisponering_finansiering.md`
- `leveranser/2026-04-20_fg30_arbeidsrapport.md` (overordnet mal for struktur)

## Kjente feil å unngå

- Automatisk generering av docx (ikke gjør det — brukeren bestiller eksplisitt)
- Bruk av «EL» eller «Eirik» som subjekt i prosa (bruk «prosjektleder»/passiv)
- Hallusinerte paragrafhenvisninger (verifisér mot `bakgrunn/lovverk/` eller `forretningsplan/lover/` først)
- Ferdig-presentasjon av endringsmeldinger som allerede er godkjent (jf. T114 i ARCHIVE.md)
