for n in range(289123456, 389123457):
    sqn = n ** 0.5
    if sqn != int(sqn):
        continue
    sqn = int(sqn)
    dels = [sqn]
    for dell in range(2, sqn):
        if n % dell == 0:
            dell2 = n // dell
            dels.append(dell)
            dels.append(dell2)
            if len(dels) > 3:
                break
    if len(dels) == 3:
        print(n, max(dels))