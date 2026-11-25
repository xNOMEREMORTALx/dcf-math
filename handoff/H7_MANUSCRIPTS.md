# DCF Handoff 7 of 8: the manuscripts and notes, status and next step for each
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 24 November 2026 (after L3997)

**Each manuscript's numbers come from committed round outputs.** All files are in `dcf-math/notes/`; older versions are kept beside the latest.

---

## Manuscript 1: the iron–sulfur ladder (`Manuscript_FeS_ladder_draft_v0.12.md`)
**Title.** "One iron–sulfur motif sorts microbial genomes by energy metabolism: pre-registered, blind tests from raw DNA."

**Core.**
- **The motif:** the 3-3-4 ladder C-x₂-C-x₂-C-x₃-C, per 1,000 aa of label-free predicted proteins.
- **The scale:** four tiers (lactic | O₂ respirers | H₂ fermenters | ferredoxin-based).
- **Blind results:**
  - **35 of 37** genomes in their pre-assigned tier, ρ = 0.962; the latest set 12 of 12.
  - **Large-protein ladders** separate O₂ respirers from H₂ fermenters 5.3×, against 0.99× for small-ferredoxin counts (the closest prior art, Campbell et al. 2019).
  - **Protists with Ladder-P (…-C-P):** 10 of 10.
- **Mechanism (from annotation, read after grading):** hydrogenases, PFOR, Rnf, heterodisulfide reductase and electron-bifurcating flavoproteins.

**Status.**
- v0.12, with an overclaim check, a number audit and four figures.
- The submission plan is `Submission_plan_FeS_ladder_v0.1.md`: bioRxiv → Peer Community In Microbiology → Peer Community Journal.

**Next.** An outside reader, then the preprint.

**Companion notes:**
- **Note H v0.8** (ferredoxin signature);
- **Note "information iron" v0.3:** DNA-repair FCL iron is a switch, energy iron is a dial; blind 3/3.

## Manuscript 2: nerve metal chemistry (`Manuscript_nerve_metals_draft_v0.21.md`)
**Title.** "Reading the metal chemistry of nervous systems from sequence alone: pre-registered blind tests across animals."

**Core.**
- **Label-free selectivity rules:** K⁺ T-V-G-Y-G, Na⁺ DEKA, Ca²⁺ EEEE/EEDD, and the P-type pump loop.
- **Blind record:** **149 of 181** predictions over 29 tests. Na vs Ca: 4 swaps in 23,994 calls. UniProt reference: 345 of 351 class calls agree.
- **The sodium domain-III letter E → K** marks the step to nerve-type NAV1. The sea urchin and acorn worm lost NAV1 (they keep E-type NAV2).
- **Battery ratio:** channels per pump ≈ 1.8 separates animals with and without nerves.
- **Neural kit:** NR1 or a lysine sodium channel, 34 of 36 organisms. The NALCN ring is followed across the tree.

**Status.**
- v0.21, with Figures 1–9 and the reader brief `Reader_brief_Manuscript2.md`.
- Audit: 149/181.

**Next.**
- Consider splitting it into a **methods paper** (the rules and blind tests) and an **evolution paper** (E → K, NALCN, the battery).
- Run a rule audit (standing rules 4–8 for absence claims).
- Then an outside reader.

## Manuscript 3: K⁺-channel genes at CTCF loop anchors (`Manuscript3_CTCF_nerve_metal_genes_draft_v2.9.md`)
**Title.** "Pore-forming potassium-channel genes sit at CTCF-bound chromatin loop anchors across human cells and tissues: a pre-registered report."

**Core (sections 3.1–3.28):**
- **The main result:** the matched-gene (length and density) dependence-aware test.
  - **Ten cell lines:** K⁺ p = 0.008, all p = 0.002.
  - **WTC11, blind:** p = 0.006.
  - **CTCF-anchored Hi-C loops** in motor neurons, astrocytes, colon and muscle, under three CTCF references.
- **The same genes carry it everywhere** (ρ 0.66–0.78).
  - **Leaders:** the non-voltage-gated families.
  - **Core genes:** KCNMA1, KCNJ5, KCNQ5, KCNC1, KCNJ11, KCNH1 and KCNA2.
- **Never shown by:**
  - auxiliary subunits;
  - non-K⁺ tetramers;
  - six-fold channels;
  - OXPHOS genes;
  - resting-potential transporters, in tissues.
- **Loop partners:** K⁺-gene loops end at gene starts half as often as matched genes' loops (Hi-C; replicated blind).
- **Honest downgrades:**
  - the neural-lineage reading;
  - the T-cell assay reading (L3953 → L3961);
  - T cells are mixed.

**Figures.**
- `figures/L3821_manuscript3.png`;
- `figures/L3841_manuscript3_fig1_v2.png`;
- `figures/L3865_tencell_z.png`.

The later sections (3.16–3.28) have tables but no new figure yet.

**Next.**
1. Leads 1–2 of H5 (T-cell activation, HUVEC Hi-C).
2. Freeze v3.0.
3. A new Figure 3: the three-reference forest plot and the partner fractions.
4. A reader brief.
5. bioRxiv.

## Manuscript 4: the cryptochrome tryptophan chain (`Manuscript4_cryptochrome_tetrad_note_draft_v0.7.md`)
**Title.** "The cryptochrome tryptophan chain predates nervous systems: a pre-registered sequence survey from single-celled relatives to birds."

**Core.**
- **Conservation:** the TrpA–D chain is conserved in bird CRY1/2/4 (615 sequences) and in every sponge.
- **The family rule:** aromatic TrpD = cryptochrome, 98.6% of 2,564 PANTHER proteins.
- **Fish class I photolyases:** H → Y at TrpD in several fish groups (descriptive).
- **The reader** is on the phone (menu 37) and in dcf-genefinder.

**Status.** v0.7.

**Next.**
- The fish H/Y blind test (H5 lead 11).
- PANTHER CRY1/2, plant CRY and CRY-DASH subfamilies, for a superfamily-wide TrpD map.

## Mathematics notes
| note | file | status |
|---|---|---|
| Λ, digit agreement | `Note_Lambda_digit_agreement_draft_v0.5.md` | proved core; literature check pending |
| Star grids / Lehmer | `Note_star_grids_Lehmer_draft_v0.2.md` | proved; OEIS/zbMATH check [N2] |
| Heegner 41/163 (Note K) | `Note_Heegner_41_163_v0.1.md` | verified classical facts; expository |
| E8 / 600-cell (Note E) | `Note_E8_600cell_helix_v0.1.md` | verified; expository |
| Gene finder (Note G) | dcf-genefinder `docs/NoteG_label_free_gene_finder_draft_v1.2.md` | needs v2.32 and the 140/143 code record |
| Decimal periods paper | claude.ai Project `Paper_draft_v0.38_Decimal_periods_as_signals.md` | older; cleanup lead [Manuscript v1.21] |

**Status pages:** `notes/DCF_status_2026-11-23.md` (latest).

**Methods appendix:** `notes/Standing_methods_rules_v1.md`.

## Summary
- **Four manuscripts:**
  - Manuscript 1 (iron ladder) is submission-ready pending a reader;
  - Manuscript 2 (nerve chemistry) is ready for a reader and may split;
  - Manuscript 3 (CTCF anchors) is two data tests from a v3.0 freeze;
  - Manuscript 4 (cryptochrome) is a short note awaiting the fish blind test.
- **The mathematics notes** are proved or verified, and need literature checks before any novelty claim.

## Potential leads for future research
- **[Readers]** One outside reader per manuscript, using the reader-brief template.
- **[Figure 3, Manuscript 3]** A forest plot of p and excess across all maps and references.
- **[Note G v1.3]** Update with v2.32 and the 140/143 code record.
