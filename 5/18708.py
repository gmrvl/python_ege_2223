for i in range(1, 10001):
    n = bin(i)[2:]
    summ = n.count('1')
    # n += str(summ % 2) другое решение, тоже правильное
    # summ = n.count('1')
    # n += str(summ % 2)
    if summ % 2 == 1:
        n += '10'
    else:
        n += '00'
    r = int(n, 2)
    if r > 85:
        print(i)
        break
