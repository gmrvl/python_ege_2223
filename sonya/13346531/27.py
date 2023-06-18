file = open('27A.txt')
N = int(file.readline())
K = int(file.readline())
ns = [int(i) for i in file]
maxsumm = 0
n = 0
for i in range(K,N):
    n = max(n, ns[i - K])
    maxsumm = max(maxsumm, n + ns[i])
print(maxsumm)