#par
file_path = '/Users/makbuk/Downloads/rosalind_par.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()
n = int(lines[0].strip())
arr = lines[1].split()
arr = [int(i) for i in arr]
pivot = arr[0]
arr1 = []
arr2 = []
for x in arr[1:]:
    if x <= pivot:
        arr1.append(x)
    else:
        arr2.append(x)
print(*arr1, pivot, *arr2)
