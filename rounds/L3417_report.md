# DCF L3417: Ladder-P passes its second blind test (2 of 2). Oxygen-free protists from three new lineages sort correctly, and the *Naegleria* trap reads as an oxygen-breather; 10 of 10 across both sets
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 13 November 2026

**Data:** `protists4`, five UniProt proteomes, each a single taxon, with protein counts exactly as frozen.

**Pre-registration:** `PREREGISTERED_L3413_ladderp_b.txt` (`bbe56b2e…`); script `dcf_ladderp_L3397.py` (`9fa53ce3…`, unchanged). Output committed (`3247c1de…f739`) before grading.

---

## 1. Results
| organism | lineage | side (fixed in advance) | plain ladder | **Ladder-P** | call at 0.0017 |
|---|---|---|---|---|---|
| *Paratrimastix pyriformis* | preaxostylan | oxygen-free | 0.0108 | **0.0070** | ✓ |
| *Giardia muris* | diplomonad | oxygen-free | 0.0068 | **0.0042** | ✓ |
| *Tritrichomonas foetus* | parabasalid | oxygen-free | 0.0060 | **0.0025** | ✓ |
| *Acanthamoeba castellanii* | amoebozoan | oxygen-breathing | 0.0029 | **0.0012** | ✓ |
| *Naegleria fowleri* | heterolobosean (trap) | oxygen-breathing | 0.0019 | **0.0004** | ✓ |

| id | prediction | result | verdict |
|---|---|---|---|
| **LB1** | ≥ 4 of 5 correct at 0.0017 | **5 of 5** | **PASS** |
| **LB2** | every oxygen-free above every oxygen-breather | 0.0025 > 0.0012 | **PASS** |

## 2. Reading
- **The *Entamoeba* limitation is removed.** Oxygen-free protists from three further lineages sort above the cut. Across both Ladder-P blind sets the result is **10 of 10**, with oxygen-free species from four lineages: *Entamoeba*, diplomonads, parabasalids and preaxostylans.
- **The trap worked as predicted.** *Naegleria fowleri*, whose relative carries a token anaerobic toolkit, reads 0.0004, the lowest of all. That confirms the ladder measures how much of the proteome serves ferredoxin metabolism.
- ***Tritrichomonas*, with its large proteome, reads lowest of the oxygen-free group (0.0025),** like its relative *Trichomonas*, but still twice the highest oxygen-breather.
- **Manuscript v0.10:** the eukaryote section and the abstract now report 10 of 10; the limitations list 24 protists in all.

## Record
**This round:** 2 graded, 2 passed.

**Total: 325 of 463 pre-registered predictions passed, plus 3 split.**

## Summary
- **The proline-ending ladder passed again, 5 of 5.** This time the oxygen-free protists came from three new groups (*Paratrimastix*, *Giardia muris*, *Tritrichomonas*), and the trap *Naegleria fowleri* read lowest of all, as predicted.
- **Across both blind tests Ladder-P is now 10 for 10,** so the eukaryote result no longer rests on one genus. The manuscript is at v0.10.

## Potential leads for future research
- **[Send enquiry]**, **[Zenodo]**, **[Outside reader]**: Gary's steps toward submission.
- **[Figure 4]** One figure of all 24 protists (two motifs, the cuts, the lineages).
- **[Lineage map]** Endonuclease III cluster loss across Lactobacillaceae (needs genomes).
