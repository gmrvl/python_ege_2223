file = open('27_A.txt')

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

zatrat = 0
for i in range(n):
    zatrat = 0
    for x in range(n):
        zatrat += abs(a[i][0] - a[x][0]) * a[x][1]
    minn = min(zatrat,minn)
print(minn)