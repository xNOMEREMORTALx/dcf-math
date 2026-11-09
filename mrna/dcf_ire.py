"""dcf_ire.py - label-free iron-responsive-element (IRE) scanner for mRNA (DCF, Gary NOMEREMORTAL Mason). Frozen L3245.
Model (DNA letters, T = U): 5'-[lower stem 3]-C-[upper stem 5]-CAGTGN-[upper stem 5']-[lower stem 3']-3'
 - loop CAGTG + any base (the CAGUGN hexaloop); the C bulge sits unpaired between lower and upper stem on the 5' side;
 - upper stem: 5 pairs, Watson-Crick or G-U, at most 1 mismatch; lower stem: 3 pairs, at most 1 mismatch.
CDS = longest ATG..stop ORF on the + strand (label-free); 5' UTR = before it, 3' UTR = after it.
Usage: python3 -I dcf_ire.py file.gb   (multi-record GenBank)   -> one line per record."""
import re, sys
P={('A','T'),('T','A'),('G','C'),('C','G'),('G','T'),('T','G')}
def pairs(a,b): return sum((x,y) in P for x,y in zip(a,b[::-1]))
def scan(s):
    hits=[]
    for m in re.finditer(r'(?=CAGTG[ACGT])',s):
        i=m.start()
        if i<9 or i+14>len(s): continue
        up_l=s[i-5:i]; up_r=s[i+6:i+11]; lo_l=s[i-9:i-6]; lo_r=s[i+11:i+14]
        if s[i-6]=='C' and pairs(up_l,up_r)>=4 and pairs(lo_l,lo_r)>=2: hits.append(i)
    return hits
def longest_orf(s):
    best=(0,0)
    for f in range(3):
        i=f
        while i<len(s)-2:
            if s[i:i+3]=='ATG':
                j=i
                while j<len(s)-2 and s[j:j+3] not in ('TAA','TAG','TGA'): j+=3
                if j-i>best[1]-best[0]: best=(i,j+3)
                i=j+3
            else: i+=3
    return best
if __name__=='__main__':
    txt=open(sys.argv[1]).read()
    for rec in txt.split('\n//'):
        if 'ORIGIN' not in rec: continue
        acc=re.search(r'LOCUS\s+(\S+)',rec).group(1)
        d=re.search(r'DEFINITION\s+(.*?)\n\S',rec,re.S); d=' '.join(d.group(1).split()) if d else ''
        s=re.sub(r'[^ACGT]','N',''.join(re.findall(r'[A-Za-z]+',rec.split('ORIGIN')[1])).upper())
        a,b=longest_orf(s); H=scan(s)
        where=['5UTR' if h<a else ('3UTR' if h>=b else 'CDS') for h in H]
        print("%s\tlen %d\tCDS %d-%d\tIRE hits %d %s\t%s"%(acc,len(s),a+1,b,len(H),','.join('%s@%d'%(w,h+1) for w,h in zip(where,H)),d[:70]))
