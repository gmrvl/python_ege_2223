def ДЕЛ(n, m):
    if n % m == 0:
        return 1
    else:
        return 0

for A in range(1,100):
    ok = True
    for x in range(1,100):
        if ((A < 50) and ((not(ДЕЛ(x, A))) <= (ДЕЛ(x, 10) <= (not(ДЕЛ(x, 18)))))) == 0:
            ok = False
            break
    if ok:
        print(A)