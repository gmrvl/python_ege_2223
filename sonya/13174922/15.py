def f(x, A):
    return ((x&28 != 0) or (x&45 != 0)) <= ((x&17 == 0) <= (x&A != 0))

for A in range(0, 100):
    ok = True
    for x in range(0,100):
        if f(x, A) == 0:
            ok = False
            break
    if ok:
        print(A)