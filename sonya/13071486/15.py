def f(x,y,A):
    return (x*y < 120) or (y > A) or (x > A)

for A in range(100):
    ok = True
    for x in range(100):
        for y in range(100):
            if f(x,y,A) != 1:
                ok = False
                break
    if ok:
        print(A)