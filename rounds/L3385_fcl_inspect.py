import re, glob
lactic={'NC_013198','NC_004116','NC_007929','NC_008530','NC_005362','NC_009785','NC_010080','NC_013853','NC_015759','NC_008497','NC_010471','NC_008526','NC_009009'}
done=set(); rows=[]
for f in sorted(glob.glob('/home/claude/L3*/g/*.gb')):
    a=f.split('/')[-1][:-3]
    if a in done: continue
    done.add(a); t=open(f).read().split('\nORIGIN')[0]
    for feat in re.split(r'\n     CDS             ',t)[1:]:
        ff=feat.replace('\n                     ',' ')
        pr=re.search(r'/product="([^"]+)"',ff); tr=re.search(r'/translation="([^"]+)"',ff)
        if not pr or not tr: continue
        p=pr.group(1).lower()
        if not (re.search(r'endonuclease iii(?! domain)',p) or 'a/g-specific adenine glycosylase' in p): continue
        s=tr.group(1).replace(' ','')
        tail=s[-90:] if 'endonuclease' in p else s[150:260]
        fcl=bool(re.search(r'C.{6}C..C.{5}C',s)); nC=s.count('C')
        rows.append((a in lactic,a,('EndoIII' if 'endonuclease' in p else 'MutY'),len(s),nC,fcl,re.sub(r'[^C]','.',s)[-80:] if 'endonuclease' in p else ''))
for lac in (True,False):
    R=[r for r in rows if r[0]==lac]
    for enz in ('EndoIII','MutY'):
        X=[r for r in R if r[2]==enz]
        print("%s %s: %d proteins, with FCL motif %d, median cysteines %s"%('LACTIC' if lac else 'others',enz,len(X),sum(r[5] for r in X),sorted(r[4] for r in X)[len(X)//2] if X else '-'))
print("\nlactic EndoIII, cysteine positions in last 80 aa:")
for r in rows:
    if r[0] and r[2]=='EndoIII': print("  %s len %d C=%d FCL=%s  %s"%(r[1],r[3],r[4],r[5],r[6]))
print("example non-lactic EndoIII:")
for r in [r for r in rows if not r[0] and r[2]=='EndoIII'][:4]: print("  %s len %d C=%d FCL=%s  %s"%(r[1],r[3],r[4],r[5],r[6]))
