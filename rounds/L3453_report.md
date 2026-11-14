# DCF L3453: New chicken links; the 9-letter rhythm is confined to the voltage sensor (lead closed)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 13 November 2026

## 1. Chicken data
**The problem:** the `refseq/G_gallus/mRNA_Prot` links return "object not found."

**The fix:** the replacement source is the RefSeq **genome-annotation RNA file** for the current chicken assembly, **GCF_016699485.2** (bGalGal1.mat.broiler.GRCg7b). It holds the same kind of NM_/XM_ mRNA records.
- This was recorded as **amendment 2** to the chicken pre-registration **before any chicken data exist here.**
- Predictions, scripts and thresholds are unchanged.

## 2. [Harmonic beyond the motif]: development, descriptive
**Question:** does the 9-letter rhythm of the voltage sensor continue outside the matched stretch? If it did, it would be an independent feature of the DNA, not a consequence of how the windows were picked.

**Method:**
- 403 sensor sites in human and mouse mRNA.
- 45-letter windows at the motif, **90 letters before** it, and **90 letters after** it (no overlap with the motif).
- Power at each period divided by that of 2,745 random coding windows.

| window | period 3 (codon) | period 6 | **period 9** | period 12 |
|---|---|---|---|---|
| 90 letters before | 1.75 | 0.99 | **0.93** | 1.01 |
| **the sensor itself** | 1.86 | 0.89 | **1.95** | 0.77 |
| 90 letters after | 2.30 | 0.67 | **1.00** | 0.75 |

**Reading:**
- **The 9-letter rhythm exists only inside the sensor** (1.95). On either side it falls straight back to background (0.93, 1.00). So it is the charge pattern written in codons, and nothing more: **the lead is closed** as an independent harmonic.
- **What does extend beyond the motif is the 3-letter codon beat.** It is strongest just after the sensor (2.30), where the channel's pore helices follow, matching the strongly periodic codon use of membrane-spanning segments. This is a known general property of coding DNA, and here it is simply visible.

## Record
No predictions graded. **352 of 494 passed, plus 3 split.** C1–C14 are waiting for the chicken file.

## Summary
- **New chicken source:** the RNA file of assembly GCF_016699485.2, recorded as an amendment before any data.
- **The voltage sensor's 9-letter DNA rhythm is local:** strong inside the sensor and absent 90 letters away on either side. It reflects the protein's charge pattern, not a wider DNA harmonic. The lead is closed.

## Potential leads for future research
- **[Chicken]** Grade C1–C14.
- **[Battery balance]** Pump-to-channel gene ratio across life (bacteria → protists → animals).
- **[Codon beat in membranes]** The 3-letter beat is stronger in membrane-spanning stretches. Test whether codon periodicity alone can locate membrane helices label-free (development, then blind).
