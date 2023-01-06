def f(x,a):
    return (x&41 != 0) <= ((x&33 == 0) <= (x&a != 0))
for a in range(1,1000):
    ok=True
    for x in range(0,1000):
        if not f(x,a):
            ok=False
            break
    if ok:
        print(a)
        break
