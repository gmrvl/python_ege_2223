file = open('27B.txt')
N = int(file.readline())
K = int(file.readline())
m = 0
a = [0] * N
a[0] = int(file.readline())
for i in range(1, K):
    value = int(file.readline())
    a[i] = max(a[i - 1], value)

result = 0
for i in range(K, N):
    value = int(file.readline())
    a[i] = max(a[i - 1], value)
    result = max(result, value + a[i - K])

print(result)

file.close()

