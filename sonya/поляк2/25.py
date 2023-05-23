from fnmatch import*
a = []
for n in range(1, 10**7):
    if fnmatch(str(n), '3*52?'):
        if n ** 0.5 == int(n ** 0.5):
            a.append(n)
print(a)
for i in a:
    sqi = int(i ** 0.5)
    dells = []
    for dell in range(2, sqi + 1):
        if i % dell == 0:
            dell2 = i // dell
            if dell2 == dell:
                dells.append(dell)
            else:
                dells.append(dell)
                dells.append(dell2)
    if len(dells) % 2 == 1:
        print(i, max(dells))


