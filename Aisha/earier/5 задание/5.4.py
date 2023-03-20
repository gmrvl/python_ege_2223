for i in range(1000, 10000):
    n = str(i)
    s1 = int(n[0]) + int(n[1])
    s2 = int(n[1]) + int(n[2])
    s3 = int(n[2]) + int(n[3])

    z = max(s1, s2, s3)
    w = min(s1, s2, s3)
    s = s1 + s2 + s3 - z - w

    res = str(s) + str(z)
    if res == '613':
        print(i)
