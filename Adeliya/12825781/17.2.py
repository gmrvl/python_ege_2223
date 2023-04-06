file=open('17.2.txt')
count=0
maxx=0
s=0
n=0
arr=[int(i) for i in file]
for i in range(len(arr)):
    if arr[i]%2==1:
        s+=arr[i]
        n+=1
x=s/n
for i in range(len(arr)-1):
    if (arr[i]%5==0 or arr[i+1]%5==0)  and (arr[i]< x or arr[i+1]<x):
        count+=1
        maxx=max(maxx,arr[i]+arr[i+1])
print(count,maxx)