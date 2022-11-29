count = 0
n = 11000001
while count < 5:
    dells = []
    sqn = int(n ** 0.5)
    for i in range(2, sqn + 1):
        if n % i == 0:
            dells.append(i)
        if len(dells) >= 2:
            break
    if len(dells) < 2:
        res = 0
    else:
        res = n // dells[0] + n // dells[1]
    if 0 < res < 10000:
        print(res, n)
        count += 1
    n += 1
