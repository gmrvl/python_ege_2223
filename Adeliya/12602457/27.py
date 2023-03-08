file=open('27.A.txt')
n=int(file.readline())
summ=0
maxx=0
for i in file:
    a,b=i.split('  ')
    a=int(a)
    b=int(b)
    summ+=min(a,b)
    maxx=max(maxx,max(a,b))
if summ%3==0:
    print(summ)