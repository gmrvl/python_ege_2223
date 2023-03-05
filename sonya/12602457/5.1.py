for n in range(100,1000):
    n = str(n)
    a = int(n[0]) * int(n[1])
    b = int(n[1]) * int(n[2])
    if a > b:
        r = str(b) + str(a)
    else:
        r = str(a) + str(b)
    if r == '621':
        print(n)
        break