for i in range(101000000, 102000001):
    sq = i ** 0.5
    sq = int(sq)
    a = []
    for dell in range(1, sq+1):
        if i % dell == 0:
            if dell % 2 == 0:
                a.append(dell)
            if (i // dell) % 2 == 0:
                a.append(i // dell)
        if len(a) > 3:
            break
    if len(a) == 3:
        a = sorted(a)
        print(i)
