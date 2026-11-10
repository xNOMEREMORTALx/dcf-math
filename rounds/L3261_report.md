# DCF L3261: 11,723 human mRNAs — no new iron hairpins beyond chance once each gene is counted once; the metal numbers stay null in RNA (replicated); and a repeated 7-nucleotide family of rhythms (14, 21, 28, 42) appears in human coding sequence
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 9 November 2026

**Leads:** [IRE-wide], [Metal-mRNA] (pre-registered L3253), replication on a sealed second file (L3261).

**Data.** Gary's `human_rna_1_and_2.zip` held NCBI RefSeq `human.1.rna.fna.gz` (SHA-256 `a9ce8e63…8410`) and `human.2.rna.fna.gz` (`452ea6a0…7cb0`).
- **File 1:** 2,114 protein-coding mRNAs (NM_), plus 15,389 non-coding RNAs (NR_) excluded by the frozen rule.
- **File 2:** 9,609 NM_ mRNAs. It was sealed, read-only and unopened, until file 1 was graded.

**Pre-registrations, in order:**
1. `PREREGISTERED_L3253_mRNA.txt` (`54fa43b0…`), file 1.
2. `PREREGISTERED_L3261_rep.txt` (`ca8257b6…`), the file-2 rule, frozen before file 1's results.
3. `PREREGISTERED_L3261_rep_amend.txt` (`5d5f7fd8…`), frozen after file 1 but **before file 2 was unsealed**.

**A bug, fixed in the open.** The frozen script crashed in its *shuffled control* on file 1 before printing any result: the two-letter shuffle gave up after 50 tries. It was fixed, tested on 20,000 synthetic sequences with 0 failures, and logged in the ledger as v1.1 (`05c1b061…`) **before** the rerun. The scan, statistics and thresholds were unchanged.

---

## 1. Iron-responsive elements across human mRNA
| set | 5′ UTR hairpins, real | shuffled (2-letter-preserving) | ratio |
|---|---|---|---|
| file 1, as frozen | 4 | 6.2 | 0.65 |
| file 2, as frozen | 44 | 23.2 | 1.90 |
| file 2, distinct UTRs only [exploratory] | 34 | 17.7 | 1.92 |
| **file 2, one transcript per gene** [exploratory] | **8** | **9.5** | **0.84** |
| **file 1, one transcript per gene** [exploratory] | **2** | **1.9** | **1.05** |

| id | prediction | result | verdict |
|---|---|---|---|
| W1 | file 1: real 5′ hits ≥ 2× shuffled | 0.65× | **FAIL** |
| W2 | known IRE genes in file 1 detected | none of FTH1, FTL, TFRC, ALAS2, ACO2, SLC40A1 is in file 1 | **not graded** |
| RW1 | file 2: real 5′ hits ≥ 2× shuffled | 1.90× | **FAIL** |

**The lesson: pseudo-replication.**
- File 2's apparent excess came from **the same 5′ UTR counted many times**, once per transcript variant: ACBD5 14 times, ADAM29 6, ANKRD6 5, ZNF331 5.
- Each variant's shuffle is an independent draw, but the real hairpins are copies. **One transcript per gene removes the excess entirely** (8 real vs 9.5 shuffled).
- **So, outside the known iron genes, the scanner's hits occur at the chance rate.** No new IRE candidate is supported.
- The 8 genes hit (ADAM29, ADGRB3, ANKRD6, NUPR1, NUTM1, NWD2, RASD2, SERPINB10) are listed for completeness only. NUPR1 is noted because it has been linked to ferroptosis in the literature (not checked this round).

**What stands.** The scanner recognises the real iron switch (L3249: 6 of 7 known, 0 of 8 controls). A genome-wide discovery would need a stronger signal than the IRE shape alone: conservation across species, or a second structure model.

## 2. Metal numbers in human RNA
**File 1, as frozen (W3).** Three metal periods had their 99.83% interval entirely above 1: coding 30 (Fe neutrons, Zn protons), coding 56 (Fe mass number) and UTR 20 (Ca, K). **W3 therefore FAILS as written.**

**But the interval was wrong.** A calibration on **78 non-metal periods** put 11 outside it (5 above, 6 below), against about 0.13 expected. Windows of joined mRNAs are not independent, and protein structure adds real rhythms. The rule was amended for file 2 **before unsealing**: compare each metal period with the 39 non-metal periods of the same file.

| id | prediction (file 2) | result | verdict |
|---|---|---|---|
| **RW3a** | coding 30, coding 56, UTR 20 do **not** replicate above the non-metal 95th percentile | 1.007, 1.006, 1.022, against cut-offs 1.290 / 1.036 | **PASS** (null) |
| **RW3b** | ≤ 4 of the 30 metal tests above the non-metal 95th percentile | **0 of 30** | **PASS** (null) |

**Reading.** In 9,609 human mRNAs, **none** of the body metals' proton, neutron or mass numbers stands out against ordinary periods. File 1's three "positives" did not replicate: they were noise from a miscalibrated interval. With the DNA test (L3253), the metal numbers are now null in DNA **and** RNA.

## 3. An unexpected pattern: rhythms at multiples of 7 nucleotides [exploratory, replicated, not yet tested]
Among the **non-metal** periods, human coding sequence shows the same peaks in both files:

| period (nt) | file 1 | file 2 |
|---|---|---|
| **14** | 1.19 | **1.74** |
| **21** (= 7 codons, the coiled-coil heptad) | 1.32 | **1.45** |
| **28** | 1.21 | **1.23** |
| **42** | — (not above interval) | **1.27** |

**Reading [D].**
- **21 nt = 7 amino acids** is the heptad repeat of coiled-coil proteins, a known protein rhythm.
- **14 and 28 do not follow simply from the heptad** in codon coordinates, so their origin is open.
- **This was found after looking, not predicted.** It must be pre-registered and tested on fresh data (human RNA files 3–18, or another species) before it counts.

## Record
**This round:** 5 graded, 2 passed (W1, W3 and RW1 failed; RW3a and RW3b passed; W2 not graded).

**Total: 291 of 411 pre-registered predictions passed, plus 3 split.**

## Summary
- **No hidden iron switches turned up in 11,723 human mRNAs.** An apparent excess of iron-like hairpins in the second file came from counting the same gene's message many times. Counted once per gene, the hits match chance. The scanner still recognises the known iron switch; finding new ones needs more evidence than shape alone.
- **The metal numbers are null in RNA too.** Three "hits" in the first file were noise from error bars that were too narrow (the same bars flagged 11 of 78 ordinary periods), and none came back in the second file. Proton, neutron and mass numbers of the body's metals have now failed in proteins, DNA and RNA.
- **Two methodological lessons were caught and fixed in the open:** a shuffle bug (fixed and logged before rerunning) and the variant double-counting.
- **A genuinely unexpected, replicated pattern:** human coding sequence carries extra rhythm at 14, 21, 28 and 42 nucleotides, all multiples of 7. It is next for a proper pre-registered test.

## Potential leads for future research
- **[Seven-rhythm]** Pre-register: in a fresh human RNA file (e.g. `human.3.rna.fna.gz`, 6.3 MB), coding periods 7, 14, 21, 28, 35 and 42 exceed the 95th percentile of the non-multiple-of-7 periods (8–62), with a one-transcript-per-gene rule. Also test a second species, to see whether it is human-specific.
- **[Seven-cause]** If it holds: per-protein spectra to find which protein families carry it (coiled coils, collagen-like Gly-X-Y? Note: Gly-X-Y is period 9 nt, which is not a multiple of 7, so a clean contrast).
- **[IRE-conserve]** For any future IRE candidate: require the hairpin in the mouse orthologue's mRNA (pre-registered).
- **[Redox-age b]**, **[Fe-ladder note]**, **[Lit-redox]** carried.
- **[Method note]** Add the two lessons (variant pseudo-replication; window-bootstrap miscalibration) to `methodology` in INTEGRATION.md.
