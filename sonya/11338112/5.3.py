

for i in range(2,1000):
    n = bin(i)[2:]
    summ = n.count('1')
    if summ % 2 == 0:
        n += '00'
    else:
        n += '10'
    r = int(n,2)
    if r > 83:
        print(r)

