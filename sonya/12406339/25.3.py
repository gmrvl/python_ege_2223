for n in range(35000000, 40000000):
    sqn = int(n ** 0.5)
    ndells = []
    for dell in range(1, sqn + 1):
        if n % dell == 0:
            dell2 = n // dell
            if dell == dell2:
                if dell % 2 != 0:
                    ndells.append(dell)
            else:
                if dell % 2 != 0:
                    ndells.append(dell)
                if dell2 % 2 != 0:
                    ndells.append(dell2)
            if len(ndells) > 5:
                break
    if len(ndells) == 5:
        print(n)

