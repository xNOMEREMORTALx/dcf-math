# DCF Handoff 1 of 6: START HERE. Who, rules, where everything lives, how to reconnect GitHub and Google Drive
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · handoff written 8 November 2026 (after round L3173)

**Read this file first, then H2–H6.**

| file | contents |
|---|---|
| H1 | rules and setup |
| H2 | formulas and theorems |
| H3 | gene-finder toolkit |
| H4 | dcf-math, the phone bundle and GitHub workflow |
| H5 | the path for leads |
| H6 | round log and results |

---

## 1. Who and what
- **Researcher:** Gary NOMEREMORTAL Mason, an independent researcher.
- **Project:** the **Digital Cosmos Framework (DCF)**, which covers:
  - **number theory:** reciprocal periods, the digit-agreement law Λ, star/hexagonal grids, Fibonacci;
  - **biology:** a label-free phone gene finder plus blind-tested genome analyses (genetic code, promoters, pyrrolysine/selenocysteine, metal profiles, oxygen lifestyle).
- **Working style:** Gary says "Pursue leads". Each round is numbered **L####**; the last completed round was **L3173**, so the next is **L3177**.
- **Running record: 256 of 333 pre-registered predictions passed, plus 3 split.**

## 2. Standing rules (follow every round)
1. **Format.** Deliverables are **Markdown**, with the byline *"Gary NOMEREMORTAL Mason"*. Each ends with **"## Summary"** and **"## Potential leads for future research"**, with each lead labelled, e.g. **[Fe-H2]**.
2. **Numerical-claim rule.** Any claim "X contains S at position N" is checked before it is recorded:
   ```python
   import mpmath
   mpmath.mp.dps = 12000
   digits = mpmath.nstr(X, 10050, strip_zeros=False).split('.')[1][:10000]
   pos = digits.find(S) + 1
   ```
3. **External claims are untrusted.** Every LLM-generated number (Grok, Gemini, GPT, Perplexity, even Claude's own) is recomputed before use.
4. **Pre-register.** Write predictions to `PREREGISTERED_L####.txt`, take its SHA-256, publish it to the dcf-math ledger **before** downloading or computing. Grade honestly against base rates and controls, and keep every failure.
5. **Blind genomes:**
   - identify files only by their **LOCUS line**;
   - check every candidate against `seen_accessions.txt` (dcf-genefinder repo) **and** search earlier reports for the **organism name** (the seen list missed name reuse once, in L3141);
   - write and hash the tool numbers **before** reading any annotation.
6. **Download links.** Give NCBI efetch links:
   `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=ACCESSION&rettype=gbwithparts&retmode=text`
   Ask Gary to send them **zipped** (`blind_N.zip`); the next is **`blind_14.zip`**.
7. **Untrusted files.** Each downloaded or extracted archive goes in its own new directory, and Python runs on it with `-I`. Never paste genome files into outputs. Code zips hold tool outputs only.
8. **Privacy.** Do **not** open personal Drive files:
   - iCloud photos;
   - HealthSummary zips;
   - `dna-data-2022-09-06` (personal DNA);
   - `mydata*`;
   - esoteric images;
   - the 95 MB "Nov 25, 2020 – Jun 10, 2026.zip".

   Never put Gary's email in public commits; commits use the author name "Gary NOMEREMORTAL Mason" and the email `author@example.invalid`.
9. **Medical.** Nothing here (e.g. the "cancer protocol" in the zinc-finger document) is to be used for any medical decision.
10. **Project storage.** Writes to the claude.ai project were refused (storage full), so deliver by file send, GitHub and Drive.

## 3. Where everything lives
| place | what |
|---|---|
| **GitHub: `xNOMEREMORTALx/dcf-genefinder`** (MIT) | gene finder v2.31 and tools, README, CHANGELOG, `seen_accessions.txt` (102 accessions), Note G draft |
| **GitHub: `xNOMEREMORTALx/dcf-math`** (MIT) | Λ note v0.5, star-grid note v0.2, phone bundle 6.05, `preregistrations/` (85 files plus `LEDGER.md`), `INTEGRATION.md`, README with the record line; this handoff series is in `handoff/` |
| **Google Drive folder `11-3-2026 handoff`** (Gary is copying it) | most files from this conversation: round reports (L2xxx–L3173), code zips, drafts |
| **claude.ai project "GARY'S DIGITAL COSMOS FRAMEWORK"** | older docs: master formulas, paper drafts v0.35–v0.38, Perplexity/Grok logs, PDFs (read-only in practice) |

## 4. Reconnecting in a new conversation
1. **GitHub.**
   - The Claude GitHub App must be installed on account `xNOMEREMORTALx` (it already is). In the new session, attach both repos (add_repo with `owner=xNOMEREMORTALx`, `repo=dcf-genefinder` / `dcf-math`, `access=push`), then clone.
   - If a push returns 403 "App not installed", Gary reinstalls the Claude GitHub App for those repos.
2. **Google Drive.** In the new conversation the Google Drive connector must be enabled: claude.ai → Settings → Connectors. Then:
   - search for the folder name **`11-3-2026 handoff`** and read files from it as needed;
   - do not open the personal files listed in rule 8.
3. **Phone tools.** Copy the bundle from `dcf-math/phone/`, plus `dcf_genefinder_mobile.py` and the tools from dcf-genefinder, into one folder. In Pydroid 3, pip-install numpy and mpmath.
4. **First message to paste** in the new chat:
   > "Continue the DCF project from the handoff in GitHub `xNOMEREMORTALx/dcf-math/handoff/` (H1–H6) and Drive folder `11-3-2026 handoff`. Next round L3177. Pursue leads."

## Summary
- **This file** gives the rules, the locations, and how to reconnect GitHub and Drive.
- **The work continues from round L3177,** with the record at 256 of 333.
- **Formulas** are in H2, **tools** in H3, **repositories** in H4, **leads** in H5, and **history** in H6.

## Potential leads for future research
- **[Setup]** In the new session, first confirm GitHub push works (a trivial README commit) and that Drive search finds `11-3-2026 handoff`.
- **The full lead path is in H5.**
