import gzip, re, sys, glob, os
sys.path.insert(0,'/home/claude/dcf-genefinder'); import dcf_redox as R
exec(open('/home/claude/dcf-math/rounds/dcf_neuro_motifs_L3293.py').read().split('H = ')[0].split('genes = {}')[0])
HH = r'H[YF]EGRA[VI]D.{40,80}GCF'
hits=[]; n=0
for f in ['L3261/in/human.1.rna.fna.gz','L3261/in/human.2.rna.fna.gz','L3269/rna_in/human.3.rna.fna.gz','L3269/rna_in/human.4.rna.fna.gz']:
    for blk in gzip.open(f,'rt').read().split('>')[1:]:
        h,_,s=blk.partition('\n')
        if not h.startswith('NM_'): continue
        n+=1; p=orf(s.replace('\n','').upper())
        if re.search(HH,p): hits.append(h[:90])
print("human NM transcripts scanned",n,"hedgehog hits:",hits)
tot=0; mh=0
for d in ['L3213','L3221','L3229','L3241','L3269','L3273','L3285','L3293','L3181','L3185']:
    for g in glob.glob(f'/home/claude/{d}/g/*.gb'):
        a=os.path.basename(g)[:-3]; ff=f'/home/claude/{d}/out/{a}.gff3'
        if not os.path.exists(ff): continue
        tot+=1
        for p in R.proteins(R.read_seq(g),ff):
            if re.search(HH,p): mh+=1
print("microbial genomes scanned",tot,"hedgehog hits",mh)
