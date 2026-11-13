# DCF L3365: the eukaryote cut passes blind (6 of 6); *Naegleria* fails the twist (2 of 3). The ladder measures how much of the proteome runs on ferredoxin, not whether any anaerobic enzyme is present
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 12 November 2026

**Data:** `protist2.zip`, seven UniProt reference proteomes, each a single taxon matching the pre-registration. *Cryptosporidium* (3,762) and *Leishmania* (7,845) are slightly smaller than the UniProt record lists (3,805 and 8,039), probably from retired entries.

**Pre-registration:** `PREREGISTERED_L3361_eukscale.txt` (`f0282f90…ffe4`). **Tool:** `dcf_motif_scan.py` (`7f8dd785…`, matches). The scan output was committed (`aabb259a…bef4`) before grading.

---

## 1. Results
| organism | group (fixed in advance) | ladder proteins | ladder /1000 aa | call at 0.0035 |
|---|---|---|---|---|
| *Blastocystis hominis* | anaerobe | 25 | **0.0171** | ✓ |
| *Spironucleus salmonicida* | anaerobe | 28 | **0.0151** | ✓ |
| *Cryptosporidium parvum* | anaerobe | 3 | **0.0036** | ✓ (by 0.0001) |
| *Trypanosoma brucei* | aerobe | 13 | 0.0030 | ✓ |
| *Chlamydomonas reinhardtii* | aerobe | 19 | 0.0016 | ✓ |
| *Leishmania major* | aerobe | 7 | 0.0014 | ✓ |
| ***Naegleria gruberi*** | special case | 11 | **0.0017** | — |

| id | prediction | result | verdict |
|---|---|---|---|
| **ES1** | cut classifies ≥ 5 of 6 | **6 of 6** | **PASS** |
| **ES2** | every anaerobe above every aerobe | 0.0036 > 0.0030 | **PASS** |
| ES3 | *Naegleria* ≥ 0.0035 | 0.0017 | **FAIL** |

## 2. What the ladder proteins are [after grading]
- ***Spironucleus*:** FeFe-hydrogenases 4 and 7, pyruvate-flavodoxin oxidoreductase 5, ferredoxins (including Fd3), nitroreductase–ferredoxin fusions. A full hydrogen-making toolkit.
- ***Blastocystis*:** 8 PFOR-type "pyruvate dehydrogenase (NADP⁺)", an iron hydrogenase, succinate dehydrogenase Fe–S subunits.
- ***Cryptosporidium*:** only 3. One is its PFOR-type PNO, and its small proteome carries the result.
- ***Naegleria*:** one iron hydrogenase and one anaerobic glycerol-3-phosphate dehydrogenase among **15,631** proteins, plus 7 uncharacterised and a DPYD.

## 3. Reading
- **The eukaryote cut works on new species.** Across 14 protists in two blind sets, oxygen-free and oxygen-breathing species separate perfectly (*Naegleria* aside).
- ***Naegleria* refines the lesson.** It has anaerobic enzymes, but only a token set in a large aerobic proteome, and the ladder correctly reads it as an aerobe.
- **What the ladder measures:** the **share** of the proteome given to ferredoxin-based energy metabolism, not the mere presence of an anaerobic gene. Labels "from enzymes" must therefore weigh how many, not just which.

The manuscript is updated to **v0.5**.

## Record
**This round:** 3 graded, 2 passed (ES1 and ES2 passed; ES3 failed).

**Total: 316 of 451 pre-registered predictions passed, plus 3 split.**

## Summary
- **The eukaryote cutoff passed on seven new protists.**
  - All six ordinary cases were sorted correctly. The fish parasite *Spironucleus* and the gut organism *Blastocystis* read high on their hydrogenases and PFOR; *Leishmania*, *Trypanosoma* and the alga *Chlamydomonas* read low.
  - *Cryptosporidium* scraped in by a hair.
- **The twist failed, and taught something.** *Naegleria* carries an iron hydrogenase, but it's one gene among 15,631, so it reads as the oxygen-breather it mostly is. The ladder measures how much of a cell's protein kit runs on ferredoxin, not whether any anaerobic gene is present.

## Potential leads for future research
- **[Quantity labels]** Turn the lesson into a rule: label genomes by the **number** of PFOR, hydrogenase and Rnf genes per 1,000 genes (from annotation, frozen before tool numbers). Use it for any future borderline test.
- **[Venue]** The manuscript now covers bacteria, archaea and eukaryotes, with every number audited for the prokaryote part. Choose a journal.
- **[Metagenome tier]** Community energy metabolism from metagenome assemblies (novel).
- **[Ladder-P]** The stricter C-P ending to remove eukaryote look-alikes.
