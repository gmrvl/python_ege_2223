file = open('26.5.txt')
n = int(file.readline())
maxs = 0
ns = []
lastx = ''
lasty = ''
for i in file:
    x, y = map(int, i.split())
    ns.append([x, y])
ns = sorted(ns)
nss = []
for i in range(1, len(ns)):
    if ns[i][0] != ns[i-1][0] or ns[i][1] != ns[i-1][1]:
        nss.append(ns[i])
count = 0
maxcount = 0
for i in range(1, len(nss)):
    if nss[i][0] == nss[i - 1][0]:
        if nss[i][1] - nss[i - 1][1] == 2:
            count += 1
        else:
            if count > maxcount:
                maxcount = count
                maxs = nss[i - 1][0]
            count = 1
    else:
        if count > maxcount:
            maxcount = count
            maxs = nss[i - 1][0]
        count = 1
print(maxcount, maxs)



