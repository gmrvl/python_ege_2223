for i in range(1000, 10000):
    n1 = i // 1000
    n2 = i // 100 % 10
    n3 = i // 10 % 10
    n4 = i % 10
    s1 = n1 + n2
    s2 = n2 + n3
    s3 = n3 + n4
    a = [s1, s2, s3]
    a = sorted(a)
    res = str(a[1]) + str(a[2])
    if res == '1315':
        print(i)
