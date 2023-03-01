for i in range(125256, 125331):
    sq = int(i**0.5)
    dells = []
    for dell in range(1, sq + 1):
        if i % dell == 0:
            dell2 = i // dell
            if dell == dell2:
                if dell % 2 == 0:
                    dells.append(dell)
            else:
                if dell % 2 == 0:
                    dells.append(dell)
                if dell2 % 2 == 0:
                    dells.append(dell2)
    if len(dells) == 6:
        a=sorted(dells)
        print(a)