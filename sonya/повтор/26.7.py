file = open('26.7.txt')
N, M = map(int, file.readline().split())
n = []
a = []
b = []
for i in file:
    x, y = i.split()
    if y == 'A':
        a.append(int(x))
    else:
        b.append(int(x))
    n.append(int(x))
n = sorted(n)
a = sorted(a)
b = sorted(b)
count = 0
m = 0
for i in n:
    if m + i <= M:
        count += 1
        m += i
ma = []
for i in a:
    if len(ma) >= count:
        break
    if sum(ma) + i <= M:
        ma.append(i)
    else:
        break
mb = []
for i in b:
    if len(ma) + len(mb) >= count:
        break
    if (sum(mb) + sum(ma) + i) <= M:
        mb.append(i)
    else:
        while (sum(mb) + sum(ma) + i) > M:
            del ma[-1]
        mb.append(i)
print(print(len(ma), M - sum(mb) - sum(ma)))


