for i in range(0,100000):
    s = i
    n = 1
    while s < 47:
        s = s + 4
        n = n * 2
    if n == 64:
        print(i)