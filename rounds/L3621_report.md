# DCF L3621: A second tardigrade confirms channel loss (2 of 2). Its channels-per-pump ratio is 1.53, and it has no voltage-gated sodium channel, only the NALCN leak channel
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 15 November 2026

**Data:**
- **The file:** Gary's `29.gz`, saved as `L3621/z/tard.tsv.gz`.
- **Contents:** 22,945 UniProt proteins of *Ramazzottius varieornatus*, the only organism in the file.

**Procedure:**
1. **Frozen files:** the pre-registration (`PREREGISTERED_L3617_aplysia_tardigrade.txt`, part B), `dcf_battery_L3609.py` and `dcf_nerve_v2_L3549.py`. All three hashes matched the ledger.
2. **Tool output:** `rounds/L3621_tool_output.txt`. It read only Entry and Sequence, and was committed and pushed before any protein name was read.
3. **Grading:** `rounds/L3621_grade_output.txt`.

---

## Results
| # | prediction | result |
|---|---|---|
| **T1** | channels / metal pumps < 1.8 | **23 / 15 = 1.53, PASS** |
| **T2** | no DEKA (voltage-gated Na) call | **0 calls, PASS** |

**The two tardigrades agree closely:** *Hypsibius* 1.54 (L3613), *Ramazzottius* 1.53. Both sit inside the non-neural range (0.05–1.60), even though tardigrades have a brain and nerve cords.

## Descriptive, after grading
**What the tool called** (with UniProt names):
- **Pumps:**
  - Na⁺/K⁺ pumps: 6, all named Na/K ATPase;
  - Ca²⁺ pumps: 8, all named Ca ATPase;
  - Cu pumps: 1, a P-type Cu⁺ transporter.
- **Channels:**
  - Ca: 2. The two entries have identical alignment scores, so they are probably one Cav2 gene listed twice.
  - Ca T-type: 1, nearest mouse Cacna1h.
  - K: 15. These include KQT (Kv7), the BK channel and several BTB-domain (Kv-type) channels.
  - K2P: 5, all "Potassium channel domain".
- **Other finders:**
  - iGluR: 10, all "ionotropic glutamate receptor";
  - iron hydroxylases: 7 true (PAH ×5, **tryptophan 5-hydroxylase 2**, an AAAH domain) plus **1 false** (dipeptidyl peptidase 3).

**Is a sodium channel hiding?** Every protein of 1,000 aa or more was searched for a domain-III loop of type [TS][FY][K/R/E][GA]W.
- **A0A1D1UFD6 (1,748 aa) carries S-F-K-G-W.** Its nearest mouse match is **Nalcn**, by a wide margin (score 4,573, against 482 for the next match). NALCN is the sodium *leak* channel that sets resting potential, not the spike channel. It has no full S4 voltage sensor, so the tool's gate excluded it correctly.
- **A0A1D1UR64 carries T-F-E-G-W, but it is an L-type calcium channel.** Mouse Cacna1c, Cacna1d and Cacna1s carry the same T-F-E-G-W loop.
- **No NAV1 or NAV2 channel was found.** On this evidence the tardigrade fires without voltage-gated sodium channels.

**Real misses** (not graded):
- **2 L-type calcium channels (Cav1) were not called.** One is a 1,238-aa fragment with 2 S4 sites. The other has no S4 match under the strict pattern.
- **The tardigrade therefore has all three calcium-channel families (Cav1, Cav2, Cav3),** while the tool caught only Cav2 and Cav3.

**Caution for the E→K story (L3557):**
- **T-F-E-G-W is also the normal L-type calcium-channel loop.**
- **The ancestral "E" pore loop counts only when the protein is a sodium channel by alignment (NAV2 family).** The earlier rounds identified those proteins as sodium channels by alignment, so they stand, but any future motif-only use of T-F-E-G-W must exclude Cav1.

## Reading
- **Tardigrades are a nervous system running on a small battery.** Their ratio, 1.5 channels per pump, is like that of a sponge or a choanoflagellate.
- **Tardigrades have no voltage-gated sodium channel.** Their impulses would then have to rely on calcium channels, as in the nematode (L3473).
- **Both independent tardigrade proteomes agree,** so the L3613 "exception" is a real biological pattern, not noise.
  - **The neural/non-neural battery cut of 1.8 has one consistent exception class:** miniaturised animals that lost channels.
  - **A testable thought:** the two lineages without sodium spikes so far (nematodes, tardigrades) are both small, moulting animals (Ecdysozoa).

## Record
**+2 passed. 440 of 599 passed, plus 3 split.** Nerve-chemistry audit **107 of 126.**

## Summary
- **A second tardigrade, tested blind with frozen rules, passed both predictions.**
  - Its battery ratio is 1.53, almost exactly that of the first tardigrade (1.54).
  - It has no voltage-gated sodium channel.
- **The only sodium-lysine protein is NALCN,** a leak channel, which the tool's voltage-sensor gate rightly excluded.
- **Tardigrade nerves likely fire with calcium,** like worm nerves.
- **The tool missed the two L-type calcium channels,** and the T-F-E-G-W loop turns out to be shared with L-type channels. Both are recorded as method limits.

## Potential leads for future research
- **[Ecdysozoa sodium loss]** Pre-register: other small moulting animals that have lost sodium channels (e.g. rotifer-sized nematode relatives, mites) have a ratio below 1.8 and no DEKA. A counter-test: large moulting animals (crab, horseshoe crab) keep NAV1 and have a ratio above 1.8.
- **[Cav1 recall]** The L-type calcium channels slip past the strict S4 rule. Test a calcium rule based on the pore-loop set (T-F-E-G-W plus EEEE) in development, then blind.
- **[NALCN finder]** Add an explicit NALCN call (sodium-lysine loop, no S4) so the leak channel is counted separately in the battery.
- **[NMDA across the tree]** Carried from L3617; the tardigrade's 10 iGluR calls can be sorted by alignment.
- **[Manuscript 2]** Add §3.13 (sea-hare NMDA) and §3.14 (second tardigrade).
