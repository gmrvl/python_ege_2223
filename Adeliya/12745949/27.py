file=open('27-B.txt')
n=int(file.readline())
a=[int(i) for i in file]
ch=0
summ=0
maxx=0
for i in range(len(a)):
    summ+=a[i]
    if a[i]%2==0:
        ch+=1
    if ch%10==0:
        maxx=max(maxx,summ)
print(maxx)
