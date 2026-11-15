"""Manuscript 2, Figure 7: channels per metal pump (dcf_nerve v2 calls) in 17 organisms (rounds/L3609_battery_seen.txt)."""
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
rows=[('Geodia (sponge)',0.05,0),('Ephydatia (sponge)',0.33,0),('Oopsacas (glass sponge)',0.67,0),('Amphimedon (sponge)',0.83,0),('Monosiga (choanoflagellate)',1.00,0),('Trichoplax (placozoan)',1.60,0),
      ('Ciona (sea squirt)',2.00,1),('Lingula (brachiopod)',3.35,1),('Drosophila (fly)',3.50,1),('Strongylocentrotus (sea urchin)',4.22,1),('Capitella (annelid)',4.57,1),('Hofstenia (acoel)',4.86,1),
      ('Gallus (chicken)',6.27,1),('Saccoglossus (acorn worm)',6.67,1),('Nematostella (sea anemone)',11.33,1),('Mnemiopsis (comb jelly)',13.27,1),('Branchiostoma (lancelet)',14.25,1)]
fig,ax=plt.subplots(figsize=(7.5,5.2),dpi=150)
for i,(n,v,neu) in enumerate(rows):
    ax.barh(i,v,color='#2b6cb0' if neu else '#c05621',height=0.65); ax.text(v*1.08,i,'%.2f'%v,va='center',fontsize=8)
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows],fontsize=8.5); ax.set_xscale('log'); ax.set_xlim(0.03,40)
ax.axvline(1.8,color='#6e7781',ls='--',lw=0.8)
for s in ('top','right'): ax.spines[s].set_visible(False)
ax.set_xlabel('channels per metal pump (log scale)',color='#6e7781')
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color='#c05621',label='no nervous system'),Patch(color='#2b6cb0',label='nervous system')],fontsize=8,frameon=False,loc='lower right')
ax.set_title('The nerve battery: chargers vs dischargers across 17 organisms',fontsize=10.5,loc='left')
plt.tight_layout(); plt.savefig('figures/L3609_battery_ratio.png')
