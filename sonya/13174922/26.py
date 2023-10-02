file = open('inf_26_04_21_26.txt')
n = int(file.readline())
ns = [int(i) for i in file]
count = 0
maxsumm = 0
nss = set(ns)
for x in range(0, len(ns) - 1):
    for y in range(x + 1, len(ns)):
        dx = ns[x] % 2
        dy = ns[y] % 2
        if dx == dy:
            if (ns[x] + ns[y]) in nss:
                count += 1
                maxsumm = max(maxsumm, (ns[x]+ ns[y]))
print(count, maxsumm)

