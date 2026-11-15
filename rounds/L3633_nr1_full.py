"""L3633 descriptive v3: align EVERY 600-1600 aa protein of sea urchin and Ciona to mouse Grin1 (k-mer prefilters failed: L3633_nr1_search*.txt).
Prints the top 8 by Grin1 score; Hydra's NR1 scores 1616-1766 (positive control, L3633_nr1_search.txt)."""
import gzip,pickle,runpy
sc=runpy.run_path('/home/claude/dcf-math/rounds/dcf_localalign_L3585.py')['score']
P,D=pickle.load(open('/home/claude/L3469/P6.pkl','rb')); g1=P['mouse']['Grin1']
for f,org in [('/home/claude/L3557/z/oc.tsv.gz','Ciona'),('/home/claude/L3533/z/bil.tsv.gz','Strongylocentrotus')]:
    rows=[l.split('\t') for l in gzip.open(f,'rt').read().splitlines()[1:] if l.split('\t')[1].startswith(org) and 600<=len(l.split('\t')[3])<=1600]
    res=sorted(((sc(s,g1),a,len(s),n) for a,o,n,s in rows),reverse=True)[:8]
    print('##',org,'aligned',len(rows))
    for v,a,n,nm in res: print('  %-11s %5d Grin1 %5d | %s'%(a,n,v,nm[:60]),flush=True)
