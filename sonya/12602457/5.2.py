for n in range(2,1000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = r + '00'
    else:
        r = r + '11'
    if int(r,2) < 134:
        print(n)