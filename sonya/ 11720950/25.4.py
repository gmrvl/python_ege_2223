a = []
d = []
for i in range(500000, 500100):
    for dell in range(9, int(i ** 0.5)):
        if i % dell == 0:
            if dell % 10 == 8 and dell != i:
                a.append(i)
                d.append(dell)
                break
print(a, d)