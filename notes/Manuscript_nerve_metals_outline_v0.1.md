# Manuscript 2 (outline v0.1): Reading the metal chemistry of nervous systems from mRNA sequence alone. Pre-registered tests across mammals, fish and birds
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 14 November 2026 · outline, not for submission

## Working abstract (draft)
**The idea.** Ion channels and pumps choose their metal ion with short, conserved loops:
- the K⁺ filter T-V-G-Y-G;
- the Na⁺ DEKA ring;
- the Ca²⁺ EEEE/EEDD ring;
- the P-type pump helix-4 loop.

**What we built.** We wrote label-free rules that read these loops from the longest open reading frame of each mRNA, and sort proteins by the ion they pass. Additional rules find:
- glutamate and NMDA receptors (the SYTANLAAF gate);
- the iron site of the aromatic amino-acid hydroxylases (dopamine, serotonin).

**How we tested them.** Every rule was frozen and hashed before blind testing. Tool output was committed before gene names were read.

**Results.** Across four blind data sets (mouse, zebrafish curated, zebrafish predicted, chicken), **40 of 45 pre-registered predictions passed.**
- **Four of the five failures** were calls on genes that are channels or receptors by their own NCBI description or nearest relative, but that the frozen naming rule did not credit.
- **One failure** was a chance 6-residue match. It was corrected (7 residues) and clean in the next blind test.

**Conclusion.** The metal-selecting loops of the nervous system are conserved in kind across ~450 million years, and they can be read directly from sequence.

## 1. Introduction
- Ion selectivity is set by short loops (structural background: K⁺ filter, Na⁺/Ca²⁺ rings, P-type pumps).
- The gap: annotation transfer depends on names and homology search. A transparent, label-free motif reader is useful for new or poorly annotated genomes.
- **The nerve "battery":**
  - pumps store ATP energy as ion gradients;
  - channels release it as impulses.

## 2. Methods
1. **Input:** RefSeq mRNA. One transcript per gene: lowest NM_ number (mouse) or longest ORF (fish/bird).
2. **Rules:**
   - voltage sensor S4;
   - calcium ring count;
   - sodium lysine loop;
   - K filter (`k_filter2`);
   - weak-sensor route (Kv7, KCNH);
   - K2P rule;
   - iGluR, NMDA7, FeHyd2;
   - pump signature + helix-4 loop.
   
   Table of each rule with its development data.
3. **Pre-registration protocol:**
   - hash ledger;
   - tool-before-names commits;
   - dropped-not-replaced files;
   - amendments only before data.
4. **Truth rules** v1 (symbols), v2 (symbol or description), v3 (any word order; fly list). The limitation is stated: names lag biology.
5. **Development sets:** human files 1–4, mouse files 1–3, zebrafish (after its test), each listed.

## 3. Results
| § | content | source |
|---|---|---|
| 3.1 | development: the textbook rings recovered (CACNA1B, CACNA1G, SCN2A pore loops) | L3425 |
| 3.2 | mouse blind (10/10); note that v1 and v2 gave identical calls, so they are not independent | L3429 |
| 3.3 | zebrafish curated (10/11) and predicted (7/10); paralogs keep their metal | L3441, L3445 |
| 3.4 | chicken (13/14; 103/104 calls correct); pumps by metal 11/11 | L3457 |
| 3.5 | failures, every one explained | table |
| 3.6 | the 9-nt rhythm: an illustration only, local to S4 (flank test 0.93 / 1.95 / 1.00) | L3449, L3453 |
| 3.7 | (if run) insect blind test | L3461 |

## 4. Discussion
- **Conservation in kind:** the same ring and filter types appear across all four lineages, and both copies of duplicated fish genes kept their metal.
- **What this approach cannot do:**
  - auxiliary/silent subunits (KCNG);
  - divergent K2P channels;
  - sodium sensors (Naₓ);
  - consciousness itself.
- **What it can support:** quick, transparent screening of poorly annotated genomes (the unnamed Kv-like zebrafish genes).

## 5. Data and code
- Repositories dcf-math (rounds, pre-registrations, LEDGER) and dcf-genefinder (`dcf_nerve.py`, `dcf_pump.py`, `dcf_neurometal.py`, `dcf_k2p.py`).
- Phone menu 34.
- Zenodo DOIs before submission.

## Figures planned
1. The metal-gate motifs (K, Na, Ca, pump loop) with real examples from four species.
2. Blind results per species: precision and recall bars, with failures annotated.
3. Phylogenetic distance against pass rate (mouse, fish, bird, [fly]).

## Before drafting
- **Wait for the fly result** (L3461). It is the largest evolutionary span.
- Recompute every number in the table from the committed grade outputs (number audit, as for Manuscript 1).

## Summary
- The nerve-chemistry work now has enough frozen, graded results across four data sets for a short second paper: **40 of 45 passed, with every failure explained.** This outline sets its structure.

## Potential leads for future research
- **[Fly]** Run L3461 when the file arrives; it becomes §3.7.
- **[Audit 2]** A number audit script for the manuscript table, as with Manuscript 1.
- **[Figure N1]** The four-lineage motif panel.
