file = open('27_A.txt')
n = int(file.readline())
a = []
for i in file:
    punct, prob = map(int, i.split())
    if prob % 36 == 0:
        a.append([punct, prob // 36])
    else:
        a.append([punct, prob // 36 + 1])
minn = 10**1000000
do = [0] * n
do[0] = a[0][1]
for i in range(1, n):
    do[i] = do[i-1] + a[i][1]
s0 = 0
for i in range(n):
    s0 += abs(a[i][0] - a[0][0]) * a[i][1]
for i in range(1, n):
    rast = (a[i][0] - a[i-1][0])
    s0 = s0 + rast*do[i-1] - rast*(do[-1] - do[i-1])
    minn = min(minn, s0)
print(minn)

