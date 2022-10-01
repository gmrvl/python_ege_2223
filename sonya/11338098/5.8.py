for i in range(0,256):
    n = bin(i)[2:]
    if len(n) < 8:
        a = len(n)
        n = '0'*(8-a) + str(n)
    n = n.replace('0','t')
    n = n.replace('1', '0')
    n = n.replace('t', '1')
    n = int(n,2)
    t = n - i
    if t == 111:
        print(i)