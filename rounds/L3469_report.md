# DCF L3469: The fly failures repaired (v5), an independent truth reference (UniProt), and a pre-registered nematode test with a built-in negative control
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 14 November 2026

**Leads:** [Length-free channels], [HCN route], [Insect K2P], [Iron core], [Truth from sequence]. This is development on all five seen species: human, mouse, zebrafish, chicken, fly. **No predictions graded.**

---

## 1. v5 rules (`rounds/dcf_neurochem3_L3469.py`)
| fly failure (L3465) | v5 change | fly after (development) |
|---|---|---|
| Shab (1,607 aa) misfiled as a 4-domain channel | 4-domain branch needs ≥ 1,500 aa **and** a full voltage sensor **and** (calcium ring ≥ 3 or sodium lysine loop) | Shab → K ✓ |
| Ih (fly HCN) missed | the weak-sensor route accepts the HCN filter C-I-G-Y-G | Ih → HCN ✓ |
| K2P: length cut and filter too strict | < 1,100 aa, two filters [TS]-[TSV]-[IVT]-G-[YFL]-G | Ork1, sand, galene, Task6 found (4 of 5) |
| iron site flanks drifted | core [CVI]-H-E-[LI]-[LM]-G-H | ple, Hn, Trhn: all 3 found, no false hits in any species |
| NMDA motif shared with insect kainate receptors | **NMDA finder dropped**; the iGluR gate is kept | — |

**Development across all five species** (`rounds/L3469_dev.txt`; precision under truth v3):
- **Calcium and sodium:** every call correct in all five species. The added gate removed the large non-channel proteins that a looser test let in.
- **Iron hydroxylases:** every call correct in all five. The only "misses" listed are "trh/TRH" (*trachealess* in fly, thyrotropin-releasing hormone in vertebrates): an **error in my old truth list**, not the tool.
- **K2P:** the new rule adds three uncharacterized fly CG proteins, whose nature is unknown, and one false call in human (NUP98).

## 2. [Truth from sequence] An independent reference
**What changed:** after four rounds where failures came from hand-written name lists, the next test is graded against **UniProtKB/Swiss-Prot "Protein families"**. That is UniProt's curated, sequence-similarity classification, which the DCF did not write (`rounds/dcf_truth4_L3469.py`). For example:
- "Potassium channel family, C (Shaw) subfamily" → K;
- "Two pore domain potassium channel family" → K2P;
- "Cation transport ATPase (P-type) family, Type IIC subfamily" → Na⁺/K⁺ pump;
- "Biopterin-dependent aromatic amino acid hydroxylase family" → iron hydroxylase.

**The recall set counts only voltage-gated potassium families.** Calcium-activated, KCNN and inward-rectifier K channels are left out, because the tool is not built to find them.

## 3. Pre-registered: the nematode *C. elegans* (W1–W12)
- **Why a worm:** it is a new animal lineage, and it has a famous natural test. **Nematodes have no voltage-gated sodium channels at all;** their nerves fire with calcium.
  - **W1 is therefore a negative control:** the tool must call **zero** sodium channels. Any sodium call is a false positive.
- **Data:** UniProt reviewed *C. elegans* entries (TSV). The tool reads only accession and sequence; the family column is used only for grading, after the tool output is committed.
- **Disclosure:** while designing the truth rule I saw the family texts of about 80 reviewed worm channel entries. **No worm sequence has been scanned.**

## Action for Gary: one file
https://rest.uniprot.org/uniprotkb/stream?format=tsv&fields=accession,gene_primary,protein_families,sequence&query=organism_id%3A6239%20AND%20reviewed%3Atrue&compressed=true

It saves as a `.tsv.gz` (or `.gz`). It's small, a few MB. Please don't unzip it.

## Record
No predictions graded. **370 of 521 passed, plus 3 split.** W1–W12 are waiting.

## Summary
- **Every fly failure caused by the tool is repaired in development:**
  - the long potassium isoform is filed correctly;
  - the fly pacemaker channel is found;
  - four of five fly leak channels are found;
  - all three fly iron hydroxylases are found, by the conserved histidine core, with no false hits in any species.
- **The NMDA motif is retired,** because it is not specific outside vertebrates.
- **From now on, the truth comes from UniProt's curated families,** not from name lists I write.
- **The next blind test is a worm,** with a sharp negative control: an animal with no sodium channels should get no sodium calls.

## Potential leads for future research
- **[Worm]** Grade W1–W12.
- **[Retro-grade]** Regrade nothing (the past results stand), but report how the v4 truth would have scored earlier rounds, as a separate descriptive table.
- **[Battery balance]** Pump-to-channel ratios across species, now including the worm.
- **[Manuscript 2]** Add the v5 repair and the independent-truth design to Methods.
