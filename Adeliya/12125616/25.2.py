for i in range(312614, 312652):
    sq = i ** 0.5
    sq = int(sq)
    a = []
    for dell in range(1, sq + 1):
        if i % dell == 0:
            dell2 = i // dell
            a.append(dell)
            a.append(dell2)
            if len(a) > 6:
                break
    if len(a) == 6:
        a = sorted(a)
        print(a)
