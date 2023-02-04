for n in range(0, 100):
    r = bin(n)[2:]
    if r.count('1') % 2 == 0:
        r = r + '00'
    else:
        r = r + '10'
    if int(r,2) > 77:
        print(n)
        break