# DCF L3713: The cohesin positive control failed (0 of 3), measuring the finders' sensitivity at ~79% per gene; CTCF v2 rescues six bilaterians; the repdigit lattice; a channel-gene / loop test is frozen
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 16 November 2026

**Leads:** [Repdigit lattice], [Cohesin], [CTCF finder v2], [Biology, not digits].

---

## 1. Repdigit lattice (pure arithmetic; `rounds/L3713_repdigit_lattice.txt`)
**Background:** every triple repdigit is aaa = a · 111 = a · 3 · 37.

| repdigits | least common multiple |
|---|---|
| 444, 666, 888 (and 222) | **2,664 = 72 · 37** |
| 333, 666, 999 | 1,998 = 54 · 37 |
| all nine | 279,720 = 7,560 · 37 |

**Facts:**
- **5,328 (L3709) = 2 · 2,664.**
- **DCF key numbers that are multiples of 37:** 37 and **2701**. None is a multiple of 111.
- **2701 = 2,664 + 37 = 73 · 37 = 72 · 37 + 37.** It sits one step of 37 above the 444/666/888 lattice point. This ties the DCF numbers 72, 73 and 2701 (= T₇₃) together through 37.

**Status:** verified arithmetic.

## 2. Cohesin positive control (`PREREGISTERED_L3713_cohesin.txt`)
**Why:** cohesin (SMC1 + SMC3) is the loop-extruding motor that works with CTCF, and it exists in every eukaryote. It was meant to show the 3D folding machinery present where CTCF is absent.

**Finder:** 900–1,600 aa, with the SMC signature and a Walker A motif, nearest a mouse SMC (score ≥ 1,000).

| # | prediction | result |
|---|---|---|
| H1 | SMC1 in all 48 organisms | **FAIL:** 38 of 48 |
| H2 | SMC3 in all 48 | **FAIL:** 38 of 48 |
| H3 | both, in all 26 CTCF-absent organisms | **FAIL:** 16 of 26 |

**0 of 3 passed. The positive control failed, and the cause is my finder, not the biology.**

**What this teaches:**
- **This style of absence call has a sensitivity of about 79% per gene** (38 of 48) on UniProt sets. About **one real gene in five is reported as absent.**
- **Likely causes:**
  - fragmentary entries;
  - divergent motifs;
  - a strict length gate.

**Consequences for earlier absence claims:**
- **CTCF in non-bilaterians (L3701):** 14 of 14 absent. If CTCF were present and missed at 21% each time, all 14 would be missed with probability about 0.21¹⁴ ≈ 3 × 10⁻¹⁰. **The non-bilaterian absence stands.**
- **Single-organism absences anywhere** (CTCF in one flatworm, NR1 in one species, NAV in one fluke) **must be read as "not detected", not "lost",** unless backed by several relatives or an independent search.
  - The fluke NAV loss rests on 5 of 5 flukes, so it is stronger than any single case.

## 3. CTCF finder v2, development (`rounds/L3713_ctcf_v2_dev.txt`)
**The change:** the zinc-finger gate is lowered from ≥ 9 to ≥ 6. The reciprocal check against 365 mouse zinc-finger proteins is unchanged.

| organism | v1 | v2 |
|---|---|---|
| Ciona | absent | **present** (869) |
| *Hypsibius* (tardigrade) | absent | **present** (671) |
| *Ramazzottius* (tardigrade) | absent | **present** (690) |
| leech | absent | **present** (629) |
| *B. calyciflorus* | absent | **present** (543, nearest CTCFL) |
| *B. plicatilis* | absent | **present** (567) |
| all 14 non-bilaterians, plus 3 sponges not scanned in v1 | absent | **absent** |

- **v2 rescues six bilaterians, including the named Ciona and tardigrade CTCFs,** and adds no non-bilaterian call.
- **With v2, CTCF is found in 20 of 29 bilaterians.** The remaining absences are **all nine flatworms**, which is consistent across the whole flatworm group.
- **Disclosures:**
  - the rescued scores are low (543–690);
  - this is development.
- **v2 needs a blind test on new proteomes before it replaces v1.**

## 4. Frozen: nerve-metal genes at loop anchors (`PREREGISTERED_L3713_channel_loops.txt`)
**The question:** in human stem cells and fibroblasts, do K, Na and Ca channels, HCN, NALCN, NMDA receptors and the Na/K and Ca pumps sit at loop anchors differently from other genes?

**Predictions:**
- **C1–C2:** not enriched at CTCF loops (CTCF loops are structural).
- **C3–C4:** depleted at active-promoter (H3K4me3) loops, because these neural genes are silent in those cells.

**File needed:** the GENCODE human basic gene annotation (about 30–40 MB):
- https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_49/gencode.v49.basic.annotation.gtf.gz
- If that release number is not found, open https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/latest_release/ and take the file ending `basic.annotation.gtf.gz`.

## Record
**+0 passed, 3 failed. 498 of 680 passed, plus 3 split.** Audit **165 of 207.**

## Summary
- **The cohesin control failed (0 of 3):** my finder missed SMC1 or SMC3 in about one organism in five. That measures the sensitivity of these absence calls at about 79% per gene.
- **It changes how absences should be read:**
  - the CTCF absence across all 14 non-bilaterians still stands;
  - single-species absences are "not detected", not "lost".
- **CTCF finder v2 rescues six bilaterians,** including the named Ciona and tardigrade proteins, without any non-bilaterian call. Every flatworm still lacks it.
- **The repdigit lattice ties 2701 (= 73 · 37) one step above 2,664 (= 72 · 37 = lcm of 444, 666, 888).**
- **A test of nerve-metal genes at genome loops is frozen** and waits for the GENCODE file.

## Potential leads for future research
- **[Finder sensitivity]** Build an SMC finder v2 (relaxed length, motif or alignment only) and measure its sensitivity on the same 48 organisms. Apply the lesson to every absence finder (NR1, NAV, CTCF), reporting sensitivity alongside each absence claim.
- **[CTCF v2 blind]** Pre-register v2 on the next new proteomes.
- **[Channel genes at loops]** Grade C1–C4 when GENCODE arrives.
- **[Flatworm CTCF]** All nine flatworms lack CTCF even with v2, with flatworm SMC1/SMC3 found in most. If confirmed, flatworms fold their genomes without CTCF, like nematodes.
