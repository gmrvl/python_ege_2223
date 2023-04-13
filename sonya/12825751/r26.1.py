file = open('р26.1.txt')
N, M = map(int, file.readline().split())
a = []
b = []
ab = []
for i in file:
    x, y = i.split()
    if y == 'A':
        a.append(int(x))
    else:
        b.append(int(x))
    ab.append(int(x))
ab = sorted(ab)
m0 = 0
maxcount = 0
for i in ab:
    if m0 + i <= M:
        m0 += i
        maxcount += 1

a = sorted(a)
b = sorted(b)
m = 0
As = []
for i in a:
    if len(As) > maxcount:
        break
    else:
        if m + i <= m0:
            m += i
            As.append(i)
Bs = []
for i in b:
    if m + i <= m0:
        Bs.append(i)
    else:
        if len(Bs) + len(As) < maxcount:
            del As[-1]
            Bs.append(i)
        else:
             break
print(len(Bs), M - m0)

