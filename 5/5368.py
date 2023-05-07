for i in range(0, 1000):
    n = bin(i)[2:]
    if n.count('1') % 2 == 0:
        n += '0'
        n = '10' + n[2:]
    elif n.count('1') % 2 != 0:
        n += '1'
        n = '11' + n[2:]
    r = int(n, 2)
    if r < 35:
        print(i)

