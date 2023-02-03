n = 11000000 + 1
count = 0

while count < 5:
    sqn = int(n ** 0.5)
    dells = []
    for dell in range(2, sqn + 1):
        if n % dell == 0:
            dell2 = n // dell
            if dell == dell2:
                dells.append(dell)
            else:
                dells.append(dell)
                dells.append(dell2)
    if len(dells) > 0:
        dells.sort()
        summ = dells[-1] + dells[-2]
        if summ < 10000:
            print(summ)
            count += 1
    n += 1

