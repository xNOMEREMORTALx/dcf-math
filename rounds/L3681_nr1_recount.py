"""L3681 descriptive recount: NR1 per organism with the floored caller (dcf_nr1_L3681). Organisms whose per-call scores are already in
L3625/L3669/L3677 outputs are recounted from those lines (floor applied); the rest are recomputed with the caller."""
import gzip,glob,re,runpy,collections,pickle
C=runpy.run_path('/home/claude/dcf-math/rounds/dcf_nr1_L3681.py'); nr1=C['nr1']; FL=C['FLOOR']
out={}
org=None
for l in open('rounds/L3625_tool_output.txt'):
    if l.startswith('ORG'): org=re.match(r'ORG (.+?)\s+proteins',l).group(1).strip().replace(' (FASTA)',''); out[org]=[0,0]
    elif l.startswith('    ') and org:
        x=l.split(); out[org][0]+=x[2]=='Grin1'; out[org][1]+=(x[2]=='Grin1' and int(x[3])>=FL)
for f,o in [('rounds/L3669_tool_output.txt','Trichoplax sp. H2')]:
    L=[l.split() for l in open(f) if l.startswith('IGLUR')]; out[o]=[sum(x[4]=='Grin1' for x in L),sum(x[4]=='Grin1' and int(x[5])>=FL for x in L)]
o=None
for l in open('rounds/L3677_tool_output.txt'):
    if l.startswith('### '): o=l.split()[1]; out[o]=[0,0]
    elif l.startswith('IGLUR'): x=l.split(); out[o][0]+=x[4]=='Grin1'; out[o][1]+=(x[4]=='Grin1' and int(x[5])>=FL)
P,D=pickle.load(open('/home/claude/L3469/P6.pkl','rb'))
todo=[(sp,list(P[sp].values())) for sp in ['human','mouse','zebrafish','chicken','fly']]
for f in sorted(glob.glob('/home/claude/L3629/z/*.gz'))+sorted(glob.glob('/home/claude/L3637/z/*.gz'))+sorted(glob.glob('/home/claude/L3645/z/*.gz'))+['/home/claude/L3661/z/worm.tsv.gz']:
    L=gzip.open(f,'rt').read().splitlines(); h=L[0].split('\t'); io,iq=h.index('Organism'),h.index('Sequence'); d=collections.defaultdict(list)
    for l in L[1:]: x=l.split('\t'); d[x[io].split(' (')[0]].append(x[iq])
    todo+=list(d.items())
for o2,seqs in todo:
    a=b=0
    for s in seqs:
        ok,r,v=nr1(s)
        if r=='Grin1': a+=1; b+=ok
    out[o2]=[a,b]; print('computed',o2,a,b,flush=True)
print('ORGANISM'.ljust(32),'NR1 no floor','NR1 floor 1000')
for o2,(a,b) in out.items(): print(o2[:32].ljust(32),str(a).rjust(6),str(b).rjust(12),'  <-- changes' if a!=b else '')
