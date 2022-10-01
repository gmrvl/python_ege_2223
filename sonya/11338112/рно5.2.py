for i in range(1,10000):
    n = bin(i)[2:]
    n = n[:-1]
    if i % 2 == 0:
        n += '01'
    else:
        n += '10'
    n = int(n,2)
    if n == 2018:
        print(i)