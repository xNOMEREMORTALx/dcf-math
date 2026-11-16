# Reader brief: "Reading the metal chemistry of nervous systems from sequence alone"
### Gary NOMEREMORTAL Mason (ORCID 0009-0008-9235-4493) · draft v0.17 · code and data DOI 10.5281/zenodo.24234795

**What it claims, in one paragraph.**
- **The rules:** a handful of short, readable sequence rules sort nerve channels and pumps by the metal ion they pass (K⁺, Na⁺, Ca²⁺, Cu), straight from mRNA or protein. The rules read the selectivity loops: T-V-G-Y-G, the DEKA lysine, the EEEE/EEDD calcium ring, and the P-E-G-L pump loop.
- **How they were tested:** every rule was hashed and frozen before each blind test, and tool output was committed before any label was read.
- **The results:**
  - **overall:** **139 of 165 pre-registered predictions passed** in 26 blind tests, from protists and sponges to vertebrates (mouse, zebrafish, chicken, fruit fly, nematode, all other animals in Swiss-Prot, ~25,000 TrEMBL channels, early animals, and single proteomes of 20+ invertebrates);
  - **against UniProt's independent classification:** 345 of 351 calls agree.
- **Newer findings (v0.15–v0.17):**
  - the NMDA receptor's NR1 subunit first appears in cnidarians (§3.15);
  - loss of the sodium channel is lineage-specific (nematodes, tardigrades), not size-driven (§3.16);
  - the NALCN leak channel moves its sodium-like lysine between domain II and domain III across bilaterians, tested against a published splicing study (§3.19).
- **What the work also traced:** the fast sodium channel's DEKA lysine is absent in every non-bilaterian and in acoels, sea urchins and acorn worms. Alignment places their channels in the older NAV2 family.

**What I would like from you (three questions).**
1. Is any biological claim wrong or overstated? See especially §3.9 (E→K history), §3.11 (comb-jelly Shaker expansion), §3.16 (sodium loss twice) and §3.19 (NALCN rings).
2. Is the pre-registration convincing? The ledger, the hash-before-data rule, and the "failures stand" rule (all 26 failures are listed, plus two grading issues disclosed in §3.17).
3. Should this be one paper or two (a methods paper, and an evolution paper on E→K, NR1, sodium loss and NALCN)? Which journal would fit? Candidates: Genome Biology and Evolution, Molecular Biology and Evolution (brief communication), PeerJ.

**Where everything is.**
- **Draft:** `notes/Manuscript_nerve_metals_draft_v0.17.md` (nine figures in `figures/`; publication-resolution copies in `figures/publication/`).
- **Every test:** `preregistrations/` (frozen texts and LEDGER.md) and `rounds/` (reports and grade outputs).
- **Tools:** dcf-genefinder (DOI 10.5281/zenodo.24234986): `dcf_nerve.py`, `dcf_pump.py`, `dcf_align.py`, `dcf_localalign.py`.

**Known limits** (stated in the draft):
- Silent K subunits, divergent K2P channels and insect IR receptors are missed.
- Name-based truth rules undercounted correct calls in early tests.
- Alignment-free family calls lose power at deep distances (one failed test).
- Global alignment is biased when lengths differ (fixed with a local aligner).
- UniProt lists usually one isoform per gene, so a missing splice variant is weak evidence (§3.19).
- Nothing here measures consciousness; the "excitability kit" is a parts list.
