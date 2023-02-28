for n in range(125256, 125331):
    sqn = int(n**0.5)
    dellsch = []
    for dell in range(1, sqn + 1):
        if n % dell == 0:
            dell2 = n // dell
            if dell == dell2:
                if dell % 2 == 0:
                    dellsch.append(dell)
            else:
                if dell % 2 == 0:
                    dellsch.append(dell)
                if dell2 % 2 == 0:
                    dellsch.append(dell2)
    if len(dellsch) == 6:
        dellsch.sort()
        print(dellsch)