"""Re-render every manuscript figure at publication resolution (600 dpi PNG + vector PDF) from its unchanged source script."""
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt, os, runpy
from matplotlib.figure import Figure
_orig = Figure.savefig
def _save(self, fname, *a, **k):
    base = os.path.join('/home/claude/dcf-math/figures/publication', os.path.splitext(os.path.basename(str(fname)))[0])
    k2 = {x: y for x, y in k.items() if x != 'dpi'}
    _orig(self, base + '.png', *a, dpi=600, **k2); _orig(self, base + '.pdf', *a, **k2)
Figure.savefig = _save
os.chdir('/home/claude/dcf-math')
for s in ['L3277_iron_zinc_tiers', 'L3329_enzyme_families', 'L3341_all_blind', 'L3421_protists_ladderp',
          'L3493_motif_panel', 'L3489_blind_tests', 'L3493_battery', 'L3521_EtoK',
          'L3557_EtoK', 'L3573_navtree', 'L3593_kfamilies', 'L3609_battery_ratio', 'L3649_size_sodium', 'L3649_nr1_tree']:
    runpy.run_path('figures/%s.py' % s); plt.close('all'); print('rendered', s)
