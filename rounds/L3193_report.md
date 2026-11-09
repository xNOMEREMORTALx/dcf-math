# DCF L3193: Fibonacci-period minima to 6765 (my composite prediction failed 0 of 3); the Fe–S anaerobe contrast is already published; seen-name list filled
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 8 November 2026

**Leads pursued:** [R5b], [Seen-fix b], [Lit-FeS], [N2b].

**Waiting:** `blind_16.zip` for L3189.

---

## 1. [R5b] Smallest q with period F₁₇ … F₂₀ [pre-registered]
- **Pre-registration:** `PREREGISTERED_L3193.txt`, SHA-256 `34076d0b37a6c721a68329a399cef499fc836388dcb17075749ace74af8dace4`, commit `ca156b4`, pushed before computing.
- **Method:** every prime below 10⁸ (and its powers), so the result is exact for any minimum below 10⁸. The three minima found were re-checked by brute force over every q up to the answer.

| Fₙ | factors | smallest q | q is | prediction | verdict |
|---|---|---|---|---|---|
| 1597 | prime | **none below 10⁸** | — | M1: prime (forced) | **not graded** (as pre-registered) |
| 2584 | 2³·17·19 | **25841** = 10·2584 + 1 | prime | M2: composite | **FAIL** |
| 4181 | 37·113 | **8363** = 2·4181 + 1 | prime | M3: composite | **FAIL** |
| 6765 | 3·5·11·41 | **40591** = 6·6765 + 1 | prime | M4: composite | **FAIL** |

**Why my guess was wrong.**
- A composite q needs cheap primes whose periods are factors of Fₙ, and together they must cover **every** prime factor of Fₙ.
- **2584:** the best composite is 103 (period 34) × 457 (period 152) = 47,071. That loses to the prime 25,841.
- **4181:** a factor of period 37 first appears at 2,028,119, so the cheapest real cover is 227 × 2,028,119 ≈ 4.6 × 10⁸.
- **6765:** the cheapest composite cover is 31 (period 15) × 2707 (period 1353) = 83,917, about twice the prime 40,591.
- So composite minima need **both** a missing cheap full-period prime **and** cheap partial primes for every factor. 144, 610 and 987 had both; 2584, 4181 and 6765 did not.

**A side observation [D].** 1231 has period 41, and 1321 has period 55 (the F₁₀ minimum again).

**Full table so far (exact, F₇ to F₂₀):**

| Fₙ | 13 | 21 | 34 | 55 | 89 | 144 | 233 | 377 | 610 | 987 | 1597 | 2584 | 4181 | 6765 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| q | 53 | 43 | 103 | 1321 | 497867 | **323** | 467 | 11311 | **20141** | **12169** | > 10⁸ | 25841 | 8363 | 40591 |

(Bold marks composite minima.)

## 2. [Lit-FeS] The core Fe–S contrast is published
- **Andreini, Rosato & Banci (PLoS ONE 2017)** predicted Fe–S proteins in 434 prokaryotic genomes:
  - aerobes 1.8 ± 0.6% of genes;
  - high-content anaerobes 4.7 ± 1.0%;
  - a separate group of **low-content aerotolerant anaerobes** (2.2 ± 0.4%, 36 genomes).
- **They attribute the excess to energy production and conversion.** That is the same reading DCF reached in L3173, independently and later.
- **So the anaerobe/aerobe contrast, and the low-Fe–S anaerobes, are known.**
- **What remains possibly new:**
  - the label-free route (raw DNA → phone gene finder → CxxC);
  - the blind tests;
  - the hydrogen framing (aerobic H2 oxidisers read like anaerobes). The paper does not discuss hydrogenases.
- **Note H is updated to v0.2** with this, and a caveat found while re-reading L3165: H2-evolving clostridial fermenters (*C. kluyveri* 0.72, *L. phytofermentans* 0.64) read **above** the cut. "Fermenters read low" holds for the lactic fermenters of L3185, not for fermenters in general [D].

## 3. [N2b] Lehmer-sequence literature (partial)
- The first search found only adjacent work: Williams & Guy (INTEGERS 2012) on fourth-order divisibility sequences. It gives Legendre-symbol conditions but no densities.
- **No source yet for the mod-24 table or the density 1/3.**
- Densities of primes dividing Lucas/Lehmer sequences are a known research area (Lagarias, Moree and others). A zbMATH search by Gary is still the right check.

## 4. [Seen-fix b] Seen-name list completed
- `seen_names.txt` now has **123 names**. Blind_9–12 and the 11 L3117 methanogens were filled in from their pre-registrations and reports.
- **The L3117 list includes *M. hungatei*:** the *Methanospirillum* rejected in L3177 had indeed been used.
- **The "fermenter" note (§2)** came from re-reading these reports.
- **Remaining gap:** rounds before L2953 (covered by accession only).

## Record
**This round:** 3 graded, 0 passed (M2–M4); M1 not graded.

**Total: 261 of 341 pre-registered predictions passed, plus 3 split.**

## Summary
- **My prediction failed, and that is kept.** I expected the Fibonacci-period minima for 2584, 4181 and 6765 to be composite; all three are primes just above a multiple of the period. Composite minima need an unusual combination, which 144, 610 and 987 happen to have.
- **The iron–sulfur finding is partly known.** A 2017 study of 434 genomes already showed anaerobes carry more than twice the Fe–S proteins of aerobes, mostly for energy, and that some anaerobes are low. What DCF adds is the label-free phone route, the blind testing, and the hydrogen angle.
- **The fermenter claim needs narrowing:** hydrogen-making clostridial fermenters read high; lactic fermenters read low.
- **The list of genomes already used is now complete** from L2953 on.

## Potential leads for future research
- **[Fe-rTCA]** Grade blind_16 when it arrives.
- **[Fe-ferment H2]** Pre-register H2-evolving vs non-H2 fermenters (both anaerobic), to test the hydrogen reading inside fermenters.
- **[Lit-FeS b]** Compare CxxC density with Andreini 2017's Fe–S percentages for shared organisms.
- **[R5c]** Rule for composite minima: q is composite exactly when the cheapest "covering" product of partial-period primes beats the smallest prime ≡ 1 (mod Fₙ) of full order. Test it on F₂₁ to F₂₅ (bound 10⁹ or factor-based).
- **[N2b]** zbMATH: densities of prime divisors of Lehmer sequences (Lagarias-type results), to place the 1/3.
