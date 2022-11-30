def f(x, y, a):
    return (2*x + 3*y > 30) or (x + y <= a)

for a in range(1000):
    ok = True
    for x in range(1000):
        for y in range(1000):
            if f(x, y, a) != 1:
                ok = False
    if ok:
        print(a)