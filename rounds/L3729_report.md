# DCF L3729: Where the channel genes' CTCF loops lead (2 of 2): never to another channel gene, mostly into non-gene DNA; Manuscript 3 draft v0.1
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 16 November 2026

**Files:**
- **Pre-registration:** `PREREGISTERED_L3729_channel_partners.txt`.
- **Script:** `rounds/dcf_channel_partners_L3729.py`.
- **Output:** `rounds/L3729_tool_output.txt`.
- **Grading:** `rounds/L3729_grade_output.txt`.

## Results
| # | prediction (H1) | result |
|---|---|---|
| R1 | < 5% of channel-anchored CTCF loops reach another channel gene | **0 of 153: PASS** |
| R2 | partners at a protein-coding TSS not more common than for control loops | **11.1% vs 26.8% (OR 0.34): PASS** |

**2 of 2 passed.**

**HFFc6 (descriptive):** 0 of 119 reach another channel gene; 17.6% reach a TSS, against 27.0%.

**Reading:**
- **There is no channel-to-channel "hub".**
- **Loops from nerve-metal genes mostly reach non-gene DNA** (89% in H1, 82% in HFFc6), about **two to three times less often a gene** than loops from other genes.
- **These could be insulator-type structural loops, or loops to distant regulatory elements.** Telling them apart needs enhancer and insulator annotations.

## Manuscript 3, draft v0.1 (`notes/Manuscript3_CTCF_nerve_metal_genes_draft_v0.1.md`)
**The result chain from L3705 to L3729 as a short paper:**
- verified data;
- 4 frozen tests;
- the anchor-occupancy results (3/4), robustness (1/3), permutation (2/2) and partners (2/2);
- every failure kept;
- Methods, Discussion, limits and declarations.

## Record
**+2 passed. 506 of 691 passed, plus 3 split.** Audit **173 of 218.**

## Summary
- **The CTCF loops anchored at nerve-metal genes never join two channel genes,** and they reach non-gene DNA more often than loops from other genes.
- **The whole 3D-genome result** (fewer active loops, more CTCF anchors, robust to permutation, loops into non-gene DNA) **is now drafted as Manuscript 3 v0.1.**

## Potential leads for future research
- **[Partner regions]** Annotate the non-gene partner anchors with enhancer (H3K27ac) and insulator data for H1/HFFc6 (ENCODE files needed).
- **[Figure for Manuscript 3]** A three-panel figure (anchor shares, permutation null, partner classes).
- **[Neurons]** Loop maps from neurons or cardiomyocytes, to test the "poised" interpretation.
