from fnmatch import*
a = []
for n in range(217,10**7 + 1, 217):
    s = str(n)
    if fnmatch(s, '14?4*'):
        a.append(n)
print(a)
a = sorted(a, reverse=True)
for i in range(7):
    sqi = int((a[i])**0.5)
    dells = []
    for dell in range(1,sqi + 1):
        if a[i] % dell == 0:
            dell2 = a[i] // dell
            if dell == dell2:
                if dell % 2 != 0:
                    dells.append(dell)
            else:
                if dell2 % 2 != 0:
                    dells.append(dell2)
                if dell % 2 != 0:
                    dells.append(dell)
    print(a[i], sum(dells))
