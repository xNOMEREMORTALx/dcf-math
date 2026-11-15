# DCF L3613: The battery-ratio test, blind on five new organisms. 4 of 5 pass; the tardigrade, which has nerves, falls below the line (1.54)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 15 November 2026

**Data:** `28.gz` (31 MB), 101,463 UniProt proteins:

| organism | proteins |
|---|---|
| *Hydra vulgaris* | 35,504 |
| *Aplysia californica* | 23,632 |
| *Hypsibius exemplaris* | 20,833 |
| *Salpingoeca rosetta* | 11,700 |
| *Capsaspora owczarzaki* | 9,794 |

**Procedure:** three frozen hashes matched; frozen script `rounds/dcf_battery_L3609.py` → `rounds/L3613_grade_output.txt`.

---

## Results (PREREGISTERED_L3609_battery, cut 1.8)
| # | organism | nerves | channels | pumps | ratio | result |
|---|---|---|---|---|---|---|
| R1 | *Salpingoeca* (choanoflagellate) | no | 8 | 10 | **0.80** | **PASS** |
| R2 | *Capsaspora* (filasterean) | no | 3 | 8 | **0.38** | **PASS** |
| R3 | *Aplysia* (sea hare) | yes | 41 | 9 | **4.56** | **PASS** |
| R4 | *Hydra* | yes | 112 | 23 | **4.87** | **PASS** |
| R5 | *Hypsibius* (tardigrade) | yes | 20 | 13 | **1.54** | **FAIL** |

**4 of 5 pass.**

## Reading (descriptive kit, `rounds/L3613_kits.txt`)
- **Both single-celled relatives of animals sit well below the line** (0.38, 0.80). Both already carry metal pumps (7–8 calcium pumps each) and a few potassium channels.
- **The sea hare and hydra sit well above it.**
  - **The sea hare,** the classic animal for studying memory in single cells, carries 2 DEKA sodium channels (as a protostome should), 27 potassium channels, 8 leak channels, **33 glutamate receptors** and 2 iron hydroxylases.
  - **Hydra** carries no DEKA sodium channel (as a cnidarian should), but 67 potassium channels, 18 HCN pacemakers and 8 T-type calcium channels.
- **The tardigrade fails.**
  - Its ratio (1.54) is below the line, though it has a nervous system.
  - It also shows **no DEKA sodium channel** in its UniProt proteome, unusual for a protostome, and only 14 potassium channels.
  - **The likely reason:** tardigrades are known for compact genomes that have lost many genes, and their nervous system is small. **A nervous system does not always come with a large channel expansion.** The rule is a strong tendency, not a law.
  - Proteome completeness may also play a part. The failure stands.

## Record
**+4 passed, 1 failed. 436 of 595 passed, plus 3 split.** Nerve-chemistry audit: **103 of 122.**

## Summary
- **The battery ratio passed 4 of 5 blind predictions:**
  - two single-celled relatives of animals below the line;
  - the sea hare and hydra above it.
- **The tardigrade, which has nerves, fell below it (1.54).** It also lacks a fast sodium channel in its protein set, which fits its well-known gene losses.
- **Channel expansion with nerves is a strong pattern but not a law.**

## Potential leads for future research
- **[Tardigrade sodium channel]** Is the missing DEKA channel a gene loss or a gap in the proteome? Check a second tardigrade (*Ramazzottius varieornatus*), pre-registered.
- **[Sea hare memory kit]** Its 33 glutamate receptors: how many are NMDA-type by alignment to mouse GRIN genes? (The NMDA motif is unreliable outside vertebrates, L3465.)
- **[Manuscript 2]** Add §3.12 (battery ratio, Figure 7, 4/5 blind).
