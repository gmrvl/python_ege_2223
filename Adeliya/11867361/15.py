# (2x + 3y > 30) ∨ (x + y ≤ A)
def f(x,y,a):
    return (2*x + 3*y > 30) or (x + y <= a)
for a in range(1,1000):
    ok=True
    for x in range(0,1000):
        for y in range(0,1000):
            if not f(x,y,a):
                ok=False
                break
    if ok:
        print(a)
        break



