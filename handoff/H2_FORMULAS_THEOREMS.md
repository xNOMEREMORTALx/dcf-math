# DCF Handoff 2 of 6: formulas and theorems (proved, verified, and description-only)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 8 November 2026

**Labels:**
- **[P]** proved;
- **[V]** verified by computation or a cited source;
- **[B]** passed a blind or pre-registered test;
- **[D]** description only;
- **[✗]** failed.

**Full texts.** dcf-math `notes/Note_Lambda_digit_agreement_draft_v0.5.md` and `notes/Note_star_grids_Lehmer_draft_v0.2.md`.

---

## 1. The digit-agreement law Λ
**Theorem 1 [P].** For τ uniform and gcd(r, s) = 1:

P(⌊b{sτ}⌋ = ⌊b{rτ}⌋) = 1/b + j(d − j)/(brs), where d = gcd(r − s, b) and j = r mod d.

**Corollary 2, Theorem Λ [P].** For an integer multiplier c in base b:

**λ_b(c) = (c − 1 + gcd(c − 1, b)) / (bc)**

For a normal number x, the digits of x and cx agree with this frequency.

**Theorem 4 [P].** λ_b(r/s) ≤ 2/(b + 1), with equality only for {r, s} = {1, b + 1}.

**Theorem 5, complement [P].** P(digit x + digit (r/s)x = b − 1) = 1/b − j′(d′ − j′)/(brs), where d′ = gcd(r + s, b).

**Other results:**
- **[P]** k-digit blocks are base b^k (Corollary 7).
- **[P]** affine maps (Proposition 8).
- **[P]** powers of algebraic numbers (Corollary 9) and roots, where x = m^{1/k} and x^{kq+1} share λ(m^q) (Proposition 10).
- **[B]** `power_share` is in the phone bundle.

**Families c·λ(c) in base 10 [P]:**

| c·λ(c) | members |
|---|---|
| 3 | **{21, 26 (Fe), 29 (Cu), 30 (Zn)}** |
| 2 | {11, 16 (¹⁶O), 19 (K), 20 (Ca)} |
| 9/5 | {17, 18 (H₂O)} |
| 1 | {1 (H)}, alone |

## 2. Star grids (Gary's 11 × 11 grid: pairs sum to 122, centre 61)
**Definitions.** S_n = 6n(n − 1) + 1 (star numbers) and H_n = 3n(n − 1) + 1 (centred hexagonal numbers).

**Identity [P].** S_n = 2H_n − 1, so a square grid with m² = S_n has centre H_n (121 = S₅, centre 61 = H₅).

**Theorem 1 [P].**
- m² = S_n ⇔ 3(2n − 1)² − 2m² = 1.
- The sides are m = 1, 11, 109, 1079, 10681, …, with m_{k+1} = 10m_k − m_{k−1}.
- The generating function is (1 + x)/(1 − 10x + x²); at x = 1/100 it gives **10100/9001**.

**Theorem 2, the Lehmer form [P].** m_k = (α^(2k+1) − α^−(2k+1))/(2√2), with α = √3 + √2.

**Corollary 3 [P].** gcd(m_j, m_k) = m_g, where 2g + 1 = gcd(2j + 1, 2k + 1). Hence m_j | m_k ⇔ (2j + 1) | (2k + 1).

**Theorem 4: which primes divide some grid side, by p mod 24 [P; V p < 10⁵]:**

| p mod 24 | divides some side? |
|---|---|
| 13, 23 | always |
| 5, 7, 17, 19 | never |
| 11 | ⇔ α is a square |
| 1 | with probability 1/2^(s−1), s = v₂(p − 1) |

**Overall density = 1/3** (measured 0.3328).

**Observation 7 [B at 80%].** A star prime S_n ≡ 13 (mod 24) first divides a grid side at index **H_n** in 77 of 80 cases below 10⁶. The exceptions are at H_n/13 and H_n/61. **Side fact:** 1093 = S₁₄ is the first Wieferich prime.

**Hexagonal-number grids** have star-number sides: 13, 181, 2521, …

## 3. Reciprocal periods
- **Period of 1/q** = the order of 10 mod q (gcd(q, 10) = 1). **1/(pq) has period lcm** of the two.
- **1/323 = 1/(17 × 19): period lcm(16, 18) = 144 = 12² = F₁₂** [P]. 144 is the only square Fibonacci number > 1 (Cohn 1964).
- **4365 first appears at position 88 of 1/323** [V, mpmath]; 765 at position 5 of 1/47; 135 repeats in 1/74 (= half of 1/37). **The chain 4365 → 765 → 135 → 45 → 9 is [D].**
- **Smallest q with period F_n** [B, L3133 4/4]:

| F_n | 13 | 21 | 34 | 55 | 89 | 144 | 233 | 377 |
|---|---|---|---|---|---|---|---|---|
| q | 53 | 43 | 103 | 1321 | 497867 | 323 | 467 | 11311 |

**Rule:** a prime period n forces p ≡ 1 (mod 2n).

## 4. Physical and chemical numbers checked [V]; links [D]
| quantity | value | DCF link (description only) |
|---|---|---|
| Lyman-α | 121.567 nm | 121 = S₅ (unit-dependent) |
| H 21-cm line | 1420.405751768 MHz; 21.106114054 cm | "21" |
| ²H NMR at 9.3947 T (¹H = 400 MHz) | 61.40 MHz (ratio 0.15350) | 61 = H₅ (instrument-dependent) |
| ¹⁷O NMR at 9.3947 T | 54.23 MHz; spin 5/2; 0.037% | — |
| DNA hydrogen bonds | A–T 2, G–C 3; **2 + GC per bp** | aerobes 2.64 vs anaerobes 2.48 in our 25 genomes [D]; literature: mostly ancestry, except obligate aerobes (Aslam 2019) |
| B-DNA | ~10.5 bp per turn; 21 bp ≈ 2 turns | — |
| Genetic code | 64 codons → 20 aa + stop = 21 meanings; +Sec (TGA), +Pyl (TAG) = 23 | — |
| Masses | p53 computed 43.65 kDa (not 53); SOD1 subunit 15.94 kDa (dimer 32) | — |
| Mo/W, Fe | Fe 26, Cu 29, Zn 30, Se 34 | — |

## 5. Biology formulas used by the tools
| quantity | formula | used by |
|---|---|---|
| Fe–S density | (number of C-x-x-C motifs per 1,000 amino acids of predicted proteins); **cut 0.50** (frozen L3141) | `dcf_metals.py` |
| R | observed CxxC ÷ expected from the cysteine frequency, Σ(len − 3)·f_C² | `dcf_metals.py` |
| C2H2 zinc finger | `C.{2,4}C.{12}H.{3,5}H` | `dcf_metals.py` |
| E17 promoter self-check | share of 17-nt spacers ÷ shuffled control; > 1.5 = clear | `dcf_promoters.py` |

## Summary
- **Proved:** the digit-agreement law Λ (closed form, maximum, complement, blocks, algebraic powers), the star-grid Pell/Lehmer structure with the mod-24 prime rule, and the reciprocal-period facts (1/323 → 144).
- **Measured blind:** Fibonacci-period minima, and the star-prime index observation.
- **Checked numbers:** all physical constants here are verified against sources. Their links to 121, 61 and 21 remain description.

## Potential leads for future research
- **[N2]** OEIS / zbMATH check of the star-grid sides 1, 11, 109, 1079 and of the mod-24 table before any novelty claim.
- **[R2]** Twin-prime products p(p + 2): when is the period a square or a Fibonacci number?
- **[R5]** When is the smallest q with period F_n composite (as at 144)?
- **[O-Λ]** Λ families of all stable isotope mass numbers 1–40 vs a shuffled control.
- **[L2936l/m]** Other figurate grids; the H_n/q exception frequency to 10⁸.
