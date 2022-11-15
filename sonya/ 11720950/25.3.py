a = []
for i in range(1000000, 2000001):
    sq = int(i ** 0.5)
    k = []
    for dell in range(1, sq):
        if i % dell == 0:
            dell1 = i // dell
            dell2 = i // dell1
            raz = abs(dell1 - dell2)
            if raz <= 100:
                k.append(raz)
    if len(k) >= 3:
        a.append(i)
print(a)