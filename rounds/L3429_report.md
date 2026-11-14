# DCF L3429: Blind test on mouse file 3. Nerve channels sorted by metal ion, and the anaesthetic-target leak channels found: 10 of 10 predictions pass
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 13 November 2026

**Data:** `mouse.3.rna.fna.gz` (18.2 MB).
- 14,378 NM_ transcripts, all *Mus musculus*.
- **No accession overlaps mouse files 1–2.** Mouse file 4 was dropped beforehand (the link was unavailable), as the pre-registration requires.

**Procedure:**
1. The three script hashes were checked against `LEDGER.md` (all matched).
2. Tool output without gene names was committed and pushed first (`rounds/L3429_*_tool.txt`).
3. Names were read afterwards.
4. Grading: `rounds/L3429_grade.py` → `rounds/L3429_grade_output.txt`.

---

## Results (PREREGISTERED_L3425 + A1 + A2)
| # | prediction | v1 | v2 |
|---|---|---|---|
| N1 | called **calcium** are Cacna1 (≥ 90%) | **4/4 PASS** | **4/4 PASS** |
| N2 | called **sodium** are Scn·a (all) | **5/5 PASS** | **5/5 PASS** |
| N3 | called **potassium/HCN** are K/HCN genes (≥ 90%) | **14/14 PASS** | **14/14 PASS** |
| N4 | family genes given their own metal (≥ 75%) | **23/28 = 82% PASS** | **23/28 = 82% PASS** |
| N5 | **K2P leak** calls are Kcnk (≥ 90%) | **7/7 PASS** | — |
| N6 | Kcnk genes found (≥ 70%) | **7/7 = 100% PASS** | — |

**All 10 predictions pass. The tools made 30 metal calls, and none was wrong.**
- **Calcium:** Cacna1a (P/Q-type, transmitter release), Cacna1c and Cacna1d (L-type, heart and brain), Cacna1h (T-type, rhythm).
- **Sodium:** Scn1a, Scn2a, Scn8a (brain), Scn5a (heart), Scn10a (pain nerves).
- **Potassium:** 11 Kv channels, including Kcnh2 (hERG, the heart-rhythm channel).
- **HCN pacemakers:** Hcn1, Hcn2, Hcn4.
- **Leak (K2P):** all seven Kcnk genes in the file: Kcnk2 (TREK-1), Kcnk3 and Kcnk9 (TASK-1, TASK-3), Kcnk1, 5, 6, 13. TREK-1 and TASK channels are among the channels that general anaesthetics act on.

**The five misses (N4):**
- **Kcnq2 and Kcnq4:** their voltage sensor has four charges, not five (known gap, lead [Kcnq]).
- **Kcng3 and Kcng4:** silent subunits.
- **Scn4a (muscle sodium channel):** labelled "undecided". It has a second chance match to the calcium ring (ring 2), so the rule declined to call it. That counts as a miss, but not as a wrong call.

**Honest notes.**
- **v1 and v2 gave identical calls on this file.** It contained no Brwd3-type decoy, and only one Kcnh gene, so the header fix made no difference. They count as separate pre-registered predictions, but they are **not independent evidence.** Read the table as 6 distinct tests, all passed.
- **Kcnv1 and Kcnv2 count as correct potassium calls** under the frozen truth rule, though they are modifier subunits.

## Tools
- `dcf-genefinder` gains **`dcf_neurometal.py`** (v2) and **`dcf_k2p.py`**. Both have now passed a blind test.
- **Usage:**
  ```
  python3 -I dcf_neurometal.py grade file.rna.fna.gz
  python3 -I dcf_k2p.py grade file.rna.fna.gz
  ```

## Record
**+10 passed. 335 of 473 passed, plus 3 split.**

## Summary
- **From raw mouse mRNA it never saw, the tools sorted the nervous system's ion channels by the metal they carry: calcium, sodium, potassium and the pacemakers.** Every one of the 30 calls was right, and 23 of the 28 channel genes in the file were found.
- **The potassium leak channels that anaesthetics act on were found completely:** all 7, with no false hits.
- **The misses are already understood:** Kv7 channels (weaker voltage sensor), silent subunits, and one muscle sodium channel the rule declined to call.

## Potential leads for future research
- **[Kcnq]** A Kv7-specific signature (4-charge sensor plus the T-I-G-Y-G filter) to close the main recall gap.
- **[Scn4a]** Why the muscle sodium channel shows a second calcium-ring match. Tighten the ring to pore-loop positions only (development, then a new blind test).
- **[Phone]** Add `neurometal` and `k2p` as phone menu items.
- **[Neuro iron]** Iron enzymes that make dopamine and serotonin.
- **[NMDA metals]** The magnesium-block and zinc sites of glutamate receptors.
- **[Second species]** Repeat on another vertebrate (e.g. zebrafish or chicken) to test across a wider evolutionary span.
