file = open('26.2.txt')
n = int(file.readline())
ns = []
for i in file:
    x, y = map(int, i.split())
    ns.append([x,y])
ns = sorted(ns)
maxx = 0
for i in range(1, len(ns)):
    if ns[i][0] == ns[i-1][0]:
        if ns[i][1] - ns[i-1][1] == 14:
            maxx = ns[i][0]
minn = 0
for i in range(1,len(ns)):
    if ns[i][0] == maxx:
        if ns[i][1] - ns[i-1][1] == 14:
            minn = ns[i-1][1] + 1
print(maxx, minn)