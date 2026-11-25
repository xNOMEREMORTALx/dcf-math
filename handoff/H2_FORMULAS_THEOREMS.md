# DCF Handoff 2 of 8: formulas and theorems, mathematics and biology
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 24 November 2026 (after L3997)

**Labels:**
- **[P]** proved;
- **[V]** verified by computation or a cited source;
- **[B]** passed a blind / pre-registered test;
- **[D]** description only (true, but noticed after looking, so not evidence);
- **[✗]** tested and failed.

**Full texts.** dcf-math `notes/`:
- Λ note v0.5;
- star-grid note v0.2;
- Note K (Heegner);
- Note E (E8);
- the manuscripts;
- `rounds/L####_report.md`.

---

# Part A. Mathematics

## A1. The digit-agreement law Λ
- **Theorem 1 [P].** For τ uniform and gcd(r, s) = 1: P(⌊b{sτ}⌋ = ⌊b{rτ}⌋) = 1/b + j(d − j)/(brs), where d = gcd(r − s, b) and j = r mod d.
- **Theorem Λ [P].** For an integer multiplier c in base b: **λ_b(c) = (c − 1 + gcd(c − 1, b)) / (bc)**. The digits of a normal number x and of cx agree with this frequency.
- **Theorem 4 [P].** λ_b(r/s) ≤ 2/(b + 1), with equality only for {r, s} = {1, b + 1}.
- **Theorem 5, complement [P].** P(digit x + digit (r/s)x = b − 1) = 1/b − j′(d′ − j′)/(brs), where d′ = gcd(r + s, b).
- **Extensions [P]:** blocks of k digits use base b^k; affine maps; powers and roots of algebraic numbers.
- **Families of c·λ(c) in base 10 [P]:**
  - 3: {21, 26 (Fe), 29 (Cu), 30 (Zn)};
  - 2: {11, 16, 19 (K), 20 (Ca)};
  - 9/5: {17, 18};
  - 1: {1}.

  The element readings are [D].

## A2. Star grids (Gary's 11 × 11 grid: pairs sum to 122, centre 61)
- **Figurate numbers:** S_n = 6n(n − 1) + 1 (star) and H_n = 3n(n − 1) + 1 (centred hexagonal). **S_n = 2H_n − 1 [P]**, so 121 = S₅ has centre 61 = H₅.
- **Square star numbers [P]:** m² = S_n ⇔ 3(2n − 1)² − 2m² = 1.
  - The sides are m = 1, 11, 109, 1079, 10681, …, with m_{k+1} = 10m_k − m_{k−1}.
  - The generating function is (1 + x)/(1 − 10x + x²), which gives 10100/9001 at x = 1/100.
- **Lehmer form [P]:** m_k = (α^(2k+1) − α^−(2k+1))/(2√2), where α = √3 + √2. Also gcd(m_j, m_k) = m_g, where 2g + 1 = gcd(2j + 1, 2k + 1).
- **Which primes divide some grid side, by p mod 24 [P; V to 10⁵]:**
  - 13 and 23: always;
  - 5, 7, 17 and 19: never;
  - 11: exactly when α is a square;
  - 1: with probability 1/2^(s−1);
  - overall density 1/3.
- **Observation [B at 80%]:** a star prime S_n ≡ 13 (mod 24) first divides a grid side at index H_n in 77 of 80 cases below 10⁶.

## A3. Reciprocals 1/q
- **Period [P]:** the period of 1/q is ord_q(10). The period of 1/(pq) is the lcm of the two periods.
- **1/323 = 1/(17·19) [P]:** period lcm(16, 18) = 144 = F₁₂ = 12². It is the only twin-prime product with a square period below 10⁶, which Pell explains (L3189).
- **Smallest q with period F_n [B]:**

  | F_n | 13 | 21 | 34 | 55 | 89 | 144 | 233 | 377 |
  |---|---|---|---|---|---|---|---|---|
  | q | 53 | 43 | 103 | 1321 | 497867 | 323 | 467 | 11311 |

  - **Further minima:** they turn composite at 610 and 987 (L3189–L3197). The F₁₇ minimum is a 21-digit prime (L3201).
  - **Rule:** a prime period n forces p ≡ 1 (mod 2n).
- **Midy, exact rule for composites [P/V to 10⁴, L3601]:**
  - **The property:** 1/n has "complementary halves" (digit sum 9L/2) ⇔ 10^(L/2) ≡ −1 (mod n) ⇔ every prime-power factor's period has the same 2-adic valuation, and it is ≥ 1.
  - **Example:** 437 = 19·23 has periods 18 and 22, one factor of 2 each, so the property holds.
  - **But a digit sum of 9L/2 can occur without the property** (29 cases below 1,000) **[✗ P2].**
- **27 · 37 = 999 [P]:** so 1/37 = 0.027…, 1/27 = 0.037…, and 27 = 3³ (L3985).
- **Repunits [P]:**
  - R₂ = 11, R₃ = 111 = 3·37;
  - R₈ = 11111111 = 11·73·101·137.
  - **The primes with period 8 are exactly 73 and 137.** Every prime other than 2 and 5 divides some repunit.
- **2701 = 37·73 = T₇₃ [P]:**
  - **Period of 1/2701:** 24 (lcm of 3 and 8).
  - **One period:** 000370233246945575712699, digit sum 99 = 9·11.
  - **Every number with period exactly 24 divides 10²⁴ − 1:** there are 1,756 such numbers. **Exactly three are triangular:** 2701 (T₇₃), 37401 (T₂₇₃), 862641 (T₁₃₁₃).
  - **153 = T₁₇** is the smallest triangular number with period 16 (L3985, exact; descriptive).
- **Fibonacci digital roots [P]:** they repeat every 24 (the Pisano period mod 9). One cycle sums to **117**.
- **Repdigit identity [P] (L3709):** 444·12 = 666·8 = 888·6 = 5,328 = 144·37.

## A4. π positions (all mpmath-verified, L3985)
- **401** first occurs at position **1197**.
- **Digit 1170 is 5;** there is no 5 in 1171–1201; **digit 1202 is 5.** 1201 is prime.
- **Digits 1170–1202 sum to 127.**
- **Base rate:** 19 such 5…5 gaps of ≥ 32 digits occur in the first 5,000 digits (≈ 20 expected), so the window is ordinary.
- **The project's earlier test** put 401 at 1197 as an ordinary position (geometric-null CDF 0.70).
- **The D(n) chain (Gary's):** D(T₂₉) = 1197, D(T₇₃) = D(2701) = 9697 = prime(1197); 401 = prime(79). **[P/V arithmetic; the gold reading is D.]**

## A5. Euler 41, Heegner 163 and the near-cubes (Note K) [V]
- **Euler's polynomial:** n² + n + 41 is prime for n = 0…39.
- **Rabinowitsch:** the lucky numbers p ∈ {2, 3, 5, 11, 17, 41} are exactly those with 4p − 1 ∈ {7, 11, 19, 43, 67, 163}, the class-number-1 (Heegner) fields.
- **Near-cubes:** e^(π√163) = 640320³ + 744 − 7.5·10⁻¹³.

## A6. Geometry (Note E) [V]
- **E8:** 240 roots, each with 56 neighbours at inner product 1.
- **Packing density:** π⁴/384 (Viazovska 2017).
- **The 600-cell:** 120 unit quaternions. The E8 roots fold into two 600-cells in the golden ratio.
- **The Boerdijk–Coxeter tetrahelix** is computed in `rounds/L3233_bc_helix.py`.

## A7. Closed or failed numerical bridges (do not reopen without a new idea)
- **[✗]** 13/37 in gene architecture.
- **[✗]** Gene lengths at 10.5- or 11-nt harmonics.
- **[✗]** Metal proton/neutron numbers as DNA intervals (0 of 7; codon control 35 of 35).
- **[✗]** 5 and 41 as DNA frequencies.
- **[✗]** A nuclear-count pattern for iron.
- **[D]** The 4365 → 765 → 135 → 45 → 9 chain.
- **[D]** 7, 78, 79 and 401 in the potassium results: they are set by gene-naming and threshold choices (L3925).
- **[D]** The 1/37 → 027 reduction steps (DCF reduction rules are chosen operations).

---

# Part B. Biology formulas (frozen rules used by the tools)

## B1. Gene finder and genome readers
- **Genetic code call:**
  - read-through test plus ORF-length ratio;
  - genome-size prior (> 2.5 Mb keeps code 11);
  - tiny AT-rich genomes (< 300 kb, GC < 0.25) use a ratio cut of 1.45.
- **Start choice:** a learned start signal (log-odds −20..−1 plus start-codon preference, 30-nt window). v2.32 has a guarded GC-rich start fix (H3).
- **Pyrrolysine:** TAG read-through joins; 48/48 genes in 9 species [B].
- **Selenocysteine:** TGA read-through candidates (`dcf_secflag`). Optional coding filter `--coding T`, AUC 0.87 in development.

## B2. The iron–sulfur "ladder" energy scale (Manuscript 1)
- **The 3-3-4 ladder:** C-x₂-C-x₂-C-x₃-C (the [4Fe-4S] ferredoxin motif), counted **overlapping**, per 1,000 aa of predicted protein.
- **Prokaryote tiers (frozen L3257):** tier 1 < 0.0045 ≤ tier 2 < 0.023 ≤ tier 3 < 0.060 ≤ tier 4.
  - 1: lactic fermenters;
  - 2: oxygen respirers and oxygenic phototrophs;
  - 3: H₂-making fermenters;
  - 4: ferredoxin-based respirers and autotrophs.
  - **Blind:** 35 of 37 genomes in their pre-assigned tier, ρ = 0.962 **[B]**.
- **Ladder-P (eukaryotes):** C-x₂-C-x₂-C-x₃-C-P, counted non-overlapping. **Cut 0.0017;** protists 10/10 blind **[B]**. The plain eukaryote cut was 0.0035 (6/6 blind).
- **Large-protein ladders (> 200 aa)** separate O₂ respirers from H₂ fermenters **5.3×**; small-ferredoxin counts give 0.99× **[B]**.
- **Information iron:** the FCL loop C-x₆-C-x₂-C-x₅-C (endonuclease III / MutY) behaves as a **switch** (present or absent), while energy iron behaves as a **dial** **[B]**.
- **Other motifs:**
  - **CxxC density:** methanogens 3.4× aerobes **[B]**.
  - **C2H2 zinc finger** `C.{2,4}C.{12}H.{3,5}H`: 8/8 on human proteins **[B]**.
  - **Rubredoxin knuckle; CuA copper marker.**
  - **R** = observed CxxC ÷ Σ(len − 3)·f_C².

## B3. Nerve metal chemistry (Manuscript 2; `dcf_nerve.py` v3)
- **Potassium filter:** T-V-G-Y-G, plus T-T-L-G-Y-G for Kv3/Kv4. **Sodium:** the DEKA ring. **Calcium:** the EEEE/EEDD ring. **Pumps:** the P-type helix-4 loop.
- **The sodium domain-III letter:**
  - **K form:** A-T-F-**K**-G-W in nerve sodium channels (NAV1);
  - **E form:** A-T-F-**E**-G-W in early and ambulacrarian channels (NAV2);
  - **v3** also accepts T-W-K-G-W.
- **Battery ratio:** voltage-gated channels per P-type pump. **Cut ≈ 1.8** separates animals with and without nerves (blind 4/5; tardigrades fall below).
- **Neural kit:** NR1 (NMDA) or a lysine sodium channel → nerves. **34 of 36** organisms **[B]**. **NR1 score floor: 941.**
- **Voltage-sensor "gear teeth":** a charge every third residue in S4 (90% of true channels).
- **Record:** 149 of 181 blind predictions across 29 tests **[B]**.

## B4. Cryptochrome chain (Manuscript 4; `dcf_cryreader.py`)
- **The chain:** robin CRY4 tryptophans TrpA 395 → TrpB 372 → TrpC 318 → TrpD 369.
- **The family rule [B]:** **TrpD = W/Y/F → cryptochrome-type; otherwise → photolyase-type.** Right for **2,527 of 2,564** PANTHER-classified proteins (98.6%) at any score. Blind: 40 of 40 confident cryptochromes.
- **Exceptions:** fish class I photolyases swap H → Y at TrpD (one C → T change) in several fish groups (L3833, descriptive).

## B5. The 3D-genome (chromatin loop) test (Manuscript 3)
- **Gene table:**
  - GENCODE v49 protein-coding genes on chr1–22 and X;
  - window TSS ± 5 kb;
  - a gene is "at an anchor" if its window overlaps a loop anchor.
- **Gene sets:**
  - **KCN:** 96 K⁺ genes.
  - **KPORE:** 79 pore-forming K⁺ genes:
    - Kv, `KCN[ABCDFGHQSV]\d`, 40;
    - K2P, `KCNK`, 15;
    - Kir, `KCNJ`, 16;
    - KCa, KCNMA1/KCNN/KCNT/KCNU, 8.
  - **Kaux:** 17 auxiliary subunits.
  - **ALL:** 139 nerve-metal channel genes.
- **Matched null (L3869):**
  - each member gets the 50 nearest non-channel genes in (z log₁₀ gene length, z log₁₀(1 + TSS count within ±1 Mb));
  - 10,000 random sets draw one candidate per member;
  - all maps in a group are scored together (mean over maps);
  - p_upper and p_lower are reported.
- **Anchors:**
  - **4DN union files:** loops tagged CTCF-ChIAPET.
  - **ENCODE ChIA-PET:** top 28,270 loops by PET count.
  - **Hi-C:** all loops (the "chr" prefix is added).
  - **"CTCF-anchored" Hi-C loops:** loops whose two anchors both overlap a CTCF reference. There are three references:
    - H1/HFFc6 ChIA-PET anchors;
    - the union of T-cell ChIA-PET anchors;
    - T-cell CTCF peaks (ENCFF416VKW + ENCFF478NWL).
- **Partner fraction (L3969):** the share of a gene's loops whose other end lies within 5 kb of another protein-coding TSS, against matched genes.
- **Promoter fraction (L3929):** the share of anchors within 5 kb of a protein-coding TSS.

## B6. Methods rules (summary of `notes/Standing_methods_rules_v1.md`)
1. **Numbers from any source:** untrusted until recomputed; mpmath for positions; name number families before looking.
2. **Absence calls:** need a measured sensitivity. One organism means "not detected"; annotation sets the ceiling.
3. **Similarity searches:**
   - no k-mer shortlists at deep distances;
   - score floors are calibrated, not chosen;
   - use reciprocal best hits;
   - **rule 17:** E-value floors scale with search size (Gumbel fit to ≥ 1,000 shuffles).
4. **Statistics:**
   - use matched controls for grid/digit effects;
   - use cluster-preserving permutations;
   - thresholds must be reachable;
   - use length-matched controls.
5. **Process:** freeze, hash, run, commit, then read. Identify files by content. Test the test.
6. **Added in practice since L3877:**
   - check that a restriction step cannot import the effect (**reference control, L3961**);
   - pre-registered interpretations must cover split outcomes, or state that a split is "not established".

## Summary
- **The mathematics** has a proved core (Λ, star grids and Lehmer, reciprocal periods, Midy for composites, repunits and period 24) and the verified Heegner/E8 notes. The numerical bridges to biology remain description or have failed.
- **The biology** has frozen, blind-tested rules: the gene finder, the iron ladder scale, nerve selectivity rules, the cryptochrome family rule and the chromatin matched-gene test.

## Potential leads for future research
- **[Period-24 test]** Pre-register a statement about triangular numbers and reciprocal periods in a new range (H5).
- **[N2]** Literature/OEIS check of the star-grid sides and the mod-24 table before any novelty claim.
- **[Λ isotopes]** Λ families of stable mass numbers against a shuffled control.
