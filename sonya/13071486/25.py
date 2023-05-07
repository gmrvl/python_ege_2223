for n in range(95632, 95651):
    sqn = int(n **0.5)
    dells = []
    for dell in range(1,sqn+ 1):
        if n % dell == 0:
            dell2 = n // dell
            if dell == dell2:
                if dell % 2 == 1:
                    dells.append(dell)
            else:
                if dell % 2 == 1:
                    dells.append(dell)
                if dell2 % 2 == 1:
                    dells.append(dell2)
    if len(dells) == 6:
        print(sorted(dells))
