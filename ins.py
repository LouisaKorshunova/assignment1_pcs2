#ins 
with open('/Users/makbuk/Downloads/rosalind_ins.txt') as file:
    lines = file.readlines()  

result = [line.strip().split() for line in lines[1:] if len(line.strip()) > 0]
l1 = [int(item) for sublist in result for item in sublist]  
def ins(l1):
    counter = 0
    for i in range(1, len(l1)):
        x = l1[i]
        j = i - 1
        while j >= 0 and l1[j] > x:
            l1[j + 1] = l1[j]
            j -= 1
            counter += 1
        l1[j + 1] = x  
    return counter
print(ins(l1))
