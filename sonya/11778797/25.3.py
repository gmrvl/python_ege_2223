for s in range(289123456, 389123457):
    sqn = s ** 0.5
    if sqn != int(sqn):
        continue
    sqn = int(sqn)
    dels = [sqn]
    for dell in range(2, sqn):
        if s % dell == 0:
            dels.append(dell)
            dels.append(s // dell)
    if len(dels) == 3:
        print(s, max(dels))