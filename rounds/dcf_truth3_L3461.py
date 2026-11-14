"""Truth rule v3 (L3461): class membership by SYMBOL (vertebrate patterns + a fixed Drosophila symbol list) OR by DESCRIPTION,
where descriptions are matched with word sets in any order. Case-insensitive. Unnamed/undescribed genes have no class."""
import re
SYM = {'Ca': r'cacna1|cac$|ca-alpha1d$|ca-alpha1t$',
       'Na': r'scn\d+l?a[ab]?$|para$',
       'K': r'kcn[abcdfghqsv]\d|sh$|shab$|shaw$|shal$|eag$|sei$|elk$|kcnq$',
       'HCN': r'hcn\d|ih$',
       'K2P': r'kcnk\d|ork1$|task6$|task7$|galene$|sand$',
       'iGluR': r'gri[akdn]\d+[a-z]?$|glur[i]+[a-e]$|grik$|clumsy$|kair1d$|nmdar[12]$',
       'NMDA': r'grin[12]|nmdar[12]$',
       'FeHyd': r'(th|th2|tph1\w*|tph2\w*|pah\w*)$|ple$|hn$|trh$',
       'pump_NaK': r'atp(1a|4a|12a)|atpalpha$', 'pump_Ca': r'atp2[abc]|serca$|pmca$|spock$', 'pump_Cu': r'atp7[ab]?$'}
DESCW = {'Ca': [('calcium', 'channel', 'alpha')],
         'Na': [('sodium', 'channel', 'voltage'), ('sodium', 'channel', 'alpha'), ('sodium channel protein type',)],
         'K': [('potassium', 'channel'), ('shaker',), ('ether-a-go-go',)],
         'HCN': [('hyperpolarization', 'cyclic nucleotide')],
         'K2P': [('two pore',), ('potassium channel subfamily k',)],
         'iGluR': [('glutamate', 'receptor', 'ionotropic'), ('glutamate receptor', 'kainate'), ('glutamate receptor', 'ampa'), ('glutamate receptor', 'nmda'), ('glutamate receptor', 'delta')],
         'NMDA': [('nmda', 'subunit 1'), ('nmda', 'subunit 2'), ('n-methyl-d-aspartate', 'receptor')],
         'FeHyd': [('tyrosine', 'hydroxylase'), ('tryptophan', 'hydroxylase'), ('phenylalanine', 'hydroxylase')],
         'pump_NaK': [('sodium/potassium', 'atpase', 'alpha'), ('na+/k+', 'atpase', 'alpha'), ('h+/k+', 'atpase', 'alpha'), ('potassium-transporting', 'atpase', 'alpha')],
         'pump_Ca': [('calcium', 'transporting', 'atpase'), ('ca2+', 'atpase'), ('ca++', 'atpase')],
         'pump_Cu': [('copper', 'transporting', 'atpase'), ('atpase', 'copper')]}
EXCLUDE = r'(?i)^(nacp60e|dsc1)$'   # fly DSC1/NaCP60E: Na/Ca-mixed (DEEA ring), assigned to no class
def classes(sym, desc):
    if re.match(EXCLUDE, sym): return set()
    d = desc.lower(); out = set()
    for c in SYM:
        if re.match('(?i)(' + SYM[c] + ')', sym) or any(all(w in d for w in ws) for ws in DESCW[c]): out.add(c)
    if 'K2P' in out or 'HCN' in out: out.discard('K')
    if 'NMDA' in out: out.add('iGluR')
    return out
