file=open('24.1.txt').read()
count=0
maxcount=0
last=0

for i in file:
    if i =='A':
        if last==0 or last=='B':
            count+=1
        else:
            if count>maxcount:
                maxcount=count
            count=1
    if i=='B':
        if last=='A':
            count+=1
        else:
            if count>maxcount:
                maxcount=count
            count=0
    last=i
if count>maxcount:
    maxcount=count
print(maxcount)

