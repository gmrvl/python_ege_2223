for n in range(123456789, 223456790):
    sqn = n ** 0.5
    if sqn != int(sqn):
        continue
    sqn = int(sqn)
    dells = [sqn]
    for dell in range(2, sqn):
        if n % dell == 0:
            dell2 = n // dell
            dells.append(dell)
            dells.append(dell2)
        if len(dells) > 3:
            break
    if len(dells) == 3:
        print(n, max(dells))