"""L3373 [Acetylcholine] development on human mRNA files 1-4 (one transcript per gene, longest ORF): label-free motifs, then gene names."""
import gzip, re, sys
sys.path.insert(0,'/home/claude/dcf-genefinder'); import dcf_motif_scan as M
genes={}
for path in ['/home/claude/L3261/in/human.1.rna.fna.gz','/home/claude/L3261/in/human.2.rna.fna.gz','/home/claude/L3269/rna_in/human.3.rna.fna.gz','/home/claude/L3269/rna_in/human.4.rna.fna.gz']:
    for blk in gzip.open(path,'rt').read().split('>')[1:]:
        h,_,s=blk.partition('\n'); acc=h.split()[0]
        if not acc.startswith('NM_'): continue
        m=re.search(r'\(([A-Za-z0-9\-\.]+)\)',h); g=m.group(1) if m else acc
        num=int(re.sub(r'\D','',acc.split('.')[0]))
        if g not in genes or num<genes[g][0]: genes[g]=(num,s.replace('\n','').upper())
P={g:M.longest_orf(s) for g,(_,s) in genes.items()}
mot={'Cys-loop (corrected, ACh/GABA/Gly/5-HT receptors)':r'C.{4,6}[FY]P[FYWM]D.{3}C','cholinesterase serine site FGESAG':r'FGESAG','ladder C..C..C...C (any)':r'C..C..C...C'}
fam={'Cys-loop (corrected, ACh/GABA/Gly/5-HT receptors)':r'^(CHRN|GABR|GLR[AB]|HTR3|ZACN)','cholinesterase serine site FGESAG':r'^(ACHE|BCHE)$'}
print("genes:",len(P))
for k,pat in mot.items():
    hits=sorted(g for g,p in P.items() if re.search(pat,p))
    if k in fam:
        F=set(g for g in P if re.match(fam[k],g)); tp=set(hits)&F
        print("%s: %d hits | family present %d, found %d | hits: %s | missed: %s"%(k,len(hits),len(F),len(tp),' '.join(hits),' '.join(sorted(F-set(hits)))))
ach=[g for g in P if re.match(r'^(CHRN|ACHE|BCHE|CHAT|SLC5A7|SLC18A3|SLC44A\d|CHKA|CHKB|PCYT1)',g)]
print("acetylcholine/choline genes present:",' '.join(sorted(ach)))
for g in sorted(g for g in P if g.startswith('SLC44A')):
    p=P[g]; print("  %s (%d aa): ladders %d, ladder followed by P %d"%(g,len(p),len(re.findall(r'(?=C..C..C...C)',p)),len(re.findall(r'(?=C..C..C...CP)',p))))
