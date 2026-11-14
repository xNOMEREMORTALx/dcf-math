"""Manuscript 2, Figure 4: the domain-III pore loop of 4-domain sodium-type channels across the animal tree (sequences extracted L3505)."""
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
rows=[('choanoflagellate (Monosiga)','no animal body','VALLQVATFEGWMEIMEA'),('placozoan (Trichoplax)','no neurons','LALFEVATFEGWIQVMGD'),
      ('sea anemone (Nematostella)','nerve net','LALLQVATFEGWMEIMED'),('comb jelly (Mnemiopsis)','own nerve net','IALYQVATFEGWMEVMDD'),('fruit fly (para)','bilaterian','LCLFQVATFKGWIQIMND'),
      ('zebrafish (scn8aa)','bilaterian','LALLQVATFKGWMDIMYA'),('chicken (SCN2A)','bilaterian','LSLLQVATFKGWMDIMYA'),
      ('human (SCN2A)','bilaterian','LSLLQVATFKGWMDIMYA'),('human sensor Nax (SCN7A)','sodium sensor','LSLLQVATFNGWITIMNS')]
col={'E':'#c05621','K':'#2b6cb0','N':'#6b46c1'}
fig,ax=plt.subplots(figsize=(10,4.2),dpi=150); ax.axis('off'); ax.set_xlim(0,30); ax.set_ylim(-0.8,len(rows)+0.6)
for i,(n,t,s) in enumerate(rows):
    y=len(rows)-1-i
    ax.text(0,y,n,fontsize=9,va='center',color='#1f2328'); ax.text(8.6,y,t,fontsize=7.5,va='center',color='#6e7781')
    for j,ch in enumerate(s):
        x=12+j*0.95; c=col.get(ch,'#1f2328') if j==9 else ('#1f2328' if 6<=j<=11 else '#9aa5b1')
        if j==9: ax.add_patch(plt.Rectangle((x-0.42,y-0.38),0.84,0.76,color=c,alpha=0.15))
        ax.text(x,y,ch,family='monospace',fontsize=11,ha='center',va='center',color=c,weight='bold' if j==9 else 'normal')
ax.text(12+9*0.95,len(rows)-0.2,'↓ domain-III ring position',fontsize=8,ha='center',color='#1f2328')
ax.plot([0,30],[4.5,4.5],color='#d0d7de',lw=0.8)
ax.text(0,-0.7,'E = glutamate (DEEA-type ring, early lineages)    K = lysine (DEKA ring: fast nerve sodium channel)    N = asparagine (DENA: sodium sensor)',fontsize=7.8,color='#1f2328')
ax.set_title('One letter in one pore loop: E in early animals, K in every bilaterian nerve sodium channel',fontsize=10.5,loc='left',color='#1f2328')
plt.tight_layout(); plt.savefig('figures/L3509_EtoK.png',bbox_inches='tight')
