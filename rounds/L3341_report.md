# DCF L3341: number audit passes (every headline number re-computed from the committed tool-number files), Figure 3 made, manuscript v0.2
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 12 November 2026

**Leads:** [Number audit], [Figure 3]. Script: `figures/L3341_all_blind.py`; output: `rounds/L3341_audit.txt`.

---

## 1. Number audit
The script reads **only** the tool-number files committed before each grading, plus the tier labels frozen in the pre-registrations. It recomputes:

| claim in the draft | re-computed | match |
|---|---|---|
| blind_20 14 of 16, ρ 0.958 | 14 of 16, ρ 0.958 | ✓ |
| blind_21 controls 4 of 4 | 4 of 4 | ✓ |
| blind_22 phototrophs 5 of 5 | 5 of 5 | ✓ |
| blind_23 12 of 12, ρ 0.978 | 12 of 12, ρ 0.978 | ✓ |
| total 35 of 37; misses *C. botulinum* 0.0601, *Sulfurihydrogenibium* 0.0474 | identical | ✓ |
| large-protein ladders 5.3× vs small ferredoxins 0.99× (O₂ → H₂) | 5.32× vs 0.99× | ✓ |
| **new:** ρ over all 37 blind genomes | **0.962** | added |

**Verdict:** every headline number in the manuscript is reproduced from the raw committed files. The phylum count (8) was corrected in L3337.

## 2. Figure 3
`figures/L3341_all_blind.png`: all 37 blind genomes on the ladder axis, by pre-assigned tier, coloured and shaped by blind set, with the three frozen cuts and the two misses labelled.

- The four tiers form separate bands.
- Both misses sit near a boundary: *C. botulinum* is just over 0.060, and *Sulfurihydrogenibium*, a microaerophile, sits among the H₂ fermenters.

## 3. Manuscript v0.2
`notes/Manuscript_FeS_ladder_draft_v0.2.md`:
- ρ = 0.962 added to the abstract and the results table;
- Figure 3 added;
- the audit noted.

## Record
No predictions graded. **312 of 445 passed, plus 3 split.**

## Summary
- **Every key number in the draft paper checks out,** recomputed straight from the files committed before each test.
- **Figure 3 shows all 37 blind genomes at once:** four clean bands, two near-boundary misses. Across all of them the rank correlation is 0.962.
- **Manuscript v0.2 is complete with three figures.**

## Potential leads for future research
- **[Venue]** Choose a journal and fit the format (e.g. *Microbial Genomics* or *ISME Communications* short report; *PeerJ* for the full method and failure table).
- **[Eukaryote check]** Anaerobic vs aerobic protists from RefSeq protein FASTA (the motif scan already accepts proteins).
- **[Independent review]** A fresh read of the manuscript by someone who has not seen the work (a colleague, or a separate AI review with no project context) for clarity and overclaims.
