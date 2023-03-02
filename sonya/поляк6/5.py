for n in range(2,1000):
    r = bin(n)[2:]
    if r.count('1') % 2 == 0:
        r = '1' + r + '00'
    else:
        r = '11' + r
    r = int(r,2)
    if r >= 412:
        print(n)
        break