n = 1000000 + 1
count = 0
while count < 6:
    sqn = int(n**0.5)
    dells = []
    for dell in range(1,sqn + 1):
        if n % dell == 0:
            dell2 = n // dell
            if dell == dell2:
                dells.append(dell)
            else:
                dells.append(dell)
                dells.append(dell2)
    if len(dells) > 40:
        summ = 0
        proizved = 0
        for i in range(0, len(dells)):
            summ += dells[i]
            proizved *= dells[i]
        if summ % 2 != 0 and proizved % 2 != 0:
            print(n, len(dells))
            count += 1
    n += 1