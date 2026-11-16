"""L3653 frozen: NALCN selectivity ring (DI-DIV) per proteome.
NALCN = protein 1300-2600 aa with >= 3 ring words [TS]x[ED]xW whose nearest (local aligner) among mouse Scn2a, Scn8a, Cacna1a, Cacna1c, Cacna1g, Nalcn
is Nalcn with score >= 1000 (standing floor, L3649). Ring residue per domain: ungapped BLOSUM62 window (mouse ring word +-6, 17 aa) best match
within +-300 aa of the proportional position; residue at the word's 3rd place. Mouse Nalcn = control (expected E,E,K,E)."""
import gzip,glob,pickle,re,runpy
import numpy as np
sc=runpy.run_path('/home/claude/dcf-math/rounds/dcf_localalign_L3585.py')['score']
A=runpy.run_path('/home/claude/dcf-math/rounds/dcf_align_L3569.py'); M=A['M']; enc=A['enc']
P,D=pickle.load(open('/home/claude/L3469/P6.pkl','rb')); mN=P['mouse']['Nalcn']
ref={g:P['mouse'][g] for g in ['Scn2a','Scn8a','Cacna1a','Cacna1c','Cacna1g','Nalcn']}
W=[mN.find(w) for w in ['SQEGW','TQEGW','SLKGW','TGEDW']]; assert min(W)>0
def ring(s):
    q=np.array(enc(s)); out=''
    for p in W:
        win=np.array(enc(mN[p-6:p+11])); c=int(p*len(s)/len(mN)); lo,hi=max(0,c-300),min(len(s)-17,c+300)
        best=max(range(lo,hi+1),key=lambda i:int(M[win,q[i:i+17]].sum())); out+=s[best+6+2]
    return out
def sets():
    for sp in ['human','mouse','zebrafish','chicken','fly','worm']: yield sp,list(P[sp].items())
    F=['/home/claude/L3501/z/early.tsv.gz','/home/claude/L3509/z/cteno.tsv.gz','/home/claude/L3533/z/bil.tsv.gz','/home/claude/L3557/z/oc.tsv.gz',
       '/home/claude/L3613/z/bat.tsv.gz','/home/claude/L3621/z/tard.tsv.gz']+sorted(glob.glob('/home/claude/L3629/z/*.gz'))+sorted(glob.glob('/home/claude/L3637/z/*.gz'))+sorted(glob.glob('/home/claude/L3645/z/*.gz'))
    for f in F:
        L=gzip.open(f,'rt').read().splitlines(); h=L[0].split('\t'); io,ie,iq=h.index('Organism'),h.index('Entry'),h.index('Sequence'); d={}
        for l in L[1:]:
            x=l.split('\t'); d.setdefault(x[io].split(' (')[0],[]).append((x[ie],x[iq]))
        for o,v in d.items(): yield o,v
    N=runpy.run_path('/home/claude/dcf-math/rounds/dcf_nerve_v2_L3549.py',run_name='x')
    yield 'Hofstenia miamia',list(N['proteins']('/home/claude/L3521/z/hmia.pep.fa.gz').items())
print('control mouse Nalcn ring:',ring(mN))
for o,items in sets():
    if len(items)<5000: continue
    hits=[]
    for a,s in items:
        if 1300<=len(s)<=2600 and len(re.findall(r'(?=[TS].[ED].W)',s))>=3:
            v,r=max((sc(s,ref[g]),g) for g in ref)
            if r=='Nalcn' and v>=1000: hits.append((a,len(s),v,ring(s)))
    print('ORG %-28s NALCN %d rings %s'%(o[:28],len(hits),sorted(set(h[3] for h in hits))),flush=True)
    for h in hits: print('   ',*h)
