for i in range(1000000, 2000001):
    sq = int(i**0.5)
    a = []
    for dell in range(1, sq + 1):
        if i % dell == 0:
            dell2 = i // dell
            a.append(dell2 - dell)
    a = sorted(a)
    if len(a) >= 3:
        if a[2] <= 100:
            print(i)
