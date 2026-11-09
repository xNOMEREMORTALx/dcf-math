"""dcf_mrna_wide.py (frozen L3253) - whole mRNAs are scanned and hits assigned to the 5'/3' UTR by position (a hairpin may overlap the CDS edge); IRE-wide scan and metal-number periodicity on a large human mRNA file (FASTA or GenBank, .gz allowed).
Uses dcf_ire.scan and longest-ORF UTRs; NM_ records only. Shuffled control = dinucleotide-preserving shuffle (Altschul-Erickson style via random
Eulerian walk) of each 5' and 3' UTR, 10 replicates. Gary NOMEREMORTAL Mason (Digital Cosmos Framework).
Usage: python3 -I dcf_mrna_wide.py human.1.rna.fna.gz /path/to/dcf_ire.py"""
import sys, gzip, re, random, importlib.util, numpy as np
spec=importlib.util.spec_from_file_location('ire',sys.argv[2]); ire=importlib.util.module_from_spec(spec); spec.loader.exec_module(ire)
def records(path):
    op=gzip.open if path.endswith('.gz') else open
    txt=op(path,'rt').read()
    if txt.lstrip().startswith('>'):
        for blk in txt.split('>')[1:]:
            h,_,s=blk.partition('\n'); yield h.split()[0], h, re.sub(r'[^ACGT]','N',s.replace('\n','').upper())
    else:
        for rec in txt.split('\n//'):
            if 'ORIGIN' not in rec: continue
            acc=re.search(r'LOCUS\s+(\S+)',rec).group(1); d=re.search(r'DEFINITION\s+(.*?)\n\S',rec,re.S)
            yield acc, (' '.join(d.group(1).split()) if d else ''), re.sub(r'[^ACGT]','N',''.join(re.findall(r'[A-Za-z]+',rec.split('ORIGIN')[1])).upper())
def dishuffle(s,rng):
    if len(s)<3: return s
    edges={}
    for a,b in zip(s,s[1:]): edges.setdefault(a,[]).append(b)
    last=s[-1]
    for _ in range(50):
        # choose last-edge for each vertex (except final) forming a tree toward 'last'
        lastE={}; ok=True
        for v in edges:
            if v==last: continue
            lastE[v]=rng.choice(edges[v])
        # check every vertex reaches 'last' via lastE
        for v in lastE:
            seen=set(); x=v
            while x!=last and x not in seen: seen.add(x); x=lastE.get(x,last)
            if x!=last: ok=False; break
        if ok: break
    E={}
    for v,l in edges.items():
        l=l[:]
        if v in lastE: l.remove(lastE[v]); rng.shuffle(l); l.append(lastE[v])
        else: rng.shuffle(l)
        E[v]=l
    out=[s[0]]; idx={v:0 for v in E}
    for _ in range(len(s)-1):
        v=out[-1]; out.append(E[v][idx[v]]); idx[v]+=1
    return ''.join(out)
PER=[3,11,12,19,20,23,24,26,29,30,34,39,40,56,63,64]
def spectrum_ratios(seqs):
    s=''.join(seqs); out={}
    for p in PER:
        k=round(4100/p); W=p*k; a=np.frombuffer(s.encode(),np.uint8); n=len(a)//W; a=a[:n*W].reshape(n,W); Pw=np.zeros((n,W//2+1))
        for b in b'ACGT':
            x=(a==b).astype(float); x-=x.mean(1,keepdims=True); Pw+=np.abs(np.fft.rfft(x,axis=1))**2
        rng=np.random.default_rng(0); boots=[]
        for _ in range(2000):
            m=Pw[rng.integers(0,n,n)].mean(0); boots.append(m[k]/np.mean(np.r_[m[k-8:k-2],m[k+3:k+9]]))
        m=Pw.mean(0); out[p]=(m[k]/np.mean(np.r_[m[k-8:k-2],m[k+3:k+9]]),np.percentile(boots,0.0833),np.percentile(boots,99.9167),n)
    return out
if __name__=='__main__':
    rng=random.Random(1); n=0; hits5=hits3=0; sh5=sh3=0; L5=L3=0; cds=[]; utr=[]; lst=[]
    for acc,desc,s in records(sys.argv[1]):
        if not acc.startswith('NM_'): continue
        a,b=ire.longest_orf(s); u5=s[:a]; u3=s[b:]; n+=1; L5+=len(u5); L3+=len(u3); cds.append(s[a:b]); utr.append(u5+u3)
        H=ire.scan(s); h5=[h for h in H if h<a]; h3=[h for h in H if h>=b]; hits5+=len(h5); hits3+=len(h3)
        if h5 or h3: lst.append((acc,desc[:80],len(h5),len(h3)))
        for _ in range(10):
            t=dishuffle(u5,rng)+s[a:b]+dishuffle(u3,rng); T=ire.scan(t)
            sh5+=sum(h<a for h in T)/10; sh3+=sum(h>=b for h in T)/10
    print("NM_ mRNAs %d | 5'UTR %.1f Mb, 3'UTR %.1f Mb"%(n,L5/1e6,L3/1e6))
    print("IRE hits: 5'UTR real %d vs shuffled %.1f | 3'UTR real %d vs shuffled %.1f"%(hits5,sh5,hits3,sh3))
    for r in lst: print("  HIT",*r,sep='\t')
    for name,S in (('coding',cds),('UTR',utr)):
        for p,(r,lo,hi,nw) in spectrum_ratios(S).items(): print("%s period %d: ratio %.3f  99.83%% CI %.3f-%.3f  windows %d"%(name,p,r,lo,hi,nw))
