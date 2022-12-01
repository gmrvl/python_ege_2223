for i in range(2, 10001):
    n = bin(i)[2:]
    s1 = int(n.count('1'))
    if s1 % 2 == 1:
        n += '10'
    else:
        n += '00'
    r = int(n, 2)
    if r > 83:
        print(r)
        break
        