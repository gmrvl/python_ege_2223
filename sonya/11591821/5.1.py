for i in range(0, 256):
    n = bin(i)[2:]
    if len(n) < 8:
        n = '0'*(8 - len(n)) + n
    n = n.replace('0', 'a')
    n = n.replace('1', '0')
    n = n.replace('a', '1')
    s = int(n, 2)
    if (s - i) == 111:
        print(i)
