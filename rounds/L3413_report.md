# DCF L3413: a second Ladder-P blind test frozen, with oxygen-free protists from three groups outside *Entamoeba*
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 13 November 2026

**Lead:** [More anaerobes]. **Pre-registration:** `PREREGISTERED_L3413_ladderp_b.txt` (`bbe56b2e…`), pushed before download. Same frozen script and cut as L3397.

---

## Why
Ladder-P passed 5 of 5 (L3401), but both oxygen-free species were *Entamoeba*. This test uses three oxygen-free lineages that have never been tested, so the result can't rest on one genus.

| group | proteome (UniProt) | lineage |
|---|---|---|
| oxygen-free | *Giardia muris* (UP000315496) | diplomonad |
| oxygen-free | *Tritrichomonas foetus* (UP000179807) | parabasalid |
| oxygen-free | *Paratrimastix pyriformis* (UP001141327) | preaxostylan (oxymonad relative) |
| oxygen-breathing | *Acanthamoeba castellanii* (UP000011083) | amoebozoan |
| oxygen-breathing | *Naegleria fowleri* (UP000444721) | heterolobosean; its relative carried a token anaerobic toolkit and still read aerobic |

| id | prediction |
|---|---|
| LB1 | the 0.0017 cut classifies ≥ 4 of 5 correctly |
| LB2 | every oxygen-free protist reads above every oxygen-breather |

**Declared risks:**
- *Tritrichomonas* has a large proteome, and its relative *Trichomonas* sat near the cut (0.0020);
- the *Paratrimastix* set may not be a reference proteome.

## Action for Gary: 5 downloads
Zip as **`protists4.zip`** (files save as `stream (n).gz`; pick the 5 newest):
1. *Giardia muris*: https://rest.uniprot.org/uniprotkb/stream?format=fasta&compressed=true&query=proteome:UP000315496
2. *Tritrichomonas foetus*: https://rest.uniprot.org/uniprotkb/stream?format=fasta&compressed=true&query=proteome:UP000179807
3. *Paratrimastix pyriformis*: https://rest.uniprot.org/uniprotkb/stream?format=fasta&compressed=true&query=proteome:UP001141327
4. *Acanthamoeba castellanii*: https://rest.uniprot.org/uniprotkb/stream?format=fasta&compressed=true&query=proteome:UP000011083
5. *Naegleria fowleri*: https://rest.uniprot.org/uniprotkb/stream?format=fasta&compressed=true&query=proteome:UP000444721

## Record
No predictions graded. **323 of 461 passed, plus 3 split.**

## Summary
- **The proline-ending ladder gets a harder second test:** oxygen-free protists from three different groups, none of them *Entamoeba*, against two oxygen-breathing amoebae. One of the oxygen-breathers is a deliberate trap, a relative of the *Naegleria* that carries a few anaerobic enzymes.

## Potential leads for future research
- **[Ladder-P b]** Grade LB1–LB2 when `protists4.zip` arrives.
- **[Send enquiry]**, **[Zenodo]**, **[Outside reader]**: Gary's steps, carried.
