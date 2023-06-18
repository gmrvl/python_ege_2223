n = 600000 + 1
count = 0
while count < 5:
    sqn = int(n ** 0.5)
    dells = []
    for dell in range(2, sqn + 1):
        if n % dell == 0:
            dell2 = n // dell
            if dell == dell2:
                if dell % 10 == 7 and dell != 7:
                    dells.append(dell)
            else:
                if dell % 10 == 7 and dell != 7:
                    dells.append(dell)
                if dell2 % 10 == 7 and dell2 != 7:
                    dells.append(dell2)
    if len(dells) > 0:
        count += 1
        print(n, min(dells))
    n += 1