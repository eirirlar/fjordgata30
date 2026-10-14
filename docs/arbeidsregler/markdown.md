# Markdown – hard linebreak i signaturer, adresser og metadata

Utdyping av kjerneregelen fra `CLAUDE.md`: bruk backslash `\` eller blank linje for å unngå at logisk sammenhengende linjer kollapser til én sammenhengende setning.

## Problemet

Enkel newline i Markdown kollapser til én space når fila rendres (VS Code preview, pandoc → PDF/DOCX, GitHub-visning). Signaturer, adresse-blokker, dokument-headere med `**Bold-label:**`-linjer og lignende blir da til én sammenklumpet setning.

## Løsning

Bruk backslash `\` på slutten av hver ikke-siste linje i logisk sammenhengende blokker — eller blank linje for full paragrafbrytning.

Sjekk før hver `Write`/`Edit` som produserer signatur, header, datotabell kort format eller adresse. Referatene i `referat/` er mønsteret som brukes konsekvent.

## Unntak

Leveranser som skal *limes inn i webskjema* (ikke rendres) — vurder blank linje istedenfor backslash slik at rå tekst ikke viser `\`-tegn i skjemaet.

Dette er en tilbakevendende feil på tvers av sesjoner.
