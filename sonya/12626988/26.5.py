file = open('26.5.txt')
n = int(file.readline())
maxs = []
a = [10001 * [0] for j in range(10001)]
for i in file:
    x, y = map(int, i.split(' '))
    a[x][y] = 1
for i in range(10001):
    count = 0
    maxcount = 0
    c = 0
    for j in range(10001):
        if a[i][j] == 1 and (c == 0 or c == 1):
            count += 1
            c += 1
        if a[i][j] != 1 and c == 2:
            count += 1
            c = 0
        else:
            maxcount = max(maxcount, count)
            count = 0
            c = 0
    maxcount = max(maxcount, count)
    if maxcount > 0:
        maxs.append([maxcount, i])
maxs = sorted(maxs)
print(maxs)



