# DCF L3977 + L3979: at T cells' own CTCF sites, T-cell Hi-C shows no potassium excess, but a new T-cell ChIA-PET sample does. T cells are mixed; the tissue result holds under a third reference (1 of 3)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 23 November 2026

**Files:**
- **Pre-registration:** `PREREGISTERED_L3977_tcell_peaks.txt`.
- **Scripts:** `rounds/dcf_peakref_L3977.py` and `rounds/dcf_ksub_L3979.py`.
- **Outputs:** committed before grading.
- **Grading:** `L3977_grade_output.txt`.

**Data:** Gary's downloads from ENCSR550JJT (CTCF ChIA-PET, activated naive CD4⁺ T cells: IL-2 for 5 days, anti-CD3/CD28 for 7 days; 43-year male donor):
- **CTCF peaks:** ENCFF416VKW (54,365) and ENCFF478NWL (63,643), taken as their union. These come from the reads, not from loop calls.
- **Loops:** ENCFF840AQR (515,842 → top 28,270).

## Results
| # | prediction | result |
|---|---|---|
| P1 | T-cell Hi-C at T-cell CTCF peaks: pore K⁺ excess | **FAIL**: 0.354 vs 0.331, p = 0.33 |
| P2 | nine tissue/neuron Hi-C maps at T-cell CTCF peaks: pore K⁺ excess | **PASS**: 0.180 vs 0.104, p = 0.0009 |
| P3 | new T-cell ChIA-PET, unrestricted: no excess (earlier T-cell null repeats) | **FAIL**: 0.418 vs 0.297, p = 0.011, an excess |

**1 of 3 passed.** The failures stand.

**Descriptive:** in the T-cell peaks themselves, pore K⁺ genes sit near peaks somewhat more often than matched genes (0.494 vs 0.424).

## What it means (the fixed interpretations)
**P1 fails:** in the resting and 36-hour-activated T-cell Hi-C maps, there is no K⁺ excess at loops between T cells' own CTCF sites. For these samples, the T-cell exception is genuine and not a reference artefact.

**P3 fails, in the other direction:** a different T-cell sample (7-day activated, 43-year donor) does show the excess in CTCF ChIA-PET (p = 0.011). So the T-cell picture is **sample-dependent**.

| T-cell data | donor / state | excess? |
|---|---|---|
| 5 CTCF ChIA-PET (L3877) | CD4, as listed in L3877 | no |
| 2 Hi-C at their own CTCF sites (L3977 P1) | resting; 36 h activated | no |
| 1 CTCF ChIA-PET (L3979) | 7-day IL-2/CD3/CD28 activated, 43 y | **yes**, p = 0.011 |

**P2 passes:** the neuron/glia/gut/muscle result now holds under three independent CTCF references:
- **H1/HFFc6:** p = 0.0008.
- **T-cell loop anchors:** p = 0.005.
- **T-cell CTCF peaks:** p = 0.0009.

**Reading:** T cells are a mixed case, possibly depending on activation state or donor. This is a lead, not a conclusion.

## Record
- **+1 passed, 2 failed:** 620 of 864.
- **Audit:** 287 of 391 (entry "T-cell CTCF peaks").

## Summary
- **At T cells' own CTCF sites, T-cell Hi-C shows no K⁺ excess** (p = 0.33). Those samples are a genuine exception.
- **A long-activated T-cell ChIA-PET sample does show it** (p = 0.011), so T cells vary by sample.
- **The tissue/neuron result survives a third reference** (p = 0.0009).

## Potential leads for future research
- **[Activation time course]** ENCODE has CD4 T-cell CTCF ChIA-PET at several activation times. Pre-register: the excess rises with activation duration. ENCSR731OFF (36 h) is the next file; it is the same series as ENCSR550JJT.
- **[Loop partners in the new T-cell map]** Apply the L3969 partner test to ENCFF840AQR.
- **[Manuscript 3 v2.9]** Done: §3.28 is added, and the T-cell line in the conclusion is revised.
