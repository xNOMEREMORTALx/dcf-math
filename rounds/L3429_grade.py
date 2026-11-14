"""L3429 grading of PREREGISTERED_L3425 N1-N6 on mouse.3 (truth set built with last-parenthesis key, per A1)."""
import gzip,re,sys
Z='/home/claude/L3429/z/mouse.3.rna.fna.gz'
fam=lambda g:'Ca' if re.match(r'(?i)cacna1',g) else 'Na' if re.match(r'(?i)scn\d+a$',g) else 'K' if re.match(r'(?i)kcn[abcdfghqsv]\d',g) else 'HCN' if re.match(r'(?i)hcn\d',g) else None
truth={};k2p=set();last={}
for line in gzip.open(Z,'rt'):
    if line.startswith('>NM_'):
        m=re.findall(r'\(([A-Za-z0-9\-\.]+)\)',line)
        if not m: continue
        g=m[-1]; last[line.split()[0][1:]]=g
        if fam(g): truth[g]=fam(g)
        if re.match(r'(?i)kcnk\d',g): k2p.add(g)
def load(f):
    c={}
    for l in open(f):
        x=l.split()
        if x and x[0] in('Ca','Na','K','HCN','undecided','other','K2P'): c[x[1]]=x[0]
    return c
print('family genes present:',len(truth),sorted(truth.items())); print('Kcnk present:',sorted(k2p))
res=[]
for ver,f in [('v1','rounds/L3429_v1_tool.txt'),('v2','rounds/L3429_v2_tool.txt')]:
    calls={last[a]:c for a,c in load(f).items()}
    print('\n==',ver,sorted(calls.items()))
    def prec(cs,ok):
        L=[g for g,c in calls.items() if c in cs]; good=[g for g in L if fam(g) in ok]; return len(good),len(L),[g for g in L if g not in good]
    a,n,bad=prec(['Ca'],['Ca']); r1='PASS' if n>=2 and a/n>=0.9 else ('ungradeable' if n<2 else 'FAIL'); print('N1 Ca precision %d/%d %s %s'%(a,n,r1,bad))
    a,n,bad=prec(['Na'],['Na']); r2='PASS' if n>=1 and a==n else ('ungradeable' if n<1 else 'FAIL'); print('N2 Na precision %d/%d %s %s'%(a,n,r2,bad))
    a,n,bad=prec(['K','HCN'],['K','HCN']); r3='PASS' if a/n>=0.9 else 'FAIL'; print('N3 K/HCN precision %d/%d %s %s'%(a,n,r3,bad))
    ok=[g for g,t in truth.items() if calls.get(g)==t]; r4='PASS' if len(ok)/len(truth)>=0.75 else 'FAIL'
    print('N4 recall %d/%d = %.0f%% %s; missed %s'%(len(ok),len(truth),100*len(ok)/len(truth),r4,sorted((g,calls.get(g)) for g in truth if g not in ok)))
    res+= [r1,r2,r3,r4]
kc={last[a] for a,c in load('rounds/L3429_k2p_tool.txt').items()}
good=[g for g in kc if g in k2p]
r5='PASS' if len(kc)>=2 and len(good)/len(kc)>=0.9 else 'FAIL'; r6='PASS' if len(good)/len(k2p)>=0.7 else 'FAIL'
print('\nN5 K2P precision %d/%d %s %s'%(len(good),len(kc),r5,sorted(kc-k2p)))
print('N6 K2P recall %d/%d = %.0f%% %s; missed %s'%(len(good),len(k2p),100*len(good)/len(k2p),r6,sorted(k2p-kc)))
res+=[r5,r6]; print('\nTOTAL:',res,'passed',res.count('PASS'),'of',len([r for r in res if r!='ungradeable']))
