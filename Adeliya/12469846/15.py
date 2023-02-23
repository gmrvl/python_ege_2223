def Dell(n, m):
    if n % m == 0:
        return True
    else:
        return False

def F(x, a):
    return Dell(120,a) and ((not Dell(x,a)) <= (Dell(x,18) <= (not (Dell(x,24)))))

for a in range(1, 1000):
    OK = True
    for x in range(1, 1000):
        if not F(x, a):
            OK = False
            break
    if OK:
        print(a)
