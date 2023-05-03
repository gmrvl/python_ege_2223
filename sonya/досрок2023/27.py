file = open('27B.txt')
N = int(file.readline())
K = int(file.readline())
ns = [int(i) for i in file]
maxsumm = 0
for x in range(0, len(ns)- 1):
    for y in range(x + (K + 1), len(ns), K):
        maxsumm = max(maxsumm, ns[x] + ns[y])
print(maxsumm)
