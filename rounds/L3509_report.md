# DCF L3509: Comb jellies. 3 of 3 pass; the independent nerve lineage also reads E, not K
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 14 November 2026

**Data:** `stream_24.gz` (8.3 MB): 25,809 UniProt Ctenophora proteins. Almost all are from *Mnemiopsis leidyi* (25,263); the rest come from ~20 other comb jellies.

**Procedure:**
1. Four frozen hashes matched.
2. The v7 tool read only Entry and Sequence; its output was committed and pushed first.
3. Grading: `rounds/L3509_grade.py` → `rounds/L3509_grade_output.txt`.

---

## Results (PREREGISTERED_L3505_ctenophore)
| # | prediction | result |
|---|---|---|
| T1 | no sodium calls | **0: PASS** |
| T2 | every 4-domain voltage-sensor protein with the A-T-F-x-G-W loop has x ≠ K | **8 of 8 read E: PASS** |
| T3 | ≥ 3 potassium channels | **123: PASS** |

**3 of 3 pass.**

## Reading
- **The comb jelly's three "sodium channel proteins" read I-A-L-Y-Q-V-A-T-F-E-G-W.** That is the same E as the choanoflagellate, *Trichoplax* and the sea anemone. Its five calcium-channel-like proteins (CCH1-type) read A-T-F-**E**-G-W too.
- **So the K is absent in both lineages outside the bilaterians that have nerves,** cnidarians and comb jellies. It appears only in bilaterians.
- **Comb jellies have a striking potassium expansion:** 123 potassium-channel calls (the anemone has 46; humans have about 40 voltage-gated K genes). They also have 19 leak channels and 29 glutamate receptors.
- **Every call's UniProt name agrees with its metal** (descriptive, not graded):
  - all three pump classes: Na⁺/K⁺-ATPase α, calcium-transporting ATPase, Cu⁺ transporter;
  - all 19 K2P ("potassium channel domain");
  - glutamate receptors where the name is known.

## Figure 4 updated (`figures/L3509_EtoK.png`)
The comb jelly is added: **E** in four lineages at or before the first nerves (choanoflagellate, placozoan, sea anemone, comb jelly), **K** in every bilaterian, **N** in the sensor.

## Manuscript 2 v0.5 and audit
- **Audit:** recomputes **81 of 95** (`rounds/L3509_audit2_out.txt`).
- **Draft:** `notes/Manuscript_nerve_metals_draft_v0.5.md` adds §3.7 on comb jellies and the new Figure 4.

## Record
**+3 passed. 406 of 558 passed, plus 3 split.** Nerve-chemistry blind tests: **81 of 95.**

## Summary
- **In 25,809 comb-jelly proteins: no sodium channel, and every sodium-type channel reads E at the ring position.** That holds in the second nerve lineage too.
- **The lysine K that makes the fast nerve sodium channel appears only in bilaterians.** The comb jelly instead has a very large potassium-channel set (123).
- **Figure 4 and Manuscript 2 (v0.5) are updated;** the audited total is 81 of 95.

## Potential leads for future research
- **[K expansion]** Why does a comb jelly carry about 3× more potassium channels than a human? Sort its K calls by filter type (descriptive).
- **[Outside reader]** Manuscript 2 v0.5 is ready for review.
- **[Bilaterian base]** The earliest bilaterians (an acoel flatworm such as *Hofstenia*, or *Xenoturbella*): do they already read K? This would date the E→K step more closely.
