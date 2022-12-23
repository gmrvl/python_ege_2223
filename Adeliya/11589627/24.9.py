file=open('24.9.txt').read()

count=0
maxcount=0
string=''
for i in file:
    if i=='A':
        string=''
    else:
        string+=i
        if string.count('E') >= 3:
            count+=1
            if count>maxcount:
                maxcount=count
if count>maxcount:
    maxcount=count
print(maxcount)