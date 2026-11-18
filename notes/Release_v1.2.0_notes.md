# Release v1.2.0: notes to paste into GitHub (17 November 2026)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework

## dcf-math v1.2.0: release description (copy everything between the lines)
---
**DCF v1.2.0 (rounds L3781–L3813).** Pre-registered blind tests: 549 of 755 predictions passed overall, plus 3 split; biology audit 216 of 282. Every failure is kept.

**New since v1.1.0:**
- **Cryptochrome family marker:** a confident cryptochrome carries an aromatic residue at the fourth tryptophan of the electron chain (TrpD).
  - Blind: **40 of 40** in 11 animals (honeybee, oysters, frog, monarch, salmon, limpet, two corals, mussel; L3785, L3797, L3805).
  - The strict version failed once (L3785, 14 of 17) and is kept. The only exceptions are weak hits, which PANTHER places in the class I DNA-repair photolyase subfamily (SF18; blind test L3809 pre-registered).
- **Magnetite:** the bacterial magnetite genes MamB, MamE and MamK match only generic families in animals (zinc transporters, HtrA proteases, actin). Organisms with no magnetite carry them as strongly (L3789, 4 of 5). MamP has no homolog once noise is controlled (L3793).
- **Methods:** rule 17, a size-scaled E-value floor for shuffled-sequence calibration (L3793).
- **Manuscript 4** (cryptochrome tryptophan chain) v0.6.
- **Phone bundle 6.18** (attached): menu 37, the cryptochrome reader (family, TrpA–D chain, marker call). About 0.01 s per protein; identical to the scan on all 63 blind hits. Self-test 270/270.

Not for medical use.
---

**Asset to attach:** `phone/dcf_phone_bundle_6.18.zip`.

## dcf-genefinder v1.2.0: release description
---
**dcf-genefinder v1.2.0.**
- **dcf_cryreader.py (new):** reads a protein's cryptochrome/photolyase family against six references, its four-tryptophan electron chain (TrpA–D), and the aromatic-TrpD marker.
  - Blind-tested in dcf-math: 40 of 40 confident cryptochromes aromatic.
  - Identical to the frozen scan on all 63 blind hits.
  - Needs numpy, `dcf_localalign.py` and `dcf_align.py`.
- **README:** usage example.

Not for medical use.
---

**No asset needed.** Zenodo archives the repository automatically.

## After both releases
**Zenodo mints two new DOIs, one per repository.** Send me both and I'll put them into the CITATION files, READMEs and manuscripts, as for v1.1.0.

## Summary
- **v1.2.0 packages rounds L3781–L3813:** the cryptochrome marker (blind 40 of 40), the magnetite tests, rule 17, and the phone/genefinder cryptochrome reader.

## Potential leads for future research
- **[L3809]** The SF18/SF17 blind test goes into v1.3.0.
- **[Concept DOI]** Cite each repository's Zenodo *concept* DOI, which always points to the latest version, so the CITATION files need no edit per release.
