def Del(m, n):
    return m % n == 0


def f(x, a):
    return ((Del(x, 3)) <= (not (Del(x, 5)))) or ((x + a) >= 70)


for a in range(1, 100):
    ok = True
    for x in range(1, 100):
        if not f(x, a):
            ok = False
            break
    if ok:
        print(a)
        break