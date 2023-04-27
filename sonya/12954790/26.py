file = open('26.txt')
N, M = map(int, file.readline().split())
m = 0
a = []
b = []
ab = []
for i in file:
    y, x = i.split()
    if x == 'A':
        a.append(int(y))
    else:
        b.append(int(y))
    ab.append(int(y))

ab = sorted(ab)
b = sorted(b)
a = sorted(a)

maxcount = 0
for i in ab:
    if m + i <= M:
        m += i
        maxcount += 1
    else:
        break

ass = []
m0 = 0
for i in a:
    if len(ass) >= maxcount:
        break
    if m0 + i <= m:
        ass.append(i)
        m0 += i

bss = []
for i in b:
    if m0 + i <= M:
        bss.append(i)
        m0 += i
    else:
        if len(ass) + len(bss) > maxcount:
            del ass[-1]
            bss.append(i)
print(len(ass), M - m0)

