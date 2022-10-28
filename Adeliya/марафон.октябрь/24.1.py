file=open('24.1.txt').read()
count=0
maxcount=0
for i in file:
    if i=='Y':
        count+=1
    else:
        if count>maxcount:
            maxcount=count
        count=0
if count>maxcount:
    maxcount=count
print(maxcount)