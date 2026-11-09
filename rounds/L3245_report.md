# DCF L3245: mRNA — a label-free scanner for the iron-sensing hairpin (IRE), frozen and pre-registered with download links; why *Chloroflexus* gene calls were imprecise; Note K on the Euler–Heegner 41/163 chain
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 9 November 2026

**Leads pursued:** [RNA] (Gary: mRNA to examine), [Chloroflexus], [Heegner note].

**Pre-registration:** `PREREGISTERED_L3245_IRE.txt`, SHA-256 `82ecd2fb…46a5`, commit `c583f1a`, pushed before any mRNA download.

---

## 1. The bridge from our metal work to mRNA [V, literature]
**How cells read iron off their mRNAs.**
- Cells sense iron with **IRP1**, which is **itself an iron–sulfur protein**.
- **With iron,** IRP1 holds a 4Fe-4S cluster and acts as the enzyme aconitase, unable to bind RNA.
- **Without iron,** the cluster is lost and IRP1 binds a small hairpin, the **iron-responsive element (IRE)**, on the mRNAs of the iron-handling genes. It blocks translation from the 5′ UTR (ferritin) or protects the mRNA from the 3′ UTR (transferrin receptor).

**Why it matters here.** This is the same Fe–S chemistry our genome tests read, acting directly on mRNA.

## 2. The IRE scanner (`dcf-math/mrna/dcf_ire.py`, frozen) [pre-registered]
**Model.**
- the **CAGUGN** loop;
- a 5-pair upper stem (G–U allowed, ≤ 1 mismatch);
- the unpaired **C bulge** on the 5′ side;
- a 3-pair lower stem.

**Label-free UTRs.** The coding part is taken as the longest ORF.

**False-hit rate on random sequence:** 0.04–0.07 hits per 10 kb (GC 0.40–0.60), so a 2–5 kb mRNA has about a 1–2.5% chance of a spurious hit.

| id | prediction |
|---|---|
| R1 | ≥ 5 of 7 known IRE mRNAs carry a hit |
| R2 | ≤ 1 of 8 control mRNAs carries a hit |
| R3 | ≥ 80% of IRE-mRNA hits sit in the expected UTR (5′ for FTH1, FTL, ALAS2, ACO2, SLC40A1, EPAS1; 3′ for TFRC) |

**Honest framing.** This tests the tool on known biology, not a discovery. The risk, declared in advance: the ferritin IREs carry an extended internal loop that the strict model may miss.

## 3. Action for Gary: the mRNA download (one link, 15 human RefSeq mRNAs)
**All 15 come back as one GenBank text file;** save it and send it as **`blind_mrna1.zip`**:

https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NM_002032,NM_000146,NM_003234,NM_000032,NM_001098,NM_014585,NM_001430,NM_001101,NM_002046,NM_000546,NM_000454,NM_000518,NM_000207,NM_000477,NM_002467&rettype=gb&retmode=text

| accession | gene | role |
|---|---|---|
| NM_002032 | FTH1 (ferritin heavy chain) | IRE, 5′ UTR |
| NM_000146 | FTL (ferritin light chain) | IRE, 5′ UTR |
| NM_003234 | TFRC (transferrin receptor) | IREs, 3′ UTR |
| NM_000032 | ALAS2 (haem synthesis) | IRE |
| NM_001098 | ACO2 (mitochondrial aconitase, itself an Fe–S enzyme) | IRE |
| NM_014585 | SLC40A1 (ferroportin) | IRE |
| NM_001430 | EPAS1 (HIF-2α, oxygen sensing) | IRE |
| NM_001101, NM_002046, NM_000546, NM_000454, NM_000518, NM_000207, NM_000477, NM_002467 | ACTB, GAPDH, TP53, SOD1, HBB, INS, ALB, MYC | controls |

**Accessions.** These are the standard RefSeq accessions for each gene. Without a version number, NCBI returns the newest version. The DEFINITION line of each record is checked against the gene name before any scan.

**What else these files allow.**
- mRNA-level tests of codon usage and UTR length.
- Gary's 41/401/153 idea on mRNA. That should be pre-registered on a larger set: 15 mRNAs are too few for a periodicity test.

## 4. [Chloroflexus] Why its gene calls were only 78% correct [development]
**The numbers.** Of 4,971 calls, 1,073 match no annotated gene. Their median length is 204 nt; 982 are under 400 nt, and they are spread evenly along the genome.

**The cause.** At GC > 0.55 the finder lowers its minimum gene length from 240 to 180 nt (v2.26). In *Chloroflexus* (GC 0.567) most of the extra short calls are false. Removing calls under 240 nt shows the trade-off:

| genome | GC | correct (all calls → ≥ 240 nt) | found (all calls → ≥ 240 nt) |
|---|---|---|---|
| *Chloroflexus* | 0.567 | 78.4 → **91.3** | 94.4 → 90.7 |
| *Dehalogenimonas* | 0.550 | 89.9 → **95.6** | 84.3 → 79.3 |
| *Haloarcula* | 0.624 | 97.2 → 98.8 | 93.5 → 88.0 |
| *Xanthobacter* | 0.675 | 97.6 → 98.8 | 93.4 → 89.9 |
| *Bordetella* | 0.681 | 99.1 → 99.7 | 95.3 → 93.1 |

**Prodigal on *Chloroflexus*:** 91.0% correct, so this genome is hard for both tools.

**Reading.**
- **A blanket length cut is wrong.** It costs 2–5 points of genes found everywhere.
- **The short calls need their own evidence.** E.g. a stronger coding-rhythm score, or the learned start signal, required only for calls under 240 nt. That is development work to tune on these genomes, now seen, and then test blind (lead [G-short]).

## 5. Note K — Euler's 41, Heegner's 163, the near-cube [V]
`dcf-math/notes/Note_Heegner_41_163_v0.1.md`, all values computed:
- n² + n + 41 makes **40 primes**;
- the lucky numbers are **2, 3, 5, 11, 17, 41**, and their 4p − 1 values are the odd Heegner numbers **7, 11, 19, 43, 67, 163**;
- e^(π√d) − 744 lies within 0.22, 2.2 × 10⁻⁴, 1.3 × 10⁻⁶ and **7.5 × 10⁻¹³** of the cubes 96³, 960³, 5280³ and **640320³**;
- e^(π√163) has **12 nines** after the decimal point.

## Record
No predictions graded this round. **284 of 389 passed, plus 3 split.**

## Summary
- **Your mRNA request connects straight to the metal work.** Cells sense iron through an iron–sulfur protein that, when iron runs low, grabs a small hairpin on the mRNAs of the iron genes. I built a scanner that finds that hairpin from sequence alone (false-hit rate about 1 in 200,000 bases) and froze its test before any mRNA was downloaded. One link fetches all 15 mRNAs: 7 known iron-hairpin genes and 8 controls.
- ***Chloroflexus*'s weak precision comes from short gene calls** that the finder allows in GC-rich genomes. Simply cutting them would lose real genes elsewhere, so they need their own evidence.
- **The solid core of your 41 idea is now a self-contained note.** Euler's 41, Heegner's 163 and the near-cube e^(π√163) are one theorem, with 5 in the same family.

## Potential leads for future research
- **[IRE]** Grade R1–R3 when `blind_mrna1.zip` arrives.
- **[IRE-wide]** If the scanner passes, run it over a larger set of human mRNAs (hundreds, fetched by gene list) to look for IRE-like hairpins in genes not yet known to carry one. Pre-register the threshold and the follow-up checks first. This is where a genuine discovery could come from.
- **[mRNA-41]** Pre-register Gary's 41/401/153 periodicity on ≥ 500 mRNAs (coding parts and UTRs separately).
- **[G-short]** A short-call filter for GC > 0.55 genomes, developed on *Chloroflexus*, *Dehalogenimonas* and *Haloarcula*, then tested blind.
- **[Fe-ladder note]**, **[Island-ladder]** carried from L3241.
