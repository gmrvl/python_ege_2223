count = 0
for n in range(245690, 245756):
    count += 1
    sqn = int(n ** 0.5)
    dells = []
    for dell in range(2, sqn + 1):
        if n % dell == 0:
            dells.append(dell)
            dells.append(n // dell)
    if len(dells) == 0:
        print(count, n)
