for n in range(4,1000):
    r = bin(n)[2:]
    if n % 3 == 0:
        r = r + r[-3] + r[-2] + r[-1]
    else:
        ost = n % 3
        r = r + bin(ost*3)[2:]
    r = int(r,2)
    if r < 100:
        print(n)
