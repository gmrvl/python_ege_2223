for i in range ( 100, 1001):
    n = str(i)
    s1 = int(n[0]) + int(n[1])
    s2 = int(n[1]) + int(n[2])

    w = str(max ( s1, s2))
    z = str(min( s1, s2))

    r = w + z

    if r == '159':
        print (i)
        break