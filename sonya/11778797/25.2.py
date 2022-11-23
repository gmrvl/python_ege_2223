for n in range(123456789, 223456790):
    sqn = n ** 0.5
    dels = []
    for d in range(2, sqn + 1):
        if n % d == 0:
            if d == (n // d):
                dels.append(d)
            else:
                dels.append(d)
                dels.append(n // d)
            if len(dels) > 3:
                break
    if len(dels) == 3:
        print(n, max(dels))

for n in range(123456789, 223456790):
    sqn = n ** 0.5
    if round(sqn) == sqn:
        sqn = int(sqn)
        pardell = []
        for d in range(2,sqn + 1):
            if n % d == 0:
                pardell.append(d)
                pardell.append(n // d)
            if lenpardell > 2:
                break
            if len()



