for i in range(128, 256):
    t = i
    n = bin(i)[2:]
    n = n.replace('0', 'a')
    n = n.replace('1', '0')
    n = n.replace('a', '1')
    n = int(n,2)
    n = t - n
    if n == 105:
        print(i)