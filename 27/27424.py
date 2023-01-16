file = open('27424B.txt')
n = file.readline()

maxSum = 0
minRaz = 10001

for i in file:
    a, b = i.split(' ')
    a = int(a)
    b = int(b)
    maxSum += max(a, b)
    k = abs(a - b)
    if k < minRaz and k % 3 != 0:
        minRaz = abs(a - b)
if maxSum % 3 == 0:
    print(maxSum - minRaz)
else:
    print(maxSum)

