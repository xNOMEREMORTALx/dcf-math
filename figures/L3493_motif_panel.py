"""Manuscript 2, Figure 1: the metal-selecting loops read from real sequences in six animals (values extracted by the DCF rules, L3493)."""
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
cols=['K$^+$ filter','Na$^+$ ring: lysine (K of DEKA)','Ca$^{2+}$ ring: E/D in 4 pore loops','Na$^+$/K$^+$ pump loop','Fe hydroxylase core']
rows=[('human','TLGYG (KCNC2)','TFKGW (SCN2A)','TMEGW TGEDW TGEGW TGEAW (CACNA1B)','YVPEGL (ATP4A)','CHELLGH (TPH2)'),
      ('mouse','TVGYG (Kcna1)','TFKGW (Scn2a)','TMEGW TGEDW TGEGW TGEAW (Cacna1b)','NVPEGL (Atp1a1)','CHELLGH (Th)'),
      ('zebrafish','TVGYG (kcna1a)','TFKGW (scn8aa)','TMEGW TGEDW TGEGW TGEAW (cacna1aa)','NVPEGL (atp1a1a.1)','VHELLGH (th)'),
      ('chicken','TVGYG (KCNA1)','TFKGW (SCN2A)','TMEGW TGEDW TFEGW TGEAW (CACNA1C)','NVPEGL (ATP1A1)','CHELLGH (TH)'),
      ('fruit fly','TVGYG (Sh)','TFKGW (para)','TMEGW TGEDW TGEGW TGEAW (cac)','NVPEGL (Atpalpha)','IHELLGH (ple)'),
      ('nematode','TVGYG (shk-1)','none: no Na$^+$ channels','(not in reviewed set)','SIPEGL (mca-1, Ca pump)','IHELLGH (cat-2)')]
fig,ax=plt.subplots(figsize=(13,3.6),dpi=150); ax.axis('off')
t=ax.table(cellText=[r[1:] for r in rows],rowLabels=[r[0] for r in rows],colLabels=cols,loc='center',cellLoc='center')
t.auto_set_font_size(False); t.set_fontsize(8.5); t.scale(1,1.6)
for (i,j),cell in t.get_celld().items():
    cell.set_edgecolor('#d0d7de')
    if i==0: cell.set_text_props(weight='bold',color='#1f2328'); cell.set_facecolor('#f6f8fa')
    if j==-1: cell.set_text_props(weight='bold')
    if i>0 and j>=0: cell.get_text().set_family('monospace')
ax.set_title('The metal-selecting loops of nerve proteins, read from sequence in six animals (~600 million years apart)',fontsize=11,loc='left',color='#1f2328')
plt.tight_layout(); plt.savefig('figures/L3493_motif_panel.png',bbox_inches='tight')
