file = open('26.5.txt')
N = int(file.readline())
a = []
for i in file:
    r, m = map(int, i.split())
    a.append([r, m])
a = sorted(a)
maxx = 0
minn = 0
for i in range(1, len(a)):
    if a[i][0] == a[i-1][0]:
        if a[i][1] - a[i-1][1] == 3:
            maxx = a[i][0]
for i in range(1, len(a)):
    if a[i][0] == maxx:
        if a[i][1] - a[i-1][1] == 3:
            minn = a[i-1][1] + 1
            break
print(maxx, minn)


