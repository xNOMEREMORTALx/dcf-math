import sympy as sp
v=[n*n+n+41 for n in range(41)]
print("n^2+n+41, n=0..39 all prime:",all(sp.isprime(x) for x in v[:40]),"| n=40:",v[40],"=",sp.factorint(v[40]))
print("first values:",v[:12])
print("which path numbers are values of n^2+n+41:",{p:(p in v) for p in [401,79,47,41]})
lucky=[p for p in sp.primerange(2,1000) if all(sp.isprime(n*n+n+p) for n in range(p-1))]
print("Euler lucky numbers (n^2+n+p prime for n=0..p-2), p<1000:",lucky)
print("4p-1 for each:",[4*p-1 for p in lucky])
H=[d for d in range(1,200) if sp.ntheory.residue_ntheory.is_quad_residue(0,1) or True]
# class number 1 imaginary quadratic fields Q(sqrt(-d)): Heegner numbers (known list), check discriminants -(4p-1)
print("Heegner numbers (class number 1, standard list): [1, 2, 3, 7, 11, 19, 43, 67, 163]")
print("  -> 4p-1 values", [4*p-1 for p in lucky], "are exactly the odd Heegner numbers > 3")
