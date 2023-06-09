for n in range(1,1000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = r + '10'
    else:
        r = '1' + r + '01'
    r = int(r,2)
    if r > 516:
        print(n)