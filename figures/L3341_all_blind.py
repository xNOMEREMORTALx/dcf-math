"""L3341: Figure 3 (all 37 blind genomes on the four-tier scale) + number audit from committed tool-number files only."""
import statistics as st, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from scipy.stats import spearmanr
R='/home/claude/dcf-math/rounds/'
def load(f,col,skip):
    d={}
    for l in open(R+f).read().splitlines()[skip:]:
        x=l.split()
        if x and x[0].startswith('NC_'): d[x[0]]=float(x[col])
    return d
b20=load('L3269_tool_numbers.txt',4,2); b20.update(load('L3273_tool_numbers_gasseri.txt',4,0))
b21=load('L3285_tool_numbers.txt',4,2); b22=load('L3293_tool_numbers.txt',3,1); b23=load('L3333_tool_numbers.txt',3,1)
T={ # tiers as frozen in the pre-registrations (L3265, L3281, L3289, L3321)
 'blind_20':{'NC_013198':1,'NC_004116':1,'NC_007929':1,'NC_008530':1,'NC_012560':2,'NC_008686':2,'NC_014532':2,'NC_007651':2,'NC_009495':3,'NC_009012':3,'NC_009718':3,'NC_011898':3,'NC_009515':4,'NC_011296':4,'NC_012438':4,'NC_008554':4},
 'blind_21':{'NC_005362':1,'NC_009785':1,'NC_003551':4,'NC_013223':4},
 'blind_22':{'NC_007604':2,'NC_003272':2,'NC_004113':2,'NC_005125':2,'NC_010337':4},
 'blind_23':{'NC_010080':1,'NC_013853':1,'NC_015759':1,'NC_003295':2,'NC_007761':2,'NC_009848':2,'NC_008593':3,'NC_009616':3,'NC_014393':3,'NC_013665':4,'NC_015388':4,'NC_014378':4}}
V={'blind_20':b20,'blind_21':b21,'blind_22':b22,'blind_23':b23}
call=lambda x: 1 if x<.0045 else 2 if x<.023 else 3 if x<.060 else 4
tot=ok=0; allt=[]; allv=[]; miss=[]
for s in T:
    k=sum(call(V[s][a])==t for a,t in T[s].items()); n=len(T[s]); tot+=n; ok+=k
    print("AUDIT %s: %d of %d correct"%(s,k,n)); 
    for a,t in T[s].items():
        allt.append(t); allv.append(V[s][a])
        if call(V[s][a])!=t: miss.append((s,a,V[s][a],t))
print("AUDIT total %d of %d; misses %s"%(ok,tot,miss))
print("AUDIT rho blind_20 %.3f, blind_23 %.3f, all 37 %.3f"%(spearmanr([T['blind_20'][a] for a in T['blind_20']],[b20[a] for a in T['blind_20']])[0],spearmanr([T['blind_23'][a] for a in T['blind_23']],[b23[a] for a in T['blind_23']])[0],spearmanr(allt,allv)[0]))
big=load('L3333_tool_numbers.txt',4,1); sm=load('L3333_tool_numbers.txt',5,1)
m=lambda d,k: st.median(d[a] for a,t in T['blind_23'].items() if t==k)
print("AUDIT blind_23 O2->H2: large %.2fx, small %.2fx"%(m(big,3)/m(big,2),m(sm,3)/m(sm,2)))
# figure
cols={'blind_20':'#2a78d6','blind_21':'#eb6834','blind_22':'#1baf7a','blind_23':'#eda100'}
mk={'blind_20':'o','blind_21':'s','blind_22':'D','blind_23':'^'}
INK,MUTED,GRID,BG='#0b0b0b','#52514e','#e6e5e0','#fcfcfb'
fig,ax=plt.subplots(figsize=(8.5,4.6),dpi=200); fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
import random; random.seed(3)
for s in T:
    for a,t in T[s].items():
        ax.scatter(V[s][a],t+random.uniform(-0.22,0.22),s=48,marker=mk[s],color=cols[s],edgecolor=BG,linewidth=1.2,zorder=3)
for s in T: ax.scatter([],[],marker=mk[s],color=cols[s],s=48,label='%s (%d)'%(s,len(T[s])))
for x in (0.0045,0.023,0.060): ax.axvline(x,color=MUTED,lw=0.8,ls=(0,(3,3)),zorder=1)
for x,lab in ((0.0045,'0.0045'),(0.023,'0.023'),(0.060,'0.060')): ax.text(x+0.002,4.6,lab,ha='left',va='bottom',fontsize=7.5,color=MUTED)
for s,a,v,t in miss:
    name={'NC_009495':'C. botulinum','NC_012438':'Sulfurihydrogenibium'}.get(a,a)
    ax.annotate(name+' (miss)',(v,t),xytext=(v+0.03,t+0.38),fontsize=8,color=MUTED,arrowprops=dict(arrowstyle='-',color=MUTED,lw=0.7))
ax.set_yticks([1,2,3,4]); ax.set_yticklabels(['1 lactic','2 O2 respirers\n+ oxygenic phototrophs','3 H2-making\nfermenters','4 ferredoxin-based'],fontsize=8.5,color=INK)
ax.set_ylim(0.5,4.9); ax.set_xlim(-0.005,0.235); ax.set_xlabel('3-3-4 ferredoxin ladder per 1,000 amino acids (whole predicted proteome)',fontsize=9,color=INK)
ax.grid(axis='x',color=GRID,lw=0.6,zorder=0); [ax.spines[x].set_visible(False) for x in ('top','right')]; [ax.spines[x].set_color(MUTED) for x in ('left','bottom')]; ax.tick_params(colors=MUTED,labelsize=8)
ax.set_title('35 of 37 blind genomes fall in their pre-assigned tier (cuts frozen before download)',loc='left',fontsize=10,color=INK)
ax.legend(frameon=False,fontsize=8,loc='lower right',labelcolor=INK)
fig.tight_layout(); fig.savefig('/home/claude/dcf-math/figures/L3341_all_blind.png',facecolor=BG)
