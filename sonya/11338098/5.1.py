for i in range(1,1001):
    n = bin (i)[2:]
    summ = n.count('1')
    if summ % 2 == 0:
        n = '1' + n + '0'
    else:
        n = '11' + n + "11"
    r = int(n,2)
    if r>52:
        print(i)
        break