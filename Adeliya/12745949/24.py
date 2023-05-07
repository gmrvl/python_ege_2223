file=open('24.txt').read()
count=0
maxcount=0
last=''
for i in file:
    if i=='a':
        if last=='d':
            maxcount=max(maxcount,count)
            count=1
        else:
            count+=1
    elif i=='d':
        if last=='a':
            maxcount=max(maxcount,count)
            count=1
        else:
            count+=1
    else:
        count+=1
    last=i
maxcount=max(maxcount,count)
print(maxcount)

