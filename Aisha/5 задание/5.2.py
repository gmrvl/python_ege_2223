for i in range(2, 10001):
    n = bin(i)[2:]
    n = str(n)
    n += n[1] + n[0]
    c = int (n, 2)
    if c > 74:
        print (i)
        break
