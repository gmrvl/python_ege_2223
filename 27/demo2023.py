file = open('47231.txt')

n = int(file.readline())

a = []

for i in file:
    point, prob = map(int, i.split())
    if prob % 36 == 0:
        a.append([point, prob // 36])
    else:
        a.append([point, prob // 36 + 1])
minn = 10 ** 100000
do = n * [0] # сумма количества контейнеров из всех пунктов ДО лаборатории
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

# решение перебором
# for i in range(n):
#     s = 0
#     for j in range(n):
#         s += abs(a[i][0] - a[j][0]) * a[j][1]
#     minn = min(s, minn)
# print(minn)
