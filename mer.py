#mer 
file = open('/Users/makbuk/Downloads/rosalind_mer-3.txt')
lines = file.readlines()
n = int(lines[0])
lst1 = lines[1].split()
lst1 = [int(i) for i in lst1]
m = int(lines[2])
lst2 = lines[3].split()
lst2 = [int(i) for i in lst2]
a=sorted(lst1+lst2)
for i in a:
    print(i,end=' ')
