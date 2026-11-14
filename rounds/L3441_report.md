# DCF L3441: Blind test in a fish. Nerve channels sorted by metal ion and the dopamine/serotonin iron enzymes found across ~450 million years: 10 of 11 gradeable predictions pass
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 13 November 2026

**Data:**
- **`zebrafish.1.rna.fna.gz`:** 48.7 MB, 16,816 NM_ records, all *Danio rerio*.
- **`zebrafish.2.rna.fna.gz`:** 51.3 MB, but it holds **only XM_ (computer-predicted) records and no NM_ records.** The frozen scripts read NM_ only, so file 2 contributed nothing. This follows the pre-registration as written.

**Procedure:**
1. The script and pre-registration hashes were checked against `LEDGER.md` (all 5 matched).
2. Tool output without gene names was committed and pushed first (`rounds/L3441_*_tool.txt`).
3. Grading: `rounds/L3441_grade.py` → `rounds/L3441_grade_output.txt`.

---

## Results
| # | prediction | result |
|---|---|---|
| Z1 | calcium calls are cacna1 (≥ 90%) | **6/6 PASS** |
| Z2 | sodium calls are scn·a (all) | **6/6 PASS** |
| Z3 | potassium/HCN calls correct (v3, ≥ 90%) | **2/2 PASS** |
| Z4 | family genes given their own metal (v3, ≥ 75%) | **14/15 PASS** |
| Z5 | K2P precision | 1 call (kcnk15, correct): **ungradeable** (needs ≥ 2) |
| Z6 | K2P recall (≥ 70%) | **1/1 PASS** |
| Z7 | potassium/HCN calls correct (v4, ≥ 90%) | **2/3 FAIL** |
| Z8 | family genes found (v4, ≥ 80%) | **14/15 PASS** |
| Z9 | glutamate-receptor precision | 1 call (grin2ca, correct): **ungradeable** |
| Z10 | glutamate-receptor recall (≥ 75%) | **1/1 PASS** |
| Z11 | NMDA precision | 1 call (grin2ca, correct): **ungradeable** |
| Z12 | NMDA recall (≥ 75%) | **1/1 PASS** |
| Z13 | iron hydroxylase precision (≥ 90%) | **5/5 PASS** |
| Z14 | iron hydroxylase recall (≥ 75%) | **5/6 PASS** |

**10 of 11 gradeable predictions pass; 3 are ungradeable.** The curated NM_ set holds only one K2P gene and one glutamate receptor.

**What the fish shows.**
- **Sodium vs calcium works in fish.** All six calcium channels (cacna1aa, ab, da, fb, sa, sb) and all six sodium channels (scn1laa, scn1lab, scn5lab, scn8aa, scn8ab, scn12aa) are sorted by their pore rings, with no errors.
  - Fish have **duplicated** many channel genes (the "a/b" copies). Both copies kept the same metal gate.
- **The iron site of the neurotransmitter enzymes is conserved across ~450 million years.** pah, th2, tph1a, tph1b and tph2 all carry C-H-E-L-L-G-H. The one miss is zebrafish **th**, whose site reads **V**-H-E-L-L-G-H: the cysteine became a valine, but the iron-binding H-x₄-H is unchanged.

**The failure (Z7).**
- **The extra call:** v4's new weak-sensor route made one potassium call outside the named families, on an **unnamed zebrafish gene, si:ch73-334d15.4.**
- **It looks like a real channel.** It carries the potassium filter **T-V-G-Y-G-D** and a voltage-sensor-like stretch. Its closest mouse relatives (by shared 5-letter pieces) are **Kcnc4, Kcnc2, Kcnc1, Kcnc3**, the Kv3 potassium channels.
- **But it still counts as a failure.** The frozen truth rule counts only named families, so the prediction **fails, and it stays failed.** It is not regraded after the fact.
- **The lesson:** in a less-annotated genome, the rule can find channels before the naming catches up. A truth rule based only on names cannot credit that.

**The other miss:** hcn5 (Z4, Z8). The record encodes only 305 aa, too short to contain the full channel.

## Record
**+10 passed, 1 failed** (Z5, Z9, Z11 ungradeable, not counted). **345 of 484 passed, plus 3 split.**

## Summary
- **In a fish, about 450 million years from mammals, the tools read the metal gates of nerve channels from mRNA with no sodium/calcium errors.** The duplicated fish genes kept their metal.
- **The iron site of the enzymes that make dopamine and serotonin is conserved across that span,** with one cysteine-to-valine swap in fish tyrosine hydroxylase.
- **One prediction failed:** the new weak-sensor route called an unnamed gene that looks like a Kv3 potassium channel but is not named as one. It is counted as a failure, as frozen.
- **Three predictions could not be graded,** because the fish's curated records hold too few K2P and glutamate-receptor genes.

## Potential leads for future research
- **[XM records]** Zebrafish file 2 holds only predicted (XM_) records. A new pre-registered test could include XM_ transcripts, which would give enough K2P and glutamate receptors to grade.
- **[Unnamed channels]** List every unnamed gene that the channel rules call, in fish and other less-studied species, and compare each with its nearest named relative.
- **[FeHyd2]** Widen the iron-site finder to `[CV]-H-E-[LI]-L-G-H`; this needs a fresh blind test.
- **[Phone]** Add the iron-site and NMDA finders to menu 34 (both 100% precise in every test so far).
- **[Iron trilogy]** One figure of the three iron roles: energy ladder, DNA-repair switch, neurotransmitter hydroxylase.
