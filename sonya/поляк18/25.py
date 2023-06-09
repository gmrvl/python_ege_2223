from fnmatch import*
count = 0
ns = []
n = 336
while count < 7:
        if fnmatch(str(n), '?6*6*?6'):
            if n % 6 == 0 and n % 7 == 0 and n % 8 == 0:
                print(n)
                ns.append(n)
                count += 1
        n += 1

for n in ns:
    sqn = int(n**0.5)
    dells = []
    for dell in range(1, sqn + 1):
        if n % dell == 0:
            dell2 = n // dell
            if dell == dell2:
                dells.append(dell)
            else:
                dells.append(dell)
                dells.append(dell2)
    print(n, sum(dells))