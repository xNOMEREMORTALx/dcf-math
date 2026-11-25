# DCF L3997 + forward note: mitochondrial energy genes do not share the potassium anchor excess (blind, 2 of 2), and where this work can go next, including the "visual microphone"
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 24 November 2026

---

## 1. Mitochondria: the test (L3997, pre-registered, blind)
**Files:**
- **Pre-registration:** `PREREGISTERED_L3997_mitochondria.txt`.
- **Script:** `rounds/dcf_oxphos_L3997.py`, seed 3997.
- **Output:** committed before grading.
- **Grading:** `L3997_grade_output.txt`.

**Set (OXPHOS):** 97 nuclear genes for the mitochondrial energy machinery: respiratory complexes I–IV (NDUF*, SDHA–D, UQCR*, CYC1, COX4–8*) and ATP synthase (ATP5*). None had been examined before.

| # | maps | OXPHOS share vs matched | p | prediction | result |
|---|---|---|---|---|---|
| O1 | ten cell lines | 0.317 vs 0.311 | 0.43 | no excess | **PASS** |
| O2 | nine Hi-C maps (T-cell CTCF peak reference) | 0.110 vs 0.113 | 0.55 | no excess | **PASS** |
| (control) | pore K⁺, same runs | 0.368 vs 0.273; 0.180 vs 0.103 | 0.002; 0.001 | — | — |

**2 of 2 passed.**
- **The fixed reading:** the anchor excess is not a property of mitochondrial energy genes. They sit exactly at the matched baseline, and the K⁺ result stays specific.
- **Record:** 623 of 870. **Audit:** 290 of 397.

## 2. Mitochondrial potassium channels: a descriptive look at the L3917 gene scores
Several K⁺ channel genes also make channels inside mitochondria (established physiology; MITOK/CCDC51 is from Paggio et al., *Nature* 2019).

| gene | mitochondrial channel | excess over matched (cell lines / Hi-C / primary) |
|---|---|---|
| **KCNMA1** | mitoBK (inner membrane, heart and brain) | **+0.89 / +0.70 / +0.79**, the strongest of all 79 |
| **KCNJ11** | Kir6.2; mito-K_ATP identity debated (MITOK proposed) | +0.68 / +0.57 / +0.43 |
| KCNK9 | TASK-3, reported in mitochondria | +0.65 / +0.34 / −0.05 |
| KCNJ1 | ROMK, proposed mito-K_ATP pore | +0.18 / +0.39 / −0.02 |
| KCNN3, KCNN2 | mitoSK | small, mixed |
| KCNA3 | mitoKv1.3 | −0.20 / −0.16 / +0.25 |
| KCNK3 | TASK-1 | negative |

**What this shows:**
- **The two top genes, KCNMA1 and KCNJ11, both have mitochondrial roles.** But mitochondrial location as a whole does not predict anchoring: KCNA3 and KCNK3 are below baseline.
- **Not a test, and too few genes to test cleanly.** The energy machinery itself (§1) shows nothing.

## 3. The "visual microphone": what is real and how this work touches it
**What it is:**
- **Davis, Rubinstein et al. (SIGGRAPH 2014)** recovered intelligible sound from silent high-speed video of objects (a crisp packet, a plant leaf, water) by measuring their sub-pixel vibrations.
- **Ordinary cameras can do a lower-quality version** using the rolling shutter.

**The biology version exists:**
- **Nerve cells physically swell and shrink by about a nanometre** during each action potential.
- **Ling et al. (PNAS 2018)** imaged this deformation across whole cells with an interferometric camera, a visual microphone for nerve impulses, without dyes or electrodes.

**Where our potassium result connects (honestly):**
- **The K⁺ channels in our gene set shape the falling phase of each nerve impulse,** and so the time course of that nanometre movement.
- **Our chromatin finding says nothing about the movement itself.** It concerns how these genes are packaged in the nucleus.
- **So the link is biological context, not an application of our data.**

**Something Gary could actually do:**
- **A phone-based visual microphone, a home experiment:** film a light object (a crisp packet or a plant leaf) near a loudspeaker at the phone's highest slow-motion frame rate. Then recover the vibration signal from the video.
- **I can write a small script for the phone bundle** (frame differencing plus phase-based motion along edges) that turns such a video into a sound file and a spectrum.
- **That is a real, testable "forward motion" project:** for example, record a known tone (440 Hz) and check that the recovered spectrum peaks at 440 Hz.

## 4. Forward motion: the most useful next steps, ranked
1. **Manuscript 3 → a preprint.**
   - **It is close to a complete short report:**
     - established results under three CTCF references;
     - blind replications;
     - a new, replicated loop-partner signature;
     - controls showing specificity (non-K⁺ tetramers, resting-potential genes, OXPHOS, six-fold channels).
   - **Next:** an outside reader, then bioRxiv. This is the biggest single step outward.
2. **A reusable tool:** package the matched-gene loop-anchor test as `dcf_anchor.py` in dcf-genefinder. Input: any gene list and loops/peaks files. Output: the excess, matched null, p-values and loop partners. Other researchers could then run it on their own gene families.
3. **The visual-microphone phone script (§3).** A hands-on project with a built-in check (a known tone in, the same tone out).
4. **Mitochondria, deeper:** pre-register KCNMA1-type genes in mitochondria-rich tissue Hi-C (heart or muscle). This needs a heart Hi-C loops file; the heart experiment had none before.

## Summary
- **Blind test of 97 mitochondrial energy genes: no CTCF anchor excess** (p = 0.43 and 0.55). The potassium-channel result stays specific (p = 0.002, 0.001).
- **The top anchored K⁺ gene, KCNMA1, is also the mitochondrial BK channel,** but mitochondrial location overall does not predict anchoring.
- **The visual microphone is real, and so is its nerve-cell cousin** (nanometre swelling during impulses). Our data give context, not an application. A phone-video version is a doable home experiment.

## Potential leads for future research
- **[Preprint]** Manuscript 3, from outside reader to bioRxiv.
- **[dcf_anchor tool]** Package the test for others.
- **[Phone visual microphone]** A script plus a known-tone validation.
- **[Heart Hi-C]** Mitochondria-rich tissue for a KCNMA1 follow-up.
- **[Carried]** T-cell 36 h and HUVEC Hi-C files (links in the previous reply).

## Sources
- Davis A, Rubinstein M, et al. The visual microphone: passive recovery of sound from video. SIGGRAPH 2014. https://people.csail.mit.edu/mrub/VisualMic
- Ling T, et al. Full-field interferometric imaging of propagating action potentials. PNAS 2018. https://pubmed.ncbi.nlm.nih.gov/30564313/
- Paggio A, et al. Identification of an ATP-sensitive potassium channel in mitochondria. Nature 2019. https://ideas.repec.org/a/nat/nature/v572y2019i7771d10.1038_s41586-019-1498-3.html
