maxlen = 0

for n in range(120115, 120201):
    sqn = int(n ** 0.5)
    dells = []
    lens = 0
    for dell in range(1, sqn + 1):
        if n % dell == 0:
            dell2 = n // dell
            if dell == dell2:
                dells.append(dell)
            else:
                dells.append(dell)
                dells.append(dell2)
    lens = len(dells)
    if maxlen < lens:
        maxlen = lens
    if lens == 128:
        print(n)
print(maxlen)


