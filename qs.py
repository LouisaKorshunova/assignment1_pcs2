#qs
file = '/Users/makbuk/Downloads/rosalind_qs.txt'
with open (file,'r') as file:
    lines = file.readlines()
lst = [int(i) for i in lines[1].strip().split()]
lst = sorted(lst)
lst = ' '.join([str(x) for x in lst])
print(lst)
