for i in range(289123456, 389123456):
    sq = i**0.5
    if sq == int(sq):
        deliteli = [int(sq)]
        for dell in range(2, int(sq)):
            if i % dell == 0:
                deliteli.append(dell)
                deliteli.append(i // dell)
        if len(deliteli) == 3:
            deliteli = sorted(deliteli)
            print(i, deliteli[-1])



