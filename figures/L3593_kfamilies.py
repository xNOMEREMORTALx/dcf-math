"""Manuscript 2, Figure 6: voltage-gated K channel subfamilies (nearest mouse channel, local aligner; mouse by gene symbol, files 1-3)."""
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt, numpy as np
fams=['Kv1\nShaker','Kv2\nShab','Kv3\nShaw','Kv4\nShal','KCNH\neag/erg','Kv7\nKCNQ','silent\nKv5/6/8/9']
data={'comb jelly (122)':[104,1,3,9,2,0,3],'sea anemone (46)':[17,2,8,9,8,1,1],'placozoan, no neurons (5)':[1,1,1,0,2,0,0],'mouse, files 1-3 (39)':[8,2,4,3,8,5,9]}
cols=['#c05621','#2b6cb0','#6b46c1','#2f855a']
fig,ax=plt.subplots(figsize=(9,4.2),dpi=150); x=np.arange(len(fams)); w=0.2
for i,(k,v) in enumerate(data.items()):
    v=np.array(v,float); ax.bar(x+(i-1.5)*w,100*v/v.sum(),w,label=k,color=cols[i])
ax.set_xticks(x); ax.set_xticklabels(fams,fontsize=8); ax.set_ylabel('% of voltage-gated K channels',color='#6e7781')
for s in ('top','right'): ax.spines[s].set_visible(False)
ax.legend(fontsize=8,frameon=False); ax.set_title('Potassium-channel families: the comb jelly piles into Shaker; other lineages spread out',fontsize=10.5,loc='left')
plt.tight_layout(); plt.savefig('figures/L3593_kfamilies.png')
