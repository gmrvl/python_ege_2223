for i in range(0,1000):
    n = bin(i)[2:]
    summ = n.count('1')
    if summ % 2 == 0:
        n = n + '00'
    else:
        n = n + '10'
    r = int(n,2)
    if r>85:
        print(i)
        break