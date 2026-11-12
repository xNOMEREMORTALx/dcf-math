import sys, gzip, re, collections
sys.path.insert(0,'/home/claude/dcf-math/rounds'); import dcf_orfstart_L3309 as O
prots=[]
for f in ['/home/claude/L3313/p/human.1.protein.faa.gz','/home/claude/L3313/p/human.2.protein.faa.gz']:
    for b in gzip.open(f,'rt').read().split('>')[1:]:
        h,_,s=b.partition('\n'); s=s.replace('\n','')
        if len(s)>=50: prots.append(s)
byend=collections.defaultdict(list)
for s in prots: byend[s[-25:]].append(s)
genes={}
for path in ['/home/claude/L3261/in/human.1.rna.fna.gz','/home/claude/L3261/in/human.2.rna.fna.gz','/home/claude/L3269/rna_in/human.3.rna.fna.gz','/home/claude/L3269/rna_in/human.4.rna.fna.gz']:
    for blk in gzip.open(path,'rt').read().split('>')[1:]:
        h,_,s=blk.partition('\n'); acc=h.split()[0]
        if not acc.startswith('NM_'): continue
        m=re.search(r'\(([A-Za-z0-9\-\.]+)\)',h); g=m.group(1) if m else acc
        num=int(re.sub(r'\D','',acc.split('.')[0]))
        if g not in genes or num<genes[g][0]: genes[g]=(num,s.replace('\n','').upper())
n=eA=eK=over=overK=fix=brk=under=0; examples=[]
for g,(_,s) in genes.items():
    a=O.orf_A(s)
    cands=[p for p in byend.get(a[-25:],[]) if a.endswith(p)]
    if not cands: continue
    P=max(cands,key=len); k=O.orf_K(s); n+=1
    A=(a==P); K=(k==P); eA+=A; eK+=K
    if len(a)>len(P): over+=1; overK+=K
    if len(a)<len(P): under+=1
    if K and not A: fix+=1
    if A and not K: brk+=1; examples.append((g,len(P),len(k)))
print("graded transcripts",n,"| rule A exact %d (%.1f%%) | rule K exact %d (%.1f%%)"%(eA,100*eA/n,eK,100*eK/n))
print("A overshoots",over,"K exact among them",overK,"(%.0f%%)"%(100*overK/max(over,1)),"| A undershoots",under)
print("fixes",fix,"breaks",brk)
print("K1",'PASS' if eK>eA else 'FAIL',"| K2",'PASS' if overK>=0.5*over else 'FAIL',"| K3",'PASS' if brk<=fix/2 else 'FAIL')
print("break examples (gene, true len, K len):",examples[:12])

# development after grading: context of true starts vs false first-ATGs
import collections
tc=collections.Counter(); fc=collections.Counter(); t4=collections.Counter(); f4=collections.Counter(); nt=nf=0
for g,(_,s) in genes.items():
    a=O.orf_A(s); cands=[p for p in byend.get(a[-25:],[]) if a.endswith(p)]
    if not cands: continue
    P=max(cands,key=len); st,en=O._best(s); true_st=st+3*(len(a)-len(P))
    if true_st>=3: tc[s[true_st-3]]+=1; t4[s[true_st+3]]+=1; nt+=1
    if len(a)>len(P) and st>=3: fc[s[st-3]]+=1; f4[s[st+3]]+=1; nf+=1
pur=lambda c,n:100*(c['A']+c['G'])/max(n,1)
print("true starts: -3 purine %.1f%% (n=%d), +4 G %.1f%% | false first ATGs: -3 purine %.1f%% (n=%d), +4 G %.1f%%"%(pur(tc,nt),nt,100*t4['G']/nt,pur(fc,nf),nf,100*f4['G']/max(nf,1)))
