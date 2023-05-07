for n in range(100000, 500000):
    sqn = int(n**0.5)
    dells = []
    prostdells = []
    for dell in range(1, sqn + 1):
        if n % dell == 0:
            dell2 = n // dell
            if dell == dell2:
                dells.append(dell)
            else:
                dells.append(dell)
                dells.append(dell2)
    dellsi = []
    for i in dells:
        sqi = int(i**0.5)
        for delli in range(1, sqi + 1):
            if n % delli == 0:
                delli2 = n // delli
                if delli == delli2:
                    dells.append(delli)
                else:
                    dells.append(delli)
                    dells.append(delli2)
        if len(dellsi) == 2:
            prostdells.append(i)
    if len(prostdells) > 3:
        prostdells = sorted(prostdells)
        if (prostdells[1] - prostdells[0]) == (prostdells[2] - prostdells[1]):
            print(n, len(prostdells) * (prostdells[1] - prostdells[0]) )