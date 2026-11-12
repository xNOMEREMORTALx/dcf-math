# DCF L3317: the closest prior art for the iron ladder is found (Campbell, Bennett & Silberg 2019) and Note H is updated to v0.6; an "early start" flag is measured and rejected
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 12 November 2026

**Leads pursued:** [Lit-redox b], [ORF flag]. No new data; nothing graded.

---

## 1. [Lit-redox b] Prior art for Note H
**Found: Campbell, Bennett & Silberg 2019,** *Frontiers in Energy Research* 7:79.
- They mined **7,079 genomes** for small electron carriers (≤ 200 aa).
- **[4Fe-4S] ferredoxins dominate in anaerobes;** flavodoxins and [2Fe-2S] ferredoxins rise in relative abundance with oxygen tolerance.
- They also note that "[4Fe-4S] Fd usage is not abolished in aerobes".

**How Note H differs (now written into v0.6 §4e):**
1. **Whole-proteome motif density.** The ladder also counts the ferredoxin-like domains inside large enzymes (hydrogenases, CODH, PFOR, heterodisulfide reductase), computed label-free from raw DNA.
2. **Energy-metabolism tiers, not oxygen classes.** The ladder separates lactic fermenters (about 0.002) from H₂-making fermenters (about 0.043), both strict anaerobes, about 20-fold. It puts oxygen-making cyanobacteria and oxygen respirers together in tier 2.
3. **Blind, pre-registered tests:**
   - blind_20: 14 of 16, ρ = 0.96;
   - photosynthesis 2 of 2;
   - rubredoxin RB1/RB2;
   - six lineage pairs.

**Agreement:** our photosynthesis result fits theirs. Oxygen-makers rely on [2Fe-2S] plant-type ferredoxin and read low on a 4Fe-4S ladder.

**Still to read:** the 2021 survey "Diversification of Ferredoxins across Living Organisms" (*Curr. Issues Mol. Biol.* 43(3):98). Its page needed an approval that timed out this round.

**Note H v0.6** (`notes/Note_FeS_ferredoxin_signature_draft_v0.6.md`) also adds the photosynthesis section (§4h) and the rubredoxin/low-oxygen section (§4g).

## 2. [ORF flag] Flagging possibly early starts [development, on L3313 data]
**Flag tested:** another in-frame ATG within N codons of the first one.

| N | early starts flagged (of 111) | correct proteins flagged (of 4,972) |
|---|---|---|
| 5 | 16% | 8.6% |
| 10 | 28% | 15.2% |
| 20 | 50% | 27.7% |
| 40 | 77% | 46.3% |

**Rejected.** At N = 10, about 96% of flags would be false alarms. A second in-frame ATG near the start is common in correct proteins too.

The tools keep their single answer, with the measured accuracy stated: **exact for 97.8% of human proteins; about 2% begin a few codons early.**

## Record
No predictions graded. **309 of 442 passed, plus 3 split.**

## Summary
- **The iron-ladder note now has its key prior art:** a 2019 study of 7,079 genomes found that [4Fe-4S] ferredoxins dominate in anaerobes. Our work differs in three ways:
  - it counts the motif across the whole proteome from raw DNA;
  - it sorts genomes by type of energy metabolism (it splits lactic from hydrogen fermenters, which an oxygen classification can't);
  - its tests were pre-registered and blind.
- **Note H is at v0.6,** with the photosynthesis and rubredoxin results added.
- **A warning flag for early start codons doesn't work.** It would mostly raise false alarms, so it was dropped.

## Potential leads for future research
- **[Lit-redox c]** Read the 2021 CIMB ferredoxin survey (open the link yourself in a browser, or allow the page when asked); then Note H is ready for a methods draft.
- **[Campbell comparison]** A direct test: does the ladder separate lactic from H₂ fermenters better than a count of small [4Fe-4S] ferredoxin genes alone (≤ 200 aa, Campbell's definition)? Develop on seen genomes, then pre-register on fresh ones. This would show what the whole-proteome view adds.
- **[Exon conservation]**, **[Neuro b]**, **[hedgehog2]**: carried.
