"""Manuscript 2, Figure 2: pre-registered blind tests of nerve chemistry by metal (numbers from committed grade outputs)."""
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
rows=[('mouse','names',10,10),('zebrafish (curated)','names',10,11),('zebrafish (predicted)','names',7,10),('chicken','names+descr.',13,14),
      ('fruit fly','names+descr.',5,13),('nematode (Swiss-Prot)','UniProt',9,9),('all other animals\n(58,949 proteins)','UniProt',13,14),
      ('Na/Ca decision\n(24,796 TrEMBL channels)','UniProt names',4,4)]
fig,ax=plt.subplots(figsize=(8,4.6),dpi=150)
ink='#1f2328'; muted='#6e7781'; c_ind='#2b6cb0'; c_own='#9aa5b1'
for i,(n,t,p,g) in enumerate(rows):
    col=c_ind if 'UniProt' in t else c_own
    ax.barh(i,g,color='#e6e9ed',height=.6); ax.barh(i,p,color=col,height=.6)
    ax.text(g+0.3,i,'%d / %d'%(p,g),va='center',fontsize=9,color=ink)
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows],fontsize=8.5,color=ink); ax.invert_yaxis()
ax.set_xlabel('predictions passed / gradeable',fontsize=9,color=muted); ax.set_xlim(0,16)
for s in ('top','right'): ax.spines[s].set_visible(False)
ax.set_title('Pre-registered blind tests: 71 of 85 passed',fontsize=11,color=ink,loc='left')
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color=c_own,label='graded by our name rules'),Patch(color=c_ind,label='graded by UniProt (independent)')],fontsize=8,frameon=False,loc='lower right')
plt.tight_layout(); plt.savefig('figures/L3489_blind_tests.png')
