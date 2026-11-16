"""Manuscript 2, Figure 10: NALCN selectivity ring (DI-DIV) per organism, read from rounds/L3653_tool_output.txt and rounds/L3661_tool_output.txt (worm).
K (lysine, sodium-like) cells filled; E/D cells open. Multiple distinct rings in one organism are shown as separate rows."""
import re, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
T=open('rounds/L3653_tool_output.txt').read().splitlines(); rings={}; org=None
for l in T:
    if l.startswith('ORG '): org=l[4:33].strip()
    elif l.startswith('    '): rings.setdefault(org,set()).add(l.split()[-1])
rings['C. elegans (worm, L3661)']={l.split()[-1] for l in open('rounds/L3661_tool_output.txt') if l.startswith('W ')}
order=[('sponge',['Amphimedon queenslandica']),('cnidarians',['Nematostella vectensis','Hydra vulgaris']),('acoel',['Hofstenia miamia']),
 ('spiralians',['Aplysia californica','Capitella teleta','Lingula anatina','Dimorphilus gyrociliatus','Helobdella robusta','Brachionus calyciflorus','Brachionus plicatilis','Adineta ricciae']),
 ('ambulacrarian',['Strongylocentrotus purpuratu']),('ecdysozoans',['fly','Tetranychus urticae','Hypsibius exemplaris','Ramazzottius varieornatus','C. elegans (worm, L3661)']),
 ('chordates',['Branchiostoma floridae','zebrafish','chicken','mouse'])]
rows=[]
for g,os_ in order:
    for o in os_:
        for r in sorted(rings.get(o,[])): rows.append((g,o,r))
fig,ax=plt.subplots(figsize=(6.6,0.30*len(rows)+1.4),dpi=150)
for i,(g,o,r) in enumerate(rows):
    y=len(rows)-1-i
    for j,c in enumerate(r):
        k=c=='K'; ax.add_patch(plt.Rectangle((j+0.08,y+0.1),0.84,0.8,facecolor='#2b6cb0' if k else 'white',edgecolor='#2b6cb0' if k else '#8c959f',lw=0.8))
        ax.text(j+0.5,y+0.5,c,ha='center',va='center',fontsize=8,color='white' if k else '#24292f',fontweight='bold' if k else 'normal')
    ax.text(-0.15,y+0.5,'%s  ·  %s'%(o.replace('Strongylocentrotus purpuratu','Strongylocentrotus purpuratus'),g),ha='right',va='center',fontsize=7.5,color='#24292f')
ax.set_xlim(-0.1,4); ax.set_ylim(0,len(rows)); ax.set_xticks([0.5,1.5,2.5,3.5]); ax.set_xticklabels(['DI','DII','DIII','DIV'],fontsize=8.5); ax.xaxis.tick_top()
ax.set_yticks([]); [ax.spines[s].set_visible(False) for s in ax.spines]
ax.set_title('NALCN ring: the sodium-like lysine (K) sits in domain II or domain III',fontsize=10,loc='right',pad=18)
plt.subplots_adjust(left=0.62,right=0.98,top=0.9,bottom=0.02); plt.savefig('figures/L3665_nalcn_rings.png')
print(len(rows),'rows')
