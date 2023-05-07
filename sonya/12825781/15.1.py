def f(x,A):
    return (x & 73 == 0) <= ((x & 28 != 0) <= (x & A != 0))

for A in range(100):
    ok = True
    for x in range(100):
        if f(x, A) == 0:
            ok = False
            break
    if ok:
        print(A)