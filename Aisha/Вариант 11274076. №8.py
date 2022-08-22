for i in range (10000):
    s = i
    n = 4
    while s < 37:
        s = s + 3
        n = n * 2
    if n == 128:
        print(i)
        break