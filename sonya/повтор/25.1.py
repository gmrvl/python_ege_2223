for n in range(210235, 210301):
    sqn = int(n**0.5)
    dells = []
    for dell in range(2, sqn + 1):
        if n % dell == 0:
            dell2 = n // dell
            if dell2 == dell:
                dells.append(dell)
            else:
                dells.append(dell)
                dells.append(dell2)
    if len(dells) == 4:
        print(sorted(dells))
