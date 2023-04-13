file=open('24.5.txt').read()

string=''
maxstring=0
for i in file:
    if i=='A':
        string=''
    else:
        string+=i
        if string.count('E') >= 3 and len(string) > maxstring:
            maxstring=len(string)
if string.count('E') >= 3 and len(string) > maxstring:
    maxstring=len(string)
print(maxstring)
