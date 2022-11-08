for i in range(0,1000):
    n = bin(i)[2:]
    s = n.count('1')
    if s % 2 == 0:
        n = n + '00'
    else:
        n = n + '10'
    n = int(n,2)
    if n < 100:
        print(n)