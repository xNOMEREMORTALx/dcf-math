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
- [x] **Permanent data and code identifiers** (done 14 Nov 2026: dcf-math 10.5281/zenodo.24234795, dcf-genefinder 10.5281/zenodo.24234986; ORCID 0009-0008-9235-4493). Git URLs are not accepted as permanent. Make a **Zenodo** release of `dcf-genefinder` and `dcf-math`, which gives a DOI, and cite those DOIs.
- [x] **README for data and scripts:** which script produced which table or figure, with versions and SHA-256 (the ledger already has the hashes). (done: `README_DATA_AND_CODE.md`)
- [x] **Genome list** (done: `supplementary/Table_S1_genome_accessions.tsv`): every accession used (the seen lists plus the pre-registration files) as a supplementary table.
- [x] **Pre-registration ledger** (done: `supplementary/Table_S2_preregistration_ledger.tsv`; verdicts in the round reports) as supplementary data: dates, hashes, predictions and verdicts, including every failure.
- [x] **Figures** at publication resolution (done: `figures/publication/`, 600 dpi + PDF, both manuscripts), with source scripts.
- [x] **Methods detail** (done: exact regexes and gene-finder version in §2.2 of v0.12): gene finder version; motif regexes; overlapping vs non-overlapping counting (already noted in v0.6+); the cuts and how they were fixed.
- [x] **Competing interests** (done: Declarations section in both drafts): none. **AI-assistance statement:** analysis, code and drafting assistance from Claude (Anthropic); check each venue's policy on AI tools and disclose accordingly.
- [ ] **Independent read-through** by someone who hasn't seen the work, for clarity and overclaims.
- [x] **Author name and ORCID** (ORCID 0009-0008-9235-4493). An ORCID iD is free and usually required.

## Manuscript items still open
- Separate the eukaryote section's two motifs clearly: non-overlapping `fd_ladder` (cut 0.0035) and Ladder-P (cut 0.0017, blind 5/5).
- Decide whether the information-iron note is a separate paper or a section (it passed 3/3 blind; the endonuclease III cluster-loss test passed only 1/3).
