# DCF L3533: Dating the E → K step. 2 of 5 pass. Protostomes carry K, but the sea urchin and acorn worm still carry E, so a single early origin with no losses is ruled out
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 14 November 2026

**Data:** `26.gz` (38.4 MB), 125,720 proteins:

| species | group | proteins |
|---|---|---|
| sea urchin (*Strongylocentrotus*) | deuterostome | 35,496 |
| brachiopod (*Lingula*) | protostome | 34,462 |
| annelid (*Capitella*) | protostome | 31,954 |
| acorn worm (*Saccoglossus*) | deuterostome | 23,808 |

**Procedure:**
1. Hashes matched.
2. The v7 tool output was committed and pushed before organisms were attached.
3. Grading: `rounds/L3533_grade.py` → `rounds/L3533_grade_output.txt`.

---

## Results (PREREGISTERED_L3529_EK_dating)
| # | prediction | result |
|---|---|---|
| D1 | brachiopod has a sodium (DEKA) channel | **5: PASS** |
| D2 | annelid has a sodium (DEKA) channel | **1: PASS** |
| D3 | acorn worm has a sodium (DEKA) channel | **0: FAIL** |
| D4 | sea urchin has a sodium (DEKA) channel | **0: FAIL** |
| D5 | every species has an A-T-F-K-G-W loop | **FAIL** (acorn worm and sea urchin have none) |

**2 of 5 pass. The hypothesis (one origin of K in the ancestor of protostomes and deuterostomes, never lost) is not supported.**

## What the sequences show
| species | domain-III loop of its "sodium channel protein" |
|---|---|
| brachiopod *Lingula* | LALLQV A-T-F-**K**-G-W (all 5) |
| annelid *Capitella* | LALLQV A-T-F-**K**-G-W, plus an E-type paralog LALLQV A-T-F-**E**-G-W |
| acorn worm *Saccoglossus* | LALFQV A-T-F-**E**-G-W |
| sea urchin *Strongylocentrotus* | VALFQV **T**-T-F-**E**-G-W, found after grading. The frozen extraction regex required A/S first and missed this row; it read **E** either way, so the grade is unchanged |

- **K is found** in every protostome tested (brachiopod, annelid, fly, nematode lineage) and in vertebrates.
- **K is absent** in the two ambulacrarian deuterostomes (acorn worm, sea urchin), whose sodium-type channels read **E**, like the early animals.
- **Two explanations fit:**
  1. **Two origins:** K arose separately in the protostome line and in the chordate line (convergent evolution of the same E → K change at the same position).
  2. **One origin and a loss:** K arose once in the protostome/deuterostome ancestor and was lost in echinoderms and hemichordates.
- **These data cannot tell them apart.** A cephalochordate (lancelet *Branchiostoma*) or a tunicate would help: if they carry K while their deuterostome relatives carry E, the chordate origin is narrowed.

**Figure 4** is updated (`figures/L3533_EtoK.png`) with all four species, grouped as early lineages, deuterostome invertebrates (E), and protostomes and vertebrates (K).

## Manuscript 2 v0.7 and audit
- **Audit:** the recount is **83 of 100**, now including this failed test.
- **Draft:** §3.9 reports the failure and both explanations.

## Record
**+2 passed, 3 failed. 408 of 563 passed, plus 3 split.**

## Summary
- **The brachiopod and the annelid carry the K, as predicted. The acorn worm and the sea urchin do not:** their sodium-type channels read E, like the earliest animals.
- **So K did not simply arise once in the common bilaterian ancestor and stay.** Either it arose more than once (protostomes and chordates), or it was lost in echinoderms and acorn worms.
- **Three predictions failed,** and the failure is recorded in the record, the paper and the figure.

## Potential leads for future research
- **[Chordate base]** A lancelet (*Branchiostoma floridae*) and a tunicate (*Ciona*). Pre-register "K present in both" to test where the chordate K begins.
- **[Convergence test]** Compare the codons for K in protostomes and vertebrates. Different codon paths (AAA vs AAG, and different neighbouring changes) would favour two independent origins; that is descriptive.
- **[Regex note]** The frozen extraction pattern [AS]-T-[FY] missed the sea urchin's T-T-F-E-G-W. Future extractions should use [AST]-T-[FY].
