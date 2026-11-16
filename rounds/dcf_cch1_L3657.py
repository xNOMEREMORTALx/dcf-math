"""L3657 frozen. argv[1] = reference TSV (UniProt; yeast Cch1 P50077, human NALCN Q8IZF0); argv[2] = C. elegans proteome TSV (UP000001940).
Part C: every NALCN hit listed in rounds/L3653_tool_output.txt is scored (local aligner) against yeast Cch1 and mouse Nalcn.
Part W: C. elegans NALCN hits by the frozen L3653 rule (score floor 1000) and their rings."""
import gzip,re,runpy,sys,glob
sc=runpy.run_path('/home/claude/dcf-math/rounds/dcf_localalign_L3585.py')['score']
src=open('/home/claude/dcf-math/rounds/dcf_nalcn_ring_L3653.py').read().split("print('control mouse Nalcn ring:'")[0]
G={}; exec(src,G)                       # frozen L3653 definitions: ref, mN, ring(), sets()
L=gzip.open(sys.argv[1],'rt').read().splitlines(); h=L[0].split('\t')
REF={l.split('\t')[h.index('Entry')]:l.split('\t')[h.index('Sequence')] for l in L[1:]}
cch1=REF['P50077']; print('refs',{k:len(v) for k,v in REF.items()},'| human NALCN ring',G['ring'](REF['Q8IZF0']))
T=open('/home/claude/dcf-math/rounds/L3653_tool_output.txt').read().splitlines()
want={}; org=None
for l in T:
    if l.startswith('ORG '): org=l[4:33].strip()
    elif l.startswith('    '): want[l.split()[0]]=org
seq={}
for o,items in G['sets']():
    for a,s in items:
        if a in want: seq[a]=s
print('Part C: NALCN hits found again',len(seq),'of',len(want))
for a,o in want.items():
    s=seq[a]; c,n=sc(s,cch1),sc(s,G['mN']); print('C %-28s %-12s Cch1 %5d Nalcn %5d nearer %s'%(o,a,c,n,'Cch1' if c>n else 'Nalcn'),flush=True)
L=gzip.open(sys.argv[2],'rt').read().splitlines(); h=L[0].split('\t'); ie,iq=h.index('Entry'),h.index('Sequence')
print('Part W: C. elegans proteins',len(L)-1)
for l in L[1:]:
    x=l.split('\t'); s=x[iq]
    if 1300<=len(s)<=2600 and len(re.findall(r'(?=[TS].[ED].W)',s))>=3:
        v,r=max((sc(s,G['ref'][g]),g) for g in G['ref'])
        if r=='Nalcn' and v>=1000: print('W',x[ie],len(s),v,G['ring'](s),flush=True)
