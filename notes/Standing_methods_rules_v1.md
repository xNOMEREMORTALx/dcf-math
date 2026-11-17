# DCF standing methods rules (v1)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 17 November 2026
*Rules learned from failures in rounds L3633–L3757. Each rule names the round that taught it. Every future pre-registration should apply them.*

## A. Numbers from any source
1. **Untrusted by default.** Every numerical claim, from Grok, Gemini, GPT, a web page or Claude, is recomputed before it enters a manuscript (project rule; L3701, L3705).
2. **Position claims** ("X contains S at position N") are checked with the project's mpmath snippet.
3. **Look-elsewhere.** A pattern noticed after looking (e.g. 5,304 near 144 · 37, L3709) is recorded as arithmetic, not as evidence. **Target number families must be named before the data are seen** (L3705).

## B. Absence calls ("gene X is missing in organism Y")
4. **Every absence finder needs a measured sensitivity.** Include known positives as must-find controls in the pre-registration:
   - cohesin, 79% per gene (L3713);
   - cryptochrome shortlist, 7 of 9 (L3757).
5. **A single-organism absence is "not detected", not "lost",** unless it is supported by several relatives (e.g. fluke NAV, 5 of 5; L3701) or by an independent search.
6. **Annotation sets the ceiling.** Selenocysteine (U) appears only where the gene-model pipeline encodes it (L3733). Fragments hide genes (L3637, L3645). Name-based classes depend on how UniProt labels entries (L3753).

## C. Similarity searches
7. **No 3-letter-word (or 4-mer) shortlists at deep evolutionary distances.** They failed three times:
   - L3565 (4-mers);
   - L3633 (the Hydra control missed);
   - L3757 (fly cry ranked 81st).
   
   **Align directly** (about 85 local alignments per second per core), or use a motif prefilter whose sensitivity is measured first.
8. **Nearest-reference counts need a score floor.**
   - The floor is **calibrated on named positives and negatives** (NR1: 941, L3693), not chosen as a round number (1,000 removed true divergent NR1s, L3689).
   - **State the floor in the pre-registration,** and build it into shared code (dcf_nr1_L3693).
9. **Reciprocal best hits** against a panel of the family's paralogs prevent repeat-rich proteins posing as the target (CTCF, L3701).

## D. Statistics
10. **Grid effects.** Genomic coordinates sit on human-chosen bins. Divisibility or digit tests need matched controls with the same 2-and-5 content (L3705).
11. **Clusters break independence.** Use a genome-shift permutation that preserves gene clusters and loop structure, not unit-merging within each set separately (L3721 flaw, L3725 fix).
12. **Thresholds must be reachable.** A 99.7th-percentile criterion needs at least 333 controls (L3705 flaw).
13. **Length confounds.** Compare against length-matched controls (L3721).

## E. Process
14. **Freeze, hash, run, commit output, then read names.** Failures stand; grader bugs are fixed only in the parser, with the original kept (L3637, L3581).
15. **Files are identified by their content,** not their names: swapped names (L3661), a wrong organism (L3669), an empty download (L3669), a missing file → void (L3701).
16. **Test the test.** A self-test row that cannot fail, or fails for the wrong reason, is a bug (phone 6.16: four identical strands).

## Summary
- **Sixteen standing rules distilled from recent failures,** grouped as: number claims; absence calls; similarity searches; statistics; process.
- **Each rule cites the round that taught it.**

## Potential leads for future research
- **[Rule audit]** Re-read Manuscripts 2 and 3 against rules 4–8. Mark every absence claim with its finder's measured sensitivity, or reword it as "not detected".
- **[Reader brief]** Attach these rules to the outside-reader brief as the methods appendix.
