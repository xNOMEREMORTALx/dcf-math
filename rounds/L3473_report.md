# DCF L3473: Blind test in a nematode, graded against UniProt. 9 of 9 gradeable predictions pass, including the no-sodium control
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 14 November 2026

**Data:**
- **The file:** Gary's attachment `attachment.html`. It is the UniProt TSV saved under an .html name; its content is plain tab-separated text.
- **Contents:** 4,489 reviewed *C. elegans* entries with Entry, Gene Names (primary), Protein families and Sequence. Every row has 4 fields.

**Procedure:**
1. Five frozen hashes matched.
2. The tool read only Entry and Sequence. Its output (accessions and classes) was committed and pushed before the family column was read.
3. Grading: `rounds/L3473_grade.py` → `rounds/L3473_grade_output.txt`.
4. **Truth:** UniProt's curated "Protein families" (truth v4). It is independent of the DCF.

---

## Results (PREREGISTERED_L3469_worm)
| # | prediction | result |
|---|---|---|
| **W1** | **negative control: no sodium-channel calls** (nematodes have none) | **0 calls: PASS** |
| W2 | calcium-channel precision | ungradeable (no calls; the reviewed set holds no calcium α1 entry) |
| W3 | potassium/HCN precision | **3/3 PASS** (shk-1 Shaker, kvs-4 Shab, unc-103 ERG) |
| W4 | voltage-gated channel recall (≥ 75%) | **3/4 PASS** (missed egl-36, Shaw) |
| W5 | K2P precision | **5/5 PASS** |
| W6 | K2P recall (≥ 50%) | **5/6 PASS** (missed unc-58) |
| W7 | glutamate-receptor precision | **3/3 PASS** (glr-1, glr-2, glr-3) |
| W8 | glutamate-receptor recall | **3/3 PASS** |
| W9 | iron-hydroxylase precision | **2/2 PASS** (cat-2 = tyrosine hydroxylase, pah-1) |
| W10 | iron-hydroxylase recall | **2/2 PASS** |
| W11–12 | pumps | ungradeable (one metal pump in the reference set) |

**9 of 9 gradeable predictions pass; 3 ungradeable.** Across 4,489 worm proteins, **none of the 15 metal-class calls was wrong** by UniProt's independent classification.

## Reading
- **The negative control held.** The worm has no voltage-gated sodium channels, and across 4,489 proteins the tool called none.
  - **A caution:** the reviewed worm set holds no sodium *or* calcium α1 channel entry at all, so this control tested only for false sodium calls among non-channel proteins. It could not test whether a calcium channel would have been misread as sodium.
- **The v5 repairs worked on a new lineage:**
  - the K2P rule widened after the fly found 5 of 6 worm leak channels with no false calls;
  - the iron core found both worm aromatic-amino-acid hydroxylases, including **cat-2, the worm's tyrosine hydroxylase** (the dopamine enzyme).
- **The misses, seen after grading:**
  - **egl-36** (a Shaw K channel) has a weak voltage sensor;
  - **unc-58** (K2P) has one filter outside the pattern (T-T-C-G-Y-G);
  - **mca-1** (a calcium pump, PMCA) reads **S-I-P-E-G-L**. The pump rule requires A-[IV] before P-E-G-L, so mca-1 was filed "other." That is a real miss of the pump rule, though ungradeable here (one gene).

## Running tally (nerve-chemistry blind tests)
| species | gradeable passed | truth |
|---|---|---|
| mouse | 10/10 | names |
| zebrafish | 17/21 | names |
| chicken | 13/14 | names + descriptions |
| fruit fly | 5/13 | names + descriptions |
| **nematode** | **9/9** | **UniProt families (independent)** |
| **total** | **54/67** | |

## Record
**+9 passed. 379 of 530 passed, plus 3 split.**

## Summary
- **In a worm, graded for the first time against an independent reference (UniProt's curated families), all 9 gradeable predictions passed.**
  - The tool called **no sodium channels** in an animal that has none.
  - It found potassium, leak and glutamate-receptor channels and both iron hydroxylases, with **no wrong calls in 4,489 proteins.**
- **The fixes made after the fly failures held on a new lineage.**
- **One real weakness showed:** the worm calcium pump's loop (S-I-P-E-G-L) is outside the pump rule.

## Potential leads for future research
- **[Pump loop]** Widen the calcium-pump loop to [AS]-[IV]-P-E-G-L (development on all six species, then blind).
- **[Full worm proteome]** The reviewed set is small. A test on the full worm reference proteome (with InterPro truth) would include egl-19, unc-2 and cca-1, the calcium channels that replace sodium channels in worm nerves.
- **[Battery balance]** The worm makes nerve impulses with calcium instead of sodium. Compare pump and channel inventories with the species already tested.
- **[Manuscript 2]** Add the worm as the first independently graded test; it strengthens the paper considerably.
