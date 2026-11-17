# DCF L3721: Is the channel-gene CTCF enrichment real? Not explained by gene length, not shared by other neural genes; the cluster check failed through a design flaw, and a fairer stratified view shows enrichment in both cell types (1 of 3)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 16 November 2026

**Lead:** [Cluster-robust test] and [Specificity control] from L3717.

**Files:**
- **Pre-registration:** `PREREGISTERED_L3721_channel_loops2.txt`.
- **Script:** `rounds/dcf_channel_loops2_L3721.py`.
- **Output:** `rounds/L3721_tool_output.txt`.
- **Grading:** `rounds/L3721_grade_output.txt`.

**Data:** GENCODE v49 and the two verified 4DN loop files. **Graded on the H1 stem cells,** where the L3717 effect appeared.

---

## Results
| # | check | channel | comparison | odds ratio | result |
|---|---|---|---|---|---|
| P1 | still enriched after merging clustered genes (< 100 kb) into units | 35.9% (46/128 units) | 33.7% (control units) | 1.10, p = 0.33 | **FAIL** |
| P2 | other neural genes (neurexins, neuroligins, contactins, SHANK, DLG, synapsins, synaptotagmins; 50 genes) **also** enriched | 24.0% | 23.5% | 1.03, p = 0.52 | **FAIL** |
| P3 | still enriched against 10 length-matched genes each (median length 65.5 kb in both) | 34.5% | 23.4% | **1.73**, p = 0.003 | **PASS** |

**1 of 3 passed.**

**Disclosed design flaw in P1:**
- **Units were merged within each set separately.** Control units therefore bundle many genes, often whole gene-dense neighbourhoods, and each bundle gets many chances to hit an anchor. Channel units stayed mostly single genes (139 genes → 128 units).
- **The comparison is unequal.** The P1 failure says more about the design than about the genes. **It stands as graded.**

## Descriptive, after grading (a fairer split)
**Every gene is labelled by its genomic neighbourhood:** "isolated" means no other protein-coding gene starts within 100 kb.

| cells | neighbourhood | channel genes | other genes | odds ratio | p |
|---|---|---|---|---|---|
| H1 | in gene neighbourhoods (89 channel genes) | **38.2%** | 24.3% | **1.93** | 0.003 |
| H1 | isolated (50) | 28.0% | 19.4% | 1.61 | 0.10 |
| HFFc6 | in gene neighbourhoods | **37.1%** | 24.5% | **1.82** | 0.006 |
| HFFc6 | isolated | 16.0% | 20.0% | 0.76 | 0.81 |

- **Isolated genes are anchored less often, not more,** so gene isolation does not explain the effect.
- **Among genes that share their neighbourhood with other genes, channel genes sit at CTCF anchors about 1.9 times as often (odds) as other genes, in both cell types.**
- **This fairer view was chosen after seeing P1, so it is descriptive and needs its own pre-registered test.**

## Reading
- **Not length:** the enrichment survives length matching (P3).
- **Not neural-gene-wide:** synaptic adhesion and scaffold genes show no enrichment (P2). **If real, the effect is specific to the channel and pump genes.**
- **Not yet shown to be cluster-robust:** the frozen cluster check failed through an unequal design. A fairer stratified view shows the enrichment in both cell types, but it must be tested properly.
- **The hypothesis from L3717 (CTCF, the zinc-finger architect, pre-organises the nervous system's "battery" genes) is weakened but not refuted.**
  - **Weakened:** one robustness check failed.
  - **Not refuted:** the effect is not explained by length, appears specific to channels, and shows in both cell types within gene neighbourhoods.

## Record
**+1 passed, 2 failed. 502 of 687 passed, plus 3 split.** Audit **169 of 214.**

## Summary
- **The stem-cell enrichment of nerve-metal genes at CTCF anchors is not explained by gene length,** and other neural genes do not share it. If real, it is specific to channels and pumps.
- **The pre-registered cluster check failed,** but its design compared single channel genes with multi-gene control bundles.
- **A fairer split** (genes in gene neighbourhoods) shows the enrichment in both cell types (odds ratio about 1.9). It was chosen after the fact, so it needs a fresh pre-registered test.

## Potential leads for future research
- **[Permutation test]** Pre-register a genome-shift permutation. Shift every loop anchor by the same random offset on its chromosome (1,000 times) and recount the channel-gene anchor rate. This keeps gene clustering and loop structure intact, and is the cleanest fix for P1.
- **[Neighbourhood-stratified test]** Pre-register the stratified comparison above on a third 4DN cell type, if Gary can download one (e.g. another union-loop file from the same Zenodo/4DN release).
- **[Which channels]** If the effect holds, list the channel genes anchored in both cells and their CTCF-loop partners. Do the loops link channel genes to each other (co-regulation hubs)?
