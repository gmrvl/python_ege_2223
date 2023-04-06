file=open('24.4.txt').read()
count=0
maxcount=0
for i in file:
    if i=='B':
        count+=1
    else:
        if count>maxcount:
            maxcount=count
        count=0
if count>maxcount:
    maxcount=count
print(maxcount)