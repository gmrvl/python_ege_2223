for n in range(1,1000):
    r = bin(n)[2:]
    for i in range(2):
        if r.count('1') % 2 == 0:
            r = r[1:]
            while r[0] == '0':
                r = r[1:]
        else:
            r = '1' + r + '00'
    r = int(r, 2)
    if r > 100:
        print(n)