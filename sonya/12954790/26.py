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
    if m0 + i <= M:
        ass.append(i)
        m0 += i

bss = []
for i in b:
    if len(ass) + len(bss) >= maxcount: break
    if m0 + i <= M:
        bss.append(i)
        m0 += i
    else:
        if m0 + i > M:
            while m0 + i > M:
                m0 -= ass[-1]
                del ass[-1]
            bss.append(i)
            m0 += i
print(len(ass), M - m0)

