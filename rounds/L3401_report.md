# DCF L3401: Ladder-P passes blind (2 of 2). The proline-ending ladder sorts 5 of 5 fresh protists and separates oxygen-free from oxygen-breathing 3.5× (plain ladder 2.2×)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 13 November 2026

**Data:** `protists3.zip`, five UniProt reference proteomes, each a single taxon matching the pre-registration. *Plasmodium* has 5,172 proteins (record 5,361) and *Toxoplasma* 8,297 (8,307), probably from retired entries.

**Pre-registration:** `PREREGISTERED_L3397_ladderp.txt` (`e73ea5f4…a6ea`); script `dcf_ladderp_L3397.py` (`9fa53ce3…`, matches the ledger). Output committed (`68cd1935…92e3`) before grading.

---

## 1. Results
| organism | group (fixed in advance) | plain ladder (overlapping) | **Ladder-P** | call at 0.0017 |
|---|---|---|---|---|
| *Entamoeba invadens* | oxygen-free | 0.0094 | **0.0030** | ✓ |
| *Entamoeba dispar* | oxygen-free | 0.0074 | **0.0028** | ✓ |
| *Paramecium tetraurelia* | oxygen-breathing | 0.0025 | **0.0008** | ✓ |
| *Toxoplasma gondii* | oxygen-breathing | 0.0033 | **0.0006** | ✓ |
| *Plasmodium falciparum* | oxygen-breathing | 0.0027 | **0.0005** | ✓ |

| id | prediction | result | verdict |
|---|---|---|---|
| **LP1** | the 0.0017 cut sorts all 5 | **5 of 5** | **PASS** |
| **LP2** | Ladder-P separation (lowest anaerobe / highest aerobe) > plain | **3.5× vs 2.2×** | **PASS** |

## 2. Reading
- **The proline-ending ladder is now the validated eukaryote motif.** Requiring the C-P ending removes cysteine-rich look-alikes, so the oxygen-breathers drop to almost nothing (0.0005–0.0008) while the oxygen-free amoebae keep their real ferredoxin ladders.
- **The malaria and toxoplasmosis parasites read lowest of all.** Their only ferredoxin is the plant-type [2Fe-2S] in the apicoplast, which the ladder doesn't count.
- **Limitation:** both oxygen-free species are *Entamoeba*. A follow-up with anaerobes from other groups (oxymonads, *Mastigamoeba*) would make this stronger.
- **Manuscript v0.8** records the blind result.

## Record
**This round:** 2 graded, 2 passed.

**Total: 323 of 461 pre-registered predictions passed, plus 3 split.**

## Summary
- **The stricter, proline-ending iron ladder passed its blind test.** It sorted five new protists correctly: two oxygen-free amoebae above the cutoff, and *Paramecium* plus the malaria and toxoplasmosis parasites below it. It separated the groups more widely than the plain ladder (3.5× vs 2.2×).
- **For eukaryotes, Ladder-P is now the motif to use;** for bacteria and archaea, the plain ladder stays.

## Potential leads for future research
- **[More anaerobes]** Ladder-P on non-*Entamoeba* anaerobes, once verified UniProt sets are found.
- **[Scanner v2]** Add `ladder_p` and an overlapping `fd_ladder_ov` preset to the motif scanner and phone (new hashed versions).
- **[Venue]** The manuscript now has prokaryote and eukaryote blind results; choose a journal.
- **[Lineage map]**: carried.
