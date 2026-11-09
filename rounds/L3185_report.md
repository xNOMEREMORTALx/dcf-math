# DCF L3185: [Fe-H2] complete — 5 of 5 pass; the iron–sulfur profile tracks hydrogen chemistry, even in oxygen-breathers
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 8 November 2026

**Lead pursued:** [Fe-H2 finish]. This round grades the four predictions held in L3181.

**Pre-registration:** `PREREGISTERED_L3177.txt`, SHA-256 `6cf5ef01…dc6e`, committed before any download.

**Data:** `blind_15.zip` held exactly the two files missing from blind_14:
- NC_013799 *Hydrogenobacter thermophilus* TK-6;
- NC_006814 *Lactobacillus acidophilus* NCFM.

Both were matched by LOCUS line and are complete. Tool hashes matched H3.

**Tool numbers** were hashed before the Sec annotation was read: `tool_numbers.txt`, SHA-256 `aa031ca2d76e679eb01b4f35cb768b80fc036b58018676bbc1216a014a8e4458`. (The L3181 numbers for the other eight are hashed `9a65c14e…ae4e`.)

**One procedural note:** the gene finder's own log prints an automatic found/correct line against the file's annotation. It does not touch the predictions or the CxxC count, but it is an annotation readout that appears before the hash. It was the same in L3181.


> **Correction (L3197).** The Sec counts in this report were made with `grep -c 'aa:Sec'`, which also counts the tRNA-Sec anticodon lines (`/anticodon=(…,aa:Sec,…)`). The true selenocysteine codons (`transl_except`) are: *Desulforapulum* **26** (not 27), *C. ljungdahlii* **9** (not 12), *A. woodii* **1** (not 2), *Hydrogenobacter* **1** (not 2; in formate dehydrogenase-N alpha). Every genome reported with 0 stays 0. **No verdict changes:** F5 needed ≥ 1 Sec codon in ≥ 2 of 3 H2-anaerobes and 0 in the fermenters, which still holds (3 of 3; 0 of 3).


> **Correction (L3205).** The gene-finding numbers in §4 came from the gene finder's built-in comparison line, not from `dcf_grade.py`. The graders differ. With `dcf_grade.py`: *Hydrogenobacter* found 93.0%, correct 99.2%, exact starts 81.1%; *L. acidophilus* found 90.7%, correct **98.6%** (not 93.3%), exact starts 88.7%. No prediction depended on these numbers.

---

## 1. All ten genomes
| group | genome | GC | CxxC per 1,000 aa | annotated Sec codons |
|---|---|---|---|---|
| H2-anaerobe | *Desulforapulum autotrophicum* (sulfate reducer) | 0.49 | **0.93** | 27 |
| **H2-aerobe** | ***Hydrogenobacter thermophilus*** | 0.44 | **0.86** | **2** |
| H2-anaerobe | *Acetobacterium woodii* (acetogen) | 0.39 | **0.82** | 2 |
| H2-anaerobe | *Clostridium ljungdahlii* (acetogen) | 0.31 | **0.77** | 12 |
| H2-aerobe | *Cupriavidus necator* H16 chr 1 | 0.66 | **0.40** | 0 |
| non-H2 aerobe | *Pseudomonas protegens* Pf-5 | 0.63 | 0.33 | 0 |
| non-H2 aerobe | *Bordetella bronchiseptica* | 0.68 | 0.32 | 0 |
| fermenter | *Streptococcus mutans* | 0.37 | 0.25 | 0 |
| fermenter | ***Lactobacillus acidophilus*** | 0.35 | **0.22** | 0 |
| fermenter | *Leuconostoc mesenteroides* | 0.38 | 0.14 | 0 |

**The ranking splits exactly at the group line:** all five hydrogen handlers sit above all five others.

## 2. Grading
| id | prediction | result | verdict |
|---|---|---|---|
| F1 | all 3 H2-anaerobes > 0.50 | 0.93, 0.82, 0.77 (L3181) | **PASS** (graded in L3181) |
| **F2** | all 3 fermenters < 0.50 | 0.25, 0.22, 0.14 | **PASS** |
| **F3** | both H2-aerobes above both non-H2 aerobes | 4 of 4 pairs (0.86 and 0.40 vs 0.33 and 0.32) | **PASS** |
| **F4** | 5 vs 5, one-sided Mann–Whitney p < 0.05 | U = 25 (complete separation), exact **p = 1/252 = 0.004** | **PASS** |
| **F5** | Sec in ≥ 2 of 3 H2-anaerobes; 0 in all 3 fermenters | 3 of 3; 0 of 3 | **PASS** (low novelty, declared) |

## 3. What it means, and what it doesn't
**The finding.**
- **The label-free iron–sulfur profile follows hydrogen handling.**
  - Oxygen-free hydrogen users read high.
  - Oxygen-free fermenters read low.
  - An oxygen-breathing hydrogen eater (*Hydrogenobacter*) reads as high as the anaerobes.
- **This completes the L3173 correction.** The measure is not an oxygen meter; it reads the Fe–S-heavy energy chemistry that hydrogen metabolism needs (hydrogenases, ferredoxins, formate dehydrogenases).

**The honest limits.**
- ***Hydrogenobacter* carries two confounds,** both declared in advance:
  - it fixes carbon by the reductive TCA cycle, which is itself Fe–S-rich;
  - it is a thermophile.

  F3 shows hydrogen-chemistry organisms read high. It does **not** yet show hydrogenases are the cause. That is lead [Fe-rTCA].
- ***Cupriavidus*'s margin is small** (0.40 vs 0.33), and its main hydrogenases were not in the file (they sit on megaplasmid pHG1). Alone it would not be convincing.
- **n = 5 per group.** The p-value is the smallest this design allows, but the groups are small and hand-chosen.

**A selenocysteine surprise (descriptive).** *Hydrogenobacter*, an oxygen-breathing organism, carries **2 annotated Sec codons**, in its formate dehydrogenase region, with a tRNA-Sec. Earlier rounds found aerobes with 0 Sec (L3145: aerobes 0 vs anaerobes 49). This is the first aerobe in the series with Sec, and it is a hydrogen and formate user. It suggests Sec follows the same Fe–S/formate chemistry rather than oxygen as such. **[Sec-O]** (obligate aerobes carry no Sec) now has a known exception to plan around.

## 4. Side results
- **Genetic code:** table 11 called correctly in 2 of 2. Code record **114 of 117**.
- **Gene finding:**
  - *Hydrogenobacter*: found 93.1%, correct 99.0%.
  - *L. acidophilus*: found 92.1%, correct 93.3%.

## Record
**This round:** 4 graded, 4 pass. **[Fe-H2] overall: 5 of 5.**

**Total: 261 of 338 pre-registered predictions passed, plus 3 split.**

## Summary
- **All five [Fe-H2] predictions passed.**
- **Iron–sulfur density, counted straight from raw DNA, tracks hydrogen metabolism.** Organisms that make or eat hydrogen read high; fermenters and ordinary oxygen-breathers read low.
- **The decisive case is *Hydrogenobacter*.** It breathes oxygen yet reads like an anaerobe, and it is the first aerobe in the series carrying selenocysteine.
- **The open question** is whether hydrogenases themselves cause the high reading, or the Fe–S-rich carbon fixation that usually comes with them.

## Potential leads for future research
- **[Fe-rTCA]** Split hydrogen from carbon fixation. Pre-register a blind set with:
  - non-hydrogen reductive-TCA users (e.g. green sulfur bacteria such as *Chlorobaculum tepidum*);
  - hydrogen users with the Calvin cycle;
  - plus controls.
- **[Fe-H2b]** Re-read *Cupriavidus* with megaplasmid pHG1 included, to measure how much its hydrogenase cluster adds.
- **[Sec-O revised]** Obligate aerobes **without** hydrogen or formate metabolism carry no Sec. Narrower and better motivated than the original [Sec-O].
- **[Fe-H2 note]** Write up L3117 → L3173 → L3185 as a short note: "an iron–sulfur signature of hydrogen metabolism, visible in raw genomes", with the failures (oxygen meter, Sec within anaerobes) kept in.
- **[R-floor]** Cysteine floor for R (*Leuconostoc* R = 32 at 0.21% cysteine).
- **[Seen-fix]** Rebuild the seen list by name and accession.
