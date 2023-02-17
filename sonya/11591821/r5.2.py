for n in range(100,1000):
    r = str(n)
    a = int(r[0]) + int(r[1])
    b = int(r[1]) + int(r[2])
    if a > b:
        r = str(b) + str(a)
    else:
        r = str(a) + str(b)
    if r == '812':
        print(n)
        break