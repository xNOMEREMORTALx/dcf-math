"""Manuscript 2, Figure 3: battery balance in complete gene sets (v6 calls, rounds/L3477_battery.txt)."""
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
sp=['zebrafish','chicken','fruit fly']; K=[55,34,9]; oth=[98-55,69-34,21-9]; pumps=[23,11,6]
fig,ax=plt.subplots(figsize=(6.5,3.6),dpi=150)
x=range(len(sp)); w=.36
ax.bar([i-w/2 for i in x],K,w,color='#2b6cb0',label='K$^+$ channels'); ax.bar([i-w/2 for i in x],oth,w,bottom=K,color='#90b4dd',label='other channels (Na, Ca, HCN, K2P)')
ax.bar([i+w/2 for i in x],pumps,w,color='#c05621',label='metal pumps (Na/K, Ca, Cu)')
for i in x: ax.text(i,max(K[i]+oth[i],pumps[i])+3,'%.1f channels per pump'%((K[i]+oth[i])/pumps[i]),ha='center',fontsize=8.5,color='#1f2328')
ax.set_xticks(list(x)); ax.set_xticklabels(sp); ax.set_ylabel('genes called',color='#6e7781'); ax.set_ylim(0,120)
for s in ('top','right'): ax.spines[s].set_visible(False)
ax.legend(fontsize=7.5,frameon=False,loc='upper right'); ax.set_title('The nerve battery: few chargers, many dischargers',fontsize=10.5,loc='left')
plt.tight_layout(); plt.savefig('figures/L3493_battery.png')
