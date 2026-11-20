# DCF L3889: primary astrocytes carry the excess too (2 of 2 gradeable). The potassium-channel loop-anchor excess is a neural-lineage feature, not a cell-line one
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 20 November 2026

**Files:**
- **Pre-registration:** `PREREGISTERED_L3889_astrocytes.txt`.
- **Note:** `NOTE_L3889_files.txt` (file choices and voids, recorded before download).
- **Script:** `rounds/dcf_confirm_L3889.py`, the L3881 method with seed 3889.
- **Grader:** `rounds/dcf_grade_L3889.py`.
- **Output:** `rounds/L3889_tool_output_N.txt`, committed before grading.
- **Grading:** `rounds/L3889_grade_output.txt`.

**Data:** ENCODE in situ Hi-C from one lab (Job Dekker, UMass), ENCODE default loops files.

| cells | experiment | file | loops |
|---|---|---|---|
| primary astrocytes, cerebellum | ENCSR011GNI | ENCFF886EVV | 10,998 |
| primary astrocytes, spinal cord | ENCSR974LXZ | ENCFF424KFY | 456 (sparse) |
| brain pericyte (Part P) | ENCSR323QIP | **no loops file released** | void |
| SK-N-MC (Part L) | ENCSR834DXR | **no loops file released** | void |

---

## Results
| # | prediction | share | matched null (sd) | p (upper) | result |
|---|---|---|---|---|---|
| N1 | astrocytes: K⁺ excess | **0.146** | 0.102 (0.022) | **0.037** | **PASS** |
| N2 | astrocytes: excess, all 139 genes | **0.155** | 0.104 (0.018) | **0.005** | **PASS** |
| P1 | pericyte: no K⁺ excess | — | — | — | ungradeable (no loops file) |
| L1 | SK-N-MC: K⁺ excess | — | — | — | ungradeable (no loops file) |

**2 of 2 gradeable passed.**

**Descriptive:**
- **Pore-forming K⁺:** 0.152 vs 0.104 (p = 0.04).
- **Auxiliary K⁺:** 0.118 vs 0.096 (p = 0.41), so no excess.
- **The cerebellar file dominates,** because the spinal-cord map has only 456 loops.

## The picture across all loop maps
| cells | primary? | neural lineage? | excess? |
|---|---|---|---|
| 10 cell lines and strains (L3869) | no | mixed | **yes** (K⁺ p = 0.008) |
| 5 CD4⁺ T-cell maps (L3877) | yes | no | **no** (p = 0.58) |
| HUVEC + HMEC (L3881 A) | yes | no | **no** (p = 0.36) |
| 3 iPSC motor neurons (L3881 B) | derived | **yes** | **yes** (p = 0.009) |
| **2 primary astrocytes (L3889)** | **yes** | **yes** | **yes** (p = 0.037; all 139 p = 0.005) |

- **The interpretation fixed in advance applies:** the excess is **neural-lineage**. It appears in neurons and in primary astrocytes, and it is absent in primary non-neural cells (immune, endothelial, epithelial).
- **The lines that carry it most strongly are stem-like or neural-like** (H1, SK-N-SH, HEK293). That ranking was seen beforehand, so it is descriptive only.
- **Same-lab caveat removed for astrocytes:** they were measured by Hi-C like the neurons. The primary non-neural cells were measured by ChIA-PET, so a same-assay non-neural primary control is still missing; the pericyte was meant to be it but has no loops file.

## Record
**+2 passed, 2 ungradeable. 586 of 808 passed, plus 3 split.** Audit **253 of 335** (entry "primary astrocytes").

## Summary
- **Primary human astrocytes, like motor neurons, have potassium-channel and channel/pump genes at chromatin loop anchors more often than matched genes.** Primary immune, endothelial and mammary cells do not.
- **The pattern now reads as a property of the neural lineage.** Manuscript 3 is updated to v1.4.

## Potential leads for future research
- **[Same-assay non-neural primary control]** Find ENCODE/4DN in situ Hi-C *with released loops* in primary non-neural cells (e.g. fibroblasts, keratinocytes). Predict no excess.
- **[More neural cells]** Other primary astrocyte or neural-progenitor Hi-C, as a further blind replication.
- **[Mechanism]** Whether these anchors coincide with neural enhancers or CTCF sites that differ between neural and non-neural cells. That needs CTCF ChIP-seq or ATAC data for the same cells.
