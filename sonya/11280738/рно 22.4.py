for i in range(101,10001):
        x = i
        L = x-30
        M = x+30
        while L != M:
            if L > M:
                L = L - M
            else:
                M = M - L
        if M == 30:
            print(i)