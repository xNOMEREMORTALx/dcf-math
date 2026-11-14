"""Descriptive: nucleotide periodicity spectrum of mRNA coding the voltage-sensor S4 helix vs random coding windows (human 1-4, mouse 1-3)."""
import gzip,re,random,math
exec(open('/home/claude/dcf-math/rounds/dcf_neurometal_L3425.py').read().split("if __name__")[0])
def orf_nt(s):
    best=('',0)
    for f in range(3):
        p=''.join(CODE.get(s[i:i+3],'X') for i in range(f,len(s)-2,3)); pos=0
        for seg in p.split('*'):
            k=seg.find('M')
            if k>=0 and len(seg)-k>len(best[0]): best=(seg[k:], f+3*(pos+k))
            pos+=len(seg)+1
    return best
F=['/home/claude/L3261/in/human.1.rna.fna.gz','/home/claude/L3261/in/human.2.rna.fna.gz','/home/claude/L3269/rna_in/human.3.rna.fna.gz','/home/claude/L3269/rna_in/human.4.rna.fna.gz','/home/claude/L3377/z/mouse.1.rna.fna.gz','/home/claude/L3377/z/mouse.2.rna.fna.gz','/home/claude/L3429/z/mouse.3.rna.fna.gz']
W=45
s4w=[];ctl=[];rng=random.Random(1)
for f in F:
    for blk in gzip.open(f,'rt').read().split('>')[1:]:
        h,_,s=blk.partition('\n')
        if not h.startswith('NM_'): continue
        s=s.replace('\n','').upper(); p,st=orf_nt(s)
        if len(p)<300: continue
        ms=[m.start() for m in re.finditer(S4,p)]
        for a in ms[:3]:
            for off,lab in ((-30,'before'),(0,'motif'),(30,'after')):   # 30 codons = 90 nt away, no overlap with the 13-aa motif
                b=a+off
                if b<0: continue
                nt=s[st+3*b:st+3*b+W]
                if len(nt)==W: s4w.append((lab,nt))
        if ms or rng.random()<0.05:
            a=rng.randrange(0,len(p)-20); nt=s[st+3*a:st+3*a+W]
            if len(nt)==W and not ms: ctl.append(nt)
def spec(ws):
    out={}
    for per in range(2,16):
        tot=0
        for w in ws:
            for b in 'ACGT':
                x=[1.0 if c==b else 0.0 for c in w]; m=sum(x)/len(x)
                re_=sum((x[i]-m)*math.cos(2*math.pi*i/per) for i in range(len(x))); im=sum((x[i]-m)*math.sin(2*math.pi*i/per) for i in range(len(x)))
                tot+=re_*re_+im*im
        out[per]=tot/len(ws)
    return out
b=spec(ctl)
print('control windows',len(ctl))
for lab in ('before','motif','after'):
    ws=[w for l,w in s4w if l==lab]; a=spec(ws)
    print(lab,len(ws),' '.join('p%d=%.2f'%(per,a[per]/b[per]) for per in (3,6,9,12)))
