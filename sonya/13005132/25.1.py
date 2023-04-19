for n in range(289123456,389123456):
    sqn = n**0.5
    if sqn != int(sqn):
        continue
    sqn = int(sqn)
    dells = [sqn]
    for dell in range(2, sqn):
        if n % dell == 0:
            dells.append(dell)
            dells.append(n // dell)
            if len(dells) > 3:
                break
    if len(dells) == 3:
        print(n, max(dells))