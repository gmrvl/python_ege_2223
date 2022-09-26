for i in range (1, 11000):
    n = bin(i)[2:]
    summ = n.count('1')
    if summ % 2 == 0