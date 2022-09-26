for i in range(1,1001):
    n=bin(i)[2:]
    summ= n.count('1')
    if summ % 2 == 1:
        n += '10'
    else:
        n += '00'
    r = int(n, 2)
    if r > 125:
        print(r)
        break