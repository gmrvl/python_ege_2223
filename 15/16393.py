def F(x, y, A):
    return (2*x + 3*y > 30) or (x + y <= A)


for A in range(0, 1000):
    s = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if F(x, y, A) == 0:
                s = False
                break
        if not s:
            break
    if s:
        print(A)
        break
