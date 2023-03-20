for i in range(40, 10001):
    x = i
    L = x
    M = 5
    if L % 2 == 0:
                M = 24
    while L != M:
                if L > M:
                    L = L - M
                else:
                    M = M - L
    if M == 5:
        print(i)
        break