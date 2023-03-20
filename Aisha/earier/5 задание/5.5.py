for i in range (1000, 10001):
    n = str(i)
    s1 = int(n[0]) + int(n[1])
    s2 = int(n[1]) + int(n[2])
    s3 = int(n[2]) + int(n[3])

    w = str(s1+s2+s3 - max (s1, s2, s3) - min ( s1, s2, s3))
    q = str (max( s1, s2, s3))

    r = w + q
    if r == '1517':
        print (i)