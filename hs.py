# hs
file = '/Users/makbuk/Downloads/rosalind_hs.txt'
with open (file,'r') as file:
    lines = file.readlines()
a = [int(i) for i in lines[1].strip().split()]
z = lambda x: (x-1)//2
q = lambda x: 2*x+1
n = int(lines[0].strip()) 
for i in range(1, n):
    j = i
    while j > 0 and a[j] > a[z(j)]:
        a[j], a[z(j)] = a[z(j)], a[j]
        j = z(j)

for i in range(n-1, 0, -1):
    a[0], a[i] = a[i], a[0]
    j = 0
    while q(j) < i:
        k, l = q(j), j
        if a[l] < a[k]: l = k
        if k+1 < i and a[l] < a[k+1]: l = k+1
        if l == j: break
        a[j], a[l] = a[l], a[j]
        j = l

print(*a)


