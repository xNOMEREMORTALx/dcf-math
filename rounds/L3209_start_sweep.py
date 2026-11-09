import json, re, itertools, sys
sys.path.insert(0,'/home/claude/tools')
G={'NC_002927':'L3181','NC_004129':'L3181','NC_008313':'L3181','NC_012108':'L3181','NC_014328':'L3181','NC_016894':'L3181','NC_013799':'L3185','NC_006814':'L3185'}
def ann(gb):
    txt=open(gb).read(); A={}
    for m in re.finditer(r'\n     CDS             (complement\()?<?(\d+)\.\.>?(\d+)\)?\n',txt):
        a,b=int(m.group(2)),int(m.group(3))
        if m.group(1): A[(a,-1)]=b      # key: genome stop coord, value: start coord
        else: A[(b,1)]=a
    return A
data={}
for a,d in G.items():
    data[a]=(json.load(open('/home/claude/gstart/%s.json'%a)),ann('/home/claude/%s/g/%s.gb'%(d,a)))
def score(wM,wL,pg,pt,sel=None):
    tot=ok=0; per={}
    for a,(rows,A) in data.items():
        if sel and a not in sel: continue
        t=o=0
        for b,s,C,L in rows:
            if not C: continue
            pen={'GTG':pg,'TTG':pt}
            i=max(C,key=lambda c:wM*c[1]+c[2]+pen.get(c[5],0)+c[3]+wL*c[4])[0]
            if s==1: key=(b,1); st=i+1
            else: key=(L-b+1,-1); st=L-i
            if key in A: t+=1; o+=(A[key]==st)
        per[a]=100*o/max(t,1); tot+=t; ok+=o
    return 100*ok/tot, per
base,per=score(1,1,0,0); print("baseline pooled %.2f"%base, {k:round(v,1) for k,v in per.items()})
best=[]
for wM,wL,pg,pt in itertools.product([0.5,1,1.5],[0.5,0.75,1,1.25],[0,-0.5,-1,-2],[0,-0.5,-1,-2,-3]):
    best.append((score(wM,wL,pg,pt)[0],wM,wL,pg,pt))
best.sort(reverse=True); print("top:",[tuple(round(x,2) for x in b) for b in best[:8]])
grid=list(itertools.product([0.5,1],[0.5,0.75,1],[-1,-2,-3,-4],[-2,-3,-4,-5,-6]))
R=sorted(((score(*g)[0],)+g for g in grid),reverse=True); print("extended top:",[tuple(round(x,2) for x in b) for b in R[:5]])
# leave-one-genome-out
gains=[]
for h in data:
    tr=[a for a in data if a!=h]
    bp=max(grid,key=lambda g:score(*g,sel=tr)[0])
    held=score(*bp,sel=[h])[1][h]; b0=score(1,1,0,0,sel=[h])[1][h]
    gains.append(held-b0); print("held-out",h,"params",bp,"%.1f -> %.1f"%(b0,held))
print("LOO mean gain %.2f, min %.2f, max %.2f"%(sum(gains)/len(gains),min(gains),max(gains)))
