# DCF L3817: phone 6.19 reads a whole proteome for cryptochromes. Honeybee: 6 of 6 hits identical to the computer scan
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 18 November 2026

**Files:**
- **Phone app:** `phone/dcf_phone_6.19.py`.
- **Bundle:** `phone/dcf_phone_bundle_6.19.zip`.
- **Reader:** `phone/dcf_cryreader.py`, unchanged from L3813.

---

## What changed
- **Menu 37 now accepts a whole proteome:** a UniProt TSV or FASTA, compressed .gz files included.
- Above 200 proteins it switches to **whole-proteome mode:** it gives a time estimate and a progress line every 1,000 proteins, and lists **only the hits**.
- The closing note now gives the current blind record (40 of 40 confident) and the SF18 finding.

## Checks
| check | result |
|---|---|
| the reader on all 19,057 honeybee proteins (7,631 in the window) against the L3785 scan | **6 of 6 hits identical, no extra hits** |
| time, one computer core | 7 min 11 s; the phone estimate shown is 12–50 min |
| menu 37 run end-to-end on `bee.tsv.gz` | the same 6 lines |
| phone self-test | **270/270** |

## Other changes this round
**v1.2.0 DOIs recorded.**
- **dcf-math:** 10.5281/zenodo.24331499.
- **dcf-genefinder:** 10.5281/zenodo.24331605.
- **The "all versions" (concept) DOIs** are now cited in the CITATION files and README badges: dcf-math 10.5281/zenodo.24234794 and dcf-genefinder 10.5281/zenodo.24234985. Future releases need no citation edits.

**The dcf-math GitHub release is tagged v1.3.0, but Zenodo records it as v1.2.0** (taken from CITATION.cff, 7 seconds after publication). The phone bundle zip is inside the archived repository (`phone/dcf_phone_bundle_6.18.zip`), so the archive is complete even without an attached file.

## Summary
- **Anyone with the phone bundle can now scan a whole downloaded proteome for cryptochromes and read their electron chains.** It gives the same answers as the computer scan.

## Potential leads for future research
- **[L3809]** Waiting for the SF18 and SF17 downloads.
- **[Phone, any species]** Gary can run menu 37 on any UniProt proteome himself. A blind prediction written down *before* running would count like any other round.
- **[Manuscript 3 figure]** Re-run the frozen L3725 permutation with its null values saved (same seed, so the same summary), and draw the 3-panel figure.
