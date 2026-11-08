# DCF integration map: how the threads connect, what is proved, what is measured, and what failed
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 7 November 2026 (L3133)

**Purpose.** One page showing how every active thread connects. Each link is labelled:
- **[P]** proved;
- **[V]** verified by computation;
- **[B]** passed a blind or pre-registered test;
- **[D]** description only (true, but chosen after looking, so not evidence);
- **[✗]** tested and failed.

**Record:** 256 of 333 pre-registered predictions passed, plus 3 split.

---

## 1. The map
```
                 RECIPROCALS 1/q  ──────────────  DIGIT-AGREEMENT LAW Λ
                 periods, positions               λ_b(c) = (c−1+gcd(c−1,b))/(bc)   [P][V]
                 (mpmath rule)                    c·λ(c)=3 family {21,26,29,30}     [P]
                       │                                   │
      Fibonacci periods: 144→323, 233→467,          26 = Fe, 29 = Cu, 30 = Zn
      89→497867, 377→11311  [B, L3133 4/4]          (same family: [P] arithmetic,
                       │                             the element link is [D])
                       │                                   │
   11×11 GRID (pairs sum 122, centre 61)                   │
   121 = S₅ star, 61 = H₅ hexagon  [P]                     │
   square star grids 1, 11, 109, 1079 (Pell/Lehmer) [P]    │
   mod-24 prime rule, density 1/3  [P][V]                  │
   star prime S_n first divides at index H_n (77/80) [B]   │
                       │                                   │
   ════════════ the bridge is METHOD, not numerology ═══════════════
   (pre-register → compute → base rate → grade; the same discipline both sides)
                       │                                   │
   GENE FINDER v2.30 (label-free)                  METAL-USE PROFILE
   genes found, exact starts 52–92%  [V]           Fe–S CxxC: methanogens 3.4× aerobes, p=6e-5 [B]
   genetic code called blind 104/107 [B]           C2H2 Zn-finger counter 8/8 on human  [B]
   promoters: Firmicutes 17-bp spacer 22/22 [B]    p53 = 43.65 kDa (not 53) [V]; SOD1 15.94 (not 32) [V]
                       │                           Fe-Cu 5 blind: 4/4 PASS (L3137) [B]
                       │                                   │
   EXTRA AMINO ACIDS (the 21st and 22nd)  ─────────────────┘
   pyrrolysine at TAG: 48/48 genes, 9 species [B]  (all Fe/Co-corrinoid methyltransferase partners)
   selenocysteine at TGA: E. coli 3/3 (fdhF, fdnG, fdoG) [B]  (all Mo/W–Fe-S formate dehydrogenases)
   → NCBI note drafted (not sent)
   Sec codons follow Fe-S density blind: rho 0.84, anaerobes 49 vs aerobes 0 (L3145) [B]
   (known biology: Zhang et al., Genome Biol 2006, low oxygen promotes Sec use)
   WITHIN anaerobes, Fe-S density does NOT predict Sec count: blind rho -0.10, pooled 0.18 (L3165) [✗]
   -> the Sec-iron link is the shared oxygen-free lifestyle, not iron itself
```

## 2. The real connections
**A. The 21st and 22nd amino acids sit inside metal enzymes.**
- **Selenocysteine:** the three *E. coli* proteins we recovered are formate dehydrogenases, Mo/W enzymes packed with Fe–S clusters.
- **Pyrrolysine:** the 48 methyltransferases feed methyl groups to cobalt corrinoid proteins in methanogens, the same organisms with the strongest Fe–S signal.
- **So the "iron connector" has a real, measured form.** In our data, the extra codon meanings, Fe–S richness and anaerobic life cluster in the same genomes. That is chemistry (low oxygen keeps Fe–S and Se/Pyl enzymes stable), not a numerical code. Grade [B] for each measurement; the joint picture is [D] until Fe-Cu 5 tests it blind.

**B. 21 meanings.** The standard code has 21 meanings (20 amino acids + stop); with Sec and Pyl, 23. 21 is also exactly two helical turns of B-DNA. [D]

**C. Fibonacci in reciprocals.** For Fibonacci periods F_n (n ≥ 7), the smallest q is a prime ≡ 1 mod 2F_n when F_n is prime (233 → 467, 89 → 497867), and a composite when F_n is not (144 → 323 = 17 × 19). [B for the four pre-registered values; general rule untested]

**D. The grid and the primes.** The 121/61 relation of your 11 × 11 grid recurs inside number theory: star primes first divide star-grid sides at their hexagonal partner's index. [P][B]

## 3. What did *not* connect (tested and failed)
| idea | test | result |
|---|---|---|
| gene lengths at 10.5 / 11-nt "harmonics" | length spectra | no peak [✗] |
| whole-turn helical phasing at junctions | S1, S2 | even/odd rhythm only [✗] |
| 13/37 in gene architecture | several | closed [✗] |
| "long 3′ UTR → brain" | blind 24 genes | 67% (needed 75%) [✗] |
| E. coli promoters label-free | P1, P2, Q1 | no clear signal [✗] |
| p53 "53 kDa" and SOD1 "32 kDa" links | computed masses | 43.65 and 15.94 kDa [✗] |
| digit-chain 4365 → 765 → 135 → 45 → 9 | base rate | true arithmetic, not evidence [D] |

## 4. Where the open threads go next
1. **Fe-Cu 5** (blind, frozen): do three new anaerobes out-score three new aerobes on Fe–S?
2. **Copper motifs** (Fe-Cu 3): add a Cu-site counter (e.g. CxxxC…H…M type-1 sites) to `dcf_metals.py`, validated on known plastocyanin/azurin first.
3. **Sec/Pyl × metal profile:** pre-register that genomes with Pyl genes have Fe–S density above the median, on a new blind set.
4. **R2 twin-prime products** (143, 323, …) and **star-grid literature check** (OEIS).
5. **NCBI note:** verify residue numbers, then your decision.

## Summary
- **The genuine bridge** between the mathematics and the biology is the method: every claim on both sides is pre-registered, computed and graded against a base rate.
- **The strongest real connection** is chemical: the 21st and 22nd amino acids we detected sit inside iron–sulfur and cobalt enzymes, in the same anaerobic genomes that our metal profile marks as iron-rich.
- **Numerical bridges** (26/29 as Fe/Cu, 13/37 in genes, harmonic gene lengths) remain description or have failed tests.

## Potential leads for future research
- **[Fe-Cu 5]** Grade F1–F4 on the six blind genomes.
- **[Fe-Cu 3]** Copper-site counter, validated before use.
- **[SP-1] Sec/Pyl ↔ Fe–S:** blind test of co-occurrence.
- **[R2]** Twin-prime product periods; **[R5]** the general rule for Fibonacci-period minima.
- **[N2]** OEIS/literature for the star-grid note.

## Oxygen and hydrogen (L3169)
- **Oxygen is the hub** linking Fe-S richness and selenocysteine: both rise without oxygen [B]; neither predicts the other within anaerobes [✗].
- **Hydrogen bonds in DNA:** 2 + GC per base pair. Aerobes 2.64 vs anaerobes 2.48 in our 25 genomes [D]; literature: mostly ancestry, real only for obligate aerobes (Aslam et al. 2019).
- **Numbers [V], links [D]:** Lyman-α 121.567 nm (121 = S₅); deuterium 61.40 MHz at 9.39 T (61 = H₅; instrument-dependent); 21-cm line 1420.405751768 MHz.
- **Λ law [P]:** 1·λ(1) = 1 (hydrogen alone); 16·λ(16) = 2 (with K 19, Ca 20); 17·λ(17) = 18·λ(18) = 9/5.
- **Reciprocals [P]:** periods of 1/17 and 1/19 are 16 and 18, hence 1/323 has period lcm(16, 18) = 144.
- **Fe-O blind (L3173), 2 of 4:** facultatives fall between (barely) and carry selenocysteine; but two host-associated fermenting obligate anaerobes
  (*Fusobacterium* 0.34, *Treponema* 0.49) read below the 0.50 cut [✗]. The Fe-S profile marks Fe-S-heavy anaerobic *energy metabolism*
  (methanogens, sulfate reducers, acetogens, syntrophs), not oxygen intolerance as such.
