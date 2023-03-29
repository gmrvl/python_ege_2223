for n in range(100, 1000):
    n = str(n)
    a = int(n[0]) + int(n[1])
    b = int(n[1]) + int(n[2])
    r = str(max(a,b)) + str(min(a,b))
    if r == '1412':
        print(n)
        break