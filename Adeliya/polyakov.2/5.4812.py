for i in range(10, 100000000):
    s1 = 0
    s2 = 0
    b = str(i)
    for j in b:  # 2121
        if j in '13579':
            s1 += int(j)
    for k in range(1, len(b), 2):
        s2 += int(b[k])
    r = abs(s1-s2)
    if r == 29:
        print(i)
        break
