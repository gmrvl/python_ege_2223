def F(x, y, A):
    return ((x < A) <= (x**2 < 100)) and ((y**2 <= 64) <= (y <= A))

a = []

for A in range(0, 100):
    ok = True
    for x in range(0,100):
        for y in range(0, 100):
            if F(x, y, A) != 1:
                ok = False
                break
    if ok:
        a.append(A)
print(len(a))
