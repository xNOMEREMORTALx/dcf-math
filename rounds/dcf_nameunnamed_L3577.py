"""L3577 frozen: name unnamed zebrafish K/HCN channel calls by their nearest mouse channel (dcf_align, BLOSUM62 identity),
then compare the nearest mouse subfamily with NCBI's own description subfamily.
Unnamed = symbol starting LOC, si:, zgc:, im:. Calls from the v8 channel rule (rounds/dcf_neurochem6_L3497.py).
Subfamily key: mouse Kcn<L> -> L in {a,b,c,d,f,g,h,q,s,v}; Hcn -> HCN. Description key: 'subfamily <L>' (letter) or 'hyperpolarization' -> HCN;
'shaker' -> a; 'shaw' -> c; 'shal' -> d; 'shab' -> b; 'KQT' -> q; 'eag'/'erg'/'elk' -> h."""
import gzip,re,pickle,runpy,collections
A=runpy.run_path('/home/claude/dcf-math/rounds/dcf_align_L3569.py'); idt=A['identity']
C=runpy.run_path('/home/claude/dcf-math/rounds/dcf_neurochem6_L3497.py',run_name='x'); chan=C['chan5']
P,D=pickle.load(open('/home/claude/L3469/P6.pkl','rb'))
ref={g:p for g,p in P['mouse'].items() if re.match(r'(?i)(kcn[abcdfghqsv]\d|hcn\d)',g) and chan(p) in ('K','HCN')}
fam=lambda g: 'HCN' if g.lower().startswith('hcn') else g[3].lower()
# zebrafish unnamed with descriptions
best={}
for f in ['/home/claude/L3441/z/zebrafish.1.rna.fna.gz','/home/claude/L3441/z/zebrafish.2.rna.fna.gz']:
    for blk in gzip.open(f,'rt').read().split('>')[1:]:
        h,_,s=blk.partition('\n'); m=re.findall(r'\(([A-Za-z0-9\-\.:]+)\)',h)
        if not m or not re.match(r'(LOC|si:|zgc:|im:)',m[-1]): continue
        p=C['orf'](s.replace('\n','').upper())
        if m[-1] not in best or len(p)>len(best[m[-1]][0]): best[m[-1]]=(p,h)
def dkey(h):
    h=h.lower()
    m=re.search(r'subfamily ([a-z])\b',h)
    if 'hyperpolarization' in h: return 'HCN'
    if m and 'potassium' in h: return m.group(1)
    for k,v in (('shaker','a'),('shaw','c'),('shal','d'),('shab','b'),('kqt','q'),('ether-a-go-go','h'),('eag','h'),('elk','h')):
        if k in h and 'potassium' in h: return v
    return None
rows=[]
for g,(p,h) in sorted(best.items()):
    c=chan(p)
    if c not in ('K','HCN'): continue
    sc=sorted(((idt(p,q),r) for r,q in ref.items()),reverse=True)[:2]
    rows.append((g,c,sc[0][1],fam(sc[0][1]),round(sc[0][0],3),dkey(h),h.split(' ',1)[1][:70]))
print('reference mouse channels:',len(ref))
for r in rows: print('  %-22s call %-3s nearest %-8s fam %-3s id %.3f | description fam %-4s | %s'%r)
graded=[r for r in rows if r[5]]; ok=[r for r in graded if r[3]==r[5]]
print('described unnamed calls %d, nearest-family agrees %d'%(len(graded),len(ok)))
print('RESULT',[('U1','ungradeable' if len(graded)<5 else ('PASS' if len(ok)/len(graded)>=0.8 else 'FAIL'))])
