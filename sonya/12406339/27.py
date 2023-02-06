file = open('27_B.txt')

n = int(file.readline())

a = []

for i in file:
    point, prob = map(int, i.split())
    if prob % 36 == 0:
        a.append([point, prob // 36])
    else:
        a.append([point, prob // 36 + 1])
minn = 10**10000000
do = [0]*n
do[0] = a[0][1]

for i in range(1, n):
    do[i] = do[i - 1] + a[i][1]

zatrat = 0

for i in range(n):
    zatrat += abs(a[i][0] - a[0][0]) * a[i][1]

for i in range(1, n):
    rast = (a[i][0] - a[i-1][0])
    zatrat = zatrat + rast*do[i-1] - rast*(do[-1] - do[i-1])
    minn = min(minn,zatrat)
print(minn)


