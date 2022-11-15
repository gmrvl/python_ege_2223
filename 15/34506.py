def F(x, A):
    return (x & 25 != 0) <= ((x & 17 == 0) <= (x & A != 0))


for A in range(1000):
    OK = True
    for x in range(1000):
        if not F(x, A):
            OK = False
            break
    if OK:
        print(A)
        break
