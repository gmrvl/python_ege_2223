file = open('26.txt')
N, M = map(int, file.readline().split())
A = []
B = []
for i in file:
    x, y, z = i.split()
    x = int(x)
    y = int(y)
    if z == 'A':
        A.append([x,y])
    else:
        B.append([x,y])

A = sorted(A)
m = 0
for i in range(0, len(A)):
    for j in range(A[i][1]):
        if m + A[i][0] <= M:
            m += A[i][0]
        else:
            break

B = sorted(B)
countb = 0
for i in range(0, len(B)):
    for j in range(B[i][1]):
        if m + B[i][0] <= M:
            m += B[i][0]
            countb += 1
        else:
            break
print(countb, M - m)

