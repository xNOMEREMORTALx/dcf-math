# DCF L3773: A five-reference cryptochrome/photolyase finder (2 of 4). The 17 bilaterian absences persist; class II DNA photolyases remain invisible to this finder
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 17 November 2026

**Files:**
- **Pre-registration:** `PREREGISTERED_L3773_cry_multiref.txt`.
- **Script:** `rounds/dcf_cry_multiref_L3773.py`.
- **Output:** `rounds/L3773_tool_output.txt`.
- **Grading:** `rounds/L3773_grade_output.txt`.

**References:** robin CRY4, fly 6-4 photolyase, zebrafish cry-dash, the *Neurospora* DNA photolyase (P27526) and the diatom DASH (B7FV99).

**Organisms (25):** the four reference animals, three outgroups (alga, fungus, diatom), and the 18 bilaterians listed as having no L3761 hit.

---

## Results
| # | prediction | result |
|---|---|---|
| M1 | held-out named proteins found: fungal DASH Q7SI68, algal photolyase Q9XHE2, diatom photolyase B7FZ06 | **FAIL:** Q7SI68 yes; the other two no |
| M2 | 9 animal controls found | **PASS** (9 of 9) |
| M3 | the nematode still has 0 hits | **PASS** |
| M4 | ≥ 5 of the other 17 bilaterians gain a hit | **FAIL:** none |

**2 of 4 passed.**

**Disclosures:**
- **The pre-registered "zero-hit" list wrongly included the bdelloid rotifer *Adineta*,** which already had two DASH hits in L3761.
- **One zebrafish gene name contains colons,** which breaks the display of that hit. No grade is affected.

## Reading
- **Adding two photolyase-type references (a fungal class I DNA photolyase and a diatom DASH) found nothing new** in 17 bilaterians:
  - the nematode;
  - all nine flatworms;
  - both tardigrades;
  - the leech and *Dimorphilus*;
  - the priapulid;
  - the acoel, the acorn worm and Ciona.
  
  **This makes those absences more credible, though still "not detected"** (Standing rule 5).
- **The finder still misses a whole branch.** The algal and diatom photolyases (Q9XHE2, B7FZ06) are probably **class II** DNA photolyases, a different branch from the fungal class I reference. The fly's own class II photolyase (*phr*) was not hit either.
  - **So the remaining absences are "no cryptochrome, no class I photolyase, no DASH detected".** Class II photolyases are untested.
- **Outgroups (descriptive):**
  - the fungus's DASH reads WW-E;
  - its class I photolyase reads WWW-L;
  - the alga's DASH proteins read WWW-G / WWW-Q;
  - the diatom's DASH reads WWW-N.
  
  **In every DASH and photolyase, the fourth position is non-aromatic.** Only the animal-like cryptochrome lineage carries W or Y/F there.

## Record
**+2 passed, 2 failed. 528 of 730 passed, plus 3 split.** Audit **195 of 257.**

## Summary
- **Five references instead of one recovered the fungal DASH protein and all animal controls,** but found nothing in the 17 bilaterians where no cryptochrome was detected before. Those absences now look more solid.
- **The finder still misses class II DNA photolyases,** so they remain an untested branch.
- **Across DASH and photolyases, the fourth position of the chain is never aromatic.** Tryptophan or tyrosine there belongs to the animal-like cryptochromes.

## Potential leads for future research
- **[Class II photolyase]** Add the fly *phr* (class II CPD photolyase) as a sixth reference, with Q9XHE2 and B7FZ06 as must-find controls.
- **[The aromatic fourth as a family marker]** Pre-register: across all hits, an aromatic (W/Y/F) at TrpD occurs only in proteins nearest CRY1/CRY2/CRY4/6-4, and never in DASH or CPD photolyases.
- **[Manuscript 4]** Add §3.5 (multi-reference) and the family-marker observation.
