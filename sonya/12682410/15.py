def f(x,y,A):
    return (2*x + 3*y < 30) or (x + y >= A)

for A in range(100):
    ok = True
    for x in range(100):
        for y in range(100):
            if f(x,y,A) != 1:
                ok = False
                break
    if ok:
        print(A)