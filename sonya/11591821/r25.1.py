for n in range(95632, 95701):
    sqn = int(n**0.5)
    chdells = []
    for dell in range(1, sqn + 1):
        if n % dell == 0:
            dell2 = n // dell
            if dell == dell2:
                if dell % 2 == 0:
                    chdells.append(dell)
            else:
                if dell % 2 == 0:
                    chdells.append(dell)
                if dell2 % 2 == 0:
                    chdells.append(dell2)
    if len(chdells) == 6:
        chdells.sort()
        print(chdells)