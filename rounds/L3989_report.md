# DCF L3989: six-fold channels (connexins and ORAI) in fresh maps: no excess in new ChIA-PET, borderline in Hi-C (1 of 2). Not established
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 23 November 2026

**Files:**
- **Pre-registration:** `PREREGISTERED_L3989_hexamers.txt`.
- **Script:** `rounds/dcf_hexa_L3989.py`, seed 3989.
- **Output:** committed before grading.
- **Grading:** `L3989_grade_output.txt`.

**The lead:** in the ten cell lines (L3885), the 23 six-fold channel genes (connexins GJA/B/C/D and ORAI1–3) leaned toward CTCF anchors (p = 0.034). Their shares had never been computed in the maps used here.

## Results
| # | maps | HEXA share vs matched | p | result |
|---|---|---|---|---|
| H1 | 2 new CTCF ChIA-PET (WTC11, 7-day T cells) | 0.391 vs 0.344 | 0.33 | **FAIL** |
| H2 | 9 Hi-C, CTCF-anchored (H1/HFFc6 reference) | 0.188 vs 0.111 | 0.046 | **PASS** |

**1 of 2 passed.**

**Pore K⁺ in the same runs:** 0.437 vs 0.306, p = 0.0019 (the new pair), and p = 0.0013 (Hi-C).

## What it means
**The result is split, which the fixed interpretation did not cover.** The six-fold lead is **not established**.

**H2 carries a caveat:** it uses the H1/HFFc6 reference, and HEXA had leaned in those cells (L3885). So the same reference concern as L3961 applies, and it was not controlled here.

**The two new ChIA-PET maps behave very differently for the two gene sets:**
- **Pore K⁺:** a clear excess (p = 0.0019).
- **Connexins and ORAI:** nothing (p = 0.33).

**The excess remains clearest for potassium channels.**

## Record
- **+1 passed, 1 failed:** 621 of 867.
- **Audit:** 288 of 394.

## Summary
- **The six-fold channel lean does not replicate in two new CTCF ChIA-PET maps** (p = 0.33), and it is borderline in Hi-C (p = 0.046, reference caveat).
- **In the same new maps, pore K⁺ is strong** (p = 0.0019).

## Potential leads for future research
- **[HEXA under the T-cell reference]** Rerun H2 with the T-cell CTCF peaks (L3977 reference) to remove the reference caveat.
- **[HUVEC Hi-C]** ENCSR008UIB (dilution Hi-C) and ENCSR788FBI (intact Hi-C) are HUVEC Hi-C experiments, and the last primary-cell gap. A file-graph screenshot of each is needed.
