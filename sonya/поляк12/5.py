for n in range(1,1000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = r + bin(r.count('1'))[2:]
    else:
        r = '1' + r + '00'
    r = int(r,2)
    if r > 215:
        print(n)