def DELL(n, m):
    if n % m == 0:
        return 1
    else:
        return 0

def f(x, A):
    return DELL(120, A) and ((not(DELL(x, A))) <= (DELL(x, 18) <= (not(DELL(x, 24)))))

for A in range(1,1000):
    ok = True
    for x in range(1,1000):
        if f(x, A) == 0:
            ok = False
    if ok:
        print(A)