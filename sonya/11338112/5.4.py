for i in range(1000,10000):
    n = str(i)
    a = int(n[0]) + int(n[1])
    b = int(n[1]) + int(n[2])
    c = int(n[2]) + int(n[3])
    if a < b and a < c:
        if b > c:
            n = str(c) + str(b)
        else:
            n = str(b) + str(c)
    elif b < a and b < c:
        if a > c:
            n = str(c) + str(a)
        else:
            n = str(a) + str(c)
    else:
        if a>b:
            n = str(b) + str(a)
        else:
            n = str(a) + str(b)
    if a==b and a>c:
        n = str (c) + str(a)
    elif a == c and a>b:
        n = str(b) + str(a)
    elif b == c and b>a:
        n == str(a) + str(b)
    if n == '613':
        print(i)