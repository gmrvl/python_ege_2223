file = open('26.3.txt')
N, M = map(int, file.readline().split())
B = []
for i in file:
    a, b, c = i.split()
    a = int(a)
    b = int(b)
    if c == 'A':
        M -= a*b
    else:
        B.append([a, b])
m = 0
count = 0
B = sorted(B)
print(B)
for i in range(0, len(B)):
    n = B[i][1]
    for j in range(1, n + 1):
        if m + B[i][0] <= M:
            count += 1
            m += B[i][0]
        else:
            break

print(count, M - m)