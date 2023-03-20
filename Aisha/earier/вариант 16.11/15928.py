def F(x, y, A, mA):
    return ((mA <= x <= A) <= (x**2 <= 81)) and ((y**2 <= 36) <= (mA <= y <= A))


for i in range(1000, 0, -1):
    mA = -1*i
    A = i
    ok = True
    for x in range(-100, 100):
        for y in range(-100, 100):
            if F(x, y, A, mA) == 0:
                ok = False
                break
        if not ok:
            break
    if ok:
        print(2*A)
        break
