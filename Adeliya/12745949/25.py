count = 0
n = 500000
while count < 5:
    n += 1
    for dell in range(1, n):
        if n % dell == 0:
            if dell % 10 == 8 and dell != 8:
                count += 1
                print(n, dell)
                break