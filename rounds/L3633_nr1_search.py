"""L3633 descriptive (after L3625 grading): any NR1 hidden in sea urchin / Ciona UniProt sets? v2: proteins 600-1600 aa ranked by shared 3-mers per residue (v1 favoured giant proteins; Hydra control failed) with mouse Grin1, align top 25."""
import gzip,pickle,re,runpy
sc=runpy.run_path('/home/claude/dcf-math/rounds/dcf_localalign_L3585.py')['score']
P,D=pickle.load(open('/home/claude/L3469/P6.pkl','rb'))
ref={g:p for g,p in P['mouse'].items() if re.match(r'(?i)^(gria\d|grik\d|grid\d|grin\d\w?)$',g)}
g1=P['mouse']['Grin1']; K=set(g1[i:i+3] for i in range(len(g1)-2))
for f,org in [('/home/claude/L3533/z/bil.tsv.gz','Strongylocentrotus'),('/home/claude/L3557/z/oc.tsv.gz','Ciona'),('/home/claude/L3613/z/bat.tsv.gz','Hydra')]:
    rows=[l.split('\t') for l in gzip.open(f,'rt').read().splitlines()[1:] if l.split('\t')[1].startswith(org)]
    rows=[x for x in rows if 600<=len(x[3])<=1600]; top=sorted(rows,key=lambda x:-len(K&set(x[3][i:i+3] for i in range(len(x[3])-2)))/len(x[3]))[:25]
    print('##',org,len(rows))
    for a,o,n,s in top:
        v,r=max((sc(s,ref[x]),x) for x in ref); print('  %-11s %5d nearest %-7s %5d Grin1 %5d | %s'%(a,len(s),r,v,sc(s,g1),n[:50]),flush=True)
