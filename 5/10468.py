for i in range(1, 10000):
    n = bin(i)[2:]
    summ = n.count('1')
    if summ % 2 == 0:
        n += '00'
    else:
        n += '10'
    r = int(n, 2)
    if r > 77:
        print(i)
        break