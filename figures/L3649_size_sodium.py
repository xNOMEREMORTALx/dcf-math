"""Manuscript 2, Figure 8: battery ratio vs voltage-gated sodium channel in 10 nerve-bearing animals tested blind L3613-L3645
(ratios from rounds/L3613_grade_output.txt, L3621, L3629 (v2), L3637, L3645 tool outputs). Hatched = no voltage-gated Na channel."""
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
rows=[('Ramazzottius (tardigrade, <1 mm)',1.53,0),('Hypsibius (tardigrade, <1 mm)',1.54,0),('Brachionus calyciflorus (rotifer, 0.3 mm)',1.93,1),
      ('Brachionus plicatilis (rotifer, 0.3 mm)',2.57,1),('Helobdella (leech, cm)',2.77,1),('Tetranychus (spider mite, 0.5 mm)',3.00,1),
      ('Adineta (bdelloid rotifer, 0.3 mm)',3.04,1),('Dimorphilus (annelid, 1 mm)',3.78,1),('Priapulus (priapulid, cm)',6.20,1),('Limulus (horseshoe crab, 50 cm)',7.89,1)]
fig,ax=plt.subplots(figsize=(7.5,4.6),dpi=150)
for i,(n,v,na) in enumerate(rows):
    ax.barh(i,v,color='#2b6cb0' if na else 'white',edgecolor='#2b6cb0' if na else '#c05621',hatch=None if na else '///',height=0.62,lw=1.2)
    ax.text(max(v,1.8)+0.12,i,'%.2f'%v,va='center',fontsize=8,color='#24292f')
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows],fontsize=8.5); ax.set_xlim(0,9)
ax.axvline(1.8,color='#6e7781',ls='--',lw=0.8); ax.text(1.84,len(rows)-0.4,'cut 1.8',fontsize=7.5,color='#6e7781')
for s in ('top','right'): ax.spines[s].set_visible(False)
ax.set_xlabel('channels per metal pump',color='#6e7781')
from matplotlib.patches import Patch
ax.legend(handles=[Patch(facecolor='#2b6cb0',label='lysine (DEKA-type) Na channel present'),Patch(facecolor='white',edgecolor='#c05621',hatch='///',label='no voltage-gated Na channel')],fontsize=8,frameon=False,loc='lower right')
ax.set_title('Size does not predict sodium-channel loss; the battery ratio follows it',fontsize=10.5,loc='left')
plt.tight_layout(); plt.savefig('figures/L3649_size_sodium.png')
