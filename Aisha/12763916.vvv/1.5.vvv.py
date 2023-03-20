for i in range (1, 10000):
    n = bin(i)[2:]
    n = str(n)
    n += str(n.count("1") % 2)
    n += str(n.count("1") % 2)

    s = int(n, 2)
    if s < 90:
        print(s)