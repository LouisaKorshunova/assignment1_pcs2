with open('/Users/makbuk/Downloads/rosalind_dna.txt') as file:
    lines = file.readlines()
string = lines[0].strip()
A=string.count('A')
C=string.count('C')
G=string.count('G')
T=string.count('T')
list = [A]+[C]+[G]+[T]
list = [str(i) for i in list]
list = ' '.join(list)
print(list)
