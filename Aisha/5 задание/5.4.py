for i in range (1000, 10001):
    n = str(i)
    s1 = int(n[0]) + int(n[1])
    s2 = int(n[1]) + int(n[2])
    s3 = int(n[2]) + int(n[3])


    z = str(max(s1, s2, s3))
    w = str(min(s1, s2, s3))

    res = w + z
    if res == '613':
        print(i)
