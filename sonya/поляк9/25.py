count = 0
while count < 5:
    for k in range(0, 1000):
        n = 19500000 + k
        sqn = n ** 0.5
        dells = []
        if sqn == int(sqn):
            dells.append(sqn)
        sqn = int(sqn)
        for dell in range(2, sqn):
            if n % dell == 0:
                dell2 = n // dell
                if dell2 == dell:
                    dells.append(dell)
                else:
                    dells.append(dell)
                    dells.append(dell2)
        if len(dells) <= 3:
            print(k, max(dells))
            count += 1
