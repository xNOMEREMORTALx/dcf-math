"""Manuscript 2, Figure 5: neighbour-joining tree (topology only, unrooted, drawn from an arbitrary root) of NAV1/NAV2 channels (L3569)."""
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
nwk="(((A0A7M7N9I2,(R7TCA7,(A0ACM8CKW0,(HMIM006045,HMIM019623)))),(A9USM1,((F6QCF9,(I6NQF8,human_SCN2A)),(fly_para,(A0A1S3HN89,R7TMI4))))),((B3RSS4,((A0ACF8Y6N4,F6MZB8),(A0ACF8YBX3,(A0ACF8Y996,F6MZB9)))),(A0A9J7HQP1,A7SKR1)))"
lab={'A0A7M7N9I2':('sea urchin','E'),'R7TCA7':('annelid NAV2','E'),'A0ACM8CKW0':('acorn worm','E'),'HMIM006045':('acoel 1','E'),'HMIM019623':('acoel 2','E'),
 'A9USM1':('choanoflagellate','E'),'F6QCF9':('sea squirt NAV1','K'),'I6NQF8':('lancelet NAV1','K'),'human_SCN2A':('human SCN2A','K'),'fly_para':('fly para','K'),
 'A0A1S3HN89':('brachiopod NAV1','K'),'R7TMI4':('annelid NAV1','K'),'B3RSS4':('placozoan','E'),'A0ACF8Y6N4':('comb jelly 1','E'),'F6MZB8':('comb jelly 2','E'),
 'A0ACF8YBX3':('comb jelly 3','E'),'A0ACF8Y996':('comb jelly 4','E'),'F6MZB9':('comb jelly 5','E'),'A0A9J7HQP1':('lancelet NAV2','E'),'A7SKR1':('sea anemone','E')}
def parse(s):
    s=s.strip()
    if s[0]!='(': return s
    d=0
    for i,c in enumerate(s[1:-1],1):
        d+= c=='('; d-= c==')'
        if c==',' and d==0: return (parse(s[1:i]),parse(s[i+1:-1]))
T=parse(nwk); leaves=[]; ys={}
def depth(t): return 0 if isinstance(t,str) else 1+max(depth(t[0]),depth(t[1]))
D=depth(T)
fig,ax=plt.subplots(figsize=(8,7),dpi=150)
def draw(t,x):
    if isinstance(t,str):
        y=len(leaves); leaves.append(t); n,l=lab[t]; c='#2b6cb0' if l=='K' else '#c05621'
        ax.plot([x,D],[y,y],color='#d0d7de',lw=0.6,ls=':'); ax.text(D+0.15,y,'%s  [%s]'%(n,l),va='center',fontsize=8.5,color=c,weight='bold' if l=='K' else 'normal'); return y
    y1=draw(t[0],x+1); y2=draw(t[1],x+1)
    ax.plot([x,x],[y1,y2],color='#1f2328',lw=1); ax.plot([x,x+1],[y1,y1],color='#1f2328',lw=1); ax.plot([x,x+1],[y2,y2],color='#1f2328',lw=1)
    return (y1+y2)/2
draw(T,0); ax.set_xlim(-0.3,D+5); ax.invert_yaxis(); ax.axis('off')
ax.set_title('Sodium-type channels by real alignment: the K-type NAV1 genes group together\n(neighbour-joining on 1 - identity; topology only; unrooted, drawn from an arbitrary root)',fontsize=9.5,loc='left')
ax.text(0,len(leaves)+0.6,'[K] = A-T-F-K-G-W (DEKA, fast nerve channel)    [E] = A-T-F-E-G-W (E-type, ancestral)',fontsize=8,color='#1f2328')
plt.tight_layout(); plt.savefig('figures/L3573_navtree.png',bbox_inches='tight')
