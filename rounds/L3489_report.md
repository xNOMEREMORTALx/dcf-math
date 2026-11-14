# DCF L3489: The sodium/calcium decision on 24,796 unseen vertebrate channels. 4 of 4 pass; 4 swaps in 23,994 calls
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 14 November 2026

**Data:** `stream_24.gz` (10.7 MB), UniProt unreviewed (TrEMBL) vertebrate proteins named "sodium channel protein" or "calcium channel subunit alpha": 33,049 rows.

**The pre-registered filter (amendment 1)** was applied before the tool:
- 1,500–3,500 aa;
- human, mouse, zebrafish and chicken removed.

That leaves **24,796 proteins.** The filtered file given to the tool holds **only Entry and Sequence.**

**Procedure:**
1. Hashes matched.
2. The v7 and v6 outputs were committed and pushed before any name was read.
3. Grading: `rounds/L3489_grade.py` → `rounds/L3489_grade_output.txt`.

---

## Results (PREREGISTERED_L3485_navcav)
| # | prediction | result |
|---|---|---|
| V1 | Na↔Ca swaps ≤ 1% (v7) | **4 of 23,994 = 0.02% PASS** |
| V2 | sodium recall ≥ 90% | **9,229 / 9,886 = 93.4% PASS** |
| V3 | calcium recall ≥ 90% | **14,761 / 14,910 = 99.0% PASS** |
| V4 | v7 swaps fewer than v6 | **4 vs 44 PASS** |

**4 of 4 pass.**
- **The lysine-first rule removed 40 of the 44 swaps** that the previous rule made. Those were sodium channels read as calcium, the same Scn4a-type error as in L3481.
- **The four remaining swaps:**
  - two proteins named "sodium channel protein" called calcium;
  - two T-type calcium channels called sodium.

## Figure 2 for Manuscript 2
`figures/L3489_blind_tests.png`: all eight blind tests, passed against gradeable, coloured by who did the grading (our name rules, or UniProt independently).

## Manuscript 2 v0.2 and audit
- **Audit:** `rounds/L3485_audit2.py` now includes this test and recomputes **71 of 85** (`rounds/L3489_audit2_out.txt`).
- **Draft:** `notes/Manuscript_nerve_metals_draft_v0.2.md` has the new numbers, the TrEMBL result in the abstract, and the table row.

## Record
**+4 passed. 396 of 548 passed, plus 3 split.**

## Summary
- **Across 24,796 vertebrate sodium and calcium channel sequences the tool had never seen,** the frozen lysine-first rule confused sodium with calcium only **4 times in 23,994 calls (0.02%).** It found 93% of the sodium channels and 99% of the calcium channels.
- **The fix made after the all-animals failure removed 40 of 44 errors,** confirmed blind.
- **Manuscript 2 is at v0.2,** with its main figure and an audited total of 71 of 85.

## Potential leads for future research
- **[Four swaps]** Look at the two T-type calcium channels called sodium (descriptive): do they carry a lysine in a pore loop?
- **[Na recall]** 657 sodium proteins were not called. Many TrEMBL entries are fragments or splice forms missing the voltage sensor or a pore loop. Measure how many lack each motif (descriptive).
- **[Before nerves]** Sponge, placozoan and comb-jelly proteomes.
- **[Figures 1 and 3]** The motif panel and battery balance for Manuscript 2.
