for n in range(174457, 174506):
    sqn = n ** 0.5
    dells = []
    if sqn == int(sqn):
        continue
    sqn = int(sqn)
    for dell in range(2,sqn + 1):
        if n % dell == 0:
            dells.append(dell)
            dells.append(n // dell)
        if len(dells) > 2:
            break
    if len(dells) == 2:
        print(dells)