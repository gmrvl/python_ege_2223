def F(x, a):
    return (x & 51 == 0) or ((x & 41 == 0) <= (x & a == 0))


for a in range(0, 1000):
    ok = True
    for x in range(0, 1000):
        if F(x, a) == 0:
            ok = False
            break
    if ok:
        print(a)
