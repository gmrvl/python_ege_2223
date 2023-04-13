from fnmatch import*
count = 0

for i in range(10 ** 7 + 1, 1, - 1):
    s = str(i)
    if fnmatch(s, '9?*55*7'):
        s = int(s)
        count += 1
        sqn = int(s ** 0.5)
        dells = []
        for dell in range(1,sqn + 1):
            if s % dell == 0:
                dell2 = s // dell
                if dell == dell2:
                    dells.append(dell)
                else:
                    dells.append(dell)
                    dells.append(dell2)
        print(s, sum(dells) % 21)
        if count == 5:
            break