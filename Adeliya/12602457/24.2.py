f=open('24.2.txt').read()
count=0
maxcount=0
for i in range(len(f)-1):
    if ((f[i] != 'K' and f[i + 1] != 'L') or (f[i] != 'L' and f[i + 1] != 'K')):
        count+=1
    else:
        if count>maxcount:
            maxcount=count
        count=1
if count>maxcount:
    maxcount=count
print(maxcount)

