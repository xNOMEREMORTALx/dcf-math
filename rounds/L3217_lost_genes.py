import sys, re
def gff(p):
    return [(int(f[3]),int(f[4]),1 if f[6]=='+' else -1) for f in (l.split('\t') for l in open(p)) if len(f)>6 and f[2]=='CDS']
def ann(gb):
    t=open(gb).read(); return [(int(m.group(2)),int(m.group(3)),-1 if m.group(1) else 1) for m in re.finditer(r'\n     CDS             (complement\()?<?(\d+)\.\.>?(\d+)\)?\n',t)]
def covered(x,P):
    a,b,s=x
    return any(t==s and c<=b and d>=a and min(b,d)-max(a,c)+1>=0.5*(b-a+1) for c,d,t in P)
gb,o,n=sys.argv[1:4]; A=ann(gb); O=gff(o); N=gff(n)
lost=[x for x in A if covered(x,O) and not covered(x,N)]
gain=[x for x in A if covered(x,N) and not covered(x,O)]
print(gb.split('/')[-1],"preds v2.31 %d v2.32c %d; annotated genes lost %d gained %d"%(len(O),len(N),len(lost),len(gain)))
# for each lost gene: what does v2.32c have there? overlapping predictions on either strand
for x in lost[:12]:
    a,b,s=x
    po=[p for p in O if p[0]<=b and p[1]>=a and p[2]==s]
    pn=[p for p in N if p[0]<=b+300 and p[1]>=a-300]
    print("  ann",x,"len",b-a+1,"| v2.31",po,"| v2.32c near",pn)
