for n in range(1000000, 2000000):
    sqn = int(n ** 0.5)
    dells = 0
    for dell in range(1, sqn + 1):
        if n % dell == 0:
            dell2 = n // dell
            if abs(dell2 - dell) < 100:
                dells += 1
    if dells >= 3:
        print(n)
