for n in range(1, 1000):
    r = bin(n)[2:]
    if int(r) % 2 == 0:
        r = '1' + r + '0'
    elif int(r) % 2 != 0:
        r = '11' + r + '11'
    r = int(r, 2)
    if r > 52:
        print(n)
        break

