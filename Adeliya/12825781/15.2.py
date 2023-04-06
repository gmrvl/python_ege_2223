def Dell(n, m):
    if n % m == 0:
        return True
    else:
        return False

def F(x, A):
    return (Dell(90, A) and (not Dell(x, A)) <= (Dell(x, 15) <= (not Dell(x, 20))))


for A in range(1, 1000):
    OK = True
    for x in range(0, 1000):
        if not F(x, A):
            OK = False
            break
    if OK:
        print(A)


