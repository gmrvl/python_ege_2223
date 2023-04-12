file=open('24.3.txt')
count=0
maxcount=0
laast=''
n=file.readline().replace('AB','x')
n=n.replace('CB','x')
for i in range(len(n)):
    if n[i]=='x':
        count+=1
        maxcount=max(count,maxcount)
    else:
        count=0
print(maxcount)