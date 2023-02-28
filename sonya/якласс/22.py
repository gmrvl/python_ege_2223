for n in range(200,1, - 1):
    a = 6* n + 42
    b = 6 * n - 63
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    if a == 21:
        print(n)
        break