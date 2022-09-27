for i in range(0, 100):
    n = bin(i)[2:]
    reverse_n = ''
    for k in n:
        reverse_n = k + reverse_n
    r = int(reverse_n, 2)
    if r == 11:
        print(i)
