n =200000000
count = 0
while count < 5:
    sqn = int(n**0.5)
    k = 0
    s = 0
    m = 1
    for dell in range(sqn+1, 1, -1):
        if n % dell == 0:
            s += dell
            m *= dell
            k += 1
            if k == 5:
                if m < n and s % 2 == 0:
                    print(s,m)
                    count += 1
                break
    n -= 1
