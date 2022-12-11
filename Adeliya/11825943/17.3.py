file= open('17.3.txt')
count=0
summ=0
maxsumm=0
last=int(file.readline())
for i in file:
    i=int(i)
    if (last*i)%15==0:
        summ=last+i
        if summ%7==0:
            count+=1
            if summ>maxsumm:
                maxsumm=summ
    last=i
if summ>maxsumm:
    maxsumm=summ
print(count,maxsumm)
