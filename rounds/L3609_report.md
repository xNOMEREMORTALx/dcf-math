# DCF L3609: The nerve battery across 17 organisms. Channels per pump separates animals with and without nerves at about 1.8 (Figure 7); a 5-organism blind test is frozen
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 15 November 2026

**Leads:** [Battery ratio as a test], [Figure 7].
- **Tool:** `rounds/dcf_battery_L3609.py` (dcf_nerve v2: proteins with a channel tag ÷ proteins with a metal-pump tag).
- **Output:** `rounds/L3609_battery_seen.txt`.

---

## Figure 7 (`figures/L3609_battery_ratio.png`): channels per metal pump
| group | organisms | ratio |
|---|---|---|
| **no nervous system** | 4 sponges, choanoflagellate *Monosiga*, placozoan *Trichoplax* | **0.05–1.60** |
| **nervous system** | sea squirt, brachiopod, fly, sea urchin, annelid, acoel, chicken, acorn worm, sea anemone, comb jelly, lancelet | **2.00–14.25** |

- **The two groups do not overlap.** Every organism with a nervous system has at least 2 channels per pump; every organism without one has at most 1.6.
- **The highest ratios** belong to the lancelet (14.3), the comb jelly (13.3, its Shaker expansion) and the sea anemone (11.3).
- **This is the battery picture in one line:** the **chargers** (Na⁺/K⁺, Ca²⁺, Cu pumps) are present everywhere in similar numbers, while the **dischargers** (channels) expand where there are nerves.
- **Caveats:**
  - the cut (about 1.8) was read off these 17 organisms;
  - proteome completeness varies (sponge UniProt sets differ greatly in quality);
  - the sea squirt sits just above the line (2.00).

## Pre-registered blind test (`PREREGISTERED_L3609_battery.txt`)
**Five organisms not yet used, with the cut fixed at 1.8:**

| organism | nervous system? | prediction |
|---|---|---|
| *Salpingoeca rosetta* (choanoflagellate) | no | **R1:** below 1.8 |
| *Capsaspora owczarzaki* (single-celled relative of animals) | no | **R2:** below 1.8 |
| *Aplysia californica* (sea hare, a classic memory-research animal) | yes | **R3:** above 1.8 |
| *Hydra vulgaris* (hydra) | yes | **R4:** above 1.8 |
| *Hypsibius exemplaris* (tardigrade) | yes | **R5:** above 1.8 |

## Action for Gary: one file
https://rest.uniprot.org/uniprotkb/stream?format=tsv&compressed=true&fields=accession,organism_name,protein_name,sequence&query=organism_id%3A946362%20OR%20organism_id%3A595528%20OR%20organism_id%3A6500%20OR%20organism_id%3A6087%20OR%20organism_id%3A2072580

**If it errors:** search `organism_id:946362 OR organism_id:595528 OR organism_id:6500 OR organism_id:6087 OR organism_id:2072580` on uniprot.org and download it as TSV.

## Record
No predictions graded. **432 of 590 passed, plus 3 split.** R1–R5 are waiting.

## Summary
- **Across 17 organisms, the number of channels per metal pump cleanly separates animals with nerves (2–14) from those without (0.05–1.6).**
- **The energy-storing pumps are everywhere; the fast-release channels multiply with nerves.**
- **The cut is now frozen and will be tested blind** on two single-celled relatives of animals, a sea hare, a hydra and a tardigrade.

## Potential leads for future research
- **[R1–R5]** Grade when the file arrives.
- **[Manuscript 2]** Figure 7 and the battery ratio as a short results section.
- **[Memory link]** *Aplysia* is the classic animal for the cellular basis of memory: report its excitability kit alongside the ratio.
