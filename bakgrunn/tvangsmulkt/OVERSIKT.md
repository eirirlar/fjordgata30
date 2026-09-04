---
tittel: "Oversikt – konvertering av tvangsmulkt-mappen"
dato: 2026-09-04
status: "Konvertert. Original-PDF-ene er tatt ut av repoet av EL etter gjennomgang."
---

# Oversikt – konvertering av tvangsmulkt-mappen

46 PDF-er mottatt. Dette dokumentet viser hva som er nytt, hva vi hadde fra før, og hvilken .md som hører til hvilken PDF.

## Hvor ting ligger

| Innhold | Sted |
|---|---|
| Konverterte `.md`-filer og tegningsbilder | `bakgrunn/tvangsmulkt/` (denne mappen) |
| Original-PDF-er | Tatt ut av repoet av EL etter gjennomgang. Ligger hos EL. |

## Navnekonvensjon

Hver .md er navngitt **etter kilde-PDF-en**, ikke etter et oppfunnet emne:

1. Fjern `.pdf`
2. Alt til små bokstaver
3. Mellomrom til understrek
4. `_-_` slås sammen til `_` (bindestrek med mellomrom rundt i originalen)
5. Ellers uendret — bindestreker uten mellomrom, doble understrek og norske tegn beholdes
6. Dato-prefiks `YYYY-MM-DD_` foran

Eksempel: `Møteprotokoll 25082026 - Signert.pdf` → `2026-08-25_møteprotokoll_25082026_signert.md`

**Merk:** én fil har `-_` igjen: `2026-06-18_klage_på_innkreving_av_tvangsmulkt-_fjordgata_30_5001401149.md`. Det skyldes at TBRT selv glemte mellomrommet i sitt filnavn (`...tvangsmulkt- Fjordgata 30...`). Navnet er beholdt slik for å speile kilden.

Der én PDF ga bilder, ligger de i `bilder/` med samme avledede navn og sidenummer, f.eks. `bilder/e-9_e-15_planer-eksisterende-3.png`.

---

## 1. Hovedfunn

**Klagen er avslått.** Klageorganet i TBRT behandlet saken 25.08.2026 og tok ikke klagen til følge. Alle tre innkrevinger, til sammen **kr 184 000**, opprettholdes. Orienteringsbrev til KodeWorks Eiendom AS er datert 02.09.2026.

Brevet avslutter med: *«Pålegget anses etter dette som ikke etterkommet, og forholdet vil bli fulgt opp videre.»* Tvangsmulkten løper altså videre.

**Skjermbildene er hentet ut.** TBRT gjengav alle klagers anførsler som skjermbilder i saksfremlegget, ikke som tekst. Seks skjermbilder, punkt 4.1 til 4.6. All tekst er lest ut av bildene og skrevet av. Avskriften er kontrollert mot originalklagen: null fremmede ord.

**Pålegget hadde også bildetekst.** `Pålegg om brannsikring` har to bilder på side 2 og 3 med TBRTs *egen* tekst — sitater fra deres tidligere brev. Teksten manglet i `bakgrunn/2024-11-08_paalegg_brannsikring.md` og er nå fylt inn der som blokksitat.

**De uthentede tekstbildene er slettet.** Original-PDF-ene er beviset, ikke våre PNG-er av dem. Når teksten er skrevet av og kontrollert, har bildefilene ingen egen verdi. Bildene i `bilder/` er derfor kun tegninger.

---

## 2. Mapping — PDF til .md

| Kilde-PDF | Ny .md-fil |
|---|---|
| `Saksfremlegg til klageorganet i TBRT vedrørende Fjordgata 30 - 5001401149.pdf` | `2026-06-26_saksfremlegg_til_klageorganet_i_tbrt_vedrørende_fjordgata_30_5001401149.md` |
| `Svar på brev datert 17062026 - Fjordgata 30 - 5001401149.pdf` | `2026-06-25_svar_på_brev_datert_17062026_fjordgata_30_5001401149.md` |
| `Oppreisning av klagefrist og utsatt iverksetting - Fjordgata 30 - 5001401149.pdf` | `2026-06-26_oppreisning_av_klagefrist_og_utsatt_iverksetting_fjordgata_30_5001401149.md` |
| `Møteprotokoll 25082026 - Signert.pdf` | `2026-08-25_møteprotokoll_25082026_signert.md` |
| `Orientering om vedtak fattet av klageorganet - Fjordgata 30 - 5001401149.pdf` | `2026-09-02_orientering_om_vedtak_fattet_av_klageorganet_fjordgata_30_5001401149.md` |
| `Nabovarsel.pdf` | `2026-01-26_nabovarsel.md` |
| `Kvittering for Nabovarsel.pdf` | `2026-01-26_kvittering_for_nabovarsel.md` |
| `Ansvarsrett signert 09022026.pdf` | `2026-02-09_ansvarsrett_signert_09022026.md` |
| `Ansvarsrett signert 11022026.pdf` | `2026-02-11_ansvarsrett_signert_11022026.md` |
| `Ansvarsrett signert 11022026-2.pdf` | `2026-02-11_ansvarsrett_signert_11022026-2.md` |
| `Ansvarsrett signert 11052026.pdf` | `2026-05-11_ansvarsrett_signert_11052026.md` |
| `Klage på innkreving av tvangsmulkt- Fjordgata 30 - 5001401149.pdf` | `2026-06-18_klage_på_innkreving_av_tvangsmulkt-_fjordgata_30_5001401149.md` |
| `Klage på innkreving av tvangsmulkt - Vedlegg 1 - Rammesøknad.pdf` | `2026-06-18_klage_på_innkreving_av_tvangsmulkt_vedlegg_1_rammesøknad.md` |
| `Klage på innkreving av tvangsmulkt - Vedlegg 3 - Brannsikringsplan.pdf` | `2026-06-18_klage_på_innkreving_av_tvangsmulkt_vedlegg_3_brannsikringsplan.md` |
| `D-01 Situasjonskart.pdf` | `2023-06-13_d-01_situasjonskart.md` |
| `D-02 Situasjonsplan.pdf` | `2026-01-26_d-02_situasjonsplan.md` |
| `E-1 - E-4_ Fasade eksisterende.pdf` | `2026-05-19_e-1_e-4__fasade_eksisterende.md` |
| `E-5 - E-8_ Fasade planlagt.pdf` | `2026-05-19_e-5_e-8__fasade_planlagt.md` |
| `E-9 - E-15_Planer-eksisterende.pdf` | `2026-02-06_e-9_e-15_planer-eksisterende.md` |
| `E-16 - E-22_Planer-planlagt.pdf` | `2026-02-16_e-16_e-22_planer-planlagt.md` |
| `E-16 - E-22_ Planer planlagt.pdf` | *(duplikat — ikke konvertert, se punkt 4.4)* |
| `E-23 - E-24_ Snitt eksisterende.pdf` | `2026-02-06_e-23_e-24__snitt_eksisterende.md` |
| `E-25 - E-26_ Snitt planlagt.pdf` | `2026-02-06_e-25_e-26__snitt_planlagt.md` |

Samme konvensjon er brukt på nivået over: `2026-09-04 Fjordgata 30 - håndtering av hovedkonstruksjoner i underetasje.pdf` → `../2026-09-04_fjordgata_30_håndtering_av_hovedkonstruksjoner_i_underetasje.md`

---

## 3. Overlapp — 25 PDF-er vi hadde fra før

Disse ble **ikke** konvertert. Tekstlikhet 90–100 %.

| Kilde-PDF | Finnes allerede som |
|---|---|
| `26122001 Fjordgata 30_Brannkonsept bkl3 TEK17_160226.pdf` | `bakgrunn/2026-02-16_brannkonsept_bkl3_tek17.txt` |
| `26122001 Vedlegg A.pdf` | `bakgrunn/2026-02-16_brannkonsept_vedlegg_a.txt` |
| `2612200_BRFjordgata 30 - minilager_FIN.pdf` | `bakgrunn/2026-02-17_brannprosjektering_minilager.txt` |
| `2612200 FG30 Notat brannsikring i gjennomføringsfasen.pdf` | `bakgrunn/2026-02-26_notat_brannsikring_gjennomforingsfasen.txt` |
| `2612200 Sjekkliste Fjordgata 30_RIBr_Sign.pdf` | `bakgrunn/2026-02-02_sjekkliste_ribr.txt` |
| `B-01 Dispensasjonssøknad.pdf` | `bakgrunn/2026-01-26_dispensasjonssoknad.txt` |
| `F-01 Følgebrev_Nabovarsel.pdf` | `bakgrunn/2026-01-26_folgebrev_nabovarsel.txt` |
| `F-02 Følgebrev.pdf` | `bakgrunn/2026-02-09_folgebrev_rammesoknad.txt` |
| `F-04_Skred- og flomfare.pdf` | `bakgrunn/2023-07-06_rammesoknad_kontor_vedlegg_F.txt` |
| `F-05_Notat-VA-06022026.pdf` | `bakgrunn/2026-02-06_notat_va.txt` |
| `F-06_Notat El-kraft 10022026.pdf` | `bakgrunn/2026-02-10_notat_el-kraft.txt` |
| `F-07_Notat-Ventilasjon 10022026.pdf` | `bakgrunn/2026-02-09_notat_ventilasjon.txt` |
| `F-08 Notat_RiB 10022026.pdf` | `bakgrunn/2026-02-10_notat_rib.txt` |
| `I-01_Uttalelse riksantikvaren graving.pdf` | `bakgrunn/2023-06-28_uttalelse_riksantikvaren_graving.txt` |
| `I-02_Tilgjengelig slokkevann.pdf` | `bakgrunn/2023-06-15_notat_slokkevann.txt` |
| `I-03 ... Byantikvarens tilbake melding ....pdf` | `bakgrunn/2026-01-23_byantikvaren_tilbakemelding_endring_rammesoeknad.md` |
| `Innkreving av tvangsmulkt ... 01032026 - 18032026 ....pdf` | `bakgrunn/2026-03-19_1gangs_innkreving_tvangsmulkt.md` |
| `2 gangs innkreving ... 19032026 - 14042026 ....pdf` | `bakgrunn/2026-04-17_2gangs_innkreving_tvangsmulkt.md` |
| `3 gangs innkreving ... 15042026 - 26052026 ....pdf` | `bakgrunn/2026-06-03_3gangs_innkreving_tvangsmulkt.md` |
| `Vedtak om tvangsmulkt - Fjordgata 30 - 5001401149.pdf` | `bakgrunn/2025-05-07_vedtak_tvangsmulkt.md` |
| `Pålegg om brannsikring - Fjordgata 30 - 5001401149.pdf` | `bakgrunn/2024-11-08_paalegg_brannsikring.md` **(komplettert, se 4.5)** |
| `Tilsynsrapport - Fjordgata 30 - 5001401149.pdf` | `bakgrunn/2024-01-24_tilsynsrapport_tbrt.md` |
| `Redegjørelse til TBRT.pdf` | `bakgrunn/2026-02-26_redegjoerelse_tbrt.txt` |
| `2026-06-11_referat_statusmote_tbrt.pdf` | `referat/2026-06-11_referat_statusmote_tbrt.md` |
| `2026-06-18_tbrt_klage_innkrevinger_2026.pdf` | `leveranser/2026-06-17_tbrt_klage_innkrevinger_2026.md` |
| `D-01 Situasjonskart.pdf`, `D-02 Situasjonsplan.pdf` | tekstdelen finnes som `bakgrunn/2026-05-12_situasjonskart.txt` / `_situasjonsplan.txt`. Tegningene er likevel konvertert, siden tekstfilene ikke har bildene |

---

## 4. Ting du bør se på

### 4.1 Saksfremlegget er ikke et duplikat

Vi har `bakgrunn/2025-09-16_saksfremlegg_klageorgan_tbrt.txt` fra før. Den gjelder **klage på selve vedtaket** om tvangsmulkt, behandlet 30.09.2025.

Den nye gjelder **klage på innkrevingene**, behandlet 25.08.2026. To ulike saker. Begge skal beholdes.

### 4.2 Nabovarselet sier «Kontor og cafe»

Nabovarselet fra 26.01.2026 oppgir bruk som *«Kontor og cafe»*, og dispensasjonen gjelder *«cafevirksomhet i bygningens 1 etasje»*.

Dette er før konseptendringen til minilager. Ansvarsrettene fra februar samme år sier derimot *«Fjordgata 30 / Minilager»*. Naboene ble altså varslet om et annet formål enn det som ble søkt om.

### 4.3 TBRT går ikke inn i tre av seks anførsler

- **4.2 Faktafeil (2025 vs. 2026):** TBRT sier feilen «har ikke virket inn på resultatet». De bestrider ikke at feilen finnes.
- **4.3 Sprinkler krever byggetillatelse:** TBRT svarer ikke på det rettslige poenget. De svarer i stedet at vi har brukt lang tid.
- **4.4 Forskrift om brannforebygging § 6:** TBRT sier de har «fortløpende vurdert all dokumentasjon», men viser ikke at § 6 er drøftet.

### 4.4 Dobbelt vedlegg

`E-16 - E-22_Planer-planlagt.pdf` og `E-16 - E-22_ Planer planlagt.pdf` er samme tegningssett, sendt to ganger. 55 byte fra hverandre i størrelse. Bare den første er rendret og konvertert.

### 4.5 Pålegg-fila er komplettert

`bakgrunn/2024-11-08_paalegg_brannsikring.md` manglet teksten fra de to bildene på side 2 og 3. Den er nå fylt inn som blokksitat, med merknad om at den lå som bilde i originalen.

---

## 5. Status

Original-PDF-ene er tatt ut av repoet av EL etter gjennomgang. De er beviset i saken.

De uthentede tekstbildene er slettet etter at teksten var skrevet av og kontrollert: 6 skjermbilder fra saksfremlegget, 2 fra pålegget og 1 fra oppreisningsvedtaket. De kan hentes ut igjen fra PDF-ene med `pdfimages -png` ved behov.

Bildene som ligger igjen i `bilder/` er kun tegninger — 34 sider fra åtte tegnings-PDF-er.
