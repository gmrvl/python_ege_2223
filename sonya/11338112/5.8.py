for i in range(100,1000):
    n = str(i)
    a = int(n[0]) + int(n[1])
    l = int(n[1]) + int(n[2])
    if a > l:
        n = str(a) + str(l)
    elif l > a:
        n = str(l) + str(a)
    if n == '159':
        print(i)