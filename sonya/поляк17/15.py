def f(x,y,A):
    return (7*y + 5*x < 1000) or (x < y) or (A < x)

for A in range(0,100):
    ok = True
    for x in range(0, 100):
        for y in range(0,100):
            if f(x,y,A) == 0:
                ok = False
                break
    if ok:
        print(A)