# DCF L3461: Truth rule v3, a fruit-fly blind test pre-registered, and an outline for Manuscript 2
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 14 November 2026

**Leads:** [Truth rule v3], [Insect], [Manuscript 2]. **No predictions graded.**

---

## 1. [Truth rule v3] (`rounds/dcf_truth3_L3461.py`)
**What changed:**
- **Descriptions are matched as word sets in any order.** For example, "voltage-gated sodium channel SNS" now counts as sodium; it was the chicken C2 failure, and that **stays a failure**.
- **The calcium description must contain "alpha".** This keeps auxiliary β subunits out.
- **Fly gene symbols are listed:**
  - channels: para, cac, Ca-alpha1D, Ca-alpha1T, Sh, Shab, Shaw, Shal, eag, sei, elk, KCNQ, Ih;
  - leak channels: Ork1, Task6, Task7, galene, sand;
  - receptors: GluRIIA–E, GluRIA/B, Grik, clumsy, KaiR1D, Nmdar1/2;
  - iron hydroxylases: ple (tyrosine hydroxylase), Hn (henna), Trh;
  - pumps: Atpalpha, SERCA, PMCA, SPoCk, ATP7.
- **The fly DSC1/NaCP60E channel** (a mixed Na/Ca "DEEA" ring) is assigned to no class.

**Calibration:** v3 credits all 104 chicken calls. It was built after seeing the chicken result and is used only for future tests.

## 2. [Insect] Pre-registered blind test: fruit fly
- **Pre-registration:** `PREREGISTERED_L3461_fly.txt`, frozen.
- **The tool is unchanged:** the same `dcf_neurochem2_L3449.py` that passed 13 of 14 in chicken.
- **14 predictions, F1–F14.** Two bars were set lower or differently **in advance:**
  - K2P recall ≥ 50%, because fly leak channels are very divergent;
  - iron-hydroxylase recall ≥ 2 of 3.
- **Stated expectation (not graded):** the fly has **one** sodium channel (para), three calcium channels, and Shaker-family potassium channels. Its metal gates should be the same kinds as in vertebrates, across ~600 million years.

## 3. [Manuscript 2] Outline
- **File:** `notes/Manuscript_nerve_metals_outline_v0.1.md`.
- **Content:** working abstract, methods, results by species, a failure table, and figures planned.
- **Status:** drafting waits for the fly result.

## Action for Gary: the fly file
1. https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/001/215/GCF_000001215.4_Release_6_plus_ISO1_MT/GCF_000001215.4_Release_6_plus_ISO1_MT_rna.fna.gz
2. **Backup:** https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_000001215.4/download?include_annotation_type=RNA_FASTA (send the whole zip).

## Record
No predictions graded. **365 of 508 passed, plus 3 split.** F1–F14 are waiting.

## Summary
- **The truth rule now reads descriptions in any word order and knows fly gene names.** It was calibrated on chicken without changing any past grade.
- **The frozen nerve-chemistry tool will next be tested on the fruit fly,** the largest evolutionary jump so far.
- **A second manuscript is outlined** from the four blind data sets (40 of 45 passed).

## Potential leads for future research
- **[Fly]** Grade F1–F14.
- **[Audit 2]** A number-audit script for the Manuscript 2 table.
- **[Battery balance]** The ratio of pump genes to channel genes across species.
- **[Copper brain]** A finder for the copper enzymes DBH and PAM.
