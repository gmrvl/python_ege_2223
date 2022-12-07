def ДЕЛ(n, m):
    if n % m == 0:
        return True
    else:
        return False

def F(x, A):
    return ДЕЛ(x, A) <= (not(ДЕЛ(x, 21)) + ДЕЛ(x, 35))


for A in range(1, 100):
    ok = True
    for x in range(1, 100):
        if F(x, A) != 1:
            ok = False
            break
    if ok:
        print(A)