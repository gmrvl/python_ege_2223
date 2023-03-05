n = 452021 + 1
count = 0
while count < 5:
    sqn = int(n**0.5)
    dells = []
    for dell in range(2, sqn+ 1):
        if n % dell == 0:
            dell2 = n // dell
            if dell == dell2:
                dells.append(dell)
            else:
                dells.append(dell)
                dells.append(dell2)
    if len(dells) > 2:
        M = max(dells) + min(dells)
        if M%7 == 3:
            print(n, M)
            count += 1
    n += 1