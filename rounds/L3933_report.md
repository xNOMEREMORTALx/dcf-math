# DCF L3933: removing promoter-to-promoter loops does not bring back the potassium excess in primary cells (1 of 3)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 21 November 2026

**Files:**
- **Pre-registration:** `PREREGISTERED_L3933_pp_filter.txt`.
- **Script:** `rounds/dcf_ppfilter_L3933.py`, seed 3933.
- **Output:** `L3933_tool_output.txt`, committed before grading.
- **Grading:** `L3933_grade_output.txt`.

**Filter:** a loop is removed when both of its ends lie within 5 kb of a gene start (a promoter-to-promoter loop).

## Results
| # | prediction | result |
|---|---|---|
| Q1 | primary cells, filtered: pore K⁺ p < 0.05 | **FAIL**, 0.289 vs 0.277, p = 0.35 |
| Q2 | T cells alone, filtered: pore K⁺ p < 0.05 | **FAIL**, 0.284 vs 0.270, p = 0.37 |
| Q3 | cell lines, filtered: pore K⁺ p < 0.05 | **PASS**, 0.348 vs 0.252, p = 0.002 |

**1 of 3 passed.** The failures stand.

**Share of loops removed:** 2.2–5.2% in the cell lines, 4.1–10.1% in the primary cells (T cells 5.1–10.1%).

## What it means
**The fixed reading (Q1 and Q2 fail):** promoter-to-promoter loops do not mask the excess, and the primary-cell difference is not this simple.
- **The filter lowered the primary-cell baseline** (0.326 → 0.277).
- **But the K⁺ genes fell with it,** so they still do not stand out.

**Combined with L3917–L3929, the primary-cell result now reads as biology rather than method:**
- **Same gene ranking.** The same K⁺ genes are anchored in the primary cells (L3917).
- **Anchoring is more gene-start-heavy overall.** Primary-cell anchors sit nearer gene starts (L3929).
- **No technical fix restores the excess.** Neither trimming anchors (L3921) nor dropping promoter loops (L3933) brings it back.
- **The cell-line excess survives every filter tried** (p = 0.002 here).

## Record
- **+1 passed, 2 failed:** 604 of 836.
- **Audit:** 271 of 363 (entry "promoter-promoter filter").

## Summary
- **Dropping promoter-to-promoter loops did not restore the K⁺ excess in T cells, HUVEC or HMEC** (p = 0.35–0.37).
- **It left the cell-line excess intact** (p = 0.002).
- **The primary-cell null looks like a real cell-type difference.** The potassium genes are anchored there, just not more than comparable genes.

## Potential leads for future research
- **[Expression link]** In T cells, several K⁺ genes are expressed (KCNA3, KCNN4, KCNMB-dependent BK). Pre-register whether expressed K⁺ genes lose their excess relative to silent ones. This needs T-cell RNA-seq gene lists.
- **[Developmental reading]** The excess is in stem/cancer lines and in Hi-C from neurons, glia, gut and muscle, all at CTCF sites. The primary blood/endothelial ChIA-PET maps lack it. A Hi-C map from T cells would separate cell type from assay for the last time.
- **[Manuscript 3 v2.0]** Done: §3.20 covers L3929 and L3933.
