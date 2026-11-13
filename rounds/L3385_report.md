# DCF L3385: lactic bacteria keep their DNA-repair enzymes but have stripped out the iron-binding cysteines (endonuclease III with 0–1 cysteines in *Lactobacillus*); CRISPR memory found label-free but does not follow the iron switch; information-iron note drafted
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 12 November 2026

**Leads pursued:** [Iron-free repair], [CRISPR iron], [Information-iron note]. All development, on graded genomes; nothing graded.

---

## 1. [Iron-free repair] The enzymes stay, the iron goes
**Repair enzymes by annotation:** 13 lactic vs 77 other graded genomes.

| enzyme | lactic | others |
|---|---|---|
| endonuclease III | 9 of 13 | 63 of 77 |
| MutY | 8 of 13 | 38 of 77 |
| Fpg/MutM, UDG, Exo III, UvrABC, MutS/L, RecA | 13 of 13 each | 41–73 of 77 |

**The cluster cysteines:**
| protein | with the C-x₆-C-x₂-C-x₅-C loop | median cysteines |
|---|---|---|
| lactic endonuclease III | **1 of 9** | 4 (*Lactobacillus*: **0–1**) |
| other endonuclease III | 57 of 64 | 6 |
| lactic MutY | **0 of 8** | **0** |
| other MutY | 32 of 38 | 6 |

- **Reading.** In *L. rhamnosus*, *gasseri*, *johnsonii* and *helveticus*, endonuclease III has **no cluster cysteines at all**. Streptococcal endonuclease III keeps 2 of the 4.
- **Literature:**
  - **iron-free MutY in Lactobacillales is known** (Trasviña-Arenas 2016; the 2025 MutYX paper);
  - **iron-free endonuclease III in *Lactobacillus*** was not found in the sources checked; a wider search is needed.

## 2. [CRISPR] Immune memory, label-free [development]
- **Finder:** runs of ≥ 3 copies of a 23-letter repeat, 50–120 bp apart, with every spacer different.
- **Validation (45 genomes):** 136 arrays overlapping NCBI's CRISPR annotations, 3 annotated arrays missed, 99 unannotated hits. Precision is uncertain; some of these may be real unannotated arrays.

| tier | genomes with an array | median repeat units |
|---|---|---|
| 1 lactic | **13 of 13** | 15 |
| 2 O₂ | 8 of 13 | 6 |
| 3 H₂ ferm | 7 of 7 | 60 |
| 4 Fd-based | 12 of 12 | 57.5 |

- **Reading:** CRISPR memory **does not follow the iron switch.** The iron-free lactic bacteria all carry arrays.
- **It is higher in tiers 3–4,** but only loosely (ρ = 0.41), and several tier 3–4 genomes are thermophiles. CRISPR is known to be commoner in thermophiles, so energy and temperature are confounded here.
- No claim.

## 3. Information-iron note v0.1
`notes/Note_information_iron_v0.1.md`: question, method, development, the blind 3 of 3, the ligand-loss finding, prior art, interpretation and leads.

## Record
No predictions graded. **320 of 456 passed, plus 3 split.**

## Summary
- **Lactic bacteria didn't throw away their DNA-repair enzymes; they removed the iron from them.** *Lactobacillus* endonuclease III has no cluster cysteines at all, and lactic MutY has none either. The MutY loss was already known; the endonuclease III loss wasn't found in the sources checked.
- **CRISPR immune memory can be found without labels,** but it doesn't follow the iron switch (lactic bacteria have it). Its link to energy metabolism is confounded by temperature.
- **The information-iron result is written up as a companion note.**

## Potential leads for future research
- **[Ligand-loss blind]** Pre-register cysteine loss in endonuclease III and MutY on fresh Lactobacillales vs iron users. This needs labels to find the enzymes, so use a label-free route first (e.g. the HhH-GPD motif plus the absence of the FCL loop).
- **[Lit-infoiron]** Broader literature search on endonuclease III cluster loss.
- **[CRISPR-temperature]** Separate temperature from energy (mesophilic vs thermophilic genomes within one tier).
- **[Polymerase iron]**: carried.
