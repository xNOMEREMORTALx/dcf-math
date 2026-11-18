# DCF status page, 17 November 2026 (evening update, after L3813)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework
*A one-page map of where everything stands. Counts are from `rounds/L3485_audit2.py` and the round reports.*

## Record
- **Blind predictions overall:** **549 passed of 755, plus 3 split.**
- **Audit of the biology tests (nerve chemistry onward):** **216 of 282.**
- **Every failure is kept.** Grader bugs were fixed in the parser only, with the originals kept. Disclosed design flaws are listed in each report.

## Manuscripts
| # | title (short) | latest draft | status |
|---|---|---|---|
| 1 | Fe–S ladder (number theory and iron–sulphur) | `Manuscript_FeS_ladder_draft_v0.12.md` | submission plan ready; **waiting for an outside reader** |
| 2 | Reading the metal chemistry of nervous systems from sequence | `Manuscript_nerve_metals_draft_v0.21.md` | 29 blind tests, 149/181; §2.5 absence rules added; reader brief ready; **consider splitting** (methods paper + evolution paper) |
| 3 | Nerve-metal genes at CTCF (zinc) loop anchors | `Manuscript3_CTCF_nerve_metal_genes_draft_v0.2.md` | first full draft; **needs its 3-panel figure** |
| 4 | The cryptochrome tryptophan chain predates nervous systems | `Manuscript4_cryptochrome_tetrad_note_draft_v0.6.md` | aromatic-TrpD marker blind: **40 of 40 confident cryptochromes** in 11 animals (L3785, L3797, L3805); the only exceptions are weak hits in PANTHER SF18 (class I DNA-repair photolyases). **L3809 (SF18 vs SF17 blind) waits for two downloads** |

**Supporting documents:**
- `Reader_brief_Manuscript2.md` (outside reader);
- `Standing_methods_rules_v1.md` (16 rules + rule 17: size-scaled E-value floors, L3793);
- `Submission_plan_FeS_ladder_v0.1.md`.

## Tools
- **Phone bundle 6.18:** 12 files, self-test 270/270.
  - Menu 34: nerve chemistry.
  - Menu 35: aligner.
  - Menu 36: DNA data store with a noisy-read index.
  - Menu 37: cryptochrome reader (family, TrpA–D chain, blind-tested marker), about 0.01 s per protein on a computer.
- **dcf-genefinder:** `dcf_nerve.py` v3, `dcf_pump.py`, the aligners, and `dcf_cryreader.py` (unreleased, for v1.2.0).
- **Zenodo DOIs:**
  - dcf-math: 10.5281/zenodo.24302678 (v1.1.0; v1.0.0 24234795);
  - dcf-genefinder: 10.5281/zenodo.24302710 (v1.1.0; v1.0.0 24234986).

## What Gary can do next
1. **Download the two L3809 files** (PANTHER SF18 and SF17; links in the L3805 message).
2. **Send a reader brief** to an outside reader (Manuscripts 1 and 2).
3. **Make the next GitHub releases** (dcf-math v1.2.0, dcf-genefinder v1.2.0) when ready, so Zenodo archives the cryptochrome reader and rounds L3781–L3813.
4. **Free space in the claude.ai Project** (it is full), if documents should be kept there.

## Open scientific leads (top five)
1. **[L3809]** Are all marker exceptions class I DNA-repair photolyases (PANTHER SF18)? Pre-registered; waiting for data.
   - **Magnetite (L3789/L3793):** the bacterial magnetite genes match only generic families in animals. The real animal lead is the chiton protein RTMP1, which is parked (no deposited sequence).
2. **[CTCF v2 blind]** Pre-register the relaxed CTCF finder on new proteomes.
3. **[Neurons]** Loop maps from neurons, to test the "poised battery genes" hypothesis (Manuscript 3).
4. **[Fragment-rescue rule]** The partial sodium channel needs more blind calls before it ships.
5. **[Gear speed dial]** S4 tooth count against published channel activation speeds.

## Summary
- **One page covering the record, the four manuscripts, the tools, three actions only Gary can take, and the top five scientific leads.**

## Potential leads for future research
- **[Status page]** Refresh this page at each milestone, rather than repeating the information in every report.
