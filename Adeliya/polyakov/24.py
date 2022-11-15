file=open('24.txt')
count=0
maxcount=0
n=file.readline()
for i in range(0, len(n)):
    if (n[i]!='Q') and (n[i+1]!='W'):
        count+=1
    else:
        if count>maxcount:
            maxcount=count
        count=0
print(maxcount)