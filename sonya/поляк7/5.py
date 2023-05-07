for n in range(0,100000000):
    n = str(n)
    s1 = 0
    for i in range(0, len(n) - 1):
        if int(n[i]) % 2 == 0:
            s1 += int(n[i])
    r = ''
    for i in range(0, len(n) - 1):
        r = n[i] + r
    s2 = 0
    for i in range(0, len(n) - 1):
        if i % 2 == 0:
            s2 += int(r[i])
    r = abs(s1 - s2)
    if r == 26:
        print(n)
        break

