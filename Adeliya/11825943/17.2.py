file=open('17.2.txt')
count=0
last=0
summ=0
maxsumm=0
for i in file:
    i=int(i)
    if last%3==0 or i%3==0:
        summ=last+i
        if summ%5==0:
            count+=1
            if summ>maxsumm:
                maxsumm=summ
    last=i
if summ>maxsumm:
    maxsumm=summ
print(count,maxsumm)
