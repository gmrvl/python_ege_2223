for i in range(1, 10001):
    x = i
    L = 0
    M = 0
    while x > 0:
        M = M + 1
        if x % 2 != 0:
            L = L + 1
        x = x // 2
    if L == 5 and M == 6:
        print(i)
        break 