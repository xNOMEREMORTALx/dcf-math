"""L3581 descriptive: name each comb-jelly K/HCN/K2P call by its nearest mouse or fly channel (dcf_align identity)."""
import gzip,re,pickle,runpy,collections
A=runpy.run_path('/home/claude/dcf-math/rounds/dcf_align_L3569.py'); _al=A['align']
import numpy as np
SRC=open('/home/claude/dcf-math/rounds/dcf_align_L3569.py').read().replace('return same / max(cols, 1), int(H[n, m])','return same, cols')
G={}; exec(SRC,G)
def idt(a,b):
    # identical positions / length of the shorter sequence (L3581: guards against short references inflating identity)
    same,cols=G['align'](a,b); return same/min(len(a),len(b))

P,D=pickle.load(open('/home/claude/L3469/P6.pkl','rb'))
ref={('mouse',g):p for g,p in P['mouse'].items() if re.match(r'(?i)(kcn[a-z]+\d|hcn\d)',g) and not re.match(r'(?i)kcne|kcnip|kcnmb|kcnab|kcnrg|kcnj',g) and len(p)>=300}
ref.update({('fly',g):p for g,p in P['fly'].items() if re.match(r'^(Sh|Shab|Shaw|Shal|Shawl|eag|sei|elk|KCNQ|Ih|Ork1|Task6|Task7|sand|galene)$',g)})
S={}
for l in gzip.open('/home/claude/L3509/z/cteno.tsv.gz','rt').read().splitlines()[1:]:
    f=l.split('\t'); S[f[0]]=f[3]
calls=[l.split()[:2] for l in open('/home/claude/dcf-math/rounds/L3509_tool.txt') if l.split() and l.split()[0] in ('K','K2P','HCN')]
seen=set(); fams=collections.Counter(); rows=[]
for c,a in calls:
    if S[a] in seen: continue
    seen.add(S[a])
    sc=max((idt(S[a],q),k) for k,q in ref.items())
    sp,g=sc[1]
    f=('KCNK/K2P' if re.match(r'(?i)kcnk|ork1|task|sand|galene',g) else 'HCN' if re.match(r'(?i)hcn|^Ih$',g) else
       {'a':'Kv1 Shaker','b':'Kv2 Shab','c':'Kv3 Shaw','d':'Kv4 Shal','h':'KCNH eag/erg/elk','q':'Kv7 KCNQ','g':'Kv6 silent','s':'Kv9 silent','v':'Kv8 silent','f':'Kv5 silent','n':'KCNN SK','j':'Kir','m':'BK/slo','t':'Slack/Slick','u':'Slo3'}.get(g[3].lower(),'other') if g.lower().startswith('kcn') else
       {'Sh':'Kv1 Shaker','Shab':'Kv2 Shab','Shaw':'Kv3 Shaw','Shawl':'Kv3 Shaw','Shal':'Kv4 Shal','eag':'KCNH eag/erg/elk','sei':'KCNH eag/erg/elk','elk':'KCNH eag/erg/elk','KCNQ':'Kv7 KCNQ'}.get(g,'other'))
    fams[(c,f)]+=1; rows.append((a,c,sp,g,round(sc[0],3),f))
print('L3581 comb-jelly channel calls named by nearest mouse/fly channel (%d distinct sequences)'%len(rows))
for (c,f),n in sorted(fams.items(),key=lambda x:-x[1]): print('  %-4s %-20s %d'%(c,f,n))
ids=[r[4] for r in rows]; print('identity to nearest: median %.3f, min %.3f, max %.3f'%(sorted(ids)[len(ids)//2],min(ids),max(ids)))
for r in rows: print('   ',r)
