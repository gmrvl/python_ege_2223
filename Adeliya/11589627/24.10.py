file=open('24.10.txt').read()

count=0
maxcount=0
last=0

for i in file:
    if i=='A' or i=='C':
        if last==2:
            last = 1
        else:
            last = 0
    elif i=='B':
        if last==1:
            count+=1
        else:
            if count>maxcount:
                maxcount=count
            count = 1
        last = 2
if count > maxcount:
    maxcount = count
print(maxcount)




