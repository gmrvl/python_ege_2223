for i in range(110203, 110246):
    sq = i ** 0.5
    # if sq != int(sq): это используется только когда ищем квадраты
    #     continue
    sq = int(sq)
    a = []
    for dell in range(1, sq):
        if i % dell == 0:
            if dell % 2 == 0:
                a.append(dell)
            if (i // dell) % 2 == 0:
                a.append(i // dell)
        if len(a) > 4:
            break
    if len(a) == 4:
        a = sorted(a)
        print(a)
