import re, statistics as st, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
tier={'NC_013198':1,'NC_004116':1,'NC_007929':1,'NC_008530':1,'NC_012560':2,'NC_008686':2,'NC_014532':2,'NC_007651':2,
'NC_009495':3,'NC_009012':3,'NC_009718':3,'NC_011898':3,'NC_009515':4,'NC_011296':4,'NC_012438':4,'NC_008554':4}
R={};L={}
for l in open('/home/claude/dcf-math/rounds/L3273_zinc_ribbon.txt'):
    a=l.split()[0]; R[a]=float(re.search(r'ribbon per 1000 aa ([\d.]+)',l).group(1)); L[a]=float(re.search(r'ladder per 1000 aa ([\d.]+)',l).group(1))
BLUE,ORANGE,INK,MUTED,GRID='#2a78d6','#eb6834','#1a1a19','#6b6a63','#e6e5e0'
fig,ax=plt.subplots(figsize=(8,5),dpi=200); fig.patch.set_facecolor('#fcfcfb'); ax.set_facecolor('#fcfcfb')
for t in (1,2,3,4):
    ks=[a for a in tier if tier[a]==t]
    for j,a in enumerate(ks):
        dx=(j-1.5)*0.05
        ax.scatter(t-0.15+dx,L[a],s=46,color=BLUE,edgecolor='#fcfcfb',linewidth=1.5,zorder=3,label='Iron: ferredoxin ladder' if (t,j)==(1,0) else None)
        ax.scatter(t+0.15+dx,R[a],s=46,color=ORANGE,edgecolor='#fcfcfb',linewidth=1.5,zorder=3,marker='D',label='Zinc: ribbon knuckle' if (t,j)==(1,0) else None)
    for off,D,c in ((-0.15,L,BLUE),(0.15,R,ORANGE)):
        m=st.median(D[a] for a in ks); ax.plot([t+off-0.13,t+off+0.13],[m,m],color=c,lw=2,zorder=2)
for y in (0.0045,0.023,0.060): ax.axhline(y,color=MUTED,lw=0.8,ls=(0,(3,3)),zorder=1)
[ax.text(4.88,y+0.0015,lab,ha='right',va='bottom',fontsize=8,color=MUTED) for y,lab in ((0.060,'iron cut 0.060'),(0.023,'iron cut 0.023'),(0.0045,'iron cut 0.0045'))]
ax.annotate('Sulfurihydrogenibium\n(microaerophile)',(4-0.15+0.025,0.0474),xytext=(2.55,0.12),fontsize=8,color=MUTED,arrowprops=dict(arrowstyle='-',color=MUTED,lw=0.7))
ax.set_xticks([1,2,3,4]); ax.set_xticklabels(['1 lactic\nfermenters','2 oxygen\nrespirers','3 H2-making\nfermenters','4 ferredoxin-\nbased'],color=INK,fontsize=9)
ax.set_xlim(0.5,4.9); ax.set_ylim(0,0.235); ax.set_ylabel('motifs per 1,000 amino acids',color=INK,fontsize=9)
ax.grid(axis='y',color=GRID,lw=0.6); ax.set_axisbelow(True)
for s in ('top','right'): ax.spines[s].set_visible(False)
for s in ('left','bottom'): ax.spines[s].set_color(MUTED)
ax.tick_params(colors=MUTED,labelsize=8)
ax.set_title('Iron climbs 64× across the energy tiers; zinc only 2.3×\nblind_20, 16 fresh genomes (L3269/L3273); lines = tier medians',loc='left',fontsize=10,color=INK)
ax.legend(frameon=False,fontsize=8,loc='upper left',labelcolor=INK)
fig.tight_layout(); fig.savefig('/home/claude/dcf-math/figures/L3277_iron_zinc_tiers.png',facecolor=fig.get_facecolor())
