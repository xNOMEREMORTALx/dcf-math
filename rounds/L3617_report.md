# DCF L3617: The sea hare's learning receptors. Alignment sorts its 33 glutamate receptors into NMDA, AMPA and kainate types, matching UniProt's names one for one (2 of 2); a second tardigrade test is frozen
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 15 November 2026

**Leads:** [Sea hare memory kit], [Tardigrade sodium channel].
- **Pre-registration:** `PREREGISTERED_L3617_aplysia_tardigrade.txt`.
- **Script:** `rounds/dcf_aplysia_nmda_L3617.py` → `rounds/L3617_grade_output.txt`.

---

## A. The sea hare's glutamate receptors (local aligner, nearest mouse receptor)
| class | count | examples (UniProt name) |
|---|---|---|
| **NMDA** | **9** | 4 × "NMDA receptor subunit 1" → **Grin1**; 2 × "NR2" → Grin2b; NMDA 3A-like → Grin3a |
| AMPA | 15 | "GluR1–GluR5, GluR8, GluR10" → Gria1/2/4 |
| kainate | 9 | "GluR7", "kainate-binding protein" → Grik1/2/3 |

- **G1 (≥ 2 nearest a mouse NMDA receptor): 9, PASS.**
- **G2 (at least one nearest Grin1, the obligatory NR1 subunit): 4, PASS.**

**Descriptive, after grading:** for every one of the 33 receptors, the aligner's class matches the class in UniProt's own name (NMDA, AMPA-type GluR, or kainate).
- **Note:** UniProt lists several sea-hare receptors twice (old and new accessions with identical sequences), so the distinct count is lower than 33.

**Reading:**
- **The sea hare, the animal in which the cellular basis of learning was first worked out, carries the full NMDA "learning switch":** the NR1 subunit plus NR2 and NR3 subunits, as well as AMPA- and kainate-type receptors.
- **The NMDA motif failed outside vertebrates (L3465), but alignment identifies NMDA receptors reliably in a mollusc.**

## B. Second tardigrade (frozen, waiting for data)
**Hypothesis:** tardigrades lost channels. *Ramazzottius varieornatus* should therefore show:
- **T1:** a channels-per-pump ratio below 1.8;
- **T2:** no DEKA sodium channel.

https://rest.uniprot.org/uniprotkb/stream?format=tsv&compressed=true&fields=accession,organism_name,protein_name,sequence&query=organism_id%3A947166

## Record
**+2 passed. 438 of 597 passed, plus 3 split.** Nerve-chemistry audit **105 of 124.**

## Summary
- **The sea hare's 33 glutamate receptors sort cleanly by alignment:** 9 NMDA (including 4 NR1), 15 AMPA and 9 kainate. Every one agrees with UniProt's name.
- **The NMDA learning switch is present in this classic memory animal,** and the aligner now finds NMDA receptors where the short motif could not.
- **A second tardigrade is frozen** to test whether tardigrades lost channels.

## Potential leads for future research
- **[Tardigrade]** Grade T1–T2.
- **[NMDA across the tree]** Use the aligner to count NR1-type receptors in every lineage tested (sponge → human). Where does the learning switch first appear?
