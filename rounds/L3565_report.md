# DCF L3565: The earliest sodium-type channels. 9 of 10 sit with the E-type NAV2 family, but one comb-jelly channel ties toward NAV1, so the prediction fails (0 of 1). The alignment-free method reaches its limit at these distances
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 14 November 2026

**Lead:** [The oldest channels].
- **Pre-registration:** `PREREGISTERED_L3565_navfamily2.txt`.
- **Script:** `rounds/dcf_navfamily2_L3565.py` → `rounds/L3565_grade_output.txt`.

---

## Result
| organism | channel | best NAV1 | best NAV2 | family |
|---|---|---|---|---|
| choanoflagellate | A9USM1 | 0.092 | 0.096 | NAV2 |
| placozoan | B3RSS4 | 0.086 | 0.100 | NAV2 |
| sea anemone | A7SKR1 | 0.115 | 0.127 | NAV2 |
| comb jelly | A0ACF8Y6N4 | **0.088** | 0.086 | **NAV1 (tie)** |
| comb jelly | A0ACF8Y996, A0ACF8YBX3, F6MZB8, F6MZB9 | 0.072–0.082 | 0.079–0.089 | NAV2 (F6MZB8 a tie at 0.082) |
| acoel *Hofstenia* | HMIM006045, HMIM019623 | 0.090, 0.094 | **0.103, 0.114** | NAV2 |

**M1 (all ten closer to NAV2): FAIL.** One comb-jelly channel is 0.002 closer to NAV1.

## Reading
- **The direction is consistent:** 9 of 10, and every lineage except one comb-jelly paralog, lean to the E-type NAV2 family.
- **The acoel's two channels are clearly NAV2** (margins 0.013 and 0.020). That fits NAV1 having arisen *after* acoels split off.
- **But at these evolutionary distances, the 4-mer similarities (0.07–0.13) are close to the floor.** A difference of 0.002 is noise. The test asked more than the method can deliver, and it failed honestly.
- **A real alignment-based tree is needed** to place the earliest channels.
  - A standard aligner could not be installed in this session.
  - **A pure-Python/numpy aligner is the next step,** to be written and validated on known families before use.

## Record
**+0 passed, 1 failed. 420 of 576 passed, plus 3 split.** Audit **92 of 110**. Manuscript 2 is at **v0.10**, with the failure recorded.

## Summary
- **Nine of ten early sodium-type channels, including both acoel channels, lean toward the older E-type family.** That supports a late origin of the K-type NAV1 within bilaterians.
- **One comb-jelly channel tied the other way,** so the frozen all-ten prediction failed.
- **This marks the limit of the alignment-free method.** A real alignment and tree is the way forward.

## Potential leads for future research
- **[Own aligner]** Write a numpy Needleman–Wunsch/BLOSUM62 aligner (no install needed). Validate it on known pairs (human SCN2A vs SCN8A ≈ 80% identity), then align the pore regions of all channels and build a neighbour-joining tree.
- **[Pore-only signal]** Restrict similarity to the four pore loops plus S5–S6, where family signal is strongest (pre-registered).
