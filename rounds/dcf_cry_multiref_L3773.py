"""L3773 frozen: multi-reference photolyase/cryptochrome finder. References: robin CRY4, fly phr6-4, zebrafish cry-dash, Neurospora photolyase P27526,
diatom DASH B7FV99. Every protein 400-900 aa is scored against all five (dcf_localalign_L3585); hit = best score >= 350; family = best reference;
tetrad read by the L3753 traceback against robin CRY4. Organisms: mouse, zebrafish, chicken, fly (P6), the three outgroups (L3769), and the 18
bilaterians with no L3761 hit."""
import gzip,glob,collections,pickle,runpy
from multiprocessing import Pool
ZERO=['Caenorhabditis elegans','Ciona intestinalis','Saccoglossus kowalevskii','Hofstenia miamia','Priapulus caudatus','Hypsibius exemplaris','Ramazzottius varieornatus',
 'Helobdella robusta','Dimorphilus gyrociliatus','Schistosoma mansoni','Schistosoma japonicum','Fasciola hepatica','Clonorchis sinensis','Paragonimus westermani',
 'Echinococcus multilocularis','Taenia asiatica','Hymenolepis diminuta','Adineta ricciae']
def refs():
    PP,D=pickle.load(open('/home/claude/L3469/P6.pkl','rb'))
    R={'CRY4(robin)':[''.join(l.split('\n')[1:]) for l in open('/home/claude/L3753/z/cry.fasta').read().split('>') if l.startswith('tr|A0A2I4SZI9|')][0],
       'phr6-4(fly)':PP['fly']['phr6-4'],'cry-dash(zf)':PP['zebrafish']['cry-dash']}
    for f,a,k in [('/home/claude/L3769/z/neuro.tsv.gz','P27526','CPD-photolyase(Neurospora)'),('/home/claude/L3769/z/phaeo.tsv.gz','B7FV99','DASH(diatom)')]:
        for l in gzip.open(f,'rt'):
            x=l.rstrip('\n').split('\t')
            if x[0]==a: R[k]=x[3]
    return R
def work(args):
    o,items=args; src=open('/home/claude/dcf-math/rounds/dcf_cry_tetrad_L3753.py').read().split('recs=[]')[0]; G={}; exec(src,G)
    sc=runpy.run_path('/home/claude/dcf-math/rounds/dcf_localalign_L3585.py')['score']; R=refs(); P={'A':395,'B':372,'C':318,'D':369}; hits=[]
    for a,s in items:
        if not 400<=len(s)<=900: continue
        v,k=max((sc(s,R[r]),r) for r in R)
        if v>=350:
            mp,_=G['sw_map'](R['CRY4(robin)'],s); hits.append('%s:%d:%s:%s'%(a,v,''.join(mp.get(P[q],'-') for q in 'ABCD'),k))
    return o,hits
if __name__=='__main__':
    N=runpy.run_path('/home/claude/dcf-math/rounds/dcf_nerve_v3_L3633.py',run_name='x'); PP,D=pickle.load(open('/home/claude/L3469/P6.pkl','rb'))
    jobs=[(sp,list(PP[sp].items())) for sp in ['mouse','zebrafish','chicken','fly']]
    F=glob.glob('/home/claude/L3769/z/*.gz')+['/home/claude/L3557/z/oc.tsv.gz','/home/claude/L3533/z/bil.tsv.gz','/home/claude/L3621/z/tard.tsv.gz','/home/claude/L3613/z/bat.tsv.gz',
       '/home/claude/L3661/z/worm.tsv.gz']+glob.glob('/home/claude/L3629/z/*.gz')+glob.glob('/home/claude/L3637/z/*.gz')+glob.glob('/home/claude/L3645/z/*.gz')+glob.glob('/home/claude/L3677/z/*.gz')+glob.glob('/home/claude/L3689/z/*.gz')+glob.glob('/home/claude/L3701/z/*.gz')
    seen=set()
    for f in F:
        L=gzip.open(f,'rt').read().splitlines(); h=L[0].split('\t'); io_,ie,iq=h.index('Organism'),h.index('Entry'),h.index('Sequence'); d=collections.defaultdict(list)
        for l in L[1:]: x=l.split('\t'); d[x[io_].split(' (')[0]].append((x[ie],x[iq]))
        for o,v in d.items():
            if len(v)>=5000 and o not in seen and (o in ZERO or f.startswith('/home/claude/L3769')): seen.add(o); jobs.append((o,v))
    if 'Hofstenia miamia' not in seen: jobs.append(('Hofstenia miamia',list(N['proteins']('/home/claude/L3521/z/hmia.pep.fa.gz').items())))
    with Pool(2) as p:
        for o,hits in sorted(p.imap_unordered(work,jobs)): print('ORG\t%s\thits\t%d\t%s'%(o,len(hits),' '.join(hits)),flush=True)
