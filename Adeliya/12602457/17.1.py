file=open('17.1.txt')
count=0
maxx=0

arr = [int(i) for i in file]
for i in range(len(arr) - 2):
    arr1 = sorted([arr[i], arr[i + 1], arr[i + 2]])
    if arr1[2]**2 < (arr1[1]**2 + arr1[0]**2):
        count += 1
        maxx = max(maxx, sum(arr1))
print(count, maxx)