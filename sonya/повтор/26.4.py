file = open('26.4.txt')
N, M = map(int, file.readline().split())
b = []
for i in file:
    x, z, y = i.split()
    if y == 'A':
        M -= int(x) * int(z)
    else:
        b.append([int(x), int(z)])
b = sorted(b)
count = 0
for i in range(0, len(b)):
    for j in range(0, b[i][1]):
        if M - b[i][0] >= 0:
            M -= b[i][0]
            count += 1
        else:
            break
print(count, M)


