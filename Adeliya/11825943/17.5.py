file=open('17.5.txt')
count=0
last=0
summ=0
maxsumm=0

s=0
c=0
for i in file:
    i=int(i)
    if i%2==0:
        s+=i
        c+=1
sre = s // c

for i in file:
    i=int(i)
    if last%3==0 or i%3==0:
        if last<sre or i<sre:
            count+=1
            summ=last+i
            if summ>maxsumm:
                maxsumm=summ
    last=i
if summ>maxsumm:
    maxsumm=summ
print(count,maxsumm)
