# DCF L3869: the dependence-aware test keeps the potassium-channel and pooled excess, but not the NMDA and calcium-pore results (2 of 4). An honest correction to L3857
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 19 November 2026

**Files:**
- **Pre-registration:** `PREREGISTERED_L3869_gene_resampling.txt`, frozen before running.
- **Script:** `rounds/dcf_generesample_L3869.py`.
- **Grader:** `rounds/dcf_grade_L3869.py`.
- **Output:** `rounds/L3869_tool_output.txt`, committed before grading.
- **Grading:** `rounds/L3869_grade_output.txt`.

**Why this test:** L3857's combined Z values assumed the ten cells were independent, which they are not. This test resamples **genes** instead:
- 10,000 random sets are drawn, each family gene replaced by one of its 50 nearest ordinary genes in length and local gene density.
- Every set is scored in all ten cells at once, so shared genes and shared CTCF sites stay in the null.

---

## Results
| # | family | ten-cell mean share | null mean (sd) | p | result |
|---|---|---|---|---|---|
| R1 | K⁺ channels (96) | 0.345 | 0.270 (0.030) | **0.008** | **PASS** |
| R2 | NMDA receptors (7) | 0.500 | 0.341 (0.114) | 0.095 | **FAIL** |
| R3 | Ca²⁺ channel pores (10) | 0.170 | 0.304 (0.095) | 0.078 | **FAIL** |
| R4 | all 139 channel/pump genes | 0.347 | 0.275 (0.025) | **0.002** | **PASS** |

**2 of 4 passed.** The failures stand.

## What it means
- **Established:**
  - the nervous system's channel and pump genes, taken together, sit at CTCF loop anchors more often than matched ordinary genes, across ten cell types (p = 0.002);
  - so do the potassium-channel genes on their own (p = 0.008).
- **Not established:** the NMDA excess and the calcium-pore dip. Both are large in size and consistent in direction in nearly every cell type, but they rest on 7 and 10 genes. Matched random sets of that size vary a lot (sd ≈ 0.1), so chance cannot be ruled out.
- **L3857's Z of +4.2 and −3.8 for these two families overstated the evidence,** as its caution said. Manuscript 3 (v0.9) now quotes this test.

## Record
**+2 passed, 2 failed. 577 of 790 passed, plus 3 split.** Audit **244 of 317** (entry "gene-resampling ten cells").

## Summary
- **With a test that respects shared genes across cell types, the channel-gene excess (p = 0.002) and the potassium-channel excess (p = 0.008) hold.**
- **The NMDA and calcium-pore patterns do not reach significance and are reported as suggestive.**

## Potential leads for future research
- **[More genes per family]** NMDA and calcium findings need larger gene sets. A pre-registered "ionotropic glutamate receptors" (GRIN + GRIA + GRIK + GRID) set and a "voltage-gated Ca²⁺ complex excluding auxiliary" set would give more power. The auxiliary subunits already failed in L3837.
- **[Out-of-sample]** Apply L3869 unchanged to new ENCODE cell types (T cells) as a fixed confirmatory test for K⁺ channels.
- **[Potassium subfamilies]** Which K⁺ families carry the excess (Kv, K2P, Kir, KCa)? Pre-register before looking.
