# hamm
file=open("/Users/makbuk/Downloads/rosalind_hamm.txt")
line=file.readlines()
string1=str(line[0].strip())
string2=str(line[1].strip())
distance = 0
for n in range(len(string1)):
    if string1[n] != string2[n]:
        distance +=1
    else:
        distance = distance

print(distance)
