def f(x, A):
    return (x&51 == 0) or ((x&41 == 0) <= (x&A == 0))

for A in range(0,100):
    ok = True
    for x in range(0,100):
        if f(x,A) == 0:
            ok = False
    if ok:
        print(A)