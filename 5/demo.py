for i in range(1, 10001):
    n = bin(i)[2:]  #101010111
    summ = n.count('1')
    if summ % 2 == 0:
        n += '0'
        n = '10' + n[2:]
    else:
        n += '1'
        n = '11' + n[2:]

    r = int(n, 2)
    if r > 40:
        print(i)
        break
