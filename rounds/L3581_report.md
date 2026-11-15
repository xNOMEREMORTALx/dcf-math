# DCF L3581: Naming the comb jelly's 123 potassium channels. The global aligner is not reliable when lengths differ greatly; a local aligner is needed first
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 15 November 2026

**Lead:** [Comb jelly's 123 K channels]. Descriptive. **No predictions graded.**

---

## What was tried (`rounds/L3581_cteno_k_names.py`, `rounds/L3581_cteno_k_names_out.txt`)
**The setup:** each of the comb jelly's 141 distinct K/K2P/HCN-called sequences was aligned with `dcf_align` against mouse and fly channels, and named by its nearest one.

**Two attempts, both failed:**
1. **Identity over aligned columns** (the L3569 measure). Almost every comb-jelly channel's "nearest" was **Kcne2/Kcne3**, tiny accessory peptides of about 100 aa. A global alignment of a 500-aa protein to a 100-aa one leaves few aligned columns, which inflates identity.
2. **Excluding short accessory proteins, and dividing identities by the shorter length.** The bias flipped: 130 of 141 were "nearest" to fly **Shab** (a long ~900-aa channel), **including 17 of the 18 K2P leak channels.** K2P channels are not Shab, so this naming is wrong.

## Conclusion
- **Global alignment with simple identity is reliable only between proteins of similar length and architecture.** That condition held in L3569 (sodium channels against sodium channels) and L3577 (K channels against K channels, similar lengths). It **fails** when a query is compared with references of very different lengths.
- **No naming result for the comb jelly is reported.**
- **The earlier, pre-registered results stand,** because their comparisons were length-matched:
  - L3569's NAV families: all ~1,450–2,050 aa;
  - L3577's six named zebrafish channels agreed with NCBI's own descriptions.

**The fix:** a **local** aligner (Smith–Waterman, best-matching region only), or alignment restricted to the shared pore domain (S5–P–S6). Either must be validated before any more naming.

## Record
No predictions graded. **423 of 579 passed, plus 3 split.**

## Summary
- **Naming the comb jelly's potassium channels by global alignment did not work:** first tiny accessory peptides, then one long channel, absorbed most of the matches. Both are artifacts of comparing proteins of very different lengths.
- **No naming is claimed.** The aligner's earlier, length-matched results are unaffected.
- **A local aligner is the next tool to build.**

## Potential leads for future research
- **[Local aligner]** Smith–Waterman in numpy (the same row trick, with a floor at 0). Validate it on K2P vs Kv vs Shab examples with known families, then rerun this naming as a pre-registered test.
- **[Pore-domain extraction]** Cut each channel to its pore domain (from the filter motif ±120 aa) before aligning.
