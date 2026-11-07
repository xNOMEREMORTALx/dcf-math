# Square star numbers, a Lehmer sequence, and the primes that divide it
### Draft v0.2 · Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 6 November 2026

**Status.** A companion note to the Λ note. Every statement is labelled:
- **[P]** proved;
- **[V]** verified by computation, with ranges stated;
- **[pre-reg]** predicted before the check (L3017–L3033, 12 of 12 passed).

**Origin.** Gary's 11 × 11 grid: 1–121 placed with point symmetry, mirrored pairs summing to 122, and 61 in the centre.

---

## 1. Star grids
**Definitions.**
- Star numbers: S_n = 6n(n − 1) + 1 (1, 13, 37, 73, 121, …).
- Centred hexagonal numbers: H_n = 3n(n − 1) + 1 (1, 7, 19, 37, 61, …).

**Identity [P].** S_n = 2H_n − 1.
- So a square grid of side m whose cell count m² is a star number S_n has centre (m² + 1)/2 = H_n.
- For m = 11: 121 = S₅, and the centre is 61 = H₅.

**Theorem 1 (square star numbers) [P].**
- m² = S_n ⇔ 3(2n − 1)² − 2m² = 1, a Pell-type equation.
- Its solutions are m = 1, 11, 109, 1079, 10681, …, with m_{k+1} = 10m_k − m_{k−1}.
- The star indices are n = 1, 5, 45, 441, …
- The grid centres are 1, 61, 5941, 582121, …, with c_{k+1} = 98c_k − c_{k−1} − 36 [V].

**Generating function [P].** Σ m_k x^k = (1 + x)/(1 − 10x + x²).
- At x = 1/100 this is **10100/9001** (9001 prime): the grid sides stacked in 2-digit steps.
- It is the analogue of 1/89 for Fibonacci.

## 2. The Lehmer structure
**Theorem 2 [P].** With α = √3 + √2 (so α⁻¹ = √3 − √2):

m_k = (α^(2k+1) − α^−(2k+1)) / (2√2).

These are the odd-index terms of the Lehmer sequence with (α + α⁻¹)² = 12 and α·α⁻¹ = 1.

**Corollary 3 (strong divisibility) [P; V].**
- **gcd(m_j, m_k) = m_g, where 2g + 1 = gcd(2j + 1, 2k + 1).** Checked on 1,600 pairs.
- **m_j divides m_k exactly when (2j + 1) divides (2k + 1).** Checked on 3,081 pairs.
- **Example.** m₇ = 10,360,559 = 11 × 109 × 8641, because 15 = 3 × 5.

## 3. Which primes divide a star-grid side
**Criterion [P].** Put ω = α² = 5 + 2√6. A prime p ≥ 5 divides some m_k ⇔ ω has odd order mod p (verified against brute force for p < 3000).

**Theorem 4 (mod-24 classification) [P; V for p < 10⁵].** The p-th power map sends √2 → (2/p)√2 and √3 → (3/p)√3. Hence:

| p mod 24 | (2/p), (3/p) | result | measured |
|---|---|---|---|
| 13 | −, + | **always** (α^(p+1) = 1 and (p + 1)/2 is odd) | 1,193 / 1,193 |
| 23 | +, + | **always** (α^(p−1) = 1 and (p − 1)/2 is odd) | 1,194 / 1,194 |
| 5, 19 | −, − | **never** (α^(p−1) = −1) | 0 / 2,411 |
| 7, 17 | +, − | **never** (α^(p+1) = −1) | 0 / 2,408 |
| 11 | −, + | ⇔ α^((p+1)/2) = 1 (α a square); half | 612 / 1,203; criterion exact for all |
| 1 | +, + | ⇔ α^(odd part of p − 1) = ±1; probability 1/2^(s−1), s = v₂(p − 1) | s = 3, 4, 5: 0.247, 0.114, 0.054 |

**Corollary 5 [heuristic + V].** The density of primes dividing some star-grid side is (2 + 1/2 + 1/6)/8 = **1/3**. Measured: 3,192 / 9,590 = 0.3328 for p < 10⁵.

## 4. Star primes and their hexagonal partners
**Proposition 6 [P].** A prime star number p = S_n with p ≡ 13 (mod 24) always divides a grid side (Theorem 4). Its first index 2k + 1 divides (p + 1)/2 = **H_n**, its own hexagonal partner.

**Observation 7 [V, pre-registered at 80%].** The first index equals H_n exactly for **77 of 80** such primes below 10⁶:

| star prime S_n | first index | hexagonal partner H_n |
|---|---|---|
| 13 = S₂ | 7 | 7 = H₂ |
| 37 = S₃ | 19 | 19 = H₃ |
| 181 = S₆ | 91 | 91 = H₆ |
| 541 = S₁₀ | 271 | 271 = H₁₀ |
| 661 = S₁₁ | 331 | 331 = H₁₁ |
| 1093 = S₁₄ | 547 | 547 = H₁₄ |

**The three exceptions** (71941, 156493, 574741) have index H_n/13, H_n/13 and H_n/61. Each happens when H_n has a small prime factor q and ω is a q-th power.

**Reading.** The 121/61 relation of the 11 × 11 grid (cells S₅, centre H₅) reappears in the primes: a star prime S_n almost always first divides a star-grid side at index H_n.

**Side fact [V].** 1093 = S₁₄ is the first Wieferich prime (2¹⁰⁹² ≡ 1 mod 1093²).

## 4b. Hexagonal grids have star-number sides (added in v0.2, L3033)
**Theorem 8 [P; V, pre-registered].** If a square grid's cell count m² is a centred hexagonal number H_n, then its side m is a star number S_j.
- **The sides** are 1, **13, 181, 2521, 35113, 489061, …**, with m_{k+1} = 14m_k − m_{k−1}.
- **As star numbers:** S₂, S₆, S₂₁, S₇₇, S₂₈₆, …
- **The cell counts** are H₈, H₁₀₅, H₁₄₅₆, …

*Proof.*
- m² = H_n ⇔ (2m)² − 3(2n − 1)² = 1, so 2m + (2n − 1)√3 is an odd power of 2 + √3 (since 2m is even).
- Write 2 + √3 = (1 + √3)²/2. Then (2 + √3)^(2r+1) = (c + d√3)²/2 with c² − 3d² = −2.
- So 2m = (c² + 3d²)/2 = 3d² − 1, i.e. 2m + 1 = 3d² with d odd.
- But a star number satisfies 2S_j + 1 = 3(2j − 1)². Hence m = S_j with j = (d + 1)/2. ∎

**Contrast [V, pre-registered].** Square triangular numbers (sides 1, 6, 35, 204, 1189, …, with m_{k+1} = 6m_k − m_{k−1}) contain **no** star number among their first 12 sides.

**Reading.**
- **Star and hexagonal numbers interlock both ways.** A star-number grid has a hexagonal centre (121 → 61). A hexagonal-number grid has a star-number side (169 → 13).
- **The 13 × 13 grid is the smallest example:** 169 cells = H₈, side 13 = S₂.

## 5. Framework numbers, with base rates
| number | class | where it divides |
|---|---|---|
| 11 | p ≡ 11; α is a square | every 3rd side |
| 13, 37, 61, 109 | p ≡ 13 (always) | every 7th, 19th, 31st, 5th side |
| 937 | p ≡ 1, s = 3 (1-in-4 chance) | every 13th side |

**Base rate.** About a third of primes divide some side. The framework numbers were chosen before this analysis but not blind to it, so their membership is description, not evidence.

## 6. Literature (to check)
- Pell equations for "square star numbers" may be catalogued in OEIS: the sides 1, 11, 109, 1079 and the squares 1, 121, 11881.
- The classification of prime divisors of Lehmer sequences by Legendre symbols is classical (Lehmer 1930; Lagarias 1985 for densities). The **specific** mod-24 table and the H_n-index observation should be checked against these before any claim of novelty.

## Summary
- **The grids.** The square grids whose cell count is a star number (sides 1, 11, 109, 1079, …) follow from a Pell equation and form a classical Lehmer sequence built from √3 + √2.
- **Divisibility.** Which grid sides divide which is fixed by a simple index rule.
- **Which primes divide them.** That is fixed by the remainder mod 24: always for 13 and 23, never for 5, 7, 17 and 19, and sometimes, by an exact rule, for 1 and 11. Overall it is one third of all primes.
- **The 121/61 pattern.** A star-number prime almost always first divides a grid side at the index given by its hexagonal partner, the same relation as 121 and 61 in the 11 × 11 grid.

## Potential leads for future research
- **[L2936k] OEIS / literature check.** Search for 1, 11, 109, 1079 and for "square star numbers", then for the Lehmer divisor classification with (α + α⁻¹)² = 12.
- **[L2936l] Other figurate grids.** Which square grids have a centred hexagonal or triangular cell count? Same method: Pell equation, Lehmer sequence, mod-N classification.
- **[L2936m] Exceptions in Observation 7.** Predict the frequency of index H_n/q from 1/q heuristics, then pre-register and test up to 10⁸.
