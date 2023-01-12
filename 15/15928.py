def F(x, y, A0, A1):
    return ((A0 <= x <= A1) <= (x**2 <= 81)) and ((y**2 <= 36) <= (A0 <= y <= A1))


for A in range(1000, 0, -1):
    A0 = -1 * A
    A1 = A
    OK = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if not F(x, y, A0, A1):
                OK = False
                break
        if not OK:
            break
    if OK:
        print(A*2)
        break
