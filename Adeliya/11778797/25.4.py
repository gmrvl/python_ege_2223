for i in range(95632, 95701):
    sqn = int(i ** 0.5)
    a = []
    for dell in range(1, sqn + 1):
        if i % dell == 0:
            if dell % 2 == 0:
                a.append(dell)
            if (i // dell) % 2 == 0 and (i // dell) != dell:
                a.append(i // dell)
        if len(a) > 6:
            break
    if len(a) == 6:
        a=sorted(a)
        print(a)