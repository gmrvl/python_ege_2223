file=open('17.txt')
count=0
maxx=0
arr=[int(i) for i in file]
for i in range(len(arr)):
    arr[i]=int(arr[i])
for i in range(len(arr)-1):
    if (arr[i]%5==0 or arr[i+1]%5==0) and (arr[i]+arr[i+1])%7==0:
        count+=1
        maxx=max(maxx,arr[i]+arr[i+1])
print(count,maxx)