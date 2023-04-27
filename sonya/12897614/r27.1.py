file = open('р27-B_demo.txt')
minsumm = 0
minne3 = 0
n = int(file.readline())
ns = []
maxs = []
mins = []
for i in file:
    x, y = map(int, i.split())
    ns.append([x, y])

for i in range(n):
    minsumm += min(ns[i][0], ns[i][1])
    maxs.append(max(ns[i][0], ns[i][1]))
    mins.append(min(ns[i][0], ns[i][1]))



if minsumm % 3 == 0:
    maxx = maxs.index(min(maxs))
    minn = mins.index(min(mins))
    summ1 = minsumm - min(ns[maxx][0], ns[maxx][1]) + max(ns[maxx][0], ns[maxx][1])
    summ2 = minsumm - min(ns[minn][0], ns[minn][1]) + max(ns[minn][0], ns[minn][1])
    minsumm = min(summ1, summ2)
    if minsumm % 3 == 0:
        minsumm = max(summ1, summ2)
print(minsumm, minsumm/3)

