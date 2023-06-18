file = open('17.txt')
ns = [int(i) for i in file]
count = 0
maxsumm = 0
for x in range(0, len(ns) - 1):
    for y in range(x + 1, len(ns)):
        if abs(ns[x] - ns[y]) % 2 == 0:
            if ns[x] % 19 == 0 or ns[y] % 19 == 0:
                count += 1
                maxsumm = max(maxsumm, ns[x] + ns[y])
print(count, maxsumm)