for i in range(174457, 174506):
    sq = i ** 0.5
    a = []
    if sq == int(sq):
        continue
    sq = int(sq)
    for dell in range(2, sq + 1):
        if i % dell == 0:
            a.append(dell)
            a.append(i // dell)
        if len(a) > 2:
            break
    if len(a) == 2:
        print(a)