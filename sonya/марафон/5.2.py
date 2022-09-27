for i in range(100,1000):
    n = str(i)
    a = int(n[0]) + int(n[1])
    b = int(n[1]) + int(n[2])
    if a > b:
        n = str(a) + str(b)
    else:
        n = str(b) + str(a)
    if n == '159':
        print(i)
