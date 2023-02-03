count = 0
n = 11000001
while count < 5:
    a = []
    sq = int(n ** 0.5)
    for i in range(2, sq + 1):
        if n % i == 0:
            a.append(i)
            a.append(n // i)
    if len(a) >= 2:
        m = a[0] + a[1]
    else:
        m = 0
    if 0 < m < 10000:
        print(m)
        count += 1

