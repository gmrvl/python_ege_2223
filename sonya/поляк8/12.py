n = 360
dells = []
for dell in range(1,360):
    if n % dell == 0:
        if dell <= 30:
            dells.append(dell)
print(len(dells) - 2)
