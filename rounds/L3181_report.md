# DCF L3181: [Fe-H2] blind — hydrogen handlers read high, fermenters and ordinary aerobes read low; F1 passes, four predictions wait on two missing files
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 8 November 2026

**Lead pursued:** [Fe-H2], pre-registered in L3177 (`PREREGISTERED_L3177.txt`, SHA-256 `6cf5ef01…dc6e`, committed before download).

**Data:** `blind_14.zip` held **8 of the 10** pre-registered genomes. Every file was matched by its LOCUS line and is complete (one record, ends with `//`).
- **Missing:** NC_013799 *Hydrogenobacter thermophilus* and NC_006814 *Lactobacillus acidophilus*.
- **Name update:** NC_012108 is now annotated as *Desulforapulum autotrophicum* HRM2 (same strain, renamed genus).

**Tool numbers** were written and hashed **before** any annotation was read: `tool_numbers.txt`, SHA-256 `9a65c14e594561b545288541770d046d34a6a50f933683946676aa358a68ae4e`. All six tool hashes matched H3.


> **Correction (L3197).** The Sec counts in this report were made with `grep -c 'aa:Sec'`, which also counts the tRNA-Sec anticodon lines (`/anticodon=(…,aa:Sec,…)`). The true selenocysteine codons (`transl_except`) are: *Desulforapulum* **26** (not 27), *C. ljungdahlii* **9** (not 12), *A. woodii* **1** (not 2), *Hydrogenobacter* **1** (not 2; in formate dehydrogenase-N alpha). Every genome reported with 0 stays 0. **No verdict changes:** F5 needed ≥ 1 Sec codon in ≥ 2 of 3 H2-anaerobes and 0 in the fermenters, which still holds (3 of 3; 0 of 3).

---

## 1. Iron–sulfur density, label-free
| group | genome | GC | CxxC per 1,000 aa | R | annotated Sec codons |
|---|---|---|---|---|---|
| H2-anaerobe | *Desulforapulum autotrophicum* (sulfate reducer) | 0.49 | **0.93** | 5.6 | 27 |
| H2-anaerobe | *Acetobacterium woodii* (acetogen) | 0.39 | **0.82** | 5.3 | 2 |
| H2-anaerobe | *Clostridium ljungdahlii* (acetogen) | 0.31 | **0.77** | 4.1 | 12 |
| H2-aerobe | *Cupriavidus necator* H16 chr 1 | 0.66 | **0.40** | 4.7 | 0 |
| H2-aerobe | *Hydrogenobacter thermophilus* | — | *file missing* | — | — |
| non-H2 aerobe | *Pseudomonas protegens* Pf-5 | 0.63 | 0.33 | 3.1 | 0 |
| non-H2 aerobe | *Bordetella bronchiseptica* RB50 | 0.68 | 0.32 | 3.7 | 0 |
| fermenter | *Streptococcus mutans* UA159 | 0.37 | 0.25 | 8.6 | 0 |
| fermenter | *Leuconostoc mesenteroides* | 0.38 | **0.14** | 32.2 | 0 |
| fermenter | *Lactobacillus acidophilus* | — | *file missing* | — | — |

**Reading.**
- **The eight genomes split cleanly by energy chemistry.** Every hydrogen handler (0.40–0.93) is above every non-handler (0.14–0.33). The lactic fermenters are lowest of all.
- ***Cupriavidus* sits above both ordinary aerobes** (0.40 vs 0.32/0.33) even though its main hydrogenases are on the megaplasmid, which was not in the file. The gap is small, so it waits for *Hydrogenobacter* before it means much.
- ***Leuconostoc*'s R of 32 is an artefact of very low cysteine** (0.21% of residues): R divides by the expected count, which is tiny. Density is the robust measure, as frozen.

## 2. Grading
| id | prediction | result | verdict |
|---|---|---|---|
| **F1** | all 3 H2-anaerobes > 0.50 | 0.93, 0.82, 0.77 | **PASS** |
| F2 | all 3 fermenters < 0.50 | 2 of 2 received (0.25, 0.14) | **PENDING** (needs *L. acidophilus*) |
| F3 | both H2-aerobes above both non-H2 aerobes (4/4 pairs) | 2 of 2 pairs received | **PENDING** (needs *Hydrogenobacter*) |
| F4 | 5 vs 5 Mann–Whitney p < 0.05 | 4 vs 4 so far: complete separation, exact p = 1/70 = 0.014 | **PENDING** |
| F5 | Sec in ≥ 2 of 3 H2-anaerobes; 0 in all 3 fermenters | 3 of 3 carry Sec; 0 in 2 of 2 fermenters | **PENDING** (needs *L. acidophilus*) |

**Why pending rather than graded:** each of F2–F5 was frozen on the full set. Grading them on a subset would change the test after the data arrived. They are graded when the two missing files come in; the current partial results above are not counted.

**Selenocysteine detail (descriptive).** The Sec genes are dominated by Fe–S redox proteins (4Fe-4S dicluster proteins, ferredoxin, a NiFeSe hydrogenase maturation protease in *Desulforapulum*), consistent with Sec riding on anaerobic Fe–S energy chemistry.

## 3. Side results (routine)
- **Genetic code:** table 11 called in **8 of 8**, all correct. Code record **112 of 115**.
- **Gene finding:** found 86.0–95.3%, correct 95.5–99.1%, exact starts 79.0–91.0%. GC-rich *Bordetella* (0.68) reached 79% exact starts, above the 72–76% usually seen at GC ≥ 0.65.

## Record
**This round:** 1 graded, 1 pass; 4 pending.

**Total: 257 of 334 pre-registered predictions passed, plus 3 split.**

## Summary
- **Hydrogen chemistry, not oxygen, lines up with the iron–sulfur profile.** In the 8 genomes received, every hydrogen-using organism reads above every fermenter and ordinary aerobe. The two acetogens and the sulfate reducer clear the frozen 0.50 cut (F1 passes).
- **Lactic fermenters read lowest of all,** supporting the L3173 correction that the profile measures Fe–S energy metabolism.
- **The hydrogen-eating aerobe *Cupriavidus* edges above the ordinary aerobes,** but the decisive comparison needs *Hydrogenobacter*.
- **Two files were missing from the zip,** so four predictions are held, not graded.

## Potential leads for future research
- **[Fe-H2 finish]** Gary: download the two missing files, zip as **`blind_14b.zip`**:
  - https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NC_013799&rettype=gbwithparts&retmode=text
  - https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NC_006814&rettype=gbwithparts&retmode=text
- **[Fe-H2b]** Add *Cupriavidus* megaplasmid pHG1 to see how much its hydrogenase cluster moves the reading.
- **[Fe-rTCA]** Separate hydrogen use from the reductive TCA cycle in Aquificae.
- **[R-floor]** R becomes unstable when cysteine is below ~0.3%; add a cysteine floor or report density only for such genomes.
- **[Seen-fix]** Rebuild the seen list by name and accession (*L. plantarum* gap from L3177).
- **[Fe-ferment]** Next in the H5 path once F2 is graded.
