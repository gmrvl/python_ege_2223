for i in range(200000000,400000000):
    m = 0
    n = 0
    l = i
    while l > 1:
        if l % 2 == 0:
            m += 1
            l //= 2
        elif l % 3 == 0:
            n += 1
            l //= 3
        else:
            break
    if m % 2 == 0 and n % 2 != 0 and l == 1:
        print(i)