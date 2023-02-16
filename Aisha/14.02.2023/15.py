def F(x, A):
    return (x & 51 == 0) or ((x & 41 == 0) <= (x & A == 0))


for A in range(1000):
    s = True
    for x in range(1000):
        if F(x, A) == 0:
            s = False
            break
    if s:
        print(A)
        break
