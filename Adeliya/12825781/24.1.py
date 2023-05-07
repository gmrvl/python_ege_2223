file=open('24.1.txt').read()
count=0
maxcount=0
last=''
for i in file:
    if i=='K':
        if last=='L':
            maxcount=max(maxcount,count)
            count=1
        else:
            count+=1
    elif i=='L':
        if last=='K':
            maxcount=max(maxcount,count)
            count=1
        else:
            count+=1
    else:
        count+=1
    last=i
max(maxcount,count)
print(maxcount)



