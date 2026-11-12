"""L3289 development on seen genomes: plant-type [2Fe-2S] ferredoxin motif C-x4-C-x2-C-x(27..31)-C."""
import sys, re, glob, os
sys.path.insert(0,'/home/claude/dcf-genefinder'); import dcf_redox as R
for d in ('/home/claude/L3269','/home/claude/L3273','/home/claude/L3285'):
    for g in sorted(glob.glob(d+'/g/*.gb')):
        a=os.path.basename(g)[:-3]; f=f'{d}/out/{a}.gff3'
        seq=R.read_seq(g); n=c=0
        for p in R.proteins(seq,f): n+=len(p); c+=len(re.findall(r'(?=C....C..C.{27,31}C)',p))
        defn=open(g).read(2000).split('DEFINITION')[1].split(',')[0].split('\n')[0].strip()
        print("%-10s %-45s fd2 %.4f"%(a,defn[:45],1000*c/n))
