for i in range(1000,10000):
    n = str(i)
    a = int(n[0]) + int(n[1])
    b = int(n[1]) + int(n[2])
    c = int(n[2]) + int(n[3])
    if a > b and b > c:
        n = str(b) + str(a)
    elif a > c and c > b:
        n = str(c) + str(a)
    elif b > a and a > c:
        n = str(a) + str(b)
    elif b > c and c > a:
        n = str(c) + str(b)
    elif c > b and b > a:
        n = str(b) + str(c)
    elif c > a and a > b:
        n = str(c) + str(a)
    if n == '1517':
        print(i)

