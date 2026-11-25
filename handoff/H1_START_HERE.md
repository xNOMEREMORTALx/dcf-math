# DCF Handoff 1 of 8: START HERE. Who, rules, where everything lives, and how to reconnect
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · handoff written 24 November 2026 (after round L3997)

**Read this file first, then H2–H8.**

| file | contents |
|---|---|
| **H1** | who, the standing rules, locations, how to reconnect, the first message to paste |
| **H2** | every formula and theorem (mathematics and biology), labelled proved / verified / blind / description / failed |
| **H3** | the genome toolkit ("gene finder / sequence reader"): tools, versions, blind records, usage, the blind protocol |
| **H4** | dcf-math, the phone bundle, GitHub and Zenodo: repositories, releases, DOIs, the next release checklist |
| **H5** | the lead path (prioritised), closed leads, and what waits on Gary |
| **H6** | round log L3177–L3997 (one line per round) and the record |
| **H7** | the four manuscripts and the notes: status and next step for each |
| **H8** | applications and future directions for DCF across fields |

This series replaces the 8 November handoff (H1–H6 after L3173). The old versions are in git history.

---

## 1. Who and what
- **Researcher:** Gary NOMEREMORTAL Mason, an independent researcher. ORCID 0009-0008-9235-4493.
- **Project:** the **Digital Cosmos Framework (DCF)**. It covers:
  - **number theory:** reciprocal periods, the digit-agreement law Λ, star/hexagonal grids, Fibonacci periods, Euler/Heegner 41/163, repunits;
  - **biology, all label-free and pre-registered:**
    - a gene finder and genome readers;
    - the iron–sulfur "ladder" energy scale;
    - nerve metal chemistry (channels and pumps by ion);
    - the cryptochrome tryptophan chain;
    - potassium-channel genes at CTCF chromatin-loop anchors (3D genome).
- **Working style:**
  - Gary says "Pursue leads". Each round is numbered **L####** in steps of 4.
  - **The last round was L3997, so the next is L4001.**
- **Running record (24 Nov 2026):**
  - **623 of 870 pre-registered predictions passed, plus 3 split** (all rounds).
  - **Biology audit (nerve chemistry onward): 290 of 397** (`rounds/L3485_audit2.py`).

## 2. Standing rules (follow every round)
1. **Format.** Deliverables are **Markdown**, with the byline "Gary NOMEREMORTAL Mason". Each ends with **"## Summary"** and **"## Potential leads for future research"**, with each lead labelled, e.g. **[T-cell activation]**.
2. **Numerical-claim rule (verbatim, from Gary).** Any claim "X contains substring S at position N" is checked before it is recorded:
   ```python
   import mpmath
   mpmath.mp.dps = 12000
   pos = mpmath.nstr(X, 10000, strip_zeros=False).split('.')[1].find(S) + 1
   print(pos)
   ```
3. **Untrusted by default (Gary's policy).** "Any new numerical claim from any source — Grok, Gemini, GPT, even me — gets run through the mpmath check before it touches a manuscript draft." Other numbers (masses, constants) are recomputed or checked against a primary source.
4. **Pre-register.**
   - Write `preregistrations/PREREGISTERED_L####_<topic>.txt`.
   - Append `| path | \`sha256\` |` rows for it, the script and the grader to `preregistrations/LEDGER.md`.
   - Commit and push **before computing**.
   - Then run, commit the tool output **before grading**, and grade with a separate grader script.
5. **Failures stand.** Grader bugs are fixed only in the parser, with the original kept. Missing or void files are dropped, never substituted. Amendments are made only before data are seen.
6. **Downgrades.** When a later round undercuts an earlier conclusion, add a dated note to the earlier report (example: L3953 after L3961). The grading itself never changes.
7. **The 16 + 1 standing methods rules** (`notes/Standing_methods_rules_v1.md`; summarised in H2 §8) apply to every pre-registration.
8. **Untrusted files.** Each download or extracted archive goes in its own new directory. Python that reads it runs with `-I`. Never paste genome files into outputs. Identify files by content (LOCUS line, MD5, headers), not by name.
9. **Privacy (H1 rule 8, verbatim).** "Do **not** open personal Drive files: iCloud photos; HealthSummary zips; `dna-data-2022-09-06` (personal DNA); `mydata*`; esoteric images; the 95 MB "Nov 25, 2020 – Jun 10, 2026.zip". Never put Gary's email in public commits; commits use the author name "Gary NOMEREMORTAL Mason" and the email `author@example.invalid`."
10. **Medical.** Not for medical use. Nothing in DCF is a diagnosis or a treatment.
11. **Releases.** GitHub releases are made by Gary (he presses "Publish"); Zenodo archives them automatically and mints DOIs. Claude prepares the notes (H4).
12. **Commit trailer** used in this session (keep whatever the new session's system instructions give):
    ```
    Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
    ```

## 3. Where everything lives
| place | what |
|---|---|
| **GitHub `xNOMEREMORTALx/dcf-math`** (MIT) | everything except the gene-finder code: `rounds/` (all round scripts, tool outputs, grade outputs, reports L3181–L3997), `preregistrations/` (236 files + `LEDGER.md`), `notes/` (manuscripts, notes, status page, standing rules), `phone/` (bundle 6.20 + `dcf_visualmic.py`), `figures/`, `supplementary/`, `data/`, `handoff/` (this series), `INTEGRATION.md`, `CITATION.cff` |
| **GitHub `xNOMEREMORTALx/dcf-genefinder`** (MIT) | gene finder v2.32 and tools (H3), `CHANGELOG.md`, `seen_accessions.txt` (201), `seen_names.txt`, `docs/` |
| **Zenodo** | archived releases of both repositories (DOIs in H4) |
| **Google Drive folder `11-3-2026 handoff`** | older round reports (to L3173) and code zips |
| **claude.ai Project "GARY'S DIGITAL COSMOS FRAMEWORK"** | older docs (master formulas, paper drafts v0.35–v0.38, Perplexity/Grok logs, PDFs) and **this handoff series (H1–H8)** |

**Data files are NOT in the repositories** (licence and size). The new session has to re-download them; the accessions are in H5 §4.
- **ENCODE / 4DN loop and peak files:** a few MB each.
- **GENCODE v49 GTF.**

## 4. Reconnecting in a new conversation
1. **GitHub.** The Claude GitHub App is installed on `xNOMEREMORTALx`. In the new session:
   - attach both repos (`add_repo`, owner `xNOMEREMORTALx`, repos `dcf-math` and `dcf-genefinder`, access `push`);
   - clone them;
   - confirm a push works with a trivial commit.
   - If a push returns 403, Gary reinstalls the app for those repos.
2. **Google Drive** (optional): enable the connector in claude.ai Settings → Connectors. Search `11-3-2026 handoff`. Respect the privacy list.
3. **Data for the chromatin work:**
   - **The shell cannot reach encodeproject.org.** WebFetch/WebSearch can read pages.
   - **Gary downloads the files** from direct links of the form `https://www.encodeproject.org/files/ENCFFxxxxxx/@@download/ENCFFxxxxxx.bedpe.gz` and attaches them (zipped or as-is).
   - **He sends screenshots of ENCODE file graphs** so Claude can pick the starred default file.
   - **GENCODE v49 GTF:** Gary attaches it if it cannot be fetched.
4. **Phone:** see H4 §3 (Pydroid 3; copy all 12 bundle files; pip install numpy, mpmath; opencv-python for the visual microphone).
5. **First message to paste in the new chat:**
   > "Continue the DCF project from the handoff in GitHub `xNOMEREMORTALx/dcf-math/handoff/` (H1–H8) and the claude.ai Project. Next round L4001. Record 623 of 870 (+3 split), audit 290 of 397. Pursue leads."

## Summary
- **This file covers** the rules (verbatim where Gary set them), where everything lives, how to reconnect GitHub, Drive and data, and the first message for the next chat.
- **The work continues from L4001,** with the record at 623 of 870 plus 3 split, and the audit at 290 of 397.

## Potential leads for future research
- **[Setup check]** In the new session, first confirm that a GitHub push works and that the last commit in dcf-math is the handoff commit of 24 November 2026.
- **The full lead path is in H5;** future directions are in H8.
