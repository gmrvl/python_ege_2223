file=open('24.1.txt').read()
count=0

maxcount = 0
last = 0
for i in file:
    if i == 'X':
        last = 1
        count+=1
    elif i=='Z':
        if last == 1:
            last = 2
        elif last == 2:
            last = 3
        else:
            last = 0
        count+=1
    elif i == 'Y':
        if last == 3:
            if count>maxcount:
                maxcount = count
            count=3
        else:
            count+=1
        last=4
if count>maxcount:
    maxcount=count
print(maxcount)
