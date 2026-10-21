# Prosjekt-skills for Fjordgata 30

Skills definert for dette repoet. Hver skill ligger i egen undermappe med `SKILL.md` som definerer navn, beskrivelse og prosedyre.

Skills aktiveres av Claude Code enten ved at brukeren skriver `/<navn>` eller ved at Claude matcher brukerens intensjon mot skill-ens beskrivelse. Hver skill-fil leses først når skill-en invokeres, så bruk av skills påvirker ikke kontekstvinduet før de trengs.

## Definerte skills

| Skill | Formål |
|---|---|
| [`framdriftsrapport/`](framdriftsrapport/SKILL.md) | Framdriftsrapport, utbetalingsanmodning eller endringsmelding til tilskuddsgiver (KMF, BYA, UNI, Enova, SkatteFunn) |
| [`last-ned-paragraf/`](last-ned-paragraf/SKILL.md) | Verbatim lovparagraf-nedlasting fra Lovdata via curl. Bruk ALLTID før en konkret paragraf siteres i leveranse eller chat |
| [`pdf-til-md/`](pdf-til-md/SKILL.md) | Konverter PDF til Markdown med `pdftotext -layout`, dato-prefix og `kilde:`-metadata |
| [`motereferat/`](motereferat/SKILL.md) | Fra lydopptak i `referat/nye/` til ferdig møtereferat (WhisperX + redaksjon) |
| [`arkiver-sak/`](arkiver-sak/SKILL.md) | Arkiver lukket sak til `<domene>/arkiv/<sak>/`, oppdater alle referanser via Python |

## Kandidater som ikke er definert ennå

Fra kartleggingen i T186 ble disse identifisert som gode kandidater, men ikke høyeste prioritet. Legges til ved behov:

- `arbeidsavtale` – midlertidig ansettelse (mal + norsk-ID-sjekk)
- `verifiser-sitater` – dokumentkonsistens mot kilder
- `opprett-sak-indeks` – ny `saker/<sak>/OVERSIKT.md` for krysserssak
- `rolle-review` – multi-agent-review av leveransepakke
- `aggreger-arbeidsokter` – timer/arbeidsøkt-sammenstilling periodisk
- `bildegrid` – pipe-tabell med bilder for rapport
- `konverter-md` – md → docx eller md → pdf med pandoc
