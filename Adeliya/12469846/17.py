file=open('17.txt')
n=file.readlines()
count=0
maxx=0
mini=100000
for i in range(len(n)):
    n[i]=int(n[i])
for i in range(len(n)):
    if n[i]%21==0 and n[i]< mini:
        mini=n[i]
for i in range(len(n)-1):
    if (n[i]%mini==0) or (n[i+1]%mini==0):
        count+=1
        maxx=max(maxx,n[i]+n[i+1])
print(count,maxx)



