# REVC
with open('/Users/makbuk/Downloads/rosalind_revc.txt') as file:
    lines = file.readlines()
string = lines[0].strip()
mapping = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
complement = ''.join(mapping[char] for char in string)[::-1]
print(complement)
