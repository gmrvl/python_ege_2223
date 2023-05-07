maxdells = 0
maxn = 0
for n in range(120115,  120201):
    sqn = int(n**0.5)
    dells = 0
    for dell in range(1, sqn + 1):
        if n % dell == 0:
            dell2 = n // dell
            if dell == dell2:
                dells += 1
            else:
                dells += 2
    if dells > maxdells:
        maxdells = dells
        maxn = n
    if dells == maxdells:
        maxn = max(maxn, n)
print(maxdells, maxn)