import json, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
c=json.load(open('/home/claude/L3325/fam_counts.json'))
fams=[('Hydrogenases','#2a78d6'),('PFOR / 2-oxoacid:Fd','#eb6834'),('Hdr + bifurcating flavoproteins','#1baf7a'),('Rnf / complex I-type pumps','#eda100'),('Other Fe-S / other','#c9c8c2')]
tiers=['1','2','3','4']; lab=['1 lactic\nfermenters','2 oxygen\nrespirers','3 H2-making\nfermenters','4 ferredoxin-\nbased']
INK,MUTED,GRID,BG='#0b0b0b','#52514e','#e6e5e0','#fcfcfb'
fig,ax=plt.subplots(figsize=(8,5),dpi=200); fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
bottom=[0]*4
for name,col in fams:
    v=[c[t].get(name,0)/4 for t in tiers]
    ax.bar(range(4),v,bottom=bottom,color=col,edgecolor=BG,linewidth=2,width=0.6,label=name,zorder=3)
    bottom=[b+x for b,x in zip(bottom,v)]
for i,b in enumerate(bottom): ax.text(i,b+1.5,'%.0f'%b,ha='center',va='bottom',fontsize=9,color=INK)
ax.set_xticks(range(4)); ax.set_xticklabels(lab,fontsize=9,color=INK)
ax.set_ylabel('3-3-4 ladders in proteins > 200 aa, per genome',fontsize=9,color=INK)
ax.grid(axis='y',color=GRID,lw=0.6,zorder=0); [ax.spines[s].set_visible(False) for s in ('top','right')]
[ax.spines[s].set_color(MUTED) for s in ('left','bottom')]; ax.tick_params(colors=MUTED,labelsize=8)
ax.set_title('What the iron ladder counts: ferredoxin-coupled energy enzymes\nblind_20 genomes (4 per tier, graded L3269/L3273); development analysis L3325',loc='left',fontsize=10,color=INK)
h,l=ax.get_legend_handles_labels(); ax.legend(h[::-1],l[::-1],frameon=False,fontsize=8,loc='upper left',labelcolor=INK)
fig.tight_layout(); fig.savefig('/home/claude/dcf-math/figures/L3329_enzyme_families.png',facecolor=BG)
