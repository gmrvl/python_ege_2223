def f(x,y,A):
    return (x + 3*y > A) or (y < 30) or (x < 30)

for A in range(1,1000):
    ok = True
    for x in range(0,100):
        for y in range(0,100):
            if f(x,y,A) != 1:
                ok = False
    if ok:
        print(A)

