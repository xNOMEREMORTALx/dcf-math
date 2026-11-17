# DCF L3717: Nerve-metal genes in human 3D genome loops (3 of 4). In stem cells, channel and NMDA genes sit at CTCF (zinc) loop anchors more often than other genes, while their active-promoter loops are reduced
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 16 November 2026

**Data:**
- **Gene positions:** Gary's GENCODE file, release 49 basic, GRCh38, dated 2025-07-08. It has 20,014 protein-coding genes on the autosomes and X.
- **Loops:** the two verified 4DN loop files (L3705).

**Procedure:**
1. **Frozen files:** `PREREGISTERED_L3713_channel_loops.txt` and `rounds/dcf_channel_loops_L3713.py`; the hashes matched.
2. **Tool output:** `rounds/L3717_tool_output.txt`, pushed before grading.
3. **Grading:** `rounds/L3717_grade_output.txt`.

**Gene sets:**
- **Channel set (139 genes):** K channels (KCN*), Na channels (SCN*A), CaV α1 (CACNA1*), HCN1–4, NALCN, NMDA receptors (GRIN*), Na/K pumps (ATP1A*), SERCA (ATP2A*) and PMCA (ATP2B*).
- **Control:** every other protein-coding gene.
- **"At a loop":** the gene's start site ± 5 kb overlaps a loop anchor.

---

## Results
| # | cells | loop type | channel genes | other genes | odds ratio | prediction | result |
|---|---|---|---|---|---|---|---|
| C1 | H1 (stem) | **CTCF** | **34.5%** | 23.5% | **1.72** (p = 0.002) | not enriched | **FAIL** |
| C2 | HFFc6 (fibroblast) | CTCF | 29.5% | 23.7% | 1.34 (p = 0.07) | not enriched | **PASS** |
| C3 | H1 | active promoter (H3K4me3) | 63.3% | 70.6% | 0.72 (p = 0.04) | depleted | **PASS** |
| C4 | HFFc6 | active promoter | 33.8% | 60.5% | **0.33** (p = 2 × 10⁻¹⁰) | depleted | **PASS** |

**3 of 4 passed.**

## Descriptive, after grading
| family | n | at CTCF anchors, H1 | HFFc6 |
|---|---|---|---|
| NMDA receptors (GRIN) | 7 | **57%** | **57%** |
| Na channels (SCN) | 10 | **50%** | 40% |
| Na/K and Ca pumps (ATP1A/2A/2B) | 11 | 36% | 27% |
| K channels and subunits (KCN) | 96 | 34% | 28% |
| CaV α1 (CACNA1) | 10 | 10% | 10% |
| background (all genes) | | 23.5% | 23.7% |

**Genes at CTCF anchors in H1 include:**
- **NMDA receptors:** GRIN2A, GRIN2B, GRIN2C, GRIN3B;
- **sodium channels:** SCN1A, SCN3A, SCN5A, SCN7A, SCN8A;
- **potassium channels:** KCNA1/2/3, KCNB1, KCNC1, KCNQ3/5, KCNMA1 (BK), KCNH2 (hERG), KCNJ inward rectifiers, KCNK leak channels and others.

**Caveats:**
- **Clusters break independence.** Several channel genes sit in clusters (e.g. SCN1A/2A/3A/7A on chromosome 2), and neighbours can share one anchor. The Fisher test assumes independent genes, so the p-values are optimistic.
- **The KCN pattern includes auxiliary subunits** (KCNAB, KCNE, KCNIP), as frozen.

## Reading
- **The active-promoter result came out as predicted.** Channel genes are neural and mostly silent outside nerve and muscle. In fibroblasts their active-promoter loops are **reduced to a third** of the expected odds.
- **In stem cells the reduction is mild (0.72).** That fits the known "bivalent" state of developmental genes in embryonic stem cells: marked both active and repressed, poised for later.
- **The CTCF result was not predicted.** In stem cells, nerve-metal genes, **especially NMDA receptors and sodium channels**, sit at CTCF loop anchors **more** often than other genes. In fibroblasts the trend is the same but weaker.
- **One reading, stated as a hypothesis:** genes that will later run the nervous system's metal battery are held in **CTCF-anchored (zinc-finger) loop domains** before they are switched on. The 3D architecture prepares the "battery" genes.
- **This connects the two strands of this series:**
  - the metal-selecting channel proteins (Na, K, Ca);
  - the zinc protein that structures their genes in 3D.
- **It is an association in two cell types,** not a mechanism.

## Record
**+3 passed, 1 failed. 501 of 684 passed, plus 3 split.** Audit **168 of 211.**

## Summary
- **Nerve-metal genes in human 3D genome loops:** 3 of 4 predictions passed.
- **Active-promoter loops:** as predicted, the channel genes have fewer in fibroblasts (a third of the expected odds) and slightly fewer in stem cells.
- **CTCF loop anchors, unexpected:** in stem cells, channel genes sit at CTCF anchors more often than other genes (odds ratio 1.72), especially NMDA receptors and sodium channels. The same trend is weaker in fibroblasts.
- **Hypothesis:** the zinc-finger loop architect may pre-organise the nervous system's battery genes before they are used.

## Potential leads for future research
- **[Cluster-robust test]** Repeat C1 with one gene per cluster (merge genes whose start sites are < 100 kb apart), or with a permutation that shifts the gene set along the genome. Pre-register before running.
- **[Specificity control]** Is this neural-gene-wide, or channel-specific? Compare channel genes with a matched set of other neural genes (e.g. synaptic adhesion: NRXN*, NLGN*, CNTNAP*) and with a set of genes of similar length.
- **[Neural cells]** 4DN or ENCODE loop data from neurons, if available, would show whether these CTCF-anchored channel genes gain active-promoter loops when switched on.
