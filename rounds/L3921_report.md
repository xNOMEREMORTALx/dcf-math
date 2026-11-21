# DCF L3921: the primary-cell maps do have wider anchors, but trimming them does not bring the potassium excess back (2 of 3)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 21 November 2026

**Files:**
- **Pre-registration:** `PREREGISTERED_L3921_width.txt`.
- **Script:** `rounds/dcf_trim_L3921.py` (W = 1,000, seed 3921).
- **Output:** `L3921_tool_output.txt`, committed before grading.
- **Grading:** `L3921_grade_output.txt`.

**Groups:**
- **A:** the eight ENCODE cell-line CTCF ChIA-PET maps.
- **N:** the seven primary-cell maps (five T-cell, HUVEC, HMEC).

Every map uses its top 28,270 loops (56,540 anchors).

## Results
| # | prediction | result |
|---|---|---|
| W1 | primary maps cover more genome with anchors (median) | **PASS**: 105.0 Mb vs 69.1 Mb |
| W2 | with anchors trimmed to 1 kb, primary maps show the pore K⁺ excess | **FAIL**: 0.304 vs 0.312, p = 0.59 |
| W3 | with anchors trimmed to 1 kb, cell lines still show it | **PASS**: 0.358 vs 0.269, p = 0.004 |

**2 of 3 passed.** The failure stands.

**Anchor widths overlap between the groups.** Median widths run 0.65–4.6 kb in the cell lines and 0.64–4.0 kb in the primary cells.

## What it means
**The fixed reading (W1 pass, W2 fail):** the primary maps do have wider anchors, but width does not explain their null.

**Even with every anchor cut to 1 kb, the matched-gene baseline stays higher in the primary cells:** 0.312 vs 0.269 for the cell lines.
- **So their CTCF loop anchors simply land nearer gene starts in general.**
- **The K⁺ genes do not gain correspondingly.**

**The cell-line excess survives trimming** (p = 0.004). So it was never a width effect either.

**Still open:** why primary-cell CTCF loops sit closer to genes. One possibility is more promoter-anchored CTCF loops in differentiated primary cells. That is a guess, not tested.

## Record
- **+2 passed, 1 failed:** 601 of 831.
- **Audit:** 268 of 358 (entry "anchor width, primary cells").

## Summary
- **Primary-cell CTCF maps have wider anchors, but trimming them to 1 kb does not restore the K⁺ excess** (p = 0.59).
- **In the cell lines it survives trimming** (p = 0.004).
- **The primary-cell difference is a higher gene-wide anchoring baseline,** with the same K⁺ gene ranking (L3917).

## Potential leads for future research
- **[Promoter-anchored CTCF loops]** Pre-register: the fraction of anchors within 5 kb of any protein-coding TSS is higher in the primary maps than in the cell lines. This is cheap, and it uses the same files.
- **[Distance-matched null]** Match control genes also on their distance to the nearest CTCF anchor in a reference map. That separates "K⁺ genes are special" from "the baseline moved".
- **[Manuscript 3 v1.9]** Add §3.19 (this test) to the limitations.
