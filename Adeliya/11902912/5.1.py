for i in range(1, 10000):
    s = bin(i)[2:]
    s = str(s)
    s = s[:-1]
    if i % 2 != 0:
        s += "10"
    else:
        s += "01"
    r = int(s, 2)
    if r == 2018:
        print(i)

