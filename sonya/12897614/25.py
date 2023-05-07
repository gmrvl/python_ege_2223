n = 200000000 + 1
count = 0
while count < 5:
    sqn = int(n**0.5)
    dells = []
    for dell in range(2, sqn + 1):
        if n % dell == 0:
            dell2 = n // dell
            if dell2 == dell:
                dells.append(dell)
            else:
                dells.append(dell)
                dells.append(dell2)
    if len(dells) >= 5:
        dells = sorted(dells)
        m = dells[0] * dells[1] * dells[2] * dells[3] * dells[4]
        if 0 < m < n:
            count += 1
            print(m)
    n += 1
