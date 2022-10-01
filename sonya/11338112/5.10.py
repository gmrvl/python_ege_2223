

for i in range(100,1000):
    n = bin(i)[2:]
    a = n.count('1')
    b = n.count('0')
    for t in range(3):
        if a == b:
            n = n + n[-1]
        elif a > b:
            n = n + '0'
        else:
            n = n + '1'
    r = int(n,2)
    if r % 4 == 0:
        print(i)