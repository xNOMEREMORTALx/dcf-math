"""L3373 [Proline] development: residue after the ladder's 4th cysteine, by tier (graded prokaryotes), protists, human."""
import sys, re, gzip, glob, collections
sys.path.insert(0,'/home/claude/dcf-genefinder'); import dcf_redox as R
sets={'/home/claude/L3269':{'NC_013198':1,'NC_004116':1,'NC_007929':1,'NC_012560':2,'NC_008686':2,'NC_014532':2,'NC_007651':2,'NC_009495':3,'NC_009012':3,'NC_009718':3,'NC_011898':3,'NC_009515':4,'NC_011296':4,'NC_012438':4,'NC_008554':4},
 '/home/claude/L3273':{'NC_008530':1},'/home/claude/L3285':{'NC_005362':1,'NC_009785':1,'NC_003551':4,'NC_013223':4},
 '/home/claude/L3293':{'NC_007604':2,'NC_003272':2,'NC_004113':2,'NC_005125':2,'NC_010337':4},
 '/home/claude/L3333':{'NC_010080':1,'NC_013853':1,'NC_015759':1,'NC_003295':2,'NC_007761':2,'NC_009848':2,'NC_008593':3,'NC_009616':3,'NC_014393':3,'NC_013665':4,'NC_015388':4,'NC_014378':4}}
nxt={t:collections.Counter() for t in (1,2,3,4)}
for d,T in sets.items():
    for a,t in T.items():
        for p in R.proteins(R.read_seq(f'{d}/g/{a}.gb'),f'{d}/out/{a}.gff3'):
            for m in re.finditer(r'(?=C..C..C...C(.))',p): nxt[t][m.group(1)]+=1
def show(lab,c):
    n=sum(c.values()); print("%-34s n=%4d  P %4.0f%%  top: %s"%(lab,n,100*c['P']/max(n,1),' '.join('%s%.0f'%(k,100*v/n) for k,v in c.most_common(5))))
print("Residue after the 4th ladder cysteine")
for t in (2,3,4): show("prokaryote tier %d"%t,nxt[t])
an=collections.Counter(); ae=collections.Counter()
groups={'anaerobe':['Entamoeba','Giardia','Trichomonas','Blastocystis','Cryptosporidium','Spironucleus'],'aerobe':['Dictyostelium','Phytophthora','Tetrahymena','Thalassiosira','Leishmania','Trypanosoma','Chlamydomonas']}
for f in glob.glob('/home/claude/L3353/z/*.gz')+['/home/claude/L3357/tvag.fasta.gz']+glob.glob('/home/claude/L3365/z/*'):
    t=gzip.open(f,'rt').read(); nm=f+(re.search(r'OS=(\S+)',t[:3000]).group(1) if 'OS=' in t[:3000] else '')
    g='anaerobe' if any(x in nm for x in groups['anaerobe']) else 'aerobe' if any(x in nm for x in groups['aerobe']) else None
    if not g: continue
    for b in t.split('>')[1:]:
        s=b.partition('\n')[2].replace('\n','')
        for m in re.finditer(r'(?=C..C..C...C(.))',s): (an if g=='anaerobe' else ae)[m.group(1)]+=1
show("anaerobic protists (6)",an); show("aerobic protists (7)",ae)
h=collections.Counter(); seen=set()
for f in ['/home/claude/L3313/p/human.1.protein.faa.gz','/home/claude/L3313/p/human.2.protein.faa.gz']:
    for b in gzip.open(f,'rt').read().split('>')[1:]:
        hd,_,s=b.partition('\n'); k=re.sub(r' isoform.*','',hd.split(' ',1)[1].split(' [')[0])
        if k in seen: continue
        seen.add(k)
        for m in re.finditer(r'(?=C..C..C...C(.))',s.replace('\n','')): h[m.group(1)]+=1
show("human look-alikes (5,390 proteins)",h)
