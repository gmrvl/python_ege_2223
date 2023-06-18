for A in range(0,1000):
    for x in '012345678':
        M = int('842' + x + '5', 9)
        N = int('8' + x + '725', 9)
        if (M + A) % N == 0:
            print(A)
