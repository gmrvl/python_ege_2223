def ДЕЛ(n, m):
    if n % m == 0:
        return 1
    else:
        return 0

for A in range(1,100):
    ok = True
    for x in range(1,100):
        if ((ДЕЛ(x, 7) <= (not(ДЕЛ(x, 21)))) or (2*x + A >= 120)) != 1:
            ok = False
            break
    if ok:
        print(A)