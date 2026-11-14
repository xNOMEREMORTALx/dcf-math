# DCF L3425: Metals and the nervous system. Nerve channels sorted by the ion they pass (potassium, sodium, calcium) from raw mRNA; a new two-pore potassium "leak" channel finder; blind test on mouse files 3–4 frozen and waiting
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 13 November 2026

**Leads:** [Neuro map +] (the sodium/calcium split), [Neuro b] (`k_filter2`), plus Gary's request: potassium, other metals, nervous system, consciousness.
**Status:** development and a frozen check on files already opened. **No predictions graded;** the counted test needs mouse files 3 and 4.

---

## 1. The idea: each channel's "gate" is built for one metal ion
A nerve impulse is metal ions crossing the membrane in a fixed order:
1. **sodium (Na⁺)** rushes in and fires the spike;
2. **potassium (K⁺)** flows out and resets it;
3. **calcium (Ca²⁺)** enters at the synapse and releases the neurotransmitter.

Each channel has a narrow **selectivity filter**, a short loop of protein that fits one ion. These loops are short sequence motifs, so the DCF tools can read them straight from mRNA:

| ion | filter in the protein | how it reads in sequence |
|---|---|---|
| **K⁺** | the T-V-G-Y-G loop: backbone oxygens set exactly to a K⁺ ion's size | `[TSC][VITL]G[YF]G` (`k_filter2`) |
| **Na⁺** | the "DEKA" ring: one residue from each of the 4 domains, D, E, **K (lysine)**, A | lysine loop `[TS][FY][KR][GA]W`, with **at most 1** acidic loop |
| **Ca²⁺** | the "EEEE" ring: an acidic E or D in **all four** domains (T-type: EEDD) | the calcium ring `[TS]x[ED]xW`, counted **≥ 3** times |

## 2. The calcium ring (new, development on human files 1–4)
The four pore loops of each 4-domain channel, read from the tool's output:

| channel | loop I | loop II | loop III | loop IV | ring count |
|---|---|---|---|---|---|
| CACNA1B (N-type Ca) | TM**E**GW | TG**E**DW | TG**E**GW | TG**E**AW | 4 |
| CACNA1G (T-type Ca) | TL**E**GW | TQ**E**DW | SK**D**GW | TG**D**NW | 4 |
| SCN2A (brain Na) | TQ**D**FW | CG**E**W (no T/S) | TF**K**GW | TS**A**GW | 1 |

- **The motif recovers the textbook rings:** EEEE in the high-voltage Ca channels, EEDD in the T-type, and DEKA in sodium.
- **Across all 9,632 human genes,** only 16 proteins have the calcium ring 3 or more times. The 4-domain gate (≥ 1,500 aa, with a voltage sensor) leaves only the true calcium channels.

## 3. The frozen rule and what the frozen check found
**v1 (frozen first).**
- **Human files 1–4 (development):** 22 of 22 channels got their own metal class.
- **Mouse files 1–2 (frozen check; opened before, not counted):**
  - **Calcium:** 6 of 6 correct.
  - **Potassium/HCN:** 15 of 15 correct.
  - **Sodium:** 3 of 4. **Brwd3,** a large non-channel protein with a chance voltage-sensor match, was called sodium.
  - **A header bug:** the gene name was taken from the **first** bracket. Every mouse Kcnh gene's description contains "(eag-related)", so they all merged under one name.

**v2 (amendment A1, frozen before the blind files).**
- Sodium now also needs the **lysine loop**, the K of DEKA.
- The gene name is taken from the **last** bracket.
- **On mouse 1–2** (now development):
  - **Precision:** 27 of 27 calls correct (6 Ca, 3 Na, 17 K, 1 HCN).
  - **Recall:** 27 of 36 family genes found.
  - **The misses:** Kcnq (whose voltage sensor has only four charges), Kcng (silent subunits), three Kcnh, and Scn7a (Naₓ, a sodium *sensor*, not a spike channel).

**The blind test will run v1 and v2 side by side** (8 predictions, N1–N4 for each).

## 4. Potassium "leak" channels, a link to consciousness (amendment A2)
- **What K2P channels are:** "two-pore" potassium channels. They have **no voltage sensor and two K⁺ filters**, and leak K⁺ steadily to hold the neuron at rest.
- **Why they matter for consciousness:** the TREK and TASK members are opened by **general anaesthetics** (e.g. isoflurane), which helps quiet the brain.
- **Rule:** < 700 aa, no S4, and two or more `T[VIT]G[YFL]G` filters.

| set | calls | correct | family found |
|---|---|---|---|
| human 1–4 (development) | 7 | **7 KCNK** | 7 of 9 |
| mouse 1–2 (frozen check, not counted) | 7 | **7 Kcnk** | 7 of 11 |

- **Precision is perfect in both sets.**
- **Recall on mouse 1–2 (64%) is below the 70% bar set for the blind test.** This is a warning that N6 may fail.
- **The second filter usually ends G-F-G-D or G-L-G-D,** a two-filter rhythm that tells K2P channels apart from all other K⁺ channels.

## 5. Other metals in the nervous system (background, not tested here)
| metal | role in nerves | DCF status |
|---|---|---|
| **Zn²⁺** | packed into glutamate vesicles (ZnT3) and released at synapses; tunes NMDA receptors | zinc-ribbon/C2H2 presets exist; no neuro test yet |
| **Mg²⁺** | plugs the NMDA receptor at rest (the learning "coincidence detector") | no motif yet |
| **Fe** | tyrosine and tryptophan hydroxylases make dopamine and serotonin; myelin-forming cells are iron-rich | lead [Neuro iron] |
| **Cu** | dopamine β-hydroxylase makes noradrenaline (alertness) | CuA preset is for respiration, not this site |

**On consciousness, honestly:**
- **No sequence motif measures consciousness.**
- **What we *can* map** is the metal machinery whose state changes with it:
  - **T-type calcium and HCN channels** drive the thalamus–cortex rhythms that differ between waking and sleep;
  - **K2P leak channels and GABA-A receptors** (a Cys-loop family) are where anaesthetics act.
- **All of these are now findable label-free** (sections 2–4).

## 6. Action for Gary: two mouse files for the blind test
1. https://ftp.ncbi.nlm.nih.gov/refseq/M_musculus/mRNA_Prot/mouse.3.rna.fna.gz
2. https://ftp.ncbi.nlm.nih.gov/refseq/M_musculus/mRNA_Prot/mouse.4.rna.fna.gz

Each is a compressed file of a few tens of MB. **Keep the names `mouse.3.rna.fna.gz` and `mouse.4.rna.fna.gz`;** don't unzip them. Zip both together as **`mouse_rna_3_4.zip`**. If a link doesn't work, tell me. A missing file is dropped, not replaced.

## Files
- **Scripts:**
  - `rounds/dcf_neurometal_L3425.py` (v1, `ca04afbb…`);
  - `rounds/dcf_neurometal_L3425_A1.py` (v2, `aae28b5e…`);
  - `rounds/dcf_k2p_L3425.py`.
- **Pre-registrations:** `preregistrations/PREREGISTERED_L3425_neurometal.txt`, plus amendments A1 and A2. All hashes are in `LEDGER.md`.
- **Outputs:**
  - `rounds/L3425_human_dev.txt`;
  - `rounds/L3425_mouse12_tool.txt` (committed before names), `rounds/L3425_mouse12_grade.txt`;
  - `rounds/L3425_A1_dev_*.txt`;
  - `rounds/L3425_k2p_*.txt`.

## Record
No predictions graded. **325 of 463 passed, plus 3 split.** Ten predictions are pre-registered and waiting: N1–N4 for v1 and for v2, plus N5–N6.

## Summary
- **Nerve channels can be sorted by the metal ion they carry, from raw mRNA:** K⁺ by the T-V-G-Y-G filter, Na⁺ by the DEKA lysine, Ca²⁺ by an acidic ring in all four domains. On the development and frozen-check data, every call made was correct (27 of 27 in mouse with v2).
- **The frozen check caught two faults before the blind test,** a false sodium call and a gene-name bug. Both are fixed in a frozen amendment, and the original version is still graded alongside it.
- **The potassium leak channels that anaesthetics act on** are found with perfect precision but incomplete recall.
- **Consciousness cannot be read from sequence,** but the metal machinery it depends on now can be.

## Potential leads for future research
- **[Mouse 3–4]** Grade N1–N6 when the files arrive.
- **[Kcnq]** Kv7 (M-current) channels have a 4-charge voltage sensor. Develop a Kv7-specific signature.
- **[Neuro iron]** Map iron-using brain enzymes (tyrosine/tryptophan hydroxylase, the 2-His-1-carboxylate iron site), linking the iron ladder work to neurotransmitter synthesis.
- **[NMDA metals]** Find the Mg²⁺-block asparagine (N-site) and the zinc site of glutamate receptors label-free.
- **[Phone]** Add `neurometal` and `k2p` as menu options on the phone after the blind test.
