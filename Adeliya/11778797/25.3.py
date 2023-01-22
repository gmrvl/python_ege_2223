for i in range(289123456, 389123457):
    sq=i**0.5
    if sq != int(sq):
        continue
    sq = int(sq)
    a = [sq]
    for dell in range(2, sq):
        if i % dell == 0:
            a.append(dell)
            a.append(i // dell)
    if len(a) == 3:
        print(i, max(a))