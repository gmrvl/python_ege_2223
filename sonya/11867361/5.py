for  i in range(105, 1000):
    n = bin(i)[2:]
    c = 0
    while c <= 2:
        if n.count('0') == n.count('1'):
            n = n + n[-1]
        else:
            if n.count('0') > n.count('1'):
                n = n + '1'
            if n.count('0') < n.count('1'):
                n = n + '0'
        c += 1
    n = int(n)
    if n % 4 == 0:
        print(i)
        break
