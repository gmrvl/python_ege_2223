def F(x,A):
    return (x & 33 == 0) <= ((x & 45 != 0) <= (x & A != 0))

for A in range(100):
    ok = True
    for x in range(100):
        if F(x, A) != 1:
            ok = False
            break
    if ok:
        print(A)