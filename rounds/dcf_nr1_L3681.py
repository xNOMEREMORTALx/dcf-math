"""dcf_nr1 (L3681): shared NR1 caller. A protein is NR1 if (1) dcf_nerve v3 tags it iGluR, (2) its nearest of the 18 mouse iGluRs by local aligner
(dcf_localalign_L3585) is Grin1, and (3) that score is >= FLOOR = 1000 (standing rule, L3649). nr1(seq) -> (bool, nearest, score)."""
import pickle,re,runpy
FLOOR=1000
_N=runpy.run_path('/home/claude/dcf-math/rounds/dcf_nerve_v3_L3633.py',run_name='x')
_sc=runpy.run_path('/home/claude/dcf-math/rounds/dcf_localalign_L3585.py')['score']
_P,_D=pickle.load(open('/home/claude/L3469/P6.pkl','rb'))
REF={g:p for g,p in _P['mouse'].items() if re.match(r'(?i)^(gria\d|grik\d|grid\d|grin\d\w?)$',g)}
def nr1(s):
    if 'iGluR' not in _N['tags'](s): return (False,None,0)
    v,r=max((_sc(s,REF[g]),g) for g in REF)
    return (r=='Grin1' and v>=FLOOR, r, v)
