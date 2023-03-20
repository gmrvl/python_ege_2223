def F(x, y, A):
    return (3*x + 4*y != 70) or (A > x) or (A > y)

for A in range(10000):
    ok = True
    for x in range(1000):
        for y in range(1000):
            if F(x, y, A) == 0:
                ok = False
                break
        if not ok:
            break
    if ok:
        print(A)
        break
        