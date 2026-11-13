# DCF L3405: validated ladder motifs built into the scanner and the phone (6.09d, 263/263); a submission route chosen: bioRxiv preprint → Peer Community In Microbiology (free) → Peer Community Journal; *Microbial Genomics* as fallback
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 13 November 2026

**Leads:** [Scanner v2], [Venue].

---

## 1. Scanner v2
**`dcf_motif_scan.py`** (`5be0a329…`) gains two presets:
- **`fd_ladder_ov`:** the overlapping ladder, the prokaryote tier motif (cuts 0.0045 | 0.023 | 0.060; blind 35/37);
- **`ladder_p`:** C-x₂-C-x₂-C-x₃-C-P, overlapping, the eukaryote motif (cut 0.0017; blind 5/5).

**The frozen `fd_ladder`** (non-overlapping, used in the protist tests) is unchanged, and its description now says so.

**Checks:**
- *E. invadens* gives 0.0094 (overlapping) and 0.0030 (Ladder-P), the same as the frozen L3397 script;
- *L. gasseri* gives 0.

**Phone bundle 6.09d:** self-test **263/263**. In menu 32, type `ladder_p` or `fd_ladder_ov`.

## 2. Venue
Pages read: *Microbial Genomics* scope, ISME Communications journal information, and the PCI Microbiology guide for authors.

| option | cost to publish | fit | notes |
|---|---|---|---|
| **bioRxiv → PCI Microbiology → Peer Community Journal** | **free** | good if framed around evolution (scope check needed) | open reviews published; data and code need DOIs (Zenodo) and READMEs |
| *Microbial Genomics* | APC (amount not on the page read) | strong: "methods … that can scale to … thousands of genomes", genome evolution | Gold OA |
| ISME Communications (Brief Communication) | not stated on the page read | weaker: microbial ecology focus | fully OA |

**Plan:** `notes/Submission_plan_FeS_ladder_v0.1.md`, with a full checklist:
- Zenodo DOIs;
- READMEs;
- the genome table;
- the ledger as supplementary data;
- figures and methods detail;
- the AI-assistance disclosure;
- ORCID;
- an independent read-through.

## Record
No predictions graded. **323 of 461 passed, plus 3 split.**

## Summary
- **The validated motifs are now built into the tools.** The scanner and the phone (6.09d, 263/263) offer the overlapping ladder for bacteria and archaea and the proline ladder for eukaryotes.
- **A publishing route is chosen:** post the manuscript as a free preprint, then submit it to Peer Community In Microbiology. Its peer review is free, and recommended papers can be published free in the Peer Community Journal. *Microbial Genomics* is the fallback.
- **The main practical step is giving the code and data permanent DOIs** through Zenodo.

## Potential leads for future research
- **[Zenodo]** Link the GitHub repos to Zenodo and make a release of each, which gives citable DOIs. Gary does this from his GitHub and Zenodo accounts.
- **[PCI fit]** Draft a short enquiry to the PCI Microbiology managing board about scope.
- **[ORCID]** Register an ORCID iD if there isn't one yet.
- **[Independent review]**, **[More anaerobes]**: carried.
