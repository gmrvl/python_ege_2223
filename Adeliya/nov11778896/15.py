# (x·y < 140) ∨ (y > A) ∨ (x > A)
def f(x,y,a):
    return (x * y < 140) or (y > a) or (x > a)
for a in range(1,1000):
    ok=True
    for x in range(0,1000):
        for y in range(0,1000):
            if not f(x,y,a):
                ok=False
                break
    if ok:
        print(a)
