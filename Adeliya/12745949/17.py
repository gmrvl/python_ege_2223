file=open('17.txt')
count=0
maxx=0
arr=[int(i) for i in file]
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if (arr[i]+arr[j])%62==0:
            count+=1
            maxx=max(maxx,arr[i]+arr[j])
print(count,maxx)