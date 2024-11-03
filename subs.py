# subs
file=open("/Users/makbuk/Downloads/rosalind_subs.txt")
line=file.readlines()
string=str(line[0].strip())
sub_string=str(line[1].strip())
for i in range(len(string)):
    if string[i:].startswith(sub_string):
        print(i+1,end=' ')
