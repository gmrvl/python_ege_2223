for i in range(1, 100000):

    n_b = bin(i)[2:]
    summ = n_b.count('1')
    if summ % 2 == 0:
        n_b += '00'
    else:
        n_b += '10'
    r = int(n_b, 2)

    if r > 97:
        print(i)
        break
