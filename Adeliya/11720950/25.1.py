for i in range(174457, 174506):
    sq = int(i ** 0.5)
    count = 0
    a = []
    for dell in range(2, sq):
        if i % dell == 0:
            count += 1
            a.append(dell)
            a.append(i//dell)
        if count > 1:
            break
    if count == 1:
        a = sorted(a)
        print(a)
