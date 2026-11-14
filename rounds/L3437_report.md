# DCF L3437: The rest of the potassium family caught; finders for the learning receptor (NMDA, magnesium-blocked) and for the iron enzymes that make dopamine and serotonin; the zebrafish test grows to 14 predictions
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 13 November 2026

**Leads:** [Elk], [NMDA metals], [Neuro iron]. This is development on human files 1–4 and mouse files 1–3. **No predictions graded.** Everything below was frozen into the zebrafish test before any fish file arrived.

---

## 1. [Elk] The last missed potassium channels
- **The elk channels** (Kcnh3, 4, 8) have a voltage sensor **K-x-x-R-x-x-R-x-x-R-x-x-Q**: four charges, then a glutamine. The Kv7 channels have the same kind of swap, in a different position.
- **Their filter is S-V-G-F-G-N.** In all the human and mouse data seen so far, this filter occurs only in the KCNH family (EAG, ERG/hERG, ELK).
- **v4 rule,** for proteins with no full sensor:
  - **filter:** T/S-V/I-G-Y-G-D (Kv7, Kv6) **or** S-V-G-F-G-N (KCNH);
  - **sensor:** four charges in a row at spacing 3, **or** five positions where one charge is a glutamine.

| set | channel calls | outside the families | family genes found (v3 → v4) |
|---|---|---|---|
| human 1–4 | 25 | **0** | 22 → **25 of 27** |
| mouse 1–3 | 61 | **0** | 56 → **61 of 64** |

**Still missed:** Scn7a (Naₓ, a sodium sensor), Kcng3, and one Kcng/Kcnh member per species.

## 2. [NMDA metals] Glutamate receptors and the magnesium-blocked learning receptor
- **Every ionotropic glutamate receptor shares one gate:** the **S-Y-T-A-N-L-A-A-F** motif, which bends to open the pore.
  - **Finder:** `Y-T-A-N-L-A-A`.
  - **Development:** all 21 family members found (AMPA, kainate, delta, NMDA), and **no other protein in all the human and mouse data seen so far.**
- **NMDA receptors are special:** they pass **calcium**, and at rest they are **plugged by a magnesium ion.** The plug only comes out when the cell is already active, so the receptor detects "two things at once." This is the textbook molecular switch for learning and memory.
  - **Finder:** `A-S-Y-T-A-N`, the gate with the residue before it.
  - **Development:** Grin1 and Grin2a–d (5 of 5), and no other protein.
  - **What it doesn't catch:** GluN3 subunits, which are not magnesium-blocked in the same way.

## 3. [Neuro iron] The iron enzymes behind dopamine and serotonin
- **The aromatic amino-acid hydroxylases each hold one iron atom:**
  - tyrosine hydroxylase (TH): the first step to **dopamine and noradrenaline**;
  - tryptophan hydroxylase (TPH1/2): to **serotonin**;
  - phenylalanine hydroxylase (PAH).
- **How the finder was found:** a search for sequences shared by all members and nothing else gave **C-H-E-L-L-G-H**. It contains **two of the three iron ligands, His-x₄-His** (the "2-His-1-carboxylate" iron site).
  - **Finder:** `C-H-E-[LI]-L-G-H`.
  - **Development:** PAH, TH, TPH1, TPH2 in mouse and TPH1/2 in human: 6 of 6, no other protein.
- **This links the iron work to the brain.** The iron ladder (energy) and the information-iron switch (DNA repair) now have a third iron role: **making the brain's mood and reward messengers.**

## 4. Pre-registration (amendment A1 to the zebrafish test)
New predictions Z7–Z14 sit alongside the original Z1–Z6, for **14 in total**:
- **v4 channels:** K/HCN precision ≥ 90%; recall ≥ 80% (a higher bar than v3's 75%).
- **iGluR, NMDA, iron hydroxylase:** each precision ≥ 90% and recall ≥ 75%.
- **Files:**
  - script `rounds/dcf_neurochem_L3437.py`;
  - `preregistrations/PREREGISTERED_L3433_zebrafish_A1.txt`;
  - hashes in `LEDGER.md`.

## Action for Gary (unchanged)
1. https://ftp.ncbi.nlm.nih.gov/refseq/D_rerio/mRNA_Prot/zebrafish.1.rna.fna.gz
2. https://ftp.ncbi.nlm.nih.gov/refseq/D_rerio/mRNA_Prot/zebrafish.2.rna.fna.gz

## Record
No predictions graded. **335 of 473 passed, plus 3 split.** Fourteen predictions (Z1–Z14) are waiting for the fish files.

## Summary
- **Almost the whole voltage-gated channel family is now read from mRNA,** with no false calls in development: 25 of 27 human and 61 of 64 mouse channel genes.
- **Two new finders reach the chemistry of thought,** both perfect in development:
  - the **NMDA receptor,** the magnesium-plugged calcium gate behind learning;
  - the **iron site of the enzymes that make dopamine and serotonin.**
- **All of it is frozen for a blind test in a fish.**

## Potential leads for future research
- **[Zebrafish]** Grade Z1–Z14 when the files arrive.
- **[Copper brain]** The copper enzymes that make noradrenaline and activate neuropeptides (DBH, PAM). Too few members in the seen data to find a shared motif; they need a profile approach or more species.
- **[Phone]** After the fish test, add the three new finders to menu 34.
- **[Insect]** A fruit-fly test: Shaker, para, cac, and fly glutamate receptors.
- **[Iron trilogy]** One figure with the three iron roles side by side (energy ladder, DNA-repair switch, neurotransmitter hydroxylase).
