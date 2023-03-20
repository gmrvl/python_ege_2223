for i in range(128, 256):
    s = bin(i)[2:]
    s = str(s)
    s = s.replace('1', '2')
    s = s.replace('0', '1')
    s = s.replace('2', '0')
    z = int(s, 2)
    if i - z == 105:
        print(i)