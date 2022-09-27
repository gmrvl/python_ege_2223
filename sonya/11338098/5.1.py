for i in range(1,1001):
    n = bin(i)[2:]
    n = int(n)
    if n % 2 == 0:
        n = '1' + str(n) + '0'
    else:
        n = '11' + str(n) + "11"
    r = int(n,2)
    if r > 52:
        print(i)
        break