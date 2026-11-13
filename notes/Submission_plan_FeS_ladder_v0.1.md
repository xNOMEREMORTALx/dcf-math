# Submission plan: iron-ladder manuscript (v0.8)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 13 November 2026

## Recommended route
1. **Post a preprint on bioRxiv** (Microbiology or Genomics section). Independent researchers can post; list the affiliation as "Independent researcher".
2. **Submit the preprint to Peer Community In Microbiology** for free, open peer review.
   - If recommended, publish in the **Peer Community Journal**: free to read, **free to publish**, open access, published as the recommended preprint.
   - **Scope check needed:** the PCI page read in L3405 says eligibility depends on the question "relating to evolution". The manuscript should then foreground the evolutionary angle: tiers across bacteria, archaea and eukaryotes; anaerobic protists converging on PFOR and Fe-hydrogenase; the lineage-specific loss of the endonuclease III cluster. Email the managing board to confirm fit before submitting.
3. **Fallback: *Microbial Genomics*** (Microbiology Society, Gold OA). Its scope explicitly welcomes "new methods of microbial sequence analysis that can scale to large datasets including thousands of genomes" and genome evolution. It charges an APC, whose amount was not stated on the page read; check its Open Access costs page.
4. **Less suitable: *ISME Communications*** (Brief Communications exist, fully OA, APC not stated on the page read). Its scope is microbial **ecology**, and it excludes single-organism studies without an ecological context. Our work is genome-centred, so the fit is weaker.

## What every route needs (checklist)
- [ ] **Permanent data and code identifiers.** Git URLs are not accepted as permanent. Make a **Zenodo** release of `dcf-genefinder` and `dcf-math`, which gives a DOI, and cite those DOIs.
- [ ] **README for data and scripts:** which script produced which table or figure, with versions and SHA-256 (the ledger already has the hashes).
- [ ] **Genome list:** every accession used (the seen lists plus the pre-registration files) as a supplementary table.
- [ ] **Pre-registration ledger** as supplementary data: dates, hashes, predictions and verdicts, including every failure.
- [ ] **Figures 1–3** at publication resolution, with source scripts.
- [ ] **Methods detail:** gene finder version; motif regexes; overlapping vs non-overlapping counting (already noted in v0.6+); the cuts and how they were fixed.
- [ ] **Competing interests:** none. **AI-assistance statement:** analysis, code and drafting assistance from Claude (Anthropic); check each venue's policy on AI tools and disclose accordingly.
- [ ] **Independent read-through** by someone who hasn't seen the work, for clarity and overclaims.
- [ ] **Author name and ORCID.** An ORCID iD is free and usually required.

## Manuscript items still open
- Separate the eukaryote section's two motifs clearly: non-overlapping `fd_ladder` (cut 0.0035) and Ladder-P (cut 0.0017, blind 5/5).
- Decide whether the information-iron note is a separate paper or a section (it passed 3/3 blind; the endonuclease III cluster-loss test passed only 1/3).
