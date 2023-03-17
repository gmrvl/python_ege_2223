file = open('26.5.txt')
n = int(file.readline())
maxs = 0
ns = []
for i in file:
    x, y = map(int, i.split())
    ns.append([x, y])
ns = sorted(ns)
for i in ns:
    print(i)
count = 1
maxcount = 0
for i in range(1, n):
    if ns[i][0] == ns[i - 1][0]:
        if ns[i][1] - ns[i - 1][1] == 2:
            count += 1
        else:
            if count > maxcount:
                maxcount = count
                maxs = ns[i - 1][0]
            count = 1
    else:
        if count > maxcount:
            maxcount = count
            maxs = ns[i - 1][0]
        count = 1
print(maxcount, maxs)



