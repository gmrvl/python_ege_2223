for i in range(1000,10000):
    n = str(i)
    a = int(n[0]) + int(n[1])
    b = int(n[1]) + int(n[2])
    c = int(n[2]) + int(n[3])
    f = str(a + b + c - max(a,b,c)-min(a,b,c))
    s = str(max(a,b,c))
    n = f + s
    if n == '1517':
        print(i)

