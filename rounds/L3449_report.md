# DCF L3449: The nerve battery. Pumps that store energy and channels that release it, sorted by metal; a 9-letter rhythm in the voltage sensor's DNA; corrected rules frozen for a bird
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 13 November 2026

**Leads:**
- correct the rules ([Truth rule], [NMDA7], [K2P misses], [FeHyd2]);
- Gary's themes: potassium, nervous system and consciousness, the language and harmonics of DNA, oscillation, and storing and retrieving energy to do work.

Everything here is **development on seen data** (human 1–4, mouse 1–3, zebrafish 1–2). **No predictions graded.** The corrected rules are frozen for a blind test in chicken.

---

## 1. Storing and retrieving energy: the pump side of the battery
A neuron works like a rechargeable battery:
- **Charging:** P-type **pumps** spend ATP to push ions uphill.
  - The **Na⁺/K⁺ pump** loads the cell with K⁺ and expels Na⁺; it uses a large share of the brain's energy.
  - **Ca²⁺ pumps** keep calcium low, ready for signalling.
  - **Copper pumps** (ATP7A/B) deliver copper to the enzyme that makes **noradrenaline**.
- **Discharging:** the **channels** sorted in L3425–L3445 let the stored gradient run back downhill. That flow is the nerve impulse: **stored energy turned into work and information.**

**New finder (`rounds/dcf_pump_L3449.py`):**
1. Every P-type pump has the phosphate-accepting site **D-K-T-G-T-[LIVM]-[TI]**.
2. The ion is then read from the **metal-binding loop in membrane helix 4**: the residue just before **P-E-G-L** decides.

| loop | pump class | examples |
|---|---|---|
| **[N/Y]-V-P-E-G-L** | Na⁺/K⁺ (and gastric H⁺/K⁺) | ATP1A1–4, ATP4A, ATP12A |
| **A-[I/V]-P-E-G-L** | Ca²⁺ | SERCA (ATP2A), PMCA (ATP2B), SPCA (ATP2C) |
| **C-P-C** + ≥ 2 **G-M-x-C-x-x-C** copper repeats | Cu | ATP7A, ATP7B |
| none of these | lipid flippases (ATP8–11), P5 (ATP13A); no metal | |

**Development:**
- **Human and mouse:** 47 pumps, **0 mismatches.**
- **Zebrafish:** one fix was needed. Three fish Na⁺/K⁺ paralogs (atp1a1a.2, .3, .5) end P-E-G-L-**P** like a calcium pump. The residue *before* the loop (N-V vs A-I) still tells them apart, so the rule reads that residue instead.
- **After the fix:** 42 fish pumps, 0 named mismatches; one unnamed gene (si:dkey-28b4.8) was called calcium.

## 2. Corrected rules
- **NMDA7, `A-S-Y-T-A-N-L`:** one letter longer than the motif that failed in L3445. It finds all 15 NMDA receptor genes (GluN1/GluN2) in mouse and fish, and **nothing else**. The chance hit in cars2 is gone.
- **FeHyd2, `[C/V]-H-E-[L/I]-L-G-H`:** also accepts the fish tyrosine hydroxylase, which has V where the others have C. The iron-binding H-x₄-H is unchanged.
- **Truth rule v2 (`rounds/dcf_truth2_L3449.py`):** a call is correct if the gene's **symbol or its NCBI description** names the class (e.g. "potassium voltage-gated channel subfamily A member"). Unnamed but described genes are now judged on biology.
  - On the fish data it would have credited all but 7 of 164 calls.
  - The 7 left are genes with no description at all, which stay wrong.
- **K2P misses:** checked and **left unchanged.** In the missed genes, one of the two filters has drifted (T-M-G-F-G, T-T-G-L-G, or lost). Widening the filter added a false call without adding a single missed gene.

## 3. The harmonics of DNA: a 9-letter rhythm in the voltage sensor
- **The voltage sensor is a protein rhythm:** a positive charge every **3rd** amino acid. One amino acid is 3 DNA letters, so in the mRNA the rhythm becomes **every 9 letters**, on top of the codon's own 3-letter beat.
- **The measurement (`rounds/L3449_harmonics.py`):** the strength of each repeat period in 45-letter mRNA windows coding the sensor (403 windows), against random coding windows (2,745).

| period (letters) | sensor power ÷ random power |
|---|---|
| 2 | 0.76 |
| **3 (codon)** | **1.86** |
| 4–8 | 0.74–1.09 |
| **9 (one charge every 3 residues)** | **1.95** |
| 10–15 | 0.63–1.19 |

- **Reading:** the sensor's DNA carries a clear **second harmonic at 9 letters**, nearly twice the background.
- **Honest limits:**
  - The windows were *chosen* by the charge pattern, so a 9-letter rhythm is **expected by construction.**
  - What the measurement shows is how strongly it stands out in the raw DNA letters (the arginine/lysine codons AGR/CGN/AAR at every 9th position).
  - This is an **illustration of the protein-to-DNA "language" mapping**, not a new discovery.
  - It has a physical side: the sensor's charges spiral up a tightly wound helix and move together when the membrane voltage changes. That movement is the **switch that turns stored energy into an impulse.**

## 4. Oscillation, time and evolution: what the data now support
- **The oscillator parts list is readable from mRNA in mammals and fish:**
  - **HCN** pacemaker channels (the depolarizing "drive");
  - **T-type calcium** channels (the rebound bursts);
  - **potassium** channels (the reset);
  - **K2P** leak channels (the resting level that anaesthetics shift).
- **Brain rhythms come from these parts.** The thalamus–cortex rhythms that differ between waking and sleep are built from them.
- **Across ~450 million years (fish to mammals), the metal gates are unchanged in kind:**
  - EEEE/EEDD calcium rings, DEKA sodium rings, T-V-G-Y-G potassium filters, P-E-G-L pump loops;
  - the iron H-x₄-H of the dopamine/serotonin enzymes;
  - fish duplicated many genes, and **both copies kept their metal.**
- **What this does *not* show:** a direct link to space-time or the origin of DNA. That would be speculation beyond what sequence data can test, and I've kept it out of the claims. The data show **conservation through time:** the metal "words" of the nervous system are among the most stable sentences in the genetic language.

## 5. Pre-registered blind test: chicken (bird, ~310 million years from mammals)
`PREREGISTERED_L3449_chicken.txt` and the four script hashes are in `LEDGER.md`, frozen before any chicken file exists here.
- **14 predictions, C1–C14:** channel precision and recall; K2P; iGluR; NMDA7; FeHyd2; pump precision and recall.
- **Graded with the truth rule v2** (symbol or description).
- **One amendment, made the same evening before any data:** the potassium symbol pattern was narrowed back to voltage-gated K genes. The broader pattern would have added inward-rectifier genes that the rule is not built to find to the recall denominator.

## Action for Gary: two chicken files
1. https://ftp.ncbi.nlm.nih.gov/refseq/G_gallus/mRNA_Prot/chicken.1.rna.fna.gz
2. https://ftp.ncbi.nlm.nih.gov/refseq/G_gallus/mRNA_Prot/chicken.2.rna.fna.gz

**Keep the names. If one link doesn't work, send the other;** a missing file is dropped.

## Record
No predictions graded. **352 of 494 passed, plus 3 split.** Fourteen predictions (C1–C14) are waiting.

## Summary
- **The nerve battery is now readable from mRNA from both sides:**
  - pumps that store ATP energy as ion gradients (Na⁺/K⁺, Ca²⁺, Cu), sorted by a one-residue switch in their metal loop;
  - channels that release the energy as impulses.
- **The faulty rules from the fish tests are corrected:** the longer NMDA motif, the wider iron site, and a truth rule that reads descriptions. All are frozen for a bird.
- **The voltage sensor writes a 9-letter rhythm into DNA,** a clear harmonic on top of the 3-letter codon beat. It follows from the sensor's charge pattern and is shown as an illustration.
- **The metal "words" of the nervous system have held across ~450 million years.** That is the strongest link to time and evolution these data can support.

## Potential leads for future research
- **[Chicken]** Grade C1–C14 when the files arrive.
- **[Harmonic beyond the motif]** A non-circular test: does the 9-letter rhythm continue *outside* the matched sensor stretch (flanking windows), or in sensors found only by the weak-sensor route?
- **[Battery balance]** Per species, the ratio of pump genes to channel genes (chargers vs dischargers), across bacteria, protists and animals. This would link the iron-ladder energy tiers to the nervous system.
- **[Copper brain]** ATP7A delivers copper to DBH (noradrenaline). Pair the copper-pump finder with a copper-enzyme finder.
- **[Phone]** Add pumps, NMDA7 and FeHyd2 to menu 34 after the chicken test.
