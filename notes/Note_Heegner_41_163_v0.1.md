# Note K: Euler's 41, Heegner's 163 and the near-cube e^(π√163) — the verified core of the 41 path
### Draft v0.1 · Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 9 November 2026

**Status.** Every number below is computed by `notes/heegner_check_L3245.py` (sympy, mpmath at 50 digits) or `rounds/L3241_euler41.py`. The theorems are classical (Euler 1772; Rabinowitsch 1913; Heegner 1952, Baker 1966, Stark 1967).

**Labels:** [V] verified; [D] description only.

---

## 1. Euler's prime-generating polynomial [V]
- **n² + n + 41 is prime for n = 0, 1, …, 39: forty primes in a row.** At n = 40 it gives 41².
- Its first values are **41, 43, 47**, 53, 61, 71, 83, 97, 113, 131 … (41 and 47 are on Gary's path).

## 2. Why 41: Euler's lucky numbers and the Heegner numbers [V]
- **The full list.** The primes p for which n² + n + p is prime for every n = 0, …, p − 2 are exactly **2, 3, 5, 11, 17, 41** (checked to 10⁴; known to be complete).
- **Rabinowitsch's theorem:** p is lucky exactly when ℚ(√−(4p − 1)) has class number 1, i.e. unique factorisation.
- **Their values of 4p − 1 are 7, 11, 19, 43, 67, 163:** the odd Heegner numbers above 3. Heegner, Baker and Stark proved the list of class-number-1 fields is complete, with **163 the largest**.
- **So 41 is the last lucky number because 163 is the last Heegner number. 5 is in the same family (4·5 − 1 = 19).**

## 3. The near-integers and the cubes [V]
| p | d = 4p − 1 | e^(π√d) | distance to nearest integer | e^(π√d) − 744 vs a cube |
|---|---|---|---|---|
| 5 | 19 | 885479.7777 | 0.22 | 96³ − 0.22 |
| 11 | 43 | 884736743.99978 | 2.2 × 10⁻⁴ | 960³ − 0.00022 |
| 17 | 67 | 147197952743.9999987 | 1.3 × 10⁻⁶ | 5280³ − 0.0000013 |
| **41** | **163** | **262537412640768743.99999999999925** | **7.5 × 10⁻¹³** | **640320³ − 7.5 × 10⁻¹³** |

**Why.** For these d, the j-invariant j((1 + √−d)/2) is an integer and a perfect cube (j = −640320³ for d = 163). The expansion j = 1/q + 744 + 196884 q + …, with q = −e^(−π√d), makes e^(π√d) ≈ cube + 744. The error shrinks as d grows, which is why 163 gives the closest approach.

## 4. How this sits with the rest of Gary's 41 path (L3241)
| step | status |
|---|---|
| 41 ↔ 163 ↔ a cube | **[V] theorem** (this note) |
| 41 and 5 are siblings | **[V]** both lucky numbers (Heegner 163 and 19) |
| 41 → 5 | **[V]** 1/41 has period 5 (41 × 271 = 11111) |
| 401 → 79 | **[V]** 401 is the 79th prime |
| √5 → φ → π | **[V]** φ = 2 cos(π/5) |
| 79 → 47; 131.81 → 41; 41 ↔ E8; an energy path | [D] not supported |
| 41, 401, 153 as DNA or protein periodicities | **tested, null** (L3241 K1–K4, 35 genomes) |

## Summary
- **The solid core of the 41 idea is one classical theorem.** Euler's polynomial makes 40 primes because 4·41 − 1 = 163, the largest number giving unique factorisation in its imaginary quadratic field.
- **That same 163 makes e^(π√163) a whole cube plus 744,** missing by less than a trillionth (computed here).
- **5 belongs to the same short list** (2, 3, 5, 11, 17, 41), and its partner 19 gives the same pattern more weakly (96³).

## Potential leads for future research
- **[K-digits]** Fold the near-integer table into the DCF reciprocal and digit work: the decimal expansion of e^(π√163) has 12 nines after the point. Any claim about digit positions in it must use the mpmath rule.
- **[K-periods]** The reciprocal periods of the lucky numbers and Heegner numbers (1/41 → 5, 1/163 → 81, …) as a small table, checked for any pattern against a matched control set of primes before any claim.
