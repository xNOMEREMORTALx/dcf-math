# DCF L3237: blind_19 frozen (lineage pairs in three new phyla, the 3-3-4 ladder as a marker, the island finder with self-set eligibility); Note E (E8 geometry) and Note G v1.2 written
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 9 November 2026

**Leads pursued:** [Fe-lineage], [Fe-ladder], [Fe-island b] (pre-registered), [E8-note], [Note G v1.2], [H4-codes] (assessed).

**Pre-registration:** `PREREGISTERED_L3237.txt`, SHA-256 `25031d48…784e`, commit `5bdd62d`, pushed before download. The new ladder script, `rounds/dcf_ladder_L3237.py`, was frozen in the same commit (SHA-256 `68c51f7b…7d91`).

---

## 1. blind_19 — three new phyla
| pair | ferredoxin-based member | partner (same phylum) |
|---|---|---|
| P1 Euryarchaeota | NC_007681 *Methanosphaera stadtmanae* DSM 3091 (H2/methanol methanogen) | NC_006396 *Haloarcula marismortui* chr I (aerobic halophile) |
| P2 Chloroflexota | NC_014314 *Dehalogenimonas lykanthroporepellens* BL-DC-9 (anaerobic organohalide respirer) | NC_010175 *Chloroflexus aurantiacus* J-10-fl (phototroph, 3-hydroxypropionate cycle) |
| P3 Bacteroidota | NC_009615 *Parabacteroides distasonis* ATCC 8503 (anaerobic fermenter, ferredoxin-dependent PFOR) | NC_009441 *Flavobacterium johnsoniae* UW101 (aerobe) |

**Checks.** All six are absent from both seen lists, and each was matched to a genome page by accession (BacMap/KEGG).

**Predictions:**
- **L1:** CxxC member > partner in 3 of 3 pairs.
- **L2:** 3-3-4 ladder member > partner in 3 of 3.
- **L3:** the ladder separates pairs more sharply than CxxC in ≥ 2 of 3.
- **L4, L5:** the island finder, eligible only where CxxC ≥ 0.60. L4: ≥ 3× enrichment in each eligible genome. L5: ≥ 60% of islands carry an Fe–S/redox gene.

**Ladder smoke test** (seen genomes only): *Desulforapulum* 0.127 ladders per 1,000 aa; *Leuconostoc* 0.

**Action for Gary.** Zip these six as **`blind_19.zip`**:
1. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NC_007681&rettype=gbwithparts&retmode=text
2. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NC_006396&rettype=gbwithparts&retmode=text
3. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NC_014314&rettype=gbwithparts&retmode=text
4. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NC_010175&rettype=gbwithparts&retmode=text
5. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NC_009615&rettype=gbwithparts&retmode=text
6. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NC_009441&rettype=gbwithparts&retmode=text

## 2. Note E v0.1 — "From sphere packing to E8: a computed tour"
`dcf-math/notes/Note_E8_600cell_helix_v0.1.md`:
- E8's 240 roots and packing density;
- the 600-cell counts;
- the E8 → two 600-cells fold in the golden ratio;
- the tetrahedral helix (131.81°, rise 1/√10, 2.73 per turn, rings of 30).

Every number is reproduced by the L3233 scripts. A table marks which links are theorems, which are published biology (α-helix and collagen via Sadoc–Rivier), and which are coincidences (DNA, 30, 10).

## 3. [H4-codes] E8 and DNA storage — assessed, not adopted
**The connection is real.** E8 is built from the extended Hamming [8,4,4] code (Construction A). It is the optimal lattice for **continuous (Gaussian) noise**.

**Why it isn't the right code here.** The DCF DNA codec (`dcf_dna_ecc.py` v6) faces **substitutions, insertions, deletions and lost strands**. It already handles them with Reed–Solomon erasure coding across strands, a rotating inner code and consensus alignment. E8's advantage does not carry over to that error type.

**Recorded as [D]:** a fair comparison would use a quaternary analogue, e.g. a Hamming-type inner code over GF(4), against the current inner code on simulated reads.

## 4. Note G v1.2
In dcf-genefinder: v2.32 and its two blind start tests (§3k: the failure without the guard, then the pass), and the code record of 134 of 137. The start gap to Prodigal narrows from about 6 points to about 4.

## Record
No predictions graded this round. **281 of 380 passed, plus 3 split.**

## Summary
- **The next blind test is frozen.** Three pairs of related microbes from three phyla not yet tested (archaea, Chloroflexota, Bacteroidota). It asks whether the ferredoxin-based member reads higher, whether the 3-3-4 cysteine ladder is a sharper marker than the simple count, and whether the island finder works when it decides for itself where it applies.
- **The E8 / 600-cell / helix geometry is now a self-contained note**, with every number reproducible.
- **E8 links to error-correcting codes, but its strength is for continuous noise,** so it would not improve the DNA storage codec as it stands.
- **The gene-finder paper draft is current** with v2.32.

## Potential leads for future research
- **[Blind 19]** Grade L1–L5 when `blind_19.zip` arrives.
- **[GF4-inner]** Simulated comparison: a GF(4) Hamming-type inner code vs the current rotating inner code, under substitution-heavy read errors.
- **[DNA-packing]** Literature: tetrahedral or icosahedral models of condensed or encapsidated DNA.
- **[Ess-strand]** Re-run the strand test without ribosomal-like genes (pre-register first).
