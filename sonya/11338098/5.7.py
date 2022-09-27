for i in range(128, 256):
    n = bin(i)[2:]
    n = n.replace('0', 'a')
    n = n.replace('1', '0')
    n = n.replace('a', '1')
