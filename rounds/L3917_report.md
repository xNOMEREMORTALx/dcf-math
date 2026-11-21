# DCF L3917: the same potassium-channel genes sit at CTCF loop anchors in cell lines, tissues, neurons and even the "negative" primary cells (2 of 3)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 21 November 2026

**Files:**
- **Pre-registration:** `PREREGISTERED_L3917_gene_level.txt`, frozen before any per-gene frequency was computed.
- **Script:** `rounds/dcf_genelevel_L3917.py`.
- **Output:** `L3917_tool_output.txt`, committed before grading; it includes the full 79-gene list.
- **Grading:** `L3917_grade_output.txt`.

**Groups (26 maps):**
- **A:** ten cell lines (CTCF ChIA-PET).
- **B:** nine Hi-C maps (motor neurons, astrocytes, colon, muscle), CTCF-anchored loops only.
- **N:** seven primary-cell CTCF ChIA-PET maps (five T-cell, HUVEC, HMEC), the "no excess" group.

**Score per gene:** for each of the 79 pore-forming K⁺ genes, how often it sits at an anchor, minus the average of its 50 matched genes.

---

## Results
| # | prediction | result |
|---|---|---|
| G1 | the same genes stand out in cell lines and Hi-C maps: rho(A, B) > 0, p < 0.05 | **PASS**, rho = 0.73, p = 0.0001 |
| G2 | the negatives anchor the same genes: rho(A, N) > 0, p < 0.05 | **PASS**, rho = 0.78, p = 0.0001 |
| G3 | rho(A, B) > rho(A, N) | **FAIL**, 0.73 vs 0.78 |

**2 of 3 passed.** Also, rho(B, N) = 0.66.

| group | pore K⁺ anchor frequency | matched genes | average excess |
|---|---|---|---|
| A, ten cell lines | 0.368 | 0.273 | **+0.095** |
| B, Hi-C, CTCF-anchored | 0.165 | 0.094 | **+0.071** |
| N, primary ChIA-PET | 0.329 | 0.326 | +0.003 |

## What it means
**G1:** a shared gene set carries the excess. The same K⁺ genes stand out in stem cells, fibroblasts and cancer lines (ChIA-PET) and in neurons, astrocytes, colon and muscle (Hi-C).

**G2 is the surprise, and the fixed interpretation applies:** the "negative" primary cells anchor the same genes, in nearly the same order (rho 0.78). Their null result is not a different gene set. Two things combine:
- **Their matched genes sit at anchors more often** (0.326 vs 0.273 in the cell lines). The general CTCF anchoring is denser in these maps, which raises the bar.
- **The K⁺ genes that are weak elsewhere are weaker still there,** so the average excess cancels out.

**G3 fails:** the negatives are no less similar to the cell lines than the Hi-C maps are.

**Genes at anchors in all three groups** (descriptive; excess > 0.3 in each group):
- **KCNMA1** (BK channel);
- **KCNJ5** (GIRK4);
- **KCNQ5**;
- **KCNC1** (Kv3.1);
- **KCNJ11** (Kir6.2, the K_ATP pore);
- **KCNH1** (EAG1);
- **KCNA2** (Kv1.2).

**Genes that drop out in particular groups:**
- **In the primary cells:** KCNK9 (TASK-3) and KCNF1.
- **In the Hi-C maps:** KCNS1, KCNF1 and KCNK7.

## Record
- **+2 passed, 1 failed:** 599 of 828.
- **Audit:** 266 of 355 (entry "gene-level consistency").

## Summary
- **The potassium-channel anchor pattern is the same gene set everywhere tested:** rho = 0.66–0.78 between groups, all p = 0.0001.
- **The primary cells that showed "no excess" anchor the same genes.** Their null comes from a higher baseline in matched genes, not from losing the K⁺ genes.
- **Seven genes are anchored in every group:** KCNMA1, KCNJ5, KCNQ5, KCNC1, KCNJ11, KCNH1 and KCNA2.

## Potential leads for future research
- **[Baseline in primary maps]** Why do matched genes anchor more in T-cell/HUVEC/HMEC maps? Pre-register: these maps have more anchors per Mb (denser CTCF calls). If so, an anchor-density-matched comparison should restore the excess.
- **[The seven core genes]** Are their anchors the same CTCF sites in every map (shared site coordinates)? That would be a constitutive CTCF boundary at each gene.
- **[Expression]** Are the core seven silent or expressed in the cells where they are anchored? This needs expression data (GTEx/ENCODE RNA-seq).
- **[Manuscript 3 v1.8]** Done: §3.18 is added.
