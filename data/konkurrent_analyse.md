# Konkurranseanalyse – Fjordgata 30 Minilager

*Generert av `scripts/analyse_konkurrentpriser.py`. Data: `data/konkurrent_priser.csv`.*

## Analysemetode

**FG30-boder:**
| Kategori | Størrelse | Antall |
|---|---|---|
| Micro | ~1,7 m² | 22 |
| Standard | ~2,1 m² | 432 |
| Medium+ | ~2,9 m² | 51 |

**Størrelsesvekting:** Gaussisk forfall sentrert på 2.1 m² (σ = 2.0 m²).
Enheter på 2,1 m² får vekt 1,0; vekten faller raskt med avstand fra FG30s typiske bodstørrelse.

| Størrelse (m²) | Gaussvekt |
|---|---|
| 1.0 | 0.860 |
| 1.7 | 0.980 |
| 2.1 | 1.000 |
| 2.9 | 0.923 |
| 4.0 | 0.637 |
| 5.0 | 0.350 |
| 7.0 | 0.050 |

**Arealkorreksjoner:**
- *Skrå tak* (skratak): Effektiv m² = m³ ÷ 2.4 m; vekt ganges med 0.6 (lavere brukervennlighet)
- *Høy takhøyde*: ingen korreksjon – ekstra høyde over TEK17-standard (2,4 m) gir ikke mer verdi
- *Visuelle estimater* (Extra Minilager): ingen vektstraf – usikkerhet i areal er ikke systematisk skjevhet

**Ekskludert fra analyse:**
- Gammelt Green Storage-datapunkt (1,5 m²/919 kr – inkonsistent, merket USIKKERT)
- Containere behandles separat (annen produkttype)

## Innendørs enheter – vektet kr/kvm/mnd

| Aktør | Vektet kr/kvm/mnd | Dp totalt | Dp med vekt > 5 % | Avstand sentrum | Merknad |
|---|---|---|---|---|---|
| ESP Lager | **133** | 7 | 4 | 12.0 km |  |
| Minilager1 | **249** | 6 | 4 | 9.0 km |  |
| Trondheim Minilager | **306** | 17 | 14 | 7.5 km |  |
| Green Storage | **365** | 4 | 4 | 3.5 km |  |
| Utleiebod | **365** | 8 | 6 | 1.2 km |  |
| Extra Minilager | **412** | 4 | 4 | 9.0 km | ⚠️ størrelse estimert fra bilde (±40 %) |

## Detaljer per aktør

### ESP Lager

| Bod | Eff. m² | Eff. kr/kvm/mnd | Størrelsesvekt | Typefaktor | Totalvekt | Korreksjon |
|---|---|---|---|---|---|---|
|  | 4.80 | 135 | 0.402 | 1.00 | 0.402 | – |
|  | 5.00 | 136 | 0.350 | 1.00 | 0.350 | – |
|  | 6.00 | 127 | 0.149 | 1.00 | 0.149 | – |
|  | 6.80 | 121 | 0.063 | 1.00 | 0.063 | – |
|  | 9.00 | 125 | 0.003 | 1.00 | 0.003 | – |
|  | 10.00 | 120 | 0.000 | 1.00 | 0.000 | – |
|  | 13.00 | 112 | 0.000 | 1.00 | 0.000 | – |

### Minilager1

| Bod | Eff. m² | Eff. kr/kvm/mnd | Størrelsesvekt | Typefaktor | Totalvekt | Korreksjon |
|---|---|---|---|---|---|---|
| Mini | 1.90 | 316 | 0.995 | 1.00 | 0.995 | – |
| Small | 2.10 | 238 | 1.000 | 1.00 | 1.000 | – |
| Medium | 4.40 | 159 | 0.516 | 1.00 | 0.516 | – |
| Large | 6.60 | 151 | 0.080 | 1.00 | 0.080 | – |
| XL | 8.80 | 148 | 0.004 | 1.00 | 0.004 | – |
| XXL | 16.00 | 93 | 0.000 | 1.00 | 0.000 | – |

### Trondheim Minilager

| Bod | Eff. m² | Eff. kr/kvm/mnd | Størrelsesvekt | Typefaktor | Totalvekt | Korreksjon |
|---|---|---|---|---|---|---|
| bod-808 | 1.79 | 352 | 0.988 | 0.60 | 0.593 | skratak → 1.8 m² eff. (4.3 m³ ÷ 2.4 m) |
| bod-728 | 1.83 | 344 | 0.991 | 0.60 | 0.595 | skratak → 1.8 m² eff. (4.4 m³ ÷ 2.4 m) |
| bod-736 | 1.90 | 332 | 0.995 | 1.00 | 0.995 | – |
| bod-841 | 1.90 | 332 | 0.995 | 1.00 | 0.995 | – |
| bod-827 | 2.10 | 333 | 1.000 | 1.00 | 1.000 | – |
| bod-713 | 2.21 | 317 | 0.999 | 0.60 | 0.599 | skratak → 2.2 m² eff. (5.3 m³ ÷ 2.4 m) |
| bod-819 | 2.46 | 297 | 0.984 | 0.60 | 0.590 | skratak → 2.5 m² eff. (5.9 m³ ÷ 2.4 m) |
| bod-417 | 2.90 | 279 | 0.923 | 1.00 | 0.923 | – |
| bod-48 | 3.00 | 280 | 0.904 | 1.00 | 0.904 | – |
| bod-51 | 3.10 | 277 | 0.882 | 1.00 | 0.882 | – |
| bod-46 | 3.20 | 275 | 0.860 | 1.00 | 0.860 | – |
| bod-9 | 5.70 | 261 | 0.198 | 1.00 | 0.198 | – |
| bod-335 | 6.10 | 251 | 0.135 | 1.00 | 0.135 | – |
| bod-114 | 6.50 | 251 | 0.089 | 1.00 | 0.089 | – |
| bod-1043 | 7.00 | 214 | 0.050 | 1.00 | 0.050 | – |
| bod-1047 | 7.20 | 224 | 0.039 | 1.00 | 0.039 | – |
| bod-21 | 7.40 | 220 | 0.030 | 1.00 | 0.030 | – |

### Green Storage

| Bod | Eff. m² | Eff. kr/kvm/mnd | Størrelsesvekt | Typefaktor | Totalvekt | Korreksjon |
|---|---|---|---|---|---|---|
| 1m2 | 1.00 | 438 | 0.860 | 1.00 | 0.860 | – |
| 3m2 | 3.00 | 399 | 0.904 | 1.00 | 0.904 | – |
| 4m2 | 4.00 | 297 | 0.637 | 1.00 | 0.637 | – |
| 5m2 | 5.00 | 218 | 0.350 | 1.00 | 0.350 | – |

### Utleiebod

| Bod | Eff. m² | Eff. kr/kvm/mnd | Størrelsesvekt | Typefaktor | Totalvekt | Korreksjon |
|---|---|---|---|---|---|---|
| 1m2 | 1.00 | 399 | 0.860 | 1.00 | 0.860 | – |
| 2m2 | 2.00 | 369 | 0.999 | 1.00 | 0.999 | – |
| 3m2 | 3.00 | 369 | 0.904 | 1.00 | 0.904 | – |
| 4m2 | 4.00 | 339 | 0.637 | 1.00 | 0.637 | – |
| 5m2 | 5.00 | 339 | 0.350 | 1.00 | 0.350 | – |
| 6m2 | 6.00 | 286 | 0.149 | 1.00 | 0.149 | – |
| 8m2 | 8.00 | 305 | 0.013 | 1.00 | 0.013 | – |
| 10m2 | 10.00 | 300 | 0.000 | 1.00 | 0.000 | – |

### Extra Minilager

| Bod | Eff. m² | Eff. kr/kvm/mnd | Størrelsesvekt | Typefaktor | Totalvekt | Korreksjon |
|---|---|---|---|---|---|---|
| Bod 9 | 1.70 | 424 | 0.980 | 1.00 | 0.980 | – |
| Bod 7 | 2.00 | 390 | 0.999 | 1.00 | 0.999 | – |
| Bod 14 | 2.20 | 459 | 0.999 | 1.00 | 0.999 | – |
| Bod 30 | 2.70 | 374 | 0.956 | 1.00 | 0.956 | – |

## Containere (separat analyse)

Utemperert drive-in-container – ikke direkte sammenlignbart med FG30s innendørs boder.

| Aktør | Størrelse (m²) | Kr/kvm/mnd | Kilde |
|---|---|---|---|
| 123 Minilager | 4.7 | 296 | webfetch_prisliste |
| 123 Minilager | 4.8 | 310 | copy_paste_prosjektleder |
| 123 Minilager | 6.5 | 245 | copy_paste_prosjektleder |
| 123 Minilager | 13.9 | 158 | copy_paste_prosjektleder |

## Konklusjon

Aktører med periferi-lokasjon (>5 km) konkurrerer ikke med FG30 på sentralitet, men definerer markedets prisgulv for sammenlignbare enheter.
