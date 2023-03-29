for i in range(10000, 100000):
    n = str(i)
    s1 = int(n[0]) + int(n[2]) + int(n[4])
    s2 = int(n[1]) + int(n[3])

    if s1 > s2:
        res = str(s2) + str(s1)
    else:
        res = str(s1) + str(s2)
    if res == '723':
        print(i)
        break
