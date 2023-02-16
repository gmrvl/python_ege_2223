for i in range(95632, 95651):
    stop = int(i ** 0.5)
    dells = []
    for dell in range(1, stop + 1):
        if i % dell == 0:
            dell2 = i // dell
            if dell % 2 == 1:
                dells.append(dell)
            if dell2 % 2 == 1 and dell != dell2:
                dells.append(dell2)
        if len(dells) > 6:
            break
    if len(dells) == 6:
        dells = sorted(dells)
        print(dells)

