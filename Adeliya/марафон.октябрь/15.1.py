# (x + 2y < A) ∨ (y > x) ∨ (x > 20)
def f(x,y,a):
    return (x+ 2*y < a) or (y>x) or (x > 20)
for a in range(1,1000):
    ok=True
    for x in range(0,1000):
        for y in range(0,1000):
            if not f(x,y,a):
                ok = False
                break
    if ok:
        print(a)
        break


