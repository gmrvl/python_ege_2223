for i in range(1,101):
    n =str(bin(i)[2:])
    if i % 2 == 0:
        n += "00"
    else:
        n += "11"
    r = int(n, 2)
    if r < 134:
        print(i)
