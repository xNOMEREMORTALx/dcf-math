"""dcf_nr1 (L3693): shared NR1 caller, floor calibrated in L3693 (was 1000 in L3681). A protein is NR1 if (1) dcf_nerve v3 tags it iGluR, (2) its nearest of the 18 mouse iGluRs by local aligner
(dcf_localalign_L3585) is Grin1, and (3) that score is >= FLOOR = 941 (calibrated, rounds/L3693_calibration_output.txt). nr1(seq) -> (bool, nearest, score)."""
import pickle,re,runpy
FLOOR=941
_N=runpy.run_path('/home/claude/dcf-math/rounds/dcf_nerve_v3_L3633.py',run_name='x')
_sc=runpy.run_path('/home/claude/dcf-math/rounds/dcf_localalign_L3585.py')['score']
_P,_D=pickle.load(open('/home/claude/L3469/P6.pkl','rb'))
REF={g:p for g,p in _P['mouse'].items() if re.match(r'(?i)^(gria\d|grik\d|grid\d|grin\d\w?)$',g)}
def nr1(s):
    if 'iGluR' not in _N['tags'](s): return (False,None,0)
    v,r=max((_sc(s,REF[g]),g) for g in REF)
    return (r=='Grin1' and v>=FLOOR, r, v)
