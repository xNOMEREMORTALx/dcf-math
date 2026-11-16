"""L3669 amendment helper: UniParc FASTA (gz) -> UniProt-style TSV (gz) with Entry, Organism, Protein names, Sequence.
argv: in.fasta.gz out.tsv.gz organism_name. Entry = first header word without '>'. Protein names left empty. No sequence is changed."""
import gzip,sys
i,o,org=sys.argv[1:4]; rows=[]; a=None; s=[]
for l in gzip.open(i,'rt'):
    l=l.strip()
    if l.startswith('>'):
        if a: rows.append((a,''.join(s)))
        a=l[1:].split()[0]; s=[]
    elif l: s.append(l)
if a: rows.append((a,''.join(s)))
with gzip.open(o,'wt') as f:
    f.write('Entry\tOrganism\tProtein names\tSequence\n')
    for a,q in rows: f.write('%s\t%s\t\t%s\n'%(a,org,q))
print('records',len(rows))
