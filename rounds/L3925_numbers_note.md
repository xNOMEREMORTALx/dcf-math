# DCF L3925 (note): do 7, 78, 79 and 401 in the potassium-channel results carry a triangular or cubic pattern?
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 21 November 2026

**Status: a check, not a test.** No prediction was graded and nothing enters the record. The numbers come from `rounds/L3917_tool_output.txt` and the set definitions in `rounds/dcf_genelevel_L3917.py`. They were computed in this session.

---

## 1. Where each number comes from
| number | what it is | fixed by nature, or by a choice? |
|---|---|---|
| **79** | pore-forming K⁺ genes in the set | **a choice:** my name pattern applied to GENCODE v49 |
| **7** | genes with excess > 0.3 in all three groups | **a choice:** the 0.3 threshold was mine |
| **0.78** | rank correlation, cell lines vs primary cells | **a measurement with error:** 0.779, 95% bootstrap range 0.65–0.86 |
| **401** | the 79th prime | **exact,** but it inherits 79's dependence on the definition |

### 79 moves with the definition
| gene-set choice | count |
|---|---|
| as used (Kv 40 + K2P 15 + Kir 16 + KCa/Slo 8) | **79** |
| drop KCNU1 (sperm-only Slo3) | 78 |
| drop KCNJ18 (named in 2010) | 78 |
| drop the "silent" Kv subunits (KCNF, KCNG, KCNS, KCNV; they form no channel alone) | 69 |
| Kv + Kir only | 56 |

**A biologist could defend 69, 78 or 79,** and the gene-naming committee keeps adding genes. So 79 = Z(Au) is a coincidence of my rule, not a property of the cell.

### 7 moves with the threshold
| threshold | 0.20 | 0.25 | **0.30** | 0.35 | 0.40 | 0.50 |
|---|---|---|---|---|---|---|
| genes above it in all three groups | 12 | 9 | **7** | 7 | 6 | 4 |

### 0.78 is not a fixed constant
- **The three correlations were 0.73, 0.78 and 0.66,** and each has a range of about ±0.1.
- **Reading "78" means picking one of the three and rounding it to two digits.**

## 2. Triangular and cubic checks (computed)
| number | triangular? | cube? |
|---|---|---|
| 7 | no (6, 10) | no |
| 17 (auxiliary K⁺) | no | no |
| 78 | **yes, T₁₂ = 12·13/2** | no |
| 79 | no | no |
| 96 (all K⁺) | no | no |
| 139 (all genes) | no (T₁₆ = 136) | no |
| 401 | no (T₂₇ = 378, T₂₈ = 406) | no |

**One hit (78 = T₁₂) out of seven numbers.** About 1 in 9 integers below 100 is triangular, so one hit is what chance gives.
- **78 is also the least stable of the numbers:** it is a rounded correlation.
- **So there is no triangular or cubic pattern in the counts.**

## 3. Where real geometry is in these results (established biophysics)
- **Pore-forming K⁺ channels are four-fold (square) assemblies.** Kv, Kir and KCa channels are tetramers. K2P channels are dimers of two-pore subunits that make the same four-fold pore.
- **The auxiliary subunits (KCNE, KCNIP, KCNAB, KCNMB) are not part of that square pore.** They are exactly the group that never shows the anchor excess (nine loop sets in a row). So the anchor result follows the four-fold pore genes. That is a real, if descriptive, link between gene geometry and the data.
- **In the selectivity filter, each K⁺ ion sits in a cage of 8 oxygen atoms shaped like a square antiprism, a twisted cube.** This is the "cubic" relationship in potassium biology.
- **Gold crystallises face-centred cubic (FCC), not body-centred cubic.** Its lattice constant is 4.078 Å, the "40782" in the project notes. Gold and potassium both have cubic geometry, but in different senses (a metal lattice vs an ion cage). Nothing in these data connects them.

## 4. Policy note
Per the DCF untrusted-numbers rule, I would not carry 79 ↔ Z(Au), 401 = prime(79) or 78 = T₁₂ into Manuscript 3. Each rests on a definition or rounding choice that the biology does not fix.

## Summary
- **79, 7 and 0.78 are set by my gene-naming rule, my threshold and rounding.** Small, defensible changes give 78, 69, 6, 9 or 0.73.
- **Of 7, 17, 78, 79, 96, 139 and 401, only 78 is triangular and none is a cube.** That is chance level.
- **The real geometry is the four-fold pore and the 8-oxygen square-antiprism cage of K⁺,** and the anchor excess follows those four-fold pore genes, not their auxiliary partners.

## Potential leads for future research
- **[Symmetry, done right]** Test pore-forming four-fold genes (K⁺ tetramers, HCN, CNG) against non-four-fold channel genes of similar size at CTCF anchors. Pre-registered; the L3885 symmetry test grouped channels differently.
- **[Primary-cell baseline]** The promoter-proximity test from L3921 is still the next data step.
- **[Gold control]** If a gold link is wanted, pre-register a count fixed by nature (e.g. number of gold-binding proteins in UniProt), not one fixed by my definitions.
