file = open('27_B.txt')
n = int(file.readline())
a = []
for i in file:
    x, y = map(int, i.split())
    if y % 36 == 0:
        a.append([x, y // 36])
    else:
        a.append([x, y // 36 + 1])
minn = 10 ** 1000000
do = [0] * n
do[0] = a[0][1]

for i in range(1, n):
    do[i] = do[i-1] + a[i][1]

s = 0

for i in range(n):
    rast = abs(a[i][0] - a[0][0])
    s += rast * a[i][1]


for i in range(1,n):
    rast = a[i][0] - a[i-1][0]
    s = s + rast * do[i-1] - rast * (do[-1]-do[i-1])
    minn = min(s, minn)
print(minn)


