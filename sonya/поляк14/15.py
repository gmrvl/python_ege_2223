def ДЕЛ(n, m):
    if n % m == 0:
        return 1
    else:
        return 0
def f(x, A):
    return  (ДЕЛ(x, 6) <= (not(ДЕЛ(x, 14)))) or (x + A >= 70) and ДЕЛ(A, 20)

for A in range(1,100):
    ok = True
    for x in range(1,100):
        if f(x, A) != 1:
            ok = False
            break
    if ok:
        print(A)