n = 500000 + 1
count = 0
while count < 5:
    sqn = int(n ** 0.5)
    dell8 = []
    for dell in range(2, sqn + 1):
        if n % dell == 0:
            dell2 = n // dell
            if dell == dell2:
                if dell != 8 and dell % 10 == 8:
                    dell8.append(dell)
            else:
                if dell != 8 and dell % 10 == 8:
                    dell8.append(dell)
                if dell2 != 8 and dell2 % 10 == 8:
                    dell8.append(dell2)
    if len(dell8) > 0:
        print(n, min(dell8))
        count += 1
    n += 1