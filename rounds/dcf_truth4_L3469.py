"""Truth rule v4 (L3469): INDEPENDENT reference = UniProtKB/Swiss-Prot 'Protein families' text (curated sequence-similarity
classification), not names written by the DCF. classes(families_text) -> set of classes. Recall sets via recall_class()."""
import re
def classes(f):
    f = f or ''; out = set()
    if 'Calcium channel alpha-1 subunit' in f: out.add('Ca')
    if re.search(r'Sodium channel \(TC 1\.A\.1\.10\)', f): out.add('Na')
    if 'Two pore domain potassium channel' in f: out.add('K2P')
    elif 'HCN' in f: out.add('HCN')
    elif re.search(r'[Pp]otassium channel', f): out.add('K')
    if 'Glutamate-gated ion channel' in f: out.add('iGluR')
    if 'Biopterin-dependent aromatic amino acid hydroxylase' in f: out.add('FeHyd')
    if 'Cation transport ATPase (P-type)' in f:
        if 'Type IIC' in f: out.add('pump_NaK')
        elif 'Type IIA' in f or 'Type IIB' in f: out.add('pump_Ca')
        elif 'Type IB' in f: out.add('pump_Cu')
        else: out.add('pump_other')
    return out
def recall_class(f):
    """classes counted in recall: voltage-gated K only (Potassium channel family subfamilies, not Calcium-activated/KCNN/inward)"""
    c = classes(f)
    if 'K' in c and not re.search(r'Potassium channel family, [A-Z]+[a-z]* ?\(|Potassium channel family, (A|B|C|D|F|G|H|KQT|S|V)\b|KCNQ|KQT', f or ''): c.discard('K')
    if 'K' in c and 'Calcium-activated' in (f or ''): c.discard('K')
    return c
