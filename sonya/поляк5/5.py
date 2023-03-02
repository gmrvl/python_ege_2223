for n in range(1000_0000_0000_0000, 10_000_000_000_000_000):
    n = str(n)
    a = list(n)
    for i in range(0, 16):
        if i % 2 == 0:
            a[i] = int(a[i]) * 2
            if len(str(a[i])) == 2:
                s = str(a[i])
                a[i] = str(int(s[0]) + int(s[1]))
    summ = 0
    for i in range(0,16):
        summ += int(a[i])
    if summ == 30:
        n = int(n)
        print(n % (10**8), n, a)
        break