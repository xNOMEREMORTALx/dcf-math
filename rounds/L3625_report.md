# DCF L3625: Where did the NMDA "learning switch" begin? NR1 receptors appear in cnidarians and bilaterians, and are absent from sponges, comb jellies and single-celled relatives (12 of 15)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 15 November 2026

**Leads:** [NMDA across the tree], [Ecdysozoa sodium loss] (frozen, waiting for data).

**Files:**
- **Pre-registration:** `PREREGISTERED_L3625_nr1_tree_ecdysozoa.txt`.
- **Script:** `rounds/dcf_nr1tree_L3625.py`. It was hashed into the ledger and pushed before it ran.
- **Tool output:** `rounds/L3625_tool_output.txt`, committed before grading. Grading is in `rounds/L3625_grade_output.txt`.

**Method:**
- **Organisms:** 21 complete proteomes already on disk, from protists to chordates.
- **Steps:** every glutamate-receptor call (dcf_nerve v2) is aligned (local aligner) to the 18 mouse receptors.
- **"NR1 call":** the nearest mouse receptor is Grin1, the obligatory subunit of every NMDA receptor.

**Disclosure:** the pre-registration says "Total 16 predictions", but it lists **15**. The total was my counting error; the 15 listed predictions are graded.

---

## Results
| group | organism | iGluR calls | NR1 calls | prediction | result |
|---|---|---|---|---|---|
| non-animals | *Capsaspora*, *Monosiga*, *Salpingoeca* | 0, 0, 0 | 0 | N6: none | **PASS** |
| sponges | *Amphimedon*, *Geodia*, *Ephydatia*, *Oopsacas* | 0, 0, 0, 0 | 0 | N5: none | **PASS** |
| comb jelly | *Mnemiopsis* | 11 | **0** | N4: none | **PASS** |
| placozoan | *Trichoplax* | 8 | 0 | N3: ≥ 1 | **FAIL** |
| cnidarians | *Nematostella* | 9 | 1 | N2a | **PASS** |
| | *Hydra* | 3 | **3** | N2b | **PASS** |
| acoel | *Hofstenia* | 15 | 3 | N1i | **PASS** |
| protostomes | *Capitella* (annelid) | 16 | 1 | N1a | **PASS** |
| | *Lingula* (brachiopod) | 12 | 1 | N1b | **PASS** |
| | *Aplysia* (sea hare, L3617, not graded again) | 33 | 4 | — | — |
| | *Hypsibius* (tardigrade) | 9 | 1 | N1g | **PASS** |
| | *Ramazzottius* (tardigrade) | 10 | 2 | N1h | **PASS** |
| deuterostomes | *Strongylocentrotus* (sea urchin) | 7 | **0** | N1c | **FAIL** |
| | *Saccoglossus* (acorn worm) | 10 | 2 | N1d | **PASS** |
| | *Branchiostoma* (lancelet) | 48 | 1 | N1e | **PASS** |
| | *Ciona* (sea squirt) | 6 | **0** | N1f | **FAIL** |

**12 of 15 passed.**

## Descriptive, after grading (UniProt names)
- **Hydra:** all three NR1 calls are named "Glutamate receptor ionotropic, NMDA 1" or "NMDA receptor subunit zeta-1". The names agree with the alignment.
  - Two more Hydra entries named NMDA 1 were not called; both lack the S-Y-T-A-N-L-A-A gate (fragments or divergent).
- **Sea urchin and Ciona (failures):** no protein in either UniProt set is named NMDA, and every full-length receptor aligns nearest AMPA or kainate.
  - Either these two deuterostomes lost NR1, or their gene is missing from the annotation.
  - Both are possible. The acorn worm and lancelet, their close relatives, do have NR1, so a loss would be specific to those lineages.
- **Trichoplax (failure):** its glutamate receptors in UniProt are mostly short pieces (354–601 aa, against about 900 for a full receptor). Six align nearest kainate and two nearest AMPA; none aligns nearest NR1.
  - This failure is graded as a failure. Short entries weaken the test, and that is noted as a data limit, not an excuse.
- **Comb jelly:** it has 11 glutamate receptors but **none is NMDA-like**. They align nearest kainate or AMPA. This fits the view that comb-jelly receptors are a separate lineage.
- **Sponges and single-celled relatives:** **no protein carries the receptor gate at all,** in four sponges and three protists.

## Reading: the learning switch on the tree
```
Capsaspora, choanoflagellates ... no glutamate receptors (gate motif absent)
sponges ......................... no glutamate receptors (gate motif absent)
comb jelly ...................... glutamate receptors, but no NMDA type
placozoan ....................... receptors (fragments), no NR1 found
cnidarians ...................... NR1 present  <-- earliest NR1 in this data
acoel, protostomes, most deuterostomes ... NR1 present
sea urchin, sea squirt .......... NR1 not found (loss or missing annotation)
```
- **In these data, the NMDA learning switch first appears in the cnidarians** (sea anemone, Hydra), the first animals with nerve nets. It is kept across bilaterians, including both tardigrades.
- **It coincides with nervous systems,** not with multicellularity:
  - sponges, which have no neurons, have no glutamate receptors at all;
  - comb jellies, which built their nerves separately, have glutamate receptors but no NMDA type.
- **This is a parts list, not a measure of learning.** Animals without NR1 may still learn by other means.

## Waiting for data (part B, frozen)
**The question:** is sodium-channel loss general in moulting animals, or specific to nematodes and tardigrades?

**Predictions:** E1–E3: each animal below has ≥ 1 voltage-gated Na channel; E4–E5: the horseshoe crab's and the mite's battery ratios are above 1.8.

**Download links** (one file per organism):
- **Horseshoe crab:** https://rest.uniprot.org/uniprotkb/stream?format=tsv&compressed=true&fields=accession,organism_name,protein_name,sequence&query=organism_id%3A6850
- **Spider mite:** https://rest.uniprot.org/uniprotkb/stream?format=tsv&compressed=true&fields=accession,organism_name,protein_name,sequence&query=organism_id%3A32264
- **Priapulid:** https://rest.uniprot.org/uniprotkb/stream?format=tsv&compressed=true&fields=accession,organism_name,protein_name,sequence&query=organism_id%3A37621

## Record
**+12 passed, 3 failed. 452 of 614 passed, plus 3 split.** Nerve-chemistry audit **119 of 141.**

## Summary
- **Across 21 proteomes, the NMDA receptor's obligatory NR1 subunit appears first in cnidarians** and is kept across bilaterians.
- **Where it is absent:** sponges and single-celled relatives (no glutamate receptors at all) and the comb jelly (receptors, but no NMDA type).
- **Score:** 12 of 15 pre-registered predictions passed.
- **The three failures:**
  - **Trichoplax:** its receptor entries are fragments.
  - **Sea urchin and sea squirt:** no NR1 was found. That is either a loss or missing annotation, still to be resolved.
- **The learning switch arrives with nerves.**

## Potential leads for future research
- **[Sea urchin / Ciona NR1]** Test with mRNA (RefSeq) rather than UniProt. If NR1 is found there, the failure was the annotation; if not, it is a loss.
- **[Trichoplax full-length]** A newer placozoan assembly (e.g. *Trichoplax* sp. H2 or *Hoilungia*) to retest N3 with full-length receptors.
- **[Comb-jelly receptor class]** Align *Mnemiopsis* receptors to each other and to the anemone's. Do they form their own group (the "epsilon"-type idea)?
- **[Ecdysozoa sodium loss]** Grade E1–E5 when the three files arrive.
- **[Manuscript 2]** Add §3.13 (sea hare), §3.14 (second tardigrade) and §3.15 (NR1 on the tree) as a new figure: presence/absence on the animal tree.
