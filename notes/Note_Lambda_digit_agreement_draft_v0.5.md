# How often do x and (r/s)x share digits? A closed form, the maximum 2/(b+1), and applications
### Draft v0.5 · Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 6 November 2026

**Changes from v0.1.**
- A closed form for every rational multiplier, proved by Fourier analysis.
- The maximum 2/(b + 1) is now **proved for all rational multipliers** (it was verified only).
- A complement version.
- The φⁿ applications.

**Status.**
- Every formula is checked against exact counting: 8,325 cases, bases 2–16, r, s ≤ 30, 0 mismatches (L2937).
- Every numerical claim comes from pre-registered rounds L2879–L2937.
- A specialist literature search is still pending before submission.

---

## Abstract
Let b ≥ 2 and let r, s be coprime positive integers. For x normal in base b, and for the repetend of a/p as a runs over a full coset, the proportion of positions at which the digits of x and (r/s)·x coincide is

**λ_b(r/s) = 1/b + j(d − j)/(brs),  d = gcd(r − s, b),  j = r mod d.**

**Consequences.**
- **Maximum.** The proportion never exceeds **2/(b + 1)**, and it equals 2/(b + 1) only for r/s = b + 1 or 1/(b + 1): ×11 in decimal, ×5 in base 4.
- **Complement version.** The proportion of positions where the digit of x and the digit of (r/s)x sum to b − 1 is 1/b − j′(d′ − j′)/(brs), with d′ = gcd(r + s, b) and j′ = r mod d′.
- **Coding theory.** The base-b periods of a/p (a cyclic AN code) have relative minimum distance → (b − 1)/(b + 1).
- **The golden ratio.** φ and φⁿ share digits at rate λ(Fₙ), and φ and φ⁻ⁿ at rate λ(Fₙ) or the complement rate, by the parity of n.

## 1. The closed form
**Theorem 1.** Let τ be uniform on [0, 1) and gcd(r, s) = 1. Then

P(⌊b{sτ}⌋ = ⌊b{rτ}⌋) = 1/b + j(d − j)/(brs),

where d = gcd(r − s, b) and j = r mod d (when j = 0 the value is 1/b).

*Proof.*
1. **Fourier expansion.** Write 1_{I_k} for the indicator of [k/b, (k+1)/b). By Parseval on the line t ↦ (sτ, rτ), only frequency pairs (rt, −st) contribute:

   P = Σ_k Σ_t 1̂_{I_k}(rt)·conj(1̂_{I_k}(st)).

2. **Summing over digits.** Summing over k forces rt ≡ st (mod b), i.e. (b/d) | t, and gives

   P = 1/b + (2b/(π²rs)) Σ_{t ≥ 1, b | (r − s)t} sin²(πrt/b)/t².

3. **Evaluating the series.** Put t = (b/d)u and use Σ_{u ≥ 1} sin²(πxu)/u² = (π²/2)·{x}(1 − {x}) with x = r/d, so {x} = j/d. ∎

**Corollary 2 (integer multipliers, Theorem Λ).** For s = 1 and c = r: d = gcd(c − 1, b) and j = 1, so λ = (c − 1 + d)/(bc).

**Corollary 3 (normal numbers).** If x is normal in base b, then {bⁿx} is uniformly distributed. For integer c the digits of x and cx coincide with frequency λ_b(c).

**Theorem 4 (the maximum, all rationals).** For every reduced r/s ≠ 1, λ_b(r/s) ≤ 2/(b + 1), with equality only for {r, s} = {1, b + 1}.

*Proof.*
1. **Reduction.** By symmetry (r ≡ s mod d, so j is the same for r and s), take r < s.
2. **Trivial case.** If d = 1 then λ = 1/b. So take d ≥ 2.
3. **Size bounds.** Since j ≡ r (mod d) with 1 ≤ j ≤ d − 1, we have r ≥ j. Since d | s − r and s > r, we have s ≥ r + d ≥ j + d. Hence rs ≥ j(j + d).
4. **The inequality.** The claim λ − 1/b ≤ (b − 1)/(b(b + 1)) is j(d − j)(b + 1) ≤ (b − 1)·rs. It suffices that (d − j)(b + 1) ≤ (b − 1)(j + d), i.e. d ≤ bj. That holds because d ≤ b and j ≥ 1.
5. **Equality.** Equality needs d = b, j = 1, r = j and s = j + d, i.e. r = 1, s = b + 1. ∎

**Theorem 5 (complement).** By the same computation with digit k paired against b − 1 − k:

P(digit of x + digit of (r/s)x = b − 1) = 1/b − j′(d′ − j′)/(brs), d′ = gcd(r + s, b), j′ = r mod d′.

For example λ⁻(1) = 0 in even bases (a digit never equals its own complement), and λ⁻₁₀(3) = 1/15.

## 1b. Blocks and shifts (added in v0.3, L2941)
**Corollary 7 (k-digit blocks).** Agreement on k consecutive digits is single-digit agreement in base b^k. So

P_k(c) = (c − 1 + gcd(c − 1, b^k))/(b^k c),

and the best multiplier for k-blocks is b^k + 1, with 2/(b^k + 1).

**On π (10⁶ decimals):**

| c | 2-digit agreement | prediction |
|---|---|---|
| 101 | 0.01983 | 2/101 = 0.01980 |
| 11 | 0.01814 | 1/55 = 0.01818 |
| 6 | 0.01665 | 1/60 = 0.01667 |
| 2 | 0.00996 | 1/100 |

So ×101 beats ×11 on 2-digit blocks, while ×11 beats ×101 on single digits.

**Proposition 8 (affine maps).** For y = (r/s)x + t, the shift seen at digit n is t_n = {b^{n−1}t}. The share is the average, over the orbit of t_n, of

1/b + (d²/(brs))·[B₂({β}) − B₂({β + θ})/2 − B₂({β − θ})/2],

where β = bs·t_n/d, θ = j/d and B₂(x) = x² − x + 1/6.
- **Terminating shifts leave no trace.** A shift whose decimal expansion ends (1/2, 1/4, 0.03, 1/20) has t_n = 0 after a few digits, so it changes nothing in the long run.
- **Periodic shifts persist.** A shift such as 1/3 keeps acting: π vs 11π + 1/3 shares **1/11** (measured 0.0904), half of the unshifted 2/11.

## 1c. Algebraic numbers and their powers (added in v0.4, L2949–L2989)
**Corollary 9 (powers of an algebraic number).** Let x be a root of xᵈ = a₀ + a₁x + … + a_{d−1}x^{d−1} with integer aᵢ, and write each power in the basis 1, x, …, x^{d−1}. If xⁿ = k·xᵐ + N with rational k = r/s and integer N, then xᵐ and xⁿ share λ_b(r/s) of their base-b digits (the complement law when k < 0; share 1 when k = 1).
- *Proof.* An integer N leaves the fractional part unchanged, and k < 0 turns digits into their complements; apply Corollary 3 to the normal number xᵐ (normality assumed).

**Conjecture 9′ (independence).** If no such relation exists, the share is 1/b. This assumes that the digits of 1, x, …, x^{d−1} are jointly normal, as for x vs x² (L2949). It is consistent with every measurement:
- π vs π², π³; e vs e²; ln 2 vs (ln 2)²;
- the plastic number ρ vs ρⁿ for 10 values of n, including the rival "ρ-coefficient" rule rejected at ρ⁸ (0.1007 vs 0.1333);
- every unrelated power of the roots below.

**Proposition 10 (roots).** For x = m^{1/k} (m not a k-th power), x^{kq+1} = m^q·x, so x and x^{kq+1} share λ(m^q) = (m^q − 1 + gcd(m^q − 1, 10))/(10m^q) in base 10, and all other powers share 1/10.
- **For odd m,** every such power shares extra digits.
- **For m = 2,** only q ≡ 0 (mod 4): 16x, 256x, …

**Examples (first 10⁶ decimals; all pre-registered):**

| pair | relation | predicted | measured |
|---|---|---|---|
| φ vs φ⁸ | 21φ + 13 | 1/7 | 0.14276 |
| δ = 1 + √2 vs δ³ | 5δ + 2 | 3/25 | 0.11998 |
| √5 vs φ³ | φ³ = √5 + 2 | 1 | 1.00000 |
| √5 vs φ⁹ | 17√5 + 38 | 9/85 | 0.10556 |
| φ vs √5 | √5 = 2φ − 1 | 1/10 | 0.09994 |
| ∛2 vs x¹³ | 16x | 1/8 | 0.12425 |
| ∛3 vs x⁴ | 3x | 2/15 | 0.13313 |
| √5 vs x³ | 5x | 3/25 | 0.11962 |
| √2 vs x⁹ | 16x | 1/8 | 0.12545 |
| ρ (plastic) vs ρ⁸ | needs ρ² | 1/10 | 0.10067 |

**Other bases (L2993, pre-registered, first 10⁶ base-b digits).** In base b the excess appears when c − 1 shares a factor with b, and ×(b + 1) attains the maximum 2/(b + 1) (Theorem 4).

| base | pair | relation | predicted | measured |
|---|---|---|---|---|
| 3 | √2 vs x⁵ | 4x (= b + 1) | 1/2 | 0.49994 |
| 3 | ∛2 vs x⁷ | 4x (= b + 1) | 1/2 | 0.49996 |
| 3 | ∛2 vs x¹³ | 16x | 3/8 | 0.37466 |
| 5 | ∛2 vs x¹³ | 16x | 1/4 | 0.24987 |
| 5 | √3 vs x⁹ | 81x | 17/81 | 0.20946 |
| 3 / 5 | 10 control pairs | no relation | 1/3 / 1/5 | within 0.0009 |

The same pair can be special in one base and ordinary in another: ∛2 vs 4∛2 shares 1/2 in base 3 but 1/10 in base 10.

**Remark (quadratic vs higher degree).** For a quadratic unit (φ, δ), every power is k·x + N, so every power carries a predictable share (λ(Fₙ) for φ, λ(Pₙ) for δ). For degree ≥ 3, most powers need x² as well and fall back to 1/10. That is why φ looks special: its equation is quadratic.

## 2. Values
| base | rank 1 | rank 2 | rank 3 |
|---|---|---|---|
| 10 | ×11, ×1/11: **2/11** | ×6: 1/6 | ×13/3, ×3/13: 2/13 |
| 4 | ×5: 2/5 | ×3, ×9: 1/3 | — |

Multipliers ending in 1 (c ≡ 1 mod 10) give (c + 9)/(10c): ×31 gives 4/31, ×41 gives 5/41, ×131 gives 14/131.

## 3. Evidence (pre-registered rounds)
- **Repetends, base 10.** 198 full-reptend primes:
  - 23,000+ integer and rational cases within tolerance;
  - the closest multiplier is ×11 in 115/115 primes;
  - the minimum distance is 9/11 in 56/56.
- **Repetends, base 4.** The closest pair is ×5 in 129/130 primes; d_min/T → 3/5; 6,342/6,342 rational cases match.
- **Constants (10⁶ decimals).**
  - π vs cπ for c = 2, 3, 6, 11, 21, 31, 41, 131, 671;
  - e, √2, ln 2 likewise;
  - φ vs φⁿ for n = 3–12, including **φ⁸ = 21φ + 13: 142,760 matches in 10⁶, against 142,857 predicted (1/7)**;
  - φ vs φ⁻ⁿ (complement law for even n, e.g. φ⁻⁴: 0.0671 vs 1/15);
  - base 5: φ⁸ shares 5/21;
  - algebraic numbers and roots: 66 further pre-registered pairs (§1c), all within 0.0015 (L2957–L2989);
  - bases 3 and 5: 17 pre-registered pairs, all within 0.002 (L2993).

## 4. Block uniformity
**Proposition 6.** For a sequence with exactly uniform k-blocks, |A − λ| ≤ N_bad/b^k, and A = λ exactly when c | b^{k−1}. Consequently, x-vs-cx tests see only short-block structure (L2901, L2921).

## 5. Applications
- **DNA address tags (L2866–L2883).** They carry free divisibility checks by Φ_q(4), but cannot beat random codes in distance (limit 3/5 vs 3/4).
- **Golden-angle spiral (L2925–L2933).**
  - φ = 2cos(π/5);
  - record approaches to the direction j/m on the Fibonacci ladder n = F_t/m;
  - every record has m·n a sum of at most 3 signed Fibonacci numbers.

## 6. Open problems
1. **The error term** for repetends at index k > 1 (character sums).
2. **Rational multipliers for normal x.** Show joint equidistribution of ({bⁿx}, ⌊bⁿx⌋ mod s).
3. **Literature.** Search for prior statements of Theorem 1 (normal-number correlations; AN-code Hamming distance).
4. **Joint normality** of 1, x, …, x^{d−1} (Conjecture 9′) is open, as is normality of any algebraic irrational itself.

## Summary
- **The closed form.** A short Fourier computation gives the exact rate at which a number and any rational multiple of it share digits: 1/b + j(d − j)/(brs).
- **The maximum, proved.** That proves the long-observed maximum: no multiple of any kind shares more digits than ×(base + 1), which shares 2/(b + 1) (×11 and 2/11 in decimal).
- **The evidence.** All tested data agree, from prime reciprocals to a million digits of π and φ.
- **Algebraic numbers.** Powers of φ, the silver ratio, the plastic number and roots such as ∛2, ∛3, √2 and √5 share digits exactly when they differ by a rational factor plus a whole number, at the predicted rate. Otherwise they share the chance rate.

## Potential leads for future research
- **[N2]** Specialist literature search, then submission.
- **[N4]** Two different numbers x, y with y = (r/s)x + t (affine maps): extend Theorem 1.
- **[N5]** Higher-order agreement: blocks of k equal digits in x and cx.
