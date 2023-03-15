file = open('107_26.txt')

n = int(file.readline())
ns = []
for i in file:
    x, y = map(int, i.split())
    ns.append([x, y])
ns = sorted(ns)
maxxi = 0
minni = 0
for i in range(1, n):
    if ns[i][0] == ns[i - 1][0]:
        if ns[i][1] - ns[i - 1][1] == 14:
            maxxi = ns[i][0]
            minni = ns[i - 1][1]
            continue
print(maxxi, minni)
