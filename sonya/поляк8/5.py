ch = '02468'
nch = '13579'
for n in range(0,1000000000):
    n = str(n)
    s1 = 0
    s2 = 0
    for i in range(0, len(n)):
        if n[i] in nch:
            s1 += int(n[i])
        if len(n) % 2 == 0:
            if i % 2 == 1:
                s2 += int(n[i])
        elif len(n) % 2 != 0:
            if i % 2 == 0:
                s2 += int(n[i])
    r = abs(s2 - s1)
    if r == 29:
        print(n)
        break