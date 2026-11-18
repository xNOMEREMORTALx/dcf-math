# DCF L3801: Phone 6.17, a cryptochrome reader on the phone (menu 37). It reproduces all 21 blind L3797 hits exactly; self-test 270/270
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 17 November 2026

**Files:**
- **Phone app:** `phone/dcf_phone_6.17.py`.
- **New module:** `phone/dcf_cryreader.py`.
- **Bundle:** `phone/dcf_phone_bundle_6.17.zip` (12 .py files plus README_PHONE.txt with SHA-256 hashes).

---

## What menu 37 does
Give it a protein FASTA, a UniProt TSV, or a pasted sequence. For each protein (400–900 residues) it reports:
1. **Family:** the best of six references (robin CRY4, fly 6-4 photolyase, fly class II photolyase, zebrafish DASH, fungal CPD photolyase, diatom DASH). A score below 350 means not detected.
2. **The electron chain:** the four residues at TrpA–D, read by traceback alignment to robin CRY4 (positions 395, 372, 318, 369).
3. **The marker call, in plain words:**
   - "confident" (score ≥ 900) or "weak";
   - whether TrpD fits the blind-tested marker (31 of 31 confident cryptochromes aromatic).

The method is the one frozen in L3777/L3781. It is not changed, only packaged.

## Checks
| check | result |
|---|---|
| all 21 L3797 hits (monarch, salmon, limpet), re-read by the phone module | **21 of 21 identical** (score, tetrad, family) |
| self-test row L3801: robin CRY4 reads WWWW and confident; zebrafish DASH reads non-aromatic TrpD; shuffled CRY4 not detected; 300-residue fragment refused | **PASS** |
| full phone self-test with all 12 files | **270/270** |
| without the new files | the row skips cleanly; 267/267 |
| menu 37 on the monarch's CRY1 (pasted) | score 957, WWWW, confident, fits the marker |

## Summary
- **The phone can now read any protein's cryptochrome family and its four-tryptophan electron chain** and say whether it fits the blind-tested marker.
- **It reproduces the computer scan exactly** (21 of 21) and passes the full self-test (270/270).
- **A new pre-registered round (L3805)** tests the one open question: do weak hits break the marker more often? It uses two corals and two bivalves.

## Potential leads for future research
- **[L3805, weak class]** Pre-registered; needs four downloads (staghorn coral, cauliflower coral, blue mussel, eastern oyster).
- **[Genefinder]** Add `dcf_cryreader.py` to the dcf-genefinder repository for the next release (v1.2.0).
- **[Phone speed]** The traceback is pure Python (about 280,000 cells per protein). A numpy anti-diagonal version would make whole-proteome reading practical on the phone.
