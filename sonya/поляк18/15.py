def ДЕЛ(n, m):
    if n % m == 0:
        return 1
    else:
        return 0
def f(x,y):
    return (ДЕЛ(x, 175) <= (not(ДЕЛ(x, 25)))) or (2*x + A >= 1780)

for A in range(1,10000):
    ok = True
    for x in range(1,10000):
        if f(x, A) == 0:
            ok = False
            break
    if ok:
        print(A)