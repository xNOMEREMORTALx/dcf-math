# DCF L3573: Figure 5 (the sodium-channel tree) and phone 6.13 with a protein aligner (menu 35)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 14 November 2026

**Leads:** [Figure 5], [Phone aligner]. **No predictions graded.**

---

## Figure 5 (`figures/L3573_navtree.png`)
**What it shows:** the neighbour-joining tree from L3569, drawn with names and the ring letter at each tip (blue K, orange E).

**Reading:**
- **The six K-type NAV1 genes form one block:** sea squirt, lancelet and human, then fly, brachiopod and annelid. That is the chordate and protostome sides of the bilaterian tree.
- **Every E-type channel lies outside it:** sea urchin, acorn worm, acoel, annelid NAV2, comb jellies, placozoan, sea anemone and lancelet NAV2.
- **Caveats:**
  - the tree is unrooted, uses topology only, and is drawn from an arbitrary root;
  - the choanoflagellate's position next to the NAV1 block is not resolved;
  - lancelet NAV2 pairs with the sea anemone, which a full analysis may not reproduce.

**Manuscript 2 v0.11** lists it as Figure 5.

## Phone bundle 6.13 (`phone/dcf_phone_bundle_6.13.zip`)
- **New menu 35, "align two protein sequences":** pick a FASTA with two proteins (or paste them) to get percent identity and score. It uses BLOSUM62, gap 8; validated: mouse Scn2a vs Scn8a 78.3%.
- **It needs numpy.** In Pydroid 3: **Pip → numpy**. Without numpy, the menu explains this and the self-test row is skipped.
- **Self-test 266/266.**
- **Install:** copy all **nine** `.py` files into one folder and open `dcf_phone_6.13.py`.

## Record
No predictions graded. **422 of 578 passed, plus 3 split.**

## Summary
- **Figure 5 shows the result of the last two rounds at a glance:** the K-type fast sodium channels (NAV1) of chordates and protostomes group together, apart from every E-type channel.
- **The phone can now align any two proteins** and report how alike they are.

## Potential leads for future research
- **[Pore-only tree]** Align only the pore regions for a sharper placement of the choanoflagellate channel.
- **[Outside reader]** Manuscript 2 v0.11 now has five figures.
- **[Aligner in the gene finder]** Use `dcf_align` to name unnamed genes by their nearest annotated relative (e.g. the unnamed zebrafish Kv channels).
