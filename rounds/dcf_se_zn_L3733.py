"""L3733 frozen: selenium and zinc proteomes from sequence, every organism seen.
Se: proteins containing U (selenocysteine) - UniProt sets only (the P6 RefSeq-ORF sets read UGA as stop, so they cannot show U).
Zn: proteins with >= 3 C2H2 motifs C.{2,4}C.{12}H.{3,5}H; reported as count and share of the proteome; P6 sets included for Zn."""
import gzip,glob,collections,pickle,re,runpy
ZF=re.compile(r'C.{2,4}C.{12}H.{3,5}H')
N=runpy.run_path('/home/claude/dcf-math/rounds/dcf_nerve_v3_L3633.py',run_name='x')
P,D=pickle.load(open('/home/claude/L3469/P6.pkl','rb'))
sets=[(sp+' (RefSeq ORF)',list(P[sp].values()),False) for sp in ['mouse','zebrafish','chicken','fly']]
F=['/home/claude/L3501/z/early.tsv.gz','/home/claude/L3509/z/cteno.tsv.gz','/home/claude/L3533/z/bil.tsv.gz','/home/claude/L3557/z/oc.tsv.gz','/home/claude/L3605/z/nn.tsv.gz',
   '/home/claude/L3613/z/bat.tsv.gz','/home/claude/L3621/z/tard.tsv.gz','/home/claude/L3661/z/worm.tsv.gz','/home/claude/L3669/z3/h2.tsv.gz']+sorted(glob.glob('/home/claude/L3629/z/*.gz'))+\
  sorted(glob.glob('/home/claude/L3637/z/*.gz'))+sorted(glob.glob('/home/claude/L3645/z/*.gz'))+sorted(glob.glob('/home/claude/L3677/z/*.gz'))+sorted(glob.glob('/home/claude/L3689/z/*.gz'))+sorted(glob.glob('/home/claude/L3701/z/*.gz'))
for f in F:
    L=gzip.open(f,'rt').read().splitlines(); h=L[0].split('\t'); io,iq=h.index('Organism'),h.index('Sequence'); d=collections.defaultdict(list)
    for l in L[1:]: x=l.split('\t'); d[x[io].split(' (')[0]].append(x[iq])
    sets+=[(o,v,True) for o,v in d.items()]
sets.append(('Hofstenia miamia (FASTA)',list(N['proteins']('/home/claude/L3521/z/hmia.pep.fa.gz').values()),True))
seen=set()
for o,seqs,uni in sets:
    if len(seqs)<5000 or o in seen: continue
    seen.add(o); se=sum('U' in s for s in seqs) if uni else -1; zn=sum(len(ZF.findall(s))>=3 for s in seqs)
    print('ORG\t%s\tproteins\t%d\tSe_U\t%s\tZn_C2H2x3\t%d\tZn_share\t%.4f'%(o,len(seqs),se if se>=0 else 'n/a',zn,zn/len(seqs)),flush=True)
