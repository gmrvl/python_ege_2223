for i in range(1, 10000):
    n = str(bin(i)[2:])
    n = n[:-1]
    if i % 2 != 0:
        n += "10"
    else:
        n += "01"
    r = int(n, 2)
    if r == 2017:
        print(i)