file=open('27_B.txt')
n = int(file.readline())
a = []

for i in file:
    point, prob = map(int, i.split())
    if prob % 36 == 0:
        a.append([point, prob // 36])
    else:
        a.append([point, prob // 36 + 1])
min_cost = 1000000000 ** 10

for i in range(n):
    s = 0
    for j in range(n):
        s += abs(a[i][0] - a[j][0]) * a[j][1]
    min_cost = min(s, min_cost)
print(min_cost)