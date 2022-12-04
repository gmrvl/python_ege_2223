for i in range(2, 100000):
    n = bin(i)[2:]
    n = n[:-1]
    if i % 2 != 0:
        n = n + '10'
    else:
        n = n + '01'
    n = int(n, 2)
    if n == 2018:
        print(i)