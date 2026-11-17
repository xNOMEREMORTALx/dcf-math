# DCF L3793: a size-scaled noise floor removes every false MamP hit (3 of 4); rule 17 adopted. The bacterial magnetite genes still match ordinary families in all six organisms, but the fungal protease falls just outside the cut
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 17 November 2026

**Files:**
- **Pre-registration:** `PREREGISTERED_L3793_magnetite_evalue.txt`.
- **Script:** `rounds/dcf_magnetite_evalue_L3793.py`.
- **Output:** `rounds/L3793_tool_output.txt`, committed before grading.
- **Grader:** `rounds/dcf_grade_L3793.py`, committed before the output was read.
- **Grading:** `rounds/L3793_grade_output.txt`.

**Not blind.** This re-analyses L3789's data, so it tests the floor method, not new biology.

**Method:** a Gumbel (extreme-value) curve fitted to 1,000 shuffled proteins per reference and organism. The E-value is scaled by the number of proteins searched, and hit = E < 0.01.

---

## Results
| # | prediction | result |
|---|---|---|
| E1 | MamP has 0 hits in all six | **PASS:** 0 in all six (best E 0.23–2.93) |
| E2 | MamB, MamE, MamK each hit in all six | **FAIL:** fungal MamE best E = 0.0118, just above 0.01 |
| E3 | ISCA1 hits in all but the fungus | **PASS:** fungus also hits (E = 4e-4) |
| E4 | every hit count ≤ L3789's | **PASS** |

**3 of 4 passed.**

## Hit counts: lenient floor (L3789) → E-value floor
| reference | bee | oyster | frog | alga | fungus | diatom |
|---|---|---|---|---|---|---|
| MamB | 8 → 6 | 123 → 14 | 37 → 4 | 22 → 3 | 8 → 4 | 24 → 2 |
| MamE | 138 → 2 | 908 → 1 | 312 → 5 | 61 → 5 | 65 → **0** | 85 → 2 |
| MamK | 59 → 4 | 447 → 24 | 40 → 9 | 19 → 1 | 38 → 1 | 65 → 3 |
| MamP | 35 → **0** | 52 → **0** | 6 → **0** | 80 → **0** | 33 → **0** | 18 → **0** |
| ISCA1 | 4 → 2 | 355 → 3 | 47 → 3 | 7 → 2 | 12 → 1 | 11 → 3 |

**Best E-values:**
- **MagR/ISCA1:** 1e-62 (frog), 1e-46 (bee, oyster), 1e-26 (diatom), 1e-19 (alga).
- **MamE:** HtrA/PDZ proteases, 1e-21 (diatom) to 1e-9 (alga).
- **MamB:** zinc and cation transporters, 5e-16 (diatom) to 1e-6 (bee).
- **MamK:** actin, 3e-6 to 2e-3, the weakest family.

## Reading
- **The magnetite-specific gene MamP has no homolog** in any of the six, once noise is controlled. That agrees with Bellinger et al.
- **The "magnetosome homologs" MamB, MamE and MamK are real but generic families.** Organisms without magnetite match them as strongly as animals do; the diatom gives the best MamB and MamE scores of all six. **The L3789 conclusion holds:** these genes cannot mark magnetite making.
- **E2's failure is a real limit of the cut.** The fungal nma111 is a genuine HtrA-family protease (named so in UniProt), but its E = 0.012 misses 0.01. Rule 17 therefore requires reporting the best E-value, not just the yes/no call.

## Record
**+3 passed, 1 failed. 541 of 747 passed, plus 3 split.** Audit **208 of 274** (entry "E-value floor (rule 17)").

**Rule 17 adopted** (Standing methods rules, rule 9a): size-scaled E-value floors for shuffled-sequence calibration.

## Summary
- **A floor fitted to 1,000 shuffles and scaled by proteome size cut false hits by up to 900-fold.** It removed every MamP hit while keeping the real families, at E-values down to 10⁻⁶².
- **Bacterial magnetite genes have no animal-specific signal:** the only true matches are transporters, proteases and actin, shared with an alga, a fungus and a diatom.
- **One borderline true homolog (fungal HtrA, E = 0.012) fell outside the cut,** so E2 failed and stands.

## Potential leads for future research
- **[Rule 17 back-check]** Re-score earlier shuffled-floor rounds with the E-value method (descriptive), and list any call that would change.
- **[Marker v2, L3797]** Pre-registered; waiting for the monarch, salmon, coral and limpet proteomes.
- **[RTMP1]** Parked: no deposited protein sequence (the paper gives only raw-read accessions), and it is low-complexity (Ser/Gly-rich), so alignment tests would be unreliable. Revisit if a protein accession appears.
- **[Phone]** Port the E-value floor into the phone's similarity search.
