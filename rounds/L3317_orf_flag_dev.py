# development (graded data reused): flag 'start may be early' if the first ATG is followed by another in-frame ATG within N codons
exec(open('/home/claude/L3313/grade_orf.py').read().split('n=eA=eK=')[0])
for N in (5,10,20,40):
    tp=fp=over=ok=0
    for g,(_,s) in genes.items():
        a=O.orf_A(s); c=[p for p in byend.get(a[-25:],[]) if a.endswith(p)]
        if not c: continue
        P=max(c,key=len); flag='M' in a[1:N+1]
        if len(a)>len(P): over+=1; tp+=flag
        else: ok+=1; fp+=flag
    print("N=%2d codons: flags %d of %d early starts (%.0f%%), and %d of %d correct ones (%.1f%%)"%(N,tp,over,100*tp/over,fp,ok,100*fp/ok))
