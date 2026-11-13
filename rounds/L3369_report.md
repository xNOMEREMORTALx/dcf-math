# DCF L3369: Ladder-P (C-x₂-C-x₂-C-x₃-C-P) removes eukaryote look-alikes and cleans the protist gap, while leaving bacteria unchanged; a counting inconsistency between two tools found and documented
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 12 November 2026

**Lead:** [Ladder-P]. Development only, on graded data: 37 blind prokaryote genomes, 14 protists, 5,390 human proteins. Script: `rounds/L3369_ladderP_dev.py`.

---

## 1. Plain ladder vs Ladder-P
**Bacteria and archaea (37 graded blind genomes, overlapping counts)**
| motif | ρ with tier | tier medians | tier 2 max vs tier 3 min |
|---|---|---|---|
| plain C-x₂-C-x₂-C-x₃-C | 0.962 | 0 / 0.0139 / 0.0441 / 0.1338 | 0.0226 vs 0.0352 (clean) |
| Ladder-P …C-**P** | 0.964 | 0 / 0.0118 / 0.0317 / 0.1006 | 0.0185 vs 0.0209 (narrower) |

**Protists (overlapping counts)**
| group | plain | Ladder-P |
|---|---|---|
| anaerobes (6) | 0.0036 – 0.0186 | 0.0020 – 0.0114 |
| aerobes (7) | 0.0009 – **0.0039** | 0.0004 – **0.0014** |
| gap | **overlaps** (*Trypanosoma* 0.0039 > *Cryptosporidium* 0.0036) | **clean** (0.0020 > 0.0014) |
| *Naegleria* | 0.0017 | 0.0003 |

**Human (5,390 proteins):** plain 12 hits (integrins, metallothionein, zinc fingers…); **Ladder-P 0**.

**Reading.**
- **Ladder-P is the better eukaryote motif.** The trailing proline is part of the classic bacterial-type ferredoxin fold, and cysteine-rich structural look-alikes lack it.
- **For prokaryotes it adds nothing.** The plain ladder keeps a cleaner tier-2/3 gap, so it stays the prokaryote motif.
- **Proposal:** Ladder-P for eukaryotes, to be tested blind on fresh protists.

## 2. A counting inconsistency, found and documented
- **The difference:** `dcf_redox.py` and all prokaryote results count ladders overlapping. The motif scanner's `fd_ladder` preset, which graded both protist tests, counts **non-overlapping** matches, because its pattern lacks the look-ahead.
- **Effect:** the protist values differ slightly by method (*Trypanosoma* 0.0030 graded vs 0.0039 overlapping; *Giardia* 0.0089 vs 0.0095).
- **The grades stand,** because the eukaryote cut was set and tested with the same scanner. But the manuscript's Methods said "counted overlapping" for everything. **Manuscript v0.6 now states which counting each section used** and notes that with overlapping counts *Trypanosoma* would edge above *Cryptosporidium*.
- **Lesson:** keep one counting convention across tools. A fix (an overlapping `fd_ladder` preset) must be a new, separately hashed version, so as not to alter frozen results.

## Record
No predictions graded. **316 of 451 passed, plus 3 split.**

## Summary
- **A sharper motif for eukaryotes.** Requiring the proline that follows the last cysteine in real bacterial-type ferredoxins removes every human look-alike hit (12 → 0). It also separates oxygen-free from oxygen-breathing protists with a clean gap, while making no difference for bacteria. It's development, so it needs a fresh blind test.
- **An honest catch.** The motif scanner counted ladders slightly differently (non-overlapping) from the main tool. The protist grades are unaffected because the same scanner set and tested the cut, but the manuscript now says exactly which counting each result used.

## Potential leads for future research
- **[Ladder-P blind]** Pre-register Ladder-P with a eukaryote cut (about 0.0017, between 0.0014 and 0.0020) on fresh protists: anaerobic *Monocercomonoides*, *Mastigamoeba*, *Entamoeba invadens*, *Giardia muris*; aerobic *Toxoplasma*, *Plasmodium*, *Paramecium*, *Bigelowiella*.
- **[Scanner v2]** Add overlapping `fd_ladder_ov` and `ladder_p` presets to the motif scanner and phone, as new hashed versions.
- **[Venue]**, **[Metagenome tier]**: carried.
