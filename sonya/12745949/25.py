n = 500000 + 1
count = 0
while count < 5:
    sqn = int(n**0.5)
    dells = []
    for dell in range(2, sqn + 1):
        if n % dell == 0:
            dell2 = n // dell
            if dell % 10 == 8 and dell != 8:
                dells.append(dell)
            if dell2 % 10 == 8 and dell2 != 8:
                dells.append(dell2)
    if len(dells) > 0:
        print(n, min(dells))
        count += 1
    n += 1