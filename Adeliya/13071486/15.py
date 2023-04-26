def f(x,y, A):
    return (x*y < 120) or (y > A) or (x > A)

for A in range(1,1000):
    ok=True
    for x in range(0,1000):
        for y in range(0,1000):
            if not f(x,y,A):
                ok=False
                break
    if ok:
        print(A)
