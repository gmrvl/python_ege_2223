def Dell(n, m):
    if n % m == 0:
        return True
    else:
        return False


def F(x, A):
    return (Dell(A, 40)) and (Dell(780, x)) <= ((not(Dell(A, x))) <= (not(Dell(180, x))))


for A in range(1, 1000):
    OK = True
    for x in range(1, 1000):
        if not F(x, A):
            OK = False
            break
    if OK:
        print(A)
        break
