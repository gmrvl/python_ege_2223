for n in range(2,1000):
    r = bin(n)[2:]
    r = r + r[-1]
    if r.count('1') == 0:
        r = r + '0'
    else:
        r = r + '1'
    r = int(r,2)
    if r > 105:
        print(r)
        break
