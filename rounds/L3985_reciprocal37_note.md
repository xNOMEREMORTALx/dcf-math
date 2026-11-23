# DCF L3985 (note): 1/37, 2701, the π window 1170–1202 and the number 11. Every claim checked with mpmath, and a check against DNA's helix
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 23 November 2026

**Status: verification and context, not a pre-registered test.** Nothing enters the record.
- **The π positions** were checked with the project's mpmath rule (12,000 digits).
- **The arithmetic** was checked with sympy.

---

## 1. Gary's claims, checked
| claim | check | status |
|---|---|---|
| 1/37 = 0.027027… | 0.027027027027027 | ✔ exact |
| 2701 = 37 × 73 = T₇₃ (the 73rd triangular number) | 37·73 = 2701 = 73·74/2 | ✔ exact |
| 117 = sum of the Fibonacci "wheel of 24" | Fibonacci digital roots repeat every 24 (Pisano period mod 9 = 24); one cycle sums to 117 | ✔ exact |
| π digit 1170 is a 5 | 5 | ✔ (mpmath) |
| the next 5 is at position 1202 | digits 1171–1201 contain no 5; digit 1202 = 5 | ✔ (mpmath) |
| 1202 is one above the centroid 1201 | 1201 is prime; digit 1201 = 8 | ✔ |
| 401 first occurs at position 1197 | first position = 1197 | ✔ (mpmath) |
| sum of digits 1170–1202 | 127 | ✔ (matches the project notes) |

**All of the claimed facts are correct.**

## 2. How unusual is the 5…5 window?
A run of 32 or more digits between consecutive 5s, as from 1170 to 1202:
- **occurs 19 times in the first 5,000 digits of π;**
- **random digits would give about 20.**

**So the window itself is ordinary.** What makes it notable is only that it contains 401's first appearance. The project's own 2026-09 test put that at an ordinary position (geometric-null CDF 0.70).

## 3. New exact links found while checking (Gary asked about 11)
| fact | value | type |
|---|---|---|
| 27 × 37 = 999 | so 1/37 = 0.**027** repeating, and 1/27 = 0.**037** repeating: each one's digits are the other number | exact |
| 27 = 3³ | **a cube**, the "cubic" relationship asked about earlier | exact |
| 111 = 3 × 37 and 11 = 11 | 37 divides the repunit R₃ = 111; 11 *is* R₂ | exact |
| 11111111 = 11 × 73 × 101 × 137 | **73 and 11 divide the same repunit, R₈** | exact |
| period of 1/2701 | **24**: lcm(3, 8), from 1/37 (period 3) and 1/73 (period 8) | exact |
| one period of 1/2701 | 000370233246945575712699, digit sum **99 = 9 × 11** | exact |

**The new item:**
- **1/2701 repeats every 24 digits**, the same 24 as the Fibonacci digital-root wheel whose cycle sums to 117.
- **One period of 1/2701 has digit sum 99 = 9·11.**
- **Both facts are exact.** They are now in the arithmetic, not in π.

**Caveat (the same as for every repunit link):**
- **Every prime other than 2 and 5 divides some repunit.** That is what the period of 1/p means.
- **So "11, 37 and 73 all divide repunits" is true of every such prime.**
- **The specific fact is narrower:** 11 and 73 share R₈, and the periods 3 and 8 combine to 24. That is exact but not unique; many numbers have period 24.

**On the reduction steps (0.027027… → 09027 → 927 → 117 → 27):**
- **These use DCF reduction rules,** chosen operations rather than identities.
- **927 = 3²·103 and 9027 = 3²·17·59.** Neither factors through 37 or 11.

## 4. Does 027 correspond to the DNA helix?
**Measured DNA geometry (established structural biology):**

| form | base pairs per turn | twist per bp | rise per bp | pitch |
|---|---|---|---|---|
| B-DNA (normal) | ~10.5 | ~34.3° | 3.4 Å | ~34–36 Å |
| A-DNA (dehydrated, RNA–DNA) | **~11** | ~32.7° | 2.6 Å | ~28 Å |
| Z-DNA (left-handed) | 12 | −30° | 3.7 Å | ~45 Å |

- **No 027, 27 or 37 appears in these numbers.** So the 1/37 pattern does not correspond to the helix.
- **The repeating *period 3* of 1/37 matches the three-letter genetic code (codons).** But every number whose reciprocal has period 3 (27, 37, 111, 333, 999…) shares that, so it is not specific to 37.
- **11 does appear:** A-DNA, and the RNA double helix, which adopts the A form, have about **11 base pairs per turn**. That is the genuine "11" in nucleic-acid geometry, though the exact value varies with conditions (10.7–11.0).

## Summary
- **Every numerical claim in the message is correct** (mpmath/sympy). The 5…5 window around 401 is ordinary for π (19 such windows in 5,000 digits vs ~20 expected).
- **New exact facts:**
  - 27·37 = 999 (with 27 a cube);
  - 1/2701 has period 24, matching the Fibonacci 24-wheel;
  - its digit sum is 99 = 9·11;
  - 11 and 73 divide the same repunit.
- **027 does not match DNA's helix numbers.** The real 11 in nucleic acids is A-form DNA/RNA, at about 11 base pairs per turn.

## Potential leads for future research
- **[Period-24 reciprocals]** Pre-register: among n ≤ 10,000 with period-24 reciprocals, how often does the period's digit sum equal 99, and how many are triangular? That shows whether 2701 is special among its class.
- **[A-form and the 11 link]** If the K⁺ work ever touches RNA structure, the A-form 11 bp/turn is the measured anchor point. Use that, not a reduction.
- **[Data lead carried]** The T-cell activation time course (ENCSR731OFF file graph screenshot).

---
## Addendum: the period-24 check, run right away (descriptive, not pre-registered)
- **Numbers n ≤ 10,000 whose reciprocal repeats every 24 digits:** 18.
- **Of these, 8 have a period digit sum of 99,** so a sum of 99 is common in this class (44%).
- **Only one of the 18 is a triangular number: 2701.**

**What this shows:**
- **2701 is the only triangular number up to 10,000 whose reciprocal has period 24.** That is exact.
- **Not pre-registered:** the question was asked *because* of 2701, so it describes 2701 and does not test it.
- **What would make it a test:** a fixed, written-in-advance statement about a different triangular number or a larger range.

## Addendum 2: all triangular numbers with period 24 (complete, exact)
**Method:** every number whose reciprocal repeats with period exactly 24 is a divisor of 10²⁴ − 1. There are 1,756 such numbers among its 2,048 divisors, so the list below is complete, not a sample.

**Exactly three are triangular:**

| number | triangular index | factorization |
|---|---|---|
| **2701** | T₇₃ | 37 · 73 |
| **37401** | T₂₇₃ | 3 · 7 · 13 · 137 |
| **862641** | T₁₃₁₃ | 3² · 13 · **73** · 101 |

**Check:** the factorizations are recomputed and printed in `L3985_period24.txt`. 73 appears in both 2701 and 862641, and 137 appears in 37401. Both are factors of the repunit R₈. That is forced: a period of 24 needs at least one prime-power factor whose own period is 8 or 24. The primes with period 8 are 73 and 137.

**Other periods, for comparison (triangular numbers among all numbers with that period):**

| period | triangular numbers |
|---|---|
| 3 | none |
| 8 | none |
| 12 | none |
| 6 | 21, 91, 231, 351, 3003 |
| 16 | **153**, 561, 5151 |
| 24 | 2701, 37401, 862641 |
| 48 | four |

**What this shows:**
- **2701 is the smallest of exactly three triangular numbers whose reciprocal has period 24.** Exact.
- **153, the project's "gold guide" number, is the smallest triangular number with period 16.** Also exact.
- **These are descriptive facts about finite sets, not tests.**
