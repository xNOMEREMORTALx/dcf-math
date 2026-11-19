# DCF L3849: the gene-family pattern at CTCF loop anchors holds blind in four more cell types (4 of 4). Across ten cell types: K⁺ channels above baseline in 10, NMDA receptors in 9, Ca²⁺ pores below in 10
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 19 November 2026

**Files:**
- **Pre-registration:** `PREREGISTERED_L3849_ctcf_family.txt`.
- **Note:** `NOTE_L3849_files.txt`, the file maps from Gary's screenshots, recorded before download.
- **Script:** `rounds/dcf_ctcf_neural_L3825a.py`, unchanged.
- **Grader:** `rounds/dcf_grade_L3849.py`.
- **Outputs:** `rounds/L3849_tool_output_{HEK293,MCF10A,BJ,RWPE1}.txt`, each committed unread, before grading.
- **Grading:** `rounds/L3849_grade_output.txt`.

**Data:** ENCODE CTCF in-situ ChIA-PET, Ruan lab. The larger replicate was used in each cell, keeping its strongest 28,270 loops.

| cell | experiment | used | loops | other replicate |
|---|---|---|---|---|
| HEK293 (kidney) | ENCSR410UHV | ENCFF432WRY | 1,436,296 | ENCFF701GLV, 1,401,339 |
| MCF 10A (breast) | ENCSR403ZYJ | ENCFF310MTX | 1,965,094 | ENCFF035RRT, 968,476 |
| BJ (skin fibroblast) | ENCSR573PZV | ENCFF253KLV | 884,636 | ENCFF763HTH, 167,812 |
| RWPE1 (prostate) | ENCSR030KAB | ENCFF479KLF | 908,910 | ENCFF041WND, 375,050 |

Gary's uploads held two duplicate files (identical content); they were ignored.

---

## Results
| # | prediction (≥ 3 of 4 cells) | result |
|---|---|---|
| F1 | K⁺ channels above other genes | **PASS:** 4 of 4 |
| F2 | NMDA receptors above other genes | **PASS:** 3 of 4 (MCF 10A 0.14 vs 0.30) |
| F3 | Ca²⁺ channel pores below other genes | **PASS:** 4 of 4 |
| F4 | pooled D > 0 | **PASS:** 4 of 4 |

**4 of 4 passed.**

## Ten cell types
| cell | D | p | KCN | GRIN | CACNA1 | other |
|---|---|---|---|---|---|---|
| H1 stem cells | 0.110 | 0.001 | 0.34 | 0.57 | 0.10 | 0.24 |
| HFFc6 fibroblasts | 0.057 | 0.018 | 0.28 | 0.57 | 0.10 | 0.24 |
| SK-N-SH neuroblastoma | 0.100 | 0.001 | 0.44 | 0.57 | 0.20 | 0.33 |
| K562 leukemia | 0.026 | 0.24 | 0.34 | 0.43 | 0.10 | 0.28 |
| HepG2 liver cancer | 0.042 | 0.18 | 0.33 | 0.43 | 0.30 | 0.31 |
| IMR-90 lung fibroblasts | 0.053 | 0.09 | 0.34 | 0.43 | 0.20 | 0.29 |
| **HEK293 kidney** | **0.088** | **0.009** | 0.36 | **0.71** | 0.20 | 0.29 |
| MCF 10A breast | 0.011 | 0.42 | 0.32 | **0.14** | 0.10 | 0.30 |
| BJ skin fibroblasts | 0.051 | 0.073 | 0.36 | 0.57 | 0.20 | 0.32 |
| RWPE1 prostate | 0.039 | 0.14 | 0.31 | 0.57 | 0.20 | 0.30 |

**Tallies (descriptive: they mix rounds whose results I had already seen):**
- **K⁺ channels:** above baseline in 10 of 10.
- **NMDA receptors:** above in 9 of 10.
- **Ca²⁺ channel pores:** below in 10 of 10.
- **Pooled D:** positive in 10 of 10 (sign test p = 1/1024).
- **Significant D:** in 4 of 10. With no effect, about 1 cell in 20 would be.

## What it means
- **A small but very consistent tilt:** the nervous system's potassium-channel and NMDA-receptor genes sit at CTCF loop anchors more often than other genes, and calcium-channel pore genes less often. This holds in stem cells, fibroblasts, epithelia, blood and cancer lines.
- **The tilt is cell-type general, not neural:** the largest effects are in stem cells, the neural line and kidney cells.
- **Each single cell type has little power** (null sd ≈ 0.03), which is why only 4 of 10 reach significance alone. The consistency across ten is the evidence.

## Record
**+4 passed. 563 of 774 passed, plus 3 split.** Audit **230 of 301** (entry "CTCF family pattern, 4 new cells").

## Summary
- **Blind in four more human cell types, the family pattern held again:**
  - K⁺ channels above baseline in 4 of 4;
  - NMDA receptors in 3 of 4;
  - Ca²⁺ channel pores below in 4 of 4;
  - overall excess positive in 4 of 4.
- **Over ten cell types the direction never reverses for potassium or calcium channels.** Manuscript 3 now rests on this consistency.

## Potential leads for future research
- **[Meta-analysis]** Pre-register a single combined test across all ten cell types: Stouffer-combined genome-shift z for D, and for each family contrast. Then test it on any further ENCODE cell types (T cells and others) as a fixed out-of-sample check.
- **[Why the CACNA1 dip?]** Look at what sits around the 10 pore genes (gene deserts, very long genes?). Gene length is a candidate confounder for every family. Pre-register a length-matched control.
- **[Figure]** A 10-cell dot plot (family share − other share, one dot per cell) for Manuscript 3.
- **[Manuscript 3]** v0.6 with the ten-cell table.
