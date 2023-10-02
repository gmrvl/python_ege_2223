for n in range(2000000, 3000001):
    sqn = int(n ** 0.5)
    raz = []
    for dell in range(1, sqn + 1):
        if n % dell == 0:
            dell2 = n // dell
            ra = abs(dell - dell2)
            if ra <= 115:
                raz.append(ra)
            if len(raz) == 3:
                break
    if len(raz) >= 3:
        print(n)