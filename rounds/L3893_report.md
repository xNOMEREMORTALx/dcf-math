# DCF L3893: colon tissue shows the potassium-channel excess too (2 of 3 gradeable; E3 failed). The "neural-lineage" reading is now confounded with the assay
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 20 November 2026

**Files:**
- **Pre-registration:** `PREREGISTERED_L3893_tissues.txt`.
- **Note:** `NOTE_L3893_files.txt` (file choices; heart void), recorded before download.
- **Script:** `rounds/dcf_confirm_L3893.py`, the L3881 method with seed 3893.
- **Grader:** `rounds/dcf_grade_L3893.py`.
- **Outputs:** `rounds/L3893_tool_output_{M,C}.txt`, committed before grading.
- **Grading:** `rounds/L3893_grade_output.txt`.

**Data:** ENCODE in situ Hi-C of adult human tissue (Bing Ren lab), default loops files.

| tissue | experiment | file | loops |
|---|---|---|---|
| skeletal muscle (gastrocnemius) | ENCSR479USL | ENCFF735TXQ | 6,478 |
| skeletal muscle (gastrocnemius) | ENCSR089CCK | ENCFF509PNA | 7,391 |
| transverse colon | ENCSR079IDJ | ENCFF008FXM | 6,615 |
| transverse colon | ENCSR295BDK | ENCFF259LCX | 9,121 |
| heart left ventricle (×2, intact Hi-C) | ENCSR385MKW, ENCSR529BKV | **no loops released** | void |

---

## Results
| # | prediction (neural-lineage reading) | share | matched null | p (upper) | result |
|---|---|---|---|---|---|
| E1 | muscle: no K⁺ excess | 0.240 | 0.203 | 0.18 | **PASS** |
| E2 | heart: no K⁺ excess | — | — | — | ungradeable (no loops) |
| E3 | colon: no K⁺ excess | **0.276** | 0.205 | **0.028** | **FAIL** |
| E4 | muscle: no excess, all 139 genes | 0.223 | 0.198 | 0.21 | **PASS** |

**2 of 3 gradeable passed.** E3 failed, and the failure stands.

**Descriptive:**
- **Pore-forming K⁺** is above its matched null in muscle (0.272 vs 0.202, p = 0.042) and in colon (0.272 vs 0.203, p = 0.046).
- **Auxiliary K⁺ subunits** are not (p = 0.95 and 0.20).

## What it means: an assay confound I should have weighed before L3889
| map type | cells | K⁺ excess? |
|---|---|---|
| ChIA-PET | 10 cell lines | **yes** |
| ChIA-PET | 5 primary T-cell sets | no |
| ChIA-PET | primary HUVEC, HMEC | no |
| **Hi-C** | 3 iPSC motor neurons | **yes** |
| **Hi-C** | 2 primary astrocytes | **yes** |
| **Hi-C** | 2 colon tissues | **yes** (p = 0.028) |
| **Hi-C** | 2 skeletal-muscle tissues | not significant (pore-forming K⁺ p = 0.04) |

- **Every "no" came from a primary-cell ChIA-PET map. Every Hi-C map leans the same way,** including colon, which is not neural.
- **The fixed interpretation of L3889 ("neural lineage") is no longer safe.** It was the right reading of that test alone, but the colon result shows the Hi-C/ChIA-PET difference could explain the split.
- **Colon is a mixed tissue:** epithelium, immune cells, smooth muscle and a small enteric nervous system. So this result does not cleanly separate the explanations either.
- **What survives across both assays:**
  - pore-forming potassium-channel genes sit at loop anchors more often than matched genes in most datasets;
  - their auxiliary subunits never do.

## Record
**+2 passed, 1 failed, 1 ungradeable. 588 of 811 passed, plus 3 split.** Audit **255 of 338** (entry "tissues: muscle, colon").

## Summary
- **Colon tissue, which is not neural, shows the potassium-channel excess** (p = 0.028), against the prediction. Skeletal muscle shows only a weak, non-significant lean.
- **Because all the "no excess" results came from one assay (primary-cell ChIA-PET) and all Hi-C maps lean the same way, the neural-lineage conclusion is withdrawn** to "possible, confounded with assay".
- **Manuscript 3 is updated to v1.5.**

## Potential leads for future research
- **[Same cells, both assays]** The decisive test: one primary non-neural cell type with *both* Hi-C loops and CTCF ChIA-PET loops. HUVEC and HMEC ChIA-PET exist; ENCODE/4DN Hi-C of HUVEC or HMEC with loops would settle the assay question. Pre-register: same result in both assays.
- **[H1, both assays]** The 4DN H1 union file merges ChIA-PET- and Hi-C-supported loops. Running H1 Hi-C-only loops against CTCF-ChIAPET-only loops is a direct, cheap assay check. It is not blind (H1 seen), but it is informative.
- **[Pore vs auxiliary]** Consistent in every dataset; the most robust statement so far.
