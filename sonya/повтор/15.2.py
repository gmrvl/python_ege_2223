def f(x, y, A):
    return (x >= 12) or (3*x<y) or (x*y<A)

for A in range(0,1000):
    ok = True
    for x in range(0,100):
        for y in range(0,100):
            if f(x, y, A) == 0:
                ok = False
                break
    if ok:
        print(A)