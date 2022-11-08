for i in range(0,1000):
    n = bin(i)[2:]
    s = n.count('1')
    if s % 2 == 0:
        n = n + '00'
    elif s % 2 != 0:
        n = n + '10'
    r = int(n,2)
    if r > 43:
        print(r)