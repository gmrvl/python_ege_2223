file = open('27890B.txt')

n = file.readline()
maxSum = 0
minRaz = 10001
for i in file:
    a, b = i.split(' ')
    a, b = int(a), int(b)
    maxSum += max(a, b)
    k = abs(a - b)
    if minRaz > k and k % 5 != 0:
        minRaz = k
if maxSum % 5 == 0:
    print(maxSum - minRaz)
else:
    print(maxSum)

