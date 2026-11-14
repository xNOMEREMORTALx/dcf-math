# DCF L3481: Blind test across all other animals in Swiss-Prot (58,949 proteins, graded by UniProt). 13 of 14 pass; both negative controls hold
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 14 November 2026

**Data:** `stream_24.gz`, 13.8 MB. It holds 58,949 reviewed animal proteins from every species except the six already used. The largest contributors are rat (8,239), cow (6,055) and the frogs *Xenopus laevis* and *X. tropicalis*. One entry is Neanderthal, a different organism ID from human, so it stays in.

**Procedure:**
1. Five frozen hashes matched.
2. The v6 tool read only Entry and Sequence; its output was committed and pushed first.
3. Graded with truth v4, UniProt's curated "Protein families": `rounds/L3481_grade.py` → `rounds/L3481_grade_output.txt`.

---

## Results (PREREGISTERED_L3477_metazoa)
| # | prediction | result |
|---|---|---|
| M1 | calcium-channel calls correct (≥ 90%) | **22/24 PASS** |
| M2 | sodium-channel calls correct | **17/17 PASS** |
| M3 | potassium/HCN calls correct | **86/86 PASS** |
| M4 | voltage-gated Na + Ca + K found (≥ 75%) | **119/125 = 95% PASS** |
| M5 | K2P calls correct | **18/18 PASS** |
| M6 | K2P found (≥ 60%) | **18/19 PASS** |
| M7 | glutamate-receptor calls correct | **47/47 PASS** |
| M8 | glutamate receptors found | **47/55 PASS** |
| M9 | iron-hydroxylase calls correct | **15/15 PASS** |
| M10 | iron hydroxylases found | **15/16 PASS** |
| M11 | pump calls (Na/K, Ca, Cu) correct | **60/64 PASS** |
| M12 | metal pumps found | **60/62 PASS** |
| **M13** | **negative control: no sodium calls on 919 nematode proteins** | **0 calls: PASS** |
| M14 | no sodium↔calcium swaps among 41 true Na/Ca channels | **2 swaps: FAIL** |

**13 of 14 pass.** Across 58,949 proteins the tool made 351 class calls, and **345 agree with UniProt's independent classification.**

## The failure, and the other "wrong" calls
- **M14, a real error:**
  - **What happened:** rat and horse **Scn4a** (the muscle sodium channel) were called **calcium**. Their domain-I outer loop carries repeats such as S-N-D-T-W and S-Q-E-S-W. Each one matches the calcium-ring motif outside the pore, which pushed the ring count to 3.
  - **It's the same channel** that was "undecided" in mouse (L3429). In these orthologs the extra repeats tipped it the wrong way.
  - **v7 fix (development, frozen for the next test):** in the 4-domain branch, the **sodium lysine loop (the K of DEKA) decides first.**
    - No calcium channel in any data set carries that lysine (checked on all seven data sets).
    - The only other ≥ 1,500-aa proteins with the loop (ASPM, DIP2A, collagen XXIV) lack a voltage sensor, so they never reach this branch.
- **M11's four "wrong" pump calls are, in fact, correct:**
  - two insect SERCA calcium pumps, a brine-shrimp pump, and hamster ATP7A (a copper pump);
  - UniProt lists their family without the subfamily ("Type IIA", "Type IB"), so the frozen truth rule could not credit them. The prediction passed anyway.
- **Misses:**
  - **Glutamate receptors:** insect "ionotropic receptors" (IR8a, IR21a, IR75a, IR76b), smell and taste receptors of the same family with a modified gate, and frog/duck "kainate-binding proteins."
  - **Others:** one flatworm tyrosine hydroxylase, the sodium sensor Scn7a, and Kcng3 (a silent subunit).

## Reading
- **Across the animal kingdom in Swiss-Prot,** frogs, mammals, birds, insects, molluscs and nematodes, the frozen rules read the metal gates of nerves from sequence alone, with **98% agreement with UniProt's curated classification.**
- **Both controls held where they could be tested:**
  - **no sodium channel in any of 919 nematode proteins** (worms have none);
  - **the potassium, K2P, glutamate-receptor, iron-enzyme and sodium calls were 100% precise.**
- **The descriptive spread is uneven.** Most calls fall in chordates and arthropods, because Swiss-Prot's reviewed entries are concentrated there. Sponges, comb jellies and placozoans contribute almost nothing. The question of *which metal gates existed before nerves* needs their full proteomes.

## Running tally (nerve-chemistry blind tests)
| test | gradeable passed | truth |
|---|---|---|
| mouse | 10/10 | names |
| zebrafish | 17/21 | names |
| chicken | 13/14 | names + descriptions |
| fruit fly | 5/13 | names + descriptions |
| nematode | 9/9 | UniProt families |
| **all other animals** | **13/14** | **UniProt families** |
| **total** | **67/81** | |

## Record
**+13 passed, 1 failed. 392 of 544 passed, plus 3 split.**

## Summary
- **On 58,949 reviewed animal proteins the frozen tool had never seen, 13 of 14 predictions passed.** 345 of 351 calls agree with UniProt, an independent judge, and there were **no sodium calls in 919 nematode proteins.**
- **The one real error:** two orthologs of the muscle sodium channel were read as calcium, because of calcium-like repeats outside the pore. The fix is frozen for the next test: the sodium lysine decides first.

## Potential leads for future research
- **[Before nerves]** Full proteomes of a sponge (*Amphimedon*), a placozoan (*Trichoplax*), a comb jelly and a choanoflagellate. Which metal gates predate the nervous system? This needs an independent truth (InterPro) or a pre-stated biological expectation.
- **[v7 test]** A blind test of the lysine-first rule on new sodium-channel sequences (e.g. TrEMBL Nav entries from reptiles and fishes).
- **[IR family]** Insect smell receptors evolved from glutamate receptors. Map how the gate motif changes in that family (descriptive).
- **[Manuscript 2]** The all-animals test, graded by UniProt, becomes the headline result. Update the outline.
