for i in range(100, 1000):
    i = str(i)
    n1 = int(i[0]) + int(i[1])
    n2 = int(i[1]) + int(i[2])
    if n1 < n2:
        res = str(n2) + str(n1)
    else:
        res = str(n1) + str(n2)
    if res == '1711':
        print(i)
        break