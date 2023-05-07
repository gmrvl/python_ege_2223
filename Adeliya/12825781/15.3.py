def F(x,a):
    return (x & 73 == 0) <= ((x & 28 != 0) <= (x & a != 0))

for a in range(1,1000):
    ok=True
    for x in range(0,1000):
        if not F(x,a):
            ok=False
            break
    if ok:
        print(a)
        break