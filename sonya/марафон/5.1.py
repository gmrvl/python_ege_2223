for i in range(0,1000):
    n = bin(i)[2:]
    a = n.count('1')
    b = n.count('0')
    if a > b:
        n = n + '1'
    else:
        n = n + '0'
    n = int(n,2)
    if n > 100:
        print(n)
        break