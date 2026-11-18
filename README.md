# Digital Cosmos Framework: verified mathematics and phone toolkit

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24234794.svg)](https://doi.org/10.5281/zenodo.24234794) (all versions; latest v1.2.0: [10.5281/zenodo.24331499](https://doi.org/10.5281/zenodo.24331499); v1.1.0: [10.5281/zenodo.24302678](https://doi.org/10.5281/zenodo.24302678); v1.0.0: [10.5281/zenodo.24234795](https://doi.org/10.5281/zenodo.24234795))


**Author:** Gary NOMEREMORTAL Mason.

Verified number-theory results from the Digital Cosmos Framework (DCF).
- **Pre-registration.** Every prediction was hashed and frozen before its test was run.
- **Honest grading.** Every result is graded honestly, failures included.
- **Running record:** 291 of 411 pre-registered predictions passed, plus 3 split (L3261).

## Contents
- **`notes/Note_Lambda_digit_agreement_draft_v0.5.md`:** a closed-form law for how often a number and its multiple share digits.
  - The formula: λ_b(r/s) = 1/b + j(d − j)/(brs).
  - The proved maximum 2/(b + 1), and the complement, block and shift laws.
  - Algebraic numbers: powers of φ, the silver and plastic numbers, and roots.
  - Bases 3 and 5.
  - Confirmed on 10⁶ digits of π, e, √2, φ and others.
- **`notes/Note_star_grids_Lehmer_draft_v0.2.md`:** square grids whose cell count is a star number (sides 1, 11, 109, 1079, …).
  - Their Lehmer-sequence structure.
  - A mod-24 classification of the primes that divide them (density 1/3).
  - Star-number sides of hexagonal-number grids.
- **`notes/Note_FeS_ferredoxin_signature_draft_v0.3.md`:** Note H, an iron–sulfur signature of ferredoxin-based metabolism in raw genomes (eight pre-registered rounds, failures kept).
- **`phone/`:** the DCF phone toolkit (latest `dcf_phone_6.18.py`, bundle `dcf_phone_bundle_6.18.zip`, self-test 270/270): nerve chemistry, aligners, DNA data store and the cryptochrome reader (menu 37). Runs in Pydroid 3 on Android.
- **`preregistrations/`:** 185 frozen prediction files from round L2746 on, with amendments, and `LEDGER.md` listing their SHA-256 hashes.
- **`rounds/`:** round reports and hashed tool numbers from L3181 on.

**Related.** The gene finder is in [dcf-genefinder](https://github.com/xNOMEREMORTALx/dcf-genefinder).

## Status
**Drafts.** Both notes still need a specialist literature check (zbMATH/MathSciNet, OEIS) before any claim of novelty.

**What the record is.** The pre-registration record documents the method. It is not a claim that every DCF idea holds; failed predictions are kept and reported.

## License
MIT (see `LICENSE`), the same as dcf-genefinder.

- **[INTEGRATION.md](INTEGRATION.md):** one-page map of all threads, each link labelled proved / verified / blind-passed / description / failed.

- **[handoff/](handoff/):** six-part handoff (H1 start here, H2 formulas and theorems, H3 gene-finder toolkit, H4 repos/phone/Drive workflow, H5 leads path, H6 round log).
