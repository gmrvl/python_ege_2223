def f(x, y, A):
    return (x + 2*y < A) or (y > x) or (x > 20)

for A in range(0,100):
    ok = True
    for x in range(0,100):
        for y in range(0,100):
            if f(x,y,A) != 1:
                ok = False
    if ok:
        print(A)
        break