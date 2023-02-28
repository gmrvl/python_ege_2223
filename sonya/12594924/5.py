for n in range(2,1000):
    r = bin(n)[2:]
    if r.count('1') > r.count('0'):
        r = r + '1'
    else:
        r = r + '0'
    r = int(r,2)
    if r > 100:
        print(r)