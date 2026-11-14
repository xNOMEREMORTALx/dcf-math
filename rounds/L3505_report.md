# DCF L3505: Figure 4 (the E → K letter across the animal tree) and a pre-registered comb-jelly test
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 14 November 2026

**Leads:** [E→K figure], [Ctenophore]. **No predictions graded.**

---

## 1. Figure 4 (`figures/L3505_EtoK.png`)
**What it shows:** the domain-III pore loop of the 4-domain sodium-type channel in eight sequences, read from the files already graded.

| organism | loop (6 letters each side) |
|---|---|
| choanoflagellate (*Monosiga*) | VALLQV **ATF E GW** MEIMEA |
| placozoan (*Trichoplax*) | LALFEV **ATF E GW** IQVMGD |
| sea anemone (*Nematostella*) | LALLQV **ATF E GW** MEIMED |
| fruit fly (para) | LCLFQV **ATF K GW** IQIMND |
| zebrafish (scn8aa) | LALLQV **ATF K GW** MDIMYA |
| chicken (SCN2A) | LSLLQV **ATF K GW** MDIMYA |
| human (SCN2A) | LSLLQV **ATF K GW** MDIMYA |
| human Naₓ sensor (SCN7A) | LSLLQV **ATF N GW** ITIMNS |

**Reading:**
- **The A-T-F-·-G-W frame,** and even the "Q-V" just before it, is identical from a single-celled choanoflagellate to human.
- **Only the ring letter changes:**
  - **E** in the three lineages at or before the first nerves;
  - **K** in every bilaterian nerve sodium channel;
  - **N** in the sensor.
- **The placozoan sequence,** which completes the early group, was found while making this figure. It was not part of a prediction.

**Manuscript 2 v0.4** now lists Figure 4.

## 2. [Ctenophore] Pre-registered (`PREREGISTERED_L3505_ctenophore.txt`)
**Why comb jellies:** they may have evolved nerves independently of all other animals. If the K is a bilaterian invention, their sodium-type channels should not carry it.

**Predictions:**
- **T1:** no sodium calls.
- **T2:** every 4-domain voltage-sensor protein with the A-T-F-x-G-W loop has **x ≠ K**.
- **T3:** at least 3 potassium channels.

## Action for Gary: one file
https://rest.uniprot.org/uniprotkb/stream?format=tsv&compressed=true&fields=accession,organism_name,protein_name,sequence&query=taxonomy_id%3A10197

**If it errors:** search `taxonomy_id:10197` on uniprot.org and download as TSV.

## Record
No predictions graded. **403 of 555 passed, plus 3 split.** T1–T3 are waiting.

## Summary
- **One picture now tells the story:** the same pore loop, letter for letter, across 600+ million years. The only change is E → K, at the step from early animals to the nerve sodium channels of bilaterians, plus N in the sodium sensor.
- **Next:** the comb jellies, the other lineage with nerves. Do they also lack the K?

## Potential leads for future research
- **[Ctenophore]** Grade T1–T3.
- **[Outside reader]** Manuscript 2 v0.4 is ready for someone outside the project to read.
- **[DEEA selectivity]** Do E-type channels behave as calcium-selective? The literature says the early DEEA channels pass calcium. This is a literature note for the Discussion, not a computation.
