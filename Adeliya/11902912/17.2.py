file=open('17.2.txt')
count=0
summ=0
maxsumm=0

s=0
c=0
for i in file:
    i=int(i)
    if i % 2 !=0:
        s+=i
        c+=1
sre=s//c

file=open('17.2.txt')
last=int(file.readline())

for i in file:
    i=int(i)
    if last%5==0 or i%5==0:
        if last < sre or i<sre:
            count+=1
            summ=last+i
            if summ>maxsumm:
                maxsumm=summ
    last=i
if summ >maxsumm:
    maxsumm=summ
print(count,maxsumm)


