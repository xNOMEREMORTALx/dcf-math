"""Truth rule v2 (L3449): a gene belongs to a class if its SYMBOL or its RefSeq DESCRIPTION says so (case-insensitive).
Used to grade dcf_neurochem2_L3449 output. Description patterns accept '-like'. Unnamed genes (LOC/si:) are judged by description."""
import re
SYM = {'Ca': r'cacna1', 'Na': r'scn\d+l?a[ab]?$', 'K': r'kcn[a-z]+\d', 'HCN': r'hcn\d', 'K2P': r'kcnk\d',
       'iGluR': r'gri[akdn]\d', 'NMDA': r'grin[12]', 'FeHyd': r'(th|th2|tph1\w*|tph2\w*|pah\w*)$',
       'pump_NaK': r'atp(1a|4a|12a)', 'pump_Ca': r'atp2[abc]', 'pump_Cu': r'atp7[ab]'}
DESC = {'Ca': r'calcium (voltage-gated )?channel.{0,40}alpha ?1|voltage-dependent [lnpqrt/-]*-?type calcium channel subunit alpha',
        'Na': r'sodium (voltage-gated )?channel.{0,25}alpha|sodium channel protein type',
        'K': r'potassium.{0,60}channel|shaker|ether-a-go-go',
        'HCN': r'hyperpolarization[- ]activated cyclic nucleotide',
        'K2P': r'two pore domain|potassium channel subfamily k',
        'iGluR': r'glutamate (ionotropic )?receptor|glutamate receptor ionotropic|glutamate receptor, ionotropic',
        'NMDA': r'nmda type subunit [12]|n-methyl-d-aspartate receptor subunit|nmda receptor subunit (nr)?[12]|glutamate receptor ionotropic, nmda [12]',
        'FeHyd': r'tyrosine (3-mono)?hydroxylase|tryptophan (5-)?hydroxylase|phenylalanine (4-)?hydroxylase',
        'pump_NaK': r'na\+/k\+ transporting.{0,20}alpha|sodium/potassium-transporting atpase subunit alpha|h\+/k\+ transporting.{0,20}alpha|potassium-transporting atpase alpha',
        'pump_Ca': r'calcium[- ]transporting atpase|ca\+\+ transporting|ca2\+ transporting',
        'pump_Cu': r'copper[- ]transporting atpase|atpase copper transporting'}
CHAN = ('Ca', 'Na', 'HCN', 'K')
def classes(sym, desc):
    out = set()
    for c in SYM:
        if re.match('(?i)' + SYM[c], sym) or re.search('(?i)' + DESC[c], desc): out.add(c)
    if 'HCN' in out: out.discard('K')
    if 'K2P' in out: out.discard('K')
    return out
