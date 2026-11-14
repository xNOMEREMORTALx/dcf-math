"""L3501 grading of PREREGISTERED_L3493_before_nerves S1-S7 + descriptive per-species table and pore loops."""
import gzip,re,collections
O={};N={};S={}
for l in gzip.open('/home/claude/L3501/z/early.tsv.gz','rt').read().splitlines()[1:]:
    f=l.split('\t'); O[f[0]]=f[1].split(' (')[0]; N[f[0]]=f[2]; S[f[0]]=f[3]
calls=collections.defaultdict(lambda:collections.defaultdict(list))
for l in open('rounds/L3501_tool.txt'):
    x=l.split()
    if x and x[0]!='proteins:': calls[O[x[1]]][x[0]].append(x[1])
sp=['Monosiga brevicollis','Amphimedon queenslandica','Trichoplax adhaerens','Nematostella vectensis']
cnt=lambda s,c: len(calls[s][c])
R=[('S1','PASS' if cnt(sp[0],'Na')==0 else 'FAIL'),('S2','PASS' if cnt(sp[1],'Na')==0 else 'FAIL'),('S3','PASS' if cnt(sp[2],'Na')==0 else 'FAIL'),
   ('S4','PASS' if cnt(sp[3],'Na')==0 else 'FAIL'),('S5','PASS' if cnt(sp[3],'Ca')>=1 else 'FAIL'),('S6','PASS' if cnt(sp[2],'Ca')>=1 else 'FAIL'),
   ('S7','PASS' if cnt(sp[3],'K')>=3 else 'FAIL')]
cl=['Na','Ca','undecided','K','HCN','K2P','iGluR','FeHyd','pump_NaK','pump_Ca','pump_Cu','pump_other','other']
print('%-26s'%'species'+''.join('%9s'%c[:9] for c in cl))
for s in sp: print('%-26s'%s+''.join('%9d'%cnt(s,c) for c in cl))
print('\nDescriptive: every 4-domain call (Ca/Na/undecided) with its calcium-ring hits and lysine/Nax loops, and UniProt name')
RING=r'(?=[TS].[ED].W)'
for s in sp:
    for c in ('Ca','Na','undecided'):
        for a in calls[s][c]:
            p=S[a]; print('  %-22s %-9s %s %4d aa | ring %s | K-loop %s | N-loop %s | %s'%(s[:22],c,a,len(p),[p[m.start():m.start()+5] for m in re.finditer(RING,p)],re.findall(r'[TS][FY][KR][GA]W',p),re.findall(r'[TS]F[NQ]GW',p),N[a][:50]))
print('\nRESULT',R); print('passed',sum(r=='PASS' for _,r in R),'of',len(R))
