maxx = 0
for i in range(120115, 120201):
    numdell = 0
    for dell in range(1, i + 1):
        if i % dell == 0:
            numdell += 1
    if numdell >= maxx:
        maxx = numdell
        maxxnum = i
print(maxx, maxxnum)