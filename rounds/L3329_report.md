# DCF L3329: Note H v0.7 gains its mechanism section and Figure 2; tier 4 is marked by heterodisulfide reductase and electron-bifurcating flavoproteins
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 12 November 2026

**Lead:** [Note H §5 mechanism], from L3325. Development on graded genomes. Waiting for `blind_23.zip`.

---

## 1. Figure 2: what the iron ladder counts
`figures/L3329_enzyme_families.png`: 3-3-4 ladders in proteins over 200 aa, per genome, stacked by enzyme family.

| tier | per genome | hydrogenases | PFOR | Hdr + bifurcating flavoproteins | Rnf / complex I | other |
|---|---|---|---|---|---|---|
| 1 lactic | 1 | 0 | 0 | 0 | 0 | 1 |
| 2 O₂ | 12 | 3 | 0 | 0 | 2 | 8 |
| 3 H₂ fermenters | 38 | 8 | 3 | 3 | 7 | 17 |
| 4 Fd-based | 84 | 13 | 0.5 | **21** | 2 | 47 |

**Reading.**
- **Each tier step adds a recognisable set of ferredoxin-coupled energy enzymes:**
  - hydrogenases and Rnf pumps in H₂ fermenters;
  - PFOR, the pyruvate:ferredoxin enzyme, almost only in tier 3;
  - **heterodisulfide reductase and the electron-bifurcating flavoproteins (ETF, FAD oxidoreductases), which jump 7-fold into tier 4.** These are the hallmark of methanogens, sulfate reducers and acetogens.
- The keyword grouping was refined after L3325: it now catches the misspelled "ferrodoxin" annotations and groups ETF/FAD oxidoreductases with heterodisulfide reductase.

## 2. Note H v0.7
`notes/Note_FeS_ferredoxin_signature_draft_v0.7.md`. New §4i "Mechanism" with the table and Figure 2.

**The note now has every part:**
- the result: blind tiers, lineage pairs, photosynthesis;
- the contrast: iron vs zinc (Figure 1);
- the mechanism: enzyme families (Figure 2);
- the prior art and what is new;
- an honest record of every failure.

## Record
No predictions graded. **309 of 442 passed, plus 3 split.**

## Summary
- **The iron note now explains why its scale works.** The ladder counts the enzymes that move energy through ferredoxin, and each tier adds its own set: hydrogenases and PFOR in hydrogen fermenters; heterodisulfide reductase and electron-bifurcating flavoproteins, 7-fold more, in methanogens, sulfate reducers and acetogens.
- **A clean figure** (Figure 2) shows this. Note H v0.7 has all its main parts and is ready for a methods draft once blind_23 is graded.

## Potential leads for future research
- **[blind_23]** Grade C1–C3 when the zip arrives.
- **[Bifurcation marker]** Pre-register: Hdr + bifurcating-flavoprotein ladders separate tier 4 from tier 3 better than the whole ladder (development 7× vs 2.2×). This needs a label-free definition first, since annotation can't be used blind; e.g. the ladder inside proteins that also carry an FAD-binding G-x-G-x-x-G motif.
- **[Methods draft]** Write the Note H methods section (gene finder v2.32, motif definitions, pre-registration ledger, seen lists, grading rules) as the first piece of a submission draft.
