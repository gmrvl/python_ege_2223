def f(x, A):
    return (x&39 == 0) or ((x&11 == 0) <= (x&A != 0))


for A in range(0,100):
    ok = True
    for x in range(0,100):
        if f(x,A) != 1:
            ok = False
            break
    if ok:
        print(A)