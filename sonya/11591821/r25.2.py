n = 700000 + 1
count = 0
while count < 5:
    sqn = int(n ** 0.5)
    dells = []
    for dell in range(2,sqn+ 1):
        if n % dell == 0:
            dells.append(dell)
            dells.append(n//dell)
    if len(dells) > 0:
        M = min(dells) + max(dells)
        if M % 10 == 8:
            print(n,M)
            count += 1
    n += 1

