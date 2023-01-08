for n in range(110203, 110246):
    dells = []
    sqn = int(n ** 0.5)
    if n % 2 == 0:
        dells.append(n)
    for dell in range(2, sqn + 1):
        if n % dell == 0:
            dell2 = n // dell
            if dell % 2 == 0:
                dells.append(dell)
            if dell2 % 2 == 0:
                dells.append(dell2)
        if len(dells) > 4:
            break
    if len(dells) == 4:
        print(dells)

