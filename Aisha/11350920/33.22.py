for i in range (1, 100001):
    x = i
    Q = 6
    L = 0
    while x >= Q:
        L = L + 1
        x = x - Q
    M = x
    if M < L:
        M = L
        L = x
    if L == 3 and M == 5:
        print(i)