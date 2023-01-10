def F(x,A):
    return (x & 25 != 0) <= ((x & 19 == 0) <= (x & A != 0))

for A in range(0, 1000):
    ok = True
    for x in range(0, 1000):
        if F(x, A) != 1:
            ok = False
            break
    if ok:
        print(A)
        break