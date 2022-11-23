count = 0
i = 500000
while count < 5:
    mindell = i
    dels = []
    for dell in range(1, int(i ** 0.5) + 1):
        if i % dell == 0:
            dels.append(dell)
            dels.append(i // dell)
    for d in dels:
        if d % 10 == 8 and d != 8:
            if mindell > d:
                mindell = d
    if mindell < i:
        print(i, mindell)
        count += 1
    i += 1