# DCF L3325: which enzymes carry the iron ladder? Hydrogenases, heterodisulfide reductase, PFOR and the flavin electron-bifurcation machinery of anaerobes
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 12 November 2026

**Lead:** [Enzyme map], from L3321. Development on the 16 graded blind_20 genomes: each predicted protein over 200 aa carrying a 3-3-4 ladder was matched to its annotated product by stop codon. Annotation is used here only because these genomes are already graded. Waiting for `blind_23.zip`.

---

## 1. Ladders in large proteins, by tier
| tier | ladders in large proteins | leading enzyme families |
|---|---|---|
| 1 lactic | **5** | two ferredoxin-domain proteins; nothing else |
| 2 O₂ | 49 | hydrogenases 22%, Rnf complex 16%, ferredoxin-domain 18% |
| 3 H₂ fermenters | 153 | **hydrogenases 20%**, NADH/complex I-type 10%, **PFOR / 2-oxoacid:ferredoxin oxidoreductases 8%**, Rnf 8% |
| 4 Fd-based | **334** | ferredoxin-domain proteins 37%, hydrogenases 16%, **heterodisulfide reductase 11%**, sulfite/APS reductase |

**The "other" ladders in tiers 3–4 are mostly real redox machinery:**
- **FAD-dependent oxidoreductases** (48) and **electron-transfer flavoprotein α** (10): the partners in **flavin-based electron bifurcation**, the anaerobes' way of making low-potential ferredoxin;
- **EFR1-family ferredoxins** (10; missed by the keyword list because the annotation spells it "ferrodoxin");
- glycine-radical-enzyme activases.

Only 10 ladders had no annotated match.

## 2. Reading
- **The ladder count climbs about 70-fold from tier 1 to tier 4** (5 → 334 in large proteins). The enzymes behind the climb are the textbook ferredoxin users of anaerobic energy metabolism:
  - **hydrogenases** make or split H₂ with ferredoxin electrons (tiers 3–4);
  - **PFOR** turns pyruvate into acetyl-CoA and reduces ferredoxin (tier 3 fermenters);
  - **heterodisulfide reductase** and the **ETF/FAD electron-bifurcating complexes** couple ferredoxin to energy conservation in methanogens, sulfate reducers and acetogens (tier 4);
  - the **Rnf complex** pumps ions using ferredoxin.
- **Lactic fermenters have almost none,** because their energy path (glycolysis to lactate) never touches ferredoxin.
- **This gives the tier scale a mechanistic explanation:** the ladder density is roughly a count of how many ferredoxin-coupled energy enzymes a genome carries. It belongs in Note H as the "why it works" section (and Figure 2).

## Record
No predictions graded. **309 of 442 passed, plus 3 split.**

## Summary
- **The iron ladder counts the enzymes anaerobes use to move energy through ferredoxin:**
  - hydrogenases;
  - the pyruvate:ferredoxin enzyme (PFOR) of fermenters;
  - heterodisulfide reductase and the electron-bifurcating flavoproteins of methanogens, sulfate reducers and acetogens.
- **Lactic fermenters have almost none (5 ladders in four genomes), and ferredoxin-based microbes have hundreds (334).** That is why the scale works.
- **Development only.** It explains the result rather than testing it; blind_23 is the next test.

## Potential leads for future research
- **[blind_23]** Grade C1–C3 when the zip arrives (Gary downloading).
- **[Note H §5 mechanism]** Add this enzyme map as the "why" section, with a stacked bar figure by tier.
- **[Bifurcation marker]** Test whether ETF-α/FAD-oxidoreductase ladders alone mark tier 4 (methanogens, sulfate reducers, acetogens) better than hydrogenases; develop on seen genomes, then pre-register.
