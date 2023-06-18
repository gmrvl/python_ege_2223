for n in range(1,1000):
    r = bin(n)[2:]
    if r.count('1') % 2 == 1:
        r = r + '10'
    else:
        r = r + '00'
    r = int(r,2)
    if r > 97:
        print(n)