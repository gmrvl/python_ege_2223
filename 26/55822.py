file = open('55822.txt')

k = int(file.readline())
n = int(file.readline())
a = sorted([list(map(int, i.split())) for i in file])

g = [0] * k
count = 0
last = 0
for i in a:
    for j in range(len(g)):
        if g[j] == 0 or i[0] - g[j] >= 1:
            g[j] = i[1]
            count += 1
            last = j + 1
            break

print(count, last)
