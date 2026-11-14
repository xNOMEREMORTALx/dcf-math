import pickle,re,runpy,collections
P,D=pickle.load(open('P5.pkl','rb'))
T=runpy.run_path('/home/claude/dcf-math/rounds/dcf_truth3_L3461.py')['classes']
H='[AVILMFWYGSTC]'; S4=r'(?=[RK]'+H+'{2}[RK]'+H+'{2}[RK]'+H+'{2}[RK]'+H+'{2}[RK])'
RING=r'(?=[TS].[ED].W)'; LYS=r'[TS][FY][KR][GA]W'
def weak(p):
    return re.search(r'(?=[RK]..[RK]..[RK]..[RK])',p) or any(sum(x in 'RK' for x in m.groups())==4 for m in re.finditer(r'(?=([RKQ])..([RKQ])..([RKQ])..([RKQ])..([RKQ]))',p))

def chan5(p):
    s4=bool(re.search(S4,p)); r=len(re.findall(RING,p)); lys=bool(re.search(LYS,p))
    kv7=len(p)<1500 and re.search(r'(?=R..Q..R..[RH])',p) and re.search(r'[TS][VI]GYGD',p)
    if not (s4 or kv7) and re.search(r'[TS][VI]GYGD|SVGFGN|CIGYG',p): kv7=weak(p)
    if not (s4 or kv7): return None
    if len(p)>=1500 and s4 and (r>=3 or lys):
        if lys and r<=2: return 'Na'
        return 'Ca' if r>=3 else 'undecided'
    if 'CIGYG' in p: return 'HCN'
    if re.search(r'[TSC][VITL]G[YF]G',p): return 'K'
    return 'other'
K2P5=r'[TS][TSV][IVT]G[YFL]G'
def k2p5(p): return len(p)<1100 and not re.search(S4,p) and len(re.findall(K2P5,p))>=2
FE5=r'[CVI]HE[LI][LM]GH'
res=collections.defaultdict(lambda:[0,0,[] ,0,0,[]])
for sp in P:
    for g,p in P[sp].items():
        tr=T(g,D.get((sp,g),''))
        calls=[]; c=chan5(p)
        if c in('Ca','Na','K','HCN'): calls.append(c)
        if k2p5(p): calls.append('K2P')
        if re.search(FE5,p): calls.append('FeHyd')
        for c in calls:
            r=res[(sp,c)]; r[1]+=1
            if c in tr: r[0]+=1
            else: r[2].append(g)
        for c in ('Ca','Na','K','HCN','K2P','FeHyd'):
            if c in tr and re.match('(?i)('+runpy.run_path.__self__ if False else '(?i).*', g) and c in tr:
                pass
    # recall by symbol
    S=runpy.run_path('/home/claude/dcf-math/rounds/dcf_truth3_L3461.py')['SYM']
    for c in ('Ca','Na','K','HCN','K2P','FeHyd'):
        fam=[g for g in P[sp] if re.match('(?i)('+S[c]+')',g) and c in T(g,D.get((sp,g),''))]
        got=[g for g in fam if (chan5(P[sp][g])==c if c in('Ca','Na','K','HCN') else (k2p5(P[sp][g]) if c=='K2P' else bool(re.search(FE5,P[sp][g]))))]
        r=res[(sp,c)]; r[3]=len(got); r[4]=len(fam); r[5]=[g for g in fam if g not in got]
for (sp,c),r in sorted(res.items()):
    print('%-9s %-5s precision %3d/%-3d recall %3d/%-3d  wrong %s  missed %s'%(sp,c,r[0],r[1],r[3],r[4],r[2][:6],r[5][:8]))
