file=open('17.txt')
count=0
maxx=0
a=[int(i) for i in file]
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if (a[i]+a[j])%126==0:
            count+=1
            maxx=max(maxx,a[i]+a[j])
print(count,maxx)

