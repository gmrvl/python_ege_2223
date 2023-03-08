count = 0
for n in range(2422000, 2422081):
    count += 1
    sqn = int(n**0.5)
    dells = 0
    for dell in range(2, sqn + 1):
        if n % dell == 0:
            dell2 = n // dell
            if dell == dell2:
                dells += 1
            else:
                dells += 2
    if dells == 0:
        print(count, n)