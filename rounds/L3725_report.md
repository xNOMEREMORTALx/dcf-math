# DCF L3725: The channel-gene CTCF excess survives a cluster-preserving genome-shift test in both human cell types (2 of 2)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 16 November 2026

**Lead:** [Permutation test] (L3721).

**Files:**
- **Pre-registration:** `PREREGISTERED_L3725_channel_perm.txt`.
- **Script:** `rounds/dcf_channel_perm_L3725.py` (seed 3725).
- **Output:** `rounds/L3725_tool_output.txt`.
- **Grading:** `rounds/L3725_grade_output.txt`.

**Method:**
- **The statistic:** the share of 139 nerve-metal genes whose start site is at a CTCF loop anchor (± 5 kb), minus the same share among all other protein-coding genes.
- **The null:** 1,000 shuffles. Each shifts every CTCF anchor on a chromosome by one common random offset, wrapping at the chromosome end.
  - **This keeps** gene clusters, gene density and the loop pattern intact.
  - **It breaks only** their alignment with each other.
  - **It answers the flawed cluster check of L3721.**

---

## Results
| # | cells | observed difference | null mean ± sd | null 95th percentile | p | result |
|---|---|---|---|---|---|---|
| Q1 | H1 stem cells | **0.110** | 0.004 ± 0.027 | 0.050 | **0.001** (no shuffle reached it) | **PASS** |
| Q2 | HFFc6 fibroblasts | **0.057** | 0.004 ± 0.024 | 0.046 | **0.018** | **PASS** |

**2 of 2 passed.**

**Note:** this script counts 20,023 protein-coding genes; L3713 counted 20,014, because it keyed genes by name and 9 duplicated names collapsed. The observed differences match L3717.

## The evidence so far, together
| check | H1 | HFFc6 |
|---|---|---|
| L3717: raw Fisher test | OR 1.72, p = 0.002 | OR 1.34, p = 0.07 |
| L3721 P3: against length-matched genes | OR 1.73, p = 0.003 | OR 1.27, p = 0.13 (descriptive) |
| L3721 P2: other neural genes share it? | **no** (OR 1.03) | no (OR 0.70) |
| L3721 P1: cluster-merged units (flawed design) | failed | failed |
| **L3725: cluster-preserving genome shift** | **p = 0.001** | **p = 0.018** |

## Reading
**Nerve-metal genes sit at CTCF loop anchors more often than other genes, in both stem cells and fibroblasts.** That covers K, Na and Ca channels, HCN, NALCN, NMDA receptors, and the Na/K and Ca pumps. The excess is:
- **not explained** by gene length, gene clustering or gene density;
- **not shared** by other neural genes (synaptic adhesion and scaffold proteins);
- **stronger in stem cells** (11 percentage points) than in fibroblasts (6).

**Meanwhile, the same genes have fewer active-promoter loops,** a third of the expected odds in fibroblasts (L3717).

**Hypothesis, now with stronger support:** in non-neural cells, the genes for the nervous system's metal battery are held in CTCF-anchored (zinc-finger) loop structures while they are switched off. This could be a "poised" architecture, ready for activation in neurons.

**Open questions:**
- Whether these anchors are the same in neurons.
- Whether the loops connect channel genes to each other or to their enhancers.

**Status:** an association, replicated in two cell types under a robust null. Still not a mechanism.

## Record
**+2 passed. 504 of 689 passed, plus 3 split.** Audit **171 of 216.**

## Summary
- **A genome-shift permutation test, which keeps gene clusters and loop structure, confirms the excess in both human cell types:** p = 0.001 in stem cells and p = 0.018 in fibroblasts.
- **Nerve-metal genes sit at CTCF (zinc-finger) loop anchors more often than other genes,** not because of length or clustering, and not as a general neural-gene trait.
- **Together with their reduced active-promoter loops,** this suggests the "battery" genes are held in a poised 3D structure in non-neural cells.

## Potential leads for future research
- **[Loop partners]** For channel genes anchored in both cells, list their CTCF-loop partners. Do loops join channel genes to one another, or to non-coding regions?
- **[Neurons]** Loop data from neurons (4DN or ENCODE) would test whether these anchored channel genes switch to active-promoter loops when used.
- **[Manuscript]** This 3D-genome result (L3717–L3725) could become a short third paper, or a section of Manuscript 2: "CTCF loop anchoring of nerve-metal genes".
