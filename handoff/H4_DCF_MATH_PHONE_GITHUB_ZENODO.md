# DCF Handoff 4 of 8: dcf-math, the phone bundle, GitHub and Zenodo
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 24 November 2026 (after L3997)

---

## 1. Repositories
| repo | contents | state on 24 Nov 2026 |
|---|---|---|
| **`xNOMEREMORTALx/dcf-math`** (MIT) | rounds, pre-registrations, notes/manuscripts, phone bundle, figures, supplementary, handoff | **~510 commits;** tags v1.0.0, v1.1.0, v1.2.0, v1.3.0 (v1.3.0 = Gary's re-release of v1.2.0 with the phone zip attached). **Unreleased since v1.3.0:** rounds L3817–L3997, Manuscript 3 v0.1→v2.9, Manuscript 4 v0.7, status pages, `dcf_visualmic.py`, this handoff |
| **`xNOMEREMORTALx/dcf-genefinder`** (MIT) | tools (H3), CHANGELOG, seen lists, Note G | tags v1.0.0, v1.1.0, v1.2.0. **Unreleased:** the dcf_cryreader family rule (L3829) |

### dcf-math layout
```
README.md            overview + record line (refreshed 24 Nov: 623/870, audit 290/397)
INTEGRATION.md       map of threads with [P]/[V]/[B]/[D]/[✗] labels (last full rewrite L3261)
CITATION.cff         citation, ORCID, DOIs
rounds/              L####_report.md, dcf_*_L####.py, L####_tool_output*.txt, L####_grade_output.txt,
                     L3485_audit2.py (the biology audit; run it to print the total)
preregistrations/    PREREGISTERED_L####_*.txt (236 files), LEDGER.md (path | sha256)
notes/               manuscripts (all versions), notes, DCF_status_2026-11-23.md, Standing_methods_rules_v1.md,
                     Release_v1.x_notes.md, Reader_brief_Manuscript2.md, Submission_plan_FeS_ladder_v0.1.md
phone/               dcf_phone_6.05 … 6.20.py, bundles 6.10 … 6.20 (.zip), dcf_visualmic.py, README_PHONE.txt
figures/ supplementary/ data/ mrna/   publication figures, supplementary tables, small data
handoff/             H1–H8 (this series)
```

## 2. Zenodo DOIs (as recorded in the READMEs and CITATION files)
| repo | concept DOI (all versions, **cite this**) | v1.0.0 | v1.1.0 | v1.2.0 |
|---|---|---|---|---|
| dcf-math | **10.5281/zenodo.24234794** | 10.5281/zenodo.24234795 | 10.5281/zenodo.24302678 | 10.5281/zenodo.24331499 |
| dcf-genefinder | **10.5281/zenodo.24234985** | 10.5281/zenodo.24234986 | 10.5281/zenodo.24302710 | 10.5281/zenodo.24331605 |

- **Check needed (Gary):** the dcf-math **v1.3.0** release (the phone zip re-release) may have its own Zenodo DOI. Gary's message listed 24331605 and 24331499, which are the v1.2.0 DOIs in our files.
  - Open https://doi.org/10.5281/zenodo.24234794 and look at "Versions".
  - If v1.3.0 has a new DOI, send it so the CITATION file and README can list it.
- **ORCID:** 0009-0008-9235-4493.

## 3. Phone bundle (Pydroid 3 on Android)
**Current bundle: 6.20** (`phone/dcf_phone_bundle_6.20.zip`, 12 .py files + README_PHONE.txt).
- **SHA-256:** `dcf_phone_6.20.py` d2020bfe…; zip 551c5b57….
- **Self-test:** 270/270.

**Set up:**
1. Copy **all 12 .py files** into one folder.
2. Pydroid → Pip: `numpy`, `mpmath`.
3. Open `dcf_phone_6.20.py` and press Run.

**Menus (selection):**

| menu | what |
|---|---|
| 25 | DNA view of 1/p (base-4 Midy = Watson–Crick) |
| 26 | gene finder |
| 27 | DNA data storage (codec + error correction) |
| 28–29 | theorems; Gary's reduction in any base and the period clock |
| 30 | energy-metal tier from a genome |
| 32 | motif scan (ladder, `ladder_p`, hedgehog, voltage sensor, zinc) |
| 33 | exon map (mRNA → chromosome) |
| 34 | nerve chemistry by metal (channels, pumps, NMDA, iron enzymes, battery ratio, excitability kit) |
| 35 | protein aligner (global / local) |
| 36 | DNA data store with a noisy-read 6-letter word index |
| 37 | cryptochrome reader (whole proteome; family rule; TrpA–D) |

**New (24 Nov), stand-alone `phone/dcf_visualmic.py`: the visual microphone.**
- **What it does:** turns slow-motion video of a vibrating object into a .wav file, a spectrum PNG and a report.
- **Install:** Pydroid → Pip: `opencv-python`, `numpy` (and `matplotlib`, optional).
- **Settings:** `MODE = "selftest"` checks itself; `MODE = "video"` reads the newest video in DCIM/Camera. Set `CAPTURE_FPS` to the real shooting rate and `TEST_TONE_HZ` to the tone played.
- **Frequency limit:** only vibrations below **frame rate ÷ 2** can be recovered (240 fps → 120 Hz). The report warns about aliasing.
- **Tested here:** self-test 37 Hz, MATCH; compressed mp4 at 80 Hz, MATCH; a 150 Hz alias predicted at 90 Hz and found; a still scene never matched.
- **Experimental:** `ROLLING = True` (rolling-shutter trick), untested on real video.
- **Not yet in the bundle menus.** Lead: add it as menu 38 in 6.21.

## 4. Git workflow (cloud session)
```bash
git -c user.name="Gary NOMEREMORTAL Mason" -c user.email=author@example.invalid commit -m "L####: <what>

<attribution lines from the session's system instructions>"
git push
```
**After every graded round:**
1. Add an audit entry in `rounds/L3485_audit2.py` (tuple `('<label>', 'L####_grade_output.txt')`), then run it to get the total.
2. Write the report `rounds/L####_report.md`.
3. Update the manuscript version if the round touches it.
4. Refresh the status page at milestones.
5. Never commit genome or loop data files, personal data, or Gary's email.

## 5. Next releases: a checklist (Gary presses "Publish")
**dcf-math v1.4.0, "rounds L3817–L3997".**

The release description (to paste) should say:
- **Record:** 623 of 870 pre-registered predictions passed (+3 split); biology audit 290 of 397; failures kept.
- **New:**
  - Manuscript 3 (K⁺-channel genes at CTCF loop anchors) v2.9;
  - the loop-partner signature (replicated blind);
  - specificity controls: non-K⁺ tetramers, resting-potential genes, six-fold channels and mitochondrial OXPHOS genes all show no excess;
  - the T-cell reference controls;
  - the period-24 / 2701 enumeration;
  - phone `dcf_visualmic.py`.
- **Not for medical use.**
- **Asset:** `phone/dcf_phone_bundle_6.20.zip` (or 6.21 if the visual microphone is added).

**Steps:**
1. Claude updates CITATION version and date, and the README record line.
2. Gary: GitHub → Releases → "Draft a new release" → tag `v1.4.0` → paste the description → attach the zip → Publish.
3. Zenodo mints a DOI. Gary sends it back, and Claude adds it to CITATION, README and the manuscripts.

**dcf-genefinder v1.3.0.**
- `dcf_cryreader.py` now calls the chain type by the family rule (L3829).
- The README version line (already corrected to 2.32 on 24 Nov).
- Same steps as above.

## Summary
- **Both repositories are current on GitHub,** with Zenodo concept DOIs 24234794 (dcf-math) and 24234985 (dcf-genefinder).
- **Eighty-plus rounds (L3817–L3997) and the visual microphone are committed but not yet released.** v1.4.0 / v1.3.0 are ready to prepare.
- **Phone bundle 6.20** (self-test 270/270) plus the stand-alone visual microphone.

## Potential leads for future research
- **[Release v1.4.0 / v1.3.0]** Prepare the notes, then Gary publishes.
- **[Phone 6.21]** Add the visual microphone as menu 38 and a "dcf_anchor" summary as menu 39.
- **[INTEGRATION refresh]** Rewrite `INTEGRATION.md`, last fully updated at L3261, to include the nerve, cryptochrome and chromatin threads.
