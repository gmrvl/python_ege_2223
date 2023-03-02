n = 300000000
count = 0
while count < 5:
    sqn = int(n**0.5)
    dells = 0
    m = 0
    for dell in range(2, sqn + 1):
        if n % dell == 0:
            dells += 1
            m += dell
            if dells == 7:
                if m % 2 == 1:
                    count += 1
                    print(m)
    n += 1
