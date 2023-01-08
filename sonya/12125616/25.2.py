for n in range(312614, 312652):
    dells = [1, n]
    sqn = int(n ** 0.5)
    for dell in range(2, sqn + 1):
        if n % dell == 0:
            dell2 = n // dell
            if dell == dell2:
                dells.append(dell)
            else:
                dells.append(dell)
                dells.append(dell2)
        if len(dells) > 6:
            break
    if len(dells) == 6:
        dells.sort()
        print(dells)



