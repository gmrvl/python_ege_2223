for i in range(1,1000):
    n = str(bin(i)[2:])
    if i % 2 == 0:
        n += "10"
    else:
        n += "01"
    r = int(n, 2)
    if r < 109:
        print(r)
       