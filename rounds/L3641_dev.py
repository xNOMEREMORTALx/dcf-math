"""L3641 development: (a) fragment rescue: 800-1499 aa, >=4 S4 matches (v3 S4 regex, overlapping lookahead count), v3 lysine loop -> Na_partial;
(b) every [TS]WK[GA]W protein >= 800 aa. All protein sets seen (L3469 P6 + every UniProt file through L3637). Names read here (development)."""
import gzip,pickle,runpy,glob,re
V3=runpy.run_path('/home/claude/dcf-math/rounds/dcf_nerve_v3_L3633.py',run_name='x'); S4=re.compile(V3['S4']); LYS=re.compile(V3['LYS'])
P,D=pickle.load(open('/home/claude/L3469/P6.pkl','rb'))
sets=[(sp,[(g,'',s) for g,s in d.items()]) for sp,d in P.items()]
F=['/home/claude/L3481/z/metazoa.tsv.gz','/home/claude/L3501/z/early.tsv.gz','/home/claude/L3509/z/cteno.tsv.gz','/home/claude/L3533/z/bil.tsv.gz','/home/claude/L3557/z/oc.tsv.gz',
   '/home/claude/L3605/z/nn.tsv.gz','/home/claude/L3613/z/bat.tsv.gz','/home/claude/L3621/z/tard.tsv.gz']+sorted(glob.glob('/home/claude/L3629/z/*.gz'))+sorted(glob.glob('/home/claude/L3637/z/*.gz'))
for f in F:
    L=gzip.open(f,'rt').read().splitlines(); h=L[0].split('\t'); ie=h.index('Entry'); iq=h.index('Sequence'); io=h.index('Organism')
    ip=h.index('Protein names') if 'Protein names' in h else (h.index('Protein families') if 'Protein families' in h else None)
    sets.append((f.split('/')[-1],[(x[ie]+'|'+x[io].split(' (')[0][:22],x[ip] if ip is not None else '',x[iq]) for x in (l.split('\t') for l in L[1:])]))
for name,items in sets:
    for k,n,s in items:
        frag=800<=len(s)<1500 and len(S4.findall(s))>=4 and LYS.search(s) and V3['channel'](s)!='Na'
        w=len(s)>=800 and re.search(r'[TS]WK[GA]W',s)
        if frag: print('FRAG',name,k,len(s),len(S4.findall(s)),LYS.search(s).group(),'|',n[:70])
        if w: print('WLOOP',name,k,len(s),V3['channel'](s),re.search(r'.{4}[TS]WK[GA]W.{3}',s).group() if re.search(r'.{4}[TS]WK[GA]W.{3}',s) else '','|',n[:70])
