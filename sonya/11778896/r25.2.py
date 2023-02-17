for n in range(110203, 110245):
    sqn = int(n ** 0.5)
    dells = []
    for dell in range(1, sqn + 1):
        if n % dell == 0:
            dell2 = n //dell
            if dell == dell2:
                if dell % 2 == 0:
                    dells.append(dell)
            else:
                if dell % 2 == 0:
                    dells.append(dell)
                if dell2 % 2 == 0:
                    dells.append(dell2)
    if len(dells) == 4:
        dells.sort()
        print(dells)
