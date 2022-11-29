for n in range(123456789, 223456790):
    sqn = n ** 0.5
    if sqn != int(sqn):
        continue
    sqn = int(sqn)
    dels = [sqn]
    for d in range(2, sqn):
        if n % d == 0:
            dels.append(d)
            dels.append(n // d)
            if len(dels) > 3:
                break
    if len(dels) == 3:
        print(n, max(dels))






