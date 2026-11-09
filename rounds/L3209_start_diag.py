import sys, importlib.util, collections
spec=importlib.util.spec_from_file_location('g','/home/claude/tools/dcf_grade.py'); g=importlib.util.module_from_spec(spec); spec.loader.exec_module(g)
def load(gff):
    P={}
    for l in open(gff):
        f=l.rstrip('\n').split('\t')
        if len(f)>6 and f[2]=='CDS':
            a,b,s=int(f[3]),int(f[4]),1 if f[6]=='+' else -1
            P[((b if s==1 else a),s)]=(a,b)
    return P
gb,dcf,prod=sys.argv[1:4]
seq,cds=g.read_gb(gb); D=load(dcf); Pr=load(prod)
up=dn=ok=0; codon=collections.Counter(); dist=[]; both_wrong=dcf_only=0
for a,b,c in cds:
    s=-1 if c else 1; key=((b if s==1 else a),s)
    if key not in D: continue
    da,db=D[key]; ann=a if s==1 else b; pr=da if s==1 else db
    d=(ann-pr) if s==1 else (pr-ann)   # >0: prediction starts upstream (longer) of annotation
    if d==0: ok+=1
    else:
        dist.append(d); up+= d>0; dn+= d<0
        p=Pr.get(key); pp=(p[0] if s==1 else p[1]) if p else None
        if pp==ann: dcf_only+=1
n=ok+up+dn
import statistics
print(gb.split('/')[-1],"n=%d exact=%.1f%% wrong-upstream(too long)=%d wrong-downstream(too short)=%d; of DCF errors, Prodigal exact in %d (%.0f%%); median |shift| %d nt"%(n,100*ok/n,up,dn,dcf_only,100*dcf_only/max(1,up+dn),statistics.median(abs(x) for x in dist)))
# codon of annotated vs chosen start, for too-short errors
L=len(seq); comp=str.maketrans('ACGTN','TGCAN')
def cod(pos,s):
    return seq[pos-1:pos+2] if s==1 else seq[pos-3:pos].translate(comp)[::-1]
C=collections.Counter()
for a,b,c in cds:
    s=-1 if c else 1; key=((b if s==1 else a),s)
    if key not in D: continue
    da,db=D[key]; ann=a if s==1 else b; pr=da if s==1 else db
    d=(ann-pr) if s==1 else (pr-ann)
    if d<0: C[(cod(ann,s),cod(pr,s))]+=1
print("  too-short errors, (annotated codon -> chosen codon):",C.most_common(6))
