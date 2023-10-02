for n in range(43):
    nb = bin(n)[2:]
    summ = nb.count('1')
    if summ % 2 == 0:
        r = nb + '00'
    else:
        r = nb + '10'
    r = int(r, 2)
    if r > 43:
        print(r)
        break

