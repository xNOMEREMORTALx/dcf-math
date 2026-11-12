"""L3301 [Neuro map]: label-free 'electrical parts list' of human mRNA files 1-4 from the voltage sensor (passed L3293 N2).
Class by shape only: 4-domain (>= 1500 aa) = Na/Ca-type; 1-domain with K filter [TSC][VIT]G[YF]G = K-type
(C-I-G-Y-G = HCN-type); other voltage-sensor proteins = 'other'. Gene names are read only afterwards, to check."""
import gzip, re, collections
exec(open('/home/claude/dcf-math/rounds/dcf_neuro_motifs_L3293.py').read().split('genes = {}')[0])
genes={}
for path in ['/home/claude/L3261/in/human.1.rna.fna.gz','/home/claude/L3261/in/human.2.rna.fna.gz','/home/claude/L3269/rna_in/human.3.rna.fna.gz','/home/claude/L3269/rna_in/human.4.rna.fna.gz']:
    for blk in gzip.open(path,'rt').read().split('>')[1:]:
        h,_,s=blk.partition('\n'); acc=h.split()[0]
        if not acc.startswith('NM_'): continue
        m=re.search(r'\(([A-Za-z0-9\-\.]+)\)',h); g=m.group(1) if m else acc
        num=int(re.sub(r'\D','',acc.split('.')[0]))
        if g not in genes or num<genes[g][0]: genes[g]=(num,s.replace('\n','').upper())
cls=collections.defaultdict(list)
for g,(_,s) in genes.items():
    p=orf(s); s4=len(re.findall(MOT['S4'],p))
    if not s4: continue
    kf=re.search(r'[TSC][VIT]G[YF]G',p)
    c='Na/Ca 4-domain' if len(p)>=1500 else ('HCN-type (CIGYG)' if re.search('CIGYG',p) else ('K-type' if kf else 'other'))
    cls[c].append((g,len(p),s4))
truth=lambda g: 'Na' if g.startswith('SCN') else 'Ca' if g.startswith(('CACNA1','CATSPER','TPCN')) else 'HCN' if g.startswith('HCN') else 'K' if g.startswith(('KCN',)) else '-'
print("genes scanned",len(genes))
for c in ['Na/Ca 4-domain','K-type','HCN-type (CIGYG)','other']:
    L=sorted(cls[c]); t=collections.Counter(truth(g) for g,_,_ in L)
    print("\n%s: %d genes | by name afterwards: %s"%(c,len(L),dict(t)))
    print("  "+", ".join("%s(%d aa, S4 x%d)"%x for x in L))
