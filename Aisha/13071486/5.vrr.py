for i in range(1, 100):
    n = bin(i)[2:]
    n += str(n.count('1') % 2)
    n += str(n.count('1') % 2)
    res = int(n, 2)
    if res < 90:
        print(res)
