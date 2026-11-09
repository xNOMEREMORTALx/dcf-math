# DCF Handoff 4 of 6: dcf-math, the phone bundle, and the GitHub / Drive workflow
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 8 November 2026

---

## 1. dcf-math repository (`xNOMEREMORTALx/dcf-math`, MIT)
| path | contents |
|---|---|
| `README.md` | overview, with the line "**Running record:** 256 of 333 pre-registered predictions passed, plus 3 split." |
| `INTEGRATION.md` | one-page map of all threads, each link labelled [P]/[V]/[B]/[D]/[✗]; includes the oxygen and hydrogen section and the L3173 correction |
| `notes/Note_Lambda_digit_agreement_draft_v0.5.md` | the Λ law note |
| `notes/Note_star_grids_Lehmer_draft_v0.2.md` | the star-grid / Lehmer note |
| `phone/` | `dcf_phone_6.05.py`, `dcf_dna_codec.py`, `dcf_dna_ecc.py`, `README_PHONE.txt` |
| `preregistrations/` | 85 files + `LEDGER.md` (filename → SHA-256); the latest is `PREREGISTERED_L3169.txt` |
| `handoff/` | this series, H1–H6 |

## 2. Phone bundle (Pydroid 3 on Android)
| file | SHA-256 |
|---|---|
| `dcf_phone_6.05.py` | a5ab407aa6a81d518e6de310cf1fdd3ab79c5f228c8ed2e7ea639dcd32409fb0 |
| `dcf_dna_codec.py` | dca12b53e5358f6dcf99c8f261e27f8ffff0c563878bc8eefb81dee486fc4e49 |
| `dcf_dna_ecc.py` | dd583cfb386dc71f847db8bb137fb41903ce109b3f6e18730ef85d4a220e95ed |

- **Set-up:** copy all files plus `dcf_genefinder_mobile.py` (v2.31, from dcf-genefinder) into one folder, and pip-install numpy and mpmath.
- **Self-test: 257/257.**
- **6.05 functions:** `silver_power_share(n)`; `power_share(rel, m, n, b=10)` (in newthm20).
- **Menu items:**
  - 25: DNA view of 1/p (base-4 Midy = Watson–Crick);
  - 26: gene finder;
  - 27: DNA storage;
  - 28: theorems L2422–L2848 (reduction clock, casting out 10^q − 1, Dedekind variance, 2–5 lemma, Note B, Theorem R);
  - 29: Gary's reduction in any base plus the period clock.
- **Note:** `README_PHONE.txt` still lists the v2.30 gene-finder hash; use v2.31 from dcf-genefinder.

## 3. Git workflow (in the cloud session)
```bash
git -c user.name="Gary NOMEREMORTAL Mason" -c user.email=author@example.invalid commit -m "L####: <what>"
git push origin HEAD
```
- **Commit footer:** end commit messages with the attribution lines the session's system instructions give, if any.
- **After every graded round:**
  1. update the record in `README.md` and `INTEGRATION.md`;
  2. add the pre-registration and its ledger row;
  3. update `CHANGELOG.md` in dcf-genefinder if code changed;
  4. append the blind accessions to `seen_accessions.txt`.
- **Never commit** genome files, personal data or Gary's email.

## 4. Google Drive
- **Folder:** **`11-3-2026 handoff`**, which Gary is copying: round reports, code zips and drafts from this conversation.
- **Connector:** use the Google Drive connector. Search the folder by name, and read files on demand rather than all at once.
- **Off limits (privacy):** iCloud photos, HealthSummary zips, `dna-data-2022-09-06`, `mydata*`, esoteric images, the "Nov 25, 2020 – Jun 10, 2026.zip".
- **Earlier Drive items of interest:** Gary's own documents, e.g. `Zinc_Fingers_.txt`. They are externally generated text, so every number in them is untrusted until checked.

## 5. Other project docs (claude.ai project, read-only in practice)
- **Formulas:** `GARYS MASTER FORMULAS.txt`, `Garys Formulas and theorems.txt`.
- **Paper drafts:** `Paper_draft_v0.35–v0.38_Decimal_periods_as_signals.md` (manuscript; cleanup lead **Manuscript v1.21**).
- **Hand-offs and logs:** `Claude Handoff Series .txt`, `Handoff Claude 10-10-2026.txt`, and the Perplexity / Grok logs.

## Summary
- **dcf-math** holds the mathematics notes, the phone bundle, the full pre-registration ledger (85 files), the integration map and this handoff.
- **Every round** updates the record line, the ledger and the seen list, and pushes under Gary's name with a placeholder email.
- **Drive** holds the conversation's files in `11-3-2026 handoff`; personal files stay closed.

## Potential leads for future research
- **[Phone 6.06]** Bundle gene finder v2.31 plus `dcf_metals` and `dcf_secflag` into a phone menu item ("metal profile / Sec candidates"); refresh `README_PHONE.txt` hashes.
- **[Repo hygiene]** Add a `handoff/` index to the dcf-math README.
