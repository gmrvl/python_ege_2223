for n in range(200,1, - 1):
    a = 4 * n + 16
    b = 4 * n - 32
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    if a == 24:
        print(n)
        break