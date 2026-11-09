# DCF L3189: all leads pursued — blind_16 pre-registered; 1/323 is the only twin-prime square period below 10⁶, explained by Pell; Fibonacci-period minima turn composite at 610 and 987; star-grid sides found in OEIS
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 8 November 2026

**Leads pursued:** [Fe-rTCA], [Fe-H2b], [Sec-O revised], [R2], [R5], [O-Λ], [N2], [R-floor], [Seen-fix], [Repo hygiene], [Fe-H2 note].

---

## 1. Blind_16 pre-registered [Fe-rTCA, Fe-H2b, Sec-O revised]
`PREREGISTERED_L3189.txt`, SHA-256 `264e1faf2fdbcf5a6783fd652f6dfa73a65561f36d69c7a54ec90106a2fb0816`, commit `2779a14`, pushed **before** any download.

| group | accession | organism |
|---|---|---|
| reductive TCA, anaerobe (green sulfur) | NC_002932 | *Chlorobaculum tepidum* TLS |
| reductive TCA, anaerobe (green sulfur) | NC_007514 | *Chlorobium chlorochromatii* CaD3 |
| Calvin + H2, aerobe | NC_009720 | *Xanthobacter autotrophicus* Py2 |
| Calvin, no H2, aerobe | NC_013422 | *Halothiobacillus neapolitanus* c2 |
| Calvin, no H2, aerobe | NC_007614 | *Nitrosospira multiformis* ATCC 25196 |
| megaplasmid | NC_005241 | *Cupriavidus necator* H16 pHG1 |

All six are absent from the seen list and from every report on Drive. Five were matched to a genome page by web search; pHG1's accession is unconfirmed until the LOCUS check.

| id | prediction |
|---|---|
| G1 | both green sulfur bacteria > 0.50 |
| G2 | both Calvin non-H2 aerobes < 0.50 |
| G3 | *Xanthobacter* > both Calvin non-H2 aerobes (H2 with carbon fixation held constant) |
| G4 | pHG1 > *Cupriavidus* chromosome 1 (0.40) |
| G5 | *Halothiobacillus* and *Nitrosospira* carry 0 annotated Sec |

**Action for Gary.** Zip these six as **`blind_16.zip`**:
1. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NC_002932&rettype=gbwithparts&retmode=text
2. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NC_007514&rettype=gbwithparts&retmode=text
3. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NC_009720&rettype=gbwithparts&retmode=text
4. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NC_013422&rettype=gbwithparts&retmode=text
5. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NC_007614&rettype=gbwithparts&retmode=text
6. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NC_005241&rettype=gbwithparts&retmode=text

## 2. [R2] Twin-prime products p(p + 2) [V, P]
**Computation [V].** Of the 8,167 twin-prime pairs with 7 ≤ p < 10⁶, the period of 1/(p(p + 2)) is a perfect square in exactly **one** case, and a Fibonacci number in exactly **one** case. Both are **17 × 19 = 323, period 144**.

**Why 323 [P].** Suppose both p and p + 2 have full period, i.e. ord = p − 1 and p + 1.
- Since gcd(p − 1, p + 1) = 2, the period of 1/(p(p + 2)) is (p² − 1)/2.
- This is a square k² exactly when **p² − 2k² = 1**: the Pell equation of the silver ratio 1 + √2.
- Its solutions are p = 3, 17, 99, 577, 3363, 19601, … (pₖ₊₁ = 6pₖ − pₖ₋₁).
- For p = 17: (289 − 1)/2 = 144 = 12².

**Search [V].** Among the first 18 Pell solutions (to 3 × 10¹³), **17 is the only one that is a twin prime with both members full-period.** (3 is a twin prime but 1/3 has period 1.)

**Reading.** The 144 in 1/323 is a Pell coincidence, not a general twin-prime pattern. It is the silver-ratio Pell equation x² − 2y² = 1, a cousin of the star-grid Pell equation 3x² − 2y² = 1 [D link].

## 3. [R5] When the smallest q with period Fₙ is composite [V]
Exact: every prime power below 2 × 10⁷ was scanned, and the three composite answers were re-checked by brute force.

| Fₙ | smallest q | factors (part periods) | prime? |
|---|---|---|---|
| 13 | 53 | — | prime |
| 21 | 43 | — | prime |
| 34 | 103 | — | prime |
| 55 | 1321 | — | prime |
| 89 | 497867 | — | prime |
| **144** | **323** | 17 (16) × 19 (18) | **composite**; smallest full-period prime 8929 |
| 233 | 467 | — | prime |
| 377 | 11311 | — | prime |
| **610** | **20141** | 11 (2) × 1831 (305) | **composite**; no full-period prime below 2 × 10⁷ |
| **987** | **12169** | **43 (21)** × 283 (141) | **composite**; no full-period prime below 2 × 10⁷ |

**Reading.**
- The H2 table (13 → 377) is reproduced exactly.
- **New:** the minimum turns composite at 610 and 987. It happens when no small prime has order exactly Fₙ, but primes with orders that are factors of Fₙ combine cheaply.
- **987 is built on 43, the Fibonacci-period prime for 21:** 987 = lcm(21, 141).
- **610 = 10 × 61.** Its minimum uses 1831, of period 305 = 5 × 61. The appearance of **61** (Gary's grid centre H₅) is [D] only.

## 4. [O-Λ] Isotope mass numbers vs Λ families — closed as ill-posed
- **Every mass number from 1 to 40 has a stable nuclide except 5 and 8** (standard nuclear data).
- So "stable mass numbers 1–40" is almost the whole range, and **no control can differ from it.**
- **Closed** without a test. A reformulation would need a real selection, e.g. the most abundant isotope of each element.

## 5. [N2] Literature check of the star-grid sequences [partial]
- **Square star numbers 1, 121, 11881, 1164241** (sides 1, 11, 109, 1079) are known: the Wikipedia *Star number* page cites OEIS A054318 and A006061.
- **Hexagonal-number grid sides 1, 13, 181, 2521, …** are OEIS **A001570** ("numbers k such that k² is centered hexagonal", aₙ = 14aₙ₋₁ − aₙ₋₂).
- **So the sequences themselves are not new.** The Lehmer form, the gcd law and the mod-24 prime table still need a zbMATH/MathSciNet check. Lehmer-sequence divisibility is classical (Lehmer 1930), so the mod-24 table may well follow from known results.

## 6. Housekeeping
- **[R-floor]:**
  - `dcf_metals.py` now warns when cysteine is below 0.4%; density and R values are unchanged.
  - The new SHA-256 is `1850ab53…8ea3`.
  - Blind_16 will be graded with the frozen L3141 version (`a640abc9…`).
- **[Seen-fix]:**
  - `seen_names.txt` (about 90 names) is now in dcf-genefinder.
  - *L. plantarum* NC_004567 was added to the accession list.
  - **Known gap:** names for blind_9–12 and the L3117 methanogens still need adding from those reports.
- **[Repo hygiene]:**
  - The dcf-math README already had the handoff index.
  - Its stale pre-registration count (78 files to L3121) is corrected to 86 files to L3189.
  - A `rounds/` entry was added.
- **Noticed:** the "reading" label inside `dcf_metals.py` uses 0.7, not the frozen 0.50 cut. All grading used 0.50, so no result changes. The label is left alone during blind testing.

## 7. [Fe-H2 note]
`notes/Note_FeS_hydrogen_signature_draft_v0.1.md`:
- the six pre-registered Fe–S rounds in order, failures included;
- the L3185 table;
- the open confounds (carbon fixation, plasmids, sample size, literature).

## Record
No new predictions were graded this round. **Still 261 of 338 passed, plus 3 split;** G1–G5 will take it to 343.

## Summary
- **Blind_16 is frozen.** It asks whether the iron–sulfur signal comes from hydrogen itself or from the carbon-fixation chemistry that often travels with it, and reads *Cupriavidus*'s hydrogenase plasmid.
- **1/323's period 144 is explained.** For twin primes with full periods, a square period requires the Pell equation p² − 2k² = 1, and 17 is the only solution that works up to 3 × 10¹³.
- **The Fibonacci-period minima are now known through 987.** They are composite at 144, 610 and 987.
- **The star-grid sides are already in OEIS,** so any novelty must come from the Lehmer and mod-24 results.
- **The isotope test was closed,** because nearly every mass number is stable.

## Potential leads for future research
- **[Fe-rTCA]** Grade G1–G5 when `blind_16.zip` arrives (round L3193).
- **[R2b]** Prove or bound: a square period of 1/(p(p+2)) when the orders are not full (none below 10⁶ besides 323).
- **[R5b]** Predict when the Fₙ minimum is composite. Candidate rule: no prime ≡ 1 (mod Fₙ) below some bound has order exactly Fₙ. Test it on F₁₆ = 987 → F₂₀ = 6765.
- **[N2b]** zbMATH/MathSciNet search: "Lehmer sequence" with "prime divisors" and "mod 24" (Gary can search too).
- **[Seen-fix b]** Fill the blind_9–12 and L3117 names from Drive into `seen_names.txt`.
- **[Lit-FeS]** Search the literature on genome-wide Fe–S content by energy metabolism before Note H goes further.
- **[Label-cut]** After blind_16, align the `dcf_metals.py` reading label with the frozen 0.50 cut.
