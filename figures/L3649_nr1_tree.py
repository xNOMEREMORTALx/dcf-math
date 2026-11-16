"""Manuscript 2, Figure 9: NMDA NR1 calls (nearest mouse Grin1, local aligner) per proteome, ordered on the tree (rounds/L3625_tool_output.txt)."""
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
rows=[('Capsaspora (filasterean)',0,0,'protists'),('Monosiga (choanoflagellate)',0,0,'protists'),('Salpingoeca (choanoflagellate)',0,0,'protists'),
 ('Amphimedon (sponge)',0,0,'sponges'),('Geodia (sponge)',0,0,'sponges'),('Ephydatia (sponge)',0,0,'sponges'),('Oopsacas (sponge)',0,0,'sponges'),
 ('Mnemiopsis (comb jelly)',11,0,'comb jelly'),('Trichoplax (placozoan)',8,0,'placozoan'),('Nematostella (sea anemone)',9,1,'cnidarians'),('Hydra',3,3,'cnidarians'),
 ('Hofstenia (acoel)',15,3,'bilaterians'),('Capitella (annelid)',16,1,'bilaterians'),('Lingula (brachiopod)',12,1,'bilaterians'),('Aplysia (sea hare)',33,4,'bilaterians'),
 ('Hypsibius (tardigrade)',9,1,'bilaterians'),('Ramazzottius (tardigrade)',10,2,'bilaterians'),('Strongylocentrotus (sea urchin)',7,0,'bilaterians'),
 ('Saccoglossus (acorn worm)',10,2,'bilaterians'),('Branchiostoma (lancelet)',48,1,'bilaterians'),('Ciona (sea squirt)',6,0,'bilaterians')]
fig,ax=plt.subplots(figsize=(7.5,6),dpi=150)
for i,(n,ig,nr,g) in enumerate(rows):
    y=len(rows)-1-i
    if nr: ax.barh(y,nr,color='#2b6cb0',height=0.62)
    else: ax.plot(0,y,marker='o',ms=6,mfc='white',mec='#c05621',mew=1.3)
    ax.text(max(nr,0)+0.18,y,'%d NR1 · %d iGluR'%(nr,ig),va='center',fontsize=7.5,color='#24292f')
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows][::-1],fontsize=8); ax.set_xlim(-0.3,6.5)
for s in ('top','right'): ax.spines[s].set_visible(False)
ax.set_xlabel('NR1 calls (nearest mouse Grin1)',color='#6e7781')
from matplotlib.lines import Line2D
ax.legend(handles=[Line2D([],[],color='#2b6cb0',lw=6,label='NR1 found'),Line2D([],[],marker='o',ls='',mfc='white',mec='#c05621',label='no NR1 call')],fontsize=8,frameon=False,loc='lower right')
ax.set_title('The NMDA learning switch (NR1) first appears in cnidarians',fontsize=10.5,loc='left')
plt.tight_layout(); plt.savefig('figures/L3649_nr1_tree.png')
