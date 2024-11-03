#par3
file_path = '/Users/makbuk/Downloads/rosalind_par3.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()
n = int(lines[0].strip())
arr = lines[1].strip().split()
arr = [int(i) for i in arr]
pivot = arr[0]
less_than_pivot = []
equal_to_pivot = []
greater_than_pivot = []
for x in arr:
    if x < pivot:
        less_than_pivot.append(x)
    elif x == pivot:
        equal_to_pivot.append(x)
    else:
        greater_than_pivot.append(x)

result = less_than_pivot + equal_to_pivot + greater_than_pivot
result = ' '.join([str(x) for x in result])
print(result)
