# ДЕЛ(x, А) → (ДЕЛ(x, 21) + ДЕЛ(x, 35)) наименьшее
def Del(x,y):
    return x%y==0
def f(x,a):
    return Del(x,a) <= (Del(x,21)+Del(x,35))
for a in range(1,100):
    ok=True
    for x in range(0,100):
        if not f(x,a):
            ok=False
            break
    if ok:
        print(a)

