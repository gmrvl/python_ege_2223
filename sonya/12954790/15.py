def f(x,A):
    return (x&25 != 0) <= ((x&9 == 0) <= (x&A != 0))

for A in range(100):
    ok = True
    for x in range(100):
        if f(x, A) != 1:
            ok = False
            break
    if ok:
        print(A)