def ДЕЛ(n, m):
    if n % m == 0:
        return 1
    else:
        return 0

def f(x,A):
    return (ДЕЛ(x, 250) <= (not(ДЕЛ(x, 10)))) or (3*x + 2*A >= 1000)

for A in range(1,1000):
    ok = True
    for x in range(1,1000):
        if f(x,A) != 1:
            ok = False
            break
    if ok:
        print(A)