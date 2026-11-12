# DCF L3349: two development results. A label-free electron-bifurcation marker fails (worse than the plain ladder); the human proteome reads near zero, and its few hits are cysteine-rich false positives, a warning for the eukaryote test
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 12 November 2026

**Leads:** [Bifurcation marker], [Human ladder] (new). Development only, on already-graded data.

The Ensembl page request timed out again. **Gary: please paste `https://ftp.ensemblgenomes.ebi.ac.uk/pub/protists/current/fasta/` into a message**; the tool needs the URL to come from you.

---

## 1. [Bifurcation marker] Fails in development
**Marker tested:** proteins carrying both a 3-3-4 ladder and a Rossmann FAD/NAD-binding G-x-G-x-x-G, the signature combination of electron-bifurcating flavoproteins. **Data:** 32 graded genomes with tier labels.

| measure | ρ with tier | tier-4 / tier-3 medians | Mann–Whitney p (t4 > t3) |
|---|---|---|---|
| **whole ladder** | **0.961** | **3.08×** | **0.0006** |
| ladder + G-x-G-x-x-G proteins | 0.808 | 1.66× | 0.036 |
| ≥ 2 ladders + G-x-G-x-x-G | 0.818 | 1.70× | 0.036 |

**Dropped.** G-x-G-x-x-G occurs in very many enzymes, so the combination adds noise rather than specificity. The plain ladder remains the best label-free marker.

## 2. [Human ladder] (new) The human proteome on the scale
**Data:** 5,390 human proteins (one isoform per name) from the NCBI human.1 and human.2 protein files.
- **Density 0.0042 per 1,000 aa**, below the bacterial lactic cut (0.0045). That is as low as a lactic fermenter, even though humans respire oxygen.
- **All 11 hits look like false positives:** integrins β1/5/6/7/8 (cysteine-rich extracellular domains), metallothionein, zinc-finger proteins, a DnaJ protein, a calcium-binding protein and a choline transporter.
- The genuine human [4Fe-4S] ferredoxin-type proteins (complex I NDUFS8, ABCE1, DPYD and others) are not in this half of the files.

**Reading.**
- In large eukaryotic proteomes the **real ferredoxin ladders are few and diluted,** while cysteine-rich structural proteins contribute **false ladders of the same order**.
- So the bacterial scale may not transfer to eukaryotes. This bears on prediction EU3 of the frozen eukaryote test (L3345), and it is written down **before** any protist file arrives. The test stands as frozen.
- **Possible fix (for a later, separately pre-registered version):** require the ladder's last cysteine to be followed by proline (C-x₂-C-x₂-C-x₃-C-**P**), the classic bacterial ferredoxin signature. Integrins and metallothioneins rarely have it.

## Record
No predictions graded. **312 of 445 passed, plus 3 split.**

## Summary
- **Two honest negatives.** A combined bifurcation marker does worse than the simple iron ladder, so it's dropped. And in human proteins the ladder is so rare that cysteine-rich look-alikes (integrins, metallothionein) are as common as the real thing.
- **This warns that the bacterial tier scale may not carry over to eukaryotes as it stands.** It's recorded before the protist test data arrive. A stricter motif (the classic C-P ending) is the obvious refinement.

## Potential leads for future research
- **[Eukaryote check]** Grade the frozen EU1–EU3 when the protist files arrive (paste the Ensembl URL).
- **[Ladder-P]** Test the stricter C-x₂-C-x₂-C-x₃-C-P motif: on bacteria it must keep the tier separation (development on graded genomes); on human proteins it should drop the integrin and metallothionein false hits.
- **[Metagenome tier]** (new, novel) Apply the ladder to **whole microbial communities** (gut, ocean, hot spring, sediment metagenome assemblies) to read the community's dominant energy metabolism from raw DNA. Pre-register predictions, e.g. sediment and gut > ocean surface.
