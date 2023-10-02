maxx = 0
for n in range(568023, 569231):
    sqn = int(n ** 0.5)
    dells = 0
    for dell in range(1, sqn + 1):
        if n % dell == 0:
            dell2 = n // dell
            if dell == dell2:
                dells += 1
            else:
                dells += 2
    maxx = max(dells, maxx)
for n in range(568023, 569231):
    sqn = int(n ** 0.5)
    dells = []
    for dell in range(1, sqn + 1):
        if n % dell == 0:
            dell2 = n // dell
            if dell == dell2:
                dells.append(dell)
            else:
                dells.append(dell2)
                dells.append(dell)
    if len(dells) == maxx:
        print(len(dells), n)