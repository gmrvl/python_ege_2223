for n in range(101000000, 102000001):
    sqn = int(n ** 0.5)
    chdells = 0
    for dell in range(1, sqn + 1):
        if n % dell == 0:
            dell2 = n // dell
            if dell == dell2:
                if dell % 2 == 0:
                    chdells += 1
            else:
                if dell % 2 == 0:
                    chdells += 1
                if dell2 % 2 == 0:
                    chdells += 1
            if chdells > 3:
                break
    if chdells == 3:
        print(n)