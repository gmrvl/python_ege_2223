for i in range(10, 100000000):
    s1 = 0
    s2 = 0
    b = str(i)
    for j in b:
        if j in '2468':
            s1 += int(j)
    for k in range(0, len(b), 2):
        s2 += int(b[k])
    r = abs(s1-s2)
    if r == 26:
        print(i)
        break
