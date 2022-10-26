file=open('24.3.txt').read()
count=0
maxcount=0
last=3
for i in file:
    if i=='X':
        if last==3:
            count+=1
        else:
            if count>maxcount:
                maxcount=count
            count=1
        last=1
    if i=='Y':
        if last==1:
            count+=1
            last=2
        else:
            if count>maxcount:
                maxcount=count
            count=0
            last=0
    if i=='Z':
        if last==2:
            count+=1
            last=3
        else:
            if count>maxcount:
                maxcount=count
            count=0
        last=3
if count>maxcount:
    maxcount=count
print(maxcount)





