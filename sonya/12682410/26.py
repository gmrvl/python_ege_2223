file = open('107_26.txt')

n = int(file.readline())
ns = []
for i in file:
    x, y = map(int, i.split())
    ns.append([x,y])
ns = sorted(ns)
maxxi = 0
minni = 0
for i in range(1,n - 1):