file = open('27A.txt')
N = int(file.readline())
K = int(file.readline())
a = []
for i in range(K):
    a.append(int(file.readline()))
maxsumm=0
max_digit = 0
for d in file:
    d = int(d)
    maxsumm = max(d + max_digit, maxsumm)
    for i in range(len(a)-1):
        a[i] = a[i + 1]
    a[-1] = d
    max_digit = max(a[0], max_digit)
print(maxsumm)

