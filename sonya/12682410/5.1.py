for n in range(1000,10000):
    n = str(n)
    a = int(n[0]) + int(n[1])
    b = int(n[1]) + int(n[2])
    c = int(n[2]) + int(n[3])
    r = str(a + b + c - min(a,b,c) - max(a,b,c)) + str(max(a,b,c))
    if r == '613':
        print(n)