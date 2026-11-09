import sys, re, math, importlib.util
spec=importlib.util.spec_from_file_location('sf','/home/claude/tools/dcf_secflag.py'); sf=importlib.util.module_from_spec(spec); spec.loader.exec_module(sf)
def codon_tables(seq,G):
    L=len(seq); R=sf.rc(seq); cod={}; bg={}
    for a,b,s in G:
        g=seq[a-1:b] if s=='+' else sf.rc(seq[a-1:b])
        for i in range(0,len(g)-3,3): c=g[i:i+3]; cod[c]=cod.get(c,0)+1
        for sh in (1,2):   # out-of-frame background from the same genes
            for i in range(sh,len(g)-3,3): c=g[i:i+3]; bg[c]=bg.get(c,0)+1
    tc=sum(cod.values()); tb=sum(bg.values())
    return {c:math.log((cod.get(c,0)+1)/tc)-math.log((bg.get(c,0)+1)/tb) for c in set(cod)|set(bg)}
def score_upstream(S,i,lo,T):
    # mean coding log-odds of the in-frame stretch lo..i (upstream part, excluding stops)
    cs=[S[k:k+3] for k in range(lo,i,3)]
    return sum(T.get(c,0) for c in cs)/max(len(cs),1)
def run(gb,gff):
    seq=sf.read_seq(gb); G=sf.read_gff(gff); L=len(seq); R=sf.rc(seq)
    T=codon_tables(seq,G)
    C=sf.cands(seq,G)
    txt=open(gb).read()
    sec=set(int(m.group(1)) for m in re.finditer(r'transl_except=\(pos:(?:complement\()?(\d+)\.\.\d+\)?,aa:Sec',txt))
    rows=[]
    for s,p,t in C:
        S=seq if s=='+' else R
        i=(p-1) if s=='+' else L-p-2   # index of TGA in strand coords
        if t=='upstream':
            j=i-3
            while j>=0 and S[j:j+3] not in sf.STOP: j-=3
            us=[k for k in range(j+3,i,3) if S[k:k+3] in sf.START]; lo=us[0]
            sc=score_upstream(S,i,lo,T)
        else:
            k=i+3
            while k<L-3 and S[k:k+3] not in sf.STOP: k+=3
            sc=score_upstream(S,k,i+3,T)   # downstream continuation
        rows.append((sc,p in sec,t))
    return rows,len(sec)
if __name__=='__main__':
    out=[]
    for gb,gff in zip(sys.argv[1::2],sys.argv[2::2]):
        rows,n=run(gb,gff); out.append((gb.split('/')[-1],rows,n))
    import json; json.dump([(a,[(round(s,4),bool(h),t) for s,h,t in r],n) for a,r,n in out],open('/home/claude/sec3/rows.json','w'))
    for a,r,n in out: print(a,"cands",len(r),"hits",sum(h for _,h,_ in r),"of",n)
