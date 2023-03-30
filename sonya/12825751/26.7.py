file = open('26.7.txt')
n = int(file.readline())
a = [[0] * 10001 for i in range(10001)]
for i in file:
    r, m = map(int, i.split())
    a[r][m] = 1

number = 0
maxx = 0
for i in range(10001):
    count = 0
    maxcount = 0
    for j in range(10001):
        if a[i][j] == 1:
            count += 1
        else:
            maxcount = max(maxcount, count)
            count = 0
    maxx = max(maxcount, maxx)

for i in range(10001):
    count = 0
    for j in range(10001):
        if a[i][j] == 1:
            count += 1
        else:
            if count == maxx:
                number = i
                break
            else:
                count = 0
print(maxx, number)
