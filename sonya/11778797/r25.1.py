n = 600000 + 1
count = 0

while count < 5:
    dells7 = []
    sqn = int(n ** 0.5)
    for dell in range(2, sqn + 1):
        if n % dell == 0:
            dell2 = n // dell
            if dell % 10 == 7 and dell != 7:
                dells7.append(dell)
            if dell2 % 10 == 7 and dell2 != 7:
                dells7.append(dell2)
    if len(dells7) != 0:
        print(n, min(dells7))
        count += 1
    n += 1

