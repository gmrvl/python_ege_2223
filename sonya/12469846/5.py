for n in range(2, 10000):
    r = bin(n)[2:-1]
    if n % 2 == 0:
        r += '01'
    else:
        r += '10'
    r = int(r, 2)
    if r == 2017:
        print(n)

