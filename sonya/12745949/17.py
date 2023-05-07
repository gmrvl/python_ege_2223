file = open('17.txt')
ns = [int(i) for i in file]
count = 0
maxsumm = 0
for x in range(0,len(ns) - 1):
    for y in range(x + 1, len(ns)):
        if (ns[x] * ns[y]) % 62 == 0:
            count += 1
            maxsumm = max(maxsumm, ns[x] + ns[y])
print(count, maxsumm)
