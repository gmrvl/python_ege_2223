file=open('24.1.txt').read()
count=0
maxcount=0
last=''
for i in file:
    if last!=i:
        count+=1
    else:
        if count>maxcount:
            maxcount=count
        count=0
    last=i
if count>maxcount:
    maxcount=count
print(maxcount)