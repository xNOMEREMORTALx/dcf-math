"""L3385 [Iron-free repair] (graded genomes, annotation): DNA-repair glycosylases present in lactic vs iron-using genomes."""
import re, glob, collections
lactic={'NC_013198','NC_004116','NC_007929','NC_008530','NC_005362','NC_009785','NC_010080','NC_013853','NC_015759','NC_008497','NC_010471','NC_008526','NC_009009'}
cats=[('EndoIII (Nth, Fe-S)',r'endonuclease iii(?! domain)|\bnth\b'),('MutY (Fe-S)',r'a/g-specific adenine glycosylase|mutY'),
      ('Fpg/MutM (Zn finger)',r'formamidopyrimidine|mutm|fpg'),('Nei / Endo VIII',r'endonuclease viii'),('UDG uracil glycosylase',r'uracil-dna glycosylase'),
      ('3-methyladenine glycosylase',r'3-methyladenine|alkylbase'),('Endo IV (Nfo, Zn)',r'endonuclease iv|deoxyribonuclease iv'),('Exo III (Xth)',r'exodeoxyribonuclease iii|exonuclease iii'),
      ('UvrABC excision',r'excinuclease abc'),('MutS/MutL mismatch',r'dna mismatch repair'),('RecA',r'recombinase reca|protein reca')]
gen={}
for f in glob.glob('/home/claude/L3*/g/*.gb'):
    a=f.split('/')[-1][:-3]
    if a in gen: continue
    t=open(f).read().split('\nORIGIN')[0].lower().replace('\n                     ',' ')
    prods=re.findall(r'/product="([^"]+)"',t)
    gen[a]={c:sum(bool(re.search(p,x)) for x in prods) for c,p in cats}
L=[a for a in gen if a in lactic]; I=[a for a in gen if a not in lactic]
print("lactic genomes %d, other genomes %d"%(len(L),len(I)))
print("%-30s %-24s %s"%("enzyme","lactic: genomes with it","others: genomes with it"))
for c,_ in cats:
    print("%-30s %2d of %-18d %d of %d"%(c,sum(gen[a][c]>0 for a in L),len(L),sum(gen[a][c]>0 for a in I),len(I)))
