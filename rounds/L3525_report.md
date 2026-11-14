# DCF L3525: Both repositories archived with DOIs; ORCID added; supplementary tables, publication figures and declarations prepared. Both manuscripts are one step from an outside reader
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 14 November 2026

**Lead:** [Submission]. **No predictions graded.**

---

## Permanent identifiers
| repository | Zenodo record (checked) | DOI |
|---|---|---|
| dcf-math v1.0.0 | "Digital Cosmos Framework (DCF): pre-registered tests of iron-sulfur energy tiers and of nerve metal chemistry read from sequence" | **10.5281/zenodo.24234795** |
| dcf-genefinder v1.0.0 | "DCF gene finder and nerve-chemistry tools: label-free gene calling and metal-class annotation" | **10.5281/zenodo.24234986** |

- **ORCID:** 0009-0008-9235-4493.
- **Where it now appears:**
  - `CITATION.cff` in both repositories (ORCID and DOI);
  - `.zenodo.json` (ORCID, for future versions);
  - a DOI badge in both READMEs;
  - `README_DATA_AND_CODE.md`;
  - both manuscripts.

## Manuscripts
- **Manuscript 1 (iron ladder) v0.12** (`notes/Manuscript_FeS_ladder_draft_v0.12.md`):
  - data availability now cites both DOIs, and both archives are in the reference list;
  - exact regexes and the gene-finder version are added to §2.2;
  - a Declarations section is added (competing interests, funding, AI-assistance statement, ORCID).
- **Manuscript 2 (nerve metals) v0.6** (`notes/Manuscript_nerve_metals_draft_v0.6.md`):
  - DOIs and ORCID;
  - §3.8, the *Hofstenia* result (exploratory; E, against my K leaning);
  - Figure 4 with the acoel row;
  - Declarations.

## Supplementary material (`supplementary/`)
- **Table S1:** 200 genome accessions, 186 of them named in pre-registration files.
- **Table S2:** 170 ledger entries, each with SHA-256 and first commit date. Four rows have annotated names that git could not date; their hashes are still in the ledger.
- **Publication figures** (`figures/publication/`): all eight manuscript figures at 600 dpi PNG and vector PDF, re-rendered by `render_all.py` from the unchanged source scripts.

## Submission checklist (Manuscript 1; the same applies to Manuscript 2)
**Done:**
- [x] DOIs
- [x] data/code README
- [x] genome list
- [x] ledger
- [x] figures
- [x] methods detail
- [x] declarations
- [x] ORCID

**Left:**
- [ ] **independent read-through** by someone who hasn't seen the work;
- then the PCI Microbiology scope enquiry (drafted in L3409) and the bioRxiv preprint.

## Record
No predictions graded. **406 of 558 passed, plus 3 split.**

## Summary
- **Both repositories now have permanent DOIs,** confirmed against the Zenodo records, and your ORCID is attached everywhere a citation looks for it.
- **Both manuscripts now cite the archives,** carry declarations, and have supplementary tables and publication-quality figures.
- **The only remaining step before submission is an outside reader.**

## Potential leads for future research
- **[Outside reader]** One person, both drafts, three questions: any wrong claim, is the pre-registration convincing, which journal.
- **[bioRxiv]** Post Manuscript 1 as a preprint after the read-through.
- **[E→K dating]** The pre-registered test on early protostomes and deuterostomes.
- **[Future versions]** Each new GitHub release now creates a new Zenodo version automatically, under the same concept DOI.
