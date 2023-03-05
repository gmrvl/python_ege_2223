count = 0
for n in range(245690, 245757):
    count += 1
    sqn = int(n ** 0.5)
    dells = []
    for dell in range(1, sqn + 1):
        if n % dell == 0:
            dell2 = n // dell
            if dell == dell2:
                dells.append(dell)
            else:
                dells.append(dell)
                dells.append(dell2)
    if len(dells) == 2:
        print(count, n)