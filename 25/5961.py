for i in range(12, 10**7, 12):
    stri = str(i)
    if stri[0:2] == '12' and stri[-3:] == '348':
        dells = []
        stop = int(i**0.5)
        for d in range(2, stop + 1):
            if i % d == 0:
                dells.append(d)
                dells.append(i // d)
        if len(dells) == 10:
            print(i, max(dells))
