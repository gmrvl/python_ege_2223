for i in range(105, 1000):
    n = bin(i)[2:]
    for k in range(3):
        count0 = n.count('0')
        count1 = n.count('1')
        if count0 == count1:
            n += n[-1]
        else:
            if count0 > count1:
                n += '1'
            else:
                n += '0'
    r = int(n, 2)
    if r % 4 == 0:
        print(i)
        break