file = open('р26.2.txt')
ns = [int(i) for i in file]
nss = set(ns)
count = 0
maxsumm = 0
for x in range(0, len(ns) - 1):
    for y in range(x + 1, len(ns)):
        if ((ns[x] % 2) == (ns[y] % 2)):
            summ = ns[x] + ns[y]
            if summ in nss:
                count += 1
                maxsumm = max(maxsumm, summ)
print(count, maxsumm)


