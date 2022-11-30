for i in range(400000000, 600000001):
    m = 0
    n = 0
    s = i
    while s % 2 == 0 or s % 3 == 0:
        if s % 2 == 0:
            m += 1
            s //= 2
        if s % 3 == 0:
            n += 1
            s //= 3
    if s == 1 and m % 2 == 0 and n % 2 != 0:
        print(i)