def ДЕЛ(n,m):
    if n  % m == 0:
        return 1
    else:
        return 0

def f(x, A):
    return (ДЕЛ(72,x) <= (not(ДЕЛ(90,x))))or (A-x>80)

for A in range(1,100):
    ok= True
    for x in range(1,100):
        if f(x, A) == 0:
            ok = False
            break
    if ok:
        print(A)