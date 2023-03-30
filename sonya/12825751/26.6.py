file = open('26.6.txt')
n = int(file.readline())
ns = []
for i in file:
    r, m = map(int, i.split())
    ns.append([r, m])
ns = sorted(ns)
maxx = 0
minn = 0
for i in range(1, len(ns)):
    if ns[i][0] == ns[i-1][0]:
        if ns[i][1] - ns[i - 1][1] == 14:
            maxx = ns[i][0]

for i in range(1, len(ns)):
    if ns[i][0] == maxx:
        if ns[i][1] - ns[i - 1][1] == 14:
            minn = ns[i - 1][1] + 1
print(maxx,minn)
