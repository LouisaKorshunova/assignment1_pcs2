# ps
file_path = '/Users/makbuk/Downloads/rosalind_ps-2.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()
lst = [int(i) for i in lines[1].strip().split()]
k = int(lines[2].strip())
lst = sorted(lst)
lst = lst[:k]
print(*lst)
