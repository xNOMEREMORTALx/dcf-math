"""L3757 frozen: cryptochrome/photolyase family and its tryptophan tetrad across all proteomes seen.
Shortlist: proteins 400-900 aa ranked by the number of distinct 3-mers shared with robin CRY4 (A0A2I4SZI9); top 20 per proteome.
Hit: local score (dcf_localalign_L3585) vs robin CRY4 >= 600. Each hit is mapped by the L3753 traceback aligner; tetrad read at A395 B372 C318 D369."""
import gzip,glob,collections,pickle,re,runpy,io,contextlib,sys
src=open('/home/claude/dcf-math/rounds/dcf_cry_tetrad_L3753.py').read().split('recs=[]')[0]; G={}; exec(src,G); sw_map=G['sw_map']
sc=runpy.run_path('/home/claude/dcf-math/rounds/dcf_localalign_L3585.py')['score']
ref=None
for l in open('/home/claude/L3753/z/cry.fasta').read().split('>'):
    if l.startswith('tr|A0A2I4SZI9|'): ref=''.join(l.split('\n')[1:])
K3=set(ref[i:i+3] for i in range(len(ref)-2)); P={'A':395,'B':372,'C':318,'D':369}
N=runpy.run_path('/home/claude/dcf-math/rounds/dcf_nerve_v3_L3633.py',run_name='x')
PP,D=pickle.load(open('/home/claude/L3469/P6.pkl','rb'))
sets=[(sp,list(PP[sp].items())) for sp in ['mouse','zebrafish','chicken','fly']]
F=['/home/claude/L3501/z/early.tsv.gz','/home/claude/L3509/z/cteno.tsv.gz','/home/claude/L3533/z/bil.tsv.gz','/home/claude/L3557/z/oc.tsv.gz','/home/claude/L3605/z/nn.tsv.gz',
   '/home/claude/L3613/z/bat.tsv.gz','/home/claude/L3621/z/tard.tsv.gz','/home/claude/L3661/z/worm.tsv.gz','/home/claude/L3669/z3/h2.tsv.gz']+sorted(glob.glob('/home/claude/L3629/z/*.gz'))+\
  sorted(glob.glob('/home/claude/L3637/z/*.gz'))+sorted(glob.glob('/home/claude/L3645/z/*.gz'))+sorted(glob.glob('/home/claude/L3677/z/*.gz'))+sorted(glob.glob('/home/claude/L3689/z/*.gz'))+sorted(glob.glob('/home/claude/L3701/z/*.gz'))
for f in F:
    L=gzip.open(f,'rt').read().splitlines(); h=L[0].split('\t'); io_,ie,iq=h.index('Organism'),h.index('Entry'),h.index('Sequence'); d=collections.defaultdict(list)
    for l in L[1:]: x=l.split('\t'); d[x[io_].split(' (')[0]].append((x[ie],x[iq]))
    sets+=list(d.items())
sets.append(('Hofstenia miamia',list(N['proteins']('/home/claude/L3521/z/hmia.pep.fa.gz').items())))
seen=set()
for o,items in sets:
    if len(items)<5000 or o in seen: continue
    seen.add(o)
    cand=sorted(((len(K3&set(s[i:i+3] for i in range(len(s)-2))),a,s) for a,s in items if 400<=len(s)<=900),reverse=True)[:20]
    hits=[]
    for _,a,s in cand:
        v=sc(s,ref)
        if v>=600:
            mp,_=sw_map(ref,s); hits.append((a,len(s),v,''.join(mp.get(P[k],'-') for k in 'ABCD')))
    print('ORG\t%s\thits\t%d\t%s'%(o,len(hits),' '.join('%s:%d:%s'%(a,v,t) for a,n,v,t in hits)),flush=True)
