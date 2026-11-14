"""Figure 4 (L3421): Ladder-P for all 24 protists. Hollow = development (used to set the cut), filled = blind (L3401, L3417)."""
import re, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
ens={'EAL60371':'Dictyostelium discoideum','ENY66069':'Entamoeba histolytica','KAE8302772':'Giardia intestinalis','PITG_':'Phytophthora infestans','EAR81369':'Tetrahymena thermophila','EED86244':'Thalassiosira pseudonana'}
anaer=['Entamoeba','Giardia','Trichomonas','Tritrichomonas','Blastocystis','Cryptosporidium','Spironucleus','Paratrimastix']
rows=[]
for l in open('/home/claude/dcf-math/rounds/L3421_all24_ladderp.txt'):
    kind,rest=l.split('|',1); name=rest.split(' | ')[0]
    for k,v in ens.items():
        if name.startswith(k): name=v
    name=re.sub(r' \(.*','',name); lp=float(re.search(r'ladderP ([\d.]+)',rest).group(1))
    rows.append((lp,name,kind.strip(),any(a in name for a in anaer)))
rows.sort()
BLUE,ORANGE,INK,MUTED,GRID,BG='#2a78d6','#eb6834','#0b0b0b','#52514e','#e6e5e0','#fcfcfb'
fig,ax=plt.subplots(figsize=(8.6,7.2),dpi=200); fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
for i,(lp,name,kind,an) in enumerate(rows):
    c=BLUE if an else ORANGE
    ax.scatter(lp,i,s=60,marker='o',facecolor=c if kind=='blind' else BG,edgecolor=c,linewidth=1.8,zorder=3)
ax.axvline(0.0017,color=MUTED,lw=0.9,ls=(0,(3,3)),zorder=1); ax.text(0.00175,len(rows)-0.4,'eukaryote cut 0.0017',fontsize=8,color=MUTED,va='top')
ax.set_xscale('log'); ax.set_xlim(0.0002,0.02); ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[1]+(' (token anaerobic enzymes)' if 'Naegleria' in r[1] else '') for r in rows],fontsize=8,color=INK,style='italic'); ax.tick_params(axis='y',length=0); ax.set_ylim(-0.8,len(rows)-0.2)
ax.set_xlabel('Ladder-P (C-x2-C-x2-C-x3-C-P) per 1,000 amino acids, log scale',fontsize=9,color=INK)
ax.grid(axis='x',color=GRID,lw=0.6,zorder=0); [ax.spines[s].set_visible(False) for s in ('top','right','left')]; ax.spines['bottom'].set_color(MUTED); ax.tick_params(colors=MUTED,labelsize=8)
for lab,c,f in (('oxygen-free, blind',BLUE,BLUE),('oxygen-free, development',BLUE,BG),('oxygen-breathing, blind',ORANGE,ORANGE),('oxygen-breathing, development',ORANGE,BG)):
    ax.scatter([],[],s=60,facecolor=f,edgecolor=c,linewidth=1.8,label=lab)
ax.legend(frameon=False,fontsize=8,loc='lower right',labelcolor=INK)
ax.set_title('24 protists on the proline-ending iron ladder: 10 of 10 blind calls correct\nhollow = used to set the cut; filled = tested blind afterwards (L3401, L3417)',loc='left',fontsize=10,color=INK)
fig.tight_layout(); fig.savefig('/home/claude/dcf-math/figures/L3421_protists_ladderp.png',facecolor=BG)
