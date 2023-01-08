for i in range(312614, 312652):
    sq = i ** 0.5
    if sq != int(sq):
        continue
    sq = int(sq)
    a = [sq]
    for dell in range(2, sq):
        if i % dell == 0:
            dell2 = i // dell
            a.append(dell)
            a.append(dell2)
            if len(a) > 6:
                break
    if len(a) == 6:
        print(i, max(a))
