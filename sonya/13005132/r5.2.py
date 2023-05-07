for n in range(10000, 100000):
    n = str(n)
    a = int(n[0]) + int(n[2]) + int(n[4])
    b = int(n[1]) + int(n[3])
    r = str(min(a,b)) + str(max(a,b))
    if r == '621':
        print(n)