for A in range(0, 1000):
    ok = True
    for x in range(0, 1000):
        if ((x & 17 == 0) <= ((x & 29 != 0) <= (x & A != 0))) != 1:
            ok = False
            break
    if ok:
        print(A)
        break
