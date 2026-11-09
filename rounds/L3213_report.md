# DCF L3213: four blind tests on 14 genomes — 10 of 13 pass; hydrogen use alone does *not* raise the iron–sulfur reading (Note H revised); the start fix gains +2.2 points but misses one condition
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 9 November 2026

**Leads graded:** [Fe-rTCA] + [Fe-H2b] + [Sec-O revised] (L3189), [Fe-ferment H2] (L3197), [Sec-3] (L3197), [G-starts] (L3209).

**Data:** `blind_16.zip` (6 files) and `blind_17.zip` (8 files). All 14 were matched by LOCUS line and are complete. Renamed but the same strains:
- NC_009720 → *Xanthobacter versatilis* Py2;
- NC_003869 → *Caldanaerobacter subterraneus* subsp. *tengcongensis*;
- NC_014833 → *Hominimerdicola alba* 7 (= *Ruminococcus albus* 7).

**Tools:** all five SHA-256 values matched the frozen versions.

**Tool numbers** were written and hashed **before** any annotation was read: `tool_numbers.txt`, SHA-256 `1e911f73829ac507099541de66768eeb23c113473766353cdd054359bb71f645`.

---

## 1. Iron–sulfur density (label-free)
| group | genome | GC | CxxC per 1,000 aa | Sec codons |
|---|---|---|---|---|
| plasmid | *Cupriavidus* pHG1 | 0.62 | **0.90** | 0 |
| H2 fermenter | *Ruminococcus albus* 7 | 0.44 | **0.77** | 0 |
| rTCA green sulfur | *Chlorobaculum tepidum* | 0.57 | **0.69** | 0 |
| H2 fermenter | *Caldicellulosiruptor* | 0.35 | **0.66** | 0 |
| rTCA green sulfur | *Chlorobium chlorochromatii* | 0.44 | **0.61** | 0 |
| H2 fermenter | *Clostridium beijerinckii* | 0.30 | **0.60** | 0 |
| H2 fermenter | *Caldanaerobacter tengcongensis* | 0.38 | **0.56** | 3 |
| Calvin, non-H2 aerobe | *Nitrosospira multiformis* | 0.54 | 0.51 | 0 |
| Calvin, non-H2 aerobe | *Halothiobacillus* | 0.55 | 0.43 | 0 |
| **Calvin + H2 aerobe** | ***Xanthobacter* Py2** | 0.67 | **0.35** | **1** |
| lactic | *S. thermophilus* | 0.39 | 0.29 | 0 |
| lactic | *L. delbrueckii* | 0.50 | 0.27 | 0 |
| lactic | *P. pentosaceus* | 0.37 | 0.23 | 0 |
| lactic | *O. oeni* | 0.38 | 0.16 | 0 |

## 2. Grading
| id | prediction | result | verdict |
|---|---|---|---|
| G1 | both green sulfur > 0.50 | 0.69, 0.61 | **PASS** |
| G2 | both Calvin non-H2 aerobes < 0.50 | 0.43, **0.51** | **FAIL** |
| G3 | *Xanthobacter* > both Calvin non-H2 aerobes | 0.35 vs 0.43 and 0.51: **0 of 2** | **FAIL** |
| G4 | pHG1 > chr 1 (0.40) | **0.90** | **PASS** |
| G5 | 0 Sec in *Halothiobacillus*, *Nitrosospira* | 0, 0 | **PASS** |
| H1 | 4 H2 fermenters > 0.50 | 0.77, 0.66, 0.60, 0.56 | **PASS** |
| H2 | 4 lactic < 0.50 | 0.29, 0.27, 0.23, 0.16 | **PASS** |
| H3 | complete separation | 16 of 16 pairs, exact p = 1/70 = 0.014 | **PASS** |
| H4 | 0 Sec in lactic fermenters | 0 of 4 | **PASS** |
| S3a | filter keeps ≥ 90% of caught Sec sites (needs ≥ 5) | only 3 sites caught (all 3 kept) | **not graded** |
| S3b | median candidate cut ≥ 50% at GC < 0.45 | **52.3%** (8 genomes, 34–68%) | **PASS** |
| T1 | v2.32 candidate: mean exact-start gain ≥ +1.0 | **+2.2** (13 chromosomes) | **PASS** |
| T2 | no genome loses > 1.0 point of starts | none lost (+0.2 to +5.9) | **PASS** |
| T3 | found and correct move < 0.5 in every genome | found −0.6 (*Ruminococcus*), −0.5 (*Nitrosospira*) | **FAIL** |

## 3. What it means
**Hydrogen alone is not the driver [revises Note H].**
- *Xanthobacter* lives on H2 and oxygen, yet reads like an ordinary aerobe.
- *Cupriavidus* chromosome 1 was similar (0.40, L3185).
- The aerobic H2 user that read high, *Hydrogenobacter*, also runs the iron–sulfur-rich reductive TCA cycle, and so do the green sulfur bacteria, which read high without being H2-driven.

**What reads high across eight rounds is ferredoxin-based, low-potential metabolism:**
- the reductive TCA cycle;
- Wood–Ljungdahl acetogenesis;
- sulfate reduction;
- methanogenesis;
- **ferredoxin-dependent H2 production in fermenters.** The fermenter test passed cleanly: 4 of 4, complete separation.

Lactic fermenters, with no ferredoxin step in their energy metabolism, read lowest. This reading was formed after the results, so it is [D] until tested (lead [Fe-Fd]). Note H is now v0.3, retitled, with the hydrogen headline withdrawn.

**The 0.50 cut has a soft edge.** *Nitrosospira* read 0.51, failing G2 by 0.01.

**Selenocysteine.**
- *Xanthobacter* carries 1 Sec codon: a second aerobe with Sec, again an H2/formate user.
- *Caldanaerobacter* carries 3; the lactic fermenters carry none.

**The Sec-3 filter.**
- Too few Sec sites in these sets to grade its recall (S3a not graded).
- It cut false candidates by a median 52% in AT-rich genomes (S3b pass).
- In GC-rich *Xanthobacter* it went from 3,093 to 677 candidates: still too many.

**The start fix (v2.32 candidate).**
- **Starts:** blind gain **+2.2 points** (82.3% → 84.5%), with no genome losing starts. GC-rich genomes gained most: *Chlorobaculum* +5.9, *Chlorobium* +4.5, *Xanthobacter* +4.3, *Halothiobacillus* +4.0.
- **Genes found:** fell slightly (mean −0.2), and by 0.5–0.6 points in two genomes, which fails T3.
- **Decision:** following the frozen rule, **v2.32 is not released;** v2.31 stays the default until the found loss is understood (lead [G-starts c]).

**Prodigal on the same 13 chromosomes (same grader):**

| measure | v2.31 | v2.32c | Prodigal |
|---|---|---|---|
| found | 89.1% | 88.9% | 96.8% |
| **correct** | **97.1%** | **97.1%** | **97.3%** |
| exact starts | 82.3% | 84.5% | 88.4% |

DCF precision was equal to or above Prodigal's in **8 of 13** genomes.

**Genetic code:** all 14 called table 11 correctly. Code record **128 of 131**.

## Record
**This round:** 13 graded, 10 passed (G2, G3, T3 failed; S3a not graded).

**Total: 274 of 357 pre-registered predictions passed, plus 3 split.**

## Summary
- **The fermenter test passed cleanly.** Hydrogen-making fermenters read high and lactic fermenters low, with no overlap.
- **The hydrogen idea failed where it mattered.** A hydrogen-eating aerobe with the ordinary Calvin cycle reads low. The best reading now is that the iron–sulfur profile marks **ferredoxin-based, low-energy-potential metabolism**: the reductive TCA cycle, acetogens, sulfate reducers, methanogens and hydrogen-making fermenters. It does not mark oxygen, and it does not mark hydrogen use as such. Note H is revised to say so.
- **The start fix works** (+2.2 points of exact starts on 13 new genomes, up to +6 in GC-rich ones). It costs a little sensitivity in two genomes, just past the frozen limit, so it is not released yet.
- **Against Prodigal, precision stays level** (97.1% vs 97.3%).

## Potential leads for future research
- **[Fe-Fd]** Pre-register the ferredoxin reading on lineage-matched pairs, to separate metabolism from ancestry: e.g. a non-H2 Clostridium vs an H2-producing one, or rTCA vs Calvin autotrophs within one phylum.
- **[G-starts c]** Find which genes v2.32 loses (*Ruminococcus*, *Nitrosospira*), fix, and re-test blind.
- **[Sec-3b]** The GC-rich candidate flood (*Xanthobacter* 677 after filtering) needs a second filter.
- **[Sec-O]** *Xanthobacter* and *Hydrogenobacter*: aerobes with Sec are both H2/formate users. Pre-register "aerobes with Sec carry a formate dehydrogenase" on a fresh set.
- **[Fe-cut]** Report a grey zone (e.g. 0.45–0.55) rather than a single cut.
