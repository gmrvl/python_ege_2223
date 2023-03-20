for i in range (1, 10001):
    x = i
    K = 9
    L = 0
    while x >= K:
        L = L + 1
        x = x - K
    M = x
    if M < L:
        M = L
        L = x
    if L == 5 and M == 8:
        print(i)
        break 
