# DCF L3501: Before nerves. 7 of 7 pass. One letter in one pore loop, E → K, marks the step from the early animal channel to the nerve sodium channel
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 14 November 2026

**Data:** `stream_24.gz` (18.2 MB): four UniProt reference proteomes, 67,936 proteins in all.

| organism | what it is | proteins |
|---|---|---|
| *Monosiga brevicollis* | choanoflagellate, single-celled | 9,150 |
| *Amphimedon queenslandica* | sponge, no nervous system | 22,831 |
| *Trichoplax adhaerens* | placozoan, no neurons | 11,520 |
| *Nematostella vectensis* | sea anemone, nerve net | 24,435 |

**Procedure:**
1. Four frozen hashes matched.
2. The v7 tool read only Entry and Sequence; its output was committed and pushed before organisms were attached.
3. Grading: `rounds/L3501_grade.py` → `rounds/L3501_grade_output.txt`.

---

## Results (PREREGISTERED_L3493_before_nerves)
| # | prediction | result |
|---|---|---|
| S1–S4 | **no sodium calls** in choanoflagellate, sponge, placozoan, sea anemone | **0, 0, 0, 0: all PASS** |
| S5 | sea anemone has calcium channels | **2: PASS** |
| S6 | *Trichoplax* has calcium channels | **2: PASS** |
| S7 | sea anemone has ≥ 3 potassium channels | **46: PASS** |

**7 of 7 pass.**

## What the four genomes show (descriptive)
| | Na | Ca | K | HCN | K2P | iGluR | Na/K pump | Ca pump | Cu pump |
|---|---|---|---|---|---|---|---|---|---|
| choanoflagellate | 0 | 0 | 2 | 0 | 3 | 0 | 1 | 3 | 1 |
| sponge | 0 | 0 | 2 | 2 | 1 | 0 | 2 | 3 | 1 |
| placozoan | 0 | 2 | 5 | 0 | 1 | 8 | 1 | 3 | 1 |
| **sea anemone** | 0 | 2 | **46** | 2 | **18** | 9 | 2 | 3 | 1 |

### 1. The chargers came first
- **Every one of the four, including the single-celled choanoflagellate,** already has the full pump set: Na⁺/K⁺, Ca²⁺ and copper.
- **The nerve battery's charging side is older than animals.**

### 2. The dischargers exploded with the first nerves
- **Without nerves:** the sponge and choanoflagellate have about 5–7 channels.
- **The anemone's nerve net:** 70 (46 potassium, 18 leak). This is the same pattern as the vertebrate "few chargers, many dischargers" figure, but here we see the **moment it began.**

### 3. Calcium channels, including the T-type, predate neurons
- ***Trichoplax* (no neurons) has an L/N-type ring** (S-L-E-G-W, S-G-E-D-W, T-G-E-N-W).
- **It also has a T-type ring:** T-L-E-A-W, T-Q-E-D-W, S-K-D-G-W, T-G-D-N-W. That is the same EEDD pattern as human CACNA1G.
- **The anemone has both kinds too.**

### 4. The DEKA origin, one letter (`rounds/L3501_deka_origin.txt`)
- **Where the early sodium-channel homologues went:** they were not called sodium. They lack the lysine. Their domain-III loop reads **A-T-F-E-G-W**:
  - the anemone "sodium channel protein" (A7SKR1);
  - the choanoflagellate four-domain channel (A9USM1).
- **In every bilaterian sodium channel tested** (fly para, fish, bird, mammal), that same loop reads **A-T-F-K-G-W**.

| organism | domain-III loop of the 4-domain Na-type channel | ring |
|---|---|---|
| choanoflagellate (A9USM1) | A-T-F-**E**-G-W | DEEA type |
| sea anemone (A7SKR1) | A-T-F-**E**-G-W | DEEA type |
| fruit fly (para) … human (SCN2A) | A-T-F-**K**-G-W | **DEKA** |
| human/mouse Naₓ (SCN7A) | A-T-F-**N**-G-W | DENA (sensor) |

- **The reading:** the fast sodium spike of bilaterian nerves traces to a **single letter change, glutamate (E) to lysine (K),** at one fixed position of one pore loop. The rest of the loop (A-T-F-x-G-W) stayed the same for over 600 million years.
  - This matches the published picture of sodium-channel evolution: DEEA in early lineages, DEKA in bilaterians.
  - Our tool's lysine rule, frozen before these genomes were seen, drew the line in the same place.

## Record
**+7 passed. 403 of 555 passed, plus 3 split.** Nerve-chemistry blind tests: **78 of 92.**

## Summary
- **At the base of the animal tree, all seven predictions held:**
  - no nerve-type sodium channel in a choanoflagellate, a sponge, a placozoan or a sea anemone;
  - calcium channels already present before neurons;
  - a potassium-channel expansion in the first nerve net.
- **The battery's chargers (Na⁺/K⁺, Ca²⁺ and Cu pumps) are older than animals.** The dischargers multiplied when nerves appeared.
- **The step to the bilaterian nerve sodium channel is visible as one letter:** A-T-F-**E**-G-W in the early channels became A-T-F-**K**-G-W in every bilaterian sodium channel. This is a concrete link between the "language" of the sequence, evolution through time, and the energy of the nerve impulse.

## Potential leads for future research
- **[E→K figure]** Figure 4 for Manuscript 2: the domain-III loop across the tree, choanoflagellate → anemone → fly → human, with Naₓ.
- **[Manuscript 2 v0.4]** Add the before-nerves test as §3.7 and the E→K result to the abstract.
- **[Ctenophore]** Comb jellies may have evolved nerves separately. A pre-registered test: their sodium-type channels should read E (or another non-K letter), not K, at this loop.
- **[Nax blind]** Test the DENA (N) branch on unseen sensor sequences.
