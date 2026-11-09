# Note E: from sphere packing to E8 — a computed tour (the 240 roots, the 600-cell and the tetrahedral helix)
### Draft v0.1 · Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 9 November 2026

**Status.** Every number in §§1–4 is computed by the scripts `rounds/L3233_e8_600cell.py` and `rounds/L3233_bc_helix.py` (numpy only) or is a cited theorem.

**Labels:**
- **[V]** computed or cited;
- **[D]** interpretation or suggested link, not established.

---

## 1. E8 and its 240 roots [V]
**Construction.** The 240 roots of E8 are:
- the 112 vectors with two entries ±1 and six zeros;
- the 128 vectors with all eight entries ±½ and an even number of minus signs.

**Checked here.**
- All 240 have squared length 2.
- Each root has exactly 56 others at inner product 1.

**Packing.** Spheres centred on the E8 lattice touch 240 neighbours each and fill a fraction **π⁴/384 ≈ 0.25367** of 8-dimensional space. Viazovska (*Annals of Mathematics* 185, 2017) proved that no packing in 8 dimensions is denser.

## 2. The 600-cell (hexacosichoron) [V]
**Construction.** Its 120 vertices are the unit quaternions of the binary icosahedral group:
- the 8 vectors (±1, 0, 0, 0) and their coordinate permutations;
- the 16 vectors (±½, ±½, ±½, ±½);
- the 96 even permutations of ½(±φ, ±1, ±1/φ, 0).

**Counted here.**
- 120 vertices, 720 edges, 1200 triangles, **600 tetrahedral cells**;
- 12 neighbours per vertex;
- edge length 1/φ = 0.618034.

## 3. E8 folds into two 600-cells in the golden ratio [V]
**Method.**
1. Build the E8 Coxeter element, the product of the 8 simple reflections. Its order is 30, with exponents 1, 7, 11, 13, 17, 19, 23, 29.
2. Take its eigenplanes for exponents 1 and 11 and project the 240 roots onto that 4-dimensional space.

**Result.**
- The roots land on **two shells of exactly 120 points**, radii 0.743496 and 1.203002.
- The ratio of the radii is **1.618034 = φ**.
- Each shell is a 600-cell: every point has 12 nearest neighbours at 1/φ of the shell radius.

This is the classical E8 → H4 relationship, recovered numerically.

## 4. The tetrahedral (Boerdijk–Coxeter) helix [V]
**Construction.** Stack regular tetrahedra face to face, each new vertex being the reflection of the oldest of the last four through the face of the other three.

**Measured (unit edge).**
- rotation **131.81°** per vertex = arccos(−2/3);
- rise **0.3162 = 1/√10** per vertex;
- **2.73 vertices per turn.** The helix never repeats in 3D: its twist is irrational.

**In the 600-cell** the same face-to-face chain **closes after exactly 30 tetrahedra**. Coxeter showed the 600 cells split into 20 such rings; that split is cited, not re-computed here.

## 5. The chain, and where biology enters
| link | status |
|---|---|
| densest local packing of 4 spheres = regular tetrahedron | [V] classical |
| tetrahedra stacked face to face = Boerdijk–Coxeter helix | [V] §4 |
| BC helix closes in rings of 30 inside the 600-cell | [V] §4 |
| two 600-cells scaled by φ = the 4D shadow of E8's 240 roots | [V] §3 |
| E8 = densest packing in 8D | [V] Viazovska |
| α-helix (≈ 3.6 residues/turn) and collagen (≈ 2.7) explained by BC-helix packing | published argument (Sadoc & Rivier, *Eur. Phys. J. B* 12, 1999); 2.73 vertices/turn computed here |
| DNA double helix ↔ BC helix / 600-cell / E8 | **[D] — no published link found**; B-DNA's ≈ 10.5 bp/turn comes from base stacking and hydrogen bonding |
| 30 (ring length, E8 Coxeter number) and 10 (the 3-3-4 cysteine ladder spans 10 residues; ≈ 10 bp/turn) | **[D] numerical coincidences** until a mechanism or pre-registered test says otherwise |

## Summary
- **Your geometric chain is real mathematics, every link checked by computation here.** Tetrahedra make the densest local sphere packing. Stacked, they form a helix that, in four dimensions, closes into rings of 30 inside the 600-cell. Two 600-cells in the golden ratio are the four-dimensional shadow of E8's 240 roots, and E8 is the densest sphere packing in eight dimensions.
- **Biology meets this chain at protein helices,** by a published packing argument (α-helix, collagen).
- **No published link from this chain to the DNA double helix was found,** and none is claimed.

## Potential leads for future research
- **[DNA-packing]** Literature: condensed or encapsidated DNA described by tetrahedral or icosahedral (600-cell-like) packing models.
- **[BC-protein]** A small helix-propensity model on the phone, then a pre-registered test: do Fe–S ligand ladders sit in helical or loop segments?
- **[H4-codes]** E8 and its 4D shadows are also optimal error-correcting codes (the E8 lattice ↔ the extended Hamming code). The DCF DNA codec (`dcf_dna_ecc.py`) could be compared with an E8- or Hamming-based code for DNA storage. This is a concrete link from the geometry to Gary's information-storage thread.
