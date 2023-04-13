file=open('24.8.txt').read()
string=''
maxstring=0
for i in file:
    if i=='E':
        string=''
    else:
        string+=i
        if string.count('A') >= 3 and len(string) > maxstring:
            maxstring=len(string)
if string.count('A') >= 3 and len(string) > maxstring:
    maxstring=len(string)
print(maxstring)
