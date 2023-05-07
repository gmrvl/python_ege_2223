def Dell(x, A):
    return x % A == 0


def F(x, A):
    return Dell(120, A) and ((not(Dell(x, A))) <= (Dell(x, 18) <= (not(Dell(x, 24)))))


for A in range(1, 1000):
    s = True
    for x in range(1, 1000):
        if F(x, A) == 0:
            s = False
            break
    if s:
        print(A)
