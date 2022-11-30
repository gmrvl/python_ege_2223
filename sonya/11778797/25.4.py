for n in range(95632, 95701):
    sqn = int(n ** 0.5)
    dels = []
    for d in range(1, sqn + 1):
        if n % d == 0:
            if d % 2 == 0:
                dels.append(d)
            if (n // d) % 2 == 0 and (n//d) != d:
                dels.append(n // d)
        if len(dels) > 6:
            break
    if len(dels) == 6:
        dels.sort()
        print(dels[0], dels[1], dels[2], dels[3], dels[4], dels[5])