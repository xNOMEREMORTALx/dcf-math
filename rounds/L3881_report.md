# DCF L3881: the potassium-channel excess at loop anchors appears in human motor neurons and is absent in primary non-neural cells (4 of 4)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 20 November 2026

**Files:**
- **Pre-registration:** `PREREGISTERED_L3881_primary_neuron.txt`, frozen before any file map.
- **Amendment:** `AMENDMENT_L3881_a.txt`, made before download (file maps; for Hi-C, ENCODE's default loops file).
- **Script:** `rounds/dcf_confirm_L3881.py`, the L3877 method plus a Hi-C adapter that was smoke-tested beforehand.
- **Grader:** `rounds/dcf_grade_L3881.py`.
- **Outputs:** `rounds/L3881_tool_output_A.txt` (committed unread) and `_B.txt`, both committed before grading.
- **Grading:** `rounds/L3881_grade_output.txt`.

**Data:**

| part | cells | assay | file used | loops |
|---|---|---|---|---|
| A | HUVEC, primary umbilical-vein endothelium (ENCSR404FPI) | CTCF ChIA-PET, Charles Lee lab | ENCFF377RDA (largest of 3 replicates) | 1,002,484 → top 28,270 |
| A | HMEC, primary mammary epithelium (ENCSR819BBB) | CTCF ChIA-PET, Charles Lee lab | ENCFF436NFY (single) | 145,146 → top 28,270 |
| B | iPSC-derived motor neurons (ENCSR550JLK) | in situ Hi-C, Snyder lab | ENCFF215XMY (default) | 2,933 |
| B | iPSC-derived motor neurons (ENCSR794RDS) | in situ Hi-C | ENCFF638CCE (default) | 4,800 |
| B | iPSC-derived motor neurons (ENCSR866FWQ) | in situ Hi-C | ENCFF836TQT (default) | 4,522 |

The uploads also held duplicate copies of HUVEC files; they were ignored.

**Method:** gene resampling matched for length and local gene density, with the cells of each part scored together (10,000 sets, seed 3881).

---

## Results
| # | prediction | share | matched null (sd) | p (upper) | result |
|---|---|---|---|---|---|
| A1 | primary non-immune: no K⁺ excess | 0.344 | 0.328 (0.038) | 0.36 | **PASS** |
| A2 | primary non-immune: no excess, all 139 | 0.367 | 0.338 (0.032) | 0.19 | **PASS** |
| B1 | motor neurons: K⁺ excess | **0.198** | 0.131 (0.027) | **0.009** | **PASS** |
| B2 | motor neurons: excess, all 139 | **0.182** | 0.129 (0.022) | **0.011** | **PASS** |

**4 of 4 passed.**

**Not predicted, read after grading:**
- in motor neurons, **pore-forming K⁺ genes** sit at 0.224 against 0.129 (p = 0.0009);
- **K⁺ auxiliary subunits** sit at 0.078 against 0.142, *below* their null.

This repeats the pore-versus-auxiliary split seen in L3873.

## What it means
**Taking all fifteen non-neuron maps and the three neuron maps together:**

| where | potassium-channel / channel-gene excess at loop anchors |
|---|---|
| 10 cultured cell lines and strains (L3869) | **yes** (p = 0.008 for K⁺) |
| 5 primary CD4⁺ T-cell maps (L3877) | **no** (p = 0.58) |
| 2 primary non-immune cells, HUVEC and HMEC (L3881 A) | **no** (p = 0.36) |
| **3 iPSC-derived motor neurons (L3881 B)** | **yes** (p = 0.009; pore-forming K⁺ p = 0.0009) |

- **By the interpretation fixed in advance, the excess is present in nerve cells.** That is where these genes are used.
- **Absent in primary non-neural cells; present in neurons and in many cultured lines.** Why the lines carry it is open: several are stem-like or neural-like (H1, SK-N-SH, HEK293, which has neuronal features), and culture may matter too.

**Caveats:**
- **The neuron maps are a different assay.** Hi-C loops are fewer and called at 5–25 kb resolution, which raises every gene's chance of touching an anchor. The matched null absorbs that, since the controls see the same anchors, but the neurons were not measured by CTCF ChIA-PET.
- **The motor neurons were grown from iPS cells.** They are differentiated in culture, not taken from a brain.
- **The "no excess" passes (A1, A2) are absence of evidence** in two cell types, not proof of absence.

## Record
**+4 passed. 584 of 806 passed, plus 3 split.** Audit **251 of 333** (entry "primary cells and motor neurons").

## Summary
- **In three human motor-neuron Hi-C maps, potassium-channel genes, and the nervous system's channel and pump genes overall, sit at chromatin loop anchors more often than matched genes** (p ≈ 0.01). Pore-forming potassium channels show it most strongly (p = 0.0009).
- **In primary endothelial and mammary cells, as in primary T cells, they do not.**
- **The pattern now looks neural-linked rather than universal.** Manuscript 3 is updated to v1.3.

## Potential leads for future research
- **[Neurons by ChIA-PET]** A CTCF ChIA-PET or HiChIP map of neurons would remove the assay difference. Search ENCODE/4DN for neural CTCF HiChIP.
- **[Which lines carry it?]** Already visible, so descriptive only and not testable on these data: the three largest pooled D values among the ten lines are **H1 (0.110), SK-N-SH (0.100) and HEK293 (0.088)**, the stem-like and neural-like lines. A blind test needs new stem or neural lines.
- **[Pore vs auxiliary]** Now seen in the ten lines and in neurons; pre-register it on any further dataset.
- **[Other neurons]** Cortical/excitatory iPSC neurons or brain-tissue Hi-C (4DN, PsychENCODE) as a further blind test.
