for i in range(100, 1001):
    n = bin(i)[2:]
    zero = n.count('0')
    ones = n.count('1')
    for j in range(3):
        if zero == ones:
            last = n[-1]
            n += last
            if last == '1':
                ones += 1
            else:
                zero += 1
        elif zero > ones:
            n += '1'
            ones += 1
        else:
            n += '0'
            zero += 1
    r = int(n, 2)
    if r % 4 == 0:
        print(i)
        break
