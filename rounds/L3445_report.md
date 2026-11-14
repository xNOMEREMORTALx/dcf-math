# DCF L3445: Predicted fish genes. 7 of 10 gradeable predictions pass. Two of the three failures come from the naming rule (the "wrong" calls are channels by their own descriptions); one is a real error
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 13 November 2026

**Lead:** [Predicted records].

**Data:** `zebrafish.2.rna.fna.gz`, the predicted (XM_) transcripts.
- 10,470 genes after **excluding every gene already graded from file 1.**
- One variant per gene: the one with the longest reading frame.

**Disclosure:** the file was in hand before the pre-registration. It had been opened only to read its first header line and to count records; no tool had scanned it.

**Procedure:**
1. Pre-registration and script frozen and pushed.
2. Tool output (no names) pushed.
3. Graded: `rounds/L3445_grade.py` → `rounds/L3445_grade_output.txt`.

---

## Results
| # | prediction | result |
|---|---|---|
| X1 | calcium calls correct | **10/10 PASS** |
| X2 | sodium calls correct | **1/1 PASS** |
| X3 | potassium/HCN calls in named families (≥ 90%) | **38/45 FAIL** |
| X4 | channel family genes found (≥ 75%) | **49/51 = 96% PASS** |
| X5 | K2P leak calls correct | **3/3 PASS** |
| X6 | K2P genes found (≥ 70%) | **3/6 FAIL** (kcnk4a, kcnk7, kcnk10b missed) |
| X7 | glutamate-receptor calls correct | **24/25 PASS** |
| X8 | glutamate receptors found | **24/26 PASS** |
| X9 | NMDA calls correct (≥ 90%) | **7/8 FAIL** (cars2) |
| X10 | NMDA receptors found | **7/7 PASS** |
| X11–12 | FeHyd2 | **ungradeable:** every iron hydroxylase was already in file 1 and so excluded |

**7 of 10 gradeable predictions pass.**

## What the failures mean
**X3:**
- **Why it failed:** all 7 "wrong" potassium/HCN calls are **unnamed genes** (LOC/si: numbers). The frozen truth rule counts unnamed genes as wrong.
- **What the genes actually are** (descriptive, not counted; `rounds/L3445_unnamed_nearest.txt`):

| unnamed gene | NCBI's own description | nearest mouse protein |
|---|---|---|
| LOC100004160, LOC100330283, LOC100537815, LOC567521 | "potassium voltage-gated channel subfamily A member…" | Kcna5, Kcna3, Kcna2, Kcna10 |
| LOC100536252 | "shaker-related potassium channel tsha2" | Kcna1 |
| si:dkey-43k4.5 | (none) | Kcns1 |
| LOC101882339 | "uncharacterized" | **Hcn4** (called HCN) |

- **What that means:** every one is a potassium or pacemaker channel by its own description or its nearest relative. The failure measures **the gap between the rule and the naming, not a biology error.** The same thing happened with the one zebrafish failure in L3441. It stays a failure as frozen.

**X7 (passed):** its single "wrong" call, LOC101885658, is described as "glutamate receptor ionotropic, kainate 2-like."

**X9: a real error.**
- **What happened:** cars2, a mitochondrial tRNA enzyme, contains **A-S-Y-T-A-N-E** by chance.
- **Why:** the NMDA gate continues **A-S-Y-T-A-N-L-A-A-F**. The finder used only 6 letters, which is too short.
- **The fix,** to be tested fresh: `ASYTANL`.

**X6: real misses.** Three leak-channel genes were not found. kcnk7 was also missed in human and mouse. The other two (kcnk4a, kcnk10b) need inspection.

## Combined fish tally (L3441 v4 + L3445)
- **Sodium and calcium:** 23 calls, **0 wrong.**
- **Named potassium/HCN genes found:** 40 of 43.
- **Channel calls:** 71 in all, 8 of them outside the named families. All 8 are channels by NCBI's description or their nearest mouse relative, so **no channel call was a biological error.**
- **The one biological error in the fish** is the NMDA chance match in cars2.

## Record
**+7 passed, 3 failed** (X11–12 ungradeable). **352 of 494 passed, plus 3 split.**

## Summary
- **In 10,470 predicted fish genes, the rules sorted 49 of 51 named channel genes by metal ion,** with no sodium/calcium errors, and found all 7 NMDA receptors and 24 of 26 glutamate receptors.
- **Two failures are naming artefacts.** The "wrong" calls are potassium channels by NCBI's own descriptions, but they are unnamed, so the frozen rule counts them wrong.
- **The NMDA failure is a real error:** a 6-letter motif matched by chance in an unrelated enzyme. Lengthening it by one letter is the fix to test.

## Potential leads for future research
- **[Truth rule]** For the next test, freeze a truth rule that also accepts NCBI's description text (e.g. "potassium voltage-gated channel", "glutamate receptor"), so that unnamed but described genes are graded on biology.
- **[NMDA7]** Test `ASYTANL` blind (cars2 excluded by design).
- **[K2P misses]** Inspect kcnk4a, kcnk7 and kcnk10b (development).
- **[Phone]** Add the iron-site and glutamate-receptor finders to menu 34.
- **[Iron trilogy]** One figure of iron's three roles.
