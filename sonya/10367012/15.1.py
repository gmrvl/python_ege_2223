def F(x, A):
    return ((x & 28 != 0) or (x & 45 != 0)) <= ((x & 17 == 0) <= (x & A != 0))

for A in range(1000):
    OK = True
    for x in range(1000):
        if F(x, A) != 1:
            OK = False
            break
    if OK:
        print(A)
