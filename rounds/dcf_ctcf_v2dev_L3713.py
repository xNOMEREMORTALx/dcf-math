"""CTCF finder v2 (L3713 development: zinc-finger gate >= 6 instead of >= 9; reciprocal panel unchanged). Reciprocal best hit: (1) among proteins with >= 9 C2H2 motifs (C.{2,4}C.{12}H.{3,5}H), the top scorer against mouse Ctcf
(local aligner); (2) that protein's nearest among all 365 mouse proteins with >= 9 C2H2 motifs. CTCF call = (2) is Ctcf or Ctcfl.
ctcf(seqs) -> (call, top_score, nearest, nearest_score, n_zf_proteins, top_id)."""
import pickle,re,runpy
ZF=re.compile(r'C.{2,4}C.{12}H.{3,5}H')
_sc=runpy.run_path('/home/claude/dcf-math/rounds/dcf_localalign_L3585.py')['score']
_P,_D=pickle.load(open('/home/claude/L3469/P6.pkl','rb'))
PANEL={k:s for k,s in _P['mouse'].items() if len(ZF.findall(s))>=9}
CT=_P['mouse']['Ctcf']
def ctcf(items):
    zf=[(a,s) for a,s in items if len(ZF.findall(s))>=6]
    if not zf: return (False,0,None,0,0,None)
    v,a,s=max((_sc(s,CT),a,s) for a,s in zf)
    w,r=max((_sc(s,PANEL[k]),k) for k in PANEL)
    return (r in ('Ctcf','Ctcfl'),v,r,w,len(zf),a)
