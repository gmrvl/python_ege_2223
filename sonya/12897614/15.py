def f(x, A):
    return (x&41 != 0) <= ((x&33 == 0) <= (x&A != 0))

for A in range(100):
    ok = True
    for x in range(100):
        if f(x, A) != 1:
            ok = False
            break
    if ok:
        print(A)