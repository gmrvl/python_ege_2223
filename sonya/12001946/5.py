for n in range(1, 1000):
    r = bin(n)[2:]
    s = r.count('1')
    if s % 2 == 0:
        r = r + '00'
    else:
        r = r + '10'
    r = int(r, 2)
    if r > 85:
        print(n)
        break

