file = open('27B.txt')
N = int(file.readline())
K = int(file.readline())
n = [int(i) for i in file]
maxsumm = 0
for x in range(0, len(n)- 1):
    for y in range(x + (K + 1), len(n), K):
        maxsumm = max(maxsumm, n[x] + n[y])
print(maxsumm)
