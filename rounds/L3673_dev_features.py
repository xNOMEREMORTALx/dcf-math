"""L3673 development: per organism seen, (a) NR1 calls (iGluR nearest mouse Grin1, L3625 method), (b) lysine Na calls (v3) and Na_partial (L3641 rule),
(c) battery ratio (v3). NR1 for organisms already in L3625 is taken from rounds/L3625_tool_output.txt (not recomputed); H2 from L3669."""
import gzip,glob,pickle,re,runpy,collections
B=runpy.run_path('/home/claude/dcf-math/rounds/dcf_battery_v3_L3633.py',run_name='x'); N=B['N']; S4=re.compile(N['S4']); LYS=re.compile(N['LYS'])
sc=runpy.run_path('/home/claude/dcf-math/rounds/dcf_localalign_L3585.py')['score']
P,D=pickle.load(open('/home/claude/L3469/P6.pkl','rb'))
igr={g:p for g,p in P['mouse'].items() if re.match(r'(?i)^(gria\d|grik\d|grid\d|grin\d\w?)$',g)}
known={}
for l in open('rounds/L3625_tool_output.txt'):
    m=re.match(r'ORG (.+?)\s+proteins\s+\d+ iGluR\s+\d+ NR1\s+(\d+)',l)
    if m: known[m.group(1).strip().replace(' (FASTA)','')]=int(m.group(2))
known['Trichoplax sp. H2']=0
sets=[(sp,list(P[sp].values())) for sp in ['human','mouse','zebrafish','chicken','fly','worm']]
F=['/home/claude/L3501/z/early.tsv.gz','/home/claude/L3509/z/cteno.tsv.gz','/home/claude/L3533/z/bil.tsv.gz','/home/claude/L3557/z/oc.tsv.gz','/home/claude/L3605/z/nn.tsv.gz',
   '/home/claude/L3613/z/bat.tsv.gz','/home/claude/L3621/z/tard.tsv.gz','/home/claude/L3669/z3/h2.tsv.gz']+sorted(glob.glob('/home/claude/L3629/z/*.gz'))+sorted(glob.glob('/home/claude/L3637/z/*.gz'))+sorted(glob.glob('/home/claude/L3645/z/*.gz'))+['/home/claude/L3661/z/worm.tsv.gz']
for f in F:
    L=gzip.open(f,'rt').read().splitlines(); h=L[0].split('\t'); io,iq=h.index('Organism'),h.index('Sequence'); d=collections.defaultdict(list)
    for l in L[1:]: x=l.split('\t'); d[x[io].split(' (')[0]].append(x[iq])
    sets+=list(d.items())
sets.append(('Hofstenia miamia',list(N['proteins']('/home/claude/L3521/z/hmia.pep.fa.gz').values())))
seen=set()
for o,seqs in sets:
    if len(seqs)<5000 or o in seen: continue
    seen.add(o); na=part=ch=pu=0; nr1=known.get(o)
    if nr1 is None: nr1=0; compute=True
    else: compute=False
    for s in seqs:
        c=N['channel'](s); t=N['tags'](s)
        if c=='Na': na+=1
        elif 800<=len(s)<1500 and len(S4.findall(s))>=4 and LYS.search(s): part+=1
        if compute and 'iGluR' in t:
            v,r=max((sc(s,igr[g]),g) for g in igr); nr1+=(r=='Grin1')
    print('ORG %-30s proteins %6d NR1 %2d%s Na %3d Na_partial %2d'%(o[:30],len(seqs),nr1,'' if compute else '*',na,part),flush=True)
print('* NR1 taken from L3625/L3669 outputs')
