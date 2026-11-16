"""L3693 frozen calibration of the NR1 score floor. For every organism seen (L3681 recount set + L3677 + L3689), every dcf_nerve v3 iGluR call
whose nearest of the 18 mouse iGluRs (local aligner) is Grin1 is listed with its score and its name.
Label: POS if name matches NR1 (regex POS); NEG if it has a name that is not POS and not uninformative (regex UNINF); else excluded.
Floor = the threshold t (over observed scores) maximising balanced accuracy (TPR+TNR)/2 for 'score >= t'; ties -> the lowest t.
Vertebrate/fly sets (P6) use gene symbols as names."""
import gzip,glob,pickle,re,runpy,collections
POS=re.compile(r'(?i)(NMDA[^,;]*\b(subunit|receptor)\s*(1|zeta[- ]?1)\b|NMDA 1\b|NMDA receptor 1|zeta-1|^grin1[ab]?$|^Nmdar1$|NR1\b)')
UNINF=re.compile(r'(?i)^(uncharacterized protein|protein of unknown function|hypothetical protein|)$|domain-containing protein$')
N=runpy.run_path('/home/claude/dcf-math/rounds/dcf_nerve_v3_L3633.py',run_name='x')
sc=runpy.run_path('/home/claude/dcf-math/rounds/dcf_localalign_L3585.py')['score']
P,D=pickle.load(open('/home/claude/L3469/P6.pkl','rb'))
REF={g:p for g,p in P['mouse'].items() if re.match(r'(?i)^(gria\d|grik\d|grid\d|grin\d\w?)$',g)}
sets=[(sp,[(g,g,s) for g,s in P[sp].items()]) for sp in ['human','mouse','zebrafish','chicken','fly']]
F=['/home/claude/L3501/z/early.tsv.gz','/home/claude/L3509/z/cteno.tsv.gz','/home/claude/L3533/z/bil.tsv.gz','/home/claude/L3557/z/oc.tsv.gz',
   '/home/claude/L3613/z/bat.tsv.gz','/home/claude/L3621/z/tard.tsv.gz','/home/claude/L3661/z/worm.tsv.gz']+sorted(glob.glob('/home/claude/L3629/z/*.gz'))+\
  sorted(glob.glob('/home/claude/L3637/z/*.gz'))+sorted(glob.glob('/home/claude/L3645/z/*.gz'))+sorted(glob.glob('/home/claude/L3677/z/*.gz'))+sorted(glob.glob('/home/claude/L3689/z/*.gz'))
for f in F:
    L=gzip.open(f,'rt').read().splitlines(); h=L[0].split('\t'); io,ie,iq=h.index('Organism'),h.index('Entry'),h.index('Sequence')
    ip=h.index('Protein names') if 'Protein names' in h else None; d=collections.defaultdict(list)
    for l in L[1:]:
        x=l.split('\t'); d[x[io].split(' (')[0]].append((x[ie],x[ip] if ip is not None else '',x[iq]))
    sets+=list(d.items())
rows=[]; seen=set()
for o,items in sets:
    if len(items)<5000 or o in seen: continue
    seen.add(o)
    for a,n,s in items:
        if 'iGluR' not in N['tags'](s): continue
        v,r=max((sc(s,REF[g]),g) for g in REF)
        if r!='Grin1': continue
        lab='POS' if POS.search(n) else ('EXCL' if UNINF.search(n.strip()) else 'NEG')
        rows.append((o,a,v,lab,n)); print('ROW\t%s\t%s\t%d\t%s\t%s'%(o[:28],a,v,lab,n[:70]),flush=True)
pos=sorted(v for *_,v,l,n in [(r[0],r[1],r[2],r[3],r[4]) for r in rows] if l=='POS'); neg=sorted(r[2] for r in rows if r[3]=='NEG')
print('POS',len(pos),pos); print('NEG',len(neg),neg)
best=None
for t in sorted(set(r[2] for r in rows)):
    tpr=sum(v>=t for v in pos)/len(pos) if pos else 0; tnr=sum(v<t for v in neg)/len(neg) if neg else 0; ba=(tpr+tnr)/2
    if best is None or ba>best[0]+1e-12: best=(ba,t,tpr,tnr)
print('FLOOR %d balanced_accuracy %.3f TPR %.3f TNR %.3f'%(best[1],best[0],best[2],best[3]))
