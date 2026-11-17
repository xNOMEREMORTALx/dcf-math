"""L3749 frozen: the voltage sensor's charge spacing ("gear teeth") in UniProt-labelled channels, independent of DCF channel rules.
Data: reviewed Metazoa file (L3481; columns include Protein families and Sequence). Channels = Protein families matching
'Potassium channel family' (excluding 'Two pore'/'Inward rectifier'/'calcium-activated'), 'Sodium channel', or 'Calcium channel alpha-1'.
Run = >= 4 K/R at exactly spacing s (any residues between); s = 2, 3, 4. Teeth = longest run at spacing 3."""
import gzip,re,collections
L=gzip.open('/home/claude/L3481/z/metazoa.tsv.gz','rt').read().splitlines(); h=L[0].split('\t'); fi,qi=h.index('Protein families'),h.index('Sequence')
def run(s,k,n=4): return re.search('(?=[KR]'+('.'*(k-1)+'[KR]')*(n-1)+')',s) is not None
def teeth(s):
    best=0
    for i,c in enumerate(s):
        if c in 'KR':
            n=1
            while i+3*n<len(s) and s[i+3*n] in 'KR': n+=1
            best=max(best,n)
    return best
def is_ch(f):
    if re.search(r'Two pore|Inward rectifier|calcium-activated|Calcium-activated',f): return False
    return bool(re.search(r'Potassium channel family|Sodium channel|Calcium channel alpha-1',f))
ch=[];other=[]
for l in L[1:]:
    x=l.split('\t'); (ch if is_ch(x[fi]) else other).append((x[fi],x[qi]))
for name,S in [('channels',ch),('other proteins',other)]:
    print('%-15s n=%6d  spacing-2 %.4f  spacing-3 %.4f  spacing-4 %.4f'%(name,len(S),*[sum(run(s,k) for _,s in S)/len(S) for k in (2,3,4)]))
fam=collections.defaultdict(list)
for f,s in ch: fam[re.sub(r'\..*','',f.split(';')[0])[:60]].append(teeth(s))
print('teeth (longest spacing-3 K/R run) by family: median, max, n')
for k,v in sorted(fam.items(),key=lambda kv:-len(kv[1]))[:12]: v=sorted(v); print('  %-60s %2d %2d %4d'%(k,v[len(v)//2],v[-1],len(v)))
