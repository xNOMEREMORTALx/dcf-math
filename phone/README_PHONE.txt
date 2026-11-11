DCF phone bundle 6.06, round L3277 (Gary NOMEREMORTAL Mason), 10 Nov 2026.
Copy ALL FIVE .py files into ONE folder on the phone. Pydroid 3: install numpy and mpmath (menu -> Pip). Open dcf_phone_6.06.py and press Run. Self-test: 261/261.
  NEW 30  energy-metal tier of a genome: runs the gene finder if needed, then iron ferredoxin ladder, copper CuA, zinc ribbon -> tier 1-4
          (blind record 14 of 16 fresh genomes, L3269/L3273). Not for medical use.
  NEW 31  number checks: first 1/n containing one or more digit strings (with the base rate: median first n = 71 for 3-digit strings),
          supersingular (Monster) primes, Euler lucky numbers.
  Gene finder updated to v2.32 (was v2.30 in 6.05).
SHA-256:
7df4098f3a8208dede404d9d18e86d71efdbdb1a4ed801940e3125b292bd6474  dcf_phone_6.06.py
4aecee5c25d09f1f3d634e274037643174af1c419f561c1c4e49c86f50d1a7d1  dcf_redox.py
fa30258bd3e19c1a186f225ebb8b50f4993530948f4ffa50644d37d92930297c  dcf_genefinder_mobile.py
dca12b53e5358f6dcf99c8f261e27f8ffff0c563878bc8eefb81dee486fc4e49  dcf_dna_codec.py
dd583cfb386dc71f847db8bb137fb41903ce109b3f6e18730ef85d4a220e95ed  dcf_dna_ecc.py
dcf_phone_6.05.py is kept for reference.

DCF phone bundle, round L3013 (Gary NOMEREMORTAL Mason, Digital Cosmos Framework), 5 Nov 2026.
Copy ALL four .py files into ONE folder on the phone. Pydroid 3: install numpy and mpmath (menu -> Pip).
Open dcf_phone_6.05.py and press Run. Self-test: 257/257.
  25 DNA view of 1/p (base-4 Midy = Watson-Crick)    26 gene finder on a genome file    27 DNA storage
  28 NEW: theorems L2422-L2848 (reduction clock P3, casting out 10^q-1, Dedekind variance, 2-5 lemma, Note B, Theorem R)
Gene finder v2.30 (learned start window 30 nt; blind S. epidermidis exact starts 92.0%, L3013); v2.29 (learns each genome's own start signal: Bacteroides exact starts 52 -> 70%, E. coli 79 -> 85%, L3001); v2.28 (start search extended back to the previous stop: E. coli exact starts 63% -> 79%, L2993); v2.27 (best-start scoring for every genome's final gene calls, ORF minimum 240 nt; code detection back to v2.25, which restores Hodgkinia, L2973); v2.26 (GC-rich genomes > 0.55: each ORF scored from its best start codon and ORFs >= 180 nt; held-out Streptomyces 74.5 -> 94.9% found, Deinococcus 82.9 -> 93.3%, L2969); v2.25 (tiny AT-rich genomes < 300 kb, GC < 0.25: the length ratio with cut 1.45 decides TGA = Trp, L2957); v2.24 (adds the repeat flag and fixes the minus-strand bug in the codon-phase line, L2921; helical rhythm L2913; calls unchanged); v2.21: + stem-loop scan with a dinucleotide null for genomes < 100 kb (mitochondria), mitochondrial stop note.
SHA-256:
dca12b53e5358f6dcf99c8f261e27f8ffff0c563878bc8eefb81dee486fc4e49  dcf_dna_codec.py
dd583cfb386dc71f847db8bb137fb41903ce109b3f6e18730ef85d4a220e95ed  dcf_dna_ecc.py
6b26c0324bdead98547f26bb0dc3d00c2ad60974fb166b184cf203b99b5d5022  dcf_genefinder_mobile.py
a5ab407aa6a81d518e6de310cf1fdd3ab79c5f228c8ed2e7ea639dcd32409fb0  dcf_phone_6.05.py

L2853 (phone 5.87): new menu 29 "Gary's reduction in any base + the period clock".
Type 1/7 (or any 1/p) and a base: steps, carries (Lemma C1), first-half sum mod b-1 (Theorem C3_b),
three-phase sums (dark frequencies: 1/277 gives 108, 108, 108). Or type a whole number for Theorem R_b.
Self-test: 256/256 (19 new rows).

L2858 (phone 5.88): 2 new rows: the (10w-1) lattice lemma for the three-phase sums, and the new balanced primes 1/287449 and 1/333667. 257/257.
L2866 (phone 5.89): lattice lemma in any base/order (lattice_check), and the free mod-63 check of reciprocal DNA strands (strand_check_mod63). 257/257.
L2871 (phone 5.90): deletion theorem for the mod-63 tag check, tag_rotate() removes the leading-A blind spot. 257/257.
L2875 (phone 5.91): tag_rotate_v2 (no leading/trailing A blind spots), tag_check_full (known-address check), mod 4^9-1 check for 9 | T. 257/257.
L2879 (phone 5.92): agreement_lambda(c) and word_agreement(p, c): why reciprocal tag sets have d_min/T -> 3/5. 257/257.
L2883 (phone 5.93): ratio_free_library(p, K). 257/257.
L2887 (phone 5.94): agreement_lambda_b(c, b), the proved agreement law in any base. 257/257.
L2892 (phone 5.95): agreement_lambda_rs(r, s, b), the law for fraction multipliers. 257/257.
L2896 (phone 5.96): lambda_symmetric(r, s, b) and the global-maximum check. 257/257.
L2901 (phone 5.97): normality_lambda_test(digits). 257/257.
L2909 (phone 5.98): rna_strand(p) (1/p as RNA + translation), share_5_divides_period(). 257/257.
L2925 (phone 5.99): vogel_records(beta): golden-spiral record approaches (Fibonacci, F_3k/2, pentagon 3, 11, 244, 1231, ...). 257/257.
L2929 (phone 6.00): fib_ladder(m), phi_power_share(n). 257/257.
L2933 (phone 6.01): agreement_lambda_neg(c), phi_inverse_power_share(n). 257/257.
L2937 (phone 6.02): lambda_closed(r, s, b, complement): closed form and proof of the 2/(b+1) maximum. 257/257.
L2941 (phone 6.03): block_share(c, k), affine_share(r, s, t). 257/257.
L2957 (phone 6.04): silver_power_share(n): delta = 1 + sqrt 2 shares lambda(P_n) of its decimals with delta^n (Pell numbers). 257/257.
L2977 (phone 6.05): power_share(rel, m, n): digit sharing of any two powers of a root of x^d = rel[0] + ... (phi [1,1], silver [1,2], plastic [1,1,0]). 257/257.
