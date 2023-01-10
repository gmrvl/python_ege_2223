for n in range(0, 1000):
    r = bin(n)[2:]
    s = r.count('1')
    if s % 2 == 0:
        r = r + '00'
    elif s % 2 != 0:
        r = r + '10'
    r = int(r, 2)
    if r > 97:
        print(r)
        break