file = open('26.5.txt')
n = file.readline()
a = []
for i in file:
    x, y = map(int, i.split(' '))
    a.append([x, y])
a = sorted(a)

b = []
for i in range(1, len(a)):
    if a[i] != a[i-1]:
        b.append(a[i])

count = 0
max_count = 0
num = 0
for i in range(1, len(b)):
    if b[i][0] == b[i - 1][0]:
        if b[i][1] - b[i - 1][1] == 2:
            count += 1
        else:
            if count > max_count:
                max_count = count
                num = b[i][0]
            count = 1
    else:
        if count > max_count:
            max_count = count
            num = b[i][0]
        count = 1

if count > max_count:
    max_count = count
    num = b[-1][0]
count = 1

print(max_count, num)
