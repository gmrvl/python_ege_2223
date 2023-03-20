for i in range(100, 1000):
    n = str(i)
    mult1 = int(n[0]) * int(n[1])
    mult2 = int(n[1]) * int(n[2])
    if mult1 > mult2:
        s = str(mult2) + str(mult1)
    else:
        s = str(mult1) + str(mult2)

    if s == '621':
        print(i)
