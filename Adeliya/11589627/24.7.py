file=open('24.7.txt').read()

count=0
maxcount=0
last=0

for i in file:
    if i=='K':
        if last == 2:
            if count>maxcount:
                maxcount=count
            count = 1
        else:
            count+=1
        last = 1
    elif i=='L':
        if last==1:
            if count>maxcount:
                maxcount=count
            count = 1
        else:
            count+=1
        last = 2
    else:
        count+=1
        last = 0
if count>maxcount:
    maxcount=count
print(maxcount)
