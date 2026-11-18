# DCF L3821: Manuscript 3 gets its figure. The recomputed permutation null is identical to the frozen L3725 result, and the per-family view shows the excess is uneven
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 18 November 2026

**Files:**
- **Figure:** `figures/L3821_manuscript3.png`.
- **Script:** `figures/L3821_manuscript3.py`.
- **Manuscript:** `notes/Manuscript3_CTCF_nerve_metal_genes_draft_v0.3.md`.

---

## How the figure was made
- **No new test.** The script reuses the frozen L3725 code for the gene table and anchor matching.
- **It reruns the 1,000 genome shifts with the same seed (3725), keeps the null values, and checks its summary line against `rounds/L3725_tool_output.txt`.** It stops if they differ.
- **They are identical:** H1 D = 0.1102, p = 0.0010; HFFc6 D = 0.0574, p = 0.0180.

## The three panels
- **A:** share of genes at a CTCF loop anchor, by family, in two cell types.
- **B:** the shifted-anchor null with the observed value.
- **C:** where the other loop end goes (from L3729).

## Something the figure shows that the text did not
**The excess is uneven across families (descriptive; the families were never tested one by one):**

| family | H1 | HFFc6 | genes |
|---|---|---|---|
| NMDA receptors (GRIN) | 0.57 | 0.57 | 7 |
| Ca²⁺ pumps (ATP2A/B) | 0.57 | 0.29 | 7 |
| Na⁺ channels (SCN) | 0.50 | 0.40 | 10 |
| K⁺ channels (KCN) | 0.34 | 0.28 | 96 |
| HCN | 0.25 | 0.50 | 4 |
| Na⁺/K⁺ pump (ATP1A) | 0.00 | 0.25 | 4 |
| **Ca²⁺ channels (CACNA1)** | **0.10** | **0.10** | 10 |
| NALCN | 0 | 0 | 1 |
| all other genes | 0.24 | 0.24 | 19,884 |

**Calcium channels sit below the genome-wide share in both cell types.** Most families are small, so none of this is a finding yet.

## Summary
- **Manuscript 3 now has its 3-panel figure,** built from the frozen statistic and verified identical to it.
- **The per-family view shows the CTCF-anchor excess comes mainly from potassium and sodium channels and NMDA receptors.** Calcium channels are an apparent exception, worth a pre-registered test.

## Potential leads for future research
- **[Family-level test]** Pre-register per-family predictions (KCN, SCN, GRIN above; CACNA1 below) and test them on loop maps from new cell types.
- **[Neurons]** Neuronal loop maps remain the key test of the "poised" idea.
- **[Publication render]** Add L3821 to `figures/publication/render_all.py` for the 600-dpi and PDF versions when the manuscript is submitted.
