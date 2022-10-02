def f(x,y,a):
    return ((x < 5) <= (x**2 < a)) and ((y**2 <= a) <= (y <= 5))
for a in range(1,1000):
    ok = True
    for x in range(0,1000):
        for y in range(0,1000):
            if not f(x,y,a):
                ok = False
                break
    if ok:
        print(a)

