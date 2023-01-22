maxdells = 0
for n in range(84052, 84131):
    sqn = int(n**0.5)
    dells = 0
    for dell in range(1, sqn + 1):
        if n % dell ==0:
            dell2 = n // dell
            if dell == dell2:
                dells += 1
            else:
                dells += 2
    maxdells = max(maxdells,dells)
print(maxdells)

for n in range(84052, 84131):
    sqn = int(n**0.5)
    dells = 0
    for dell in range(1, sqn + 1):
        if n % dell ==0:
            dell2 = n // dell
            if dell == dell2:
                dells += 1
            else:
                dells += 2
    if dells == 72:
        print(n)