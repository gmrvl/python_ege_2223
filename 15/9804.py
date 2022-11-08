def F(x, A):
    return ((x & 29 != 0) <= ((x & 17 == 0) <= (x & A != 0)))


for A in range(10000):
    c = True
    for x in range(10000):
        if F(x, A) == 0:
            c = False
            break
    if c:
        print(A)
        break
