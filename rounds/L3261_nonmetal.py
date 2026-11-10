import sys
sys.argv=['x',sys.argv[1],'/home/claude/dcf-math/mrna/dcf_ire.py']
src=open('/home/claude/dcf-math/mrna/dcf_mrna_wide.py').read().split("if __name__")[0]
src=src.replace("PER=[3,11,12,19,20,23,24,26,29,30,34,39,40,56,63,64]","PER=[13,14,15,16,17,18,21,22,25,27,28,31,32,33,35,36,37,38,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,57,58,59,60,61,62]")
exec(src)
cds=[];utr=[]
for acc,desc,s in records(sys.argv[1]):
    if not acc.startswith('NM_'): continue
    a,b=ire.longest_orf(s); cds.append(s[a:b]); utr.append(s[:a]+s[b:])
for name,S in (('coding',cds),('UTR',utr)):
    for p,(r,lo,hi,nw) in spectrum_ratios(S).items(): print("%s period %d: ratio %.3f"%(name,p,r))
