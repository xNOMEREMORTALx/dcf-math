# DCF L3493: The four remaining swaps explained, why sodium channels were missed, Figures 1 and 3 for Manuscript 2, and a pre-registered test of metal gates before nerves
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 14 November 2026

**Leads:** [Four swaps], [Na recall], [Figures 1 and 3], [Before nerves]. This is descriptive work on the graded TrEMBL set (not counted). **No predictions graded.**

---

## 1. [Four swaps] (`rounds/L3493_swaps_recall.txt`)
- **Two duck T-type calcium channels were called sodium.** They carry a perfect EEDD calcium ring (T-L-E-G-W, T-Q-E-D-W, S-K-D-G-W, T-G-D-N-W) and *also* a lysine loop, **S-F-K-G-W**, so lysine-first sent them to sodium.
- **Two ghost-shark proteins named "sodium channel protein" were called calcium.** They have no lysine loop, and they have three ring matches (T-D-E-E-W, T-L-D-Y-W, T-F-E-G-W). *Callorhinchus* is a cartilaginous fish, and these may be unusual sodium-channel homologues; their nature is unknown.
- **Could a ring cut fix the ducks?** I tested "lysine with ring ≥ 4 → calcium" on the same data.
  - **It would fix 2 errors and create 11:** 10 sodium-named proteins have the lysine and ring 4, and 1 has ring 5.
  - **Lysine-first (v7) stays.** That lead is closed.

## 2. [Na recall] Why 657 sodium-named proteins were not called sodium
| reason | count |
|---|---|
| voltage sensor present, **no lysine loop** (ring < 3, so they fell to the 1-domain branch) | 574 |
| no voltage sensor and no lysine loop (fragments or models missing domains) | 64 |
| lysine loop present but **no voltage sensor** | 17 |
| called calcium | 2 |

**By name:**
- **67 are Naₓ** ("type 7 subunit alpha"), the sodium *sensor*, which is known to lack the DEKA lysine. The tool has missed it in every species.
- **572 carry only the generic name "Sodium channel protein".** None of them has the A-T-F-K-G-W loop at all, so they are probably Naₓ-like or incomplete gene models.

The misses are concentrated in one channel type, not scattered.

## 3. Figures for Manuscript 2
- **Figure 1** (`figures/L3493_motif_panel.png`): **the metal-selecting loops read from real sequences in six animals.**
  - **K⁺ filter:** T-V-G-Y-G everywhere.
  - **Sodium lysine:** T-F-K-G-W in every animal that has sodium channels; none in the worm.
  - **Calcium ring:** T-M-E-G-W, T-G-E-D-W, T-G-E-G-W, T-G-E-A-W, identical in human, mouse, fish and fly.
  - **Pump loop:** N-V-P-E-G-L.
  - **Iron core:** C/V/I-H-E-L-L-G-H.
- **Figure 3** (`figures/L3493_battery.png`): **the nerve battery: few chargers, many dischargers.** 4.3, 6.3 and 3.5 channels per metal pump in zebrafish, chicken and fly.

## 4. [Before nerves] Pre-registered (`PREREGISTERED_L3493_before_nerves.txt`)
**Gary's question:** how did nervous systems and their metal chemistry arise? The test uses four organisms at the base of the animal tree:

| organism | what it is |
|---|---|
| ***Monosiga*** (choanoflagellate) | the single-celled relatives of animals |
| ***Amphimedon*** (sponge) | an animal with no nervous system |
| ***Trichoplax*** (placozoan) | no neurons |
| ***Nematostella*** (sea anemone) | one of the first nerve nets |

**Truth:** a pre-stated expectation from the literature on sodium-channel evolution. The DEKA lysine is a bilaterian invention; earlier sodium-channel homologues have DEEA or DKEA rings.

**Predictions:**
- **S1–S4:** zero sodium calls in all four.
- **S5–S6:** calcium channels in the anemone and *Trichoplax*. Calcium signalling predates nerves.
- **S7:** at least 3 potassium channels in the anemone.

## Action for Gary: one file (four proteomes)
https://rest.uniprot.org/uniprotkb/stream?format=tsv&compressed=true&fields=accession,organism_name,protein_name,sequence&query=proteome%3AUP000007879%20OR%20proteome%3AUP000009022%20OR%20proteome%3AUP000001593%20OR%20proteome%3AUP000001357

**If it errors:** search the same text (`proteome:UP000007879 OR proteome:UP000009022 OR proteome:UP000001593 OR proteome:UP000001357`) on uniprot.org and download it as TSV.

## Record
No predictions graded. **396 of 548 passed, plus 3 split.** S1–S7 are waiting.

## Summary
- **The last sodium/calcium errors are understood:**
  - two duck calcium channels carry a stray sodium-like lysine;
  - two shark proteins have no lysine at all.
  
  A ring cut would make things worse, so the rule stays.
- **Missed sodium channels are almost all one type,** the Naₓ sodium sensor and look-alikes without the DEKA lysine.
- **Manuscript 2 now has its three figures:** the motif panel, the blind tests and the battery balance.
- **Next blind test:** the animals at the dawn of nerves. If the lysine is a bilaterian invention, sponges, placozoans, sea anemones and choanoflagellates should get **no sodium calls**, while calcium channels should already be there.

## Potential leads for future research
- **[Before nerves]** Grade S1–S7.
- **[Naₓ finder]** A specific rule for the sodium sensor (its own DIII loop), development then blind.
- **[Manuscript 2 v0.3]** Insert Figures 1–3 and the swap/recall analysis.
