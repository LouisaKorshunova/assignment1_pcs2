# RNA
with open('/Users/makbuk/Downloads/rosalind_rna.txt') as file:
    lines = file.readlines()
rna = lines[0].strip()
print(rna.replace('T','U'))
