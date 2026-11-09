# Digital Cosmos Framework: verified mathematics and phone toolkit

**Author:** Gary NOMEREMORTAL Mason.

Verified number-theory results from the Digital Cosmos Framework (DCF).
- **Pre-registration.** Every prediction was hashed and frozen before its test was run.
- **Honest grading.** Every result is graded honestly, failures included.
- **Running record:** 284 of 389 pre-registered predictions passed, plus 3 split (L3241).

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
- **`phone/`:** the DCF phone toolkit (`dcf_phone_6.05.py`, self-test 257/257), a DNA codec and an error-correcting code. Runs in Pydroid 3 on Android.
- **`preregistrations/`:** 86 frozen prediction files from rounds L2746–L3189, with `LEDGER.md` listing their SHA-256 hashes.
- **`rounds/`:** round reports and hashed tool numbers from L3181 on.

**Related.** The gene finder is in [dcf-genefinder](https://github.com/xNOMEREMORTALx/dcf-genefinder).

## Status
**Drafts.** Both notes still need a specialist literature check (zbMATH/MathSciNet, OEIS) before any claim of novelty.

**What the record is.** The pre-registration record documents the method. It is not a claim that every DCF idea holds; failed predictions are kept and reported.

## License
MIT (see `LICENSE`), the same as dcf-genefinder.

- **[INTEGRATION.md](INTEGRATION.md):** one-page map of all threads, each link labelled proved / verified / blind-passed / description / failed.

- **[handoff/](handoff/):** six-part handoff (H1 start here, H2 formulas and theorems, H3 gene-finder toolkit, H4 repos/phone/Drive workflow, H5 leads path, H6 round log).
