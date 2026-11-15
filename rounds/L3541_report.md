# DCF L3541: Triangle-file audit, part 2. Neurotransmitter weights, repetend sums and the small iron/copper proteins all check out; two repetend sums follow from Midy's theorem; "11/7 ≈ φ" is overstated
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 14 November 2026

**Leads:** [Neurotransmitter table], [Cycle lens on 1/p sums], [Small iron proteins].
- **Output:** `rounds/L3541_triangle_audit2.py` → `rounds/L3541_triangle_audit2_out.txt`.
- **No predictions graded.**

---

## A. Neurotransmitters and hormones: all 8 correct
| molecule | formula | MW | claim |
|---|---|---|---|
| dopamine | C₈H₁₁NO₂ | 153.18 | 153 ✓ |
| acetylcholine (cation) | C₇H₁₆NO₂⁺ | 146.21 | 146 ✓ |
| norepinephrine | C₈H₁₁NO₃ | 169.18 | 169 ✓ |
| serotonin | C₁₀H₁₂N₂O | 176.22 | 176 ✓ |
| glutamic acid | C₅H₉NO₄ | 147.13 | 147 ✓ |
| GABA | C₄H₉NO₂ | 103.12 | 103 ✓ |
| epinephrine | C₉H₁₃NO₃ | 183.21 | 183 ✓ |
| cortisol | C₂₁H₃₀O₅ | 362.47 | 362 ✓ |

## B. Repetend digit sums S(1/n): all 7 correct (exact long division)
| n | period | S | claim | why |
|---|---|---|---|---|
| 17 | 16 | 72 | ✓ | **Midy's theorem**: prime with even period, so S = 9 × 16/2 |
| 89 | 44 | 198 | ✓ | **Midy**: 9 × 44/2 |
| 43 | 21 | 90 | ✓ | odd period: not forced by Midy |
| 437 = 19 × 23 | 198 | 891 | ✓ | equals 9 × 198/2 although 437 is composite |
| 153 = 9 × 17 | 16 | 65 | ✓ | |
| 306 | 16 (1 pre-digit) | 73 | ✓ | |
| 372 | 15 (2 pre-digits) | 54 | ✓ | |

- **The cycle lens again:** S(1/17) = 72 and S(1/89) = 198 are **guaranteed** by Midy's theorem, which says the two halves of an even prime period sum to 999…9.
- **That makes them consequences, not coincidences.** The same applies to any "S(1/p) = 9L/2" landmark for a prime p with even period.

## C. Fibonacci statements
- **F(9)/2 = 17, F(12)/2 = 72, F(15)/2 = 305:** correct.
- **The file's recurrence h[k] = 4·h[k−1] + h[k−2]** is the standard identity F(n+3) = 4F(n) + F(n−3), checked to n = 55. It is true for all n.
- **"11/7 ≈ φ is a genuine near-identity" is overstated.**
  - 11/7 = 1.5714 is **2.9% below** φ = 1.6180.
  - 11/7 is not a ratio of Fibonacci numbers.
  - The nearby Fibonacci ratio 13/8 = 1.625 is 0.43% off.
  - Recommendation: drop "near-identity."

## D. Small iron/copper proteins: all 3 correct (UniProt mature chains)
- *C. pasteurianum* **ferredoxin** P00195: chain 2–56 = **55** ✓.
- *C. pasteurianum* **rubredoxin** P00268: **54** ✓.
- Poplar **plastocyanin** P00299: chain 70–168 = **99** ✓.

## Tally of the whole triangle-file audit (L3537 + L3541)
- **Correct:**
  - 26 molecular weights;
  - 17 Fibonacci digit sums;
  - 7 repetend sums;
  - 3 Fibonacci halvings;
  - the F(24k) mod-9 theorem;
  - the F(3k) recurrence;
  - 4 protein lengths (cytochrome c, ferredoxin, rubredoxin, plastocyanin).
- **Wrong:** 3 protein lengths (ATP synthase β "510", complex IV "520", complex II "140").
- **Overstated:** 2 claims ("11/7 ≈ φ near-identity", "golden angle ≈ α⁻¹" presented as more than a coincidence).
- **Explained by cycles:** the self-encoder classes (Pisano mod 9), and S(1/17), S(1/89) (Midy).
- **Not testable as stated:** the names attached to numbers (e.g. "gold_guide", "Monster²"). They are labels, not claims that can pass or fail.

## Record
No predictions graded. **410 of 565 passed, plus 3 split.**

## Summary
- **The rest of the triangle file's checkable numbers are correct:** all 8 neurotransmitter and hormone weights, all 7 repetend digit sums, the Fibonacci halvings, and the three small iron/copper protein lengths.
- **Two of the repetend "landmarks" (72 and 198) are forced by Midy's theorem.** The self-encoder classes are forced by the Fibonacci cycle: the cycle lens explains several DCF regularities.
- **To correct in the file:**
  - drop three protein lengths;
  - present 11/7 vs φ (2.9% apart) and the golden angle vs α⁻¹ (0.34% apart) as coincidences, not identities.

## Potential leads for future research
- **[Cycle catalog]** Go through the DCF verified-results catalog and mark each regularity as *forced* (Midy, Pisano, divisibility) or *unexplained*. The unexplained ones are where genuine discoveries would sit.
- **[1/43 and 1/437]** S(1/437) = 9L/2 holds for a composite. Find the condition for composites (e.g. 10^(L/2) ≡ −1 mod n), and pre-register which composites < 1,000 satisfy it.
- **[Manuscript polish]** Outside reader for both papers.
