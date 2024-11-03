# prot
from Bio.Seq import Seq
with open("/Users/makbuk/Downloads/rosalind_prot.txt", "r") as handle:
    seq = Seq(handle.read())
    print(seq.translate())
