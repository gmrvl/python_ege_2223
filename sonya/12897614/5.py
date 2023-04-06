for n in range(1000, 10000):
    n = str(n)
    a = int(n[0]) + int(n[1])
    b = int(n[2]) + int(n[3])
    r = str(min(a, b)) + str(max(a, b))
    if r == '117':
        print(n)


