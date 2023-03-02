for n in range(2,1000):
    r = bin(n)[2:]
    if r.count('1') % 2 == 0:
        r = '11' + r + '1'
    else:
        r = '11' + r
    r = int(r, 2)
    if r >= 457:
        print(n)