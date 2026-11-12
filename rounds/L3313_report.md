# DCF L3313: the Kozak start-codon rule fails decisively (0 of 3), and the test shows the current rule is already right for 97.8% of human proteins
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 12 November 2026

**Data:** `human_protein_1_2.zip`, NCBI's human.1 and human.2 protein files (11,728 proteins), used as the answer key.

**Pre-registration:** `PREREGISTERED_L3309_orfstart.txt` (`290b44cd…c2e2`); script `dcf_orfstart_L3309.py`, hash verified against the ledger (`63ad96c1…4809`).

---

## 1. Results
**Test set:** 5,083 human genes from RNA files 1–4 (one transcript per gene) whose reading frame ends exactly where an NCBI protein ends.

| measure | rule A (current: longest frame, first ATG) | rule K (first ATG with A/G at −3) |
|---|---|---|
| **exactly right** | **4,972 (97.8%)** | 4,294 (84.5%) |
| too long (starts early) | 111 (2.2%) | — |
| too short (starts late) | 0 | — |

| id | prediction | result | verdict |
|---|---|---|---|
| K1 | rule K exact more often than rule A | 84.5% vs 97.8% | **FAIL** |
| K2 | rule K exact in ≥ 50% of rule A's overshoots | 29 of 111 (26%) | **FAIL** |
| K3 | breaks ≤ half of fixes | **707 breaks vs 29 fixes** | **FAIL** |

## 2. Why it failed [development, after grading]
| context | true starts (4,836) | false upstream first ATGs (106) |
|---|---|---|
| purine (A/G) at −3 | **84.6%** | **64.2%** |
| G at +4 | 48.7% | 42.5% |

- **15% of real human start codons have a C or T at −3,** and rule K skipped all of them. That is the 707 breaks.
- **Most false upstream ATGs (64%) also have a purine at −3,** so the rule can't tell them apart. SHH, whose false ATG has T at −3, was the exception, not the pattern.
- **The Kozak context is a preference, not a rule.** Ribosomes weigh it alongside other signals, and one base cannot carry the decision.

## 3. What we learned that is useful
- **The current tools' protein positions are reliable.** The longest-frame/first-ATG rule gives exactly the right protein for **97.8%** of human genes and never starts too late. Positions reported by the motif scanner, the hedgehog and nerve tools and phone menu 32 inherit that accuracy.
- **The 2.2% that start early are a known biological case:** an extra in-frame ATG upstream (as in SHH). These are best flagged rather than "fixed".
- **Decision:** rule A stays in all tools. Rule K is not adopted.

## Record
**This round:** 3 graded, 0 passed.

**Total: 309 of 442 pre-registered predictions passed, plus 3 split.**

## Summary
- **The new start-codon rule failed clearly:** it fixed 29 genes but broke 707, because about 1 in 7 real human start codons lacks the A/G that the rule demanded.
- **The good news from the same test:** our existing method picks exactly the right protein for 97.8% of 5,083 human genes. The SHH problem (starting 3 codons early) affects only about 2%.
- **The tools stay as they are.** The new rule is not adopted.

## Potential leads for future research
- **[ORF flag]** Instead of changing the start, flag proteins whose first ATG has an in-frame ATG within 10 codons downstream ("start may be early"), and report both positions in the motif scanner.
- **[Exon conservation]** Human–mouse coding exon lengths (PAX6, OTX2, FOXG1); SHH's exons 1 and 2 matched exactly.
- **[Neuro b]**, **[hedgehog2]**: the corrected motifs await fresh data (mouse RNA; zebrafish/chicken hedgehogs).
