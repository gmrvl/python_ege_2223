def F(x, A1, A2):
    return ((A1 <= x <= A2) <= (x**2 <= 100)) and ((x**2 <= 64) <= (A1 <= x <= A2))


for i in range(1000, 0, -1):
    A1 = -1*i
    A2 = i
    c = True
    for x in range(1000):
        if F(x, A1, A2) == 0:
            c = False
            break
    if c:
        print(i * 2)
        break
