for n in range(1000000,2000001):
    sqn = int(n ** 0.5)
    raz = []
    for dell in range(2,sqn+ 1):
        if n % dell == 0:
            dell2 = n // dell
            if abs(dell2 - dell) <= 100:
                raz.append(abs(dell2 - dell))
    if len(raz) >= 3:
        print(n)


