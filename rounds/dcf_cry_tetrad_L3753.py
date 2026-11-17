"""L3753 frozen: the cryptochrome tryptophan tetrad (TrpA-D) across bird cryptochromes. argv: UniProt FASTA (bird cryptochromes).
Reference: robin CRY4 A0A2I4SZI9. Tetrad positions (1-based, my recollection of Xu et al. 2021, checked as Q1): A 395, B 372, C 318, D 369.
Each other sequence is aligned to the reference by Smith-Waterman (BLOSUM62 from dcf_align, gap 8) WITH traceback; the residue aligned to
each tetrad position is read ('-' if unaligned). Class from the FASTA header name: CRY4 if 'ryptochrome 4' or 'CRY4' in the header; CRY1/CRY2
likewise; full length = >= 450 aa."""
import re,sys,runpy
import numpy as np
A=runpy.run_path('/home/claude/dcf-math/rounds/dcf_align_L3569.py'); M=A['M']; enc=A['enc']; GAP=8
def sw_map(ref,q):
    a=np.array(enc(ref)); b=np.array(enc(q)); n,m=len(a),len(b); H=np.zeros((n+1,m+1),np.int32); T=np.zeros((n+1,m+1),np.int8)
    for i in range(1,n+1):
        s=M[a[i-1],b]
        for j in range(1,m+1):
            d=H[i-1,j-1]+s[j-1]; u=H[i-1,j]-GAP; l=H[i,j-1]-GAP; v=max(0,d,u,l); H[i,j]=v
            T[i,j]=0 if v==0 else (1 if v==d else (2 if v==u else 3))
    i,j=np.unravel_index(np.argmax(H),H.shape); mp={}
    while i>0 and j>0 and T[i,j]!=0:
        t=T[i,j]
        if t==1: mp[i]=q[j-1]; i-=1; j-=1
        elif t==2: i-=1
        else: j-=1
    return mp,int(H.max())
recs=[]; h=None; s=[]
for l in open(sys.argv[1]):
    l=l.strip()
    if l.startswith('>'):
        if h: recs.append((h,''.join(s)))
        h=l[1:]; s=[]
    elif l: s.append(l)
if h: recs.append((h,''.join(s)))
ref=[q for hh,q in recs if hh.split('|')[1]=='A0A2I4SZI9'][0]
P={'A':395,'B':372,'C':318,'D':369}
print('reference length',len(ref),'| residues at A395 B372 C318 D369:',{k:ref[v-1] for k,v in P.items()})
for hh,q in recs:
    acc=hh.split('|')[1]; nm=hh.split(' OS=')[0].split(' ',1)[1]; org=re.search(r'OS=(.*?) OX=',hh).group(1)
    cls='CRY4' if re.search(r'ryptochrome[ -]4|CRY4',hh) else ('CRY1' if re.search(r'ryptochrome[ -]1|CRY1|regulator 1',hh) else ('CRY2' if re.search(r'ryptochrome[ -]2|CRY2|regulator 2',hh) else 'other'))
    if len(q)<450: continue
    mp,sc=sw_map(ref,q); r=''.join(mp.get(P[k],'-') for k in 'ABCD')
    print('ROW\t%s\t%s\t%s\t%d\t%d\t%s'%(acc,cls,org,len(q),sc,r),flush=True)
