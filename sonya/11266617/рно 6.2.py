for i in range(6,10001):
    s = i
    s = (s + 1) // 7
    n = 36
    while s < 2050:
        s = s * 2
        n = n + 3
    if n==60:
        print(i)