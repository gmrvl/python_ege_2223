def f(x, A):
    return (x & 85 == 0) <= ((x & 54 != 0) <= (x & A != 0))
for A in range(1000):
    ok=True
    for x in range(1000):
        if  f(x,A)==0:
            ok=False
            break
    if ok:
        print(A)
        break