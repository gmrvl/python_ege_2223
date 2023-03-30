file=open('27-A.txt')
a=[int(i) for i in file]
a=sorted(a)
count=0
ch=0
for i in range(len(a)):
    if a[i]%2==0:
        ch+=1
        count+=a[i]


