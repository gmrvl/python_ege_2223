file=open('17.3.txt')
count=0
maxx=0
arr=[int(i) for i in file]
for i in range(len(arr)-1):
    if (arr[i]%3==0) or (arr[i+1]%3==0):
        count+=1
        maxx=max(maxx,arr[i]+arr[i+1])
print(count,maxx)
