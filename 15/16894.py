def F(x, y, A):
    return (2*x + 3*y != 60) or (A >= x) or (A >= y)


for A in range(1000):
    c = True
    for x in range(1000):
        for y in range(1000):
            if F(x, y, A) == 0:
                c = False
                break
        if not c:
            break
    if c:
        print(A)
        break
