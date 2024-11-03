# med
file_path = '/Users/makbuk/Downloads/rosalind_med-2.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()
lst = [int(i) for i in lines[1].strip().split()]
k = int(lines[2].strip())
lst = sorted(lst)
print(lst[k - 1])  
