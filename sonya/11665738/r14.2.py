for A in range(1, 1000):
    for x in range(0,9):
        M = int('842' + str(x) + '5', 9)
        N = int('8' + str(x) + '725', 9)
        if (M + A) % N == 0:
            print(A)
            break