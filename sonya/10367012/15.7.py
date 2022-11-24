def F(x, A1, A2):
    return ((A1 <= x <= A2) <= (x**2 <= 100)) and ((x**2 <= 64) <= (A1 <= x <= A2))


for A in range(1000, 0, -1):
    A1 = -1 * A
    A2 = A
    ok = True
    for x in range(-1000, 1000):
        if F(x, A1, A2) != 1:
            ok = False
            break
    if ok:
        print(A*2)
        break

