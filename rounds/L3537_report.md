# DCF L3537: Auditing the "Battery–Biology–Physics Triangle" file. Every checkable molecular weight and Fibonacci digit sum is correct; the protein lengths are not; and the Fibonacci "self-encoder" classes turn out to be forced by a Pisano period (2 of 2 new predictions pass)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 14 November 2026

**Input:** Gary's `BATTERY-BIOLOGY-PHYSICS_TRIANGLE.txt` (166 KB, 4,286 lines, dated March 2026).
- **Under the standing rule,** external and earlier numerical claims are recomputed before use.
- **Scripts and outputs:**
  - `rounds/L3537_triangle_audit.py` → `rounds/L3537_triangle_audit_out.txt`;
  - `rounds/L3537_protein_lengths.txt`;
  - `rounds/L3537_fib_model.py`, `rounds/dcf_fib_selfenc_L3537.py`.

---

## 1. What checks out (all exact)
- **Molecular weights, from formulas with standard atomic weights. All 18 claims round correctly:**
  - nucleotides: ATP 507.18, ADP 427.20, AMP 347.22, GTP 523.18, GDP 443.20, CTP 483.16, CDP 403.18, UTP 484.14, UDP 404.16, dTTP 482.17;
  - metabolites: lactic acid 90.08, citric acid 192.12, glucose 180.16;
  - neurotransmitters: dopamine 153.18, acetylcholine cation 146.21;
  - small molecules: OH 17.01, CO₂ 44.01, 6 H₂O 108.09.
- **Fibonacci digit sums (exact big integers). All 17 claims correct:**
  - all 12 values of F(24k) for k = 1–12 (27, 54, 72, 90, 126, 126, 153, 180, 216, 198, 252, 306);
  - F(3), F(7), F(31), F(127) = 2, 4, 31, 121;
  - the list of 16 self-encoders up to 600.
- **"digit_sum(F(24k)) ≡ 0 (mod 9) for all k" is a true theorem.** 9 divides F(12) = 144, so 9 divides every F(12k), and a digit sum keeps the residue mod 9. Checked for k up to 199.
- **Golden angle 137.508° vs 1/α = 137.036:** a real numerical closeness (0.34%), with **no known physical link.** It should be presented as a coincidence.

## 2. What does not check out
**The electron-transport-chain protein lengths** don't match. The file's values against cow Swiss-Prot entries (full-length precursors):

| claim | Swiss-Prot (cow) |
|---|---|
| ATP synthase F1 β = 510 | ATP5F1B 528 aa (about 480 after the import signal is removed; neither is 510) |
| Complex IV core = 520 | MT-CO1 514 aa |
| Cytochrome c = 104 | CYCS 105 aa (104 after the first methionine is removed: **OK**) |
| Complex II = 140 | SDHA 665, SDHB 280, SDHC 169, SDHD 158 (no subunit is 140) |

**Consequence:** the identities built on 510 ("operator product") and 520 should not be used. The clostridial ferredoxin (55), rubredoxin (54) and plastocyanin (99) lengths match the classic textbook proteins but were not checked against a file here.

## 3. New result: the "Class A / Class B" self-encoders are forced by the Pisano period
**The argument:**
- A digit sum keeps its residue mod 9. So digit_sum(F(n)) = n **requires F(n) ≡ n (mod 9).**
- Fibonacci numbers repeat mod 9 with period 24 (the Pisano period).
- Together, only **8 residues of n mod 72 are possible: {0, 1, 5, 10, 31, 35, 36, 62}.**

**Gary's two classes are exactly this:**
- **Class A ("multiples of 9")** = n ≡ 0 or 36 (mod 72), i.e. **multiples of 36**: 72, 180, 216, 252, 360, 504, 540.
- **Class B** = n ≡ 1, 5, 10, 31, 35, 62 (mod 72): 1, 5, 10, 31, 35, 62, 175, 251, 494.
- **The first members of Class B are the residues themselves.**

**Pre-registered** (`PREREGISTERED_L3537_fib_selfencoding.txt`) before any digit sum beyond 600 was computed. The model expected 1.8 self-encoders in [601, 1000], 2.2 in [1001, 3000] and 0.2 in [3001, 20000].

| # | prediction | result |
|---|---|---|
| Q2 | 1–8 self-encoders in [601, 3000] | **3 (946, 1188, 2222): PASS** |
| Q3 | ≤ 1 in [3001, 20000] | **0: PASS** |
| Q1, Q4 (checks) | every one in the allowed residues; Class A = multiples of 36 | **946 ≡ 10, 1188 ≡ 36, 2222 ≡ 62 (mod 72): hold** |

**2 of 2 pass.**
- **The full list up to 20,000:** 1, 5, 10, 31, 35, 62, 72, 175, 180, 216, 251, 252, 360, 494, 504, 540, 946, 1188, 2222.
- **The list stops at 2222.** The digit sum of F(n) grows like about 0.94 n, so it falls further and further below n.

## Record
**+2 passed. 410 of 565 passed, plus 3 split.**

## Summary
- **The triangle file's arithmetic is sound:** 18 molecular weights and 17 Fibonacci digit sums are all exactly right, and the F(24k) mod-9 theorem is true, with a one-line proof.
- **Its protein lengths are not:** ATP synthase β is not 510, complex IV is not 520, and no complex II subunit is 140. Identities built on those numbers should be dropped.
- **New finding: the self-encoder classes are a consequence of the Fibonacci cycle mod 9.** Only 8 residues mod 72 are allowed, and "Class A" is exactly the multiples of 36. A frozen model then predicted correctly how many more appear (3 up to 3,000, none from 3,000 to 20,000). The list ends at **2222**.

## Potential leads for future research
- **[Neurotransmitter table]** The file's neurochemistry section (§ "Consciousness pathway") lists more molecular weights. Audit them the same way.
- **[Pisano lens]** Other DCF digit-sum patterns may also be forced by a Pisano or repetend period mod 9. Check the 1/p digit-sum claims with the same argument.
- **[Ferredoxin lengths]** Verify 55/54/99 against UniProt (*C. pasteurianum* ferredoxin and rubredoxin, poplar plastocyanin).
