for i in range(1, 256):
    n = str(bin(i)[2:])
    n = (8 - len(n)) * '0'
    if '1' in n or '0' in n:
        n = n.replace('1', '0', 1)
        n = n.replace('0', '1', 1)
        r = int(n, 2)
        if i == '178':
            print(r)
