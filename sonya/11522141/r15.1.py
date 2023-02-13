def f(x,A):
    return (x & 105 == 0) <= ((x & 58 != 0) <= (x & A != 0))

for A in range(100):
    ok = True
    for x in range(100):
        if f(x, A) == 0:
            ok = False
    if ok:
        print(A)