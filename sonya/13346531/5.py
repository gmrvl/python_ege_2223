for n in range(2,10000):
    r = bin(n)[2:]
    r = r[0:-1]
    if n % 2 == 1:
        r = r + '10'
    else:
        r = r + '01'
    r = int(r,2)
    if r == 2017:
        print(n)