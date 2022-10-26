file=open('24.9.txt').read()
count=0
maxcount=0
last=''
for i in file:
    if last!= i:
        count+=1
    else:
        if count>maxcount:
            maxcount=count
        count=1
    last=i
if count>maxcount:
    maxcount=count
print(maxcount)