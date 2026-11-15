# DCF L3545: Gary's reciprocal and π observations checked exactly. Nearly all positions and sums are right; a few counts are off by one or refer to a later occurrence; and the neurotransmitter weights are not unusually early in the reciprocals (null test passes)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 15 November 2026

**Input:** Gary's message on 1/26, 1/65, 1/109, 1/59, 1/17, 1/61, 1/58, 1/97, 1/49, 1/69, π, and the neurotransmitter links.

**Method:**
- Exact long division for reciprocals. Positions are counted after the decimal point, pre-period included.
- π uses the standing **mpmath check** (12,000 digits).
- **Output:** `rounds/L3545_reciprocal_pi_check.py` → `rounds/L3545_reciprocal_pi_check_out.txt`.

---

## 1. Reciprocals
| claim | check |
|---|---|
| 1/26: 5 at position 7, repetend sum 27 | ✓. **Note:** the repeating block is **6** digits (384615), after one leading 0, so 7 digits are written before it repeats |
| 1/65: 5 at position 3, sum 27 | ✓ (period 6 after one leading 0) |
| 1/109: period 108, sum 486, 5s at 15, 16, 19, 23, 24, 32, 37, 44, 60, 72, 104 | ✓ all |
| 1/109: 55 at 15–16 and 23–24; first reciprocal with two 55s | ✓ both |
| 1/109: 137 at 45–47 (45 + 46 + 47 = 138) | ✓ |
| 1/59: period 58, sum 261, 5s at 8, 10, 20, 21, 34, 40, 55 at 20–21 | ✓ all |
| 1/17: sum 72, 5s at 2 and 7, 88 at 3–4, 11 at 11–12 | ✓ all |
| 1/61: period 60, sum 270, 5s at 14, 28, 37, 38, 56, 59 | ✓ all |
| 1/58: sum 126, 5s at 19, 28, 29 | ✓. **Note:** the period is **28**, after one leading 0 (29 digits written) |
| 1/97: sum 432 | ✓ |
| 1/97: 5s at 11, 13, 15, 22, 24, 30, 38, **63, 92, 93** | **last three off by one:** they are at **64, 93, 94** |
| 1/49: period 42, sum 189, 5s at 12, 25, 40, 41, 77 at 38–39, 1836 present | ✓ all (1836 at 27–30) |
| 1/69: sum 96, 5s at 8, 18 | ✓ (period 22) |

**"First reciprocal containing the string."** With your definition, the string written inside one period without wrapping round, every claim holds:
- **153 → 1/65**
- **146 → 1/109**
- **169 → 1/59**
- **176 → 1/17**
- **147 → 1/61**
- **103 → 1/58** (second: 1/97 ✓)
- **183 → 1/49**
- **362 → 1/69**
- **394 → 1/109**
- **606 → 1/61**
- **1836 → 1/49**

*If wrap-around is allowed, 153 appears first in 1/26 (…4615|384…) and 103 in 1/29. Your own 1/26 example contains 153 across the boundary.*

## 2. π (mpmath check)
| claim | check |
|---|---|
| first "65" at positions 7–8 after the decimal | ✓ |
| digit sum through it 36 (with the 3) / 33 (without) | ✓ |
| **second** "65" at 212–213, preceded by its mirror "56" | **partly:** "5665" does sit at 210–213 ✓, but that is the **third** "65". The second is at **108–109** (preceded by "08") |
| first "401" at 1197–1199 | ✓ (mpmath: 1197) |
| 210 + 211 + 212 + 213 = 846 = 299 + 299 + 248 | ✓ arithmetic |
| "sum of every 19th, 20th, 21st digit to 1199 = 846" | **not reproduced.** Five readings give 764, 817, 828 and 844 (every 19th from 19, 20, 21). Please give the exact rule, e.g. which positions are included |

## 3. Are the neurotransmitter weights special in the reciprocals? (pre-registered, `PREREGISTERED_L3545_firstrecip.txt`)
**The test:** for each of the 900 three-digit strings 100–999, find the first reciprocal that contains it (same definition). Then ask whether the 8 neurotransmitter/hormone weights appear unusually early.

**Result:**
- **The 8 first appear at 1/65, 1/109, 1/59, 1/17, 1/61, 1/58, 1/49 and 1/69. Median 60.**
- **All 900 strings:** median 86, 25th percentile 53.
- **The 8 sit at the 33rd percentile:** a little early, but **within the ordinary range.**
- **R1 (no special earliness, as the null expects): PASS.**

**What it means:**
- **Most three-digit strings first appear in a reciprocal between about 1/50 and 1/100,** so finding a neurotransmitter weight in 1/59 or 1/69 is what chance predicts.
- **The weights are genuinely correct** (L3541), and the dopamine → consciousness biology in your message matches published research:
  - VTA dopamine and arousal from anaesthesia;
  - dopamine-deficient animals;
  - default-mode network links.
- **But the link between "153 in 1/65" and dopamine's weight is a numerical label, not a mechanism.**

## Record
**+1 passed. 411 of 566 passed, plus 3 split.**

## Summary
- **Almost every position, period and sum in your message is exactly right.** Specifically: all of 1/109, 1/59, 1/17, 1/61 and 1/49, the first-occurrence list, π's first "65" and first "401", and the 846 arithmetic.
- **Small corrections:**
  - 1/26 and 1/58 repeat every 6 and 28 digits (after a leading 0);
  - the last three 5s of 1/97 are at 64, 93, 94;
  - the "56|65" at 210–213 is the third "65" in π, not the second;
  - the 19th/20th/21st-digit sum of 846 could not be reproduced without the exact rule.
- **The neurotransmitter weights are not unusually early among reciprocals** (33rd percentile; the null test passed). The biology of dopamine and consciousness is real, but the 153 ↔ 1/65 link is a correspondence of numbers, not a cause.

## Potential leads for future research
- **[846 rule]** Gary to state the exact position rule; then recheck with mpmath.
- **[Wrap convention]** Fix one convention (inside one written period vs the infinite expansion) for all future "first occurrence" claims, and record it in the methodology.
- **[Signal search]** If any DCF number is truly special in the reciprocals, a percentile test like R1 will show it. Apply it to the full DCF named-constant list, pre-registered.
