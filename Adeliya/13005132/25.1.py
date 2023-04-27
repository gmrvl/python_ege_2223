for i in range(289123456, 389123456):
    sq = i**0.5
    if sq == int(sq):
        dells = [int(sq)]
        for dell in range(2, int(sq)):
            if i % dell == 0:
                dells.append(dell)
                dells.append(i // dell)
        if len(dells) == 3:
            dells = sorted(dells)
            print(i, dells[-1])
