# gc
from Bio import SeqIO
max_gc_id = ""
max_gc_content = 0
with open("/Users/makbuk/Downloads/rosalind_gc.txt", "r") as handle:
    for record in SeqIO.parse(handle, "fasta"):
        id = record.id
        seq = record.seq
        
        def GC(seq):
            G = seq.count('G')
            C = seq.count('C')
            GC_content = (G + C) / len(seq) * 100  
            return GC_content
        
        gc_content = GC(seq)
        
        if gc_content > max_gc_content:
            max_gc_content = gc_content
            max_gc_id = id

print(max_gc_id)
print(max_gc_content)
