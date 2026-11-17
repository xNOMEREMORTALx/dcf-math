"""L3761 frozen: full alignment scan (no shortlist) for the cryptochrome/photolyase family in all proteomes seen.
Every protein 400-900 aa is scored (dcf_localalign_L3585) against robin CRY4 (A0A2I4SZI9); hit = score >= 350.
Each hit: tetrad read by the L3753 traceback (A395 B372 C318 D369); family = nearest of robin CRY4, mouse Cry1, mouse Cry2, fly cry,
fly phr6-4, zebrafish cry-dash (local score). Two worker processes; output sorted by organism."""
import gzip,glob,collections,pickle,runpy,sys
from multiprocessing import Pool
def load():
    src=open('/home/claude/dcf-math/rounds/dcf_cry_tetrad_L3753.py').read().split('recs=[]')[0]; G={}; exec(src,G)
    sc=runpy.run_path('/home/claude/dcf-math/rounds/dcf_localalign_L3585.py')['score']
    ref=[''.join(l.split('\n')[1:]) for l in open('/home/claude/L3753/z/cry.fasta').read().split('>') if l.startswith('tr|A0A2I4SZI9|')][0]
    PP,D=pickle.load(open('/home/claude/L3469/P6.pkl','rb'))
    R={'CRY4(robin)':ref,'Cry1(mouse)':PP['mouse']['Cry1'],'Cry2(mouse)':PP['mouse']['Cry2'],'cry(fly)':PP['fly']['cry'],'phr6-4(fly)':PP['fly']['phr6-4'],'cry-dash(zf)':PP['zebrafish']['cry-dash']}
    return G['sw_map'],sc,ref,R
def work(args):
    o,items=args; sw_map,sc,ref,R=load(); P={'A':395,'B':372,'C':318,'D':369}; hits=[]
    for a,s in items:
        if not 400<=len(s)<=900: continue
        v=sc(s,ref)
        if v>=350:
            mp,_=sw_map(ref,s); fam=max(R,key=lambda k:sc(s,R[k])); hits.append('%s:%d:%s:%s'%(a,v,''.join(mp.get(P[k],'-') for k in 'ABCD'),fam))
    return o,hits
if __name__=='__main__':
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
    seen=set(); jobs=[]
    for o,items in sets:
        if len(items)>=5000 and o not in seen: seen.add(o); jobs.append((o,items))
    with Pool(2) as p:
        for o,hits in sorted(p.imap_unordered(work,jobs)): print('ORG\t%s\thits\t%d\t%s'%(o,len(hits),' '.join(hits)),flush=True)
