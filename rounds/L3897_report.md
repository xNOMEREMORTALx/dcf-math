# DCF L3897: in the same cells, the potassium-channel excess shows up in CTCF ChIA-PET loops but not in Hi-C loops (1 of 3)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 20 November 2026

**Files:**
- **Pre-registration:** `PREREGISTERED_L3897_assay_split.txt`, hashed in the LEDGER before either split was run.
- **Script:** `rounds/dcf_assay_L3897.py`. It uses the L3877 method: genes matched for length and local density, H1 and HFFc6 scored together, 10,000 sets, seed 3897.
- **Outputs:** `L3897_tool_output_HIC.txt` and `_CHIA.txt`, committed before grading.
- **Grading:** `L3897_grade_output.txt`.

**Not blind.** H1 and HFFc6 were used before. The data are the 4DN union loop files, split by the method tag in column 7.

---

## Results
| # | prediction | result |
|---|---|---|
| A1 | CTCF ChIA-PET loops: K+ channels p_upper < 0.05 | **PASS**, p = 0.022 |
| A2 | Hi-C loops: K+ channels p_upper < 0.05 | **FAIL**, p = 0.56 |
| A3 | Hi-C loops: all 139 genes p_upper < 0.05 | **FAIL**, p = 0.77 |

**1 of 3 passed.** The failures stand.

| loop set | loops (H1 / HFFc6) | K+ (96) | pore K+ (79) | all (139) | K+ auxiliary (17) |
|---|---|---|---|---|---|
| CTCF ChIA-PET | 28,270 / 24,421 | 0.313 vs 0.233, **p 0.022** | 0.329 vs 0.236, **p 0.015** | 0.320 vs 0.236, **p 0.006** | 0.235 vs 0.227, p 0.51 |
| Hi-C | 39,509 / 50,732 | 0.453 vs 0.456, p 0.56 | 0.475 vs 0.455, p 0.35 | 0.439 vs 0.463, p 0.77 | 0.353 vs 0.461, p 0.89 |

Each cell gives the family share, then the matched-gene null mean, then p_upper.

## What it means
**The pre-registered reading (A1 passes, A2 fails):** Hi-C is less sensitive in these cells. That cannot explain the Hi-C positives elsewhere, because motor neurons, astrocytes and colon all showed the excess in Hi-C.

**A likely reason (descriptive, not tested):**
- **Hi-C anchors are coarse.** The median Hi-C anchor in H1 is 5,000 bp wide; the median ChIA-PET anchor is 1,070 bp.
- **Coarse anchors catch almost half of all genes.** The matched-gene baseline is 0.46 with Hi-C loops and 0.23 with ChIA-PET loops.
- **So the comparison has little room** to show a family standing out.

**What changes:**
- **"The assay creates the excess" is not supported.** In the same cells, the CTCF-focused assay shows it and the coarser one does not.
- **The primary-cell ChIA-PET "no" results (T cells, HUVEC, HMEC) look more like real cell differences.** ChIA-PET found the excess in H1 and HFFc6, so the method can detect it.
- **The Hi-C positives remain real results,** but the two assays do not measure the same thing at the same resolution.

**Auxiliary K+ subunits are again never above matched genes.** That fits the pore-only pattern.

## Record
- **+1 passed, 2 failed:** 589 of 814.
- **Audit:** 256 of 341 (entry "assay split, H1 HFFc6").

## Summary
- **In H1 and HFFc6, the pore-forming K+ excess appears in CTCF ChIA-PET loops (p = 0.015–0.022) and not in Hi-C loops.**
- **Hi-C anchors are about five times wider,** and the baseline doubles, so Hi-C likely blurs the signal.
- **Assay alone does not create the excess,** and the primary-cell ChIA-PET negatives now look more like real cell-type differences.

## Potential leads for future research
- **[Resolution-matched Hi-C]** Pre-register a rerun with Hi-C anchors trimmed to their central 1 kb (or Micro-C loops, also in the 4DN files: H1 50,273, HFFc6 79,625). If the excess returns, resolution was the issue.
- **[Micro-C]** Micro-C is high-resolution like ChIA-PET but needs no CTCF pull-down. It is a clean third assay in the same two cells.
- **[Same cells, two assays]** HUVEC/HMEC Hi-C with released loops would test whether the primary-cell negatives are cell-type or assay effects.
- **[Manuscript 3]** v1.6: add §3.16 assay split, and revise the conclusion so the assay confound is stated as partly answered.
