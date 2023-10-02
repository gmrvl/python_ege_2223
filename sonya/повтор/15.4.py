def ТРЕУГ(n,m,k):
    if max(n,m,k) < (n+m+k - max(n,m,k)):
        return 1
    else:
        return 0
def МАКС(x, y):
    if x > y:
        return x
    else:
        return y
def f(x,A):
    return ((ТРЕУГ(x,10,20) <= (not(МАКС(x, 8) > 24))) == (not(ТРЕУГ(3,A, x))))

for A in range(0,1000):
    ok = True
    for x in range(0,100):
        if f(x, A) == 0:
            ok = False
            break
    if ok:
        print(A)
